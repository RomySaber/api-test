#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : MobilecrawlerAction.py
@desc       : 项目：ai 模块：MobileCrawler 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('MobileCrawler_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_mobile_phone_config(phone, reqid, token):
    """
    1、获取运营商授权初始化配置接口
    :param reqid: 会话id(非必填),string
    :param phone: 11位手机号（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1040')
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
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id(必填),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1041')
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


def test_api_mobile_login_submit(code, name, password, randompassword, reqid, token):
    """
    3、账号密码登录提交接口
    :param password: 密码（必填）,string
    :param token: 分配的token参数（必填）,string
    :param code: 图片验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :param name: 用户名（必填）,string
    :param reqid: 会话id(必填),string
    :param randompassword: 随机验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1042')
    requesturl = baseUrl + "/api/mobile/login_submit"
    LOGGER.info("3、账号密码登录提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、账号密码登录提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、账号密码登录提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_smscode(reqid, token):
    """
    2.获取二次短信验证码接口
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id(必填),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1043')
    requesturl = baseUrl + "/api/mobile/refresh_smscode"
    LOGGER.info("2.获取二次短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2.获取二次短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2.获取二次短信验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_code_submit(code, reqid, token):
    """
    2、二次验证码提交接口
    :param code: 验证码（必填,string
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1044')
    requesturl = baseUrl + "/api/mobile/code_submit"
    LOGGER.info("2、二次验证码提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、二次验证码提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、二次验证码提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_get_status(reqid, token):
    """
    1、获取运营商任务当前状态接口
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id(必填),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1045')
    requesturl = baseUrl + "/api/mobile/get_status"
    LOGGER.info("1、获取运营商任务当前状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、获取运营商任务当前状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、获取运营商任务当前状态接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_refresh_verify_pic(reqid, token):
    """
    1.获取二次图片验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1046')
    requesturl = baseUrl + "/api/mobile/refresh_verify_pic"
    LOGGER.info("1.获取二次图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1.获取二次图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.获取二次图片验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_get_result(reqid, token):
    """
    5.获取运营商采集数据接口（信用付中此接口不需要主动调用）
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1047')
    requesturl = baseUrl + "/api/mobile/get_result"
    LOGGER.info("5.获取运营商采集数据接口（信用付中此接口不需要主动调用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("5.获取运营商采集数据接口（信用付中此接口不需要主动调用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5.获取运营商采集数据接口（信用付中此接口不需要主动调用）请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_pic_code_submit(code, reqid, token):
    """
    3.验证二次图片验证码
    :param code: 图片验证码（必填）,string
    :param reqid: 必填,string
    :param token: 必填,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1798')
    requesturl = baseUrl + "/api/mobile/pic_code_submit"
    LOGGER.info("3.验证二次图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3.验证二次图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3.验证二次图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_mobile_msg_code_submit(code, reqid, token):
    """
    4.验证二次短信验证码
    :param code: 短信验证码（必填）,string
    :param reqid: 必填,string
    :param token: 必填,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1799')
    requesturl = baseUrl + "/api/mobile/msg_code_submit"
    LOGGER.info("4.验证二次短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("4.验证二次短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4.验证二次短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


