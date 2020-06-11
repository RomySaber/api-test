#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-05-09
@Author     : QA
@File       : SpiderETLAction.py
@desc       :  爬虫中心，etl接口
"""
import json
import time

import requests

from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.myConfig import ConfigUtils

TIMEOUT = ConfigUtils.getint('report', 'time_out')
# API_TEST_HEADERS = {'Content-Type': 'application/json'}
LOGGER = getlog(__name__)
rq = requests.Session()


def api_del_data(taskId):
    """
    删除数据
    :param taskId: 爬虫存储的淘宝数据的taskId
    :return:
    """
    start_time = time.time()
    baseUrl = 'http://test.craetltb.78dk.com'
    requesturl = baseUrl + "/api/del_data"
    LOGGER.info("删除数据:【{}】".format(requesturl))
    params = dict()
    params["taskId"] = taskId
    # LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝ETL请求参数：【{}】".format(params))
    # response = rq.post(requesturl, headers=API_TEST_HEADERS, data=json.dumps(params), timeout=TIMEOUT)
    response = rq.post(requesturl, data=json.dumps(params), timeout=TIMEOUT)
    LOGGER.info("淘宝ETL请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "淘宝ETL状态码检查")
    LOGGER.info("淘宝ETL请求接口耗时：【{}】".format(time.time() - start_time))
    return response.json()


def api_etl_taobao(is_encrypt, is_loan_scene, name, phone, taskId):
    """
    爬虫中心淘宝ETL
    :param is_encrypt: 是否需要脱敏
    :param is_loan_scene: 是否为借贷场景
    :param name: 借贷人姓名
    :param phone: 借贷人电话号码
    :param taskId: 爬虫存储的淘宝数据的taskId
    :return:
    """
    start_time = time.time()
    baseUrl = 'http://test.craetltb.78dk.com'
    requesturl = baseUrl + "/api/etl_taobao"
    LOGGER.info("淘宝ETL请求地址:【{}】".format(requesturl))
    params = dict()
    params["is_encrypt"] = is_encrypt
    params["is_loan_scene"] = is_loan_scene
    params["name"] = name
    params["phone"] = phone
    params["taskId"] = taskId
    # LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝ETL请求参数：【{}】".format(json.dumps(params)))
    # response = rq.post(requesturl, headers=API_TEST_HEADERS, data=json.dumps(params), timeout=TIMEOUT)
    response = rq.post(requesturl, data=json.dumps(params), timeout=TIMEOUT)
    LOGGER.info("淘宝ETL请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "淘宝ETL状态码检查")
    LOGGER.info("淘宝ETL请求接口耗时：【{}】".format(time.time() - start_time))
    return response.json()


def etl_jingdong(is_encrypt, is_loan_scene, user_name, user_phone_number, taskId):
    """
    9京东ETL
    :param is_encrypt: 是否需要脱敏
    :param is_loan_scene: 是否为借贷场景
    :param user_name: 借贷人姓名
    :param user_phone_number: 借贷人电话号码
    :param taskId: 爬虫存储的淘宝数据的taskId
    :return:
    """
    start_time = time.time()
    baseUrl = 'http://test.craetljd.78dk.com'
    requesturl = baseUrl + "/etl_jingdong"
    LOGGER.info("9京东ETL请求地址:【{}】".format(requesturl))
    params = dict()
    params["is_encrypt"] = is_encrypt
    params["is_loan_scene"] = is_loan_scene
    params["user_name"] = user_name
    params["user_phone_number"] = user_phone_number
    params["taskId"] = taskId
    # LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("9京东ETL请求参数：【{}】".format(json.dumps(params)))
    # response = rq.post(requesturl, headers=API_TEST_HEADERS, data=json.dumps(params), timeout=TIMEOUT)
    response = rq.post(requesturl, data=json.dumps(params), timeout=TIMEOUT)
    LOGGER.info("9京东ETL请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "京东ETL状态码检查")
    LOGGER.info("9京东ETL请求接口耗时：【{}】".format(time.time() - start_time))
    return response.json()


def api_etl_yys(is_encrypt, is_loan_scene, name, phone, taskId):
    """
    运营商ETL接口
    :param is_encrypt: 是否需要脱敏
    :param is_loan_scene: 是否为借贷场景
    :param user_name: 借贷人姓名
    :param phone: 借贷人电话号码
    :param taskId: 爬虫存储的淘宝数据的taskId
    :return:
    """
    start_time = time.time()
    baseUrl = 'http://test.craetlyys.78dk.com'
    requesturl = baseUrl + "/api/etl_yys"
    LOGGER.info("运营商ETL接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["is_encrypt"] = is_encrypt
    params["is_loan_scene"] = is_loan_scene
    params["name"] = name
    params["phone"] = phone
    params["taskId"] = taskId
    # LOGGER.info("淘宝ETL请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营商ETL接口请求参数：【{}】".format(json.dumps(params)))
    # response = rq.post(requesturl, headers=API_TEST_HEADERS, data=json.dumps(params), timeout=TIMEOUT)
    response = rq.post(requesturl, data=json.loads(json.dumps(params)), timeout=TIMEOUT)
    LOGGER.info("运营商ETL接口请求结果参数：【{}】".format(response.json()))
    Assertion.verity(response.status_code, 200, "运营商ETL状态码检查")
    LOGGER.info("运营商ETL接口请求接口耗时：【{}】".format(time.time() - start_time))
    return response.json()
