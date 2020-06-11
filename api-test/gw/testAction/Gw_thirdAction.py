#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Gw_thirdAction.py
@desc       : 项目：gw 模块：gw_third 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('gw_third_apiURL', 'gw')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_78dk_app_xqc_getArticleInfoPage(currentpage, from_param, pagesize, sign, ts, type):
    """
    文章分页列表
    :param currentpage: 当前页码,number
    :param pagesize: 单页记录数,number
    :param sign: 签名,string
    :param type: 类型（lb-轮播  xqtt-小启头条 wdzx-网贷咨询  ssrd-实时热点）,string
    :param from_param: 来源（固定值=xqc）,string
    :param ts: 当前时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1509')
    requesturl = baseUrl + "/api/78dk/app/xqc/getArticleInfoPage"
    LOGGER.info("文章分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["from"] = from_param
    params["pageSize"] = pagesize
    params["sign"] = sign
    params["ts"] = ts
    params["type"] = type
    LOGGER.info("文章分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_xqc__getArticleInfo(articleinfouuid, from_param, sign, ts):
    """
    获取文章详情
    :param sign: 签名,string
    :param articleinfouuid: 文章uuid,string
    :param from_param: 来源（固定值=xqc）,string
    :param ts: 当前时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1510')
    requesturl = baseUrl + "/api/78dk/app/xqc//getArticleInfo"
    LOGGER.info("获取文章详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    params["from"] = from_param
    params["sign"] = sign
    params["ts"] = ts
    LOGGER.info("获取文章详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取文章详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_third_xqc_getArticleInfoPage(currentpage, from_param, pagesize, sign, ts, type):
    """
    文章分页列表
    :param currentpage: 当前页码,number
    :param pagesize: 单页记录数,number
    :param sign: 签名,string
    :param type: 类型（lb-轮播  xqtt-小启头条 wdzx-网贷咨询  ssrd-实时热点）,string
    :param from_param: 来源（固定值=xqc）,string
    :param ts: 当前时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1527')
    requesturl = baseUrl + "/api/78dk/client/third/xqc/getArticleInfoPage"
    LOGGER.info("文章分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["from"] = from_param
    params["pageSize"] = pagesize
    params["sign"] = sign
    params["ts"] = ts
    params["type"] = type
    LOGGER.info("文章分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_third_xqc_getArticleInfo(articleinfouuid, from_param, sign, ts):
    """
    获取文章详情
    :param sign: 签名,string
    :param articleinfouuid: 文章uuid,string
    :param from_param: 来源（固定值=xqc）,string
    :param ts: 当前时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1528')
    requesturl = baseUrl + "/api/78dk/client/third/xqc/getArticleInfo"
    LOGGER.info("获取文章详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    params["from"] = from_param
    params["sign"] = sign
    params["ts"] = ts
    LOGGER.info("获取文章详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取文章详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admain_common_getVerifyToken(token):
    """
    token验证
    :param token: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2168')
    requesturl = baseUrl + "/api/78dk/admain/common/getVerifyToken"
    LOGGER.info("token验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    LOGGER.info("token验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("token验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_common_getVerifyToken(token):
    """
    token验证
    :param token: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2172')
    requesturl = baseUrl + "/api/78dk/admin/common/getVerifyToken"
    LOGGER.info("token验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    LOGGER.info("token验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("token验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


