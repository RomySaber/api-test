#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AiapiAction.py
@desc       : 项目：ai 模块：aiapi 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('aiapi_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_risk_strategy(data, scene_id, version):
    """
    1请求与响应参数
    :param version: 版本信息数据,object
    :param data: 请求数据,object
    :param scene_id: 场景ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1337')
    requesturl = baseUrl + "/risk_strategy"
    LOGGER.info("1请求与响应参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["data"] = data
    params["scene_id"] = scene_id
    params["version"] = version
    LOGGER.info("1请求与响应参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1请求与响应参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


