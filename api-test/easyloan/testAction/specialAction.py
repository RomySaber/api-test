#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Author     : QA
@File       : specialAction.py
@desc       : 项目：easyloan 模块：yygl 接口方法封装
"""

from easyloan.testAction import loginAction
import requests, json
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent as ms
from common.myConfig import MysqlConfig


baseUrl = MysqlConfig.get('yygl_apiURL', 'easyloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
shebei={"network":"Wifi","channel":"AppStore","appVersion":"1.0.6","app":"1","netIp":"","system":"iOS","uuid":"FDC0F87C54716435DAC3E49F04F8AC9B","phoneName":"iPhone","phoneVersion":"iPhone+6s+Plus"}
new_shebei=json.dumps(shebei)
API_TEST_HEADERS1 = {"Content-Type": "application/json", "Cache-Control": "no-cache","clientMess":new_shebei}
LICENCES = loginAction.test_yygl_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_clientapp_login_register(verificationcode, mobile, password, invitemobile):
    """
    注册
    :param verificationcode: 验证码（Y）,number
    :param mobile: 账号（Y）,string
    :param password: 密码（Y）,string
    :param invitemobile: 邀请人手机号（N）,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 685')
    requesturl = baseUrl + "/api/78dk/clientapp/login/register"
    LOGGER.info("注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["verificationCode"] = verificationcode
    params["mobile"] = mobile
    params["password"] = password
    params["inviteMobile"] = invitemobile
    LOGGER.info("注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS1)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text
