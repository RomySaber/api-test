#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_bmAction.py
@desc       : 项目：xyf 模块：creditpay_bm 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_bm_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_bm_login()


def test_bm_merchant_account_MerchantSettlementExport(merchantname, type):
    """
    导出商户结算表
    :param type: 放款渠道,number
    :param merchantname: 商户名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2822')
    requesturl = baseUrl + "/bm/merchant/account/MerchantSettlementExport"
    LOGGER.info("导出商户结算表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantName"] = merchantname
    params["type"] = type
    LOGGER.info("导出商户结算表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出商户结算表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_bm_merchant_account_settledHistoryExport(accountenddate, accountstartdate, examineenddate, examinestartdate, merchantname):
    """
    导出历史结算表
    :param accountenddate: 结算结束时间,
    :param accountstartdate: 结算开始时间,
    :param examineenddate: 审核结束时间,
    :param examinestartdate: 审核开始时间,
    :param merchantname: 商户名称,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2823')
    requesturl = baseUrl + "/bm/merchant/account/settledHistoryExport"
    LOGGER.info("导出历史结算表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountEndDate"] = accountenddate
    params["accountStartDate"] = accountstartdate
    params["examineEndDate"] = examineenddate
    params["examineStartDate"] = examinestartdate
    params["merchantName"] = merchantname
    LOGGER.info("导出历史结算表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出历史结算表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


