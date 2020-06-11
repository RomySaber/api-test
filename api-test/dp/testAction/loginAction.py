#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-06 下午 6:11
@Author     : 罗林
@File       : loginAction.py
@desc       : 
"""
import json

import requests

from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils as conf
from common.myConfig import MysqlConfig
from common.myFile import FileUtils
from common.mydb import MysqlClent

dp_web_URL = MysqlConfig.get('dp_web_apiURL', 'dp')
dp_app_URL = MysqlConfig.get('dp_app_apiURL', 'dp')
db_info = {"dbhost": "192.168.15.236", "dbport": 3308, "dbname": "car_screen", "dbuser": "root", "dbpasswd": "78dk.com"}
DB = MysqlClent.get_conn(**db_info)
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
rq = requests.Session()
sign = conf.get('report', 'sign')

username = 'admin'
userpassword = 'daping123'
app_username = 'luolin'
app_userpassword = '123456'


def test_dp_web_login():
    """
    web端登录
    :return:
    """
    requesturl = dp_web_URL + "/login"
    LOGGER.info("登陆请求地址:【{}】".format(requesturl))
    params = {"userName": username, "userPassword": userpassword}
    LOGGER.info("登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.json()['data']['token']


def test_dp_app_login():
    """
    手机登陆接口
    :return: response.text
    """
    tvid = FileUtils.get_mac_address()
    requesturl = dp_app_URL + "/login"
    params = {"tvId": tvid, "userName": app_username, "userPassword": app_userpassword}
    rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    requesturl = dp_app_URL + "/login/getLoginState"
    params = {"tvid": tvid}
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    return response.json()['data']['token']


def get_web_user_info():
    """
    获取web端登录用户信息
    :return:
    """
    requesturl = dp_web_URL + "/login"
    params = {"userName": username, "userPassword": userpassword}
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    return response.json()['data']['id']


if __name__ == '__main__':
    print(test_dp_app_login())
    # print(test_screen_web_login())
    # print(get_web_user_info())
