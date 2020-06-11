#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : JdAction.py
@desc       : 项目：ai 模块：jd 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('jd_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_jingdong_login(name, password, reqid, token):
    """
    1、使用用户名密码登录并获取信息
    :param token: 分配的token参数（必填）,string
    :param name: 用户名（必填）,string
    :param password: 密码（必填）,string
    :param reqid: 会话id（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1183')
    requesturl = baseUrl + "/api/jingdong/login"
    LOGGER.info("1、使用用户名密码登录并获取信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、使用用户名密码登录并获取信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、使用用户名密码登录并获取信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_getcode(reqid, token):
    """
    2、获取短信验证码
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1184')
    requesturl = baseUrl + "/api/jingdong/getcode"
    LOGGER.info("2、获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、获取短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_verifycode(code, reqid, token):
    """
    3、校验短信验证码
    :param code: 验证码（必填）,string
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1185')
    requesturl = baseUrl + "/api/jingdong/verifycode"
    LOGGER.info("3、校验短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、校验短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、校验短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_getqrcode(reqid, token):
    """
    1、获取二维码
    :param token: 分配的token参数（必填）,string
    :param reqid: 会话id（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1186')
    requesturl = baseUrl + "/api/jingdong/getqrcode"
    LOGGER.info("1、获取二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、获取二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、获取二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_verifyqrcode(reqid, token):
    """
    2、验证二维码是否已扫描，并获取信息
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1187')
    requesturl = baseUrl + "/api/jingdong/verifyqrcode"
    LOGGER.info("2、验证二维码是否已扫描，并获取信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、验证二维码是否已扫描，并获取信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、验证二维码是否已扫描，并获取信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_qrgetcode(reqid, token):
    """
    3、获取短信验证码
    :param reqid: 会话id（非必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1188')
    requesturl = baseUrl + "/api/jingdong/qrgetcode"
    LOGGER.info("3、获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、获取短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_jingdong_qrverifycode(code, reqid, token):
    """
    4、校验短信验证码
    :param token: 分配的token参数（必填）,string
    :param code: 验证码（必填）,string
    :param reqid: 会话id（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1189')
    requesturl = baseUrl + "/api/jingdong/qrverifycode"
    LOGGER.info("4、校验短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("4、校验短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、校验短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


