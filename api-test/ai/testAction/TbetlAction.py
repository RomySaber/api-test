#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : TbetlAction.py
@desc       : 项目：ai 模块：tbETL 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('tbETL_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_etl_taobao(reqid):
    """
    淘宝ETL
    :param reqid: 会话Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1691')
    requesturl = baseUrl + "/api/etl_taobao"
    LOGGER.info("淘宝ETL请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝ETL请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


