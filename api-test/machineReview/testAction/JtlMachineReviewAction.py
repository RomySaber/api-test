#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : JtlmachinereviewAction.py
@desc       : 项目：machineReview 模块：jtlMachineReview 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('jtlMachineReview_apiURL', 'machineReview')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_risk_system(params):
    """
    金螳螂家装分期机审接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 86')
    requesturl = baseUrl + "/risk_system"
    LOGGER.info("金螳螂家装分期机审接口请求地址:【{}】".format(requesturl))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_system_earnest(params):
    """
    金螳螂订金分期机审接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 87')
    requesturl = baseUrl + "/risk_system_earnest"
    LOGGER.info("金螳螂订金分期机审接口请求地址:【{}】".format(requesturl))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


