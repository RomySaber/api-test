#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : WebAction.py
@desc       : 项目：financeCloud 模块：web 接口方法封装
"""

from financeCloud.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('web_apiURL', 'financeCloud')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_web_login()


def test_accountbill_firstcheck_queryAccountLogs(accountid):
    """
    查询结算操作日志记录
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3195')
    requesturl = baseUrl + "/accountbill/firstcheck/queryAccountLogs"
    LOGGER.info("查询结算操作日志记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算操作日志记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算操作日志记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_firstcheck_queryfirstSettleList(accountamount, accountbillid, accountdate, accountnumber, accountnumbertotal, auditmoney, cashsource, cashsourcename, currentpage, discount, firstpaymentproportion, merchantdiscountamount, orderid, orderno, pagesize, partnerallname, stages, statusaccountfinalcheck, statusaccountfinalcheckname, statusaccountfirstcheck, statusaccountfirstcheckname, sumstrokecount, sumtotalmoney, username):
    """
    初审搜索分页列表
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :param orderid: 订单id,number
    :param accountbillid: 结算id,number
    :param accountdate: 应结算日期,string
    :param orderno: 订单号,string
    :param partnerallname:  商户名称,string
    :param cashsource: 放款渠道:  0启发，1香江,number
    :param cashsourcename: 放款渠道翻译成的中文,string
    :param username: 客户姓名,string
    :param auditmoney: 订单审核金额,number
    :param stages: 分期数,number
    :param merchantdiscountamount: 商户贴息金额,number
    :param firstpaymentproportion: 首打款比例,string
    :param accountnumber: 结算批次,number
    :param accountnumbertotal: 总结算批次,number
    :param accountamount: 结算金额,number
    :param statusaccountfirstcheck: 结算初审状态:status_account_firstcheck_unknown, 未开始  status_account_firstcheck_pending, 待提交  status_account_firstcheck_pass 通过,string
    :param statusaccountfinalcheck: 结算终审状态:status_account_finalcheck_unknown, status_account_finalcheck_pending,待提交  status_account_finalcheck_pass ,通过,string
    :param statusaccountfirstcheckname: 初审结算状态的中文名称,string
    :param statusaccountfinalcheckname: 终审结算状态的中文名称,string
    :param discount: 商户贴息率,string
    :param sumstrokecount: ,number
    :param sumtotalmoney: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3196')
    requesturl = baseUrl + "/accountbill/firstcheck/queryfirstSettleList"
    LOGGER.info("初审搜索分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountAmount"] = accountamount
    params["accountBillId"] = accountbillid
    params["accountDate"] = accountdate
    params["accountNumber"] = accountnumber
    params["accountNumberTotal"] = accountnumbertotal
    params["auditMoney"] = auditmoney
    params["cashSource"] = cashsource
    params["cashSourceName"] = cashsourcename
    params["currentPage"] = currentpage
    params["discount"] = discount
    params["firstPaymentProportion"] = firstpaymentproportion
    params["merchantDiscountAmount"] = merchantdiscountamount
    params["orderId"] = orderid
    params["orderNo"] = orderno
    params["pageSize"] = pagesize
    params["partnerAllName"] = partnerallname
    params["stages"] = stages
    params["statusAccountFinalcheck"] = statusaccountfinalcheck
    params["statusAccountFinalcheckName"] = statusaccountfinalcheckname
    params["statusAccountFirstcheck"] = statusaccountfirstcheck
    params["statusAccountFirstcheckName"] = statusaccountfirstcheckname
    params["sumStrokeCount"] = sumstrokecount
    params["sumTotalMoney"] = sumtotalmoney
    params["userName"] = username
    LOGGER.info("初审搜索分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审搜索分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_firstcheck_queryFirstOrderSettleDetil(orderid):
    """
    初审的订单结算详情
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3197')
    requesturl = baseUrl + "/accountbill/firstcheck/queryFirstOrderSettleDetil"
    LOGGER.info("初审的订单结算详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("初审的订单结算详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审的订单结算详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_firstcheck_saveAllPass(list, sumstrokecount, sumtotalmoney, type):
    """
    初审、终审批量通过
    :param list: 订单id列表,array
    :param sumstrokecount: 通过笔数,number
    :param sumtotalmoney:  通过金额,number
    :param type: 通过的类型： firstBatchPass: 初审通过    finaBatchPass  :终审通过,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3198')
    requesturl = baseUrl + "/accountbill/firstcheck/saveAllPass"
    LOGGER.info("初审、终审批量通过请求地址:【{}】".format(requesturl))
    params = dict()
    params["list"] = list
    params["sumStrokeCount"] = sumstrokecount
    params["sumTotalMoney"] = sumtotalmoney
    params["type"] = type
    LOGGER.info("初审、终审批量通过请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审、终审批量通过请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_firstcheck_firstOncePassOrBack(accountbillid, createdid, detaillogid, id, logremark, logresult, logtime, logtype, orderid, passorback):
    """
    初审详情中单条通过或则退回
    :param id: ,number
    :param orderid: 订单id,number
    :param accountbillid:  结算账单id,number
    :param logtime:  日志时间,string
    :param logtype: 日志类型,string
    :param logresult: 日志结果,string
    :param logremark: 日志备注,string
    :param createdid: 日志操作人员,number
    :param detaillogid: 日志详情id,number
    :param passorback: 通过还是退回: pass:通过   back:退回,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3199')
    requesturl = baseUrl + "/accountbill/firstcheck/firstOncePassOrBack"
    LOGGER.info("初审详情中单条通过或则退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountBillId"] = accountbillid
    params["createdId"] = createdid
    params["detailLogId"] = detaillogid
    params["id"] = id
    params["logRemark"] = logremark
    params["logResult"] = logresult
    params["logTime"] = logtime
    params["logType"] = logtype
    params["orderId"] = orderid
    params["passOrBack"] = passorback
    LOGGER.info("初审详情中单条通过或则退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审详情中单条通过或则退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_firstcheck_viewSettlementBill(orderid):
    """
    结算管理-用户账单
    :param orderid: orderId,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3200')
    requesturl = baseUrl + "/accountbill/firstcheck/viewSettlementBill"
    LOGGER.info("结算管理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("结算管理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结算管理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_accounthistory_queryAccountLogs(accountid):
    """
    查询结算操作日志记录
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3201')
    requesturl = baseUrl + "/accountbill/accounthistory/queryAccountLogs"
    LOGGER.info("查询结算操作日志记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算操作日志记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算操作日志记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_accounthistory_viewSettlementBill(orderid):
    """
    结算管理-用户账单
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3202')
    requesturl = baseUrl + "/accountbill/accounthistory/viewSettlementBill"
    LOGGER.info("结算管理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("结算管理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结算管理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_accounthistory_queryHistoryList(accountid):
    """
    查询历史结算列表
    :param accountid: accountId,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3203')
    requesturl = baseUrl + "/accountbill/accounthistory/queryHistoryList"
    LOGGER.info("查询历史结算列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询历史结算列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询历史结算列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_accounthistory_export(accountid, response):
    """
    导出列表
    :param response: response,object
    :param accountid: accountId,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3204')
    requesturl = baseUrl + "/accountbill/accounthistory/export"
    LOGGER.info("导出列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    params["response"] = response
    LOGGER.info("导出列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_queryAccountLogs(accountid):
    """
    查询结算操作日志记录
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3205')
    requesturl = baseUrl + "/accountbill/finalcheck/queryAccountLogs"
    LOGGER.info("查询结算操作日志记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算操作日志记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算操作日志记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_viewSettlementBill(orderid):
    """
    结算管理-用户账单
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3206')
    requesturl = baseUrl + "/accountbill/finalcheck/viewSettlementBill"
    LOGGER.info("结算管理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("结算管理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结算管理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_queryfinalSettleList(accountamount, accountbillid, accountdate, accountnumber, accountnumbertotal, auditmoney, cashsource, cashsourcename, currentpage, discount, firstpaymentproportion, merchantdiscountamount, orderid, orderno, pagesize, partnerallname, stages, statusaccountfinalcheck, statusaccountfinalcheckname, statusaccountfirstcheck, statusaccountfirstcheckname, sumstrokecount, sumtotalmoney, username):
    """
    终审搜索分页列表
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :param orderid: 订单id,number
    :param accountbillid: 结算id,number
    :param accountdate: 应结算日期,string
    :param orderno: 订单号,string
    :param partnerallname:  商户名称,string
    :param cashsource: 放款渠道:  0启发，1香江,number
    :param cashsourcename: 放款渠道翻译成的中文,string
    :param username: 客户姓名,string
    :param auditmoney: 订单审核金额,number
    :param stages: 分期数,number
    :param merchantdiscountamount: 商户贴息金额,number
    :param firstpaymentproportion: 首打款比例,string
    :param accountnumber: 结算批次,number
    :param accountnumbertotal: 总结算批次,number
    :param accountamount: 结算金额,number
    :param statusaccountfirstcheck: 结算初审状态:status_account_firstcheck_unknown, 未开始  status_account_firstcheck_pending, 待提交  status_account_firstcheck_pass 通过,string
    :param statusaccountfinalcheck: 结算终审状态:status_account_finalcheck_unknown, status_account_finalcheck_pending,待提交  status_account_finalcheck_pass ,通过,string
    :param statusaccountfirstcheckname: 初审结算状态的中文名称,string
    :param statusaccountfinalcheckname: 终审结算状态的中文名称,string
    :param discount: 商户贴息率,string
    :param sumstrokecount: ,number
    :param sumtotalmoney: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3207')
    requesturl = baseUrl + "/accountbill/finalcheck/queryfinalSettleList"
    LOGGER.info("终审搜索分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountAmount"] = accountamount
    params["accountBillId"] = accountbillid
    params["accountDate"] = accountdate
    params["accountNumber"] = accountnumber
    params["accountNumberTotal"] = accountnumbertotal
    params["auditMoney"] = auditmoney
    params["cashSource"] = cashsource
    params["cashSourceName"] = cashsourcename
    params["currentPage"] = currentpage
    params["discount"] = discount
    params["firstPaymentProportion"] = firstpaymentproportion
    params["merchantDiscountAmount"] = merchantdiscountamount
    params["orderId"] = orderid
    params["orderNo"] = orderno
    params["pageSize"] = pagesize
    params["partnerAllName"] = partnerallname
    params["stages"] = stages
    params["statusAccountFinalcheck"] = statusaccountfinalcheck
    params["statusAccountFinalcheckName"] = statusaccountfinalcheckname
    params["statusAccountFirstcheck"] = statusaccountfirstcheck
    params["statusAccountFirstcheckName"] = statusaccountfirstcheckname
    params["sumStrokeCount"] = sumstrokecount
    params["sumTotalMoney"] = sumtotalmoney
    params["userName"] = username
    LOGGER.info("终审搜索分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审搜索分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_finalOncePassOrBack(accountbillid, createdid, detaillogid, id, logremark, logresult, logtime, logtype, orderid, passorback):
    """
    终审详情中单条通过或则退回
    :param id: ,number
    :param orderid: 订单id,number
    :param accountbillid:  结算账单id,number
    :param logtime:  日志时间,string
    :param logtype: 日志类型,string
    :param logresult: 日志结果,string
    :param logremark: 日志备注,string
    :param createdid: 日志操作人员,number
    :param detaillogid: 日志详情id,number
    :param passorback: 通过还是退回: pass:通过   back:退回,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3208')
    requesturl = baseUrl + "/accountbill/finalcheck/finalOncePassOrBack"
    LOGGER.info("终审详情中单条通过或则退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountBillId"] = accountbillid
    params["createdId"] = createdid
    params["detailLogId"] = detaillogid
    params["id"] = id
    params["logRemark"] = logremark
    params["logResult"] = logresult
    params["logTime"] = logtime
    params["logType"] = logtype
    params["orderId"] = orderid
    params["passOrBack"] = passorback
    LOGGER.info("终审详情中单条通过或则退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审详情中单条通过或则退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_queryFinalOrderSettleDetil(orderid):
    """
    终审的订单结算详情
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3209')
    requesturl = baseUrl + "/accountbill/finalcheck/queryFinalOrderSettleDetil"
    LOGGER.info("终审的订单结算详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("终审的订单结算详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审的订单结算详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_finalcheck_queryStages():
    """
    分期数字典
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3210')
    requesturl = baseUrl + "/accountbill/finalcheck/queryStages"
    LOGGER.info("分期数字典请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("分期数字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分期数字典请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryUnusualAccountBills(auditstate, loanmode, merchantname, orderno, pagenum, pagesize):
    """
    异常结算列表查询
    :param orderno: 订单号,string
    :param merchantname: 商户名称,string
    :param auditstate: 结算状态,string
    :param loanmode: 放款渠道,string
    :param pagenum: 页数,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3211')
    requesturl = baseUrl + "/accountbill/account/queryUnusualAccountBills"
    LOGGER.info("异常结算列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["loanMode"] = loanmode
    params["merchantName"] = merchantname
    params["orderNo"] = orderno
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    LOGGER.info("异常结算列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("异常结算列表查询请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_afreshAccount(accountid):
    """
    再次结算
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3212')
    requesturl = baseUrl + "/accountbill/account/afreshAccount"
    LOGGER.info("再次结算请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("再次结算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("再次结算请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryAccountBills(auditstate, loanmode, merchantname, orderno, pagenum, pagesize):
    """
    待结算列表查询
    :param orderno: 订单号,string
    :param merchantname: 商户名称,string
    :param auditstate: 结算状态,string
    :param loanmode: 放款渠道,string
    :param pagenum: 页数,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3213')
    requesturl = baseUrl + "/accountbill/account/queryAccountBills"
    LOGGER.info("待结算列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["loanMode"] = loanmode
    params["merchantName"] = merchantname
    params["orderNo"] = orderno
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    LOGGER.info("待结算列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("待结算列表查询请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_auditAccountBill(accountid, logremark, type):
    """
    处理结算信息
    :param accountid: 结算账单id,number
    :param type: 处理类型,number
    :param logremark: 处理备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3214')
    requesturl = baseUrl + "/accountbill/account/auditAccountBill"
    LOGGER.info("处理结算信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    params["logRemark"] = logremark
    params["type"] = type
    LOGGER.info("处理结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("处理结算信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_beachAuditAccountBill(idlist, loandowncount, loandowntotalmoney):
    """
    批量处理结算信息
    :param idlist: 放款记录id值列表,array
    :param loandowncount: 结算笔数,number
    :param loandowntotalmoney: 结算总金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3215')
    requesturl = baseUrl + "/accountbill/account/beachAuditAccountBill"
    LOGGER.info("批量处理结算信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["idList"] = idlist
    params["loandownCount"] = loandowncount
    params["loandownTotalMoney"] = loandowntotalmoney
    LOGGER.info("批量处理结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("批量处理结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_accountBillCount():
    """
    今日结算统计
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3216')
    requesturl = baseUrl + "/accountbill/account/accountBillCount"
    LOGGER.info("今日结算统计请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("今日结算统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("今日结算统计请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryAccountProgress(accountid):
    """
    查询结算信息审核进度
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3217')
    requesturl = baseUrl + "/accountbill/account/queryAccountProgress"
    LOGGER.info("查询结算信息审核进度请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算信息审核进度请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算信息审核进度请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryAccountPlan(orderid):
    """
    结算计划
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3218')
    requesturl = baseUrl + "/accountbill/account/queryAccountPlan"
    LOGGER.info("结算计划请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("结算计划请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结算计划请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryHistoryAccountBills(auditstate, begindate, enddate, loanmode, merchantname, orderno, pagenum, pagesize):
    """
    历史结算列表查询
    :param auditstate: 结算状态,string
    :param loanmode: 放款渠道,string
    :param merchantname: 商户名称,string
    :param orderno: 订单号,string
    :param pagenum: 页数,number
    :param pagesize: 页面大小,number
    :param enddate: 结束时间,string
    :param begindate: 开始时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3219')
    requesturl = baseUrl + "/accountbill/account/queryHistoryAccountBills"
    LOGGER.info("历史结算列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["beginDate"] = begindate
    params["endDate"] = enddate
    params["loanMode"] = loanmode
    params["merchantName"] = merchantname
    params["orderNo"] = orderno
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    LOGGER.info("历史结算列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史结算列表查询请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryAccountLogs(accountid):
    """
    查询结算操作日志记录
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3220')
    requesturl = baseUrl + "/accountbill/account/queryAccountLogs"
    LOGGER.info("查询结算操作日志记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算操作日志记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算操作日志记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_viewSettlementBill(orderid):
    """
    结算管理-用户账单
    :param orderid: 账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3221')
    requesturl = baseUrl + "/accountbill/account/viewSettlementBill"
    LOGGER.info("结算管理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("结算管理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结算管理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_menus_queryPermissionTree():
    """
    用户授权菜单
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3222')
    requesturl = baseUrl + "/menus/queryPermissionTree"
    LOGGER.info("用户授权菜单请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户授权菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户授权菜单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_menus_rolePermission(menuids, roleid):
    """
    分配角色权限
    :param roleid: 角色id,number
    :param menuids: 授权菜单权限id集合,array
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3223')
    requesturl = baseUrl + "/menus/rolePermission"
    LOGGER.info("分配角色权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["menuIds"] = menuids
    params["roleId"] = roleid
    LOGGER.info("分配角色权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分配角色权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_roles_addRoles(code, createtime, id, name, remark, sort):
    """
    新增角色
    :param id: 编号,number
    :param name: 角色名称,string
    :param code: 编码,string
    :param remark: 备注/描述,string
    :param sort: 排序,number
    :param createtime: 创建时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3224')
    requesturl = baseUrl + "/roles/addRoles"
    LOGGER.info("新增角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["createTime"] = createtime
    params["id"] = id
    params["name"] = name
    params["remark"] = remark
    params["sort"] = sort
    LOGGER.info("新增角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_roles_queryRoles(pageno, pagesize):
    """
    角色分页列表
    :param pageno: 当前页,number
    :param pagesize: 页大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3225')
    requesturl = baseUrl + "/roles/queryRoles"
    LOGGER.info("角色分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNo"] = pageno
    params["pageSize"] = pagesize
    LOGGER.info("角色分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色分页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_login(password, username):
    """
    用户登录
    :param username: 用户名,string
    :param password: 密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3226')
    requesturl = baseUrl + "/user/login"
    LOGGER.info("用户登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["userName"] = username
    LOGGER.info("用户登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_logout():
    """
    用户退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3227')
    requesturl = baseUrl + "/user/logout"
    LOGGER.info("用户退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户退出登录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getLoginUser():
    """
    登录用户信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3228')
    requesturl = baseUrl + "/user/getLoginUser"
    LOGGER.info("登录用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("登录用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录用户信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_resetPassWordByEmail(email, passs, sid):
    """
    重置密码
    :param email: 邮箱,string
    :param passs: 新密码,string
    :param sid: 签名标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3229')
    requesturl = baseUrl + "/user/resetPassWordByEmail"
    LOGGER.info("重置密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["passs"] = passs
    params["sid"] = sid
    LOGGER.info("重置密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重置密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_queryUserList(pageno, pagesize):
    """
    用户信息分页列表
    :param pageno: 当前页,number
    :param pagesize: 页大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3230')
    requesturl = baseUrl + "/user/queryUserList"
    LOGGER.info("用户信息分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNo"] = pageno
    params["pageSize"] = pagesize
    LOGGER.info("用户信息分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户信息分页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_addUser(applicationid, auditstate, cardno, code, companyid, createtime, creator, email, frozen, header, id, lastlogintime, name, phone, realname, remark, role, roleids, updatetime, usestatus):
    """
    新增用户
    :param id: 编号,number
    :param code: 编码,string
    :param companyid: 租户id/企业id,number
    :param applicationid: 应用id,number
    :param name: 用户名,string
    :param realname: 真实姓名,string
    :param cardno: 身份证号,string
    :param phone: 手机号,string
    :param email: 邮箱,string
    :param header: 头像,string
    :param remark: 备注,string
    :param role: 角色,string
    :param creator: 创建人(业务管理员),string
    :param roleids: 角色id集,array
    :param auditstate: 审核状态:待审核-STATE_INIT；通过-"STATE_PASS；拒绝-STATE_REFECT,string
    :param frozen: 冻结:FROZEN_NORMAL-正常；一级-FROZEN_ONE；二级-FROZEN_TWO,string
    :param usestatus: 是否在职,string
    :param lastlogintime: 登录时间,string
    :param createtime: 创建时间,string
    :param updatetime: 更新时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3231')
    requesturl = baseUrl + "/user/addUser"
    LOGGER.info("新增用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["applicationId"] = applicationid
    params["auditState"] = auditstate
    params["cardNo"] = cardno
    params["code"] = code
    params["companyId"] = companyid
    params["createTime"] = createtime
    params["creator"] = creator
    params["email"] = email
    params["frozen"] = frozen
    params["header"] = header
    params["id"] = id
    params["lastLoginTime"] = lastlogintime
    params["name"] = name
    params["phone"] = phone
    params["realName"] = realname
    params["remark"] = remark
    params["role"] = role
    params["roleIds"] = roleids
    params["updateTime"] = updatetime
    params["useStatus"] = usestatus
    LOGGER.info("新增用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_updateUser(applicationid, auditstate, cardno, code, companyid, createtime, creator, email, frozen, header, id, lastlogintime, name, phone, realname, remark, role, roleids, updatetime, usestatus):
    """
    修改用户
    :param id: 编号,number
    :param code: 编码,string
    :param companyid: 租户id/企业id,number
    :param applicationid: 应用id,number
    :param name: 用户名,string
    :param realname: 真实姓名,string
    :param cardno: 身份证号,string
    :param phone: 手机号,string
    :param email: 邮箱,string
    :param header: 头像,string
    :param remark: 备注,string
    :param role: 角色,string
    :param creator: 创建人(业务管理员),string
    :param roleids: 角色id集,array
    :param auditstate: 审核状态:待审核-STATE_INIT；通过-"STATE_PASS；拒绝-STATE_REFECT,string
    :param frozen: 冻结:FROZEN_NORMAL-正常；一级-FROZEN_ONE；二级-FROZEN_TWO,string
    :param usestatus: 是否在职,string
    :param lastlogintime: 登录时间,string
    :param createtime: 创建时间,string
    :param updatetime: 更新时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3232')
    requesturl = baseUrl + "/user/updateUser"
    LOGGER.info("修改用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["applicationId"] = applicationid
    params["auditState"] = auditstate
    params["cardNo"] = cardno
    params["code"] = code
    params["companyId"] = companyid
    params["createTime"] = createtime
    params["creator"] = creator
    params["email"] = email
    params["frozen"] = frozen
    params["header"] = header
    params["id"] = id
    params["lastLoginTime"] = lastlogintime
    params["name"] = name
    params["phone"] = phone
    params["realName"] = realname
    params["remark"] = remark
    params["role"] = role
    params["roleIds"] = roleids
    params["updateTime"] = updatetime
    params["useStatus"] = usestatus
    LOGGER.info("修改用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_updateUseStatus(userid):
    """
    用户离职
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3233')
    requesturl = baseUrl + "/user/updateUseStatus"
    LOGGER.info("用户离职请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户离职请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户离职请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_billInfo_viewRepaymentHandleBill(orderid):
    """
    账单还款处理-用户账单
    :param orderid: orderId,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3234')
    requesturl = baseUrl + "/billInfo/viewRepaymentHandleBill"
    LOGGER.info("账单还款处理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("账单还款处理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单还款处理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_BDReport(beginmonth, endmonth):
    """
    BD审批情况表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3235')
    requesturl = baseUrl + "/ReportExport/BDReport"
    LOGGER.info("BD审批情况表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("BD审批情况表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD审批情况表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_loanMonitorCityReport(beginmonth, endmonth):
    """
    城市贷中监控表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3236')
    requesturl = baseUrl + "/ReportExport/loanMonitorCityReport"
    LOGGER.info("城市贷中监控表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("城市贷中监控表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("城市贷中监控表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_loanMonitorIndustryReport(beginmonth, endmonth):
    """
    行业贷中监控表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3237')
    requesturl = baseUrl + "/ReportExport/loanMonitorIndustryReport"
    LOGGER.info("行业贷中监控表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("行业贷中监控表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("行业贷中监控表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_loanMonitorPeriodReport(beginmonth, endmonth):
    """
    贷款期数贷中监控表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3238')
    requesturl = baseUrl + "/ReportExport/loanMonitorPeriodReport"
    LOGGER.info("贷款期数贷中监控表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("贷款期数贷中监控表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款期数贷中监控表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_loanFeatureAgeReport(beginmonth, endmonth):
    """
    贷款特征报表-年龄
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3239')
    requesturl = baseUrl + "/ReportExport/loanFeatureAgeReport"
    LOGGER.info("贷款特征报表-年龄请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("贷款特征报表-年龄请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款特征报表-年龄请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_auditCityReport(beginmonth, endmonth):
    """
    城市审批情况表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3240')
    requesturl = baseUrl + "/ReportExport/auditCityReport"
    LOGGER.info("城市审批情况表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("城市审批情况表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("城市审批情况表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ReportExport_industryReport(beginmonth, endmonth):
    """
    行业审批情况表
    :param beginmonth: 开始月份yyyy-MM,string
    :param endmonth: 结束月份yyyy-MM,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3241')
    requesturl = baseUrl + "/ReportExport/industryReport"
    LOGGER.info("行业审批情况表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginMonth"] = beginmonth
    params["endMonth"] = endmonth
    LOGGER.info("行业审批情况表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("行业审批情况表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_billshouldpay_list(endtime, key, pageno, pagesize, starttime):
    """
    应收账单列表
    :param key: 查询关键字,string
    :param starttime: 查询开始时间,string
    :param endtime: 查询结束时间,string
    :param pageno: 页数,number
    :param pagesize: 每页数据量,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3242')
    requesturl = baseUrl + "/loandown/billshouldpay/list"
    LOGGER.info("应收账单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["key"] = key
    params["pageNo"] = pageno
    params["pageSize"] = pagesize
    params["startTime"] = starttime
    LOGGER.info("应收账单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("应收账单列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_billshouldpay_export(endtime, key, starttime):
    """
    应收账单列表导出
    :param key: 查询关键字,string
    :param starttime: 查询开始时间,string
    :param endtime: 查询结束时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3243')
    requesturl = baseUrl + "/loandown/billshouldpay/export"
    LOGGER.info("应收账单列表导出请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["key"] = key
    params["startTime"] = starttime
    LOGGER.info("应收账单列表导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("应收账单列表导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_billfactpay_list(endtime, key, pageno, pagesize, starttime):
    """
    实收账单列表
    :param key: 查询关键字,string
    :param starttime: 查询开始时间,string
    :param endtime: 查询结束时间,string
    :param pageno: 页数,number
    :param pagesize: 每页数据量,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3244')
    requesturl = baseUrl + "/loandown/billfactpay/list"
    LOGGER.info("实收账单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["key"] = key
    params["pageNo"] = pageno
    params["pageSize"] = pagesize
    params["startTime"] = starttime
    LOGGER.info("实收账单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("实收账单列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_billfactpay_export(endtime, key, starttime):
    """
    实收账单列表导出
    :param key: 查询关键字,string
    :param starttime: 查询开始时间,string
    :param endtime: 查询结束时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3245')
    requesturl = baseUrl + "/loandown/billfactpay/export"
    LOGGER.info("实收账单列表导出请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["key"] = key
    params["startTime"] = starttime
    LOGGER.info("实收账单列表导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("实收账单列表导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryLoandownList(begindate, cashsource, currentpage, enddate, pagesize, searchkeywords):
    """
    放款列表
    :param searchkeywords: 搜索关键字,string
    :param cashsource: 放款渠道,number
    :param begindate: 开始日期,string
    :param enddate: 结束日期,string
    :param currentpage: 当前页,number
    :param pagesize: 每页数据大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3246')
    requesturl = baseUrl + "/loandown/accountloan/queryLoandownList"
    LOGGER.info("放款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["cashSource"] = cashsource
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["pageSize"] = pagesize
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_exportLoandownList(begindate, cashsource, enddate, searchkeywords):
    """
    导出放款列表
    :param searchkeywords: 搜索关键字,string
    :param cashsource: 放款渠道,number
    :param begindate: 开始日期,string
    :param enddate: 结束日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3247')
    requesturl = baseUrl + "/loandown/accountloan/exportLoandownList"
    LOGGER.info("导出放款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["cashSource"] = cashsource
    params["endDate"] = enddate
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("导出放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出放款列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryHistoryLoandownList(begindate, currentpage, enddate, pagesize, searchkeywords):
    """
    历史放款记录列表
    :param searchkeywords: 搜索关键字,string
    :param begindate: 开始日期,string
    :param enddate: 结束日期,string
    :param currentpage: 当前页,number
    :param pagesize: 每页数据大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3248')
    requesturl = baseUrl + "/loandown/accountloan/queryHistoryLoandownList"
    LOGGER.info("历史放款记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["pageSize"] = pagesize
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("历史放款记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史放款记录列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_exportHistoryLoandownList(begindate, enddate, searchkeywords):
    """
    导出历史放款记录列表
    :param searchkeywords: 搜索关键字,string
    :param begindate: 开始日期,string
    :param enddate: 结束日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3249')
    requesturl = baseUrl + "/loandown/accountloan/exportHistoryLoandownList"
    LOGGER.info("导出历史放款记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["endDate"] = enddate
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("导出历史放款记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出历史放款记录列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_loandownBatch(idlist, loandowncount, loandowntotalmoney):
    """
    批量放款
    :param idlist: 放款记录id值列表,array
    :param loandowncount: 放款笔数,number
    :param loandowntotalmoney: 放款总金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3250')
    requesturl = baseUrl + "/loandown/accountloan/loandownBatch"
    LOGGER.info("批量放款请求地址:【{}】".format(requesturl))
    params = dict()
    params["idList"] = idlist
    params["loandownCount"] = loandowncount
    params["loandownTotalMoney"] = loandowntotalmoney
    LOGGER.info("批量放款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("批量放款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_loandownPass(id, loandownmoney, remark):
    """
    确认放款(单条通过)
    :param id: 放款记录id,number
    :param loandownmoney: 放款金额,number
    :param remark: 备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3251')
    requesturl = baseUrl + "/loandown/accountloan/loandownPass"
    LOGGER.info("确认放款(单条通过)请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["loandownMoney"] = loandownmoney
    params["remark"] = remark
    LOGGER.info("确认放款(单条通过)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认放款(单条通过)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_loandownBack(id, loandownmoney, remark):
    """
    放款退回
    :param id: 放款记录id,number
    :param loandownmoney: 放款金额,number
    :param remark: 备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3252')
    requesturl = baseUrl + "/loandown/accountloan/loandownBack"
    LOGGER.info("放款退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["loandownMoney"] = loandownmoney
    params["remark"] = remark
    LOGGER.info("放款退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryAccountLogs(accountid):
    """
    查询结算操作日志记录
    :param accountid: 结算账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3253')
    requesturl = baseUrl + "/loandown/accountloan/queryAccountLogs"
    LOGGER.info("查询结算操作日志记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountId"] = accountid
    LOGGER.info("查询结算操作日志记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询结算操作日志记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryAccountBillList(orderid):
    """
    查询某一订单下的所有结算计划
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3254')
    requesturl = baseUrl + "/loandown/accountloan/queryAccountBillList"
    LOGGER.info("查询某一订单下的所有结算计划请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("查询某一订单下的所有结算计划请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询某一订单下的所有结算计划请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_viewSettlementBill(orderid):
    """
    财务放款处理详情管理-用户账单
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3255')
    requesturl = baseUrl + "/loandown/accountloan/viewSettlementBill"
    LOGGER.info("财务放款处理详情管理-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("财务放款处理详情管理-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务放款处理详情管理-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_orderInfo_queryOrderDetil(accountbillid, orderid):
    """
    审核页面订单详情
    :param orderid: 订单id,number
    :param accountbillid: 结算id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3256')
    requesturl = baseUrl + "/orderInfo/queryOrderDetil"
    LOGGER.info("审核页面订单详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountBillId"] = accountbillid
    params["orderId"] = orderid
    LOGGER.info("审核页面订单详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核页面订单详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_orderInfo_export(param, response):
    """
    导出列表
    :param response: response,object
    :param param: param,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3257')
    requesturl = baseUrl + "/orderInfo/export"
    LOGGER.info("导出列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["param"] = param
    params["response"] = response
    LOGGER.info("导出列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_reback(remark, repayid):
    """
    财务退回
    :param repayid: 查询关键字,number
    :param remark: 备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3258')
    requesturl = baseUrl + "/repay/accountrepay/reback"
    LOGGER.info("财务退回请求地址:【{}】".format(requesturl))
    params = dict()
    params["remark"] = remark
    params["repayId"] = repayid
    LOGGER.info("财务退回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务退回请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_viewOfflineRepaymentBill(userid):
    """
    线下还款处理详情-用户账单
    :param userid: userId,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3259')
    requesturl = baseUrl + "/repay/accountrepay/viewOfflineRepaymentBill"
    LOGGER.info("线下还款处理详情-用户账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("线下还款处理详情-用户账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线下还款处理详情-用户账单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_queryOfflineRepay(pagenum, pagesize, repaytimeend, repaytimestart, searchkey):
    """
    查询线下还款记录
    :param searchkey: 查询关键字,string
    :param repaytimestart: 还款记录开始时间, 格式yyyy-MM-dd HH:mm:ss,string
    :param repaytimeend: 还款记录结束时间, 格式yyyy-MM-dd HH:mm:ss,string
    :param pagenum: 页数,number
    :param pagesize: 页容量,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3260')
    requesturl = baseUrl + "/repay/accountrepay/queryOfflineRepay"
    LOGGER.info("查询线下还款记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["repayTimeEnd"] = repaytimeend
    params["repayTimeStart"] = repaytimestart
    params["searchKey"] = searchkey
    LOGGER.info("查询线下还款记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询线下还款记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_pass(imagekey, imagename, receiveamount, repayid):
    """
    财务确认收款
    :param repayid: 查询关键字,number
    :param imagekey: 图片key,string
    :param imagename: 图片名称,string
    :param receiveamount: 实收金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3261')
    requesturl = baseUrl + "/repay/accountrepay/pass"
    LOGGER.info("财务确认收款请求地址:【{}】".format(requesturl))
    params = dict()
    params["imageKey"] = imagekey
    params["imageName"] = imagename
    params["receiveAmount"] = receiveamount
    params["repayId"] = repayid
    LOGGER.info("财务确认收款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("财务确认收款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepayOffline_accountRepaySubmit(billid, repayamount, repaytime, userid):
    """
    线上还款申请
    :param billid: 账单id,number
    :param repayamount: 还款金额,number
    :param userid: 用户id,number
    :param repaytime: 还款时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3262')
    requesturl = baseUrl + "/repay/accountrepayOffline/accountRepaySubmit"
    LOGGER.info("线上还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["repayAmount"] = repayamount
    params["repayTime"] = repaytime
    params["userId"] = userid
    LOGGER.info("线上还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线上还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepayOffline_accountRepayCallback(billid, issuccess):
    """
    线上还款回调
    :param billid: 账单id,number
    :param issuccess: 还款金额,boolean
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3263')
    requesturl = baseUrl + "/repay/accountrepayOffline/accountRepayCallback"
    LOGGER.info("线上还款回调请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["isSuccess"] = issuccess
    LOGGER.info("线上还款回调请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线上还款回调请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user(userid):
    """
    用户详情信息
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3264')
    requesturl = baseUrl + "/user"
    LOGGER.info("用户详情信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户详情信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户详情信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_resetPassWordSendEmail(userid):
    """
    用户重置密码邮箱发送
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3265')
    requesturl = baseUrl + "/user/resetPassWordSendEmail"
    LOGGER.info("用户重置密码邮箱发送请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户重置密码邮箱发送请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户重置密码邮箱发送请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_1():
    """
    header消息头统一设置
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3266')
    requesturl = baseUrl + "/1"
    LOGGER.info("header消息头统一设置请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("header消息头统一设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("header消息头统一设置请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_menus_queryRolePermission(roleid):
    """
    指定角色菜单权限id集获取
    :param roleid: 角色id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3267')
    requesturl = baseUrl + "/menus/queryRolePermission"
    LOGGER.info("指定角色菜单权限id集获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["roleId"] = roleid
    LOGGER.info("指定角色菜单权限id集获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("指定角色菜单权限id集获取请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_menus_queryPermission():
    """
    用户授权平级菜单
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3268')
    requesturl = baseUrl + "/menus/queryPermission"
    LOGGER.info("用户授权平级菜单请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户授权平级菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户授权平级菜单请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_roles_queryRoleDic():
    """
    查询角色字典列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3269')
    requesturl = baseUrl + "/roles/queryRoleDic"
    LOGGER.info("查询角色字典列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询角色字典列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询角色字典列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_validResetUrl(sid):
    """
    重置密码超链接验证
    :param sid: sid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3270')
    requesturl = baseUrl + "/user/validResetUrl"
    LOGGER.info("重置密码超链接验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["sid"] = sid
    LOGGER.info("重置密码超链接验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重置密码超链接验证请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_queryAuditingAccountBills(auditstate, loanmode, merchantname, orderno, pagenum, pagesize):
    """
    审核中结算列表查询
    :param orderno: 订单号,string
    :param merchantname: 商户名称,string
    :param auditstate: 结算状态,string
    :param loanmode: 放款渠道,string
    :param pagenum: 页数,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3273')
    requesturl = baseUrl + "/accountbill/account/queryAuditingAccountBills"
    LOGGER.info("审核中结算列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["loanMode"] = loanmode
    params["merchantName"] = merchantname
    params["orderNo"] = orderno
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    LOGGER.info("审核中结算列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核中结算列表查询请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getOne(userid):
    """
    用户详情信息
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3274')
    requesturl = baseUrl + "/user/getOne"
    LOGGER.info("用户详情信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户详情信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户详情信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_getUserInfo(userid):
    """
    根据逾期的账单id查询贷款用户的信息
    :param userid: 用户的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3275')
    requesturl = baseUrl + "/overdue/handle/getUserInfo"
    LOGGER.info("根据逾期的账单id查询贷款用户的信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("根据逾期的账单id查询贷款用户的信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据逾期的账单id查询贷款用户的信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_findUserBillList(currentpage, keyword, overduestage, pagesize):
    """
    逾期账单统计列表
    :param keyword: 关键字搜索,string
    :param overduestage: 逾期阶段,string
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3276')
    requesturl = baseUrl + "/overdue/findUserBillList"
    LOGGER.info("逾期账单统计列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["keyword"] = keyword
    params["overdueStage"] = overduestage
    params["pageSize"] = pagesize
    LOGGER.info("逾期账单统计列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_export(currentpage, keyword, overduestage, pagesize):
    """
    逾期账单统计列表
    :param keyword: 关键字搜索,string
    :param overduestage: 逾期阶段,string
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3277')
    requesturl = baseUrl + "/overdue/export"
    LOGGER.info("逾期账单统计列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["keyword"] = keyword
    params["overdueStage"] = overduestage
    params["pageSize"] = pagesize
    LOGGER.info("逾期账单统计列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_queryOrderInfo(userid):
    """
    根据逾期的账单id查询该订单信息
    :param userid: 用户的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3278')
    requesturl = baseUrl + "/overdue/handle/queryOrderInfo"
    LOGGER.info("根据逾期的账单id查询该订单信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("根据逾期的账单id查询该订单信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据逾期的账单id查询该订单信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_ui_user_dateTest(time):
    """
    findOverdueInfoPage
    :param time: time,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3279')
    requesturl = baseUrl + "/overdue/ui/user/dateTest"
    LOGGER.info("findOverdueInfoPage请求地址:【{}】".format(requesturl))
    params = dict()
    params["time"] = time
    LOGGER.info("findOverdueInfoPage请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("findOverdueInfoPage请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_findOverdueInfoPage(currentpage, pagesize, userid):
    """
    逾期详情分页列表
    :param currentpage: 页码,number
    :param pagesize: 页面大小,number
    :param userid: 用户的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3280')
    requesturl = baseUrl + "/overdue/handle/findOverdueInfoPage"
    LOGGER.info("逾期详情分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userId"] = userid
    LOGGER.info("逾期详情分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期详情分页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_findLinkManPage(currentpage, pagesize, searchkey, userid):
    """
    逾期处理联系人分页列表
    :param currentpage: ,number
    :param pagesize: ,number
    :param userid: 用户id,number
    :param searchkey: 电话号码或者用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3281')
    requesturl = baseUrl + "/overdue/handle/findLinkManPage"
    LOGGER.info("逾期处理联系人分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["searchKey"] = searchkey
    params["userId"] = userid
    LOGGER.info("逾期处理联系人分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期处理联系人分页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_findLinkAddressPage(currentpage, pagesize, userid):
    """
    查询地址
    :param userid: 查询关键字,number
    :param pagesize: pageSize,number
    :param currentpage: currentPage,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3282')
    requesturl = baseUrl + "/overdue/handle/findLinkAddressPage"
    LOGGER.info("查询地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userId"] = userid
    LOGGER.info("查询地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询地址请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_getUserImage(userid):
    """
    查看图片
    :param userid: 用户的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3283')
    requesturl = baseUrl + "/overdue/handle/getUserImage"
    LOGGER.info("查看图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("查看图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看图片请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_saveAddress(address, addresstype, id, userid):
    """
    新增地址
    :param id: id,number
    :param userid: 用户名称,number
    :param addresstype: 地址类型,string
    :param address: 地址,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3284')
    requesturl = baseUrl + "/overdue/handle/saveAddress"
    LOGGER.info("新增地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["addressType"] = addresstype
    params["id"] = id
    params["userId"] = userid
    LOGGER.info("新增地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增地址请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_saveLineman(contactphone, contacttype, id, name, relation, userid):
    """
    添加联系人
    :param id: ,number
    :param userid: 用户id,number
    :param name: 联系人人们,string
    :param relation: 联系人关系,string
    :param contacttype: 联系方式,string
    :param contactphone: 电话号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3285')
    requesturl = baseUrl + "/overdue/handle/saveLineman"
    LOGGER.info("添加联系人请求地址:【{}】".format(requesturl))
    params = dict()
    params["contactPhone"] = contactphone
    params["contactType"] = contacttype
    params["id"] = id
    params["name"] = name
    params["relation"] = relation
    params["userId"] = userid
    LOGGER.info("添加联系人请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加联系人请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_saveRemark(calluserid, callusername, id, linkmanname, linkmanrelation, remark, userid):
    """
    通话备注添加
    :param id: id,number
    :param userid: 用户id,number
    :param linkmanname: 联系人名称,string
    :param linkmanrelation: 联系人关系,string
    :param calluserid: 通话用户id,number
    :param callusername: 通话用户名称,string
    :param remark: 通话备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3286')
    requesturl = baseUrl + "/overdue/handle/saveRemark"
    LOGGER.info("通话备注添加请求地址:【{}】".format(requesturl))
    params = dict()
    params["callUserId"] = calluserid
    params["callUserName"] = callusername
    params["id"] = id
    params["linkmanName"] = linkmanname
    params["linkmanRelation"] = linkmanrelation
    params["remark"] = remark
    params["userId"] = userid
    LOGGER.info("通话备注添加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通话备注添加请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_findCallRemarkPage(currentpage, pagesize, searchkey, userid):
    """
    历史通话详情分页列表
    :param currentpage: ,number
    :param pagesize: ,number
    :param userid: 用户id,number
    :param searchkey: 电话号码或者用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3287')
    requesturl = baseUrl + "/overdue/handle/findCallRemarkPage"
    LOGGER.info("历史通话详情分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["searchKey"] = searchkey
    params["userId"] = userid
    LOGGER.info("历史通话详情分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史通话详情分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_workcenter_data_getOutline():
    """
    统计概要数据
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3288')
    requesturl = baseUrl + "/workcenter/data/getOutline"
    LOGGER.info("统计概要数据请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("统计概要数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("统计概要数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_workcenter_data_getLoanOutline(dateend, datestart, type):
    """
    统计放款趋势
    :param type: 查询类型, TODAY今天, WEEK本周, MONTH本月, YEAR本年, CUSTOM 自定义查询时间, 只有自定义查询时间，设置的开始和结束时间才会起效,string
    :param datestart: 查询开始时间,string
    :param dateend: 查询结束时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3289')
    requesturl = baseUrl + "/workcenter/data/getLoanOutline"
    LOGGER.info("统计放款趋势请求地址:【{}】".format(requesturl))
    params = dict()
    params["dateEnd"] = dateend
    params["dateStart"] = datestart
    params["type"] = type
    LOGGER.info("统计放款趋势请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("统计放款趋势请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_workcenter_data_getPendingObj():
    """
    当前待处理
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3290')
    requesturl = baseUrl + "/workcenter/data/getPendingObj"
    LOGGER.info("当前待处理请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("当前待处理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("当前待处理请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_workcenter_data_getRepayOutline():
    """
    贷后统计
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3291')
    requesturl = baseUrl + "/workcenter/data/getRepayOutline"
    LOGGER.info("贷后统计请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("贷后统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷后统计请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_workcenter_data_getAccountOutline():
    """
    回款统计
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3292')
    requesturl = baseUrl + "/workcenter/data/getAccountOutline"
    LOGGER.info("回款统计请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("回款统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("回款统计请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_exportOrderByHistory():
    """
    根据历史结算导出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3294')
    requesturl = baseUrl + "/accountbill/account/exportOrderByHistory"
    LOGGER.info("根据历史结算导出请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("根据历史结算导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据历史结算导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_exportOrderByUnusual():
    """
    根据异常结算导出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3295')
    requesturl = baseUrl + "/accountbill/account/exportOrderByUnusual"
    LOGGER.info("根据异常结算导出请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("根据异常结算导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据异常结算导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_accountbill_account_exportOrderByWaitting():
    """
    根绝待结算导出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3296')
    requesturl = baseUrl + "/accountbill/account/exportOrderByWaitting"
    LOGGER.info("根绝待结算导出请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("根绝待结算导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根绝待结算导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryOverdueBillCount(begindate, enddate, searchkeywords):
    """
    逾期账单统计
    :param begindate: 结束日期,string
    :param enddate: 开始日期,string
    :param searchkeywords: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3307')
    requesturl = baseUrl + "/loandown/accountloan/queryOverdueBillCount"
    LOGGER.info("逾期账单统计请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["endDate"] = enddate
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("逾期账单统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_queryOverdueBillList(begindate, currentpage, enddate, pagesize, searchkeywords):
    """
    逾期账单统计列表
    :param begindate: 开始日期,string
    :param currentpage: 当前页,number
    :param enddate: 结束日期,string
    :param pagesize: 页面大小,number
    :param searchkeywords: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3308')
    requesturl = baseUrl + "/loandown/accountloan/queryOverdueBillList"
    LOGGER.info("逾期账单统计列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["pageSize"] = pagesize
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("逾期账单统计列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_orderInfo_queryRepaymentOrderDetil(orderid):
    """
    还款详情页面的订单详情
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3309')
    requesturl = baseUrl + "/orderInfo/queryRepaymentOrderDetil"
    LOGGER.info("还款详情页面的订单详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("还款详情页面的订单详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款详情页面的订单详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v3.1.0_mm_partner_goodsInfo(currentpage, id, pagesize, search):
    """
    商品管理
    :param currentpage: 当前页,number
    :param id: 商户ID,number
    :param pagesize: 每页记录数,number
    :param search: 商品名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3310')
    requesturl = baseUrl + "/api/v3.1.0/mm/partner/goodsInfo"
    LOGGER.info("商品管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["id"] = id
    params["pageSize"] = pagesize
    params["search"] = search
    LOGGER.info("商品管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商品管理请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_findOverUserBillList(currentpage, keyword, overduestage, pagesize):
    """
    逾期账单统计列表
    :param keyword: 关键字搜索,string
    :param overduestage: 逾期阶段,string
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3311')
    requesturl = baseUrl + "/overdue/findOverUserBillList"
    LOGGER.info("逾期账单统计列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["keyword"] = keyword
    params["overdueStage"] = overduestage
    params["pageSize"] = pagesize
    LOGGER.info("逾期账单统计列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_queryRepayList(currentpage, pagesize, searchkey):
    """
    还款处理搜索分页列表
    :param searchkey: 订单号/客户姓名/手机号,string
    :param currentpage: 当前页数,number
    :param pagesize: 单页记录数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3312')
    requesturl = baseUrl + "/repay/accountrepay/queryRepayList"
    LOGGER.info("还款处理搜索分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["searchKey"] = searchkey
    LOGGER.info("还款处理搜索分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款处理搜索分页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_loandown_accountloan_exportOverdueBillList(begindate, enddate, searchkeywords):
    """
    逾期账单统计导出
    :param enddate: 结束日期,string
    :param begindate: 开始日期,string
    :param searchkeywords: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3313')
    requesturl = baseUrl + "/loandown/accountloan/exportOverdueBillList"
    LOGGER.info("逾期账单统计导出请求地址:【{}】".format(requesturl))
    params = dict()
    params["beginDate"] = begindate
    params["endDate"] = enddate
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("逾期账单统计导出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计导出请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_handle_findUserBillDetail(orderid):
    """
    用户账单明细
    :param orderid: 订单iid,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3314')
    requesturl = baseUrl + "/overdue/handle/findUserBillDetail"
    LOGGER.info("用户账单明细请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("用户账单明细请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户账单明细请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_offline_repayInfo(billid):
    """
    还款明细
    :param billid: 账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3316')
    requesturl = baseUrl + "/repay/accountrepay/offline/repayInfo"
    LOGGER.info("还款明细请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    LOGGER.info("还款明细请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款明细请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_offline_repayBill(billid, overduetype, receivableamount, remark, repaytype, repayvoucherurls, subrepayamount):
    """
    线下还款
    :param billid: 账单id,number
    :param overduetype: 还款方式，account公司账户，alipay支付宝,string
    :param receivableamount: 应还款金额,number
    :param remark: 备注,string
    :param repaytype: 逾期类型/减免类型：overdue_normal-正常逾期；overdue_non_normal-非,string
    :param repayvoucherurls: 还款凭证图，多张逗号分隔,string
    :param subrepayamount: 还款减免金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3317')
    requesturl = baseUrl + "/repay/accountrepay/offline/repayBill"
    LOGGER.info("线下还款请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["overdueType"] = overduetype
    params["receivableAmount"] = receivableamount
    params["remark"] = remark
    params["repayType"] = repaytype
    params["repayVoucherUrls"] = repayvoucherurls
    params["subRepayAmount"] = subrepayamount
    LOGGER.info("线下还款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线下还款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_complete_offline_repayBill(realvoucherurls, repayamount, repayid):
    """
    线下还款,财务确认还款
    :param realvoucherurls: 实收凭证图，多张逗号分隔,string
    :param repayamount: 实际还款金额不能为空,number
    :param repayid: 还款id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3318')
    requesturl = baseUrl + "/repay/accountrepay/complete/offline/repayBill"
    LOGGER.info("线下还款,财务确认还款请求地址:【{}】".format(requesturl))
    params = dict()
    params["realVoucherUrls"] = realvoucherurls
    params["repayAmount"] = repayamount
    params["repayId"] = repayid
    LOGGER.info("线下还款,财务确认还款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线下还款,财务确认还款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_offline_repayValid(billid):
    """
    还款验证
    :param billid: 账单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3319')
    requesturl = baseUrl + "/repay/accountrepay/offline/repayValid"
    LOGGER.info("还款验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    LOGGER.info("还款验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款验证请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_queryOverdueBillByUser(overduestage, pagenum, pagesize, searchkeywords):
    """
    逾期账单统计列表查询--v4.1.2
    :param overduestage: 逾期阶段,string
    :param pagenum: 当前页,number
    :param pagesize: 页面大小,number
    :param searchkeywords: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3320')
    requesturl = baseUrl + "/overdue/queryOverdueBillByUser"
    LOGGER.info("逾期账单统计列表查询--v4.1.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["overdueStage"] = overduestage
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("逾期账单统计列表查询--v4.1.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表查询--v4.1.2请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_overdue_exportOverdueBillList(overduestage, searchkeywords):
    """
    逾期账单统计列表导出--v4.1.2
    :param overduestage: 逾期阶段,string
    :param searchkeywords: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3321')
    requesturl = baseUrl + "/overdue/exportOverdueBillList"
    LOGGER.info("逾期账单统计列表导出--v4.1.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["overdueStage"] = overduestage
    params["searchKeyWords"] = searchkeywords
    LOGGER.info("逾期账单统计列表导出--v4.1.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期账单统计列表导出--v4.1.2请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepay_repayOpLog(orderid):
    """
    还款操作日志
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3322')
    requesturl = baseUrl + "/repay/accountrepay/repayOpLog"
    LOGGER.info("还款操作日志请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("还款操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款操作日志请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


