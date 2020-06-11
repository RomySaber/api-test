#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : BankcmbcAction.py
@desc       : 项目：ai 模块：BankCMBC 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('BankCMBC_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_bankcmbc_login(name, password, reqid, token):
    """
    1、用户名密码登录
    :param name: 用户名（必填）,string
    :param password: 密码（必填）,string
    :param reqid: 会话id(非必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1174')
    requesturl = baseUrl + "/api/bankcmbc/login"
    LOGGER.info("1、用户名密码登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、用户名密码登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、用户名密码登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankcmbc_get_status(reqid, token):
    """
    2、查询任务执行阶段状态
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1175')
    requesturl = baseUrl + "/api/bankcmbc/get_status"
    LOGGER.info("2、查询任务执行阶段状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、查询任务执行阶段状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、查询任务执行阶段状态请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_bankcmbc_get_result(cardno, reqid, token):
    """
    3、获取银行抓取数据
    :param reqid: 会话id(必填),string
    :param token: 分配的token参数（必填）,string
    :param cardno: 卡号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1176')
    requesturl = baseUrl + "/api/bankcmbc/get_result"
    LOGGER.info("3、获取银行抓取数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNo"] = cardno
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、获取银行抓取数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、获取银行抓取数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


