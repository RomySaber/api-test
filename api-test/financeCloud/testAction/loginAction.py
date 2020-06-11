#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-05-22
@Author     : QA
@File       : loginAction.py
@desc       : 
"""

import json
import requests
import time

from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils
from common.myConfig import MysqlConfig

TIMEOUT = ConfigUtils.getint('report', 'time_out')
web_apiURL = MysqlConfig.get('web_apiURL', 'financeCloud')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
webUser = ''
webPasswd = ''


def test_web_login():
    """
    用户退出登录
    :return: response.text
    """
    start_time = time.time()
    requesturl = web_apiURL + "/user/login"
    LOGGER.info("用户登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = webUser
    params["userName"] = webPasswd
    LOGGER.info("用户登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_app_login():
    pass
