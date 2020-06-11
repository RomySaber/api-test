#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-03-16
@Author     : QA
@File       : loginAction.py
@desc       : 
"""
import json
import requests
from common.myCommon.Logger import getlog
from common.myConfig import MysqlConfig

LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json"}
web_baseUrl = MysqlConfig.get('web_apiURL', 'xyf')
email = "yanhong@78dk.com"
passwd = "123"
rq = requests.Session()

def test_nca_login():
    pass


def test_creditpay_cm_login():
    pass


def test_creditpay_fm_login():
    pass


def test_creditpay_mm_login():
    pass


def test_creditpay_nca_login():
    pass


def test_creditpay_om_login():
    pass


def test_creditpay_sm_login():
    pass


def cest_creditpay_ur_login():
    """
    web端登录
    :return:
    """
    requesturl = web_baseUrl + "/api/v3.1.0/am/auth/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = {"email": email, "password": passwd}
    LOGGER.info("用户登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    return response.json()['data']['MyToken']

    # print(response.json()['data']['MyToken'])


def test_app_login():
    pass