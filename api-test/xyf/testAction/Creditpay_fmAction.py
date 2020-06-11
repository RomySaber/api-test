#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_fmAction.py
@desc       : 项目：xyf 模块：creditpay_fm 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_fm_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_fm_login()


def test_fm_getUserRepaymentPage():
    """
    用户还款数据列表(v1.0.0修改)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2634')
    requesturl = baseUrl + "/fm/getUserRepaymentPage"
    LOGGER.info("用户还款数据列表(v1.0.0修改)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户还款数据列表(v1.0.0修改)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户还款数据列表(v1.0.0修改)请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


