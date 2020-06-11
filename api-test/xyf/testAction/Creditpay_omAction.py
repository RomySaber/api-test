#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_omAction.py
@desc       : 项目：xyf 模块：creditpay_om 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_om_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_om_login()


def test_om_orderinfo_search():
    """
    订单信息列表（v1.0.0修改）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2625')
    requesturl = baseUrl + "/om/orderinfo/search"
    LOGGER.info("订单信息列表（v1.0.0修改）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("订单信息列表（v1.0.0修改）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单信息列表（v1.0.0修改）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_om_manage_pageList():
    """
    分页查询退货订单（原有接口修改，请求参数不变）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2626')
    requesturl = baseUrl + "/om/manage/pageList"
    LOGGER.info("分页查询退货订单（原有接口修改，请求参数不变）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("分页查询退货订单（原有接口修改，请求参数不变）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分页查询退货订单（原有接口修改，请求参数不变）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_om_orderinfo_exportExcel(applytime_end, applytime_start, audittime_end, audittime_start, audit_result, bdid, merchantsname, mobile, money_end, money_start, orderno, orderstatus, realname, receipt_end, receipt_start):
    """
    订单信息导出(v4.0.3)
    :param orderno: 订单号,string
    :param orderstatus: 订单状态,string
    :param applytime_end: 提交审核时间_end,string
    :param applytime_start: 提交审核时间_start,string
    :param audittime_end: 审核结束时间_end,string
    :param audittime_start: 审核结束时间_start,string
    :param audit_result: 审核结果 1:通过 2:拒绝 3:返回,number
    :param bdid: BDId,number
    :param merchantsname: 商户名称,string
    :param mobile: 客户电话,string
    :param money_end: 申请金额_end,number
    :param money_start: 申请金额_start,number
    :param realname: 客户姓名,string
    :param receipt_end: 确认收货时间_end,string
    :param receipt_start: 确认收货时间_start,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2821')
    requesturl = baseUrl + "/om/orderinfo/exportExcel"
    LOGGER.info("订单信息导出(v4.0.3)请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyTime_end"] = applytime_end
    params["applyTime_start"] = applytime_start
    params["auditTime_end"] = audittime_end
    params["auditTime_start"] = audittime_start
    params["audit_result"] = audit_result
    params["bdId"] = bdid
    params["merchantsName"] = merchantsname
    params["mobile"] = mobile
    params["money_end"] = money_end
    params["money_start"] = money_start
    params["orderNo"] = orderno
    params["orderStatus"] = orderstatus
    params["realName"] = realname
    params["receipt_end"] = receipt_end
    params["receipt_start"] = receipt_start
    LOGGER.info("订单信息导出(v4.0.3)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单信息导出(v4.0.3)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


