#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

from reborn.testAction import loginAction
import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog


baseUrl = 'http://192.168.15.129:9396'
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_reborn_service_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_platform_cm_base_deleteOperator(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/deleteOperator"
    LOGGER.info("删除渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_viewChannel(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannel"
    LOGGER.info("查询渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询渠道请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_saveChannel(city, name, province, region, shortname, parentchanneluuid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/saveChannel"
    LOGGER.info("添加渠道请求地址:【{}】".format(requesturl))
    params = {"city": city, "name": name, "province": province, "region": region, "shortName": shortname, "parentChannelUuid": parentchanneluuid}
    LOGGER.info("添加渠道请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_updateChannel(channeluuid, city, name, note, province, region, shortname, operatoruuid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/updateChannel"
    LOGGER.info("编辑渠道请求地址:【{}】".format(requesturl))
    params = {"channelUuid": channeluuid, "city": city, "name": name, "note": note, "province": province, "region": region, "shortName": shortname, "operatorUuid": operatoruuid}
    LOGGER.info("编辑渠道请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_examine_examine(isadopt, message, uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/examine"
    LOGGER.info("渠道审核请求地址:【{}】".format(requesturl))
    params = {"isAdopt": isadopt, "message": message, "uid": uid}
    LOGGER.info("渠道审核请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_viewChannels(pagesize, name, pagecurrent):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannels"
    LOGGER.info("渠道列表请求地址:【{}】".format(requesturl))
    params = {"pageSize": pagesize, "name": name, "pageCurrent": pagecurrent}
    LOGGER.info("渠道列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_updateFreezeState(uid, updatestate):
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateFreezeState"
    LOGGER.info("冻结渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("冻结渠道请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_updateOpenCloseState(uid, updatestate):
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateOpenCloseState"
    LOGGER.info("渠道开关请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("渠道开关请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_examine_viewExamineChannels(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/viewExamineChannels"
    LOGGER.info("渠道审核列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("渠道审核列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_viewStateChannels(name, pagecurrent, pagesize, openclosestate, freezestate, auditstate):
    requesturl = baseUrl + "/api/78dk/platform/cm/state/viewStateChannels"
    LOGGER.info("渠道状态列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "openCloseState": openclosestate, "freezeState": freezestate, "auditState": auditstate}
    LOGGER.info("渠道状态列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_deleteBusinessInfor(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除机构请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_viewBusinessInforByChannel(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/viewBusinessInforByChannel"
    LOGGER.info("根据渠道Uid查询机构请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询机构请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, channelormerchantuuid, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/saveBusinessInfor"
    LOGGER.info("添加机构请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("添加机构请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, channelormerchantuuid, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/updateBusinessInfor"
    LOGGER.info("编辑机构请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("编辑机构请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_deleteOperator(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/deleteOperator"
    LOGGER.info("删除操作员请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除操作员请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_viewOperator(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/viewOperator"
    LOGGER.info("查询操作员请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询操作员请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_saveOperator(mail, mobile, name, password, salt, title, channelormerchantuuid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/saveOperator"
    LOGGER.info("添加操作员请求地址:【{}】".format(requesturl))
    params = {"mail": mail, "mobile": mobile, "name": name, "password": password, "salt": salt, "title": title, "channelOrMerchantUuid": channelormerchantuuid}
    LOGGER.info("添加操作员请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_updateOperator(channelormerchantuuid, mail, mobile, name, operatoruuid, password, salt, title):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/updateOperator"
    LOGGER.info("编辑操作员请求地址:【{}】".format(requesturl))
    params = {"channelOrMerchantUuid": channelormerchantuuid, "mail": mail, "mobile": mobile, "name": name, "operatorUuid": operatoruuid, "password": password, "salt": salt, "title": title}
    LOGGER.info("编辑操作员请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_deleteClearingAccount(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/deleteClearingAccount"
    LOGGER.info("删除渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道结算账户信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/viewClearingAccountByChannel"
    LOGGER.info("根据渠道Uid查询渠道结算请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询渠道结算请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_saveClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/saveClearingAccount"
    LOGGER.info("添加渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("添加渠道结算账户信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_updateClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/updateClearingAccount"
    LOGGER.info("编辑渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("编辑渠道结算账户信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_deleteLegalPerson(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/deleteLegalPerson"
    LOGGER.info("删除渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道法人代表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(uid):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/viewLegalPersonByChannel"
    LOGGER.info("根据渠道Uid查询渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询渠道法人代表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
    LOGGER.info("添加渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("添加渠道法人代表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/updateLegalPerson"
    LOGGER.info("编辑渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("编辑渠道法人代表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewProvinceLists(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/common/viewProvinceLists"
    LOGGER.info("省级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("省级下拉请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewRegionLists(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/common/viewRegionLists"
    LOGGER.info("区/县级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("区/县级下拉请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewCityLists(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/common/viewCityLists"
    LOGGER.info("市级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("市级下拉请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_deleteFundSide(uid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/deleteFundSide"
    LOGGER.info("删除资方请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除资方请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_viewFundSide(uid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSide"
    LOGGER.info("查询资方请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询资方请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_saveFundSide(name, state):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/saveFundSide"
    LOGGER.info("添加资方请求地址:【{}】".format(requesturl))
    params = {"name": name, "state": state}
    LOGGER.info("添加资方请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_updateFundSide(fundsideuuid, name, state):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/updateFundSide"
    LOGGER.info("编辑资方请求地址:【{}】".format(requesturl))
    params = {"fundSideUuid": fundsideuuid, "name": name, "state": state}
    LOGGER.info("编辑资方请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_viewFundSides(name, pagecurrent, pagesize, state):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSides"
    LOGGER.info("资方列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("资方列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_deleteFundPackage(uid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/deleteFundPackage"
    LOGGER.info("删除资金包请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除资金包请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackage(uid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackage"
    LOGGER.info("查询资金包请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询资金包请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_saveFundPackage(amount, name, state, fundsideuuid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/saveFundPackage"
    LOGGER.info("添加资金包请求地址:【{}】".format(requesturl))
    params = {"amount": amount, "name": name, "state": state, "fundSideUuid": fundsideuuid}
    LOGGER.info("添加资金包请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_updateFundPackage(amount, fundpackageuuid, name, state, fundsideuuid):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/updateFundPackage"
    LOGGER.info("编辑资金包请求地址:【{}】".format(requesturl))
    params = {"amount": amount, "fundPackageUuid": fundpackageuuid, "name": name, "state": state, "fundSideUuid": fundsideuuid}
    LOGGER.info("编辑资金包请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackages(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_deleteProduct(uid):
    requesturl = baseUrl + "/api/78dk/platform/product/base/deleteProduct"
    LOGGER.info("删除产品模版请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除产品模版请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_viewProductDetail(uid):
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetail"
    LOGGER.info("查询产品模版请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询产品模版请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_saveProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, firsthalfofthemonth, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state, fundpackageuuid, electroniccontracttemplateuuid, incomingpartstemplateuuid, machineaudittemplateuuid, loanmode):
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
    LOGGER.info("添加产品模版请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle, "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee, "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth, "maxQuota": maxquota, "minQuota": minquota, "name": name, "overdueGracePeriod": overduegraceperiod, "overdueHandlingFeeRate": overduehandlingfeerate, "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs, "productState": productstate, "remark": remark, "repaymentDateType": repaymentdatetype, "repaymentMethod": repaymentmethod, "secondHalfOfTheMonth": secondhalfofthemonth, "state": state, "fundPackageUuid": fundpackageuuid, "electronicContractTemplateUuid": electroniccontracttemplateuuid, "incomingPartsTemplateUuid": incomingpartstemplateuuid, "machineAuditTemplateUuid": machineaudittemplateuuid, "loanMode": loanmode}
    LOGGER.info("添加产品模版请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_updateProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, firsthalfofthemonth, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productdetailuuid, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state, fundpackageuuid, incomingpartstemplateuuid, machineaudittemplateuuid, electroniccontracttemplateuuid, loanmode):
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
    LOGGER.info("编辑产品模版请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle, "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee, "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth, "maxQuota": maxquota, "minQuota": minquota, "name": name, "overdueGracePeriod": overduegraceperiod, "overdueHandlingFeeRate": overduehandlingfeerate, "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs, "productDetailUuid": productdetailuuid, "productState": productstate, "remark": remark, "repaymentDateType": repaymentdatetype, "repaymentMethod": repaymentmethod, "secondHalfOfTheMonth": secondhalfofthemonth, "state": state, "fundPackageUuid": fundpackageuuid, "incomingPartsTemplateUuid": incomingpartstemplateuuid, "machineAuditTemplateUuid": machineaudittemplateuuid, "electronicContractTemplateUuid": electroniccontracttemplateuuid, "loanMode": loanmode}
    LOGGER.info("编辑产品模版请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_viewProductDetails(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetails"
    LOGGER.info("产品列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("产品列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_updateProductState(uuid, productstate):
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProductState"
    LOGGER.info("修改产品状态请求地址:【{}】".format(requesturl))
    params = {"uuid": uuid, "productState": productstate}
    LOGGER.info("修改产品状态请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_viewFundPackages(name, pagecurrent, pagesize, state):
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewProductTemplateList(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductTemplateList"
    LOGGER.info("根据模板类型获取具体模板信息请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("根据模板类型获取具体模板信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_bindProductMerchant(merchanttx, merchantuuids, productuuid):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/bindProductMerchant"
    LOGGER.info("绑定产品和商户关系请求地址:【{}】".format(requesturl))
    params = {"merchantTX": merchanttx, "merchantUuids": merchantuuids, "productUuid": productuuid}
    LOGGER.info("绑定产品和商户关系请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_saveMerchantTX(discountrate, merchantuuid, period, productdetailconfiguuid, rate):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "merchantUuid": merchantuuid, "period": period, "productDetailConfigUuid": productdetailconfiguuid, "rate": rate}
    LOGGER.info("保存商户贴息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_findMerchantTX(merchantuuid, productuuid):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/findMerchantTX"
    LOGGER.info("查询商户贴息请求地址:【{}】".format(requesturl))
    params = {"merchantUuid": merchantuuid, "productUuid": productuuid}
    LOGGER.info("查询商户贴息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(name, pagecurrent, pagesize, uuid):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewNotInMerchantsByPuid"
    LOGGER.info("根据产品id查询不相关的商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid}
    LOGGER.info("根据产品id查询不相关的商户列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(name, pagecurrent, pagesize, uuid):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewInMerchantsByPuid"
    LOGGER.info("根据产品id查询相关的商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid}
    LOGGER.info("根据产品id查询相关的商户列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_unBindProductMerchant(merchantuuids, productuuid):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/unBindProductMerchant"
    LOGGER.info("解绑产品和商户关系请求地址:【{}】".format(requesturl))
    params = {"merchantUuids": merchantuuids, "productUuid": productuuid}
    LOGGER.info("解绑产品和商户关系请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewProductDetails(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductDetails"
    LOGGER.info("查看产品信息列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查看产品信息列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_updateMerchant(merchantuuid, name, note, parentmerchantuuid, shortname, channeluuid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
    LOGGER.info("修改基本信息请求地址:【{}】".format(requesturl))
    params = {"merchantUuid": merchantuuid, "name": name, "note": note, "parentMerchantUuid": parentmerchantuuid, "shortName": shortname, "channelUuid": channeluuid}
    LOGGER.info("修改基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_deleteMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/deleteMerchant"
    LOGGER.info("删除基本信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_saveMerchant(name, note, parentmerchantuuid, shortname, channeluuid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
    LOGGER.info("新增基本信息请求地址:【{}】".format(requesturl))
    params = {"name": name, "note": note, "parentMerchantUuid": parentmerchantuuid, "shortName": shortname, "channelUuid": channeluuid}
    LOGGER.info("新增基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_viewMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
    LOGGER.info("查询基本信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询基本信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_viewMerchantList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
    LOGGER.info("查询商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_updateFreezeState(uid, updatestate):
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateFreezeState"
    LOGGER.info("下架状态请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("下架状态请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_updateOpenCloseState(uid, updatestate):
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateOpenCloseState"
    LOGGER.info("商户归档请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("商户归档请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_examine_merchanrExamine(ispass, message, uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/merchanrExamine"
    LOGGER.info("商户审核请求地址:【{}】".format(requesturl))
    params = {"isPass": ispass, "message": message, "uid": uid}
    LOGGER.info("商户审核请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_examine_viewExamineMerchantList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/viewExamineMerchantList"
    LOGGER.info("查询商户审核列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户审核列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_viewStateMerchantList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/mm/state/viewStateMerchantList"
    LOGGER.info("查询商户状态列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户状态列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_saveContractImages(key, merchantuuid, url):
    requesturl = baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存请求地址:【{}】".format(requesturl))
    params = {"key": key, "merchantUuid": merchantuuid, "url": url}
    LOGGER.info("影像资料保存请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_viewImageRoleList(uid, subdivisiontype):
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageRoleList"
    LOGGER.info("影像资料权限请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "subdivisionType": subdivisiontype}
    LOGGER.info("影像资料权限请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, channelormerchantuuid, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, businessprovincename, businesscityname, businessregionname, businesscity, businessprovince, businessregion, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/updateBusinessInfor"
    LOGGER.info("修改机构信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname, "businessCity": businesscity, "businessProvince": businessprovince, "businessRegion": businessregion, "documentCity": documentcity, "documentCityName": documentcityname, "documentProvince": documentprovince, "documentProvinceName": documentprovincename, "documentRegion": documentregion, "documentRegionName": documentregionname}
    LOGGER.info("修改机构信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_deleteBusinessInfor(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除机构信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, channelormerchantuuid, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/saveBusinessInfor"
    LOGGER.info("新增机构信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("新增机构信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/viewBusinessInforByMerchant"
    LOGGER.info("根据商户Uuid查询机构信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询机构信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/updateLegalPerson"
    LOGGER.info("修改法人信息请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("修改法人信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_deleteLegalPerson(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/deleteLegalPerson"
    LOGGER.info("删除法人信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除法人信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/saveLegalPerson"
    LOGGER.info("新增法人信息请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("新增法人信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/viewLegalPersonByMerchant"
    LOGGER.info("根据商户Uuid查询法人信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询法人信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_updateClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/updateClearingAccount"
    LOGGER.info("修改结算信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("修改结算信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_deleteClearingAccount(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/deleteClearingAccount"
    LOGGER.info("删除结算信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除结算信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/saveClearingAccount"
    LOGGER.info("新增结算信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("新增结算信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/viewClearingAccountByMerchant"
    LOGGER.info("根据商户Uuid查询结算信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询结算信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_updateStore(businessaddress, businessaddressgpsloction, managername, managerphone, merchantuuid, stormuuid, province, city, region, provincename, cityname, regionname, storename):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStore"
    LOGGER.info("修改门店信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "managerName": managername, "managerPhone": managerphone, "merchantUuid": merchantuuid, "stormUuid": stormuuid, "province": province, "city": city, "region": region, "provinceName": provincename, "cityName": cityname, "regionName": regionname, "storeName": storename}
    LOGGER.info("修改门店信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_deleteStore(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteStore"
    LOGGER.info("删除门店信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除门店信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_saveStore(businessaddress, businessaddressgpsloction, managername, managerphone, merchantuuid, stormuuid, storename, province, city, region, provincename, cityname, regionname):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
    LOGGER.info("新增门店信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "managerName": managername, "managerPhone": managerphone, "merchantUuid": merchantuuid, "stormUuid": stormuuid, "storeName": storename, "province": province, "city": city, "region": region, "provinceName": provincename, "cityName": cityname, "regionName": regionname}
    LOGGER.info("新增门店信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_viewStore(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStore"
    LOGGER.info("查询门店信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询门店信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_viewStoreList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
    LOGGER.info("查询门店列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询门店列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_uploadQrcode(storeuuid):
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/uploadQrcode"
    LOGGER.info("下载门店二维码请求地址:【{}】".format(requesturl))
    params = {"storeUuid": storeuuid}
    LOGGER.info("下载门店二维码请求参数：【{}】".format(params))
    response = requests.request('GET',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_merchantMoneyEnlarge(uid, zoomcoefficient):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/merchantMoneyEnlarge"
    LOGGER.info("修改预授信放大系数请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("修改预授信放大系数请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_updateMerchantMoney(amountday, amountmonth, amountsingle, amountsum, merchantuuid, moneyconfiguuid, zoomcoefficient):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
    LOGGER.info("修改额度管理请求地址:【{}】".format(requesturl))
    params = {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum, "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("修改额度管理请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_deleteMerchantMoney(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/deleteMerchantMoney"
    LOGGER.info("删除额度管理请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除额度管理请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_saveMerchantMoney(amountday, amountmonth, amountsingle, amountsum, merchantuuid, moneyconfiguuid, zoomcoefficient):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
    LOGGER.info("新增额度管理请求地址:【{}】".format(requesturl))
    params = {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum, "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("新增额度管理请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyByMerchant"
    LOGGER.info("根据商户Uuid查询额度管理请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询额度管理请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyList"
    LOGGER.info("风险控制列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("风险控制列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(platformprivilegeuuid, platformuseruuid):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
    LOGGER.info("新增/修改权限请求地址:【{}】".format(requesturl))
    params = {"platformPrivilegeUuid": platformprivilegeuuid, "platformUserUuid": platformuseruuid}
    LOGGER.info("新增/修改权限请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(permissiontype, platformuseruuid):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewUserPrivilegeList"
    LOGGER.info("查询权限请求地址:【{}】".format(requesturl))
    params = {"permissionType": permissiontype, "platformUserUuid": platformuseruuid}
    LOGGER.info("查询权限请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_clearUserPrivilege(uid):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/clearUserPrivilege"
    LOGGER.info("清除用户权限请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("清除用户权限请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_deleteMenu(uid):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/deleteMenu"
    LOGGER.info("删除一个菜单请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除一个菜单请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_saveMenu(name, url, platformprivilegeuuid):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveMenu"
    LOGGER.info("保存一个菜单请求地址:【{}】".format(requesturl))
    params = {"name": name, "url": url, "platformPrivilegeUuid": platformprivilegeuuid}
    LOGGER.info("保存一个菜单请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_viewMenus(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewMenus"
    LOGGER.info("查询所有菜单请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("查询所有菜单请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_updateSystemUser(email, mobile, name, platformuserprofileuuid):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUser"
    LOGGER.info("修改用户请求地址:【{}】".format(requesturl))
    params = {"email": email, "mobile": mobile, "name": name, "platformUserProfileUuid": platformuserprofileuuid}
    LOGGER.info("修改用户请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_deleteSystemUser(uid):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/deleteSystemUser"
    LOGGER.info("删除用户请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除用户请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_saveSystemUser(email, mobile, name):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/saveSystemUser"
    LOGGER.info("新增用户请求地址:【{}】".format(requesturl))
    params = {"email": email, "mobile": mobile, "name": name}
    LOGGER.info("新增用户请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUser(paramsingle):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUser"
    LOGGER.info("查询用户请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("查询用户请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_login(email, password):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = {"email": email, "password": password}
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUserList(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUserList"
    LOGGER.info("查询用户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询用户列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_resetUserPass(uid):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/resetUserPass"
    LOGGER.info("重置密码请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("重置密码请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_updateSystemUserState(uid, updatestate):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUserState"
    LOGGER.info("状态修改请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("状态修改请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_updateUserPass(passwordrepeat, email, password, uid):
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateUserPass"
    LOGGER.info("修改密码请求地址:【{}】".format(requesturl))
    params = {"passwordRepeat": passwordrepeat, "email": email, "password": password, "uid": uid}
    LOGGER.info("修改密码请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_FileUploadController_handlerFileUpload():
    requesturl = baseUrl + "/FileUploadController/handlerFileUpload"
    LOGGER.info("图片上传请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("图片上传请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_firstCheck(message, uuid, checkstate):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/firstCheck"
    LOGGER.info("初审请求地址:【{}】".format(requesturl))
    params = {"message": message, "uuid": uuid, "checkState": checkstate}
    LOGGER.info("初审请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContract(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
    LOGGER.info("初审信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("初审信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContracts(name, pagecurrent, pagesize, state):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
    LOGGER.info("初审列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("初审列表查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewTongdunInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewImageDataConfig(subdivisiontype):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewImageDataConfig"
    LOGGER.info("查询影像列表请求地址:【{}】".format(requesturl))
    params = {"subdivisionType": subdivisiontype}
    LOGGER.info("查询影像列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_selectCanAuditCheck(uid, checktype):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/selectCanAuditCheck"
    LOGGER.info("是否有权限审核请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "checkType": checktype}
    LOGGER.info("是否有权限审核请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewBaiDuInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewBaiDuInfo"
    LOGGER.info("查询百度接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询百度接口请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_saveSupplementImage(backgroundsupplementimages, contractuuid, supplementimagetype, auditchecktype):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveSupplementImage"
    LOGGER.info("提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = {"backGroundSupplementImages": backgroundsupplementimages, "contractUuid": contractuuid, "supplementImageType": supplementimagetype, "auditCheckType": auditchecktype}
    LOGGER.info("提交或编辑补录资料请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_getSupplementImages(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getSupplementImages"
    LOGGER.info("查询用户能补录的图片资料请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询用户能补录的图片资料请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_passContract(audituuid, contractuuid, description, supplementimagerequires, auditchecktype):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/passContract"
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求地址:【{}】".format(requesturl))
    params = {"auditUuid": audituuid, "contractUuid": contractuuid, "description": description, "supplementImageRequires": supplementimagerequires, "auditCheckType": auditchecktype}
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_delAuditComment(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/delAuditComment"
    LOGGER.info("删除一条评论请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除一条评论请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_findAuditCommentList(contractuuid, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findAuditCommentList"
    LOGGER.info("查询评论列表请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询评论列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_addAuditComment(auditcommentattachments, comment, contractuuid, replyauditcommentuuid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addAuditComment"
    LOGGER.info("添加一条评论请求地址:【{}】".format(requesturl))
    params = {"auditCommentAttachments": auditcommentattachments, "comment": comment, "contractUuid": contractuuid, "replyAuditCommentUuid": replyauditcommentuuid}
    LOGGER.info("添加一条评论请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_editAuditComment(auditcommentattachments, auditcommentuuid, comment, contractuuid, replyauditcommentuuid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/editAuditComment"
    LOGGER.info("编辑一条评论请求地址:【{}】".format(requesturl))
    params = {"auditCommentAttachments": auditcommentattachments, "auditCommentUuid": auditcommentuuid, "comment": comment, "contractUuid": contractuuid, "replyAuditCommentUuid": replyauditcommentuuid}
    LOGGER.info("编辑一条评论请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewTencentInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTencentInfo"
    LOGGER.info("查询腾讯接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询腾讯接口请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_updateContractInfoSignState(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/updateContractInfoSignState"
    LOGGER.info("修改合同状态为重签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("修改合同状态为重签请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findContractInfoSignStateWeb"
    LOGGER.info("修改法大大合同签署状态 修改为重签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("修改法大大合同签署状态 修改为重签请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogs(uuid, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogs"
    LOGGER.info("查询合同操作日志请求地址:【{}】".format(requesturl))
    params = {"uuid": uuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询合同操作日志请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_deleteContractCustomerLabel(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/deleteContractCustomerLabel"
    LOGGER.info("删除客户标签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除客户标签请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_addContractCustomerLabel(contractuuid, labelcontent):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addContractCustomerLabel"
    LOGGER.info("新增客户标签请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "labelContent": labelcontent}
    LOGGER.info("新增客户标签请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractLabels(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractLabels"
    LOGGER.info("通过合同UUID查询对应的客户标签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("通过合同UUID查询对应的客户标签请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogInfo(contractoperationloguuid, contractuuid):
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogInfo"
    LOGGER.info("查询操作日志详情请求地址:【{}】".format(requesturl))
    params = {"contractOperationLogUuid": contractoperationloguuid, "contractUuid": contractuuid}
    LOGGER.info("查询操作日志详情请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_telephoneCheck(checkstate, message, uuid):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/telephoneCheck"
    LOGGER.info("电核请求地址:【{}】".format(requesturl))
    params = {"checkState": checkstate, "message": message, "uuid": uuid}
    LOGGER.info("电核请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
    LOGGER.info("电核信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("电核信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(name, pagecurrent, pagesize, state):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContracts"
    LOGGER.info("电核列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("电核列表查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(answer, contractuuid, groupname, question, risktype, state, telephonecheckfeedbackuuid, groupsort, questionsort):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/addTelephoneCheckInfos"
    LOGGER.info("批量添加电核资料请求地址:【{}】".format(requesturl))
    params = {"answer": answer, "contractUuid": contractuuid, "groupName": groupname, "question": question, "riskType": risktype, "state": state, "telephoneCheckFeedbackUuid": telephonecheckfeedbackuuid, "groupSort": groupsort, "questionSort": questionsort}
    LOGGER.info("批量添加电核资料请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/deleteTelephoneCheckInfo"
    LOGGER.info("删除电核资料请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除电核资料请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFDDInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_finalCheck(message, uuid, checkstate):
    requesturl = baseUrl + "/api/78dk/platform/tm/final/finalCheck"
    LOGGER.info("终审请求地址:【{}】".format(requesturl))
    params = {"message": message, "uuid": uuid, "checkState": checkstate}
    LOGGER.info("终审请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContract(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContract"
    LOGGER.info("终审信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("终审信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContracts(name, pagecurrent, pagesize, state):
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
    LOGGER.info("终审列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("终审列表查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_after_viewAuditMonitors(enddate, pagecurrent, pagesize, qifascore, searchwhere, startdate):
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewAuditMonitors"
    LOGGER.info("贷后列表请求地址:【{}】".format(requesturl))
    params = {"endDate": enddate, "pageCurrent": pagecurrent, "pageSize": pagesize, "qifaScore": qifascore, "searchWhere": searchwhere, "startDate": startdate}
    LOGGER.info("贷后列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_after_viewReportContract(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewReportContract"
    LOGGER.info("查询报告内容请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询报告内容请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_after_viewContractTongDuns(uid):
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewContractTongDuns"
    LOGGER.info("查询贷后所用同盾报告列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询贷后所用同盾报告列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewContracts(name, pagecurrent, pagesize, begindate, enddate, orderstate):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContracts"
    LOGGER.info("合同列表查询（申请列表）请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "begindate": begindate, "enddate": enddate, "orderState": orderstate}
    LOGGER.info("合同列表查询（申请列表）请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewContract(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContract"
    LOGGER.info("合同详情查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("合同详情查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTongdunInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewFDDInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewUserBill(name, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewUserBill"
    LOGGER.info("账单信息查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("账单信息查询请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewBaiDuInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewBaiDuInfo"
    LOGGER.info("查询百度接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询百度接口请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_downContracts(begindate, enddate, name, orderstate):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "name": name, "orderState": orderstate}
    LOGGER.info("导出申请列表请求参数：【{}】".format(params))
    response = requests.request('GET',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTencentInfo(uid):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTencentInfo"
    LOGGER.info("查询腾讯接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询腾讯接口请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_saveErpInfo(contractuuid, erpinfonumber):
    requesturl = baseUrl + "/api/78dk/platform/om/contract/saveErpInfo"
    LOGGER.info("保存合同ERP信息请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "erpInfoNumber": erpinfonumber}
    LOGGER.info("保存合同ERP信息请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_trans_findTransLogList(enddate, pagecurrent, pagesize, searchwhere, begindate, transstate, transtype):
    requesturl = baseUrl + "/api/78dk/platform/om/trans/findTransLogList"
    LOGGER.info("交易流水列表请求地址:【{}】".format(requesturl))
    params = {"enddate": enddate, "pageCurrent": pagecurrent, "pageSize": pagesize, "searchWhere": searchwhere, "begindate": begindate, "transState": transstate, "transType": transtype}
    LOGGER.info("交易流水列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_offlineBalanceInit(contractnumber, number, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/offlineBalanceInit"
    LOGGER.info("手动还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "number": number, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("手动还款 结余计算 初始化请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_addRepayManualApply(actualamt, billperiod, contractuuid, optway):
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/addRepayManualApply"
    LOGGER.info("添加 手动还款申请请求地址:【{}】".format(requesturl))
    params = {"actualAmt": actualamt, "billPeriod": billperiod, "contractUuid": contractuuid, "optWay": optway}
    LOGGER.info("添加 手动还款申请请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findRepayCommons"
    LOGGER.info("获取 手动扣款 列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取 手动扣款 列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_findManuelHistoryList(billperiod, contractuuid, pagecurrent, pagesize):
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findManuelHistoryList"
    LOGGER.info("获取 手动扣款历史记录请求地址:【{}】".format(requesturl))
    params = {"billPeriod": billperiod, "contractUuid": contractuuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("获取 手动扣款历史记录请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceInit(contractnumber):
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceInit"
    LOGGER.info("提前还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber}
    LOGGER.info("提前还款 结余计算 初始化请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceRefresh(contractnumber, optway, prepaymenthandlingfeeremission, repayamt):
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceRefresh"
    LOGGER.info("提前还款 结余计算 刷新接口请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "optWay": optway, "prepaymentHandlingFeeRemission": prepaymenthandlingfeeremission, "repayAmt": repayamt}
    LOGGER.info("提前还款 结余计算 刷新接口请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_addRepayManualApply(contractuuid, optway, reliefamt, actualamt, bankseqid, remarks, urls, actualrepaydate, prepaymenthandlingfee):
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/addRepayManualApply"
    LOGGER.info("添加 提前还款申请请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "optWay": optway, "reliefAmt": reliefamt, "actualAmt": actualamt, "bankSeqId": bankseqid, "remarks": remarks, "urls": urls, "actualRepayDate": actualrepaydate, "prepaymentHandlingFee": prepaymenthandlingfee}
    LOGGER.info("添加 提前还款申请请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_findRepayPrepayments(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/findRepayPrepayments"
    LOGGER.info("获取提前还款列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取提前还款列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_addRepayManualApply(actualamt, bankseqid, billperiod, contractuuid, optway, remarks, urls):
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/addRepayManualApply"
    LOGGER.info("添加 线下还款申请请求地址:【{}】".format(requesturl))
    params = {"actualAmt": actualamt, "bankSeqId": bankseqid, "billPeriod": billperiod, "contractUuid": contractuuid, "optWay": optway, "remarks": remarks, "urls": urls}
    LOGGER.info("添加 线下还款申请请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_offlineBalanceInit(contractnumber, number):
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/offlineBalanceInit"
    LOGGER.info("线下还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "number": number}
    LOGGER.info("线下还款 结余计算 初始化请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/findRepayCommons"
    LOGGER.info("获取 线下还款列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取 线下还款列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_file_download(urlstr, filename):
    requesturl = baseUrl + "/api/78dk/platform/file/download"
    LOGGER.info("文件下载请求地址:【{}】".format(requesturl))
    params = {"urlStr": urlstr, "filename": filename}
    LOGGER.info("文件下载请求参数：【{}】".format(params))
    response = requests.request('GET',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_range_deleteMerchantManagementRange(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/range/deleteMerchantManagementRange"
    LOGGER.info("商户经营范围删除请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("商户经营范围删除请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_range_addMerchantManagementRange(city, cityname, created, merchantuuid, province, provincename, updated):
    requesturl = baseUrl + "/api/78dk/platform/mm/range/addMerchantManagementRange"
    LOGGER.info("商户经营范围新增请求地址:【{}】".format(requesturl))
    params = {"city": city, "cityName": cityname, "created": created, "merchantUuid": merchantuuid, "province": province, "provinceName": provincename, "updated": updated}
    LOGGER.info("商户经营范围新增请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_range_findMMRByMerchantUuid(uid):
    requesturl = baseUrl + "/api/78dk/platform/mm/range/findMMRByMerchantUuid"
    LOGGER.info("通过商户uuid查询商户经营范围请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("通过商户uuid查询商户经营范围请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_lm_loanOperation(bankseqid, contractuuid, loanamount, remarks, urls):
    requesturl = baseUrl + "/api/78dk/platform/om/lm/loanOperation"
    LOGGER.info("放款操作请求地址:【{}】".format(requesturl))
    params = {"bankSeqId": bankseqid, "contractUuid": contractuuid, "loanAmount": loanamount, "remarks": remarks, "urls": urls}
    LOGGER.info("放款操作请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_lm_findLoanModeList(pagecurrent, pagesize, searchwhere):
    requesturl = baseUrl + "/api/78dk/platform/om/lm/findLoanModeList"
    LOGGER.info("查询线下放款列表请求地址:【{}】".format(requesturl))
    params = {"pageCurrent": pagecurrent, "pageSize": pagesize, "searchWhere": searchwhere}
    LOGGER.info("查询线下放款列表请求参数：【{}】".format(params))
    response = requests.request('POST',requesturl, params=params)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


