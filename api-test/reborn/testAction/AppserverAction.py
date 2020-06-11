#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppserverAction.py
@desc       : 项目：reborn 模块：appserver 接口方法封装
"""

from reborn.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('appserver_apiURL', 'reborn')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_appserver_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_app_periods_applyPeriods(amount, extra, method, period, periodmoney, productdetailuuid, recommendcode, systemamount, userlocation):
    """
    申请分期
    :param productdetailuuid: 产品uuid,string
    :param extra: 扩展参数 ，选填,string
    :param amount: 总金额(Y),number
    :param userlocation: 用户位置信息(N),string
    :param method: 还款方式(Y),string
    :param period: 还款期数(Y),number
    :param periodmoney: 每期还款金额(Y),number
    :param recommendcode: 推荐码,string
    :param systemamount: 系统额度,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 493')
    requesturl = baseUrl + "/api/78dk/app/periods/applyPeriods"
    LOGGER.info("申请分期请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["extra"] = extra
    params["method"] = method
    params["period"] = period
    params["periodMoney"] = periodmoney
    params["productDetailUuid"] = productdetailuuid
    params["recommendCode"] = recommendcode
    params["systemAmount"] = systemamount
    params["userLocation"] = userlocation
    LOGGER.info("申请分期请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请分期请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getConsumption(extra, paramsingle, preferential, productdetailuuid):
    """
    获取额度测评
    :param paramsingle: 用户位置信息(Y),string
    :param productdetailuuid: 产品UUID(非必填，有就传，没有就不传),string
    :param extra: 扩展参数（非必填，有就传，没有就不传）,string
    :param preferential: 是否贴息（Y，必填参数）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 494')
    requesturl = baseUrl + "/api/78dk/app/periods/getConsumption"
    LOGGER.info("获取额度测评请求地址:【{}】".format(requesturl))
    params = dict()
    params["extra"] = extra
    params["paramSingle"] = paramsingle
    params["preferential"] = preferential
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("获取额度测评请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取额度测评请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getPeriodsOptions(money, productdetailuuid):
    """
    获取申请分期
    :param productdetailuuid: 产品信息,string
    :param money: 分期金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 495')
    requesturl = baseUrl + "/api/78dk/app/periods/getPeriodsOptions"
    LOGGER.info("获取申请分期请求地址:【{}】".format(requesturl))
    params = dict()
    params["money"] = money
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("获取申请分期请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取申请分期请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_postUserInfo(communicationcityid, communicationdistrictid, communicationinputaddress, communicationprovinceid, decorationcityid, decorationdistrictid, decorationinputaddress, decorationprovinceid, house, idcard, immediatefamily, job, kinsfolkphone, loanuse, phone, relationship, templatetype, username):
    """
    填写基本信息
    :param decorationdistrictid: 装修地址-区/县,number
    :param decorationinputaddress: 装修地址-详细,string
    :param idcard: 身份证,string
    :param loanuse: 贷款用途,string
    :param house: 房产类型,string
    :param phone: 手机号,string
    :param job: 职业类型,string
    :param templatetype: 产品类型,string
    :param decorationprovinceid: 装修地址-省,number
    :param immediatefamily: 亲属姓名,string
    :param kinsfolkphone: 亲属电话,string
    :param communicationinputaddress: 通讯地址-手入地址,string
    :param decorationcityid: 装修地址-市,number
    :param communicationcityid: 通讯地址-市 id,number
    :param username: 姓名,string
    :param communicationdistrictid: 通讯地址-区/县 id,number
    :param relationship: 亲属关系,string
    :param communicationprovinceid: 通讯地址-省 id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 496')
    requesturl = baseUrl + "/api/78dk/app/periods/postUserInfo"
    LOGGER.info("填写基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["communicationCityId"] = communicationcityid
    params["communicationDistrictId"] = communicationdistrictid
    params["communicationInputAddress"] = communicationinputaddress
    params["communicationProvinceId"] = communicationprovinceid
    params["decorationCityId"] = decorationcityid
    params["decorationDistrictId"] = decorationdistrictid
    params["decorationInputAddress"] = decorationinputaddress
    params["decorationProvinceId"] = decorationprovinceid
    params["house"] = house
    params["idcard"] = idcard
    params["immediatefamily"] = immediatefamily
    params["job"] = job
    params["kinsfolkphone"] = kinsfolkphone
    params["loanUse"] = loanuse
    params["phone"] = phone
    params["relationship"] = relationship
    params["templateType"] = templatetype
    params["username"] = username
    LOGGER.info("填写基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("填写基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_certification(idcard, phone, username, verifycode):
    """
    实名认证
    :param phone: 手机号,string
    :param verifycode: 验证码,string
    :param username: 姓名,string
    :param idcard: 身份证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 497')
    requesturl = baseUrl + "/api/78dk/app/periods/certification"
    LOGGER.info("实名认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["phone"] = phone
    params["username"] = username
    params["verifycode"] = verifycode
    LOGGER.info("实名认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("实名认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getVerify(mobile):
    """
    获取短信验证码
    :param mobile: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 498')
    requesturl = baseUrl + "/api/78dk/app/periods/getVerify"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_image_saveContractImages(key, url):
    """
    影像资料保存
    :param key: 图片配置key(Y),string
    :param url: 图片相对URL(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 499')
    requesturl = baseUrl + "/api/78dk/app/loan/image/saveContractImages"
    LOGGER.info("影像资料保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    params["url"] = url
    LOGGER.info("影像资料保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_image_viewImageRoleList(subdivisiontype, uid):
    """
    影像资料权限
    :param uid: 合同Uuid,string
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 500')
    requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageRoleList"
    LOGGER.info("影像资料权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["subdivisionType"] = subdivisiontype
    params["uid"] = uid
    LOGGER.info("影像资料权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_image_saveSupplementImage(datalists, uid):
    """
    影像资料补录保存
    :param uid: 合同Uuid(Y),string
    :param datalists: 影像资料列表(Y),array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 501')
    requesturl = baseUrl + "/api/78dk/app/loan/image/saveSupplementImage"
    LOGGER.info("影像资料补录保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["dataLists"] = datalists
    params["uid"] = uid
    LOGGER.info("影像资料补录保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料补录保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_image_viewImageSupplementList(uid):
    """
    影像资料补录列表
    :param uid: 合同Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 502')
    requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageSupplementList"
    LOGGER.info("影像资料补录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("影像资料补录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料补录列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_getUserInfo(authcode, preferential, storeuuid):
    """
    获取用户信息
    :param storeuuid: 门店/商户id(N),string
    :param authcode: 用户权限编码(Y),string
    :param preferential: 商户门店优惠(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 503')
    requesturl = baseUrl + "/api/78dk/app/base/getUserInfo"
    LOGGER.info("获取用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["authCode"] = authcode
    params["preferential"] = preferential
    params["storeUuid"] = storeuuid
    LOGGER.info("获取用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_alipay_getAlipayVid():
    """
    获取支付宝验签Vid
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 504')
    requesturl = baseUrl + "/api/78dk/app/loan/alipay/getAlipayVid"
    LOGGER.info("获取支付宝验签Vid请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取支付宝验签Vid请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取支付宝验签Vid请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_getFddUrl():
    """
    获取法大大合同地址
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 505')
    requesturl = baseUrl + "/api/78dk/app/base/getFddUrl"
    LOGGER.info("获取法大大合同地址请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取法大大合同地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取法大大合同地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_getFddResult():
    """
    获取法大大合同签订结果
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 506')
    requesturl = baseUrl + "/api/78dk/app/base/getFddResult"
    LOGGER.info("获取法大大合同签订结果请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取法大大合同签订结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取法大大合同签订结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getUserInfo():
    """
    查询基本信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 507')
    requesturl = baseUrl + "/api/78dk/app/periods/getUserInfo"
    LOGGER.info("查询基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_getWsAuditResult():
    """
    网商进件
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 508')
    requesturl = baseUrl + "/api/78dk/app/base/getWsAuditResult"
    LOGGER.info("网商进件请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("网商进件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商进件请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getContractInfoSignState(uid):
    """
    查询合同签约状态（判断是否重新签署）
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 509')
    requesturl = baseUrl + "/api/78dk/app/periods/getContractInfoSignState"
    LOGGER.info("查询合同签约状态（判断是否重新签署）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询合同签约状态（判断是否重新签署）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同签约状态（判断是否重新签署）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_findRepayPlanList(loanmoney, loanperiod, productuuid):
    """
    查询还款计划-进件流程中
    :param loanmoney: 贷款金额（Y）,string
    :param loanperiod: 贷款期数（Y）,string
    :param productuuid: 贷款产品uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 510')
    requesturl = baseUrl + "/api/78dk/app/periods/findRepayPlanList"
    LOGGER.info("查询还款计划-进件流程中请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanMoney"] = loanmoney
    params["loanPeriod"] = loanperiod
    params["productUuid"] = productuuid
    LOGGER.info("查询还款计划-进件流程中请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询还款计划-进件流程中请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_findMerchantProductInfo(productuuid):
    """
    根据商户uuid(或者及产品uuid)获取产品信息
    :param productuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 511')
    requesturl = baseUrl + "/api/78dk/app/periods/findMerchantProductInfo"
    LOGGER.info("根据商户uuid(或者及产品uuid)获取产品信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["productUuid"] = productuuid
    LOGGER.info("根据商户uuid(或者及产品uuid)获取产品信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户uuid(或者及产品uuid)获取产品信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_findProductDetailTemplateConfig(uid):
    """
    查询其对应的进件模板信息
    :param uid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 512')
    requesturl = baseUrl + "/api/78dk/app/periods/findProductDetailTemplateConfig"
    LOGGER.info("查询其对应的进件模板信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询其对应的进件模板信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询其对应的进件模板信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_hasContractUuid():
    """
    查询是否下单
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 513')
    requesturl = baseUrl + "/api/78dk/app/periods/hasContractUuid"
    LOGGER.info("查询是否下单请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询是否下单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询是否下单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_addPersonBasicBank(bankname, banknumber, branchbankname, checkcode, city, contractuuid, idcardnumber, linenumber, name, personaccounttype, personbasicinfouuid, phone, province):
    """
    添加用户银行卡资料信息
    :param personbasicinfouuid: 用户进件资料UUID,string
    :param branchbankname: 支行名称,string
    :param name: 姓名,string
    :param bankname: 银行名称,string
    :param personaccounttype: 账户类型,string
    :param linenumber: 联行行号,string
    :param city: 开户行地址-市,number
    :param phone: 手机号,string
    :param banknumber: 银行卡号,string
    :param contractuuid: 合同UUID,string
    :param province: 开户行地址-省,number
    :param idcardnumber: 身份证号,string
    :param checkcode: 短信验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 514')
    requesturl = baseUrl + "/api/78dk/app/periods/addPersonBasicBank"
    LOGGER.info("添加用户银行卡资料信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankName"] = bankname
    params["bankNumber"] = banknumber
    params["branchBankName"] = branchbankname
    params["checkCode"] = checkcode
    params["city"] = city
    params["contractUuid"] = contractuuid
    params["idcardnumber"] = idcardnumber
    params["lineNumber"] = linenumber
    params["name"] = name
    params["personAccountType"] = personaccounttype
    params["personBasicInfoUuid"] = personbasicinfouuid
    params["phone"] = phone
    params["province"] = province
    LOGGER.info("添加用户银行卡资料信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加用户银行卡资料信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_vaildBankInfo(bankname, banknumber, idcardnumber, name, phone):
    """
    银行卡四要素验证
    :param name: 姓名,string
    :param phone: 手机号,string
    :param bankname: 银行名称,string
    :param banknumber: 银行卡号,string
    :param idcardnumber: 身份证号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 515')
    requesturl = baseUrl + "/api/78dk/app/periods/vaildBankInfo"
    LOGGER.info("银行卡四要素验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankName"] = bankname
    params["bankNumber"] = banknumber
    params["idcardnumber"] = idcardnumber
    params["name"] = name
    params["phone"] = phone
    LOGGER.info("银行卡四要素验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡四要素验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_selectBankInfo(contractnumber, tokenid):
    """
    网商订单关闭-v3.2.2
    :param  contractnumber : 订单编号,string
    :param  tokenid : tokenid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 516')
    requesturl = baseUrl + "/api/78dk/app/periods/selectBankInfo"
    LOGGER.info("网商订单关闭-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["tokenId"] = tokenid
    LOGGER.info("网商订单关闭-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商订单关闭-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_selectFrontVO():
    """
    根据合同UUID查询用户基本资料
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 517')
    requesturl = baseUrl + "/api/78dk/app/periods/selectFrontVO"
    LOGGER.info("根据合同UUID查询用户基本资料请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("根据合同UUID查询用户基本资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据合同UUID查询用户基本资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_base_getVerify(mobile):
    """
    获取手机验证短信码
    :param mobile: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 518')
    requesturl = baseUrl + "/api/78dk/base/getVerify"
    LOGGER.info("获取手机验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    LOGGER.info("获取手机验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手机验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_user_getUserInfo():
    """
    获取个人信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 519')
    requesturl = baseUrl + "/api/78dk/app/user/getUserInfo"
    LOGGER.info("获取个人信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取个人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取个人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_apply_getRecords(pagecurrent, pagesize):
    """
    获取申请记录
    :param pagecurrent: 当前页,number
    :param pagesize: 每页大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 520')
    requesturl = baseUrl + "/api/78dk/app/apply/getRecords"
    LOGGER.info("获取申请记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("获取申请记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取申请记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_apply_getRepaymentPlan(pagecurrent, pagesize, paraminfo):
    """
    获取还款计划
    :param paraminfo: 合同Uuid,string
    :param pagecurrent: 当前页,number
    :param pagesize: 每页大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 521')
    requesturl = baseUrl + "/api/78dk/app/apply/getRepaymentPlan"
    LOGGER.info("获取还款计划请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["paramInfo"] = paraminfo
    LOGGER.info("获取还款计划请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取还款计划请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_apply_getRecordByUuid(paraminfo):
    """
    查询单条申请记录
    :param paraminfo: 合同Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 522')
    requesturl = baseUrl + "/api/78dk/app/apply/getRecordByUuid"
    LOGGER.info("查询单条申请记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramInfo"] = paraminfo
    LOGGER.info("查询单条申请记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询单条申请记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_getFddCheckUrl(uid):
    """
    获取法大大合同查看地址
    :param uid: 合同Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 523')
    requesturl = baseUrl + "/api/78dk/app/base/getFddCheckUrl"
    LOGGER.info("获取法大大合同查看地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("获取法大大合同查看地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取法大大合同查看地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_list_viewRegionLists(paramsingle):
    """
    获取区/县下拉列表
    :param paramsingle: 上级编码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 524')
    requesturl = baseUrl + "/api/78dk/app/base/list/viewRegionLists"
    LOGGER.info("获取区/县下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("获取区/县下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取区/县下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_list_viewCityLists(paramsingle):
    """
    获取市下拉列表
    :param paramsingle: 上级编码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 525')
    requesturl = baseUrl + "/api/78dk/app/base/list/viewCityLists"
    LOGGER.info("获取市下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("获取市下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取市下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_list_viewProvinceLists():
    """
    获取省下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 526')
    requesturl = baseUrl + "/api/78dk/app/base/list/viewProvinceLists"
    LOGGER.info("获取省下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取省下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取省下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_image_saveGroundSupplementImage(auditchecktype, audituuid, backgroundsupplementimages, bdid, contractnumber, contractuuid, supplementimagetype):
    """
    app后台提交或编辑补录资料
    :param backgroundsupplementimages: 后台补录资料实体,array<object>
    :param contractuuid: 合同UUID,string
    :param bdid: 业务人员唯一标识,string
    :param auditchecktype: 审核类型,string
    :param contractnumber: 合同编号,string
    :param supplementimagetype: 后台编辑或提交类型,string
    :param audituuid: 审核人员UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 527')
    requesturl = baseUrl + "/api/78dk/app/image/saveGroundSupplementImage"
    LOGGER.info("app后台提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["auditUuid"] = audituuid
    params["backGroundSupplementImages"] = backgroundsupplementimages
    params["bdid"] = bdid
    params["contractNumber"] = contractnumber
    params["contractUuid"] = contractuuid
    params["supplementImageType"] = supplementimagetype
    LOGGER.info("app后台提交或编辑补录资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("app后台提交或编辑补录资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_image_findContractImages(uid):
    """
    app查询影像资料
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 528')
    requesturl = baseUrl + "/api/78dk/app/image/findContractImages"
    LOGGER.info("app查询影像资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("app查询影像资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("app查询影像资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_image_getUploadToken():
    """
    查询七牛上传token与域名
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 529')
    requesturl = baseUrl + "/api/78dk/app/image/getUploadToken"
    LOGGER.info("查询七牛上传token与域名请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询七牛上传token与域名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询七牛上传token与域名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getVerifyIdByAlipayUser(tokenid):
    """
    网商VID获取-v3.2.2
    :param tokenid: 金螳螂tokenid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2206')
    requesturl = baseUrl + "/api/78dk/app/periods/getVerifyIdByAlipayUser"
    LOGGER.info("网商VID获取-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["tokenId"] = tokenid
    LOGGER.info("网商VID获取-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商VID获取-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_aliAdmittanceByAlipayUser(tokenid):
    """
    网商准入接口-v3.2.2
    :param tokenid: 金螳螂tokenid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2207')
    requesturl = baseUrl + "/api/78dk/app/periods/aliAdmittanceByAlipayUser"
    LOGGER.info("网商准入接口-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["tokenId"] = tokenid
    LOGGER.info("网商准入接口-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商准入接口-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getConsumptionByAlipayUser(tokenid, vid):
    """
    网商额度获取-v3.2.2
    :param  tokenid : 金螳螂tokenid,string
    :param  vid : 网商返回vid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2208')
    requesturl = baseUrl + "/api/78dk/app/periods/getConsumptionByAlipayUser"
    LOGGER.info("网商额度获取-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["tokenId"] = tokenid
    params["vid"] = vid
    LOGGER.info("网商额度获取-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商额度获取-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_getConsumptionUpgrade(creditamt, extra, paramsingle, preferential, productdetailuuid):
    """
    额度测评结果-v3.2.2
    :param  creditamt : 网商额度,string
    :param  extra : 扩展参数,string
    :param  paramsingle : 用户位置信息,string
    :param  preferential : 是否贴息,string
    :param  productdetailuuid : 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2209')
    requesturl = baseUrl + "/api/78dk/app/periods/getConsumptionUpgrade"
    LOGGER.info("额度测评结果-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["creditAmt"] = creditamt
    params["extra"] = extra
    params["paramSingle"] = paramsingle
    params["preferential"] = preferential
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("额度测评结果-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("额度测评结果-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_periods_applyPeriodsUpgrade(amount, contractnumber, extra, method, period, periodmoney, productdetailuuid, recommendcode, systemamount, userlocation):
    """
    申请分期产品-v3.2.2
    :param  amount : 总金额,string
    :param  contractnumber : 合同编号,string
    :param  extra: 扩展信息,string
    :param  method: 还款方式,string
    :param  period: 还款期数,number
    :param  productdetailuuid: 产品uuid,string
    :param  recommendcode: 推荐码,string
    :param  systemamount: 系统额度,string
    :param  userlocation: 银狐位置信息,string
    :param periodmoney: 没启还款金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2210')
    requesturl = baseUrl + "/api/78dk/app/periods/applyPeriodsUpgrade"
    LOGGER.info("申请分期产品-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["contractNumber"] = contractnumber
    params["extra"] = extra
    params["method"] = method
    params["period"] = period
    params["periodMoney"] = periodmoney
    params["productDetailUuid"] = productdetailuuid
    params["recommendCode"] = recommendcode
    params["systemAmount"] = systemamount
    params["userLocation"] = userlocation
    LOGGER.info("申请分期产品-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请分期产品-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_updateMerchantOrder():
    """
    网商订单更新-v3.2.2
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2211')
    requesturl = baseUrl + "/api/78dk/app/base/updateMerchantOrder"
    LOGGER.info("网商订单更新-v3.2.2请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("网商订单更新-v3.2.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("网商订单更新-v3.2.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


