#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Easyloan_webAction.py
@desc       : 项目：easyloan 模块：easyloan_web 接口方法封装
"""

from easyloan.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('easyloan_web_apiURL', 'easyloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_easyloan_web_login()
API_TEST_HEADERS['AuthorToken'] = LICENCES


def test_api_78dk_app(c, p, reqparam):
    """
    测试接口
    :param p: ,
    :param reqparam: 某请求参数,string
    :param c: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 530')
    requesturl = baseUrl + "/api/78dk/app"
    LOGGER.info("测试接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["c"] = c
    params["p"] = p
    params["reqParam"] = reqparam
    LOGGER.info("测试接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("测试接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_queryProductList(currentpage, name, pagesize, period, producttype, repaymentmethod):
    """
    分页查询
    :param producttype: 产品类型（N）,string
    :param name: 产品名称（N）,string
    :param currentpage: 当前页面数（Y）,number
    :param repaymentmethod: 还款方式（N）,string
    :param pagesize: 当前展现条数（Y）,number
    :param period: 产品期限（N）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 531')
    requesturl = baseUrl + "/api/78dk/web/product/queryProductList"
    LOGGER.info("分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["period"] = period
    params["productType"] = producttype
    params["repaymentMethod"] = repaymentmethod
    LOGGER.info("分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_enableOrDisableProduct(productdetailuuid, productstate):
    """
    产品-启用禁用
    :param productdetailuuid: 产品uuid（Y）,string
    :param productstate: 数据状态（‘0’启用‘1‘禁用）（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 532')
    requesturl = baseUrl + "/api/78dk/web/product/enableOrDisableProduct"
    LOGGER.info("产品-启用禁用请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    params["productState"] = productstate
    LOGGER.info("产品-启用禁用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品-启用禁用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_addProduct(auditmanagemonth, auditmanageper, channelcostmonth, channelfee, managefee, middlefeerate, minpenaltyfee, name, overduepenaltyrate, penaltyrate, performancerate, period, preextractscale, preforceextractscale, productapr, productdetailuuid, producttype, repaymentmethod, royaltyrate, serverfee, serverper, servicemonth):
    """
    产品-添加,修改(v1.0.4)
    :param name: 产品名称,string
    :param minpenaltyfee: 最低违约金(元),number
    :param preforceextractscale: 强制结清违约金比例(%),number
    :param middlefeerate: 代扣中间费收取比例（%）,number
    :param servicemonth: 服务费/月(%),number
    :param channelfee: 渠道费率/笔(%),number
    :param serverfee: 服务费率（%）,number
    :param managefee: 管理费率（月%）,number
    :param auditmanagemonth: 账户审核管理费/月(%,number
    :param repaymentmethod: 还款方式(`0`等额本息`1`先息后本,number
    :param auditmanageper: 账户审核管理费/笔(%),number
    :param preextractscale: 自愿结清违约金比例(%),number
    :param penaltyrate: 罚息利率（日%）,number
    :param overduepenaltyrate: 逾期违约金罚取比例(%),number
    :param productapr: 产品利率（月%）,number
    :param period: 贷款期限（月）,number
    :param serverper: 服务费/笔(%),number
    :param producttype: 产品类型(车抵押	JKFS0001 车质押	JKFS0002),number
    :param channelcostmonth: 渠道费率/月(%),number
    :param productdetailuuid: uuid（产品唯一编号）,string
    :param performancerate: 业绩比例（%）,number
    :param royaltyrate: 提成比例（%）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 533')
    requesturl = baseUrl + "/api/78dk/web/product/addProduct"
    LOGGER.info("产品-添加,修改(v1.0.4)请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditManageMonth"] = auditmanagemonth
    params["auditManagePer"] = auditmanageper
    params["channelCostMonth"] = channelcostmonth
    params["channelFee"] = channelfee
    params["manageFee"] = managefee
    params["middleFeeRate"] = middlefeerate
    params["minPenaltyFee"] = minpenaltyfee
    params["name"] = name
    params["overduePenaltyRate"] = overduepenaltyrate
    params["penaltyRate"] = penaltyrate
    params["performanceRate"] = performancerate
    params["period"] = period
    params["preExtractscale"] = preextractscale
    params["preforceExtractscale"] = preforceextractscale
    params["productApr"] = productapr
    params["productDetailUuid"] = productdetailuuid
    params["productType"] = producttype
    params["repaymentMethod"] = repaymentmethod
    params["royaltyRate"] = royaltyrate
    params["serverFee"] = serverfee
    params["serverPer"] = serverper
    params["serviceMonth"] = servicemonth
    LOGGER.info("产品-添加,修改(v1.0.4)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品-添加,修改(v1.0.4)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_queryProduct(productdetailuuid):
    """
    产品-详情
    :param productdetailuuid: 产品uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 534')
    requesturl = baseUrl + "/api/78dk/web/product/queryProduct"
    LOGGER.info("产品-详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("产品-详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品-详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_queryTrial(currentpage, mobile, orderstate, pagesize, storename, username):
    """
    我的已审-分页查询v1.0.4
    :param pagesize: 展示条数(Y),number
    :param mobile: 手机号（N）,string
    :param storename: 门店（N）,string
    :param username: 客户姓名(N),string
    :param currentpage: 当前页数(Y),number
    :param orderstate: 业务状态（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 535')
    requesturl = baseUrl + "/api/78dk/web/risk/queryTrial"
    LOGGER.info("我的已审-分页查询v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["orderState"] = orderstate
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["userName"] = username
    LOGGER.info("我的已审-分页查询v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的已审-分页查询v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addFinalProcess(cause, examineresult, lending, loanorderuuid, remark):
    """
    终审-保存处理结果
    :param examineresult: 审核结果（Y）,string
    :param loanorderuuid: 订单uuid(Y),string
    :param remark: 备注,string
    :param lending: 放款渠道,string
    :param cause: 原因,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 536')
    requesturl = baseUrl + "/api/78dk/web/risk/addFinalProcess"
    LOGGER.info("终审-保存处理结果请求地址:【{}】".format(requesturl))
    params = dict()
    params["cause"] = cause
    params["examineResult"] = examineresult
    params["lending"] = lending
    params["loanOrderUuid"] = loanorderuuid
    params["remark"] = remark
    LOGGER.info("终审-保存处理结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审-保存处理结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_queryFinalProcess(currentpage, mobile, pagesize, storename, username):
    """
    终审-分页查询搜索查询v1.0.4
    :param pagesize: 展示条数(Y),number
    :param mobile: 手机号(N),string
    :param storename: 门店(N),string
    :param username: 客户姓名（N）,string
    :param currentpage: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 537')
    requesturl = baseUrl + "/api/78dk/web/risk/queryFinalProcess"
    LOGGER.info("终审-分页查询搜索查询v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["userName"] = username
    LOGGER.info("终审-分页查询搜索查询v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审-分页查询搜索查询v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_login(password, username):
    """
    登录
    :param password: 密码(Y),string
    :param username: 账号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 538')
    requesturl = baseUrl + "/api/78dk/web/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["username"] = username
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_logout():
    """
    登出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 539')
    requesturl = baseUrl + "/api/78dk/web/logout"
    LOGGER.info("登出请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("登出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登出请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_client_queryClientInfoLists(currentpage, enddate, mobile, name, pagesize, startdate, state):
    """
    客户列表查询Page
    :param state: 实名,string
    :param startdate: 开始时间,string
    :param mobile: 手机 号码,string
    :param pagesize: 每页大小(Y),number
    :param name: 姓名,string
    :param enddate: 结束时间,string
    :param currentpage: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 540')
    requesturl = baseUrl + "/api/78dk/web/client/queryClientInfoLists"
    LOGGER.info("客户列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["mobile"] = mobile
    params["name"] = name
    params["pageSize"] = pagesize
    params["startDate"] = startdate
    params["state"] = state
    LOGGER.info("客户列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客户列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_assignOtherStore(loanuuid, storeuuid):
    """
    分配到其它门店
    :param storeuuid: 门店Uuid(Y),string
    :param loanuuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 541')
    requesturl = baseUrl + "/api/78dk/web/loan/base/assignOtherStore"
    LOGGER.info("分配到其它门店请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    params["storeUuid"] = storeuuid
    LOGGER.info("分配到其它门店请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分配到其它门店请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_refuseLoanOrder(loanuuid, refusetype):
    """
    取消订单
    :param loanuuid: 订单Uuid(Y),string
    :param refusetype: 类型（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 542')
    requesturl = baseUrl + "/api/78dk/web/loan/common/refuseLoanOrder"
    LOGGER.info("取消订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    params["refuseType"] = refusetype
    LOGGER.info("取消订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("取消订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_commitLoanOrder(loanuuid):
    """
    提交订单
    :param loanuuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 543')
    requesturl = baseUrl + "/api/78dk/web/loan/common/commitLoanOrder"
    LOGGER.info("提交订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("提交订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_returnLoanOrder(loanuuid):
    """
    退回订单
    :param loanuuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 544')
    requesturl = baseUrl + "/api/78dk/web/loan/common/returnLoanOrder"
    LOGGER.info("退回订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("退回订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退回订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_getTotalProduct():
    """
    获取产品下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 545')
    requesturl = baseUrl + "/api/78dk/web/product/getTotalProduct"
    LOGGER.info("获取产品下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取产品下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取产品下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_queryProductDetailConfig(productdetailuuid):
    """
    根据产品的uuid联动返回期限、利率（已废弃）
    :param productdetailuuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 546')
    requesturl = baseUrl + "/api/78dk/web/product/queryProductDetailConfig"
    LOGGER.info("根据产品的uuid联动返回期限、利率（已废弃）请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("根据产品的uuid联动返回期限、利率（已废弃）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品的uuid联动返回期限、利率（已废弃）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_editUserPwd(newpassword, password):
    """
    修改密码
    :param password: 当前密码(Y),string
    :param newpassword: 新密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 547')
    requesturl = baseUrl + "/api/78dk/web/editUserPwd"
    LOGGER.info("修改密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["newPassWord"] = newpassword
    params["password"] = password
    LOGGER.info("修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_updateSysRole(sysroleuuuid):
    """
    切换岗位
    :param sysroleuuuid: 选择的岗位uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 548')
    requesturl = baseUrl + "/api/78dk/web/updateSysRole"
    LOGGER.info("切换岗位请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysRoleUuuid"] = sysroleuuuid
    LOGGER.info("切换岗位请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("切换岗位请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_addOrg(city, citycontract, level, name, orgaddress, orgmainuser, orgphone, orgstatus, province, puuid, region):
    """
    组织-新增
    :param orgmainuser: 机构负责人(Y),string
    :param province: 省(Y),string
    :param orgaddress: 机构详细地址(Y),string
    :param level: 层级(Y),string
    :param orgphone: 机构联系方式(Y),string
    :param puuid: 父级机构uuid(Y),string
    :param region: 区(Y),string
    :param name: 机构名称(Y),string
    :param city: 市(Y),string
    :param orgstatus: 是否有效(Y),string
    :param citycontract: 合同城市编号代码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 549')
    requesturl = baseUrl + "/api/78dk/web/org/addOrg"
    LOGGER.info("组织-新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["cityContract"] = citycontract
    params["level"] = level
    params["name"] = name
    params["orgAddress"] = orgaddress
    params["orgMainUser"] = orgmainuser
    params["orgPhone"] = orgphone
    params["orgStatus"] = orgstatus
    params["province"] = province
    params["puuid"] = puuid
    params["region"] = region
    LOGGER.info("组织-新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织-新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_queryOrg(sysorganizationuuid):
    """
    组织-详情
    :param sysorganizationuuid: 机构uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 550')
    requesturl = baseUrl + "/api/78dk/web/org/queryOrg"
    LOGGER.info("组织-详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysOrganizationUuid"] = sysorganizationuuid
    LOGGER.info("组织-详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织-详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_delOrg(sysorganizationuuid):
    """
    组织-删除
    :param sysorganizationuuid: 机构uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 551')
    requesturl = baseUrl + "/api/78dk/web/org/delOrg"
    LOGGER.info("组织-删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysOrganizationUuid"] = sysorganizationuuid
    LOGGER.info("组织-删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织-删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_client_queryClientInfo(uuid):
    """
    查看客户信息
    :param uuid: 客户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 552')
    requesturl = baseUrl + "/api/78dk/web/client/queryClientInfo"
    LOGGER.info("查看客户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("查看客户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看客户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_queryLoanRequestLists(currentpage, mobile, pagesize, username):
    """
    借款申请列表查询Page
    :param pagesize: 每页大小(Y),number
    :param mobile: 手机号(N),string
    :param username: 客户姓名(N),string
    :param currentpage: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 553')
    requesturl = baseUrl + "/api/78dk/web/loan/base/queryLoanRequestLists"
    LOGGER.info("借款申请列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("借款申请列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款申请列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_queryLoanOrderListsKF(currentpage, mobile, pagesize, username):
    """
    借款订单列表查询Page
    :param currentpage: 当前页数(Y),number
    :param username: 客户姓名(N),string
    :param mobile: 手机号(N),string
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 554')
    requesturl = baseUrl + "/api/78dk/web/loan/base/queryLoanOrderListsKF"
    LOGGER.info("借款订单列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("借款订单列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款订单列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_queryLoanOrderListsPGS(currentpage, mobile, pagesize, username):
    """
    借款订单列表查询Page
    :param pagesize: 每页大小(Y),number
    :param username: 客户姓名(N),string
    :param mobile: 手机号(N),string
    :param currentpage: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 555')
    requesturl = baseUrl + "/api/78dk/web/loan/base/queryLoanOrderListsPGS"
    LOGGER.info("借款订单列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("借款订单列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款订单列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_queryLoanOrderListsMDJL(commituseruuid, currentpage, mobile, pagesize, username):
    """
    借款订单列表查询Page
    :param currentpage: 当前页数(Y),number
    :param commituseruuid: 提交人Uuid(N),string
    :param mobile: 手机号(N),string
    :param username: 客户姓名(N),string
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 556')
    requesturl = baseUrl + "/api/78dk/web/loan/base/queryLoanOrderListsMDJL"
    LOGGER.info("借款订单列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["commitUserUuid"] = commituseruuid
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("借款订单列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款订单列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryClientContactLists(uuid):
    """
    借款人联系人信息查看(已废弃)
    :param uuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 557')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryClientContactLists"
    LOGGER.info("借款人联系人信息查看(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("借款人联系人信息查看(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款人联系人信息查看(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryClientCardLists(uuid):
    """
    借款人银行卡查看(已废弃)
    :param uuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 558')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryClientCardLists"
    LOGGER.info("借款人银行卡查看(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("借款人银行卡查看(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款人银行卡查看(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanOrderInfo(uuid):
    """
    借款详情查看(已废弃)
    :param uuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 559')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanOrderInfo"
    LOGGER.info("借款详情查看(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("借款详情查看(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款详情查看(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanCheckResultLists(currentpage, loanorderuuid, pagesize):
    """
    历史意见列表查询Page(张琦)
    :param loanorderuuid: 订单Uuid(Y),string
    :param currentpage: 当前页数(Y),string
    :param pagesize: 每页大小(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 560')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanCheckResultLists"
    LOGGER.info("历史意见列表查询Page(张琦)请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["loanOrderUuid"] = loanorderuuid
    params["pageSize"] = pagesize
    LOGGER.info("历史意见列表查询Page(张琦)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史意见列表查询Page(张琦)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryClientRequestLists():
    """
    申请资料列表查询(已废弃)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 561')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryClientRequestLists"
    LOGGER.info("申请资料列表查询(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("申请资料列表查询(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请资料列表查询(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_addLoanFileLists(loaninfofile):
    """
    签约资料保存(张琦)
    :param loaninfofile: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 562')
    requesturl = baseUrl + "/api/78dk/web/loan/info/addLoanFileLists"
    LOGGER.info("签约资料保存(张琦)请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanInfoFile"] = loaninfofile
    LOGGER.info("签约资料保存(张琦)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约资料保存(张琦)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanFileLists(dictcode, uuid):
    """
    签约资料预览(已废弃)
    :param dictcode: 文件类型（code）(Y),string
    :param uuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 563')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanFileLists"
    LOGGER.info("签约资料预览(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    params["uuid"] = uuid
    LOGGER.info("签约资料预览(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约资料预览(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_vehicleInfoUpdate(vehicleinfo, vehicleinspect):
    """
    车辆信息保存、修改-v1.0.4
    :param vehicleinspect: 车辆静态检查,object
    :param vehicleinfo: 车辆信息,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 564')
    requesturl = baseUrl + "/api/78dk/web/loan/info/vehicleInfoUpdate"
    LOGGER.info("车辆信息保存、修改-v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["vehicleInfo"] = vehicleinfo
    params["vehicleInspect"] = vehicleinspect
    LOGGER.info("车辆信息保存、修改-v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆信息保存、修改-v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryVehicleInfo(uuid):
    """
    车辆信息查看(废弃)
    :param uuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 565')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryVehicleInfo"
    LOGGER.info("车辆信息查看(废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("车辆信息查看(废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆信息查看(废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_addVehicleProcedLists(vehiclefile):
    """
    车辆手续保存(张琦)
    :param vehiclefile: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 566')
    requesturl = baseUrl + "/api/78dk/web/loan/info/addVehicleProcedLists"
    LOGGER.info("车辆手续保存(张琦)请求地址:【{}】".format(requesturl))
    params = dict()
    params["vehicleFile"] = vehiclefile
    LOGGER.info("车辆手续保存(张琦)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆手续保存(张琦)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryVehicleProcedLists():
    """
    车辆手续列表查询(已废弃)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 567')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryVehicleProcedLists"
    LOGGER.info("车辆手续列表查询(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("车辆手续列表查询(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆手续列表查询(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_queryClientInfoLists(currentpage, mobile, orderstate, pagesize, username):
    """
    我的已办-分页查询
    :param currentpage: 当前页数(Y),number
    :param orderstate: 订单状态(N),string
    :param mobile: 手机号(N),string
    :param pagesize: 每页大小(Y),number
    :param username: 客户姓名(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 568')
    requesturl = baseUrl + "/api/78dk/web/loan/base/queryClientInfoLists"
    LOGGER.info("我的已办-分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["orderState"] = orderstate
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("我的已办-分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的已办-分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_queryAdminList(codeno, currentpage, name, pagesize, phone, sysorganizationuuid, sysroleuuid):
    """
    分页查询
    :param codeno: 编号(N),string
    :param sysorganizationuuid: 机构uuid(N),string
    :param sysroleuuid: 岗位uuid(N),string
    :param phone: 手机(N),string
    :param name: 姓名(N),string
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 569')
    requesturl = baseUrl + "/api/78dk/web/admin/queryAdminList"
    LOGGER.info("分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["codeNo"] = codeno
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["sysOrganizationUuid"] = sysorganizationuuid
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_addAdmin(idcard, blackid, email, name, password, phone, plaintextpassword, sex, status, sysorganizationuuid, sysroleuuid, username, uuidlist, volk):
    """
    用户-新增
    :param email: 邮箱(Y),string
    :param username: 登录名(Y),string
    :param volk: 民族(Y),string
    :param sex: 性别(Y),string
    :param password: 密码(Y),string
    :param phone: 手机号(Y),string
    :param uuidlist: j用户兼职岗位,array<object>
    :param name: 员工姓名(Y),string
    :param status: 是否有效(Y),string
    :param sysorganizationuuid: 机构uuid(Y),
    :param sysroleuuid: 岗位uuid(Y),
    :param plaintextpassword: 明文密码（Y）,string
    :param idcard: 身份证号,string
    :param blackid: 黑名单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 570')
    requesturl = baseUrl + "/api/78dk/web/admin/addAdmin"
    LOGGER.info("用户-新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["Idcard"] = idcard
    params["blackId"] = blackid
    params["email"] = email
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["plaintextPassword"] = plaintextpassword
    params["sex"] = sex
    params["status"] = status
    params["sysOrganizationUuid"] = sysorganizationuuid
    params["sysRoleUuid"] = sysroleuuid
    params["username"] = username
    params["uuidList"] = uuidlist
    params["volk"] = volk
    LOGGER.info("用户-新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户-新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_resetPw(sysadminuuid):
    """
    重置密码
    :param sysadminuuid: 用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 571')
    requesturl = baseUrl + "/api/78dk/web/admin/resetPw"
    LOGGER.info("重置密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("重置密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重置密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_queryRoleList(codeno, currentpage, pagesize, sysroleuuid):
    """
    分页查询
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param codeno: 岗位编号,string
    :param sysroleuuid: 岗位uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 572')
    requesturl = baseUrl + "/api/78dk/web/role/queryRoleList"
    LOGGER.info("分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["codeNo"] = codeno
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_delAdmin(sysadminuuid):
    """
    用户-删除
    :param sysadminuuid: 用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 573')
    requesturl = baseUrl + "/api/78dk/web/admin/delAdmin"
    LOGGER.info("用户-删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("用户-删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户-删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_querySecondProcess(currentpage, mobile, pagesize, storename, username):
    """
    信审-分页查询搜索查询v1.0.4
    :param username: 客户姓名,string
    :param mobile: 手机号,string
    :param pagesize: 展示条数（Y）,number
    :param currentpage: 当前页数(Y),number
    :param storename: 门店,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 575')
    requesturl = baseUrl + "/api/78dk/web/risk/querySecondProcess"
    LOGGER.info("信审-分页查询搜索查询v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["userName"] = username
    LOGGER.info("信审-分页查询搜索查询v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("信审-分页查询搜索查询v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_updateSecondProcess(uuid):
    """
    信审-返回审核金额
    :param uuid: 订单id（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 576')
    requesturl = baseUrl + "/api/78dk/web/risk/updateSecondProcess"
    LOGGER.info("信审-返回审核金额请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("信审-返回审核金额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("信审-返回审核金额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addFirstProcess(cause, examineamount, examineinfo, examineresult, loanorderuuid, remark):
    """
    评审-保存处理结果
    :param examineresult: 审核结果（Y）,string
    :param examineamount: 审核金额（Y）,number
    :param examineinfo: 评估信息(Y),string
    :param loanorderuuid: 订单uuid(Y),string
    :param remark: 备注,string
    :param cause: 原因,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 577')
    requesturl = baseUrl + "/api/78dk/web/risk/addFirstProcess"
    LOGGER.info("评审-保存处理结果请求地址:【{}】".format(requesturl))
    params = dict()
    params["cause"] = cause
    params["examineAmount"] = examineamount
    params["examineInfo"] = examineinfo
    params["examineResult"] = examineresult
    params["loanOrderUuid"] = loanorderuuid
    params["remark"] = remark
    LOGGER.info("评审-保存处理结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评审-保存处理结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_queryFirstProcess(currentpage, mobile, pagesize, storename, username):
    """
    评审-分页查询搜索查询
    :param storename: 门店(N),
    :param mobile: 手机号(N),
    :param username: 客户姓名(N),
    :param currentpage: 当前页数(Y),number
    :param pagesize: 展示条数（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 578')
    requesturl = baseUrl + "/api/78dk/web/risk/queryFirstProcess"
    LOGGER.info("评审-分页查询搜索查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["userName"] = username
    LOGGER.info("评审-分页查询搜索查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评审-分页查询搜索查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_tree():
    """
    tree
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 579')
    requesturl = baseUrl + "/api/78dk/web/org/tree"
    LOGGER.info("tree请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("tree请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("tree请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_selectRegionLists(cityid):
    """
    区下拉(暂停用)
    :param cityid: id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 580')
    requesturl = baseUrl + "/api/78dk/web/common/selectRegionLists"
    LOGGER.info("区下拉(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["cityId"] = cityid
    LOGGER.info("区下拉(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("区下拉(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_selectCityLists(provinceid):
    """
    市下拉(暂停用)
    :param provinceid: id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 581')
    requesturl = baseUrl + "/api/78dk/web/common/selectCityLists"
    LOGGER.info("市下拉(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["provinceId"] = provinceid
    LOGGER.info("市下拉(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("市下拉(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_selectProvinceLists():
    """
    省下拉(暂停用)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 582')
    requesturl = baseUrl + "/api/78dk/web/common/selectProvinceLists"
    LOGGER.info("省下拉(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("省下拉(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("省下拉(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_delDicType(sysdictionarytypeuuid):
    """
    字典类型-删除(暂停用)
    :param sysdictionarytypeuuid: 字典类型uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 583')
    requesturl = baseUrl + "/api/78dk/web/common/delDicType"
    LOGGER.info("字典类型-删除(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysDictionaryTypeUuid"] = sysdictionarytypeuuid
    LOGGER.info("字典类型-删除(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典类型-删除(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_addDicType(dictlevel, dicttypename):
    """
    字典类型-添加(暂停用)
    :param dictlevel: 级别(Y),number
    :param dicttypename: 名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 584')
    requesturl = baseUrl + "/api/78dk/web/common/addDicType"
    LOGGER.info("字典类型-添加(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictLevel"] = dictlevel
    params["dictTypeName"] = dicttypename
    LOGGER.info("字典类型-添加(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典类型-添加(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_queryDicTypeList(currentpage, dictlevel, dicttypecode, dicttypename, pagesize):
    """
    分页查询(暂停用)
    :param dicttypecode: 编号(N),string
    :param dictlevel: 级别(N),number
    :param pagesize: 每页大小(Y),string
    :param dicttypename: 名称(N),string
    :param currentpage: 当前页(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 585')
    requesturl = baseUrl + "/api/78dk/web/common/queryDicTypeList"
    LOGGER.info("分页查询(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["dictLevel"] = dictlevel
    params["dictTypeCode"] = dicttypecode
    params["dictTypeName"] = dicttypename
    params["pageSize"] = pagesize
    LOGGER.info("分页查询(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分页查询(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_listDictItem(code):
    """
    根据字典类型code查询字典条目列表(暂停用)
    :param code: 字典类型编号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 586')
    requesturl = baseUrl + "/api/78dk/web/common/listDictItem"
    LOGGER.info("根据字典类型code查询字典条目列表(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    LOGGER.info("根据字典类型code查询字典条目列表(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据字典类型code查询字典条目列表(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_delDicItem(uuid):
    """
    字典条目-删除(暂停用)
    :param uuid: 字典条目uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 587')
    requesturl = baseUrl + "/api/78dk/web/common/delDicItem"
    LOGGER.info("字典条目-删除(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("字典条目-删除(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典条目-删除(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_addDicItem(dictcode, dictname, dicttypecode, seq):
    """
    字典条目-添加(暂停用)
    :param dictname: 数据名称(Y),string
    :param seq: 排序(Y),number
    :param dictcode: 数据值(Y),string
    :param dicttypecode: 字典类型code（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 588')
    requesturl = baseUrl + "/api/78dk/web/common/addDicItem"
    LOGGER.info("字典条目-添加(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    params["dictName"] = dictname
    params["dictTypeCode"] = dicttypecode
    params["seq"] = seq
    LOGGER.info("字典条目-添加(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典条目-添加(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_getSysDictItem(uuid):
    """
    字典条目-详情(暂停用)
    :param uuid: 字典条目uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 589')
    requesturl = baseUrl + "/api/78dk/web/common/getSysDictItem"
    LOGGER.info("字典条目-详情(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("字典条目-详情(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典条目-详情(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_queryDicType(sysdictionarytypeuuid):
    """
    字典类型-详情(暂停用)
    :param sysdictionarytypeuuid: uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 590')
    requesturl = baseUrl + "/api/78dk/web/common/queryDicType"
    LOGGER.info("字典类型-详情(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysDictionaryTypeUuid"] = sysdictionarytypeuuid
    LOGGER.info("字典类型-详情(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典类型-详情(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_resource_menu():
    """
    查看可见资源
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 591')
    requesturl = baseUrl + "/api/78dk/web/resource/menu"
    LOGGER.info("查看可见资源请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查看可见资源请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看可见资源请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_client_getClientCredit(clientbaseuuid, type):
    """
    预览客户征信(已废弃)
    :param clientbaseuuid: 客户uuid(Y),string
    :param type: 信息类型：同盾、人法网（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 592')
    requesturl = baseUrl + "/api/78dk/web/client/getClientCredit"
    LOGGER.info("预览客户征信(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    params["type"] = type
    LOGGER.info("预览客户征信(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("预览客户征信(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_previewAppFlie(dictcode, uuid):
    """
    申请资料预览(已废弃)
    :param uuid: 订单uuid（Y）,string
    :param dictcode: code(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 593')
    requesturl = baseUrl + "/api/78dk/web/loan/info/previewAppFlie"
    LOGGER.info("申请资料预览(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    params["uuid"] = uuid
    LOGGER.info("申请资料预览(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请资料预览(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_getCarFile(dictcode, uuid):
    """
    车辆资料预览(已废弃)
    :param uuid: 订单uuid（Y）,string
    :param dictcode: code(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 594')
    requesturl = baseUrl + "/api/78dk/web/loan/info/getCarFile"
    LOGGER.info("车辆资料预览(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    params["uuid"] = uuid
    LOGGER.info("车辆资料预览(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆资料预览(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_acceptLoanOrder(loanuuid, name):
    """
    意向提交
    :param loanuuid: 订单Uuid(Y),string
    :param name: 姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 595')
    requesturl = baseUrl + "/api/78dk/web/loan/common/acceptLoanOrder"
    LOGGER.info("意向提交请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    params["name"] = name
    LOGGER.info("意向提交请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("意向提交请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_lawInfo_getLaw(uuid):
    """
    人法-详情（已作废）
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 596')
    requesturl = baseUrl + "/api/78dk/web/lawInfo/getLaw"
    LOGGER.info("人法-详情（已作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("人法-详情（已作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("人法-详情（已作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_queryStoreLists(merchantuuid):
    """
    根据商户获取门店下拉列表
    :param merchantuuid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 597')
    requesturl = baseUrl + "/api/78dk/web/loan/common/queryStoreLists"
    LOGGER.info("根据商户获取门店下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    LOGGER.info("根据商户获取门店下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户获取门店下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_queryMerchantLists():
    """
    获取商户下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 598')
    requesturl = baseUrl + "/api/78dk/web/loan/common/queryMerchantLists"
    LOGGER.info("获取商户下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取商户下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取商户下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_inItVehicleInfo(loanorderuuid):
    """
    车辆信息初始化(张琦)(已废弃)
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 599')
    requesturl = baseUrl + "/api/78dk/web/loan/info/inItVehicleInfo"
    LOGGER.info("车辆信息初始化(张琦)(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("车辆信息初始化(张琦)(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆信息初始化(张琦)(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_lawInfo_gettd(type, uuid):
    """
    同盾详情查看（已作废）
    :param type: 类型（Y（人法、同盾））,string
    :param uuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 600')
    requesturl = baseUrl + "/api/78dk/web/lawInfo/gettd"
    LOGGER.info("同盾详情查看（已作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    params["uuid"] = uuid
    LOGGER.info("同盾详情查看（已作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾详情查看（已作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_lawInfo_getLawCover(uuid):
    """
    人法-重新拉取（已作废）
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 601')
    requesturl = baseUrl + "/api/78dk/web/lawInfo/getLawCover"
    LOGGER.info("人法-重新拉取（已作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("人法-重新拉取（已作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("人法-重新拉取（已作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_lawInfo_getDtApp(type, uuid):
    """
    同盾-重新拉取（已作废）
    :param uuid: 订单uuid（Y）,string
    :param type: 类型（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 602')
    requesturl = baseUrl + "/api/78dk/web/lawInfo/getDtApp"
    LOGGER.info("同盾-重新拉取（已作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    params["uuid"] = uuid
    LOGGER.info("同盾-重新拉取（已作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾-重新拉取（已作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_inItLoanFile():
    """
    签约资料列表查询（张琦）(已废弃)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 603')
    requesturl = baseUrl + "/api/78dk/web/loan/info/inItLoanFile"
    LOGGER.info("签约资料列表查询（张琦）(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("签约资料列表查询（张琦）(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约资料列表查询（张琦）(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanResult(loanorderuuid):
    """
    审核结果查询（张琦）(已废弃)
    :param loanorderuuid: 订单Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 604')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanResult"
    LOGGER.info("审核结果查询（张琦）(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("审核结果查询（张琦）(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核结果查询（张琦）(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_queryLoanClientLists():
    """
    获提交人下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 605')
    requesturl = baseUrl + "/api/78dk/web/risk/queryLoanClientLists"
    LOGGER.info("获提交人下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获提交人下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获提交人下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getFdd(uuid):
    """
    合同-查看
    :param uuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 606')
    requesturl = baseUrl + "/api/78dk/web/risk/getFdd"
    LOGGER.info("合同-查看请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("合同-查看请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同-查看请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_addLoanBusinessPerson(businessperson, loanuuid):
    """
    保存订单业务员
    :param loanuuid: 订单Uuid(Y),string
    :param businessperson: 业务员(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 607')
    requesturl = baseUrl + "/api/78dk/web/loan/info/addLoanBusinessPerson"
    LOGGER.info("保存订单业务员请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessPerson"] = businessperson
    params["loanUuid"] = loanuuid
    LOGGER.info("保存订单业务员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存订单业务员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getDyw(uuid):
    """
    抵押物清单（已作废）
    :param uuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 608')
    requesturl = baseUrl + "/api/78dk/web/risk/getDyw"
    LOGGER.info("抵押物清单（已作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("抵押物清单（已作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("抵押物清单（已作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getDetail(uuid):
    """
    风控详情页面查看-v1.0.4
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 609')
    requesturl = baseUrl + "/api/78dk/web/risk/getDetail"
    LOGGER.info("风控详情页面查看-v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("风控详情页面查看-v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控详情页面查看-v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_getToken():
    """
    获取token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 610')
    requesturl = baseUrl + "/api/78dk/web/loan/common/getToken"
    LOGGER.info("获取token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanClientInfo(uuid):
    """
    借款人基本信息查看(已废弃)
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 611')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanClientInfo"
    LOGGER.info("借款人基本信息查看(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("借款人基本信息查看(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款人基本信息查看(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_delLoanFile(loaninfofileuuidlist):
    """
    签约资料删除（张琦）
    :param loaninfofileuuidlist: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 612')
    requesturl = baseUrl + "/api/78dk/web/loan/info/delLoanFile"
    LOGGER.info("签约资料删除（张琦）请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanInfoFileUuidList"] = loaninfofileuuidlist
    LOGGER.info("签约资料删除（张琦）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约资料删除（张琦）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_delVehicleProced(vehiclelist):
    """
    车辆手续删除（张琦）
    :param vehiclelist: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 613')
    requesturl = baseUrl + "/api/78dk/web/loan/info/delVehicleProced"
    LOGGER.info("车辆手续删除（张琦）请求地址:【{}】".format(requesturl))
    params = dict()
    params["vehicleList"] = vehiclelist
    LOGGER.info("车辆手续删除（张琦）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆手续删除（张琦）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_updateAdmin(email, password, phone, sex, status, sysadminuuid, uuidlist, volk):
    """
    用户-编辑
    :param sex: 性别(Y),string
    :param uuidlist: 用户岗位组织集合,array<object>
    :param email: 邮箱(Y),string
    :param password: 密码(Y),string
    :param phone: 手机号(Y),string
    :param sysadminuuid: 员工uuid,string
    :param status: 是否有效(Y),string
    :param volk: 民族(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 614')
    requesturl = baseUrl + "/api/78dk/web/admin/updateAdmin"
    LOGGER.info("用户-编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["password"] = password
    params["phone"] = phone
    params["sex"] = sex
    params["status"] = status
    params["sysAdminUuid"] = sysadminuuid
    params["uuidList"] = uuidlist
    params["volk"] = volk
    LOGGER.info("用户-编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户-编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_updateOrg(city, citycontract, name, orgaddress, orgmainuser, orgphone, orgstatus, province, region, sysorganizationuuid):
    """
    组织-编辑
    :param city: 市(Y),string
    :param orgmainuser: 机构负责人(Y),string
    :param orgphone: 机构联系方式(Y),string
    :param name: 机构名称(Y),string
    :param orgstatus: 是否有效(Y),string
    :param province: 省(Y),string
    :param orgaddress: 机构详细地址(Y),string
    :param sysorganizationuuid: uuid(Y),string
    :param region: 区(Y),string
    :param citycontract: 合同城市编号代码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 615')
    requesturl = baseUrl + "/api/78dk/web/org/updateOrg"
    LOGGER.info("组织-编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["cityContract"] = citycontract
    params["name"] = name
    params["orgAddress"] = orgaddress
    params["orgMainUser"] = orgmainuser
    params["orgPhone"] = orgphone
    params["orgStatus"] = orgstatus
    params["province"] = province
    params["region"] = region
    params["sysOrganizationUuid"] = sysorganizationuuid
    LOGGER.info("组织-编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织-编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryVehileAll(loanorderuuid):
    """
    车辆信息查询（张琦）(已废弃)
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 616')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryVehileAll"
    LOGGER.info("车辆信息查询（张琦）(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("车辆信息查询（张琦）(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆信息查询（张琦）(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_dropDown():
    """
    岗位下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 617')
    requesturl = baseUrl + "/api/78dk/web/role/dropDown"
    LOGGER.info("岗位下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("岗位下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("岗位下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_dropDown():
    """
    列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 618')
    requesturl = baseUrl + "/api/78dk/web/org/dropDown"
    LOGGER.info("列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_queryAdmin(sysadminuuid):
    """
    用户-详情
    :param sysadminuuid: 用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 619')
    requesturl = baseUrl + "/api/78dk/web/admin/queryAdmin"
    LOGGER.info("用户-详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("用户-详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户-详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_queryRole(sysroleuuid):
    """
    岗位-详情
    :param sysroleuuid: 岗位uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 620')
    requesturl = baseUrl + "/api/78dk/web/role/queryRole"
    LOGGER.info("岗位-详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("岗位-详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("岗位-详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_vehicleFill(loanorderuuid):
    """
    车辆信息编辑回显(张琦)(已废弃)
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 621')
    requesturl = baseUrl + "/api/78dk/web/loan/info/vehicleFill"
    LOGGER.info("车辆信息编辑回显(张琦)(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("车辆信息编辑回显(张琦)(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆信息编辑回显(张琦)(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_callBack_sum_getReport(authortoken, ictype, userid):
    """
    查询报告数据
    :param userid: 订单userId(Y),string
    :param authortoken: 标识（Y）,string
    :param ictype: 类型（Y）| 0：人法、1：同盾，2：运营商、3：京东、4：淘宝、5支付宝,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 622')
    requesturl = baseUrl + "/api/78dk/callBack/sum/getReport"
    LOGGER.info("查询报告数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["AuthorToken"] = authortoken
    params["icType"] = ictype
    params["userId"] = userid
    LOGGER.info("查询报告数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询报告数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_product_updateProduct(channelfee, firsthalfofthemonth, maxquota, middlehalfofthemonth, minpenaltyfee, minquota, multipleserverfee, name, overduepenaltyrate, penaltyrate, productdetailconfiglist, productdetailuuid, producttype, repaymentdatetype, repaymentmethod, secondhalfofthemonth, serverfee):
    """
    产品-编辑
    :param serverfee: 服务费(Y),number
    :param repaymentmethod: 还款方式(Y)`0`等额本息`先息后本,string
    :param firsthalfofthemonth: 固定还款日 上半月为 每月 10 日,支持可更改（Y）,number
    :param penaltyrate: 罚息日利息（Y）,number
    :param producttype: 产品类型(Y)`(`车抵押贷`车质押贷),string
    :param repaymentdatetype: 账单类型 (`实际账单日`固定账单日)（Y）,string
    :param minquota: 贷款范围_单笔额度下限(Y),number
    :param productdetailconfiglist: 产品期限+利率（Y）,array<object>
    :param secondhalfofthemonth: 固定还款日 下半月 为 每月 21 日,支持可更改.最大28日（Y）,number
    :param middlehalfofthemonth: 固定还款日 中旬 为 每月 11 日,至20日支持可更改(Y),number
    :param channelfee: 渠道费(Y),number
    :param maxquota: 贷款范围_单笔额度上限(Y),number
    :param minpenaltyfee: 最低违约金(Y),number
    :param multipleserverfee: 综合服务费（Y）,number
    :param productdetailuuid: 产品uuid,string
    :param overduepenaltyrate: 逾期违约金罚息比例(Y),number
    :param name: 产品名称（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 623')
    requesturl = baseUrl + "/api/78dk/web/product/updateProduct"
    LOGGER.info("产品-编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelFee"] = channelfee
    params["firstHalfOfTheMonth"] = firsthalfofthemonth
    params["maxQuota"] = maxquota
    params["middleHalfOfTheMonth"] = middlehalfofthemonth
    params["minPenaltyFee"] = minpenaltyfee
    params["minQuota"] = minquota
    params["multipleServerFee"] = multipleserverfee
    params["name"] = name
    params["overduePenaltyRate"] = overduepenaltyrate
    params["penaltyRate"] = penaltyrate
    params["productDetailConfigList"] = productdetailconfiglist
    params["productDetailUuid"] = productdetailuuid
    params["productType"] = producttype
    params["repaymentDateType"] = repaymentdatetype
    params["repaymentMethod"] = repaymentmethod
    params["secondHalfOfTheMonth"] = secondhalfofthemonth
    params["serverFee"] = serverfee
    LOGGER.info("产品-编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品-编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_updateDicType(dictlevel, dicttypename, sysdictionarytypeuuid):
    """
    字典类型-编辑(暂停用)
    :param dictlevel: 级别(Y),number
    :param sysdictionarytypeuuid: uuid(Y),string
    :param dicttypename: 名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 624')
    requesturl = baseUrl + "/api/78dk/web/common/updateDicType"
    LOGGER.info("字典类型-编辑(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictLevel"] = dictlevel
    params["dictTypeName"] = dicttypename
    params["sysDictionaryTypeUuid"] = sysdictionarytypeuuid
    LOGGER.info("字典类型-编辑(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典类型-编辑(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_updateDicItem(dictcode, dictname, seq, sysdictionaryitemuuid):
    """
    字典条目-编辑(暂停用)
    :param dictcode: 数据值(Y),string
    :param dictname: 数据名称(Y),string
    :param sysdictionaryitemuuid: 字典条目uuid(Y),string
    :param seq: 排序(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 625')
    requesturl = baseUrl + "/api/78dk/web/common/updateDicItem"
    LOGGER.info("字典条目-编辑(暂停用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    params["dictName"] = dictname
    params["seq"] = seq
    params["sysDictionaryItemUuid"] = sysdictionaryitemuuid
    LOGGER.info("字典条目-编辑(暂停用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典条目-编辑(暂停用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_callBack_sum_getReportBoolean(uuid):
    """
    判断报告是否有数据
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 626')
    requesturl = baseUrl + "/api/78dk/callBack/sum/getReportBoolean"
    LOGGER.info("判断报告是否有数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("判断报告是否有数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("判断报告是否有数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryVehileBrand(brandname):
    """
    评估师车辆基础信息车辆品牌(张琦)(已废弃)
    :param brandname: 车辆品牌名称,传空查所有(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 627')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryVehileBrand"
    LOGGER.info("评估师车辆基础信息车辆品牌(张琦)(已废弃)请求地址:【{}】".format(requesturl))
    params = dict()
    params["brandName"] = brandname
    LOGGER.info("评估师车辆基础信息车辆品牌(张琦)(已废弃)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评估师车辆基础信息车辆品牌(张琦)(已废弃)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_queryProcessStatusLists():
    """
    获取业务状态列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 628')
    requesturl = baseUrl + "/api/78dk/web/loan/common/queryProcessStatusLists"
    LOGGER.info("获取业务状态列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取业务状态列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取业务状态列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getKey(uuid):
    """
    获取key
    :param uuid: 订单id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 629')
    requesturl = baseUrl + "/api/78dk/web/risk/getKey"
    LOGGER.info("获取key请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("获取key请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取key请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addRemark(remarkloanorder):
    """
    保存备注-v1.0.3
    :param remarkloanorder: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 630')
    requesturl = baseUrl + "/api/78dk/web/risk/addRemark"
    LOGGER.info("保存备注-v1.0.3请求地址:【{}】".format(requesturl))
    params = dict()
    params["remarkLoanorder"] = remarkloanorder
    LOGGER.info("保存备注-v1.0.3请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存备注-v1.0.3请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_queryRemark(uuid):
    """
    查询备注-v1.0.3（废弃加入风控详情接口）
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 631')
    requesturl = baseUrl + "/api/78dk/web/risk/queryRemark"
    LOGGER.info("查询备注-v1.0.3（废弃加入风控详情接口）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("查询备注-v1.0.3（废弃加入风控详情接口）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询备注-v1.0.3（废弃加入风控详情接口）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addWeft(latitude, longitude, type, uuid):
    """
    保存经纬度-v1.0.3
    :param uuid: 订单uuid(Y),string
    :param type: 类型（`0`客户信息`1`单位信息）(Y),string
    :param longitude: 经度(Y),string
    :param latitude: 纬度(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 632')
    requesturl = baseUrl + "/api/78dk/web/risk/addWeft"
    LOGGER.info("保存经纬度-v1.0.3请求地址:【{}】".format(requesturl))
    params = dict()
    params["latitude"] = latitude
    params["longitude"] = longitude
    params["type"] = type
    params["uuid"] = uuid
    LOGGER.info("保存经纬度-v1.0.3请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存经纬度-v1.0.3请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_updateSalesman(loanfirstvo):
    """
    更新客服申请详情页面
    :param loanfirstvo: 客服修改,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 633')
    requesturl = baseUrl + "/api/78dk/web/loan/info/updateSalesman"
    LOGGER.info("更新客服申请详情页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["LoanfirstVO"] = loanfirstvo
    LOGGER.info("更新客服申请详情页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新客服申请详情页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getMailList(uuid):
    """
    获取通讯录-v1.0.3
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 634')
    requesturl = baseUrl + "/api/78dk/web/risk/getMailList"
    LOGGER.info("获取通讯录-v1.0.3请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("获取通讯录-v1.0.3请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取通讯录-v1.0.3请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getPgsDetail(uuid):
    """
    评估师、客服详情页面查看-v1.0.4
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 635')
    requesturl = baseUrl + "/api/78dk/web/risk/getPgsDetail"
    LOGGER.info("评估师、客服详情页面查看-v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("评估师、客服详情页面查看-v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评估师、客服详情页面查看-v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_delRemark(type, uuid):
    """
    删除备注-v1.0.3
    :param type: 类型（`0`客户`1`订单`2`联系人`3`文案）(Y),string
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 636')
    requesturl = baseUrl + "/api/78dk/web/risk/delRemark"
    LOGGER.info("删除备注-v1.0.3请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    params["uuid"] = uuid
    LOGGER.info("删除备注-v1.0.3请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除备注-v1.0.3请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_delRole(sysroleuuid):
    """
    岗位-删除
    :param sysroleuuid: 岗位uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 637')
    requesturl = baseUrl + "/api/78dk/web/role/delRole"
    LOGGER.info("岗位-删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("岗位-删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("岗位-删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_addRole(codeno, name, seq):
    """
    岗位-新增
    :param seq: 排序,number
    :param name: 岗位名称,string
    :param codeno: 岗位编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 638')
    requesturl = baseUrl + "/api/78dk/web/role/addRole"
    LOGGER.info("岗位-新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["codeNo"] = codeno
    params["name"] = name
    params["seq"] = seq
    LOGGER.info("岗位-新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("岗位-新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_role_updateRole(codeno, name, seq, sysroleuuid):
    """
    岗位-编辑
    :param seq: 排序,number
    :param codeno: 岗位编号,string
    :param sysroleuuid: 岗位uuid,string
    :param name: 岗位名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 639')
    requesturl = baseUrl + "/api/78dk/web/role/updateRole"
    LOGGER.info("岗位-编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["codeNo"] = codeno
    params["name"] = name
    params["seq"] = seq
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("岗位-编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("岗位-编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_getReport(authortoken, ictype, userid):
    """
    查询报告数据（v1.0.4）
    :param ictype: 类型（Y）| 0：人法、1：同盾，2：运营商、3：京东、4：淘宝、5支付宝,string
    :param authortoken: 标识（Y）,string
    :param userid: 订单userId(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 640')
    requesturl = baseUrl + "/api/78dk/web/sum/getReport"
    LOGGER.info("查询报告数据（v1.0.4）请求地址:【{}】".format(requesturl))
    params = dict()
    params["AuthorToken"] = authortoken
    params["icType"] = ictype
    params["userId"] = userid
    LOGGER.info("查询报告数据（v1.0.4）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询报告数据（v1.0.4）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_getReportBoolean(uuid):
    """
    判断报告是否有数据
    :param uuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 641')
    requesturl = baseUrl + "/api/78dk/web/sum/getReportBoolean"
    LOGGER.info("判断报告是否有数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("判断报告是否有数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("判断报告是否有数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_print_printLink(bigendate, enddate, loanamount, ordermainstate, storename, usrename):
    """
    报表导出
    :param bigendate: 开始时间,string
    :param enddate: 结束时间,string
    :param loanamount: 放款金额,number
    :param ordermainstate: 订单状态（SHJDZS02 已通过  SHJDXS01 已取消 SHJDCL01处理中）,string
    :param storename: 商户,string
    :param usrename: 用户名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 642')
    requesturl = baseUrl + "/api/78dk/web/print/printLink"
    LOGGER.info("报表导出请求地址:【{}】".format(requesturl))
    params = dict()
    params["bigenDate"] = bigendate
    params["endDate"] = enddate
    params["loanAmount"] = loanamount
    params["orderMainState"] = ordermainstate
    params["storeName"] = storename
    params["usreName"] = usrename
    LOGGER.info("报表导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报表导出请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_print_printPage(bigendate, currentpage, enddate, loanamount, ordermainstate, pagesize, storename, usrename):
    """
    报表导出分页
    :param bigendate: 开始时间,string
    :param currentpage: 当前页(Y),number
    :param enddate: 结束时间,string
    :param loanamount: 放款金额,string
    :param ordermainstate: 订单状态订单状态（SHJDZS02 已通过  SHJDXS01 已取消 SHJDCL01处理中）,string
    :param pagesize: 页面条数（Y）,number
    :param storename: 门店名称(北京1店"FQBJ001 "成都武侯1店"FQSC001"内蒙1店"FQNMG001"),string
    :param usrename: 客户姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 643')
    requesturl = baseUrl + "/api/78dk/web/print/printPage"
    LOGGER.info("报表导出分页请求地址:【{}】".format(requesturl))
    params = dict()
    params["bigenDate"] = bigendate
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["loanAmount"] = loanamount
    params["orderMainState"] = ordermainstate
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["usreName"] = usrename
    LOGGER.info("报表导出分页请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报表导出分页请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_queryOrgMd():
    """
    门店获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 644')
    requesturl = baseUrl + "/api/78dk/web/org/queryOrgMd"
    LOGGER.info("门店获取请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("门店获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店获取请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_finance_financePage(begindate, beginloanamount, contractno, currentpage, enddate, endloanamount, ordermainstate, orderno, pagesize, storename, username, years):
    """
    财务管理分页
    :param begindate: 单据时间（前者）,string
    :param beginloanamount: 放款金额（前者）,number
    :param contractno: 合同编号,string
    :param currentpage: 页数(Y),number
    :param enddate: 单据时间（后者）,string
    :param endloanamount: 放款金额（后者）,number
    :param ordermainstate: 单据状态单据状态（0待处理 1 通过）,string
    :param orderno: 单据编号,string
    :param pagesize: 当前页条数(Y),number
    :param storename: 门店,string
    :param username: 客户名称,string
    :param years: 年度,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 645')
    requesturl = baseUrl + "/api/78dk/web/finance/financePage"
    LOGGER.info("财务管理分页请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["beginLoanAmount"] = beginloanamount
    params["contractNo"] = contractno
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["endLoanAmount"] = endloanamount
    params["orderMainState"] = ordermainstate
    params["orderNo"] = orderno
    params["pageSize"] = pagesize
    params["storeName"] = storename
    params["userName"] = username
    params["years"] = years
    LOGGER.info("财务管理分页请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务管理分页请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_finance_queryLoanFinance(uuid):
    """
    财务管理详情
    :param uuid: 财务管理uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 646')
    requesturl = baseUrl + "/api/78dk/web/finance/queryLoanFinance"
    LOGGER.info("财务管理详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("财务管理详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务管理详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_finance_addLoanFinance(bankbranch, loantype, moenyuse, uuid):
    """
    财务详情保存
    :param bankbranch: 所属支行,string
    :param loantype: 放款方式（`1`公司转账`2`网银支付`3`代付）,string
    :param moenyuse: 汇款用途（`0`融资租赁`1`贷款）,string
    :param uuid: 财务uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 647')
    requesturl = baseUrl + "/api/78dk/web/finance/addLoanFinance"
    LOGGER.info("财务详情保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankBranch"] = bankbranch
    params["loanType"] = loantype
    params["moenyUse"] = moenyuse
    params["uuid"] = uuid
    LOGGER.info("财务详情保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务详情保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getRiskStrategyResult(loanorderuuid):
    """
    风控机审列表-v1.0.4
    :param loanorderuuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 648')
    requesturl = baseUrl + "/api/78dk/web/risk/getRiskStrategyResult"
    LOGGER.info("风控机审列表-v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("风控机审列表-v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控机审列表-v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getRiskScoreResult(loanorderuuid):
    """
    风控评分列表-v1.0.4
    :param loanorderuuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 649')
    requesturl = baseUrl + "/api/78dk/web/risk/getRiskScoreResult"
    LOGGER.info("风控评分列表-v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("风控评分列表-v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控评分列表-v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_queryNoticeList(currentpage, issue, pagesize, title, type):
    """
    公告列表
    :param currentpage: 当前页(Y),number
    :param type: 类型（N）,string
    :param pagesize: 每页大小(Y),number
    :param title: 标题（N）,string
    :param issue: 发布状态（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 650')
    requesturl = baseUrl + "/api/78dk/web/notice/queryNoticeList"
    LOGGER.info("公告列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["issue"] = issue
    params["pageSize"] = pagesize
    params["title"] = title
    params["type"] = type
    LOGGER.info("公告列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_addNotice(content, issue, noticeuuid, sysrecipientlist, title, type):
    """
    公告新增
    :param title: 标题(Y),string
    :param type: 类型(Y),string
    :param content: 公告类容（Y）,string
    :param issue: 自动发布(Y),string
    :param sysrecipientlist: 数据列表,array<object>
    :param noticeuuid: 公告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 651')
    requesturl = baseUrl + "/api/78dk/web/notice/addNotice"
    LOGGER.info("公告新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["content"] = content
    params["issue"] = issue
    params["noticeUuid"] = noticeuuid
    params["sysRecipientList"] = sysrecipientlist
    params["title"] = title
    params["type"] = type
    LOGGER.info("公告新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_rfw(uuid):
    """
    人法主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 652')
    requesturl = baseUrl + "/api/78dk/web/sum/rfw"
    LOGGER.info("人法主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("人法主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("人法主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_alipay(uuid):
    """
    alipay主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 653')
    requesturl = baseUrl + "/api/78dk/web/sum/alipay"
    LOGGER.info("alipay主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("alipay主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("alipay主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_jd(uuid):
    """
    京东主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 654')
    requesturl = baseUrl + "/api/78dk/web/sum/jd"
    LOGGER.info("京东主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("京东主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("京东主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_td(uuid):
    """
    同盾主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 655')
    requesturl = baseUrl + "/api/78dk/web/sum/td"
    LOGGER.info("同盾主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("同盾主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_taobao(uuid):
    """
    淘宝主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 656')
    requesturl = baseUrl + "/api/78dk/web/sum/taobao"
    LOGGER.info("淘宝主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("淘宝主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sum_carrier(uuid):
    """
    运营商主动触发
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 657')
    requesturl = baseUrl + "/api/78dk/web/sum/carrier"
    LOGGER.info("运营商主动触发请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("运营商主动触发请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营商主动触发请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_queryControllerList(contractno, mobile, username):
    """
    合同查询
    :param contractno: 合同编号,string
    :param mobile: 手机号,string
    :param username: 客户姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 658')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/queryControllerList"
    LOGGER.info("合同查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNo"] = contractno
    params["mobile"] = mobile
    params["userName"] = username
    LOGGER.info("合同查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getBreakRuleList(loanorderuuid):
    """
    查询违章列表
    :param loanorderuuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 659')
    requesturl = baseUrl + "/api/78dk/web/risk/getBreakRuleList"
    LOGGER.info("查询违章列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("查询违章列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询违章列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_detailOrg(sysorganizationuuid):
    """
    组织机构明细
    :param sysorganizationuuid: 机构uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 660')
    requesturl = baseUrl + "/api/78dk/web/org/detailOrg"
    LOGGER.info("组织机构明细请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysOrganizationUuid"] = sysorganizationuuid
    LOGGER.info("组织机构明细请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织机构明细请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_getRoueList(orguuid):
    """
    根据机构uuid获取岗位
    :param orguuid: 机构uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 661')
    requesturl = baseUrl + "/api/78dk/web/admin/getRoueList"
    LOGGER.info("根据机构uuid获取岗位请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgUuid"] = orguuid
    LOGGER.info("根据机构uuid获取岗位请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据机构uuid获取岗位请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_delNotice(noticeuuid):
    """
    公告删除
    :param noticeuuid: 公告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 662')
    requesturl = baseUrl + "/api/78dk/web/notice/delNotice"
    LOGGER.info("公告删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["noticeUuid"] = noticeuuid
    LOGGER.info("公告删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_updateIssueNotice(noticeuuid):
    """
    公告发布
    :param noticeuuid: 公告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 663')
    requesturl = baseUrl + "/api/78dk/web/notice/updateIssueNotice"
    LOGGER.info("公告发布请求地址:【{}】".format(requesturl))
    params = dict()
    params["noticeUuid"] = noticeuuid
    LOGGER.info("公告发布请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告发布请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_newNotice_newNotice():
    """
    消息通知
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 664')
    requesturl = baseUrl + "/api/78dk/web/newNotice/newNotice"
    LOGGER.info("消息通知请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("消息通知请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("消息通知请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_newNotice_queryNewNotice(uuid):
    """
    消息查看
    :param uuid: 消息uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 665')
    requesturl = baseUrl + "/api/78dk/web/newNotice/queryNewNotice"
    LOGGER.info("消息查看请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("消息查看请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("消息查看请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_info_queryLoanCheckResult(loanorderuuid):
    """
    审核意见列表查询Page
    :param loanorderuuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 666')
    requesturl = baseUrl + "/api/78dk/web/loan/info/queryLoanCheckResult"
    LOGGER.info("审核意见列表查询Page请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("审核意见列表查询Page请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核意见列表查询Page请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_org_getOrgAdminTree(name):
    """
    机构人员tree
    :param name: 用户名（传空查询全部）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 667')
    requesturl = baseUrl + "/api/78dk/web/org/getOrgAdminTree"
    LOGGER.info("机构人员tree请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    LOGGER.info("机构人员tree请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构人员tree请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_delSoldNotice(noticeuuid):
    """
    公告下架
    :param noticeuuid: 公告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 668')
    requesturl = baseUrl + "/api/78dk/web/notice/delSoldNotice"
    LOGGER.info("公告下架请求地址:【{}】".format(requesturl))
    params = dict()
    params["noticeUuid"] = noticeuuid
    LOGGER.info("公告下架请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告下架请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_queryHomePageNoticeList(currentpage, pagesize, title, type):
    """
    公告首页列表
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param title: 标题,string
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 669')
    requesturl = baseUrl + "/api/78dk/web/notice/queryHomePageNoticeList"
    LOGGER.info("公告首页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["title"] = title
    params["type"] = type
    LOGGER.info("公告首页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告首页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_queryOrderStateList(currentpage, mobile, ordermainstate, orderno, pagesize, username):
    """
    订单状态实时查询
    :param currentpage: 当前页（Y）,number
    :param mobile: 手机号(N),string
    :param ordermainstate: 订单状态(N),string
    :param orderno: 订单编号(N),string
    :param pagesize: 每页大小（Y）,number
    :param username: 姓名（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 670')
    requesturl = baseUrl + "/api/78dk/web/notice/queryOrderStateList"
    LOGGER.info("订单状态实时查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["orderMainState"] = ordermainstate
    params["orderNo"] = orderno
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("订单状态实时查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单状态实时查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_notice_queryNoticeInfo(noticeuuid):
    """
    公告详情
    :param noticeuuid: 公告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 671')
    requesturl = baseUrl + "/api/78dk/web/notice/queryNoticeInfo"
    LOGGER.info("公告详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["noticeUuid"] = noticeuuid
    LOGGER.info("公告详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("公告详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_approved(currentpage, loanorderuuid, pagesize):
    """
    审核记录
    :param currentpage: 当前页数(Y),string
    :param loanorderuuid: 订单Uuid(Y),string
    :param pagesize: 每页大小(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 672')
    requesturl = baseUrl + "/api/78dk/web/risk/approved"
    LOGGER.info("审核记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["loanOrderUuid"] = loanorderuuid
    params["pageSize"] = pagesize
    LOGGER.info("审核记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_clientRecommendation_clientRecommendationPage(currentpage, fromtime, pagesize, recommendedphone, referrerphone, totime):
    """
    推荐人管理
    :param recommendedphone: 被推荐人手机号,string
    :param totime: 查询结束日期,string
    :param referrerphone: 推荐人手机号,string
    :param fromtime: 查询开始日期,string
    :param currentpage: 当前页码,number
    :param pagesize: 单页记录数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1556')
    requesturl = baseUrl + "/api/78dk/web/clientRecommendation/clientRecommendationPage"
    LOGGER.info("推荐人管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["fromTime"] = fromtime
    params["pageSize"] = pagesize
    params["recommendedPhone"] = recommendedphone
    params["referrerPhone"] = referrerphone
    params["toTime"] = totime
    LOGGER.info("推荐人管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("推荐人管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addProtocolMessage(clientcards, clientjointborrower):
    """
    审核信息详情-借款协议拟定添加（添加，修改用一个接口）
    :param clientcards: 用户银行卡信息,object
    :param clientjointborrower: 共借人信息,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1557')
    requesturl = baseUrl + "/api/78dk/web/risk/addProtocolMessage"
    LOGGER.info("审核信息详情-借款协议拟定添加（添加，修改用一个接口）请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientCards"] = clientcards
    params["clientJointBorrower"] = clientjointborrower
    LOGGER.info("审核信息详情-借款协议拟定添加（添加，修改用一个接口）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核信息详情-借款协议拟定添加（添加，修改用一个接口）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_getRecommendation(storeuuid):
    """
    查询业务员
    :param storeuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1598')
    requesturl = baseUrl + "/api/78dk/web/risk/getRecommendation"
    LOGGER.info("查询业务员请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    LOGGER.info("查询业务员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询业务员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_creatcontractController(loanoderuuid):
    """
    合同生成
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1604')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/creatcontractController"
    LOGGER.info("合同生成请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("合同生成请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同生成请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_querycontractControlle(loanoderuuid):
    """
    合同查询
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1605')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/querycontractControlle"
    LOGGER.info("合同查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("合同查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_hkglfwsms(loanoderuuid):
    """
    还款管理服务说明
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1606')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/hkglfwsms"
    LOGGER.info("还款管理服务说明请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("还款管理服务说明请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款管理服务说明请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_wtkksqs(loanoderuuid):
    """
    委托扣款授权书
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1607')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/wtkksqs"
    LOGGER.info("委托扣款授权书请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("委托扣款授权书请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("委托扣款授权书请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_fwxy(loanoderuuid):
    """
    服务协议
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1608')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/fwxy"
    LOGGER.info("服务协议请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("服务协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("服务协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_dywqd(loanoderuuid):
    """
    抵押物清单
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1609')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/dywqd"
    LOGGER.info("抵押物清单请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("抵押物清单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("抵押物清单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_st(loanoderuuid):
    """
    收条
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1610')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/st"
    LOGGER.info("收条请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("收条请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("收条请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_esclmmht(loanoderuuid):
    """
    车辆买卖合同
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1611')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/esclmmht"
    LOGGER.info("车辆买卖合同请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("车辆买卖合同请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆买卖合同请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_grzhktxy(loanoderuuid):
    """
    个人账号开通协议
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1612')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/grzhktxy"
    LOGGER.info("个人账号开通协议请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("个人账号开通协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("个人账号开通协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_jkxy(loanoderuuid):
    """
    借款协议
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1613')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/jkxy"
    LOGGER.info("借款协议请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("借款协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_xxzxglfwxy(loanoderuuid):
    """
    信息咨询管理服务协议
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1614')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/xxzxglfwxy"
    LOGGER.info("信息咨询管理服务协议请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("信息咨询管理服务协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("信息咨询管理服务协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_appropriationController(loanoderuuid):
    """
    批款通知单
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1615')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/appropriationController"
    LOGGER.info("批款通知单请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("批款通知单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("批款通知单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_querycontractController(loanoderuuid):
    """
    合同查询
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1617')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/querycontractController"
    LOGGER.info("合同查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("合同查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_printcontractController_wxts(loanoderuuid):
    """
    温馨提示
    :param loanoderuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1618')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/printcontractController/wxts"
    LOGGER.info("温馨提示请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOderUuid"] = loanoderuuid
    LOGGER.info("温馨提示请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("温馨提示请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_planandpicture(contractno):
    """
    金融还款计划发标照片面审报告
    :param contractno: 合同号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1648')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/planandpicture"
    LOGGER.info("金融还款计划发标照片面审报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNO"] = contractno
    LOGGER.info("金融还款计划发标照片面审报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("金融还款计划发标照片面审报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_backLoanOrder(loanuuid):
    """
    客服回退风控信审
    :param loanuuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1697')
    requesturl = baseUrl + "/api/78dk/web/loan/common/backLoanOrder"
    LOGGER.info("客服回退风控信审请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("客服回退风控信审请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客服回退风控信审请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_baihangcreditApplyController_baihangaiche(applyamount, customtype, guaranteetype, idcard, loanpurpose, name, phone, queryreason):
    """
    百行报告
    :param applyamount: 申请金额,string
    :param customtype: 99,number
    :param guaranteetype: 2,number
    :param idcard: 身份证,string
    :param loanpurpose: 99,number
    :param name: 姓名,string
    :param phone: 手机号,string
    :param queryreason: 1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1760')
    requesturl = baseUrl + "/baihangcreditApplyController/baihangaiche"
    LOGGER.info("百行报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyamount"] = applyamount
    params["customtype"] = customtype
    params["guaranteetype"] = guaranteetype
    params["idcard"] = idcard
    params["loanpurpose"] = loanpurpose
    params["name"] = name
    params["phone"] = phone
    params["queryreason"] = queryreason
    LOGGER.info("百行报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("百行报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_loanContract_baihangaiche(applyamount, idcard, name, phone):
    """
    百行报告
    :param applyamount: 申请金额,string
    :param idcard: 身份证,string
    :param name: 姓名,string
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1761')
    requesturl = baseUrl + "/api/78dk/web/loan/loanContract/baihangaiche"
    LOGGER.info("百行报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyamount"] = applyamount
    params["idcard"] = idcard
    params["name"] = name
    params["phone"] = phone
    LOGGER.info("百行报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("百行报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_risk_addSecondProcess(examineamount, examineinfo, examineresult, loanorderuuid, remark):
    """
    信审-保存处理结果
    :param loanorderuuid: 订单uuid(Y),string
    :param remark: 备注,string
    :param examineamount: 放款金额(Y),number
    :param examineinfo: 项目风险等级（Y）,string
    :param examineresult: 审核结果(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1792')
    requesturl = baseUrl + "/api/78dk/web/risk/addSecondProcess"
    LOGGER.info("信审-保存处理结果请求地址:【{}】".format(requesturl))
    params = dict()
    params["examineAmount"] = examineamount
    params["examineInfo"] = examineinfo
    params["examineResult"] = examineresult
    params["loanOrderUuid"] = loanorderuuid
    params["remark"] = remark
    LOGGER.info("信审-保存处理结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("信审-保存处理结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_base_LoanworkOrder(idcard, mobile, orderno, username):
    """
    工单查询
    :param idcard: 身份证号（N）,string
    :param mobile: 手机号（N）,string
    :param orderno: 订单号（N）,string
    :param username: 用户名（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1800')
    requesturl = baseUrl + "/api/78dk/web/loan/base/LoanworkOrder"
    LOGGER.info("工单查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["idCard"] = idcard
    params["mobile"] = mobile
    params["orderNo"] = orderno
    params["userName"] = username
    LOGGER.info("工单查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("工单查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin__black(id, idcard, state):
    """
    黑名单增删查
    :param id: 删除时必传,number
    :param idcard: 新增查询时必传,string
    :param state: 0新增  1删除,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1802')
    requesturl = baseUrl + "/api/78dk/web/admin//black"
    LOGGER.info("黑名单增删查请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["idcard"] = idcard
    params["state"] = state
    LOGGER.info("黑名单增删查请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("黑名单增删查请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_selectLimitPage(currentpage, pagesize, storename):
    """
    风控限额查询
    :param currentpage: 当前页,string
    :param storename: 门店名称,string
    :param pagesize: 每页数量,string
    :param : ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2163')
    requesturl = baseUrl + "/api/78dk/web/admin/selectLimitPage"
    LOGGER.info("风控限额查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["storename"] = storename
    LOGGER.info("风控限额查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控限额查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin__selectLimit():
    """
    客服限额查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2164')
    requesturl = baseUrl + "/api/78dk/web/admin//selectLimit"
    LOGGER.info("客服限额查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("客服限额查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客服限额查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_selectLimit(id):
    """
    限额修改查询
    :param id: 限额id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2165')
    requesturl = baseUrl + "/api/78dk/web/admin/selectLimit"
    LOGGER.info("限额修改查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("限额修改查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("限额修改查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_addLimit(cycle, limit, storename, twentyfourlimit, valid):
    """
    新增限额
    :param cycle: 周期 0 天 1 周 2 月,number
    :param limit: 12期 限额,number
    :param storename: 门店名称,string
    :param twentyfourlimit: 24期限额,number
    :param valid: 0 有效 1无效,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2166')
    requesturl = baseUrl + "/api/78dk/web/admin/addLimit"
    LOGGER.info("新增限额请求地址:【{}】".format(requesturl))
    params = dict()
    params["cycle"] = cycle
    params["limit"] = limit
    params["storename"] = storename
    params["twentyfourlimit"] = twentyfourlimit
    params["valid"] = valid
    LOGGER.info("新增限额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增限额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_admin_updateLimit(cycle, id, limit, storename, twentyfourlimit, valid):
    """
    修改限额
    :param id: 限额表ID,number
    :param cycle: 周期 0 天 1 周 2 月,number
    :param limit: 12期 限额,number
    :param storename: 门店名称,string
    :param twentyfourlimit: 24期限额,number
    :param valid: 0 有效 1无效,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2167')
    requesturl = baseUrl + "/api/78dk/web/admin/updateLimit"
    LOGGER.info("修改限额请求地址:【{}】".format(requesturl))
    params = dict()
    params["cycle"] = cycle
    params["id"] = id
    params["limit"] = limit
    params["storename"] = storename
    params["twentyfourlimit"] = twentyfourlimit
    params["valid"] = valid
    LOGGER.info("修改限额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改限额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_backLoanOrderToPGS(loanuuid):
    """
    借款申请退回
    :param loanuuid: loanUuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2169')
    requesturl = baseUrl + "/api/78dk/web/loan/common/backLoanOrderToPGS"
    LOGGER.info("借款申请退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("借款申请退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款申请退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_acceptKFLoanOrder(loanuuid):
    """
    借款申请受理
    :param loanuuid: loanUuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2170')
    requesturl = baseUrl + "/api/78dk/web/loan/common/acceptKFLoanOrder"
    LOGGER.info("借款申请受理请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("借款申请受理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款申请受理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_common_backLoanOrderToservice(loanuuid):
    """
    分公司评估师退回
    :param loanuuid: loanUuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2171')
    requesturl = baseUrl + "/api/78dk/web/loan/common/backLoanOrderToservice"
    LOGGER.info("分公司评估师退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanUuid"] = loanuuid
    LOGGER.info("分公司评估师退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分公司评估师退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


