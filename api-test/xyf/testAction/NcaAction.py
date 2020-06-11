#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : NcaAction.py
@desc       : 项目：xyf 模块：nca 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('nca_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_nca_login()


def test_auditing_orderAuditing_rule_approve(orderid):
    """
    审核详情_认证信息
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1794')
    requesturl = baseUrl + "/auditing/orderAuditing/rule/approve"
    LOGGER.info("审核详情_认证信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("审核详情_认证信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情_认证信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_applicant_viewApplicantInfo(orderid):
    """
    审核详情_申请人信息_第五个模块
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1795')
    requesturl = baseUrl + "/auditing/applicant/viewApplicantInfo"
    LOGGER.info("审核详情_申请人信息_第五个模块请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("审核详情_申请人信息_第五个模块请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情_申请人信息_第五个模块请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_orderAuditing_rule_readTongdun(orderid, userid):
    """
    审核详情_认证信息_查看同盾报告
    :param orderid: 订单id,number
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1796')
    requesturl = baseUrl + "/auditing/orderAuditing/rule/readTongdun"
    LOGGER.info("审核详情_认证信息_查看同盾报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["userId"] = userid
    LOGGER.info("审核详情_认证信息_查看同盾报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情_认证信息_查看同盾报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_applicant_userAuthDetail(orderid, type):
    """
    审核详情申请人报告信息（运营商）
    :param type: 报告类型,number
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1797')
    requesturl = baseUrl + "/auditing/applicant/userAuthDetail"
    LOGGER.info("审核详情申请人报告信息（运营商）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["type"] = type
    LOGGER.info("审核详情申请人报告信息（运营商）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情申请人报告信息（运营商）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_mauditaccept_searchScore(orderid):
    """
    评分详情
    :param orderid: 订单id(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1801')
    requesturl = baseUrl + "/auditing/mauditaccept/searchScore"
    LOGGER.info("评分详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("评分详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评分详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_finalAuditing_queryFinalAuditingList(card_no, create_time_end, create_time_start, firstauditmoney_end, firstauditmoney_start, mobile, name, order_name, order_no, real_name, secondaudittime_end, secondaudittime_start, secondauditusername, state):
    """
    终审列表
    :param firstauditmoney_start: 一审金额_开始,number
    :param secondaudittime_end: 二审时间_结束,string
    :param create_time_start: 进件时间_开始,string
    :param mobile: 手机号,string
    :param state: 选项卡的状态,number
    :param name: 商家名称,string
    :param secondauditusername: 二审同学,string
    :param real_name: 用户名,string
    :param firstauditmoney_end: 一审金额_结束,number
    :param order_name: 商品名称,string
    :param card_no: 身份证号,string
    :param order_no: 订单号,string
    :param create_time_end: 进件时间_结束,string
    :param secondaudittime_start: 二审时间_开始,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2203')
    requesturl = baseUrl + "/auditing/finalAuditing/queryFinalAuditingList"
    LOGGER.info("终审列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["card_no"] = card_no
    params["create_time_end"] = create_time_end
    params["create_time_start"] = create_time_start
    params["firstAuditMoney_end"] = firstauditmoney_end
    params["firstAuditMoney_start"] = firstauditmoney_start
    params["mobile"] = mobile
    params["name"] = name
    params["order_name"] = order_name
    params["order_no"] = order_no
    params["real_name"] = real_name
    params["secondAuditTime_End"] = secondaudittime_end
    params["secondAuditTime_start"] = secondaudittime_start
    params["secondAuditUserName"] = secondauditusername
    params["state"] = state
    LOGGER.info("终审列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_finalAuditing_addRemark(audit_opinion, audit_status, order_no):
    """
    终审决策备注
    :param order_no: 订单号,string
    :param audit_status: 审核状态,number
    :param audit_opinion: 审核意见,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2204')
    requesturl = baseUrl + "/auditing/finalAuditing/addRemark"
    LOGGER.info("终审决策备注请求地址:【{}】".format(requesturl))
    params = dict()
    params["audit_opinion"] = audit_opinion
    params["audit_status"] = audit_status
    params["order_no"] = order_no
    LOGGER.info("终审决策备注请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审决策备注请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


