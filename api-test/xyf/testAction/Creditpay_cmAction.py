#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_cmAction.py
@desc       : 项目：xyf 模块：creditpay_cm 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_cm_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_cm_login()


def test_cm_goods_add(overdue_rate, platform_service_rate, service_fee_charge_method):
    """
    添加商品（v1.0.0修改）
    :param overdue_rate: 逾期费率,number
    :param platform_service_rate: 平台服务费率,number
    :param service_fee_charge_method: 平台服务费收取方式（v1.0.0新增  1 确认收货时一次性收取 2 随每期账单收取）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2627')
    requesturl = baseUrl + "/cm/goods/add"
    LOGGER.info("添加商品（v1.0.0修改）请求地址:【{}】".format(requesturl))
    params = dict()
    params["overdue_rate"] = overdue_rate
    params["platform_service_rate"] = platform_service_rate
    params["service_fee_charge_method"] = service_fee_charge_method
    LOGGER.info("添加商品（v1.0.0修改）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加商品（v1.0.0修改）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cm_goods_edit(overdue_rate, platform_service_rate, service_fee_charge_method):
    """
    修改商品（v1.0.0修改）
    :param platform_service_rate: 平台服务费,number
    :param overdue_rate: 逾期费率,number
    :param service_fee_charge_method: 平台服务费收取方式（1.0.0新增  1 确认收货时一次性收取 2 随每期账单收取）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2628')
    requesturl = baseUrl + "/cm/goods/edit"
    LOGGER.info("修改商品（v1.0.0修改）请求地址:【{}】".format(requesturl))
    params = dict()
    params["overdue_rate"] = overdue_rate
    params["platform_service_rate"] = platform_service_rate
    params["service_fee_charge_method"] = service_fee_charge_method
    LOGGER.info("修改商品（v1.0.0修改）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改商品（v1.0.0修改）请求参数：【{}】".format(params))
    response = rq.put(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cm_income_getconfig():
    """
    查看某进件配置详情(v1.0.0修改)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2629')
    requesturl = baseUrl + "/cm/income/getconfig"
    LOGGER.info("查看某进件配置详情(v1.0.0修改)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查看某进件配置详情(v1.0.0修改)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看某进件配置详情(v1.0.0修改)请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cm_income_updateincomeconfig(particularinfo):
    """
    保存进件配置(v1.0.0修改)
    :param particularinfo: 特别信息(v1.0.0新增),object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2630')
    requesturl = baseUrl + "/cm/income/updateincomeconfig"
    LOGGER.info("保存进件配置(v1.0.0修改)请求地址:【{}】".format(requesturl))
    params = dict()
    params["particularInfo"] = particularinfo
    LOGGER.info("保存进件配置(v1.0.0修改)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存进件配置(v1.0.0修改)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_cm_income_configform():
    """
    获取所有进件配置（v1.0.0）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2631')
    requesturl = baseUrl + "/api/cm/income/configform"
    LOGGER.info("获取所有进件配置（v1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取所有进件配置（v1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有进件配置（v1.0.0）请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


