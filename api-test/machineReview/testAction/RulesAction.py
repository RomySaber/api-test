#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-09 上午 11:47
@Author     : 罗林
@File       : RulesAction.py
@desc       : 
"""

import json
import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog

baseUrl = ''
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def testrules(orderId, userId, ruleKey, ruleParams, testParams, ruleState, code, msg):
    requesturl = baseUrl + ""
    LOGGER.info("机审规则测试地址:【{}】".format(requesturl))
    params = {"orderId": orderId, "userId": userId, "ruleKey": ruleKey, "page": ruleParams, "testParams": testParams,
              "other": ''}
    LOGGER.info("机审结果表数据请求参数：【{}】".format(params))
    response = requests.request('POST', requesturl, params=params, headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    Assertion.verity(json.loads(response)["orderId"], orderId)
    Assertion.verity(json.loads(response)["userId"], userId)
    Assertion.verity(json.loads(response)["ruleKey"], ruleKey)
    # 10001：规则代码有误, 10000 正常, code: 10002 取不到数据
    Assertion.verity(json.loads(response)["code"], code)  
    Assertion.verity(json.loads(response)["msg"], msg)
    Assertion.verity(json.loads(response)["ruleState"], ruleState)
    
    
