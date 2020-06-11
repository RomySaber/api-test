#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : CrawleroperatorAction.py
@desc       : 项目：ai 模块：crawlerOperator 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('crawlerOperator_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_mobile_phone_config(phone, reqid, token):
    """
    1、获取运营商授权初始化配置接口
    :param reqid: 会话id(非必填),string
    :param token: 分配的token参数（必填）,string
    :param phone: 11位手机号（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1008')
    requesturl = baseUrl + "/api/mobile/phone_config"
    LOGGER.info("1、获取运营商授权初始化配置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、获取运营商授权初始化配置接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、获取运营商授权初始化配置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_sms_code(reqid, token):
    """
    2、刷新运营商登录的短信验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1009')
    requesturl = baseUrl + "/api/mobile/refresh_sms_code"
    LOGGER.info("2、刷新运营商登录的短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、刷新运营商登录的短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、刷新运营商登录的短信验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_verify_code(reqid, token):
    """
    3、刷新运营商登录的图片验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1010')
    requesturl = baseUrl + "/api/mobile/refresh_verify_code"
    LOGGER.info("3、刷新运营商登录的图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、刷新运营商登录的图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、刷新运营商登录的图片验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_login_submit(code, name, password, randompassword, reqid, token):
    """
    6、账号密码登录提交接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :param name: 用户名（必填）,string
    :param password: 密码（必填）,string
    :param code: 图片验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :param randompassword: 随机验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1011')
    requesturl = baseUrl + "/api/mobile/login_submit"
    LOGGER.info("6、账号密码登录提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("6、账号密码登录提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、账号密码登录提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_verify_pic(reqid, token):
    """
    4、获取二次图片验证
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1012')
    requesturl = baseUrl + "/api/mobile/refresh_verify_pic"
    LOGGER.info("4、获取二次图片验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("4、获取二次图片验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、获取二次图片验证请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_smscode(reqid, token):
    """
    5、获取二次短信验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1013')
    requesturl = baseUrl + "/api/mobile/refresh_smscode"
    LOGGER.info("5、获取二次短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("5、获取二次短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、获取二次短信验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_code_submit(code, reqid, token):
    """
    8、二次验证码提交接口
    :param code: 验证码（必填,string
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1014')
    requesturl = baseUrl + "/api/mobile/code_submit"
    LOGGER.info("8、二次验证码提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("8、二次验证码提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("8、二次验证码提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_get_status(reqid, token):
    """
    7、获取运营商任务当前状态接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1015')
    requesturl = baseUrl + "/api/mobile/get_status"
    LOGGER.info("7、获取运营商任务当前状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("7、获取运营商任务当前状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("7、获取运营商任务当前状态接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_get_result(reqid, token):
    """
    9、获取运营商采集数据接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1016')
    requesturl = baseUrl + "/api/mobile/get_result"
    LOGGER.info("9、获取运营商采集数据接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("9、获取运营商采集数据接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("9、获取运营商采集数据接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


