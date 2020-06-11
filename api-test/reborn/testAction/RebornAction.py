#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from reborn.testAction import loginAction
import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog


baseUrl = 'http://192.168.15.129:9396'
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_reborn_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_app_periods_applyPeriods(amount, period, periodmoney, method, userlocation, productdetailuuid, extra):
    requesturl = baseUrl + "/api/78dk/app/periods/applyPeriods"
    LOGGER.info("申请分期请求地址:【{}】".format(requesturl))
    params = {"amount": amount, "period": period, "periodMoney": periodmoney, "method": method, "userLocation": userlocation, "productDetailUuid": productdetailuuid, "extra": extra}
    LOGGER.info("申请分期请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_getConsumption(paramsingle):
    requesturl = baseUrl + "/api/78dk/app/periods/getConsumption"
    LOGGER.info("获取额度测评请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("获取额度测评请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_getPeriodsOptions(money, productdetailuuid):
    requesturl = baseUrl + "/api/78dk/app/periods/getPeriodsOptions"
    LOGGER.info("获取申请分期请求地址:【{}】".format(requesturl))
    params = {"money": money, "productDetailUuid": productdetailuuid}
    LOGGER.info("获取申请分期请求参数：【{}】".format(params))
    response = requests.request('GET',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_postUserInfo(house, idcard, immediatefamily, job, kinsfolkphone, phone, relationship, username, decorationcityid, decorationdistrictid, decorationinputaddress, decorationprovinceid):
    requesturl = baseUrl + "/api/78dk/app/periods/postUserInfo"
    LOGGER.info("填写基本信息请求地址:【{}】".format(requesturl))
    params = {"house": house, "idcard": idcard, "immediatefamily": immediatefamily, "job": job, "kinsfolkphone": kinsfolkphone, "phone": phone, "relationship": relationship, "username": username, "decorationCityId": decorationcityid, "decorationDistrictId": decorationdistrictid, "decorationInputAddress": decorationinputaddress, "decorationProvinceId": decorationprovinceid}
    LOGGER.info("填写基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_certification(idcard, phone, username, verifycode):
    requesturl = baseUrl + "/api/78dk/app/periods/certification"
    LOGGER.info("实名认证请求地址:【{}】".format(requesturl))
    params = {"idcard": idcard, "phone": phone, "username": username, "verifycode": verifycode}
    LOGGER.info("实名认证请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_getVerify(mobile):
    requesturl = baseUrl + "/api/78dk/app/periods/getVerify"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = {"mobile": mobile}
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_loan_image_saveContractImages(key, url):
    requesturl = baseUrl + "/api/78dk/app/loan/image/saveContractImages"
    LOGGER.info("影像资料保存请求地址:【{}】".format(requesturl))
    params = {"key": key, "url": url}
    LOGGER.info("影像资料保存请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_loan_image_viewImageRoleList(uid, subdivisiontype):
    requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageRoleList"
    LOGGER.info("影像资料权限请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "subdivisionType": subdivisiontype}
    LOGGER.info("影像资料权限请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_loan_image_saveSupplementImage(datalists, uid):
    requesturl = baseUrl + "/api/78dk/app/loan/image/saveSupplementImage"
    LOGGER.info("影像资料补录保存请求地址:【{}】".format(requesturl))
    params = {"dataLists": datalists, "uid": uid}
    LOGGER.info("影像资料补录保存请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_loan_image_viewImageSupplementList(uid):
    requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageSupplementList"
    LOGGER.info("影像资料补录列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("影像资料补录列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_getUserInfo(authcode, storeuuid, preferential):
    requesturl = baseUrl + "/api/78dk/app/base/getUserInfo"
    LOGGER.info("获取用户信息请求地址:【{}】".format(requesturl))
    params = {"authCode": authcode, "storeUuid": storeuuid, "preferential": preferential}
    LOGGER.info("获取用户信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_loan_alipay_getAlipayVid():
    """
    获取支付宝验签Vid
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/loan/alipay/getAlipayVid"
    LOGGER.info("获取支付宝验签Vid请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("获取支付宝验签Vid请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_getFddUrl():
    """
    获取法大大合同地址
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/base/getFddUrl"
    LOGGER.info("获取法大大合同地址请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("获取法大大合同地址请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_getFddResult():
    """
    获取法大大合同签订结果
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/base/getFddResult"
    LOGGER.info("获取法大大合同签订结果请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("获取法大大合同签订结果请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_getUserInfo():
    """
    查询基本信息
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/periods/getUserInfo"
    LOGGER.info("查询基本信息请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("查询基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_getWsAuditResult():
    """
    网商进件
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/base/getWsAuditResult"
    LOGGER.info("网商进件请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("网商进件请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_getContractInfoSignState(uid):
    requesturl = baseUrl + "/api/78dk/app/periods/getContractInfoSignState"
    LOGGER.info("查询合同签约状态（判断是否重新签署）请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询合同签约状态（判断是否重新签署）请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_findRepayPlanList(loanmoney, loanperiod, productuuid):
    requesturl = baseUrl + "/api/78dk/app/periods/findRepayPlanList"
    LOGGER.info("查询还款计划-进件流程中请求地址:【{}】".format(requesturl))
    params = {"loanMoney": loanmoney, "loanPeriod": loanperiod, "productUuid": productuuid}
    LOGGER.info("查询还款计划-进件流程中请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_findMerchantProductInfo(productuuid):
    requesturl = baseUrl + "/api/78dk/app/periods/findMerchantProductInfo"
    LOGGER.info("根据商户uuid(或者及产品uuid)获取产品信息请求地址:【{}】".format(requesturl))
    params = {"productUuid": productuuid}
    LOGGER.info("根据商户uuid(或者及产品uuid)获取产品信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_findProductDetailTemplateConfig(uid):
    requesturl = baseUrl + "/api/78dk/app/periods/findProductDetailTemplateConfig"
    LOGGER.info("查询其对应的进件模板信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询其对应的进件模板信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_periods_hasContractUuid():
    """
    查询是否下单
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/periods/hasContractUuid"
    LOGGER.info("查询是否下单请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("查询是否下单请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_user_getUserInfo():
    """
    获取个人信息
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/user/getUserInfo"
    LOGGER.info("获取个人信息请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("获取个人信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_apply_getRecords(pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/app/apply/getRecords"
    LOGGER.info("获取申请记录请求地址:【{}】".format(requesturl))
    params = {"pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("获取申请记录请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_apply_getRepaymentPlan(pagesize, pagecurrent, paraminfo):
    requesturl = baseUrl + "/api/78dk/app/apply/getRepaymentPlan"
    LOGGER.info("获取还款计划请求地址:【{}】".format(requesturl))
    params = {"pageSize": pagesize, "pageCurrent": pagecurrent, "paramInfo": paraminfo}
    LOGGER.info("获取还款计划请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_apply_getRecordByUuid(paraminfo):
    requesturl = baseUrl + "/api/78dk/app/apply/getRecordByUuid"
    LOGGER.info("查询单条申请记录请求地址:【{}】".format(requesturl))
    params = {"paramInfo": paraminfo}
    LOGGER.info("查询单条申请记录请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_getFddCheckUrl(uid):
    requesturl = baseUrl + "/api/78dk/app/base/getFddCheckUrl"
    LOGGER.info("获取法大大合同查看地址请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("获取法大大合同查看地址请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_list_viewRegionLists(paramsingle):
    requesturl = baseUrl + "/api/78dk/app/base/list/viewRegionLists"
    LOGGER.info("获取区/县下拉列表请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("获取区/县下拉列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_list_viewCityLists(paramsingle):
    requesturl = baseUrl + "/api/78dk/app/base/list/viewCityLists"
    LOGGER.info("获取市下拉列表请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("获取市下拉列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_app_base_list_viewProvinceLists():
    """
    获取省下拉列表
    :return: response.text
    """
    requesturl = baseUrl + "/api/78dk/app/base/list/viewProvinceLists"
    LOGGER.info("获取省下拉列表请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("获取省下拉列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


