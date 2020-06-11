#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-03-20 下午 3:10
@Author     : 罗林
@File       : loginAction.py
@desc       : 
"""
import hashlib
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
from common.mydb.MyRedis import MyRedis

LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json"}
DB = ms.get_conn('192.168.15.161', 3306, 'xqkji78dkv23', 'i78dk', 'i78dk.com')
redisDB = MyRedis('192.168.15.161', 6388, 5, '123456')
baseUrl = MysqlConfig.get('xqkj_web_finance_consumption_apiURL', 'xqkj')
app_baseUrl = MysqlConfig.get('xqkj_app_finance_consumption_apiURL', 'xqkj')
pms_apiURL = MysqlConfig.get('pms_apiURL', 'xqkj')
sht_apiURL = MysqlConfig.get('sht_apiURL', 'xqkj')
global_dict = GlobalDict(os.path.dirname(__file__), 'xqkj_data')
super_email = "999@78dk.com"
super_passwd = "1"

app_phone = "13699479886"
app_passwd = "a123456"
# APP版本号
appversion = '1.1.0'
# 验证码
vercode = '123465'

pms_email = 'tongchao@78dk.com'
pms_passwd = '123456'
# 微信号 名称
wx_open_id = 'oiAz-4_RXd_h04m-G_xfSZRyxOLg'
wxUserUuid = 'df42b7b6c6a747d5bfc7dfaff5ed2c6f'
wx_name = 'luo332734508'
wx_isMaster = 'is_master_no'


rq = requests.Session()
sign = conf.get('report', 'sign')


def test_xqkj_web_finance_consumption_login():
    """
    web端登录，获取token
    :return:
    """
    # get_web_user()
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    params = {"email": super_email, "password": super_passwd}
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    r = rq.post(url, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(r.text))
    return r.json()['data']['token']


def test_xqkj_app_finance_consumption_login():
    """
    APP端登录，获取token
    :return:
    """
    requesturl = app_baseUrl + "/api/78dk/app/login/pwLogin"
    print(requesturl)
    params = {"mobile": app_phone, "password": app_passwd, "jgPushId": get_jgPushId()}
    API_TEST_HEADERS['tenantUuid'] = 'xqkj001'
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    return response.json()['data']['token']


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


def test_pms_login():
    """
    pms端登录， 获取token
    :return:
    """
    requesturl = pms_apiURL + "/login"
    LOGGER.info("登陆请求请求地址:【{}】".format(requesturl))
    params = {"password": pms_passwd, "email": pms_email}
    LOGGER.info("登陆请求请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆请求请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    return response.json()['data']['token']


def test_sht_login():
    """
    商户通 获取 token
    :return:
    """
    redis_keys = redisDB.get_keys()
    for redis_key in redis_keys:
        if wx_name in redisDB.redis_get(redis_key):
            redisDB.del_name(redis_key)
    uuid_str = str(uuid.uuid4()).replace("-", "")
    wx_name_prefix = 'wxuser_' + wx_open_id
    wx_token = hashlib.md5((wx_name_prefix + uuid_str).encode("utf-8")).hexdigest()
    wx_user_name = wx_name_prefix + wx_token
    wx_phone = 'https://wx.qlogo.cn/mmopen/vi_32' \
               '/Q0j4TwGTfTJInkWfFr8ftFB8TYjb78xiamRc9bqRDkJKZHliaeHLdldQjeGdtqIzl659XHEcBxicBeRHQq5wBOvpw/132'
    c_time = TimeFormat.getnow()
    state = 'enabled'
    created = TimeFormat.string_toTimestamp_13(c_time)
    rows = ms.select_rows(DB, 'Tbl_WX_User', 'id', 'name="{}" AND state="enabled"'.format(wx_name))
    if rows == 0:
        insert_dict = {"wx_user_uuid": wxUserUuid, "merchant_uuid": "", "name": wx_name, "phone": wx_phone,
                       "open_id": wx_open_id, "is_master": wx_isMaster, "created": c_time, "updated": c_time,
                       "state": state}
        ms.insert(DB, 'Tbl_WX_User', insert_dict)
    m_id = ms.select_one(DB, 'Tbl_WX_User', 'id', 'name="{}" AND state="enabled"'.format(wx_name))
    wx_user_info = {'created': created, 'id': m_id, 'isMaster': wx_isMaster, 'merchantUuid': '', 'name': wx_name,
                    'openId': wx_open_id, 'phone': wx_phone, 'state': state, 'token': wx_token, 'updated': created,
                    'wxUserUuid': wxUserUuid}
    redisDB.redis_set(wx_user_name, json.dumps(json.dumps(wx_user_info)))
    return wx_token


if __name__ == '__main__':
    print(test_sht_login())
    print(test_pms_login())
    print(get_user_uuid())
    print(test_xqkj_app_finance_consumption_login())
    print(test_xqkj_web_finance_consumption_login())
