#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : WebAction.py
@desc       : 项目：hmpt 模块：web 接口方法封装
"""

from hmpt.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('web_apiURL', 'hmpt')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_web_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_platform_cm_base_viewChannel(uid):
    """
    查询渠道
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2912')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannel"
    LOGGER.info("查询渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_saveChannel(city, name, parentchanneluuid, province, region, shortname):
    """
    添加渠道
    :param city: 渠道所属城市 (Y),number
    :param province: 渠道所属省份(Y),number
    :param shortname: 渠道简称(Y),string
    :param name: 渠道名称(Y),string
    :param region: 所属大区(Y),number
    :param parentchanneluuid: 父级uuid(N)不填则该渠道为根渠道,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2913')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/saveChannel"
    LOGGER.info("添加渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["name"] = name
    params["parentChannelUuid"] = parentchanneluuid
    params["province"] = province
    params["region"] = region
    params["shortName"] = shortname
    LOGGER.info("添加渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_updateChannel(channeluuid, city, name, note, operatoruuid, province, region, shortname):
    """
    编辑渠道
    :param shortname: 渠道简称 (Y),string
    :param note: 备注 (N),string
    :param city: 渠道所属城市(Y),number
    :param name: 渠道名称(Y),string
    :param region: 所属大区(Y),number
    :param operatoruuid: 操作员(N),string
    :param channeluuid: 渠道 uuid(Y),string
    :param province: 渠道所属省份 (Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2914')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/updateChannel"
    LOGGER.info("编辑渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["city"] = city
    params["name"] = name
    params["note"] = note
    params["operatorUuid"] = operatoruuid
    params["province"] = province
    params["region"] = region
    params["shortName"] = shortname
    LOGGER.info("编辑渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_examine_examine(isadopt, message, uid):
    """
    渠道审核
    :param uid: 审核的渠道id(Y),string
    :param message: 审核人填写信息(N),string
    :param isadopt: 是否通过(Y),boolean
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2915')
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/examine"
    LOGGER.info("渠道审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["isAdopt"] = isadopt
    params["message"] = message
    params["uid"] = uid
    LOGGER.info("渠道审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_viewChannels(name, pagecurrent, pagesize):
    """
    渠道列表
    :param pagesize: 每页大小(Y),string
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2916')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannels"
    LOGGER.info("渠道列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("渠道列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_state_updateFreezeState(uid, updatestate):
    """
    冻结渠道
    :param uid: 渠道id,string
    :param updatestate: 冻结状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2917')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateFreezeState"
    LOGGER.info("冻结渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["updateState"] = updatestate
    LOGGER.info("冻结渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("冻结渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_state_updateOpenCloseState(uid, updatestate):
    """
    渠道开关
    :param updatestate: 开关状态,string
    :param uid: 渠道uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2918')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateOpenCloseState"
    LOGGER.info("渠道开关请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["updateState"] = updatestate
    LOGGER.info("渠道开关请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道开关请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_examine_viewExamineChannels(name, pagecurrent, pagesize):
    """
    渠道审核列表
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2919')
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/viewExamineChannels"
    LOGGER.info("渠道审核列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("渠道审核列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道审核列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_state_viewStateChannels(auditstate, freezestate, name, openclosestate, pagecurrent, pagesize):
    """
    渠道状态列表
    :param pagesize: 每页大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param openclosestate: 冻结状态,string
    :param auditstate: 审核状态,string
    :param freezestate: 冻结状态,string
    :param name: 渠道名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2920')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/viewStateChannels"
    LOGGER.info("渠道状态列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["freezeState"] = freezestate
    params["name"] = name
    params["openCloseState"] = openclosestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("渠道状态列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道状态列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_business_deleteBusinessInfor(uid):
    """
    删除机构
    :param uid: 删除机构的uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2921')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_business_viewBusinessInforByChannel(uid):
    """
    根据渠道Uid查询机构
    :param uid: 渠道uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2922')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/viewBusinessInforByChannel"
    LOGGER.info("根据渠道Uid查询机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据渠道Uid查询机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    添加机构
    :param documentregionname: 证件区名称,string
    :param documentprovince: 证件省id,number
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param documentcity: 证件市id,number
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businessprovince: 实际经营省id,number
    :param documentprovincename: 证件省名称,string
    :param documentcityname: 证件市名称,string
    :param businesscityname: 实际经营市名称,string
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param businessinformationuuid: 业务信息 uuid(N),string
    :param businessregionname: 实际经营区名称,string
    :param documentaddress: 证件地址(Y),string
    :param businessprovincename: 实际经营省名称,string
    :param businesscity: 实际经营市id,number
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessaddress: 实际经营地址(Y),string
    :param documentregion: 证件区id,number
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessregion: 实际经营区id,number
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2923')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/saveBusinessInfor"
    LOGGER.info("添加机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["businessAddressZipCode"] = businessaddresszipcode
    params["businessCity"] = businesscity
    params["businessCityName"] = businesscityname
    params["businessHoursEndTime"] = businesshoursendtime
    params["businessHoursStartTime"] = businesshoursstarttime
    params["businessInformationUuid"] = businessinformationuuid
    params["businessProvince"] = businessprovince
    params["businessProvinceName"] = businessprovincename
    params["businessRegion"] = businessregion
    params["businessRegionName"] = businessregionname
    params["businessRegistrationNumber"] = businessregistrationnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["documentAddress"] = documentaddress
    params["documentCity"] = documentcity
    params["documentCityName"] = documentcityname
    params["documentProvince"] = documentprovince
    params["documentProvinceName"] = documentprovincename
    params["documentRegion"] = documentregion
    params["documentRegionName"] = documentregionname
    params["email"] = email
    params["organizationCode"] = organizationcode
    params["socialUnifiedCreditCode"] = socialunifiedcreditcode
    params["storeRentalEndTime"] = storerentalendtime
    params["storeRentalStartTime"] = storerentalstarttime
    params["taxRegistrationNumber"] = taxregistrationnumber
    LOGGER.info("添加机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    编辑机构
    :param documentcity: 证件市id,number
    :param businessprovincename: 实际经营省名称,string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businessinformationuuid: 业务信息 uuid(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessregion: 实际经营区id,number
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param documentregion: 证件区id,number
    :param documentprovincename: 证件省名称,string
    :param businessregionname: 实际经营区名称,string
    :param businesscityname: 实际经营市名称,string
    :param documentcityname: 证件市名称,string
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param documentprovince: 证件省id,number
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businessprovince: 实际经营省id,number
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param businesscity: 实际经营市id,number
    :param documentaddress: 证件地址(Y),string
    :param documentregionname: 证件区名称,string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2924')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/updateBusinessInfor"
    LOGGER.info("编辑机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["businessAddressZipCode"] = businessaddresszipcode
    params["businessCity"] = businesscity
    params["businessCityName"] = businesscityname
    params["businessHoursEndTime"] = businesshoursendtime
    params["businessHoursStartTime"] = businesshoursstarttime
    params["businessInformationUuid"] = businessinformationuuid
    params["businessProvince"] = businessprovince
    params["businessProvinceName"] = businessprovincename
    params["businessRegion"] = businessregion
    params["businessRegionName"] = businessregionname
    params["businessRegistrationNumber"] = businessregistrationnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["documentAddress"] = documentaddress
    params["documentCity"] = documentcity
    params["documentCityName"] = documentcityname
    params["documentProvince"] = documentprovince
    params["documentProvinceName"] = documentprovincename
    params["documentRegion"] = documentregion
    params["documentRegionName"] = documentregionname
    params["email"] = email
    params["organizationCode"] = organizationcode
    params["socialUnifiedCreditCode"] = socialunifiedcreditcode
    params["storeRentalEndTime"] = storerentalendtime
    params["storeRentalStartTime"] = storerentalstarttime
    params["taxRegistrationNumber"] = taxregistrationnumber
    LOGGER.info("编辑机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_operator_deleteOperator(uid):
    """
    删除操作员
    :param uid: 渠道操作员uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2925')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/deleteOperator"
    LOGGER.info("删除操作员请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_operator_viewOperator(uid):
    """
    查询操作员
    :param uid: 渠道操作员uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2926')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/viewOperator"
    LOGGER.info("查询操作员请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_operator_saveOperator(channelormerchantuuid, mail, mobile, name, password, salt, title):
    """
    添加操作员
    :param password: 密码(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid（Y）,string
    :param title: 职务(Y),string
    :param mail: 邮箱(Y),string
    :param name: 姓名(Y),string
    :param salt: 盐(Y),string
    :param mobile: 手机(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2927')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/saveOperator"
    LOGGER.info("添加操作员请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["mail"] = mail
    params["mobile"] = mobile
    params["name"] = name
    params["password"] = password
    params["salt"] = salt
    params["title"] = title
    LOGGER.info("添加操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_operator_updateOperator(channelormerchantuuid, mail, mobile, name, operatoruuid, password, salt, title):
    """
    编辑操作员
    :param mail: 邮箱(Y),string
    :param password: 密码(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param name: 姓名(Y),string
    :param mobile: 手机(Y),string
    :param salt: 盐(N),string
    :param title: 职务(Y),string
    :param operatoruuid: 操作员uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2928')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/updateOperator"
    LOGGER.info("编辑操作员请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["mail"] = mail
    params["mobile"] = mobile
    params["name"] = name
    params["operatorUuid"] = operatoruuid
    params["password"] = password
    params["salt"] = salt
    params["title"] = title
    LOGGER.info("编辑操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_clear_deleteClearingAccount(uid):
    """
    删除渠道结算账户信息
    :param uid: 渠道法人代表uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2929')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/deleteClearingAccount"
    LOGGER.info("删除渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(uid):
    """
    根据渠道Uid查询渠道结算
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2930')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/viewClearingAccountByChannel"
    LOGGER.info("根据渠道Uid查询渠道结算请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据渠道Uid查询渠道结算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询渠道结算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_clear_saveClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    """
    添加渠道结算账户信息
    :param linenumber: 联行行号(Y),string
    :param phone: 电话号码(Y),string
    :param accountnumber: 结算账号(Y),string
    :param province: 开户行地址-省(Y),number
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param city: 开户行地址-市(Y),number
    :param branchname: 支行名称(Y),string
    :param accountname: 账户名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param accounttype: 账户类型(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param region: 开户行地址-区(Y),number
    :param channelormerchantuuid: 渠道或者商户(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2931')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/saveClearingAccount"
    LOGGER.info("添加渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountName"] = accountname
    params["accountNumber"] = accountnumber
    params["accountOpeningBank"] = accountopeningbank
    params["accountType"] = accounttype
    params["branchName"] = branchname
    params["chamberlainIdCard"] = chamberlainidcard
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["clearingAccountUuid"] = clearingaccountuuid
    params["lineNumber"] = linenumber
    params["phone"] = phone
    params["province"] = province
    params["region"] = region
    LOGGER.info("添加渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_clear_updateClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    """
    编辑渠道结算账户信息
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param region: 开户行地址-区(Y),number
    :param phone: 电话号码(Y),string
    :param branchname: 支行名称(Y),string
    :param province: 开户行地址-省(Y),number
    :param accounttype: 账户类型(Y),string
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param accountname: 账户名称(Y),string
    :param linenumber: 联行行号(Y),string
    :param city: 开户行地址-市(Y),number
    :param accountnumber: 结算账号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2932')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/updateClearingAccount"
    LOGGER.info("编辑渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountName"] = accountname
    params["accountNumber"] = accountnumber
    params["accountOpeningBank"] = accountopeningbank
    params["accountType"] = accounttype
    params["branchName"] = branchname
    params["chamberlainIdCard"] = chamberlainidcard
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["clearingAccountUuid"] = clearingaccountuuid
    params["lineNumber"] = linenumber
    params["phone"] = phone
    params["province"] = province
    params["region"] = region
    LOGGER.info("编辑渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_deleteLegalPerson(uid):
    """
    删除渠道法人代表
    :param uid: 结算信息id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2933')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/deleteLegalPerson"
    LOGGER.info("删除渠道法人代表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(uid):
    """
    根据渠道Uid查询渠道法人代表
    :param uid: 渠道UUid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2934')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/viewLegalPersonByChannel"
    LOGGER.info("根据渠道Uid查询渠道法人代表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据渠道Uid查询渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, city, legalpersonuuid, mobile, name, province, region):
    """
    添加渠道法人代表-v1.4.0、v1.0.6
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param province: 渠道所属省份编号,number
    :param name: 法人代表姓名(Y),string
    :param mobile: 手机号码(Y),string
    :param legalpersonuuid: 法人代表uuid(N),string
    :param cardnumber: 证件号码(Y),string
    :param region: 所属大区编号 ,,number
    :param city: 渠道所属城市编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2935')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
    LOGGER.info("添加渠道法人代表-v1.4.0、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    params["province"] = province
    params["region"] = region
    LOGGER.info("添加渠道法人代表-v1.4.0、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道法人代表-v1.4.0、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, city, legalpersonuuid, mobile, name, province, region):
    """
    编辑渠道法人代表-v1.4.0
    :param cardnumber: 证件号码(Y),string
    :param region: 所属大区编号,number
    :param name: 法人代表姓名(Y),string
    :param mobile: 手机号码(Y),string
    :param city: 渠道所属城市编号,number
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param legalpersonuuid: 法人代表uuid(Y),string
    :param province: 渠道所属省份编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2936')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/updateLegalPerson"
    LOGGER.info("编辑渠道法人代表-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    params["province"] = province
    params["region"] = region
    LOGGER.info("编辑渠道法人代表-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道法人代表-v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_viewProvinceLists(paramsingle):
    """
    省级下拉
    :param paramsingle: 查询条件(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2937')
    requesturl = baseUrl + "/api/78dk/platform/common/viewProvinceLists"
    LOGGER.info("省级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("省级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("省级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_viewRegionLists(paramsingle):
    """
    区/县级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2938')
    requesturl = baseUrl + "/api/78dk/platform/common/viewRegionLists"
    LOGGER.info("区/县级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("区/县级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("区/县级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_viewCityLists(paramsingle):
    """
    市级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2939')
    requesturl = baseUrl + "/api/78dk/platform/common/viewCityLists"
    LOGGER.info("市级下拉请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("市级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("市级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundSide_deleteFundSide(uid):
    """
    删除资方
    :param uid: 资方uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2940')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/deleteFundSide"
    LOGGER.info("删除资方请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundSide_viewFundSide(uid):
    """
    查询资方
    :param uid: 资方id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2941')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSide"
    LOGGER.info("查询资方请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundSide_saveFundSide(name, state):
    """
    添加资方
    :param state: 资方状态(Y),string
    :param name: 资方名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2942')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/saveFundSide"
    LOGGER.info("添加资方请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["state"] = state
    LOGGER.info("添加资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundSide_updateFundSide(fundsideuuid, name, state):
    """
    编辑资方
    :param name: 资方名称(Y),string
    :param fundsideuuid: 资方uuid(Y),string
    :param state: 资方状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2943')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/updateFundSide"
    LOGGER.info("编辑资方请求地址:【{}】".format(requesturl))
    params = dict()
    params["fundSideUuid"] = fundsideuuid
    params["name"] = name
    params["state"] = state
    LOGGER.info("编辑资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundSide_viewFundSides(name, pagecurrent, pagesize, state):
    """
    资方列表
    :param pagecurrent: 当前页码(Y),number
    :param state: 资方状态,string
    :param name: 资方名称,string
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2944')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSides"
    LOGGER.info("资方列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["state"] = state
    LOGGER.info("资方列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资方列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundPackage_deleteFundPackage(uid):
    """
    删除资金包
    :param uid: 资金包uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2945')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/deleteFundPackage"
    LOGGER.info("删除资金包请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackage(uid):
    """
    查询资金包
    :param uid: 资金包uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2946')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackage"
    LOGGER.info("查询资金包请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundPackage_saveFundPackage(amount, fundsideuuid, name, state):
    """
    添加资金包
    :param amount: 总额度(Y),number
    :param state: 数据状态(Y),string
    :param fundsideuuid: 资方uuid(Y),number
    :param name: 资金包名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2947')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/saveFundPackage"
    LOGGER.info("添加资金包请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["fundSideUuid"] = fundsideuuid
    params["name"] = name
    params["state"] = state
    LOGGER.info("添加资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundPackage_updateFundPackage(amount, fundpackageuuid, fundsideuuid, name, state):
    """
    编辑资金包
    :param state: 数据状态(Y),string
    :param name: 资金包名称(Y),string
    :param fundpackageuuid: 资金包uuid(Y),string
    :param fundsideuuid: 资方uuid,
    :param amount: 总额度(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2948')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/updateFundPackage"
    LOGGER.info("编辑资金包请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["fundPackageUuid"] = fundpackageuuid
    params["fundSideUuid"] = fundsideuuid
    params["name"] = name
    params["state"] = state
    LOGGER.info("编辑资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackages(name, pagecurrent, pagesize):
    """
    资金包列表查询
    :param pagesize: 页面大小(Y),number
    :param name: 资金包名称(N),string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2949')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("资金包列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_deleteProduct(uid):
    """
    删除产品模版
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2950')
    requesturl = baseUrl + "/api/78dk/platform/product/base/deleteProduct"
    LOGGER.info("删除产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_viewProductDetail(uid):
    """
    查询产品模版--美佳v1.0.6
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2951')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetail"
    LOGGER.info("查询产品模版--美佳v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询产品模版--美佳v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品模版--美佳v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_saveProduct(delayrepaydate, discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, issupportdelayrepay, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    添加产品模版--美佳v1.0.6
    :param productstate: 产品状态（Y）,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param loanmode: 放款方式,string
    :param delayrepaydate: 支持的延期还款天数---美佳v1.0.6，number,number
    :param remark: 产品备注,string
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param issupportdelayrepay: 是否支持延期还款---美佳v1.0.6,true为支持,boolean
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param name: 产品名称（Y）,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :param repaymentmethod: 还款方式（Y）,string
    :param discountrate: 商户最大贴息费率（Y）,string
    :param repaymentdatetype: 还款日类型（Y）,string
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param fundpackageuuid: 资金包uuid,string
    :param maxquota: 单笔额度上限（Y）,string
    :param minquota: 单笔额度下限（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2952')
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
    LOGGER.info("添加产品模版--美佳v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["delayRepayDate"] = delayrepaydate
    params["discountRate"] = discountrate
    params["earlyRepaymentFreeCycle"] = earlyrepaymentfreecycle
    params["earlyRepaymentHandlingFee"] = earlyrepaymenthandlingfee
    params["earlyRepaymentSupport"] = earlyrepaymentsupport
    params["electronicContractTemplateUuid"] = electroniccontracttemplateuuid
    params["firstHalfOfTheMonth"] = firsthalfofthemonth
    params["fundPackageUuid"] = fundpackageuuid
    params["incomingPartsTemplateUuid"] = incomingpartstemplateuuid
    params["isSupportDelayRepay"] = issupportdelayrepay
    params["loanMode"] = loanmode
    params["machineAuditTemplateUuid"] = machineaudittemplateuuid
    params["maxQuota"] = maxquota
    params["minQuota"] = minquota
    params["name"] = name
    params["overdueGracePeriod"] = overduegraceperiod
    params["overdueHandlingFeeRate"] = overduehandlingfeerate
    params["overduePrincipalRate"] = overdueprincipalrate
    params["productConfigs"] = productconfigs
    params["productState"] = productstate
    params["remark"] = remark
    params["repaymentDateType"] = repaymentdatetype
    params["repaymentMethod"] = repaymentmethod
    params["secondHalfOfTheMonth"] = secondhalfofthemonth
    params["state"] = state
    LOGGER.info("添加产品模版--美佳v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加产品模版--美佳v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_updateProduct(delayrepaydate, discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, issupportdelayrepay, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productdetailuuid, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    编辑产品模版美佳v1.0.6
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param productdetailuuid: 产品UUID,string
    :param minquota: 单笔额度下限（Y）,string
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param name: 产品名称（Y）,string
    :param loanmode: 放款方式,string
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param issupportdelayrepay: 是否支持延期还款---美佳v1.0.6,true为支持,boolean
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param maxquota: 单笔额度上限（Y）,string
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param remark: 产品备注,string
    :param productstate: 产品状态（Y）,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param fundpackageuuid: 资金包uuid,string
    :param discountrate: 商户最大贴息费率（Y）,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param repaymentdatetype: 还款日类型（Y）,string
    :param repaymentmethod: 还款方式（Y）,string
    :param delayrepaydate: 支持的延期还款天数---美佳v1.0.6，number,number
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2953')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
    LOGGER.info("编辑产品模版美佳v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["delayRepayDate"] = delayrepaydate
    params["discountRate"] = discountrate
    params["earlyRepaymentFreeCycle"] = earlyrepaymentfreecycle
    params["earlyRepaymentHandlingFee"] = earlyrepaymenthandlingfee
    params["earlyRepaymentSupport"] = earlyrepaymentsupport
    params["electronicContractTemplateUuid"] = electroniccontracttemplateuuid
    params["firstHalfOfTheMonth"] = firsthalfofthemonth
    params["fundPackageUuid"] = fundpackageuuid
    params["incomingPartsTemplateUuid"] = incomingpartstemplateuuid
    params["isSupportDelayRepay"] = issupportdelayrepay
    params["loanMode"] = loanmode
    params["machineAuditTemplateUuid"] = machineaudittemplateuuid
    params["maxQuota"] = maxquota
    params["minQuota"] = minquota
    params["name"] = name
    params["overdueGracePeriod"] = overduegraceperiod
    params["overdueHandlingFeeRate"] = overduehandlingfeerate
    params["overduePrincipalRate"] = overdueprincipalrate
    params["productConfigs"] = productconfigs
    params["productDetailUuid"] = productdetailuuid
    params["productState"] = productstate
    params["remark"] = remark
    params["repaymentDateType"] = repaymentdatetype
    params["repaymentMethod"] = repaymentmethod
    params["secondHalfOfTheMonth"] = secondhalfofthemonth
    params["state"] = state
    LOGGER.info("编辑产品模版美佳v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑产品模版美佳v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_viewProductDetails(name, pagecurrent, pagesize):
    """
    产品列表
    :param name: 名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2954')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetails"
    LOGGER.info("产品列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("产品列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_updateProductState(productstate, uuid):
    """
    修改产品状态
    :param uuid: 产品uuid,string
    :param productstate: 产品状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2955')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProductState"
    LOGGER.info("修改产品状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["productState"] = productstate
    params["uuid"] = uuid
    LOGGER.info("修改产品状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改产品状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_viewFundPackages(name, pagecurrent, pagesize, state):
    """
    资金包列表查询
    :param state: 资金包状态,string
    :param pagesize: 每页显示条数,number
    :param name: 资金包名称,string
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2956')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["state"] = state
    LOGGER.info("资金包列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_viewProductTemplateList(paramsingle):
    """
    根据模板类型获取具体模板信息
    :param paramsingle: 模板细分类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2957')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductTemplateList"
    LOGGER.info("根据模板类型获取具体模板信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("根据模板类型获取具体模板信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据模板类型获取具体模板信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_saveProductEarlySettle(earlysettledays, earlysettlefredays, earlysettlefrerate, earlysettleinterest, earlysettlesupport, earlysettlevoidmode, productdetailuuid, productearlysettleuuid):
    """
    产品提前结清信息保存（新增、修改）-v1.5.0
    :param earlysettlevoidmode: 提前结清免收手续费方式,string
    :param productearlysettleuuid: 产品提前结清uuid,string
    :param earlysettlesupport: 是否支持提前结清,string
    :param earlysettlefredays: 免收周期（天）,number
    :param productdetailuuid: 产品uuid,string
    :param earlysettledays: 放款多少天后可提前结清,number
    :param earlysettlefrerate: 超出后手续费率,number
    :param earlysettleinterest: 提前结清利息收取方式,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2958')
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProductEarlySettle"
    LOGGER.info("产品提前结清信息保存（新增、修改）-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["earlySettleDays"] = earlysettledays
    params["earlySettleFreDays"] = earlysettlefredays
    params["earlySettleFreRate"] = earlysettlefrerate
    params["earlySettleInterest"] = earlysettleinterest
    params["earlySettleSupport"] = earlysettlesupport
    params["earlySettleVoidMode"] = earlysettlevoidmode
    params["productDetailUuid"] = productdetailuuid
    params["productEarlySettleUuid"] = productearlysettleuuid
    LOGGER.info("产品提前结清信息保存（新增、修改）-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品提前结清信息保存（新增、修改）-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_queryProductEarlySettleByProductDetailUuid(productdetailuuid):
    """
    查询产品提前结清模块信息-v1.5.0
    :param productdetailuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2959')
    requesturl = baseUrl + "/api/78dk/platform/product/base/queryProductEarlySettleByProductDetailUuid"
    LOGGER.info("查询产品提前结清模块信息-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("查询产品提前结清模块信息-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品提前结清模块信息-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_bindProductMerchant(merchantuuids, productuuid):
    """
    绑定产品和商户关系
    :param productuuid: 商户uuid(Y),string
    :param merchantuuids: 商户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2960')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/bindProductMerchant"
    LOGGER.info("绑定产品和商户关系请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuids"] = merchantuuids
    params["productUuid"] = productuuid
    LOGGER.info("绑定产品和商户关系请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定产品和商户关系请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_saveMerchantTX(discountrate, merchantuuid, period, productdetailconfiguuid, rate):
    """
    保存商户贴息
    :param productdetailconfiguuid: 产品分期uuid,string
    :param period: 分期数,string
    :param merchantuuid: 商户uuid,string
    :param discountrate: 商户贴息率,string
    :param rate: 月利率,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2961')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountRate"] = discountrate
    params["merchantUuid"] = merchantuuid
    params["period"] = period
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["rate"] = rate
    LOGGER.info("保存商户贴息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存商户贴息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_findMerchantTX(merchantuuid, productuuid):
    """
    查询商户贴息
    :param productuuid: 产品uuid,string
    :param merchantuuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2962')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/findMerchantTX"
    LOGGER.info("查询商户贴息请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    params["productUuid"] = productuuid
    LOGGER.info("查询商户贴息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户贴息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(name, pagecurrent, pagesize, uuid):
    """
    根据产品id查询不相关的商户列表
    :param name: 名称,string
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param uuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2963')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewNotInMerchantsByPuid"
    LOGGER.info("根据产品id查询不相关的商户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["uuid"] = uuid
    LOGGER.info("根据产品id查询不相关的商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品id查询不相关的商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(name, pagecurrent, pagesize, uuid):
    """
    根据产品id查询相关的商户列表
    :param uuid: 产品uuid(Y),string
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param name: 名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2964')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewInMerchantsByPuid"
    LOGGER.info("根据产品id查询相关的商户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["uuid"] = uuid
    LOGGER.info("根据产品id查询相关的商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品id查询相关的商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_unBindProductMerchant(merchantuuids, productuuid):
    """
    解绑产品和商户关系
    :param productuuid: 产品uuid,string
    :param merchantuuids: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2965')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/unBindProductMerchant"
    LOGGER.info("解绑产品和商户关系请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuids"] = merchantuuids
    params["productUuid"] = productuuid
    LOGGER.info("解绑产品和商户关系请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("解绑产品和商户关系请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_viewProductDetails(name, pagecurrent, pagesize):
    """
    查看产品信息列表
    :param name: ,string
    :param pagesize: ,number
    :param pagecurrent: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2966')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductDetails"
    LOGGER.info("查看产品信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查看产品信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看产品信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_updateMerchant(channeluuid, city, industryfirst, industrysecond, merchantuuid, name, note, parentmerchantuuid, province, repaymentmax, repaymentproportion, shortname):
    """
    基本信息-修改-hm-1.0.0
    :param shortname: 商户简称(Y),string
    :param province: 省id,number
    :param name: 商户名称(Y),string
    :param merchantuuid: 商户Uuid(Y),string
    :param industryfirst: 一级分类id,number
    :param city: 市id,number
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param note: 商户描述/备注(N),string
    :param industrysecond: 二级分类id,number
    :param channeluuid: 渠道Uuid,string
    :param repaymentproportion: 打款比例,
    :param repaymentmax: 打款上限,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2967')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
    LOGGER.info("基本信息-修改-hm-1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["city"] = city
    params["industryFirst"] = industryfirst
    params["industrySecond"] = industrysecond
    params["merchantUuid"] = merchantuuid
    params["name"] = name
    params["note"] = note
    params["parentMerchantUuid"] = parentmerchantuuid
    params["province"] = province
    params["repaymentMax"] = repaymentmax
    params["repaymentProportion"] = repaymentproportion
    params["shortName"] = shortname
    LOGGER.info("基本信息-修改-hm-1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-修改-hm-1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_deleteMerchant(uid):
    """
    基本信息-删除-v1.4
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2968')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/deleteMerchant"
    LOGGER.info("基本信息-删除-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("基本信息-删除-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-删除-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_saveMerchant(channeluuid, city, industryfirst, industrysecond, name, note, parentmerchantuuid, province, repaymentmax, repaymentproportion, shortname):
    """
    基本信息-新增-hm-1.0.0
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param city: 市id(Y),number
    :param name: 商户名称(Y),string
    :param industryfirst: 一级分类id(Y),number
    :param shortname: 商户简称(Y),string
    :param industrysecond: 二级分类id,number
    :param note: 商户描述/备注(N),string
    :param province: 省id(Y),number
    :param channeluuid: 渠道Uuid,string
    :param repaymentmax: 打款上限,
    :param repaymentproportion: 打款比例,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2969')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
    LOGGER.info("基本信息-新增-hm-1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["city"] = city
    params["industryFirst"] = industryfirst
    params["industrySecond"] = industrysecond
    params["name"] = name
    params["note"] = note
    params["parentMerchantUuid"] = parentmerchantuuid
    params["province"] = province
    params["repaymentMax"] = repaymentmax
    params["repaymentProportion"] = repaymentproportion
    params["shortName"] = shortname
    LOGGER.info("基本信息-新增-hm-1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-新增-hm-1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewMerchant(uid):
    """
    基本信息-查询hm-1.0.0
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2970')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
    LOGGER.info("基本信息-查询hm-1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("基本信息-查询hm-1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-查询hm-1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewMerchantList(auditstate, freezestate, name, openclosestate, pagecurrent, pagesize):
    """
    查询商户列表-v1.5.2v1.4.0、v1.0.6
    :param auditstate: 审核状态,string
    :param openclosestate: 开关状态,string
    :param pagesize: 分页大小(Y),number
    :param name: 商户简称(N),string
    :param freezestate: 使用状态,string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2971')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
    LOGGER.info("查询商户列表-v1.5.2v1.4.0、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["freezeState"] = freezestate
    params["name"] = name
    params["openCloseState"] = openclosestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询商户列表-v1.5.2v1.4.0、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户列表-v1.5.2v1.4.0、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_state_updateFreezeState(uid, updatestate):
    """
    下架状态
    :param updatestate: 修改状态(Y),string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2972')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateFreezeState"
    LOGGER.info("下架状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["updateState"] = updatestate
    LOGGER.info("下架状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下架状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_state_updateOpenCloseState(uid, updatestate):
    """
    商户归档
    :param uid: 商户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2973')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateOpenCloseState"
    LOGGER.info("商户归档请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["updateState"] = updatestate
    LOGGER.info("商户归档请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户归档请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_examine_viewExamineMerchantList(name, pagecurrent, pagesize):
    """
    查询商户审核列表
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :param name: 商户名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2974')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/viewExamineMerchantList"
    LOGGER.info("查询商户审核列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询商户审核列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户审核列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_state_viewStateMerchantList(name, pagecurrent, pagesize):
    """
    查询商户状态列表
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :param name: 商户名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2975')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/viewStateMerchantList"
    LOGGER.info("查询商户状态列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询商户状态列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户状态列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_saveContractImages(images):
    """
    影像资料保存-v1.5.1
    :param images: 图片数组,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2976')
    requesturl = baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存-v1.5.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["images"] = images
    LOGGER.info("影像资料保存-v1.5.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料保存-v1.5.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_viewImageRoleList(subdivisiontype, uid):
    """
    影像资料查询-v1.4
    :param uid: 商户Uuid(Y),string
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2977')
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageRoleList"
    LOGGER.info("影像资料查询-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["subdivisionType"] = subdivisiontype
    params["uid"] = uid
    LOGGER.info("影像资料查询-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料查询-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_bd_findBDMerchant(uid):
    """
    查询商户BD信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2978')
    requesturl = baseUrl + "/api/78dk/platform/mm/bd/findBDMerchant"
    LOGGER.info("查询商户BD信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询商户BD信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户BD信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_findOptLog(uid):
    """
    查询操作记录
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2979')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/findOptLog"
    LOGGER.info("查询操作记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询操作记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询操作记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid, merchantuuid, name, remark):
    """
    新增商户BD信息
    :param remark: BD备注,string
    :param bdinfouuid: BD UUID,string
    :param name: BD姓名,string
    :param merchantuuid: 商户UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2980')
    requesturl = baseUrl + "/api/78dk/platform/mm/bd/saveBDMerchant"
    LOGGER.info("新增商户BD信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdInfoUuid"] = bdinfouuid
    params["merchantUuid"] = merchantuuid
    params["name"] = name
    params["remark"] = remark
    LOGGER.info("新增商户BD信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增商户BD信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid, merchantuuid, name, remark):
    """
    修改商户BD信息
    :param merchantuuid: 商户UUID,string
    :param name: BD姓名,string
    :param bdinfouuid: BD UUID,string
    :param remark: BD备注,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2981')
    requesturl = baseUrl + "/api/78dk/platform/mm/bd/updateBDMerchant"
    LOGGER.info("修改商户BD信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdInfoUuid"] = bdinfouuid
    params["merchantUuid"] = merchantuuid
    params["name"] = name
    params["remark"] = remark
    LOGGER.info("修改商户BD信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改商户BD信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_unbind_wechart(list, uid):
    """
    微信解绑-v1.4
    :param uid: 商户Uuid,string
    :param list: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2982')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/unbind/wechart"
    LOGGER.info("微信解绑-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["list"] = list
    params["uid"] = uid
    LOGGER.info("微信解绑-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("微信解绑-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewWeChart(uid):
    """
    微信查看-v1.4
    :param uid: 商户Uuid(Y),
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2983')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewWeChart"
    LOGGER.info("微信查看-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("微信查看-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("微信查看-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewIndustryCategory():
    """
    行业分类查询-v1.4
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2984')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewIndustryCategory"
    LOGGER.info("行业分类查询-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("行业分类查询-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("行业分类查询-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_bd_listDbLogs(uid):
    """
    查询商户业BD操作日志-v1.4
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2985')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/bd/listDbLogs"
    LOGGER.info("查询商户业BD操作日志-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询商户业BD操作日志-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户业BD操作日志-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_examine_createTemporaryCode(uid):
    """
    生成临时编码-v1.4
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2986')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/createTemporaryCode"
    LOGGER.info("生成临时编码-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("生成临时编码-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("生成临时编码-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_saveImagesAndChange(images):
    """
    商户图片资料保存-1.5.2
    :param images: 图片集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2987')
    requesturl = baseUrl + "/api/78dk/platform/mm/saveImagesAndChange"
    LOGGER.info("商户图片资料保存-1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["images"] = images
    LOGGER.info("商户图片资料保存-1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户图片资料保存-1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_viewImageByMerchantUuid(uid):
    """
    查询商户图片-v1.5.2
    :param uid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2988')
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageByMerchantUuid"
    LOGGER.info("查询商户图片-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询商户图片-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户图片-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, contracttimebegin, contracttimeend, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, installmentcooperationorgs, merge, organizationcode, socialunifiedcreditcode, specialindustrylicenseorname, specialindustrytimebegin, specialindustrytimeend, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    修改机构信息-v1.4
    :param documentprovince: 证件省id,number
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param businessprovincename: 实际经营省名称,string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param contracttimebegin: 合同开始时间,string
    :param businesscityname: 实际经营市名称,string
    :param specialindustrytimeend: 特殊行业许可证有效期结束时间,string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param contracttimeend: 合同结束时间,string
    :param installmentcooperationorgs: 现有分期合作机构,array<object>
    :param businessinformationuuid: 业务信息 UUID(Y),string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param businessregionname: 实际经营区名称,string
    :param businesscity: 实际经营市id,number
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param socialunifiedcreditcode: 社会统一征信代码-三证合一后(Y),string
    :param businessprovince: 实际经营省id,number
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param documentaddress: 证件地址(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param businessaddress: 实际经营地址(Y),string
    :param documentcityname: 证件市名称,string
    :param documentregion: 证件区id,number
    :param documentprovincename: 证件省名称,string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param specialindustrytimebegin: 特殊行业许可证有效期开始时间,string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param documentcity: 证件市id,number
    :param merge: 是否三证合一,string
    :param specialindustrylicenseorname: 特殊行业许可证或证明名称：,string
    :param documentregionname: 证件区名称,string
    :param businessregion: 实际经营区id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2989')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/updateBusinessInfor"
    LOGGER.info("修改机构信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["businessAddressZipCode"] = businessaddresszipcode
    params["businessCity"] = businesscity
    params["businessCityName"] = businesscityname
    params["businessHoursEndTime"] = businesshoursendtime
    params["businessHoursStartTime"] = businesshoursstarttime
    params["businessInformationUuid"] = businessinformationuuid
    params["businessProvince"] = businessprovince
    params["businessProvinceName"] = businessprovincename
    params["businessRegion"] = businessregion
    params["businessRegionName"] = businessregionname
    params["businessRegistrationNumber"] = businessregistrationnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["contractTimeBegin"] = contracttimebegin
    params["contractTimeEnd"] = contracttimeend
    params["documentAddress"] = documentaddress
    params["documentCity"] = documentcity
    params["documentCityName"] = documentcityname
    params["documentProvince"] = documentprovince
    params["documentProvinceName"] = documentprovincename
    params["documentRegion"] = documentregion
    params["documentRegionName"] = documentregionname
    params["email"] = email
    params["installmentCooperationOrgs"] = installmentcooperationorgs
    params["merge"] = merge
    params["organizationCode"] = organizationcode
    params["socialUnifiedCreditCode"] = socialunifiedcreditcode
    params["specialIndustryLicenseOrName"] = specialindustrylicenseorname
    params["specialIndustryTimeBegin"] = specialindustrytimebegin
    params["specialIndustryTimeEnd"] = specialindustrytimeend
    params["storeRentalEndTime"] = storerentalendtime
    params["storeRentalStartTime"] = storerentalstarttime
    params["taxRegistrationNumber"] = taxregistrationnumber
    LOGGER.info("修改机构信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改机构信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_deleteBusinessInfor(uid):
    """
    删除机构信息
    :param uid: 商户机构Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2990')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_saveBusinessInfor(channelormerchantuuid, contracttimebegin, contracttimeend, installmentcooperationorgs, merge, organizationcode, socialunifiedcreditcode, specialindustrylicenseorname, specialindustrytimebegin, specialindustrytimeend, taxregistrationnumber):
    """
    新增机构信息-v1.4
    :param taxregistrationnumber: 税务登记号,string
    :param installmentcooperationorgs: 现有分期合作机构,array<object>
    :param specialindustrylicenseorname: 特殊行业许可证或者名称,string
    :param socialunifiedcreditcode: 社会统一征信代码,string
    :param organizationcode: 组织结构代码-,string
    :param specialindustrytimeend: 特殊行业许可证有效期结束时间,string
    :param merge: 是否三证合一,string
    :param specialindustrytimebegin: 特殊行业许可证有效期开始时间,number
    :param contracttimeend: 合同结束时间,number
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param contracttimebegin: 合同开始时间,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2991')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/saveBusinessInfor"
    LOGGER.info("新增机构信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["contractTimeBegin"] = contracttimebegin
    params["contractTimeEnd"] = contracttimeend
    params["installmentCooperationOrgs"] = installmentcooperationorgs
    params["merge"] = merge
    params["organizationCode"] = organizationcode
    params["socialUnifiedCreditCode"] = socialunifiedcreditcode
    params["specialIndustryLicenseOrName"] = specialindustrylicenseorname
    params["specialIndustryTimeBegin"] = specialindustrytimebegin
    params["specialIndustryTimeEnd"] = specialindustrytimeend
    params["taxRegistrationNumber"] = taxregistrationnumber
    LOGGER.info("新增机构信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增机构信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(uid):
    """
    根据商户Uuid查询机构信息（新）-v1.4
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2992')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/viewBusinessInforByMerchant"
    LOGGER.info("根据商户Uuid查询机构信息（新）-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询机构信息（新）-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询机构信息（新）-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, effectivetimebegin, effectivetimeend, legalpersonuuid, mobile, name):
    """
    修改法人信息-v1.4
    :param legalpersonuuid: 法人uuid,string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param mobile: 手机号码(Y),string
    :param effectivetimebegin: 身份证有效时间开始,string
    :param effectivetimeend: 身份证有效时间结束,string
    :param cardnumber: 证件号码(Y),string
    :param name: 法人代表姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2993')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/updateLegalPerson"
    LOGGER.info("修改法人信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["effectiveTimeBegin"] = effectivetimebegin
    params["effectiveTimeEnd"] = effectivetimeend
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("修改法人信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法人信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_deleteLegalPerson(uid):
    """
    删除法人信息
    :param uid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2994')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/deleteLegalPerson"
    LOGGER.info("删除法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, effectivetimebegin, effectivetimeend, legalpersonuuid, mobile, name):
    """
    新增法人信息-v1.4
    :param mobile: 手机号码(Y),string
    :param legalpersonuuid: 法人代表Uuid(N),string
    :param name: 法人代表姓名(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param effectivetimeend: 身份证有效时间结束,string
    :param effectivetimebegin: 身份证有效时间开始,string
    :param cardnumber: 证件号码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2995')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/saveLegalPerson"
    LOGGER.info("新增法人信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["effectiveTimeBegin"] = effectivetimebegin
    params["effectiveTimeEnd"] = effectivetimeend
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("新增法人信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增法人信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(uid):
    """
    根据商户Uuid查询法人信息-v1.4
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2996')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/viewLegalPersonByMerchant"
    LOGGER.info("根据商户Uuid查询法人信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询法人信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询法人信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_updateClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, province, region):
    """
    修改结算信息-v1.4
    :param accountopeningbank: 开户银行(Y),string
    :param linenumber: 联行行号(Y),string
    :param clearingaccountuuid: 商户结算Uuid(Y),string
    :param province: 省(Y),number
    :param region: 区/县(Y),number
    :param branchname: 支行名称(Y),string
    :param accountname: 开户人名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accounttype: 账户类型(Y),string
    :param city: 市(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2997')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/updateClearingAccount"
    LOGGER.info("修改结算信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountName"] = accountname
    params["accountNumber"] = accountnumber
    params["accountOpeningBank"] = accountopeningbank
    params["accountType"] = accounttype
    params["branchName"] = branchname
    params["chamberlainIdCard"] = chamberlainidcard
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["clearingAccountUuid"] = clearingaccountuuid
    params["lineNumber"] = linenumber
    params["province"] = province
    params["region"] = region
    LOGGER.info("修改结算信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改结算信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_deleteClearingAccount(uid):
    """
    删除结算信息
    :param uid: 商户结算Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2998')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/deleteClearingAccount"
    LOGGER.info("删除结算信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, province, region):
    """
    新增结算信息-v1.4
    :param accountopeningbank: 开户银行(Y),string
    :param city: 市(Y),number
    :param linenumber: 联行行号(Y),string
    :param accounttype: 账户类型(Y),string
    :param accountname: 开户人名称,string
    :param province: 省(Y),number
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param accountnumber: 结算账号(Y),string
    :param clearingaccountuuid: 商户结算Uuid(N),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param region: 区/县(Y),number
    :param branchname: 支行名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2999')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/saveClearingAccount"
    LOGGER.info("新增结算信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountName"] = accountname
    params["accountNumber"] = accountnumber
    params["accountOpeningBank"] = accountopeningbank
    params["accountType"] = accounttype
    params["branchName"] = branchname
    params["chamberlainIdCard"] = chamberlainidcard
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["clearingAccountUuid"] = clearingaccountuuid
    params["lineNumber"] = linenumber
    params["province"] = province
    params["region"] = region
    LOGGER.info("新增结算信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增结算信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(uid):
    """
    根据商户Uuid查询结算信息-v1.4
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3000')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/viewClearingAccountByMerchant"
    LOGGER.info("根据商户Uuid查询结算信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询结算信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询结算信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_updateStore(area, businessaddress, businessaddressgpsloction, city, cityname, email, employeesnum, idcardnumber, leasetimebegin, leasetimeend, managername, managerphone, merchantuuid, numberbegindate, numberenddate, province, provincename, region, regionname, storename, storeuuid):
    """
    修改门店信息-v1.4
    :param numberenddate: 身份证有效期结束时间,string
    :param managerphone: 门店负责人电话(Y),string
    :param leasetimebegin: 租赁开始时间,string
    :param provincename: 省名称,string
    :param numberbegindate: 身份证有效期开始时间,string
    :param businessaddress: 实际经营地址(Y),string
    :param regionname: 区名称,string
    :param area: 门店租赁面积（平方）,number
    :param region: 区id,number
    :param merchantuuid: 商户Uuid(Y),string
    :param leasetimeend: 租赁结束时间,string
    :param managername: 门店负责人姓名(Y),string
    :param province: 省id,number
    :param cityname: 市名称,string
    :param idcardnumber: 身份证号码,string
    :param employeesnum: 员工总数,number
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param city: 市id,number
    :param email: 业务邮箱,string
    :param storename: 门店名称,string
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3001')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStore"
    LOGGER.info("修改门店信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["area"] = area
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["city"] = city
    params["cityName"] = cityname
    params["email"] = email
    params["employeesNum"] = employeesnum
    params["idcardNumber"] = idcardnumber
    params["leaseTimeBegin"] = leasetimebegin
    params["leaseTimeEnd"] = leasetimeend
    params["managerName"] = managername
    params["managerPhone"] = managerphone
    params["merchantUuid"] = merchantuuid
    params["numberBeginDate"] = numberbegindate
    params["numberEndDate"] = numberenddate
    params["province"] = province
    params["provinceName"] = provincename
    params["region"] = region
    params["regionName"] = regionname
    params["storeName"] = storename
    params["storeUuid"] = storeuuid
    LOGGER.info("修改门店信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改门店信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_saveStore(area, businessaddress, businessaddressgpsloction, city, cityname, email, employeesnum, idcardnumber, leasetimebegin, leasetimeend, managername, managerphone, merchantuuid, numberbegindate, numberenddate, province, provincename, region, regionname, storename, storeuuid):
    """
    新增门店信息-v1.4、v1.0.6
    :param merchantuuid: 商户Uuid(Y),string
    :param cityname: 市名称,string
    :param city: 市id,number
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param numberbegindate: 身份证有效期开始时间,string
    :param numberenddate: 身份证有效期结束时间,string
    :param provincename: 省名称,string
    :param leasetimeend: 租赁结束时间,string
    :param employeesnum: 员工总数,number
    :param leasetimebegin: 租赁开始时间,string
    :param managerphone: 门店负责人电话(Y),string
    :param storename: 门店名称,string
    :param province: 省id,number
    :param regionname: 区名称,string
    :param storeuuid: 门店Uuid(N),string
    :param idcardnumber: 身份证号码,string
    :param email: 业务邮箱,string
    :param area: 门店租赁面积（平方),number
    :param managername: 门店负责人姓名(Y),string
    :param region: 区id,number
    :param businessaddress: 实际经营地址(Y)详细地址,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3002')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
    LOGGER.info("新增门店信息-v1.4、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["area"] = area
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["city"] = city
    params["cityName"] = cityname
    params["email"] = email
    params["employeesNum"] = employeesnum
    params["idcardNumber"] = idcardnumber
    params["leaseTimeBegin"] = leasetimebegin
    params["leaseTimeEnd"] = leasetimeend
    params["managerName"] = managername
    params["managerPhone"] = managerphone
    params["merchantUuid"] = merchantuuid
    params["numberBeginDate"] = numberbegindate
    params["numberEndDate"] = numberenddate
    params["province"] = province
    params["provinceName"] = provincename
    params["region"] = region
    params["regionName"] = regionname
    params["storeName"] = storename
    params["storeUuid"] = storeuuid
    LOGGER.info("新增门店信息-v1.4、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增门店信息-v1.4、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewStore(uid):
    """
    查询门店信息-v1.4
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3003')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStore"
    LOGGER.info("查询门店信息-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询门店信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店信息-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewStoreList(auditstate, freezestate, managername, name, pagecurrent, pagesize, sign, uid):
    """
    查询门店列表-v1.5.2、v1.0.6
    :param auditstate: 审核状态,string
    :param managername: 门店负责人,string
    :param name: 门店名称,string
    :param pagesize: 分页大小(Y),number
    :param uid: 商户Uuid(Y),string
    :param sign: 租赁状态,string
    :param freezestate: 冻结状态,string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3004')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
    LOGGER.info("查询门店列表-v1.5.2、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["freezeState"] = freezestate
    params["managerName"] = managername
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["sign"] = sign
    params["uid"] = uid
    LOGGER.info("查询门店列表-v1.5.2、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店列表-v1.5.2、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_uploadQrcode(storeuuid):
    """
    下载门店二维码
    :param storeuuid: 门店uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3005')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/uploadQrcode"
    LOGGER.info("下载门店二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["MyToken"] = LICENCES
    LOGGER.info("下载门店二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载门店二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewImageRoleList(uid):
    """
    门店影像资料查询-v1.5.2
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3006')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewImageRoleList"
    LOGGER.info("门店影像资料查询-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("门店影像资料查询-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店影像资料查询-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_uploadImageRoleList(imagelist):
    """
    门店影像资料上传-v1.4
    :param imagelist: 影像资料集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3007')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/uploadImageRoleList"
    LOGGER.info("门店影像资料上传-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["imageList"] = imagelist
    LOGGER.info("门店影像资料上传-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店影像资料上传-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_deleteStore(uid):
    """
    删除门店信息
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3008')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteStore"
    LOGGER.info("删除门店信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_freeze(type, uid):
    """
    冻结门店/解冻-v1.4
    :param type: 冻结或者解冻,string
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3009')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/freeze"
    LOGGER.info("冻结门店/解冻-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    params["uid"] = uid
    LOGGER.info("冻结门店/解冻-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("冻结门店/解冻-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_storeExamine(ispass, message, uid):
    """
    门店审核-v1.4
    :param uid: 门店iuid(Y),string
    :param ispass: 是否通过(Y),string
    :param message: 审核信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3010')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/storeExamine"
    LOGGER.info("门店审核-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["isPass"] = ispass
    params["message"] = message
    params["uid"] = uid
    LOGGER.info("门店审核-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店审核-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent, list, storeuuid, workpercent):
    """
    门店业务信息-新增或修改-v1.4
    :param discountpercent: 贴息占比,number
    :param workpercent: 工作占比,number
    :param storeuuid: 门店id,string
    :param list: 商品数据,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3011')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStoreBusiness"
    LOGGER.info("门店业务信息-新增或修改-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountPercent"] = discountpercent
    params["list"] = list
    params["storeUuid"] = storeuuid
    params["workPercent"] = workpercent
    LOGGER.info("门店业务信息-新增或修改-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店业务信息-新增或修改-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewStoreBusiness(uid):
    """
    门店业务信息-查询-v1.4
    :param uid: 门店id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3012')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreBusiness"
    LOGGER.info("门店业务信息-查询-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("门店业务信息-查询-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店业务信息-查询-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_saveImagesAndChange(images):
    """
    门店影像图片信息保存-1.5.2、v1.0.6
    :param images: 图片集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3013')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveImagesAndChange"
    LOGGER.info("门店影像图片信息保存-1.5.2、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["images"] = images
    LOGGER.info("门店影像图片信息保存-1.5.2、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店影像图片信息保存-1.5.2、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_merchantMoneyEnlarge(uid, zoomcoefficient):
    """
    修改预授信放大系数
    :param uid: 商户额度Uuid(Y),string
    :param zoomcoefficient: 预授信额度放大系数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3014')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/merchantMoneyEnlarge"
    LOGGER.info("修改预授信放大系数请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("修改预授信放大系数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改预授信放大系数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_updateMerchantMoney(amountday, amountmonth, amountsingle, amountsum, loandownlimit, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    修改额度管理-v1.5、v1.0.4
    :param amountsingle: 单笔总额度-日(Y),number
    :param amountmonth: 总额度-月(Y),number
    :param merchantuuid: 商户Uuid(Y),string
    :param loandownlimit: 单次放款上限--美佳v1.0.4新增,number
    :param zoomcoefficient: 预授信额度放大系数(N),number
    :param moneyconfiguuid: 商户额度Uuid(Y),string
    :param amountday: 总额度-日(Y),number
    :param amountsum: 总额度(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3015')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
    LOGGER.info("修改额度管理-v1.5、v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["loandownLimit"] = loandownlimit
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("修改额度管理-v1.5、v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改额度管理-v1.5、v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_deleteMerchantMoney(uid):
    """
    删除额度管理
    :param uid: 商户额度Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3016')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/deleteMerchantMoney"
    LOGGER.info("删除额度管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_saveMerchantMoney(amountday, amountmonth, amountsingle, amountsum, loandownlimit, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    新增额度管理-v1.5、v1.0.4
    :param zoomcoefficient: 预授信额度放大系数(N),number
    :param amountday: 总额度-日(Y),number
    :param merchantuuid: 商户Uuid(Y),string
    :param amountmonth: 总额度-月(Y),number
    :param moneyconfiguuid: 商户额度Uuid(N),string
    :param amountsingle: 总额度-单笔(Y),number
    :param amountsum: 总额度(Y),number
    :param loandownlimit: 单次放款上限--美佳v1.0.4新增,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3017')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
    LOGGER.info("新增额度管理-v1.5、v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["loandownLimit"] = loandownlimit
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("新增额度管理-v1.5、v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增额度管理-v1.5、v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(uid):
    """
    根据商户Uuid查询额度管理-v1.5
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3018')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyByMerchant"
    LOGGER.info("根据商户Uuid查询额度管理-v1.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询额度管理-v1.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询额度管理-v1.5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyList(name, pagecurrent, pagesize):
    """
    风险控制列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3019')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyList"
    LOGGER.info("风险控制列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("风险控制列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风险控制列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_range_deleteMerchantManagementRange(uid):
    """
    商户经营范围删除
    :param uid: 商户经营范围uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3020')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/deleteMerchantManagementRange"
    LOGGER.info("商户经营范围删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("商户经营范围删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户经营范围删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_range_addMerchantManagementRange(city, cityname, created, merchantuuid, province, provincename, updated):
    """
    商户经营范围新增
    :param created: 创建时间,string
    :param cityname: 市名称,string
    :param merchantuuid: 商户uuid,string
    :param updated: 更新时间,string
    :param provincename: 省名称,string
    :param city: 市id,number
    :param province: 省id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3021')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/addMerchantManagementRange"
    LOGGER.info("商户经营范围新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["cityName"] = cityname
    params["created"] = created
    params["merchantUuid"] = merchantuuid
    params["province"] = province
    params["provinceName"] = provincename
    params["updated"] = updated
    LOGGER.info("商户经营范围新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户经营范围新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_range_findMMRByMerchantUuid(uid):
    """
    通过商户uuid查询商户经营范围
    :param uid: 商户的uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3022')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/findMMRByMerchantUuid"
    LOGGER.info("通过商户uuid查询商户经营范围请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("通过商户uuid查询商户经营范围请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过商户uuid查询商户经营范围请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_examine_merchanrExamine(message, type, uid):
    """
    商户审核-v1.5.1
    :param message: 审核信息,string
    :param type: imperfect 打回 pass 通过 fail 失败,pending_review提交审核,string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3023')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/merchanrExamine"
    LOGGER.info("商户审核-v1.5.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["message"] = message
    params["type"] = type
    params["uid"] = uid
    LOGGER.info("商户审核-v1.5.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户审核-v1.5.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_repulse(uid):
    """
    查看被打回的模块1.5.1
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3024')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/repulse"
    LOGGER.info("查看被打回的模块1.5.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查看被打回的模块1.5.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看被打回的模块1.5.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_findBond(merchantuuid, pagecurrent, pagesize):
    """
    商户保证金缴纳记录查询-v1.5.2
    :param pagesize: 每页几条（y）,number
    :param pagecurrent: 当前页（y）,number
    :param merchantuuid: 商户UUID（y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3025')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/findBond"
    LOGGER.info("商户保证金缴纳记录查询-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("商户保证金缴纳记录查询-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户保证金缴纳记录查询-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_addOrUpdateBond(deductionamount, deductiondate, merchantuuid, payamount, paydate, poolamount, pooldate, returnamount, returndate):
    """
    新增或者编辑商户保证金模块-v1.5.2
    :param merchantuuid: 商户UUID（Y）,string
    :param returnamount: 退还商户金额,string
    :param paydate: 缴纳时间,string
    :param poolamount: 退回保证池金额,string
    :param returndate: 退还商户时间,string
    :param deductionamount: 保证金扣除金额,string
    :param pooldate: 退回保证池时间,string
    :param deductiondate: 保证金扣除时间,string
    :param payamount: 缴纳金额,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3026')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/addOrUpdateBond"
    LOGGER.info("新增或者编辑商户保证金模块-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["deductionAmount"] = deductionamount
    params["deductionDate"] = deductiondate
    params["merchantUuid"] = merchantuuid
    params["payAmount"] = payamount
    params["payDate"] = paydate
    params["poolAmount"] = poolamount
    params["poolDate"] = pooldate
    params["returnAmount"] = returnamount
    params["returnDate"] = returndate
    LOGGER.info("新增或者编辑商户保证金模块-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增或者编辑商户保证金模块-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(platformprivilegeuuid, platformuseruuid):
    """
    新增/修改权限
    :param platformprivilegeuuid: 权限UUid(Y),string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3027')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
    LOGGER.info("新增/修改权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["platformPrivilegeUuid"] = platformprivilegeuuid
    params["platformUserUuid"] = platformuseruuid
    LOGGER.info("新增/修改权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增/修改权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(permissiontype, platformuseruuid):
    """
    查询权限
    :param permissiontype: 权限类型,string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3028')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewUserPrivilegeList"
    LOGGER.info("查询权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["permissionType"] = permissiontype
    params["platformUserUuid"] = platformuseruuid
    LOGGER.info("查询权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_clearUserPrivilege(uid):
    """
    清除用户权限
    :param uid: 用户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3029')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/clearUserPrivilege"
    LOGGER.info("清除用户权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("清除用户权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("清除用户权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_deleteMenu(uid):
    """
    删除一个菜单
    :param uid: 数据UUId,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3030')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/deleteMenu"
    LOGGER.info("删除一个菜单请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除一个菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一个菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_saveMenu(name, platformprivilegeuuid, url):
    """
    保存一个菜单
    :param url: 菜单路径（Y）,string
    :param name: 菜单名称（Y）,string
    :param platformprivilegeuuid: 菜单uuid（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3031')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveMenu"
    LOGGER.info("保存一个菜单请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["platformPrivilegeUuid"] = platformprivilegeuuid
    params["url"] = url
    LOGGER.info("保存一个菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存一个菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_privilege_viewMenus(paramsingle):
    """
    查询所有菜单
    :param paramsingle: 菜单类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3032')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewMenus"
    LOGGER.info("查询所有菜单请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("查询所有菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询所有菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_updateSystemUser(email, mobile, name, platformuserprofileuuid):
    """
    修改用户
    :param mobile: 用户手机(Y),string
    :param email: 用户邮箱(Y),string
    :param platformuserprofileuuid: 用户Uuid(Y),string
    :param name: 用户姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3033')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUser"
    LOGGER.info("修改用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    params["platformUserProfileUuid"] = platformuserprofileuuid
    LOGGER.info("修改用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_deleteSystemUser(uid):
    """
    删除用户
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3034')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/deleteSystemUser"
    LOGGER.info("删除用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_saveSystemUser(email, mobile, name):
    """
    新增用户
    :param mobile: 用户手机(Y),string
    :param name: 用户姓名(Y),string
    :param email: 用户邮箱(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3035')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/saveSystemUser"
    LOGGER.info("新增用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("新增用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUser(paramsingle):
    """
    查询用户
    :param paramsingle: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3036')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUser"
    LOGGER.info("查询用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramSingle"] = paramsingle
    LOGGER.info("查询用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_login(email, password):
    """
    用户登陆
    :param email: 用户帐户(Y),string
    :param password: 用户密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3037')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["password"] = password
    LOGGER.info("用户登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUserList(name, pagecurrent, pagesize):
    """
    查询用户列表
    :param name: 用户姓名(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3038')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUserList"
    LOGGER.info("查询用户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询用户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_resetUserPass(uid):
    """
    重置密码
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3039')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/resetUserPass"
    LOGGER.info("重置密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("重置密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重置密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_updateSystemUserState(uid, updatestate):
    """
    状态修改
    :param updatestate: 修改状态(Y),string
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3040')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUserState"
    LOGGER.info("状态修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    params["updateState"] = updatestate
    LOGGER.info("状态修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("状态修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_updateUserPass(email, password, passwordrepeat, uid):
    """
    修改密码
    :param passwordrepeat: 用户密码重复(N),string
    :param email: 用户邮箱(Y),string
    :param password: 用户密码(Y),string
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3041')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateUserPass"
    LOGGER.info("修改密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["password"] = password
    params["passwordRepeat"] = passwordrepeat
    params["uid"] = uid
    LOGGER.info("修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_FileUploadController_handlerFileUpload():
    """
    图片上传
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3042')
    requesturl = baseUrl + "/FileUploadController/handlerFileUpload"
    LOGGER.info("图片上传请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("图片上传请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("图片上传请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_firstCheck(checkstate, firstchecksuggest, message, uuid):
    """
    初审---美佳v1.0.4
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :param firstchecksuggest: 初审建议首打款金额,number
    :param uuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3043')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/firstCheck"
    LOGGER.info("初审---美佳v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["firstCheckSuggest"] = firstchecksuggest
    params["message"] = message
    params["uuid"] = uuid
    LOGGER.info("初审---美佳v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审---美佳v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContract(uid):
    """
    初审信息查询-v1.5.1（美佳v1.0.0）
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3044')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
    LOGGER.info("初审信息查询-v1.5.1（美佳v1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("初审信息查询-v1.5.1（美佳v1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审信息查询-v1.5.1（美佳v1.0.0）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContracts(begindate, contractnumber, enddate, firstcheckname, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    初审列表查询---会美1.0.0
    :param name: 编号等一系列东西,string
    :param begindate: 开始时间,string
    :param phone: 电话号码,string
    :param lable: 标签,string
    :param state: 状态,string
    :param username: 用户名,string
    :param enddate: 结束时间,string
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :param contractnumber: 合同编号,string
    :param firstcheckname: 一审审核人姓名（会美1.0.0）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3045')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
    LOGGER.info("初审列表查询---会美1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["firstCheckName"] = firstcheckname
    params["lable"] = lable
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["state"] = state
    params["userName"] = username
    LOGGER.info("初审列表查询---会美1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审列表查询---会美1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewTongdunInfo(uid):
    """
    同盾信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3046')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("同盾信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewImageDataConfig(subdivisiontype):
    """
    查询影像列表-废弃
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3047')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewImageDataConfig"
    LOGGER.info("查询影像列表-废弃请求地址:【{}】".format(requesturl))
    params = dict()
    params["subdivisionType"] = subdivisiontype
    LOGGER.info("查询影像列表-废弃请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询影像列表-废弃请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_selectCanAuditCheck(checktype, uid):
    """
    是否有权限审核
    :param uid: 合同uuid,string
    :param checktype: 数据类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3048')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/selectCanAuditCheck"
    LOGGER.info("是否有权限审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkType"] = checktype
    params["uid"] = uid
    LOGGER.info("是否有权限审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("是否有权限审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_delAuditComment(uid):
    """
    删除一条评论
    :param uid: 评论uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3049')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/delAuditComment"
    LOGGER.info("删除一条评论请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_findAuditCommentList():
    """
    审核意见
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3050')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findAuditCommentList"
    LOGGER.info("审核意见请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("审核意见请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核意见请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_addAuditComment():
    """
    添加审核意见
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3051')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addAuditComment"
    LOGGER.info("添加审核意见请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("添加审核意见请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加审核意见请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_editAuditComment():
    """
    修改审核意见
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3052')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/editAuditComment"
    LOGGER.info("修改审核意见请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("修改审核意见请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改审核意见请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogs():
    """
    查看操作日志
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3053')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogs"
    LOGGER.info("查看操作日志请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查看操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看操作日志请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_deleteContractCustomerLabel(uid):
    """
    删除客户标签
    :param uid: 标签uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3054')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/deleteContractCustomerLabel"
    LOGGER.info("删除客户标签请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_addContractCustomerLabel():
    """
    添加客户标签
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3055')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addContractCustomerLabel"
    LOGGER.info("添加客户标签请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("添加客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加客户标签请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractLabels():
    """
    客户标签
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3056')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractLabels"
    LOGGER.info("客户标签请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogInfo(contractoperationloguuid, contractuuid):
    """
    查询操作日志详情
    :param contractoperationloguuid: 操作记录UUID,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3057')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogInfo"
    LOGGER.info("查询操作日志详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractOperationLogUuid"] = contractoperationloguuid
    params["contractUuid"] = contractuuid
    LOGGER.info("查询操作日志详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询操作日志详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractImages(contractuuid):
    """
    审核详情-影像资料v1.4.0（美佳1.0.0）
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3058')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractImages"
    LOGGER.info("审核详情-影像资料v1.4.0（美佳1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("审核详情-影像资料v1.4.0（美佳1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情-影像资料v1.4.0（美佳1.0.0）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewMxInfo(contractuuid, type):
    """
    查询魔蝎报告
    :param contractuuid: 合同id,string
    :param type: 报告类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3059')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewMxInfo"
    LOGGER.info("查询魔蝎报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["type"] = type
    LOGGER.info("查询魔蝎报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询魔蝎报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_fdd_findFDD(contractuuid):
    """
    法大大查询
    :param contractuuid: 合同uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3060')
    requesturl = baseUrl + "/api/78dk/platform/tm/fdd/findFDD"
    LOGGER.info("法大大查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("法大大查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_bd_viewBdInfo(uid):
    """
    查询BD信息
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3061')
    requesturl = baseUrl + "/api/78dk/platform/tm/bd/viewBdInfo"
    LOGGER.info("查询BD信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询BD信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询BD信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid):
    """
    商户结算信息查询接口
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3062')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/businessbillinginformation"
    LOGGER.info("商户结算信息查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("商户结算信息查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户结算信息查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_xuexinreport(contractuuid):
    """
    学信网报告
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3063')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/xuexinreport"
    LOGGER.info("学信网报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("学信网报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网报告请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_alipayreport(contractuuid):
    """
    支付宝报告
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3064')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/alipayreport"
    LOGGER.info("支付宝报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("支付宝报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("支付宝报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_setSupplementState2Yes(contractuuid):
    """
    翻转合同补录状态为Yes
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3065')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/setSupplementState2Yes"
    LOGGER.info("翻转合同补录状态为Yes请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("翻转合同补录状态为Yes请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("翻转合同补录状态为Yes请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_showSupplementImage(contractuuid):
    """
    展示补录的图片资料-v1.4.0
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3066')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/showSupplementImage"
    LOGGER.info("展示补录的图片资料-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("展示补录的图片资料-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("展示补录的图片资料-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_queryElectronuclearRemark(contractuuid):
    """
    电核备注-查询接口
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3067')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/queryElectronuclearRemark"
    LOGGER.info("电核备注-查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("电核备注-查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核备注-查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_saveCustomerInformation(contractuuid, customerinformation):
    """
    电核备注-客户信息保存接口
    :param customerinformation: 客户信息,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3068')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveCustomerInformation"
    LOGGER.info("电核备注-客户信息保存接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["customerInformation"] = customerinformation
    LOGGER.info("电核备注-客户信息保存接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核备注-客户信息保存接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_saveImpactData(contractuuid, impactdata):
    """
    电核备注-影像资料保存接口
    :param impactdata: 影像资料,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3069')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveImpactData"
    LOGGER.info("电核备注-影像资料保存接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["impactData"] = impactdata
    LOGGER.info("电核备注-影像资料保存接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核备注-影像资料保存接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_saveWindControlDataSource(contractuuid, windcontroldatasource):
    """
    电核备注-风控数据源保存接口
    :param contractuuid: 合同UUID,string
    :param windcontroldatasource: 风控数据源,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3070')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveWindControlDataSource"
    LOGGER.info("电核备注-风控数据源保存接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["windControlDataSource"] = windcontroldatasource
    LOGGER.info("电核备注-风控数据源保存接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核备注-风控数据源保存接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewLabels():
    """
    标签查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3071')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewLabels"
    LOGGER.info("标签查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("标签查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("标签查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_contract_repaymentPlan(uid):
    """
    还款计划（v1.0.2）
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3072')
    requesturl = baseUrl + "/api/78dk/platform/tm/contract/repaymentPlan"
    LOGGER.info("还款计划（v1.0.2）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("还款计划（v1.0.2）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款计划（v1.0.2）请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_telephoneCheck(checkstate, message, uuid):
    """
    电核
    :param uuid: 合同uuid,string
    :param message: 审核人提交信息,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3073')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/telephoneCheck"
    LOGGER.info("电核请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["message"] = message
    params["uuid"] = uuid
    LOGGER.info("电核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid):
    """
    电核信息查询-v1.5.1（美佳v1.0.0）
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3074')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
    LOGGER.info("电核信息查询-v1.5.1（美佳v1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("电核信息查询-v1.5.1（美佳v1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核信息查询-v1.5.1（美佳v1.0.0）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(begindate, contractnumber, enddate, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    电核列表查询
    :param pagecurrent: 当前页,number
    :param phone: 电话号码,string
    :param contractnumber: 合同编号,string
    :param pagesize: 页面大小,number
    :param name: 编号等一系列东西,string
    :param lable: 标签,string
    :param username: 用户名,string
    :param state: 状态,string
    :param enddate: 结束时间,string
    :param begindate: 开始时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3075')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContracts"
    LOGGER.info("电核列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["lable"] = lable
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["state"] = state
    params["userName"] = username
    LOGGER.info("电核列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(answer, contractuuid, groupname, groupsort, question, questionsort, risktype, state, telephonecheckfeedbackuuid):
    """
    批量添加电核资料
    :param risktype: 风险类型,string
    :param contractuuid: 合同UUID,string
    :param groupsort: 分组排序字段,number
    :param question: 问题,string
    :param telephonecheckfeedbackuuid: 电核uuid,string
    :param state: 数据状态,string
    :param questionsort: 问题排序字段,number
    :param answer: 答案,string
    :param groupname: 分组名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3076')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/addTelephoneCheckInfos"
    LOGGER.info("批量添加电核资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["answer"] = answer
    params["contractUuid"] = contractuuid
    params["groupName"] = groupname
    params["groupSort"] = groupsort
    params["question"] = question
    params["questionSort"] = questionsort
    params["riskType"] = risktype
    params["state"] = state
    params["telephoneCheckFeedbackUuid"] = telephonecheckfeedbackuuid
    LOGGER.info("批量添加电核资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("批量添加电核资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(uid):
    """
    查询合同已经填写的电核问题列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3077')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询合同已经填写的电核问题列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid):
    """
    删除电核资料
    :param uid: 电核资料uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3078')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/deleteTelephoneCheckInfo"
    LOGGER.info("删除电核资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除电核资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除电核资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_viewFDDInfo(uid):
    """
    法大大信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3079')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("法大大信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_finalCheck(checkstate, finalchecksuggest, preamount, uuid):
    """
    终审（美佳v1.0.0）v1.0.4
    :param checkstate: 审核状态,string
    :param finalchecksuggest: 终审建议首打款金额,string
    :param preamount: 终审金额,string
    :param uuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3080')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/finalCheck"
    LOGGER.info("终审（美佳v1.0.0）v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["finalCheckSuggest"] = finalchecksuggest
    params["preAmount"] = preamount
    params["uuid"] = uuid
    LOGGER.info("终审（美佳v1.0.0）v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审（美佳v1.0.0）v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContract(uid):
    """
    终审信息查询（美佳1.0.0新增一个字段）v1.0.4
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3081')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContract"
    LOGGER.info("终审信息查询（美佳1.0.0新增一个字段）v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("终审信息查询（美佳1.0.0新增一个字段）v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审信息查询（美佳1.0.0新增一个字段）v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContracts(begindate, contractnumber, enddate, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    终审列表查询v1.0.4
    :param state: 状态,string
    :param begindate: 开始时间,string
    :param pagesize: 页面大小,number
    :param phone: 电话号码,string
    :param lable: 标签,string
    :param pagecurrent: 当前页,number
    :param contractnumber: 合同编号,string
    :param name: 编号等一系列东西,string
    :param enddate: 结束时间,string
    :param username: 用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3082')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
    LOGGER.info("终审列表查询v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["lable"] = lable
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["state"] = state
    params["userName"] = username
    LOGGER.info("终审列表查询v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审列表查询v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_after_viewAuditMonitors(enddate, pagecurrent, pagesize, qifascore, searchwhere, startdate):
    """
    贷后列表
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :param qifascore: 启发分数状态,string
    :param enddate: 结束日期,string
    :param searchwhere: 查询条件,string
    :param startdate: 开始日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3083')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewAuditMonitors"
    LOGGER.info("贷后列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["qifaScore"] = qifascore
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("贷后列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷后列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_after_viewReportContract(uid):
    """
    查询报告内容
    :param uid: 报告UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3084')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewReportContract"
    LOGGER.info("查询报告内容请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询报告内容请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询报告内容请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_after_viewContractTongDuns(uid):
    """
    查询贷后所用同盾报告列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3085')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewContractTongDuns"
    LOGGER.info("查询贷后所用同盾报告列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询贷后所用同盾报告列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询贷后所用同盾报告列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_findTemplateDictionaries():
    """
    查询所有模板配置字典
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3086')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/findTemplateDictionaries"
    LOGGER.info("查询所有模板配置字典请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询所有模板配置字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询所有模板配置字典请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_findProductByTemplate(pagecurrent, pagesize, producttemplateuuid):
    """
    查询模板关联产品
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :param producttemplateuuid: 模板UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3087')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/findProductByTemplate"
    LOGGER.info("查询模板关联产品请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["productTemplateUuid"] = producttemplateuuid
    LOGGER.info("查询模板关联产品请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询模板关联产品请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_templateList(name, pagecurrent, pagesize):
    """
    模板查询列表
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :param name: 模板名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3088')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/templateList"
    LOGGER.info("模板查询列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("模板查询列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("模板查询列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_templateDetails(producttemplateuuid):
    """
    模板详情查询
    :param producttemplateuuid: 模板UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3089')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/templateDetails"
    LOGGER.info("模板详情查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["productTemplateUuid"] = producttemplateuuid
    LOGGER.info("模板详情查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("模板详情查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_addOrEditTemplate(producttemplateuuid, remark, sysdata, templatename, templatetype):
    """
    添加或者编辑进件模板
    :param templatename: 模板名称,string
    :param producttemplateuuid: 模板UUID,string
    :param remark: 备注,string
    :param sysdata: 进件配置项,array<number>
    :param templatetype: 模板类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3090')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/addOrEditTemplate"
    LOGGER.info("添加或者编辑进件模板请求地址:【{}】".format(requesturl))
    params = dict()
    params["productTemplateUuid"] = producttemplateuuid
    params["remark"] = remark
    params["sysData"] = sysdata
    params["templateName"] = templatename
    params["templateType"] = templatetype
    LOGGER.info("添加或者编辑进件模板请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加或者编辑进件模板请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid):
    """
    删除进件模板
    :param producttemplateuuid: 模板UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3091')
    requesturl = baseUrl + "/api/78dk/platform/tm/incoming/delTemplate"
    LOGGER.info("删除进件模板请求地址:【{}】".format(requesturl))
    params = dict()
    params["productTemplateUuid"] = producttemplateuuid
    LOGGER.info("删除进件模板请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除进件模板请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_machine_resultMachine(uuid):
    """
    机审详情
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3092')
    requesturl = baseUrl + "/api/78dk/platform/tm/machine/resultMachine"
    LOGGER.info("机审详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("机审详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机审详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_operationalCheck(begindate, enddate, name, pagecurrent, pagesize, phone, state, uuid):
    """
    运营审核列表查询-v1.5.0
    :param pagecurrent: 当前页,number
    :param name: 姓名,string
    :param enddate: 结束时间,string
    :param pagesize: 页面大小,number
    :param begindate: 开始时间,string
    :param uuid: 合同号,string
    :param phone: 电话,string
    :param state: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3093')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/operationalCheck"
    LOGGER.info("运营审核列表查询-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["state"] = state
    params["uuid"] = uuid
    LOGGER.info("运营审核列表查询-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营审核列表查询-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_operationAllsave(begindate, checkstate, enddate, message, name, pagecurrent, phone, state, uuid):
    """
    运营审核-批量
    :param phone: 电话,string
    :param begindate: 开始时间,string
    :param name: 姓名,string
    :param uuid: 合同号,string
    :param pagecurrent: 总计条数,
    :param enddate: 结束时间,string
    :param state: 订单状态(pending),string
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3094')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/operationAllsave"
    LOGGER.info("运营审核-批量请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["checkState"] = checkstate
    params["enddate"] = enddate
    params["message"] = message
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["phone"] = phone
    params["state"] = state
    params["uuid"] = uuid
    LOGGER.info("运营审核-批量请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营审核-批量请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid):
    """
    运营审批信息查询（美佳v1.0.0新增字段）
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3095')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/viewOperateCheckContract"
    LOGGER.info("运营审批信息查询（美佳v1.0.0新增字段）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("运营审批信息查询（美佳v1.0.0新增字段）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营审批信息查询（美佳v1.0.0新增字段）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_operationalsave(checkstate, message, uuid):
    """
    运营审核
    :param checkstate: 审核状态,string
    :param uuid: 合同号,string
    :param message: 审核人提交信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3096')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/operationalsave"
    LOGGER.info("运营审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["message"] = message
    params["uuid"] = uuid
    LOGGER.info("运营审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_downOperationalCheck(begindate, enddate, name, phone, state, uuid):
    """
    运营列表导出-v1.4.0
    :param uuid: 合同编号,string
    :param name: 姓名,string
    :param phone: 电话,string
    :param enddate: 结束时间,string
    :param state: 状态,string
    :param begindate: 开始时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3097')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/downOperationalCheck"
    LOGGER.info("运营列表导出-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["phone"] = phone
    params["state"] = state
    params["uuid"] = uuid
    params["MyToken"] = LICENCES
    LOGGER.info("运营列表导出-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营列表导出-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_contractDetail(contractuuid, process):
    """
    订单详情--会美1.0.0
    :param process: 订单流程，查询的是初审还是终审,string
    :param contractuuid: 订单uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3098')
    requesturl = baseUrl + "/api/78dk/platform/tm/contractDetail"
    LOGGER.info("订单详情--会美1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["process"] = process
    LOGGER.info("订单详情--会美1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单详情--会美1.0.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryMailList(contractuuid, uid):
    """
    通讯录信息-v1.5.2(美佳v1.0.2，这个接口被用于信审管理通讯录)
    :param contractuuid: 订单id，选填,
    :param uid: 用户uuid，选填，两个参数必须有一个,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3099')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryMailList"
    LOGGER.info("通讯录信息-v1.5.2(美佳v1.0.2，这个接口被用于信审管理通讯录)请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["uid"] = uid
    LOGGER.info("通讯录信息-v1.5.2(美佳v1.0.2，这个接口被用于信审管理通讯录)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通讯录信息-v1.5.2(美佳v1.0.2，这个接口被用于信审管理通讯录)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryCallList(contractuuid, pagecurrent, pagesize, useruuid):
    """
    查询通话详单(美佳v1.0.0)
    :param pagecurrent: 当前页（Y）,number
    :param pagesize: 每页条数（Y）,number
    :param contractuuid: 订单uid，和用户uid选填,
    :param useruuid: 用户uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3100')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryCallList"
    LOGGER.info("查询通话详单(美佳v1.0.0)请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["userUuid"] = useruuid
    LOGGER.info("查询通话详单(美佳v1.0.0)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询通话详单(美佳v1.0.0)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_auditReject(auditprocess, contractuuid, rejectmodel):
    """
    审核驳回--美佳v1.0.4新增
    :param contractuuid: 驳回订单uid,string
    :param rejectmodel: 被驳回的模块,array<object>
    :param auditprocess: firstCheck初审驳回、finalCheck终审驳回,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3101')
    requesturl = baseUrl + "/api/78dk/platform/tm/auditReject"
    LOGGER.info("审核驳回--美佳v1.0.4新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditProcess"] = auditprocess
    params["contractUuid"] = contractuuid
    params["rejectModel"] = rejectmodel
    LOGGER.info("审核驳回--美佳v1.0.4新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核驳回--美佳v1.0.4新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewContracts(begindate, enddate, name, orderstate, pagecurrent, pagesize):
    """
    合同列表查询（申请列表）hm-1.0.0
    :param orderstate: 订单状态(v1.1.3新增未还、初审驳回、终审驳回),string
    :param name: 组合查询字段,string
    :param begindate: 开始时间,string
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :param enddate: 结束时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3102')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContracts"
    LOGGER.info("合同列表查询（申请列表）hm-1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("合同列表查询（申请列表）hm-1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同列表查询（申请列表）hm-1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewContract(uid):
    """
    合同详情查询hm-1.0.0
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3103')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContract"
    LOGGER.info("合同详情查询hm-1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("合同详情查询hm-1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同详情查询hm-1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewTongdunInfo(uid):
    """
    同盾信息查询
    :param uid: 同盾id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3104')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("同盾信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewFDDInfo(uid):
    """
    法大大信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3105')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("法大大信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewUserBill(name, pagecurrent, pagesize):
    """
    账单信息查询
    :param name: 编号什么的,string
    :param pagesize: 每页条数,number
    :param pagecurrent: 当前页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3106')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewUserBill"
    LOGGER.info("账单信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("账单信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid):
    """
    查询合同已经填写的电核问题列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3107')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询合同已经填写的电核问题列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewBaiDuInfo(uid):
    """
    查询百度接口
    :param uid: 百度报告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3108')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewBaiDuInfo"
    LOGGER.info("查询百度接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询百度接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询百度接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_downContracts(begindate, enddate, name, orderstate):
    """
    导出申请列表-v1.4.0
    :param enddate: 结束时间,number
    :param orderstate: 订单状态,string
    :param begindate: 开始时候,number
    :param name: 组合查询字段,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3109')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["MyToken"] = LICENCES
    LOGGER.info("导出申请列表-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出申请列表-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewTencentInfo(uid):
    """
    查询腾讯接口
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3110')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTencentInfo"
    LOGGER.info("查询腾讯接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询腾讯接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询腾讯接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_chargeback(contractuuid, retreatmoney):
    """
    退单--美佳v1.0.4新增
    :param retreatmoney: 退单金额,number
    :param contractuuid: 退单uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3111')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/chargeback"
    LOGGER.info("退单--美佳v1.0.4新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["retreatMoney"] = retreatmoney
    LOGGER.info("退单--美佳v1.0.4新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退单--美佳v1.0.4新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_queryRefundInfo(contractuuid):
    """
    订单还款信息（v1.0.4）
    :param contractuuid: 合同 UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3112')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/queryRefundInfo"
    LOGGER.info("订单还款信息（v1.0.4）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("订单还款信息（v1.0.4）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单还款信息（v1.0.4）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_trans_findTransLogList(begindate, enddate, pagecurrent, pagesize, searchwhere, transstate, transtype):
    """
    交易流水列表
    :param transstate: 交易状态,string
    :param transtype: 交易类型,string
    :param begindate: 开始日期,string
    :param searchwhere: 查询条件,string
    :param enddate: 结束日期,string
    :param pagecurrent: 当前页（Y）,number
    :param pagesize: 页面大小（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3113')
    requesturl = baseUrl + "/api/78dk/platform/om/trans/findTransLogList"
    LOGGER.info("交易流水列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    params["transState"] = transstate
    params["transType"] = transtype
    LOGGER.info("交易流水列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("交易流水列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_trans_downTransLogList(begindate, enddate, searchwhereor, transstate, transtype):
    """
    下载交易流水
    :param transstate: 交易状态,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param transtype: 交易类型,string
    :param searchwhereor: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3114')
    requesturl = baseUrl + "/api/78dk/platform/om/trans/downTransLogList"
    LOGGER.info("下载交易流水请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["searchWhereOr"] = searchwhereor
    params["transState"] = transstate
    params["transType"] = transtype
    params["MyToken"] = LICENCES
    LOGGER.info("下载交易流水请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载交易流水请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_lm_loanOperation(bankseqid, contractuuid, loanamount, remarks, urls):
    """
    放款操作
    :param urls: 图片url,array<string>
    :param remarks: 备注,string
    :param bankseqid: 银行流水,string
    :param loanamount: 放款金额,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3115')
    requesturl = baseUrl + "/api/78dk/platform/om/lm/loanOperation"
    LOGGER.info("放款操作请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankSeqId"] = bankseqid
    params["contractUuid"] = contractuuid
    params["loanAmount"] = loanamount
    params["remarks"] = remarks
    params["urls"] = urls
    LOGGER.info("放款操作请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款操作请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_lm_findLoanModeList(pagecurrent, pagesize, searchwhere):
    """
    查询线下放款列表
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3116')
    requesturl = baseUrl + "/api/78dk/platform/om/lm/findLoanModeList"
    LOGGER.info("查询线下放款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    LOGGER.info("查询线下放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询线下放款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_findBdInfoList(bdstate, enddate, pagecurrent, pagesize, searchwhere, startdate):
    """
    BD列表v1.0.4
    :param pagecurrent: ,number
    :param startdate: ,string
    :param pagesize: ,number
    :param bdstate: ,string
    :param enddate: ,string
    :param searchwhere: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3117')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/findBdInfoList"
    LOGGER.info("BD列表v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdState"] = bdstate
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("BD列表v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD列表v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_addBdInfo(email, mobile, name):
    """
    BD新增v1.0.4
    :param name: 名称,string
    :param email: 邮箱,string
    :param mobile: 电话,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3118')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/addBdInfo"
    LOGGER.info("BD新增v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("BD新增v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD新增v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_replaceBdInfoMerchant(merchantuuids, newddinfouuid, oldddinfouuid):
    """
    BD替换
    :param newddinfouuid: 新BDUUID,string
    :param oldddinfouuid: 老BDUUID,string
    :param merchantuuids: 选中的商户UID,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3119')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/replaceBdInfoMerchant"
    LOGGER.info("BD替换请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuids"] = merchantuuids
    params["newDdInfoUuid"] = newddinfouuid
    params["oldDdInfoUuid"] = oldddinfouuid
    LOGGER.info("BD替换请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD替换请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid, bdstate):
    """
    BD状态修改
    :param bdstate: BD状态,string
    :param bdinfouuid: BDuuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3120')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/updateBdInfoState"
    LOGGER.info("BD状态修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdInfoUuid"] = bdinfouuid
    params["bdState"] = bdstate
    LOGGER.info("BD状态修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD状态修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_bdTj(bdstate, enddate, pagecurrent, pagesize, searchwhere, startdate):
    """
    BD统计-v1.4.0、v1.0.4
    :param enddate: 结束时间,string
    :param pagecurrent: 当前页,number
    :param bdstate: BD状态,string
    :param pagesize: 每页几条,number
    :param startdate: 开始时间,string
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3121')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/bdTj"
    LOGGER.info("BD统计-v1.4.0、v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdState"] = bdstate
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("BD统计-v1.4.0、v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD统计-v1.4.0、v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_findBdMerchantList(bdinfouuid):
    """
    查询BD对应商户
    :param bdinfouuid: BDuuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3122')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/findBdMerchantList"
    LOGGER.info("查询BD对应商户请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdInfoUuid"] = bdinfouuid
    LOGGER.info("查询BD对应商户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询BD对应商户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_queryBdInfoLog(bdinfouuid):
    """
    BD操作日志查询--v1.5.0
    :param bdinfouuid: uuid,BD列表查询到的bdInfoUuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3123')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/queryBdInfoLog"
    LOGGER.info("BD操作日志查询--v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdInfoUuid"] = bdinfouuid
    LOGGER.info("BD操作日志查询--v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD操作日志查询--v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_findRepaymentList(applyoptname, auditoptname, auditstate, contractnumber, lastpaydatebegintime, lastpaydateendtime, merchantname, overduestate, pagecurrent, pagesize, paystate, usermobile, username):
    """
    还款列表--v1.5.0（美佳v1.0.0）v1.0.4、v1.0.6
    :param usermobile: 手机号,string
    :param overduestate: 逾期状态,string
    :param contractnumber: 订单编号,string
    :param pagesize: 页面大小,number
    :param username: 借款人,string
    :param paystate: 还款状态,string
    :param pagecurrent: 当前页,number
    :param applyoptname: 提交人,string
    :param lastpaydatebegintime: 开始时间,string
    :param lastpaydateendtime: 结束时间,string
    :param merchantname: 商户名称,string
    :param auditstate: 审核状态,string
    :param auditoptname: 审核人,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3124')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findRepaymentList"
    LOGGER.info("还款列表--v1.5.0（美佳v1.0.0）v1.0.4、v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyOptName"] = applyoptname
    params["auditOptName"] = auditoptname
    params["auditState"] = auditstate
    params["contractNumber"] = contractnumber
    params["lastPayDateBeginTime"] = lastpaydatebegintime
    params["lastPayDateEndTime"] = lastpaydateendtime
    params["merchantName"] = merchantname
    params["overdueState"] = overduestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["payState"] = paystate
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("还款列表--v1.5.0（美佳v1.0.0）v1.0.4、v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款列表--v1.5.0（美佳v1.0.0）v1.0.4、v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_findRepaymentDetil(userbilluuid):
    """
    还款详情-v1.5.0
    :param userbilluuid: 用户账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3125')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findRepaymentDetil"
    LOGGER.info("还款详情-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("还款详情-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款详情-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_addRepayUnderLineApply(actualamt, actualrepaydate, picturelist, remarks, shouldrepayamt, userbilluuid):
    """
    手动还款（线下还款）-提交审核申请
    :param shouldrepayamt: 应还金额,string
    :param actualrepaydate: 实际还款时间,string
    :param remarks: 手动还款原因,string
    :param picturelist: 还款凭证 图片列表,array<object>
    :param userbilluuid: 账单Uuid,string
    :param actualamt: 实际还款金额,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3126')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/addRepayUnderLineApply"
    LOGGER.info("手动还款（线下还款）-提交审核申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["actualRepayDate"] = actualrepaydate
    params["pictureList"] = picturelist
    params["remarks"] = remarks
    params["shouldRepayAmt"] = shouldrepayamt
    params["userBillUuid"] = userbilluuid
    LOGGER.info("手动还款（线下还款）-提交审核申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动还款（线下还款）-提交审核申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_findRepayment(userbilluuid):
    """
    还款基本信息--v1.5.0(美佳v1.0.0)v1.0.6
    :param userbilluuid: 用户账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3127')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findRepayment"
    LOGGER.info("还款基本信息--v1.5.0(美佳v1.0.0)v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("还款基本信息--v1.5.0(美佳v1.0.0)v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款基本信息--v1.5.0(美佳v1.0.0)v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt, shouldrepayamt, userbilluuid):
    """
    手动代扣-提交申请
    :param actualamt: 实际还款金额,string
    :param userbilluuid: 账单Uuid,string
    :param shouldrepayamt: 应还金额,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3128')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/addRepayManualApply"
    LOGGER.info("手动代扣-提交申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["shouldRepayAmt"] = shouldrepayamt
    params["userBillUuid"] = userbilluuid
    LOGGER.info("手动代扣-提交申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动代扣-提交申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_findOneRepayBill(actualrepaydate, userbilluuid):
    """
    查询还款账单（手动还款和手动代扣弹窗页面顶部公用)---美佳v1.0.4
    :param actualrepaydate: 实际还款时间,string
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3129')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findOneRepayBill"
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)---美佳v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualRepayDate"] = actualrepaydate
    params["userBillUuid"] = userbilluuid
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)---美佳v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)---美佳v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_findManuelHistoryList(pagecurrent, pagesize, userbilluuid):
    """
    获取手动代扣历史记录
    :param pagesize: 页大小,number
    :param pagecurrent: 第几页,number
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3130')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findManuelHistoryList"
    LOGGER.info("获取手动代扣历史记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["userBillUuid"] = userbilluuid
    LOGGER.info("获取手动代扣历史记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手动代扣历史记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_auditRepayManualApply(auditstate, userbilluuid):
    """
    手动还款-审核
    :param userbilluuid: 账单Uuid,string
    :param auditstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3131')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/auditRepayManualApply"
    LOGGER.info("手动还款-审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["userBillUuid"] = userbilluuid
    LOGGER.info("手动还款-审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动还款-审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_downRepaymentList(applyoptname, auditoptname, auditstate, contractnumber, lastpaydatebegintime, lastpaydateendtime, overduestate, paystate, usermobile, username):
    """
    还款列表导出-v1.4.0v1.0.6
    :param auditstate: 审核状态,string
    :param lastpaydateendtime: 结束时间,string
    :param applyoptname: 提交人,string
    :param overduestate: 逾期状态,string
    :param contractnumber: 订单编号,string
    :param usermobile: 手机号,string
    :param lastpaydatebegintime: 开始时间,string
    :param paystate: 还款状态,string
    :param username: 借款人,string
    :param auditoptname: 审核人,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3132')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/downRepaymentList"
    LOGGER.info("还款列表导出-v1.4.0v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyOptName"] = applyoptname
    params["auditOptName"] = auditoptname
    params["auditState"] = auditstate
    params["contractNumber"] = contractnumber
    params["lastPayDateBeginTime"] = lastpaydatebegintime
    params["lastPayDateEndTime"] = lastpaydateendtime
    params["overdueState"] = overduestate
    params["payState"] = paystate
    params["userMobile"] = usermobile
    params["userName"] = username
    params["MyToken"] = LICENCES
    LOGGER.info("还款列表导出-v1.4.0v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款列表导出-v1.4.0v1.0.6请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_ap_repayment_advancePayment(paydate, remarks, urls, userbilluuid):
    """
    提前还清-v1.5.0
    :param userbilluuid: 账单uuid,string
    :param remarks: 还款备注,string
    :param paydate: 还款时间,string
    :param urls: 还款凭证key,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3133')
    requesturl = baseUrl + "/api/78dk/platform/ap/repayment/advancePayment"
    LOGGER.info("提前还清-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["payDate"] = paydate
    params["remarks"] = remarks
    params["urls"] = urls
    params["userBillUuid"] = userbilluuid
    LOGGER.info("提前还清-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还清-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_ap_repayment_findCalculate(uid):
    """
    提前还清试算-v1.5.0
    :param uid: 账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3134')
    requesturl = baseUrl + "/api/78dk/platform/ap/repayment/findCalculate"
    LOGGER.info("提前还清试算-v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("提前还清试算-v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还清试算-v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_ap_repayment_findRepaymentList(uid):
    """
    未结清列表--美佳v1.0.6
    :param uid: 账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3135')
    requesturl = baseUrl + "/api/78dk/platform/ap/repayment/findRepaymentList"
    LOGGER.info("未结清列表--美佳v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("未结清列表--美佳v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("未结清列表--美佳v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_deferredPayment(userbilluuid):
    """
    延期还款-v1.0.6
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3136')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/deferredPayment"
    LOGGER.info("延期还款-v1.0.6请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("延期还款-v1.0.6请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("延期还款-v1.0.6请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sa_updateSaState(sastate, sauuid):
    """
    SA修改在职离职状态
    :param sastate: SA状态,string
    :param sauuid: SAUUid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3137')
    requesturl = baseUrl + "/api/78dk/platform/sa/updateSaState"
    LOGGER.info("SA修改在职离职状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["saState"] = sastate
    params["saUuid"] = sauuid
    LOGGER.info("SA修改在职离职状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("SA修改在职离职状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sa_addSa(email, mobile, name):
    """
    SA新增
    :param name: 姓名,string
    :param mobile: 手机号,string
    :param email: 邮箱,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3138')
    requesturl = baseUrl + "/api/78dk/platform/sa/addSa"
    LOGGER.info("SA新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("SA新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("SA新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sa_querySaLog(sa_uuid):
    """
    SA操作日志
    :param sa_uuid: SAUUid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3139')
    requesturl = baseUrl + "/api/78dk/platform/sa/querySaLog"
    LOGGER.info("SA操作日志请求地址:【{}】".format(requesturl))
    params = dict()
    params["sa_uuid"] = sa_uuid
    LOGGER.info("SA操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("SA操作日志请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sa_querySaStatistics(enddate, pagecurrent, pagesize, sastate, searchwhere, startdate):
    """
    SA统计
    :param searchwhere: 查询条件,string
    :param sastate: SA状态,string
    :param pagesize: 每页几条,number
    :param startdate: 开始时间,string
    :param enddate: 结束时间,string
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3140')
    requesturl = baseUrl + "/api/78dk/platform/sa/querySaStatistics"
    LOGGER.info("SA统计请求地址:【{}】".format(requesturl))
    params = dict()
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["saState"] = sastate
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("SA统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("SA统计请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sa_querySaList(pagecurrent, pagesize, sastate, searchwhere):
    """
    SA列表
    :param pagesize: 每页几条,number
    :param pagecurrent: 当前页,number
    :param sastate: SA状态,string
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3141')
    requesturl = baseUrl + "/api/78dk/platform/sa/querySaList"
    LOGGER.info("SA列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["saState"] = sastate
    params["searchWhere"] = searchwhere
    LOGGER.info("SA列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("SA列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_file_download(filename, urlstr):
    """
    文件下载
    :param filename: 文件名称,string
    :param urlstr: 文件路径,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3142')
    requesturl = baseUrl + "/api/78dk/platform/file/download"
    LOGGER.info("文件下载请求地址:【{}】".format(requesturl))
    params = dict()
    params["filename"] = filename
    params["urlStr"] = urlstr
    params["MyToken"] = LICENCES
    LOGGER.info("文件下载请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文件下载请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_findQiniuToken(type):
    """
    获取七牛tocken
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3143')
    requesturl = baseUrl + "/api/78dk/platform/common/findQiniuToken"
    LOGGER.info("获取七牛tocken请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    LOGGER.info("获取七牛tocken请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛tocken请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_viewImageUrl(qiniukey, type):
    """
    获取图片url
    :param type: 类型,string
    :param qiniukey: 七牛key,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3144')
    requesturl = baseUrl + "/api/78dk/platform/common/viewImageUrl"
    LOGGER.info("获取图片url请求地址:【{}】".format(requesturl))
    params = dict()
    params["qiniuKey"] = qiniukey
    params["type"] = type
    LOGGER.info("获取图片url请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片url请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_findContactInfo(uid):
    """
    查询亲属联系人信息-美佳v1.0.0
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3145')
    requesturl = baseUrl + "/api/78dk/platform/common/findContactInfo"
    LOGGER.info("查询亲属联系人信息-美佳v1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询亲属联系人信息-美佳v1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询亲属联系人信息-美佳v1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_bm_viewUserBill(contractuuid, pagecurrent, pagesize):
    """
    个人账单--v1.5(美佳v1.0.6账单明细)
    :param pagesize: 页面大小(Y),number
    :param contractuuid: 订单uuid,string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3146')
    requesturl = baseUrl + "/api/78dk/bm/viewUserBill"
    LOGGER.info("个人账单--v1.5(美佳v1.0.6账单明细)请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("个人账单--v1.5(美佳v1.0.6账单明细)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("个人账单--v1.5(美佳v1.0.6账单明细)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_bm_viewBillList(contractnumber, merchantname, pagecurrent, pagesize, state, usermobile, username):
    """
    账单列表(美佳v1.0.6)
    :param username: 姓名,string
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param contractnumber: 订单编号,string
    :param merchantname: 商户,string
    :param usermobile: 手机号,string
    :param state: 还款状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3147')
    requesturl = baseUrl + "/api/78dk/bm/viewBillList"
    LOGGER.info("账单列表(美佳v1.0.6)请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["merchantName"] = merchantname
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["state"] = state
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("账单列表(美佳v1.0.6)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单列表(美佳v1.0.6)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_viewContract(uid):
    """
    合同信息
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3148')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewContract"
    LOGGER.info("合同信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("合同信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_downLoans(begindate, contractnumber, enddate, loanstate, merchantname, phone, username):
    """
    导出放款列表
    :param merchantname: 商户明朝,string
    :param loanstate: 放款类型,string
    :param phone: 电话号码,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param contractnumber: 合同编号,string
    :param username: 用户名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3149')
    requesturl = baseUrl + "/api/78dk/platform/lm/downLoans"
    LOGGER.info("导出放款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["loanState"] = loanstate
    params["merchantName"] = merchantname
    params["phone"] = phone
    params["userName"] = username
    params["MyToken"] = LICENCES
    LOGGER.info("导出放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出放款列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_offLineLoan(bankseqid, contractuuid, loanamount, remarks, url, urlname):
    """
    放款-v1.4.0
    :param contractuuid: 合同uuid（Y）,string
    :param url: 图片路径（Y）,string
    :param urlname: 图片名称（Y）,string
    :param bankseqid: 银行流水,string
    :param remarks: 备注（Y）,string
    :param loanamount: 放款金额（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3150')
    requesturl = baseUrl + "/api/78dk/platform/lm/offLineLoan"
    LOGGER.info("放款-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankSeqId"] = bankseqid
    params["contractUuid"] = contractuuid
    params["loanAmount"] = loanamount
    params["remarks"] = remarks
    params["url"] = url
    params["urlName"] = urlname
    LOGGER.info("放款-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款-v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_viewLoans(begindate, contractnumber, enddate, loanstate, merchantname, pagecurrent, pagesize, phone, username):
    """
    放款列表-v1.0.0(美佳v1.0.6)
    :param pagecurrent: 当前页（Y）,number
    :param begindate: 开始时间,string
    :param merchantname: 商户名称,string
    :param username: 用户名称,string
    :param pagesize: 页面大小（Y）,number
    :param contractnumber: 合同编号,string
    :param phone: 手机号,string
    :param enddate: 结束时间,string
    :param loanstate: 放款类型-v1.0.0,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3151')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewLoans"
    LOGGER.info("放款列表-v1.0.0(美佳v1.0.6)请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["loanState"] = loanstate
    params["merchantName"] = merchantname
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["userName"] = username
    LOGGER.info("放款列表-v1.0.0(美佳v1.0.6)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款列表-v1.0.0(美佳v1.0.6)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_viewUserBill(begindate, enddate, name, orderstate, pagecurrent, pagesize, state, uuid):
    """
    账单信息
    :param begindate: 开始时间,string
    :param pagecurrent: 当前页（Y）,number
    :param state: 状态 all为全部 pass为通过的 fail为没有通过的,string
    :param uuid: 合同uuid（Y）,string
    :param orderstate: 订单状态,string
    :param enddate: 结束时间,string
    :param pagesize: 页面大小（Y）,number
    :param name: 名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3152')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewUserBill"
    LOGGER.info("账单信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["state"] = state
    params["uuid"] = uuid
    LOGGER.info("账单信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_downPayMoneys(begindate, contractnumber, enddate, loanstate, merchantname, phone, username):
    """
    导出打款信息
    :param loanstate: 放款状态,string
    :param enddate: 结束时间,number
    :param begindate: 开始时间,string
    :param phone: 客户电话,string
    :param contractnumber: 合同编号,string
    :param username: 客户名称,string
    :param merchantname: 商户名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3153')
    requesturl = baseUrl + "/api/78dk/platform/lm/downPayMoneys"
    LOGGER.info("导出打款信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["contractNumber"] = contractnumber
    params["enddate"] = enddate
    params["loanState"] = loanstate
    params["merchantName"] = merchantname
    params["phone"] = phone
    params["userName"] = username
    params["MyToken"] = LICENCES
    LOGGER.info("导出打款信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出打款信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_viewLoanDetil(uid):
    """
    查看放款详情-v1.5..0(美佳v1.0.6)
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3154')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewLoanDetil"
    LOGGER.info("查看放款详情-v1.5..0(美佳v1.0.6)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查看放款详情-v1.5..0(美佳v1.0.6)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看放款详情-v1.5..0(美佳v1.0.6)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_loandownLimit(contractuuid):
    """
    查询订单放款限制--美佳v1.0.4
    :param contractuuid: 订单uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3155')
    requesturl = baseUrl + "/api/78dk/platform/lm/loandownLimit"
    LOGGER.info("查询订单放款限制--美佳v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询订单放款限制--美佳v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询订单放款限制--美佳v1.0.4请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_addMessage(communicatee, condition, datalist, overduereason, remark, replyrepaytime, useruuid):
    """
    电话催收信息提交-v1.5.2
    :param condition: 沟通情况,string
    :param useruuid: 客户UUID,string
    :param communicatee: 沟通对象,string
    :param remark: 备注,string
    :param replyrepaytime: 承诺还款时间,string
    :param overduereason: 逾期原因,string
    :param datalist: 文件,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3156')
    requesturl = baseUrl + "/api/78dk/platform/urge/addMessage"
    LOGGER.info("电话催收信息提交-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["communicatee"] = communicatee
    params["condition"] = condition
    params["dataList"] = datalist
    params["overdueReason"] = overduereason
    params["remark"] = remark
    params["replyRepayTime"] = replyrepaytime
    params["userUuid"] = useruuid
    LOGGER.info("电话催收信息提交-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电话催收信息提交-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryFile(urgeuuid):
    """
    通话记录文件下载-v1.5.2(已经作废，包含在电话催收历史记录接口中了)
    :param urgeuuid: 催收UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3157')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryFile"
    LOGGER.info("通话记录文件下载-v1.5.2(已经作废，包含在电话催收历史记录接口中了)请求地址:【{}】".format(requesturl))
    params = dict()
    params["urgeUuid"] = urgeuuid
    LOGGER.info("通话记录文件下载-v1.5.2(已经作废，包含在电话催收历史记录接口中了)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通话记录文件下载-v1.5.2(已经作废，包含在电话催收历史记录接口中了)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryHistory(pagecurrent, pagesize, useruuid):
    """
    电话催收历史记录-v1.5.2
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param useruuid: 客户UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3158')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryHistory"
    LOGGER.info("电话催收历史记录-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["userUuid"] = useruuid
    LOGGER.info("电话催收历史记录-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电话催收历史记录-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryContactsOverdueLoan(uid):
    """
    联系人逾期贷款信息-v1.5.2(美佳1.0.0)
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3159')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryContactsOverdueLoan"
    LOGGER.info("联系人逾期贷款信息-v1.5.2(美佳1.0.0)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("联系人逾期贷款信息-v1.5.2(美佳1.0.0)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("联系人逾期贷款信息-v1.5.2(美佳1.0.0)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryOverdueLoan(uid):
    """
    逾期贷款信息-v1.5.2(美佳v1.0.0)
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3160')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryOverdueLoan"
    LOGGER.info("逾期贷款信息-v1.5.2(美佳v1.0.0)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("逾期贷款信息-v1.5.2(美佳v1.0.0)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期贷款信息-v1.5.2(美佳v1.0.0)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryUserInfo(uid):
    """
    客户信息-v1.5.2美佳1.0.0修改
    :param uid: 合同uuid,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3161')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryUserInfo"
    LOGGER.info("客户信息-v1.5.2美佳1.0.0修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("客户信息-v1.5.2美佳1.0.0修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客户信息-v1.5.2美佳1.0.0修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_prompt_urge_overdue_user(currentpage, currenturge, idcard, loandatebegin, loandateend, merchantname, mobile, name, overduedaybegin, overduedayend, overduestage, pagesize, repaymentdatebegin, repaymentdateend, totalpage, urgeuuid):
    """
    逾期用户列表v1.5.2(美佳v1.0.0)
    :param urgeuuid: 催收uuid,string
    :param name: 客户姓名,string
    :param merchantname: 商户名称,string
    :param repaymentdateend: 还款日期结束,string
    :param currentpage: 当前页,number
    :param currenturge: 催收员是否是 当前用户,string
    :param loandatebegin: 贷款日期开始,string
    :param overduedayend: 逾期天数结束,string
    :param totalpage: 总页数,number
    :param repaymentdatebegin: 还款日期开始,string
    :param overduedaybegin: 逾期天数开始,string
    :param loandateend: 贷款日期结束,string
    :param pagesize: 每页几条,number
    :param idcard: 身份证号,string
    :param mobile: 手机号,string
    :param overduestage: 逾期阶段,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3162')
    requesturl = baseUrl + "/api/78dk/platform/prompt/urge/overdue/user"
    LOGGER.info("逾期用户列表v1.5.2(美佳v1.0.0)请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["currentUrge"] = currenturge
    params["idCard"] = idcard
    params["loanDateBegin"] = loandatebegin
    params["loanDateEnd"] = loandateend
    params["merchantName"] = merchantname
    params["mobile"] = mobile
    params["name"] = name
    params["overdueDayBegin"] = overduedaybegin
    params["overdueDayEnd"] = overduedayend
    params["overdueStage"] = overduestage
    params["pageSize"] = pagesize
    params["repaymentDateBegin"] = repaymentdatebegin
    params["repaymentDateEnd"] = repaymentdateend
    params["totalPage"] = totalpage
    params["urgeUuid"] = urgeuuid
    LOGGER.info("逾期用户列表v1.5.2(美佳v1.0.0)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期用户列表v1.5.2(美佳v1.0.0)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_prompt_urge_data_export(useruuids):
    """
    逾期用户列表导出v1.5.2
    :param useruuids: 客户uuid（数组）,array<string>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3163')
    requesturl = baseUrl + "/api/78dk/platform/prompt/urge/data/export"
    LOGGER.info("逾期用户列表导出v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuids"] = useruuids
    LOGGER.info("逾期用户列表导出v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期用户列表导出v1.5.2请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_user_viewSystemMembers():
    """
    查询可添加为催收人员的员工_v1.5.2
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3164')
    requesturl = baseUrl + "/api/78dk/platform/urge/user/viewSystemMembers"
    LOGGER.info("查询可添加为催收人员的员工_v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询可添加为催收人员的员工_v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询可添加为催收人员的员工_v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_user_addMemberUser(useruuid):
    """
    添加一个催收人员_v1.5.2
    :param useruuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3165')
    requesturl = baseUrl + "/api/78dk/platform/urge/user/addMemberUser"
    LOGGER.info("添加一个催收人员_v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuid"] = useruuid
    LOGGER.info("添加一个催收人员_v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加一个催收人员_v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_user_collectionPersonnelList(divisionstate, email, mobile, name, pagecurrent, pagesize):
    """
    催收人员管理列表-搜索-v1.5.2
    :param divisionstate: 分案状态,string
    :param pagecurrent: 当前页,number
    :param pagesize: 每页几条,number
    :param email: 员工邮箱（备用）,string
    :param name: 员工姓名,string
    :param mobile: 员工手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3166')
    requesturl = baseUrl + "/api/78dk/platform/urge/user/collectionPersonnelList"
    LOGGER.info("催收人员管理列表-搜索-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["divisionState"] = divisionstate
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("催收人员管理列表-搜索-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("催收人员管理列表-搜索-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_user_updateDivisionState(collectionuuid, divisionstate):
    """
    开始分案停止分案操作-v1.5.2
    :param divisionstate: 分案状态,string
    :param collectionuuid: 催收人员uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3167')
    requesturl = baseUrl + "/api/78dk/platform/urge/user/updateDivisionState"
    LOGGER.info("开始分案停止分案操作-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["collectionUuid"] = collectionuuid
    params["divisionState"] = divisionstate
    LOGGER.info("开始分案停止分案操作-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("开始分案停止分案操作-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_prompt_urge_manual_allocation(urgeuuid, useruuids):
    """
    手动分案v1.5.2
    :param urgeuuid: 催收员uuid,string
    :param useruuids: 客户uuid,array<string>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3168')
    requesturl = baseUrl + "/api/78dk/platform/prompt/urge/manual/allocation"
    LOGGER.info("手动分案v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["urgeUuid"] = urgeuuid
    params["userUuids"] = useruuids
    LOGGER.info("手动分案v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动分案v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_user_findReceivingAddress(uid):
    """
    查询京东淘宝收货地址(美佳v1.0.0)
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3169')
    requesturl = baseUrl + "/api/78dk/platform/urge/user/findReceivingAddress"
    LOGGER.info("查询京东淘宝收货地址(美佳v1.0.0)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询京东淘宝收货地址(美佳v1.0.0)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询京东淘宝收货地址(美佳v1.0.0)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_viewUserAuthByContractId(contractuuid, type):
    """
    用户报告信息（运营商）
    :param type: 报告类型,number
    :param contractuuid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3170')
    requesturl = baseUrl + "/api/78dk/platform/common/viewUserAuthByContractId"
    LOGGER.info("用户报告信息（运营商）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["type"] = type
    LOGGER.info("用户报告信息（运营商）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户报告信息（运营商）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_common_queryCallDetailsList(contractuuid, pagecurrent, pagesize):
    """
    通话详单分页列表（美佳1.0.2）
    :param pagecurrent: 当前页(Y),number
    :param contractuuid: 订单id(Y),number
    :param pagesize: 每页条数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3171')
    requesturl = baseUrl + "/api/78dk/platform/common/queryCallDetailsList"
    LOGGER.info("通话详单分页列表（美佳1.0.2）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("通话详单分页列表（美佳1.0.2）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通话详单分页列表（美佳1.0.2）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2():
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3172')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


