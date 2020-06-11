#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_mmAction.py
@desc       : 项目：xyf 模块：creditpay_mm 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_mm_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_mm_login()


def test_mm_partner_getLogs(currentpage, id, pagesize):
    """
    商户变更日志列表查询
    :param pagesize: 每页数据条数,number
    :param currentpage: 当前页,number
    :param id: 当前商户的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2615')
    requesturl = baseUrl + "/mm/partner/getLogs"
    LOGGER.info("商户变更日志列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["id"] = id
    params["pageSize"] = pagesize
    LOGGER.info("商户变更日志列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户变更日志列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_bd_queryBdLogList(currentpage, id, pagesize):
    """
    bd日志列表
    :param currentpage: 当前页,number
    :param id: 销售人员id,number
    :param pagesize: 每页数据条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2616')
    requesturl = baseUrl + "/mm/bd/queryBdLogList"
    LOGGER.info("bd日志列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["id"] = id
    params["pageSize"] = pagesize
    LOGGER.info("bd日志列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd日志列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_bd_updateBd(email, id, mobile, name, status):
    """
    修改BD
    :param email: 邮箱,string
    :param mobile: 手机号,string
    :param name: 姓名,string
    :param id: 销售人员id,number
    :param status: 状态,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2617')
    requesturl = baseUrl + "/mm/bd/updateBd"
    LOGGER.info("修改BD请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["id"] = id
    params["mobile"] = mobile
    params["name"] = name
    params["status"] = status
    LOGGER.info("修改BD请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改BD请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_bd_bdListQuery(currentpage, name, pagesize, status):
    """
    bd列表
    :param name: BD姓名,string
    :param status: 状态,number
    :param pagesize: 每页数据条数,number
    :param currentpage: 当前页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2618')
    requesturl = baseUrl + "/mm/bd/bdListQuery"
    LOGGER.info("bd列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["status"] = status
    LOGGER.info("bd列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_partner_savePartner(city, county, province):
    """
    商户保持修改
    :param city: 城市code,string
    :param county: 区域code,string
    :param province: 省code,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2619')
    requesturl = baseUrl + "/mm/partner/savePartner"
    LOGGER.info("商户保持修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["county"] = county
    params["province"] = province
    LOGGER.info("商户保持修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户保持修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_common_viewRegionLists(paramsingle):
    """
    区/县级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2830')
    requesturl = baseUrl + "/mm/common/viewRegionLists"
    LOGGER.info("区/县级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("区/县级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("区/县级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_common_viewCityLists(paramsingle):
    """
    市级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2831')
    requesturl = baseUrl + "/mm/common/viewCityLists"
    LOGGER.info("市级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("市级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("市级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_mm_common_viewProvinceLists(paramsingle):
    """
    省级下拉
    :param paramsingle: 上级编码(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2832')
    requesturl = baseUrl + "/mm/common/viewProvinceLists"
    LOGGER.info("省级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("省级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("省级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


