#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_urAction.py
@desc       : 项目：xyf 模块：creditpay_ur 接口方法封装
"""


import requests, json, time
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from xyf.testAction import Creditpay_urAction

TIMEOUT = Creditpay_urAction.TIMEOUT
baseUrl = Creditpay_urAction.baseUrl
LOGGER = getlog(__name__)
rq = requests.Session()

API_TEST_HEADERS=Creditpay_urAction.API_TEST_HEADERS

def test_ui_user_getUserInfo(userid):
    """
    用户信息
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2633')
    requesturl = baseUrl + "/ui/user/getUserInfo"
    LOGGER.info("用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户信息请求参数：【{}】".format(params))
    # response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


