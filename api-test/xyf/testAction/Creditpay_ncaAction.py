#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_ncaAction.py
@desc       : 项目：xyf 模块：creditpay_nca 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_nca_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_nca_login()


def test_auditing_orderAuditing_rule_approve(orderid):
    """
    审核详情_认证信息
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2602')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2603')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2604')
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


def test_auditing_applicant_userAuthDetail():
    """
    审核详情申请人报告信息（京东、淘宝、运营商）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2605')
    requesturl = baseUrl + "/auditing/applicant/userAuthDetail"
    LOGGER.info("审核详情申请人报告信息（京东、淘宝、运营商）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("审核详情申请人报告信息（京东、淘宝、运营商）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情申请人报告信息（京东、淘宝、运营商）请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2606')
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


def test_auditing_finalAuditing_queryFinalAuditingList(card_no, create_time_end, create_time_start, merchant_name, mobile, order_name, order_no, real_name, secondauditmoney_end, secondauditmoney_start, secondaudittime_end, secondaudittime_start, secondauditusername, state):
    """
    终审列表
    :param mobile: 手机号,string
    :param secondauditmoney_start: 二审金额_开始,number
    :param order_no: 订单号,string
    :param secondaudittime_start: 二审时间_开始,string
    :param card_no: 身份证号,string
    :param secondauditmoney_end: 二审金额_结束,number
    :param secondauditusername: 二审同学,string
    :param secondaudittime_end: 二审时间_结束,string
    :param create_time_start: 进件时间_开始,string
    :param real_name: 用户名,string
    :param state: 选项卡的状态,number
    :param create_time_end: 进件时间_结束,string
    :param order_name: 商品名称,string
    :param merchant_name: 商家名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2607')
    requesturl = baseUrl + "/auditing/finalAuditing/queryFinalAuditingList"
    LOGGER.info("终审列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["card_no"] = card_no
    params["create_time_end"] = create_time_end
    params["create_time_start"] = create_time_start
    params["merchant_name"] = merchant_name
    params["mobile"] = mobile
    params["order_name"] = order_name
    params["order_no"] = order_no
    params["real_name"] = real_name
    params["secondAuditMoney_end"] = secondauditmoney_end
    params["secondAuditMoney_start"] = secondauditmoney_start
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


def test_auditing_finalAuditing_finalSubmit(allowreapply, auditopinion, auditstate, fkrefusereason, operateid, orderid, riskcontrolpaymentproportion, ywrefusereason):
    """
    xqh_终审提交(v1.0.0修改)
    :param operateid: 操作人员id,string
    :param orderid: 订单Id,number
    :param auditstate: 审核状态,string
    :param auditopinion: 审核意见,string
    :param riskcontrolpaymentproportion: 风控打款比例（v1.0.0新增，提交百分号前的数据）,number
    :param fkrefusereason: 风控拒绝理由,string
    :param allowreapply: 允许再次进件,boolean
    :param ywrefusereason: 业务拒绝理由,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2608')
    requesturl = baseUrl + "/auditing/finalAuditing/finalSubmit"
    LOGGER.info("xqh_终审提交(v1.0.0修改)请求地址:【{}】".format(requesturl))
    params = dict()
    params["allowReApply"] = allowreapply
    params["auditOpinion"] = auditopinion
    params["auditState"] = auditstate
    params["fkRefuseReason"] = fkrefusereason
    params["operateId"] = operateid
    params["orderId"] = orderid
    params["riskControlPaymentProportion"] = riskcontrolpaymentproportion
    params["ywRefuseReason"] = ywrefusereason
    LOGGER.info("xqh_终审提交(v1.0.0修改)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_终审提交(v1.0.0修改)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_orderAuditing_result_basicInfo(orderid, userid):
    """
    xqh_信审详情-基本信息（一审，二审，终审）（包括尾部的操作日志）
    :param userid: ,
    :param orderid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2609')
    requesturl = baseUrl + "/auditing/orderAuditing/result/basicInfo"
    LOGGER.info("xqh_信审详情-基本信息（一审，二审，终审）（包括尾部的操作日志）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["userId"] = userid
    LOGGER.info("xqh_信审详情-基本信息（一审，二审，终审）（包括尾部的操作日志）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_信审详情-基本信息（一审，二审，终审）（包括尾部的操作日志）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_finalAuditing_finalAuditOpenLock(operateid, orderid):
    """
    终审未处理数据打开锁定
    :param orderid: 订单id,number
    :param operateid: 操作人员id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2610')
    requesturl = baseUrl + "/auditing/finalAuditing/finalAuditOpenLock"
    LOGGER.info("终审未处理数据打开锁定请求地址:【{}】".format(requesturl))
    params = dict()
    params["operateId"] = operateid
    params["orderId"] = orderid
    LOGGER.info("终审未处理数据打开锁定请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审未处理数据打开锁定请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_getVideoAuthList(orderid):
    """
    获取视频认证列表（v1.0.0新加）（一二终审公用）
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2611')
    requesturl = baseUrl + "/auditing/getVideoAuthList"
    LOGGER.info("获取视频认证列表（v1.0.0新加）（一二终审公用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("获取视频认证列表（v1.0.0新加）（一二终审公用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取视频认证列表（v1.0.0新加）（一二终审公用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_system_dictionary_query(type):
    """
    xqh_审核拒绝理由-查询
    :param type: 型  （ 风控还是 业务）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2612')
    requesturl = baseUrl + "/system/dictionary/query"
    LOGGER.info("xqh_审核拒绝理由-查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    LOGGER.info("xqh_审核拒绝理由-查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_审核拒绝理由-查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_goodsInfo_viewPartnerInfo(orderid):
    """
    xqh_详情（商户信息）
    :param orderid: 订单号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2613')
    requesturl = baseUrl + "/auditing/goodsInfo/viewPartnerInfo"
    LOGGER.info("xqh_详情（商户信息）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("xqh_详情（商户信息）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_详情（商户信息）请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_secondaryAudit_secondaryAuditHandel(allowreapply, fkrefusereason, operateid, orderid, result, secondaryauditopinion, supplementtwoauditremark, ywrefusereason):
    """
    xqh_二审提交
    :param allowreapply: 是否允许再申请,boolean
    :param fkrefusereason: 风控拒绝理由,string
    :param operateid: ,
    :param orderid: ,
    :param result: 2 通过，3拒绝，4 退回，5补充资料,
    :param secondaryauditopinion: ,
    :param ywrefusereason: 业务拒绝理由,string
    :param supplementtwoauditremark: 补充资料二审备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2614')
    requesturl = baseUrl + "/auditing/secondaryAudit/secondaryAuditHandel"
    LOGGER.info("xqh_二审提交请求地址:【{}】".format(requesturl))
    params = dict()
    params["allowReApply"] = allowreapply
    params["fkRefuseReason"] = fkrefusereason
    params["operateId"] = operateid
    params["orderId"] = orderid
    params["result"] = result
    params["secondaryAuditOpinion"] = secondaryauditopinion
    params["supplementTwoauditRemark"] = supplementtwoauditremark
    params["ywRefuseReason"] = ywrefusereason
    LOGGER.info("xqh_二审提交请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_二审提交请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_orderAuditing_result_modelResultHandle(allowreapply, auditmoney, fkrefusereason, model, orderid, refuse, remarks, result, supplementoneauditremark, userid, ywrefusereason):
    """
    xqh_一审提交和小模块审核
    :param allowreapply: 是否允许进件,boolean
    :param auditmoney: ,
    :param fkrefusereason: 风控拒绝理由,string
    :param model: ,
    :param orderid: ,
    :param refuse: ,
    :param remarks: ,
    :param result: 1 通过 2 拒绝 3 退回 4 补充资料,
    :param userid: ,
    :param ywrefusereason: 业务拒绝理由,string
    :param supplementoneauditremark: 补充资料一审备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2635')
    requesturl = baseUrl + "/auditing/orderAuditing/result/modelResultHandle"
    LOGGER.info("xqh_一审提交和小模块审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["allowReApply"] = allowreapply
    params["auditMoney"] = auditmoney
    params["fkRefuseReason"] = fkrefusereason
    params["model"] = model
    params["orderId"] = orderid
    params["refuse"] = refuse
    params["remarks"] = remarks
    params["result"] = result
    params["supplementOneauditRemark"] = supplementoneauditremark
    params["userId"] = userid
    params["ywRefuseReason"] = ywrefusereason
    LOGGER.info("xqh_一审提交和小模块审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("xqh_一审提交和小模块审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


