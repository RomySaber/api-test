#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : LotteryAction.py
@desc       : 项目：ai 模块：lottery 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('lottery_apiURL', 'ai')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_shensheng_login(name, password, reqid, token):
    """
    1、登录神圣计划
    :param token: 分配的token参数（必填）,string
    :param name: 用户名（必填）,string
    :param password: 密码（必填）,string
    :param reqid: 会话id（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1018')
    requesturl = baseUrl + "/api/shensheng/login"
    LOGGER.info("1、登录神圣计划请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("1、登录神圣计划请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、登录神圣计划请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_hengyao_login(name, password, reqid, token):
    """
    6、登录恒耀娱乐以抓取遗漏数据
    :param name: 用户名（必填）,string
    :param password: 密码（必填）,string
    :param reqid: 会话id（非必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1019')
    requesturl = baseUrl + "/api/hengyao/login"
    LOGGER.info("6、登录恒耀娱乐以抓取遗漏数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("6、登录恒耀娱乐以抓取遗漏数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、登录恒耀娱乐以抓取遗漏数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_hengyao_miss_hot(reqid, token):
    """
    7、获取恒耀娱乐重庆时时彩、腾讯分分彩遗漏数据
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1020')
    requesturl = baseUrl + "/api/hengyao/miss_hot"
    LOGGER.info("7、获取恒耀娱乐重庆时时彩、腾讯分分彩遗漏数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("7、获取恒耀娱乐重庆时时彩、腾讯分分彩遗漏数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("7、获取恒耀娱乐重庆时时彩、腾讯分分彩遗漏数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_shensheng_fetch_kj(reqid, token, type):
    """
    5、获取神圣计划开奖历史数据（100条）
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :param type: 彩种类型ID（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1021')
    requesturl = baseUrl + "/api/shensheng/fetch_kj"
    LOGGER.info("5、获取神圣计划开奖历史数据（100条）请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    params["type"] = type
    LOGGER.info("5、获取神圣计划开奖历史数据（100条）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、获取神圣计划开奖历史数据（100条）请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_shensheng_jh_list(reqid, token):
    """
    2、获取神圣计划所有计划字典
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1022')
    requesturl = baseUrl + "/api/shensheng/jh_list"
    LOGGER.info("2、获取神圣计划所有计划字典请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("2、获取神圣计划所有计划字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、获取神圣计划所有计划字典请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_shensheng_fetch_jh(jhid, reqid, token, type):
    """
    4、获取神圣计划实时数据
    :param jhid: 计划ID（必填）,string
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :param type: 彩种类型ID（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1023')
    requesturl = baseUrl + "/api/shensheng/fetch_jh"
    LOGGER.info("4、获取神圣计划实时数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["jhid"] = jhid
    params["reqId"] = reqid
    params["token"] = token
    params["type"] = type
    LOGGER.info("4、获取神圣计划实时数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、获取神圣计划实时数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_shensheng_rules(reqid, token):
    """
    3、获取神圣计划规则字典
    :param reqid: 会话id（必填）,string
    :param token: 分配的token参数（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1024')
    requesturl = baseUrl + "/api/shensheng/rules"
    LOGGER.info("3、获取神圣计划规则字典请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = token
    LOGGER.info("3、获取神圣计划规则字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、获取神圣计划规则字典请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


