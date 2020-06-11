#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : LocaleapiAction.py
@desc       : 项目：ai 模块：localeApi 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('localeApi_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_operator(phone_num):
    """
    请求与相应参数
    :param phone_num: 待识别的电话号码,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1039')
    requesturl = baseUrl + "/operator"
    LOGGER.info("请求与相应参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_num"] = phone_num
    LOGGER.info("请求与相应参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求与相应参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_operator_recognize(phone_num):
    """
    请求与相应参数
    :param phone_num: 待识别的手机号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3184')
    requesturl = baseUrl + "/operator_recognize"
    LOGGER.info("请求与相应参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_num"] = phone_num
    LOGGER.info("请求与相应参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求与相应参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


