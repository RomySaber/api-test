#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : ViolationAction.py
@desc       : 项目：ai 模块：Violation 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('Violation_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_wz_query(carno, ein, token, vin):
    """
    获取违章信息
    :param carno: 车牌号（必填）,string
    :param ein: 发动机号后六位（必填）,string
    :param token: 分配的token参数（必填）,string
    :param vin: 车架号后六位（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1017')
    requesturl = baseUrl + "/api/wz/query"
    LOGGER.info("获取违章信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["carno"] = carno
    params["ein"] = ein
    params["token"] = token
    params["vin"] = vin
    LOGGER.info("获取违章信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取违章信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


