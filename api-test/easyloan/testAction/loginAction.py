#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-23 下午 2:33
@Author     : 罗林
@File       : loginAction.py
@desc       : 
"""


import requests
import json
from common.myConfig import ConfigUtils as conf
from common.myCommon.Logger import getlog
from common.myConfig import MysqlConfig as ms
from common.mydb import MysqlClent

User = 'fqhd001'
Passwd = '5e81f67ed14a5443ec6a3682513f0b9b'
mobile = '13699479886'
app_passwd = 'll123456'
DB = MysqlClent.get_conn('192.168.15.159', 3306, 'easyloan', 'easyloan', '78dk.com')
web_URL = ms.get('easyloan_web_apiURL')
app_URL = ms.get('easyloan_app_apiURL')
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json"}
rq = requests.Session()
sign = conf.get('report', 'sign')


def test_easyloan_web_login():
    url = web_URL + '/api/78dk/web/login'
    querystring = json.dumps({"username": User, "password": Passwd})
    response = rq.post(url, headers=API_TEST_HEADERS, data=querystring)
    LOGGER.info("token:【{}】".format(response.json()["data"]["token"]))
    return response.json()["data"]["token"]


def test_easyloan_app_login():
    url = app_URL + '/api/78dk/clientapp/login/pwLogin'
    querystring = json.dumps({"mobile": mobile, "password": app_passwd})
    response = rq.post(url, headers=API_TEST_HEADERS, data=querystring)
    LOGGER.info("token:【{}】".format(response.json()["data"]["token"]))
    LOGGER.info(response.text)
    return response.json()["data"]["token"]


def test_yygl_login():
    pass

if __name__ == '__main__':
    test_easyloan_app_login()
