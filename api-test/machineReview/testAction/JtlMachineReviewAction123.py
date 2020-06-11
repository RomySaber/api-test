#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog


baseUrl = 'http://192.168.15.129:8002'
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Cache-Control": "no-cache"}


def test_risk_system(params):
    """
    金螳螂家装分期机审接口
    :return:
    """
    requesturl = baseUrl + "/risk_system"
    LOGGER.info("登录接口请求地址:【{}】".format(requesturl))
    LOGGER.info("登录接口请求参数：【{}】".format(params))
    response = requests.request('POST', requesturl, data=params, headers=API_TEST_HEADERS)
    # response = requests.request('POST', requesturl, data=params, headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_risk_system_earnest(params):
    """
    金螳螂订金分期机审接口
    :return:
    """
    requesturl = baseUrl + "/risk_system_earnest"
    LOGGER.info("登录接口请求地址:【{}】".format(requesturl))
    LOGGER.info("登录接口请求参数：【{}】".format(params))
    response = requests.request('POST', requesturl, data=params, headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text
