#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : ApplicationserverAction.py
@desc       : 项目：finance 模块：applicationserver 接口方法封装
"""

from finance.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('applicationserver_apiURL', 'finance')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_applicationserver_login()


def test_api_accredit(appkey, valid):
    """
    获取用户授权
    :param appkey: 某请求参数,string
    :param valid: 有效时间，单位分钟，不能大于120，默认30,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 146')
    requesturl = baseUrl + "/api/accredit"
    LOGGER.info("获取用户授权请求地址:【{}】".format(requesturl))
    params = dict()
    params["appKey"] = appkey
    params["valid"] = valid
    LOGGER.info("获取用户授权请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户授权请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


