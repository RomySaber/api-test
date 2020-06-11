#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : DishonestexecutorAction.py
@desc       : 项目：ai 模块：DishonestExecutor 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('DishonestExecutor_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_execute_searchnocap(cardnum, name, token):
    """
    获取失信人数据
    :param cardnum: 证件号码(必填),string
    :param name: 姓名,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1271')
    requesturl = baseUrl + "/api/execute/searchnocap"
    LOGGER.info("获取失信人数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardnum"] = cardnum
    params["name"] = name
    params["token"] = token
    LOGGER.info("获取失信人数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取失信人数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_court_searchnocap(cardnum, name, token):
    """
    获取被执行人数据
    :param cardnum: 证件号码（必填）,string
    :param name: 姓名,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1272')
    requesturl = baseUrl + "/api/court/searchnocap"
    LOGGER.info("获取被执行人数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardnum"] = cardnum
    params["name"] = name
    params["token"] = token
    LOGGER.info("获取被执行人数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取被执行人数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


