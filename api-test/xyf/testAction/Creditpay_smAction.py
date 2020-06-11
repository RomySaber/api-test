#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_smAction.py
@desc       : 项目：xyf 模块：creditpay_sm 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_sm_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_sm_login()


def test_api_st_sm_audit_history(currentpage, pagesize, smid):
    """
    审批历史记录
    :param currentpage: ,number
    :param pagesize: ,number
    :param smid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2620')
    requesturl = baseUrl + "/api/st/sm/audit/history"
    LOGGER.info("审批历史记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["smId"] = smid
    LOGGER.info("审批历史记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审批历史记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_st_sm_reportList(currentpage, merchantname, pagesize, type):
    """
    列表查询
    :param currentpage: ,
    :param merchantname: ,
    :param pagesize: ,
    :param type: 数据类型，1：查询全部，2：香江金融，3：启发自有,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2621')
    requesturl = baseUrl + "/api/st/sm/reportList"
    LOGGER.info("列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["merchantName"] = merchantname
    params["pageSize"] = pagesize
    params["type"] = type
    LOGGER.info("列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_st_sm_orderList(currentpage, fundtype, ordertyoe, pagesize, smid):
    """
    查看详情（v1.0.0修改）
    :param currentpage: ,
    :param fundtype: 资金类型，1：查询全部，2：香江金融，3：启发自有,
    :param ordertyoe: 订单类型，1：白条订单，2：商品分期,
    :param pagesize: ,
    :param smid: 记录ID,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2622')
    requesturl = baseUrl + "/api/st/sm/orderList"
    LOGGER.info("查看详情（v1.0.0修改）请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["fundType"] = fundtype
    params["orderTyoe"] = ordertyoe
    params["pageSize"] = pagesize
    params["smId"] = smid
    LOGGER.info("查看详情（v1.0.0修改）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看详情（v1.0.0修改）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_st_sm_history_reportList(accountenddate, accountstartdate, currentpage, examineenddate, examinestartdate, merchantname, pagesize):
    """
    列表
    :param pagesize: ,
    :param currentpage: ,
    :param examineenddate: 审核结束时间,string
    :param accountenddate: 结算结束时间,string
    :param merchantname: 商户名称,string
    :param examinestartdate: 审核开始时间,
    :param accountstartdate: 结算开始时间,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2623')
    requesturl = baseUrl + "/api/st/sm/history/reportList"
    LOGGER.info("列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountEndDate"] = accountenddate
    params["accountStartDate"] = accountstartdate
    params["currentPage"] = currentpage
    params["examineEndDate"] = examineenddate
    params["examineStartDate"] = examinestartdate
    params["merchantName"] = merchantname
    params["pageSize"] = pagesize
    LOGGER.info("列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_st_sm_report_audit(opttype, smid):
    """
    财务/信审结算通过
    :param opttype: 1：结算确认，2：财务确认,string
    :param smid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2624')
    requesturl = baseUrl + "/api/st/sm/report/audit"
    LOGGER.info("财务/信审结算通过请求地址:【{}】".format(requesturl))
    params = dict()
    params["optType"] = opttype
    params["smId"] = smid
    LOGGER.info("财务/信审结算通过请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务/信审结算通过请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


