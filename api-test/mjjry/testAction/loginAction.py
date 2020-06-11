#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-11-21
@Author     : QA
@File       : loginAction.py
@desc       : 
"""
import json
import os
import requests
import uuid
from common.myCommon import TimeFormat
from common.myCommon.GlobalDict import GlobalDict
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils as conf
from common.myConfig import MysqlConfig
from common.mydb import MysqlClent as ms


LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json"}
DB = ms.get_conn('192.168.15.161', 3316, 'Finance_meijia', 'meijia', 'meijia.com')
web_baseUrl = MysqlConfig.get('web_apiURL', 'mjjry')
app_baseUrl = MysqlConfig.get('app_apiURL', 'mjjry')
json_file = 'mjjry_data'
global_dict = GlobalDict(os.path.dirname(__file__), json_file)
super_email = "luolin@78dk.com"
super_passwd = "123456"
app_phone = "13612345678"
app_passwd = "123456"
rq = requests.Session()
sign = conf.get('report', 'sign')
idcard = '511325201911281234'
user_name = "QA-API"


def test_web_login():
    return web_login()


def get_jgPushId():
    # 手机号 + 毫秒级时间戳（13位）
    jgPushId = "{0}{1}".format(app_phone, TimeFormat.get_now_time_13())
    return jgPushId


def get_user_uuid():
    """
    获取APP端用户的 UUID
    :return:
    """
    return ms.select_one(DB, 'Tbl_UserProfile', 'user_uuid', 'mobile="{}"'.format(app_phone))


def add_platform_user():
    """
    添加web端用户信息
    :return:
    """
    user_num = ms.select_rows(DB, 'Tbl_PlatformUserProfile', condition='email="{}"'.format(super_email))
    if not user_num:
        uuid_no = str(uuid.uuid1()).replace('-', '')
        insert_dict = {"platform_user_profile_uuid": uuid_no, "name": user_name, "mobile": app_phone,
                       "password": '5e769b5d4da956294c02e0d685f3d289', "salt": '12508731b78f4b20',
                       "email": super_email, "reset_password": 'reset_password_no',
                       "user_state": 'user_state_enabled', "create_user_uuid": 'adminUUID',
                       "created": '2019-12-11 10:50:37', "updated": '2019-12-11 10:51:17', "state": 'enabled'}
        ms.insert(DB, 'Tbl_PlatformUserProfile', insert_dict)
        privileges = ms.select_col(DB, 'Tbl_PlatformPrivilege', 'platform_privilege_uuid')
        privilege_values = [[uuid_no, p, '2019-12-11 10:51:00', '2019-12-11 10:51:00', 'enabled']
                            for p in privileges]
        privilege_col = ['platform_user_uuid', 'platform_privilege_uuid', 'created', 'updated', 'state']
        ms.insert_many(DB, 'Tbl_PlatformUserPrivilegeRelation', privilege_col, privilege_values)


def add_user():
    """
    添加APP端用户信息
    :return:
    """
    user_num = ms.select_rows(DB, 'Tbl_UserProfile', condition='mobile="{}"'.format(app_phone))
    if not user_num:
        uuid_no = str(uuid.uuid1()).replace('-', '')
        uuid_no2 = str(uuid.uuid1()).replace('-', '')
        insert_dict = {"user_uuid": uuid_no2, "name": user_name, "idcard_number": idcard, "mobile": app_phone,
                       "password": "a743ab4f6a8d03018f59c15296538d9b", "salt": "0HQ",
                       "authentication_state": "authentication_state_pass", "created": "2019-12-06 14:02:54",
                       "updated": "2019-12-06 14:47:26", "state": "enabled"}
        ms.insert(DB, 'Tbl_UserProfile', insert_dict)


def test_app_login():
    return app_login()


def app_login():
    """
    登录(密码)
    """
    add_user()
    requesturl = app_baseUrl + "/api/78dk/app/login/pwLogin"
    LOGGER.info("登录(密码)请求地址:【{}】".format(requesturl))
    params = {"mobile": app_phone, "password": app_passwd, "jgPushId": get_jgPushId()}
    API_TEST_HEADERS['tenantUuid'] = 'xqkj001'
    LOGGER.info("登录(密码)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录(密码)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    return response.json()['data']['token']


def web_login():
    """
    web端登录
    :return:
    """
    add_platform_user()
    requesturl = web_baseUrl + "/api/78dk/platform/sys/user/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = {"email": super_email, "password": super_passwd}
    LOGGER.info("用户登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    return response.json()['data']['token']
