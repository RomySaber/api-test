#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : BankabcAction.py
@desc       : 项目：ai 模块：BankABC 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('BankABC_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_bankabc_login(name, password, reqid, token):
    """
    1.账号密码登录
    :param name: 账户名,string
    :param password: 密码,string
    :param reqid: 会话id（url参数）,string
    :param token: 分配的token（url参数）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1169')
    requesturl = baseUrl + "/api/bankabc/login"
    LOGGER.info("1.账号密码登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1.账号密码登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.账号密码登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankabc_get_sms(reqid, token):
    """
    2.获取短信验证码
    :param reqid: 会话id（url参数）,string
    :param token: 分配的token（url参数）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1170')
    requesturl = baseUrl + "/api/bankabc/get_sms"
    LOGGER.info("2.获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2.获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2.获取短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankabc_verify_sms(code, reqid, token):
    """
    3.验证短信验证码
    :param code: 短信验证码,string
    :param reqid: url参数,string
    :param token: url参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1171')
    requesturl = baseUrl + "/api/bankabc/verify_sms"
    LOGGER.info("3.验证短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3.验证短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3.验证短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankabc_get_status(reqid, token):
    """
    4.获取任务状态接口
    :param reqid: ,string
    :param token: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1172')
    requesturl = baseUrl + "/api/bankabc/get_status"
    LOGGER.info("4.获取任务状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("4.获取任务状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4.获取任务状态接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankabc_get_result(reqid, token):
    """
    5.获取数据接口
    :param reqid: ,string
    :param token: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1173')
    requesturl = baseUrl + "/api/bankabc/get_result"
    LOGGER.info("5.获取数据接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("5.获取数据接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5.获取数据接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankabc_qrlogin(reqid, token):
    """
    6.二维码登录接口
    :param reqid: 会话id,string
    :param token: 校验token,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1197')
    requesturl = baseUrl + "/api/bankabc/qrlogin"
    LOGGER.info("6.二维码登录接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("6.二维码登录接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6.二维码登录接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


