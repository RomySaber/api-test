#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : TelecomcrawlerAction.py
@desc       : 项目：ai 模块：TelecomCrawler 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('TelecomCrawler_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_telecom_login_submit(name, password, reqid, token):
    """
    1、账号密码登录提交接口
    :param password: 密码（必填）,string
    :param reqid: 会话id(非必填),string
    :param token: 分配的token参数（必填）,string
    :param name: 用户名（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1056')
    requesturl = baseUrl + "/api/telecom/login_submit"
    LOGGER.info("1、账号密码登录提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、账号密码登录提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、账号密码登录提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_telecom_refresh_sms_code(name, reqid, token, tu):
    """
    1、获取二次短信验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :param name: 手机号（必填）,string
    :param tu: 图形验证码（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1057')
    requesturl = baseUrl + "/api/telecom/refresh_sms_code"
    LOGGER.info("1、获取二次短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["reqId"] = reqid
    params["token"] = token
    params["tu"] = tu
    LOGGER.info("1、获取二次短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、获取二次短信验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_telecom_code_submit(code, idcard, name, password, reqid, sfzname, token, tu):
    """
    2、二次验证码提交接口
    :param code: 验证码（必填）,string
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :param sfzname: 姓名（必填）,string
    :param idcard: 身份证号（必填）,string
    :param password: 服务密码（必填）,string
    :param name: 手机号（必填）,string
    :param tu: 图形验证码（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1058')
    requesturl = baseUrl + "/api/telecom/code_submit"
    LOGGER.info("2、二次验证码提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["idcard"] = idcard
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["sfzname"] = sfzname
    params["token"] = token
    params["tu"] = tu
    LOGGER.info("2、二次验证码提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、二次验证码提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_telecom_get_status(reqid, token):
    """
    3、获取运营商任务当前状态接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1059')
    requesturl = baseUrl + "/api/telecom/get_status"
    LOGGER.info("3、获取运营商任务当前状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、获取运营商任务当前状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、获取运营商任务当前状态接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_telecom_get_result(name, reqid, token):
    """
    3、获取运营商采集数据接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :param name: 手机号（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1060')
    requesturl = baseUrl + "/api/telecom/get_result"
    LOGGER.info("3、获取运营商采集数据接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、获取运营商采集数据接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、获取运营商采集数据接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_unicom_get_result(name, reqid, token):
    """
    获取运营商数据接口
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id(必填),string
    :param name: 手机号（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1803')
    requesturl = baseUrl + "/api/unicom/get_result"
    LOGGER.info("获取运营商数据接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("获取运营商数据接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取运营商数据接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


