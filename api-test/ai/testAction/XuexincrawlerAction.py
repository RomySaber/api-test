#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : XuexincrawlerAction.py
@desc       : 项目：ai 模块：XuexinCrawler 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('XuexinCrawler_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_xuexin_refresh_verify_code(reqid, token):
    """
    2、刷新学信登录的图片验证码接口
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1317')
    requesturl = baseUrl + "/api/xuexin/refresh_verify_code"
    LOGGER.info("2、刷新学信登录的图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、刷新学信登录的图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、刷新学信登录的图片验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_unicom_login_submit(code, name, password, randompassword, reqid, token):
    """
    4、账号密码登录提交接口
    :param password: 密码（必填）,string
    :param name: 用户名（必填）,string
    :param token: 分配的token参数（必填）,string
    :param code: 图片验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :param reqid: 会话id(必填),string
    :param randompassword: 随机验证码（根据初始化配置接口获取的数据判断是否必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1318')
    requesturl = baseUrl + "/api/unicom/login_submit"
    LOGGER.info("4、账号密码登录提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("4、账号密码登录提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、账号密码登录提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_xuexin_login_submit(code, name, password, reqid, token, xx):
    """
    1、账号密码（及学校名称）登录提交接口
    :param password: 密码（必填）,string
    :param name: 用户名（必填）,string
    :param token: 分配的token参数（必填）,string
    :param code: 图片验证码（根据第一次提交登陆信息判断是否必填）,string
    :param reqid: 会话id(必填),string
    :param xx: 学校名称（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1321')
    requesturl = baseUrl + "/api/xuexin/login_submit"
    LOGGER.info("1、账号密码（及学校名称）登录提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    params["xx"] = xx
    LOGGER.info("1、账号密码（及学校名称）登录提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、账号密码（及学校名称）登录提交接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


