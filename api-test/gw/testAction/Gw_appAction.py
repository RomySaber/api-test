#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Gw_appAction.py
@desc       : 项目：gw 模块：gw_app 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('gw_app_apiURL', 'gw')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_78dk_client_clientBusiInfo_addXQKCBusiInfo(companyname, mail, name, phone, post, userscenario):
    """
    小启控车商务信息添加
    :param phone: 电话号码,string
    :param companyname: 公司名称,string
    :param name: 姓名,string
    :param userscenario: 用户场景,string
    :param mail: 邮件地址,string
    :param post: 职位,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1150')
    requesturl = baseUrl + "/api/78dk/client/clientBusiInfo/addXQKCBusiInfo"
    LOGGER.info("小启控车商务信息添加请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["mail"] = mail
    params["name"] = name
    params["phone"] = phone
    params["post"] = post
    params["userScenario"] = userscenario
    LOGGER.info("小启控车商务信息添加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启控车商务信息添加请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_clientBusiInfo_addHCKJBusiInfo(companyname, mail, name, phone, post, userscenario):
    """
    好车科技商务信息添加
    :param companyname: 公司名称,string
    :param mail: 邮件地址,string
    :param name: 姓名,string
    :param phone: 电话号码,string
    :param post: 职位,string
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1151')
    requesturl = baseUrl + "/api/78dk/client/clientBusiInfo/addHCKJBusiInfo"
    LOGGER.info("好车科技商务信息添加请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["mail"] = mail
    params["name"] = name
    params["phone"] = phone
    params["post"] = post
    params["userScenario"] = userscenario
    LOGGER.info("好车科技商务信息添加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("好车科技商务信息添加请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_clientBusiInfo_addXQXYBusiInfo(companyname, mail, name, phone, post, userscenario):
    """
    小启信用商务信息添加
    :param companyname: 公司名称,string
    :param mail: 邮件地址,string
    :param name: 姓名,string
    :param phone: 电话号码,string
    :param post: 职位,string
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1152')
    requesturl = baseUrl + "/api/78dk/client/clientBusiInfo/addXQXYBusiInfo"
    LOGGER.info("小启信用商务信息添加请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["mail"] = mail
    params["name"] = name
    params["phone"] = phone
    params["post"] = post
    params["userScenario"] = userscenario
    LOGGER.info("小启信用商务信息添加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启信用商务信息添加请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_clientBusiInfo_addXQJRYBusiInfo(companyname, mail, name, phone, post, userscenario):
    """
    小启金融云商务信息添加
    :param companyname: 公司名称,string
    :param mail: 邮件地址,string
    :param name: 姓名,string
    :param phone: 电话号码,string
    :param post: 职位,string
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1153')
    requesturl = baseUrl + "/api/78dk/client/clientBusiInfo/addXQJRYBusiInfo"
    LOGGER.info("小启金融云商务信息添加请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["mail"] = mail
    params["name"] = name
    params["phone"] = phone
    params["post"] = post
    params["userScenario"] = userscenario
    LOGGER.info("小启金融云商务信息添加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启金融云商务信息添加请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_clientArticleInfo_getArticleInfoPage():
    """
    文章列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1167')
    requesturl = baseUrl + "/api/78dk/client/clientArticleInfo/getArticleInfoPage"
    LOGGER.info("文章列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("文章列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_client_clientArticleInfo_getArticleInfo(articleinfouuid):
    """
    文章详情
    :param articleinfouuid: 文章uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1168')
    requesturl = baseUrl + "/api/78dk/client/clientArticleInfo/getArticleInfo"
    LOGGER.info("文章详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("文章详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


