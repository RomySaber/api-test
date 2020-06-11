#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Xqkj_web_finance_consumptionAction.py
@desc       : 项目：xqkj 模块：xqkj_web_finance_consumption 接口方法封装
"""

from xqkj.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('xqkj_web_finance_consumption_apiURL', 'xqkj')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_xqkj_web_finance_consumption_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_platform_cm_base_viewChannel(uid):
    """
    查询渠道
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 819')
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
    :param region: 所属大区(Y),number
    :param shortname: 渠道简称(Y),string
    :param province: 渠道所属省份(Y),number
    :param parentchanneluuid: 父级uuid(N)不填则该渠道为根渠道,string
    :param city: 渠道所属城市 (Y),number
    :param name: 渠道名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 820')
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
    :param channeluuid: 渠道 uuid(Y),string
    :param province: 渠道所属省份 (Y),number
    :param shortname: 渠道简称 (Y),string
    :param city: 渠道所属城市(Y),number
    :param note: 备注 (N),string
    :param name: 渠道名称(Y),string
    :param operatoruuid: 操作员(N),string
    :param region: 所属大区(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 821')
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
    :param message: 审核人填写信息(N),string
    :param isadopt: 是否通过(Y),boolean
    :param uid: 审核的渠道id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 822')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 823')
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
    :param updatestate: 冻结状态,string
    :param uid: 渠道id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 824')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 825')
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
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param name: 渠道名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 826')
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
    :param freezestate: 冻结状态,string
    :param pagecurrent: 当前页(Y),number
    :param auditstate: 审核状态,string
    :param openclosestate: 冻结状态,string
    :param name: 渠道名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 827')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 828')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 829')
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
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param documentcity: 证件市id,number
    :param businessaddress: 实际经营地址(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businesscityname: 实际经营市名称,string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param documentprovince: 证件省id,number
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param businessprovince: 实际经营省id,number
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businessinformationuuid: 业务信息 uuid(N),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param businessregion: 实际经营区id,number
    :param businesscity: 实际经营市id,number
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param documentprovincename: 证件省名称,string
    :param documentaddress: 证件地址(Y),string
    :param businessregionname: 实际经营区名称,string
    :param documentcityname: 证件市名称,string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param documentregion: 证件区id,number
    :param documentregionname: 证件区名称,string
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param businessprovincename: 实际经营省名称,string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 830')
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
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param documentcity: 证件市id,number
    :param documentregionname: 证件区名称,string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param businesscity: 实际经营市id,number
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param documentregion: 证件区id,number
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param documentprovincename: 证件省名称,string
    :param documentcityname: 证件市名称,string
    :param businessregionname: 实际经营区名称,string
    :param documentaddress: 证件地址(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businessregion: 实际经营区id,number
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param businessprovincename: 实际经营省名称,string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param businessprovince: 实际经营省id,number
    :param businesscityname: 实际经营市名称,string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businessinformationuuid: 业务信息 uuid(Y),string
    :param documentprovince: 证件省id,number
    :param businessaddress: 实际经营地址(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 831')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 832')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 833')
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
    :param title: 职务(Y),string
    :param mail: 邮箱(Y),string
    :param password: 密码(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid（Y）,string
    :param mobile: 手机(Y),string
    :param name: 姓名(Y),string
    :param salt: 盐(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 834')
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
    :param salt: 盐(N),string
    :param title: 职务(Y),string
    :param mobile: 手机(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param mail: 邮箱(Y),string
    :param password: 密码(Y),string
    :param operatoruuid: 操作员uuid(Y),string
    :param name: 姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 835')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 836')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 837')
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
    :param branchname: 支行名称(Y),string
    :param accountname: 账户名称(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param region: 开户行地址-区(Y),number
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param phone: 电话号码(Y),string
    :param accounttype: 账户类型(Y),string
    :param accountnumber: 结算账号(Y),string
    :param city: 开户行地址-市(Y),number
    :param channelormerchantuuid: 渠道或者商户(Y),string
    :param linenumber: 联行行号(Y),string
    :param province: 开户行地址-省(Y),number
    :param chamberlainidcard: 收款人身份证号(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 838')
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
    :param accountopeningbank: 开户银行(Y),string
    :param city: 开户行地址-市(Y),number
    :param phone: 电话号码(Y),string
    :param region: 开户行地址-区(Y),number
    :param chamberlainidcard: 收款人身份证号(N),string
    :param accountnumber: 结算账号(Y),string
    :param accountname: 账户名称(Y),string
    :param province: 开户行地址-省(Y),number
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param linenumber: 联行行号(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param accounttype: 账户类型(Y),string
    :param branchname: 支行名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 839')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 840')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 841')
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
    添加渠道法人代表-v1.4.0
    :param city: 渠道所属城市编号,number
    :param mobile: 手机号码(Y),string
    :param legalpersonuuid: 法人代表uuid(N),string
    :param name: 法人代表姓名(Y),string
    :param region: 所属大区编号 ,,number
    :param cardnumber: 证件号码(Y),string
    :param province: 渠道所属省份编号,number
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 842')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
    LOGGER.info("添加渠道法人代表-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["city"] = city
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    params["province"] = province
    params["region"] = region
    LOGGER.info("添加渠道法人代表-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道法人代表-v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, city, legalpersonuuid, mobile, name, province, region):
    """
    编辑渠道法人代表-v1.4.0
    :param legalpersonuuid: 法人代表uuid(Y),string
    :param cardnumber: 证件号码(Y),string
    :param province: 渠道所属省份编号,number
    :param city: 渠道所属城市编号,number
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param name: 法人代表姓名(Y),string
    :param mobile: 手机号码(Y),string
    :param region: 所属大区编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 843')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 844')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 845')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 846')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 847')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 848')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 849')
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
    :param state: 资方状态(Y),string
    :param fundsideuuid: 资方uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 850')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 851')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 852')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 853')
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
    :param fundsideuuid: 资方uuid(Y),number
    :param state: 数据状态(Y),string
    :param name: 资金包名称(Y),string
    :param amount: 总额度(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 854')
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
    :param name: 资金包名称(Y),string
    :param fundpackageuuid: 资金包uuid(Y),string
    :param state: 数据状态(Y),string
    :param amount: 总额度(Y),number
    :param fundsideuuid: 资方uuid,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 855')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 856')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 857')
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
    查询产品模版
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 858')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetail"
    LOGGER.info("查询产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_saveProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    添加产品模版
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param minquota: 单笔额度下限（Y）,string
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param discountrate: 商户最大贴息费率（Y）,string
    :param productstate: 产品状态（Y）,string
    :param maxquota: 单笔额度上限（Y）,string
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param name: 产品名称（Y）,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param remark: 产品备注,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param repaymentdatetype: 还款日类型（Y）,string
    :param fundpackageuuid: 资金包uuid,string
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param loanmode: 放款方式,string
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param repaymentmethod: 还款方式（Y）,string
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 859')
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
    LOGGER.info("添加产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountRate"] = discountrate
    params["earlyRepaymentFreeCycle"] = earlyrepaymentfreecycle
    params["earlyRepaymentHandlingFee"] = earlyrepaymenthandlingfee
    params["earlyRepaymentSupport"] = earlyrepaymentsupport
    params["electronicContractTemplateUuid"] = electroniccontracttemplateuuid
    params["firstHalfOfTheMonth"] = firsthalfofthemonth
    params["fundPackageUuid"] = fundpackageuuid
    params["incomingPartsTemplateUuid"] = incomingpartstemplateuuid
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
    LOGGER.info("添加产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_updateProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productdetailuuid, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    编辑产品模版
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :param minquota: 单笔额度下限（Y）,string
    :param loanmode: 放款方式,string
    :param remark: 产品备注,string
    :param productdetailuuid: 产品UUID,string
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param maxquota: 单笔额度上限（Y）,string
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param name: 产品名称（Y）,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param repaymentdatetype: 还款日类型（Y）,string
    :param discountrate: 商户最大贴息费率（Y）,string
    :param productstate: 产品状态（Y）,string
    :param fundpackageuuid: 资金包uuid,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param repaymentmethod: 还款方式（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 860')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
    LOGGER.info("编辑产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountRate"] = discountrate
    params["earlyRepaymentFreeCycle"] = earlyrepaymentfreecycle
    params["earlyRepaymentHandlingFee"] = earlyrepaymenthandlingfee
    params["earlyRepaymentSupport"] = earlyrepaymentsupport
    params["electronicContractTemplateUuid"] = electroniccontracttemplateuuid
    params["firstHalfOfTheMonth"] = firsthalfofthemonth
    params["fundPackageUuid"] = fundpackageuuid
    params["incomingPartsTemplateUuid"] = incomingpartstemplateuuid
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
    LOGGER.info("编辑产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_base_viewProductDetails(name, pagecurrent, pagesize):
    """
    产品列表
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param name: 名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 861')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 862')
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
    :param name: 资金包名称,string
    :param pagecurrent: 当前页,number
    :param pagesize: 每页显示条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 863')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 864')
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


def test_api_78dk_platform_product_pmm_bindProductMerchant(merchantuuids, productuuid):
    """
    绑定产品和商户关系
    :param merchantuuids: 商户uuid(Y),string
    :param productuuid: 商户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 865')
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
    :param rate: 月利率,string
    :param period: 分期数,string
    :param discountrate: 商户贴息率,string
    :param merchantuuid: 商户uuid,string
    :param productdetailconfiguuid: 产品分期uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 866')
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
    :param merchantuuid: 商户uuid,string
    :param productuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 867')
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
    :param uuid: 产品uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 868')
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
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :param uuid: 产品uuid(Y),string
    :param name: 名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 869')
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
    :param merchantuuids: 商户uuid,string
    :param productuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 870')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 871')
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


def test_api_78dk_platform_mm_base_updateMerchant(channeluuid, city, industryfirst, industrysecond, merchantuuid, name, note, parentmerchantuuid, province, shortname):
    """
    基本信息-修改-v1.4
    :param channeluuid: 渠道Uuid,string
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param merchantuuid: 商户Uuid(Y),string
    :param shortname: 商户简称(Y),string
    :param note: 商户描述/备注(N),string
    :param industrysecond: 二级分类id,number
    :param province: 省id,number
    :param city: 市id,number
    :param name: 商户名称(Y),string
    :param industryfirst: 一级分类id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 872')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
    LOGGER.info("基本信息-修改-v1.4请求地址:【{}】".format(requesturl))
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
    params["shortName"] = shortname
    LOGGER.info("基本信息-修改-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-修改-v1.4请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 873')
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


def test_api_78dk_platform_mm_base_saveMerchant(channeluuid, city, industryfirst, industrysecond, name, note, parentmerchantuuid, province, shortname):
    """
    基本信息-新增-v1.4
    :param industryfirst: 一级分类id(Y),number
    :param shortname: 商户简称(Y),string
    :param city: 市id(Y),number
    :param name: 商户名称(Y),string
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param note: 商户描述/备注(N),string
    :param channeluuid: 渠道Uuid,string
    :param industrysecond: 二级分类id,number
    :param province: 省id(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 874')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
    LOGGER.info("基本信息-新增-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["city"] = city
    params["industryFirst"] = industryfirst
    params["industrySecond"] = industrysecond
    params["name"] = name
    params["note"] = note
    params["parentMerchantUuid"] = parentmerchantuuid
    params["province"] = province
    params["shortName"] = shortname
    LOGGER.info("基本信息-新增-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-新增-v1.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewMerchant(uid):
    """
    基本信息-查询-v1.4
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 875')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
    LOGGER.info("基本信息-查询-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("基本信息-查询-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息-查询-v1.4请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 877')
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
    :param updatestate: 修改状态(Y),string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 878')
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


def test_api_78dk_platform_mm_examine_merchanrExamine(message, type, uid):
    """
    商户审核-v1.5.1
    :param type: imperfect 打回 pass 通过 fail 失败,pending_review提交审核,string
    :param message: 审核信息,string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 879')
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


def test_api_78dk_platform_mm_examine_viewExamineMerchantList(name, pagecurrent, pagesize):
    """
    查询商户审核列表
    :param pagesize: 分页大小(Y),number
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 880')
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
    :param name: 商户名称(N),string
    :param pagesize: 分页大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 881')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 882')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 883')
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


def test_api_78dk_platform_mm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, contracttimebegin, contracttimeend, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, installmentcooperationorgs, merge, organizationcode, socialunifiedcreditcode, specialindustrylicenseorname, specialindustrytimebegin, specialindustrytimeend, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    修改机构信息-v1.4
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param contracttimeend: 合同结束时间,string
    :param documentcityname: 证件市名称,string
    :param specialindustrytimeend: 特殊行业许可证有效期结束时间,string
    :param documentaddress: 证件地址(Y),string
    :param businessregionname: 实际经营区名称,string
    :param socialunifiedcreditcode: 社会统一征信代码-三证合一后(Y),string
    :param businessinformationuuid: 业务信息 UUID(Y),string
    :param businesscity: 实际经营市id,number
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param businesscityname: 实际经营市名称,string
    :param businessprovince: 实际经营省id,number
    :param businessregion: 实际经营区id,number
    :param merge: 是否三证合一,string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param documentcity: 证件市id,number
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param installmentcooperationorgs: 现有分期合作机构,array<object>
    :param documentprovincename: 证件省名称,string
    :param documentregionname: 证件区名称,string
    :param contracttimebegin: 合同开始时间,string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param documentprovince: 证件省id,number
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param businessprovincename: 实际经营省名称,string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businessaddress: 实际经营地址(Y),string
    :param specialindustrytimebegin: 特殊行业许可证有效期开始时间,string
    :param specialindustrylicenseorname: 特殊行业许可证或证明名称：,string
    :param documentregion: 证件区id,number
    :param channelormerchantuuid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 884')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 885')
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
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param specialindustrylicenseorname: 特殊行业许可证或者名称,string
    :param contracttimeend: 合同结束时间,number
    :param merge: 是否三证合一,string
    :param specialindustrytimeend: 特殊行业许可证有效期结束时间,string
    :param installmentcooperationorgs: 现有分期合作机构,array<object>
    :param organizationcode: 组织结构代码-,string
    :param taxregistrationnumber: 税务登记号,string
    :param socialunifiedcreditcode: 社会统一征信代码,string
    :param specialindustrytimebegin: 特殊行业许可证有效期开始时间,number
    :param contracttimebegin: 合同开始时间,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 886')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 887')
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
    :param name: 法人代表姓名(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param legalpersonuuid: 法人uuid,string
    :param effectivetimeend: 身份证有效时间结束,string
    :param mobile: 手机号码(Y),string
    :param effectivetimebegin: 身份证有效时间开始,string
    :param cardnumber: 证件号码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 888')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 889')
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
    :param cardnumber: 证件号码(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param legalpersonuuid: 法人代表Uuid(N),string
    :param name: 法人代表姓名(Y),string
    :param effectivetimeend: 身份证有效时间结束,string
    :param effectivetimebegin: 身份证有效时间开始,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 890')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 891')
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
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param linenumber: 联行行号(Y),string
    :param province: 省(Y),number
    :param clearingaccountuuid: 商户结算Uuid(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accounttype: 账户类型(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param accountname: 开户人名称(Y),string
    :param region: 区/县(Y),number
    :param branchname: 支行名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param city: 市(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 892')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 893')
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
    :param accounttype: 账户类型(Y),string
    :param clearingaccountuuid: 商户结算Uuid(N),string
    :param accountname: 开户人名称,string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param linenumber: 联行行号(Y),string
    :param region: 区/县(Y),number
    :param accountnumber: 结算账号(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param branchname: 支行名称(Y),string
    :param city: 市(Y),number
    :param province: 省(Y),number
    :param accountopeningbank: 开户银行(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 894')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 895')
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
    :param regionname: 区名称,string
    :param email: 业务邮箱,string
    :param storeuuid: 门店Uuid(Y),string
    :param leasetimebegin: 租赁开始时间,string
    :param leasetimeend: 租赁结束时间,string
    :param merchantuuid: 商户Uuid(Y),string
    :param managername: 门店负责人姓名(Y),string
    :param managerphone: 门店负责人电话(Y),string
    :param city: 市id,number
    :param businessaddress: 实际经营地址(Y),string
    :param region: 区id,number
    :param numberenddate: 身份证有效期结束时间,string
    :param area: 门店租赁面积（平方）,number
    :param numberbegindate: 身份证有效期开始时间,string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param idcardnumber: 身份证号码,string
    :param province: 省id,number
    :param employeesnum: 员工总数,number
    :param cityname: 市名称,string
    :param provincename: 省名称,string
    :param storename: 门店名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 896')
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


def test_api_78dk_platform_mm_base_store_deleteStore(uid):
    """
    删除门店信息
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 897')
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


def test_api_78dk_platform_mm_base_store_saveStore(area, businessaddress, businessaddressgpsloction, city, cityname, email, employeesnum, idcardnumber, leasetimebegin, leasetimeend, managername, managerphone, merchantuuid, numberbegindate, numberenddate, province, provincename, region, regionname, storename, storeuuid):
    """
    新增门店信息-v1.4
    :param region: 区id,number
    :param regionname: 区名称,string
    :param merchantuuid: 商户Uuid(Y),string
    :param city: 市id,number
    :param cityname: 市名称,string
    :param numberbegindate: 身份证有效期开始时间,string
    :param storename: 门店名称,string
    :param leasetimeend: 租赁结束时间,string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param idcardnumber: 身份证号码,string
    :param numberenddate: 身份证有效期结束时间,string
    :param employeesnum: 员工总数,number
    :param managerphone: 门店负责人电话(Y),string
    :param storeuuid: 门店Uuid(N),string
    :param email: 业务邮箱,string
    :param leasetimebegin: 租赁开始时间,string
    :param area: 门店租赁面积（平方),number
    :param managername: 门店负责人姓名(Y),string
    :param provincename: 省名称,string
    :param businessaddress: 实际经营地址(Y)详细地址,string
    :param province: 省id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 898')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
    LOGGER.info("新增门店信息-v1.4请求地址:【{}】".format(requesturl))
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
    LOGGER.info("新增门店信息-v1.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增门店信息-v1.4请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 899')
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


def test_api_78dk_platform_mm_base_store_uploadQrcode(storeuuid):
    """
    下载门店二维码
    :param storeuuid: 门店uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 901')
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


def test_api_78dk_platform_mm_money_merchantMoneyEnlarge(uid, zoomcoefficient):
    """
    修改预授信放大系数
    :param zoomcoefficient: 预授信额度放大系数(Y),number
    :param uid: 商户额度Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 902')
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


def test_api_78dk_platform_mm_money_updateMerchantMoney(amountday, amountmonth, amountsingle, amountsum, depositnotice, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    修改额度管理-v1.5
    :param merchantuuid: 商户Uuid(Y),string
    :param amountsum: 总额度(Y),number
    :param zoomcoefficient: 预授信额度放大系数(N),number
    :param amountday: 总额度-日(Y),number
    :param amountmonth: 总额度-月(Y),number
    :param moneyconfiguuid: 商户额度Uuid(Y),string
    :param amountsingle: 单笔总额度-日(Y),number
    :param depositnotice: 保证金提示额度,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 903')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
    LOGGER.info("修改额度管理-v1.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["depositNotice"] = depositnotice
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("修改额度管理-v1.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改额度管理-v1.5请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 904')
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


def test_api_78dk_platform_mm_money_saveMerchantMoney(amountday, amountmonth, amountsingle, amountsum, depositnotice, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    新增额度管理-v1.5
    :param amountday: 总额度-日(Y),number
    :param amountsum: 总额度(Y),number
    :param amountsingle: 总额度-单笔(Y),number
    :param amountmonth: 总额度-月(Y),number
    :param merchantuuid: 商户Uuid(Y),string
    :param moneyconfiguuid: 商户额度Uuid(N),string
    :param zoomcoefficient: 预授信额度放大系数(N),number
    :param depositnotice: 保证金缴纳提示(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 905')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
    LOGGER.info("新增额度管理-v1.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["depositNotice"] = depositnotice
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("新增额度管理-v1.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增额度管理-v1.5请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 906')
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
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :param name: 商户名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 907')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 908')
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
    :param provincename: 省名称,string
    :param city: 市id,number
    :param created: 创建时间,string
    :param updated: 更新时间,string
    :param province: 省id,number
    :param cityname: 市名称,string
    :param merchantuuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 909')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 910')
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


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(platformprivilegeuuid, platformuseruuid):
    """
    新增/修改权限
    :param platformprivilegeuuid: 权限UUid(Y),string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 911')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 912')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 913')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 914')
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
    :param platformprivilegeuuid: 菜单uuid（N）,string
    :param url: 菜单路径（Y）,string
    :param name: 菜单名称（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 915')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 916')
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
    :param name: 用户姓名(Y),string
    :param email: 用户邮箱(Y),string
    :param platformuserprofileuuid: 用户Uuid(Y),string
    :param mobile: 用户手机(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 917')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 918')
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
    :param email: 用户邮箱(Y),string
    :param name: 用户姓名(Y),string
    :param mobile: 用户手机(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 919')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 920')
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
    :param password: 用户密码(Y),string
    :param email: 用户帐户(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 921')
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
    :param pagesize: 分页大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 922')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 923')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 924')
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
    :param password: 用户密码(Y),string
    :param email: 用户邮箱(Y),string
    :param passwordrepeat: 用户密码重复(N),string
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 925')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 926')
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


def test_api_78dk_platform_tm_first_firstCheck(checkstate, message, uuid):
    """
    初审
    :param uuid: 合同uuid,string
    :param message: 审核人提交信息,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 927')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/firstCheck"
    LOGGER.info("初审请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["message"] = message
    params["uuid"] = uuid
    LOGGER.info("初审请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContract(uid):
    """
    初审信息查询-v1.5.1
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 928')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
    LOGGER.info("初审信息查询-v1.5.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("初审信息查询-v1.5.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审信息查询-v1.5.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContracts(begindate, contractnumber, enddate, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    初审列表查询
    :param lable: 标签,string
    :param name: 编号等一系列东西,string
    :param contractnumber: 合同编号,string
    :param pagecurrent: 当前页,number
    :param username: 用户名,string
    :param begindate: 开始时间,string
    :param state: 状态,string
    :param phone: 电话号码,string
    :param enddate: 结束时间,string
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 929')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
    LOGGER.info("初审列表查询请求地址:【{}】".format(requesturl))
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
    LOGGER.info("初审列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审列表查询请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 930')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 931')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 932')
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


def test_api_78dk_platform_tm_first_viewBaiDuInfo(uid):
    """
    查询百度接口(废)
    :param uid: 百度uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 933')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewBaiDuInfo"
    LOGGER.info("查询百度接口(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询百度接口(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询百度接口(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_saveSupplementImage(auditchecktype, backgroundsupplementimages, contractuuid, supplementimagetype):
    """
    提交或编辑补录资料(废)
    :param supplementimagetype: 后台编辑或提交类型,string
    :param auditchecktype: 审核类型,string
    :param backgroundsupplementimages: 补录资料实体,array<object>
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 934')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveSupplementImage"
    LOGGER.info("提交或编辑补录资料(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["backGroundSupplementImages"] = backgroundsupplementimages
    params["contractUuid"] = contractuuid
    params["supplementImageType"] = supplementimagetype
    LOGGER.info("提交或编辑补录资料(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交或编辑补录资料(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_getSupplementImages(uid):
    """
    查询用户能补录的图片资料(废)
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 935')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getSupplementImages"
    LOGGER.info("查询用户能补录的图片资料(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询用户能补录的图片资料(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户能补录的图片资料(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_passContract(auditchecktype, audituuid, contractuuid, description, supplementimagerequires):
    """
    打回初审的合同(现在支持电核和终审)(废)
    :param supplementimagerequires: 补录资料要求实体,array<object>
    :param contractuuid: 合同UUID,string
    :param auditchecktype: 审核类型,string
    :param description: 补录说明,string
    :param audituuid: 审核员UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 936')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/passContract"
    LOGGER.info("打回初审的合同(现在支持电核和终审)(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["auditUuid"] = audituuid
    params["contractUuid"] = contractuuid
    params["description"] = description
    params["supplementImageRequires"] = supplementimagerequires
    LOGGER.info("打回初审的合同(现在支持电核和终审)(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("打回初审的合同(现在支持电核和终审)(废)请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 937')
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


def test_api_78dk_platform_tm_first_findAuditCommentList(contractuuid, pagecurrent, pagesize):
    """
    查询评论列表
    :param contractuuid: 合同 UUID,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 938')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findAuditCommentList"
    LOGGER.info("查询评论列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询评论列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询评论列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_addAuditComment(auditcommentattachments, comment, contractuuid, replyauditcommentuuid):
    """
    添加一条评论
    :param contractuuid: 合同 UUID（Y）,string
    :param comment: 评论内容（Y）,string
    :param replyauditcommentuuid: 回复评论的UUID,string
    :param auditcommentattachments: 附件集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 939')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addAuditComment"
    LOGGER.info("添加一条评论请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCommentAttachments"] = auditcommentattachments
    params["comment"] = comment
    params["contractUuid"] = contractuuid
    params["replyAuditCommentUuid"] = replyauditcommentuuid
    LOGGER.info("添加一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_editAuditComment(auditcommentattachments, auditcommentuuid, comment, contractuuid, replyauditcommentuuid):
    """
    编辑一条评论
    :param contractuuid: 合同 UUID（Y）,string
    :param replyauditcommentuuid: 回复评论的UUID,string
    :param auditcommentuuid: 评论UUID （Y）,string
    :param comment: 评论内容（Y）,string
    :param auditcommentattachments: 附件集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 940')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/editAuditComment"
    LOGGER.info("编辑一条评论请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCommentAttachments"] = auditcommentattachments
    params["auditCommentUuid"] = auditcommentuuid
    params["comment"] = comment
    params["contractUuid"] = contractuuid
    params["replyAuditCommentUuid"] = replyauditcommentuuid
    LOGGER.info("编辑一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewTencentInfo(uid):
    """
    查询腾讯接口(废)
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 941')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTencentInfo"
    LOGGER.info("查询腾讯接口(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询腾讯接口(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询腾讯接口(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_updateContractInfoSignState(uid):
    """
    修改合同状态为重签(废)
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 942')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/updateContractInfoSignState"
    LOGGER.info("修改合同状态为重签(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("修改合同状态为重签(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改合同状态为重签(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(uid):
    """
    修改法大大合同签署状态修改为重签(废)
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 943')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findContractInfoSignStateWeb"
    LOGGER.info("修改法大大合同签署状态修改为重签(废)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("修改法大大合同签署状态修改为重签(废)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法大大合同签署状态修改为重签(废)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogs(pagecurrent, pagesize, uuid):
    """
    查询合同操作日志
    :param uuid: 合同uuid(Y),string
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 944')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogs"
    LOGGER.info("查询合同操作日志请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["uuid"] = uuid
    LOGGER.info("查询合同操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同操作日志请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 945')
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


def test_api_78dk_platform_tm_first_addContractCustomerLabel(contractuuid, labelcontent):
    """
    新增客户标签
    :param contractuuid: 合同 uuid,string
    :param labelcontent: 标签内容,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 946')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addContractCustomerLabel"
    LOGGER.info("新增客户标签请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["labelContent"] = labelcontent
    LOGGER.info("新增客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewContractLabels(uid):
    """
    通过合同UUID查询对应的客户标签
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 947')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractLabels"
    LOGGER.info("通过合同UUID查询对应的客户标签请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("通过合同UUID查询对应的客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过合同UUID查询对应的客户标签请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 948')
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


def test_api_78dk_platform_tm_telephone_telephoneCheck(checkstate, message, uuid):
    """
    电核
    :param checkstate: 审核状态,string
    :param uuid: 合同uuid,string
    :param message: 审核人提交信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 949')
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
    电核信息查询-v1.5.1
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 950')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
    LOGGER.info("电核信息查询-v1.5.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("电核信息查询-v1.5.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核信息查询-v1.5.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(begindate, contractnumber, enddate, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    电核列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param state: 状态,string
    :param lable: 标签,string
    :param begindate: 开始时间,string
    :param pagesize: 页面大小,number
    :param contractnumber: 合同编号,string
    :param enddate: 结束时间,string
    :param phone: 电话号码,string
    :param username: 用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 951')
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
    :param groupsort: 分组排序字段,number
    :param question: 问题,string
    :param questionsort: 问题排序字段,number
    :param groupname: 分组名,string
    :param telephonecheckfeedbackuuid: 电核uuid,string
    :param contractuuid: 合同UUID,string
    :param answer: 答案,string
    :param risktype: 风险类型,string
    :param state: 数据状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 952')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 953')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 954')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 955')
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


def test_api_78dk_platform_tm_final_finalCheck(checkstate, message, uuid):
    """
    终审
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 956')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/finalCheck"
    LOGGER.info("终审请求地址:【{}】".format(requesturl))
    params = dict()
    params["checkState"] = checkstate
    params["message"] = message
    params["uuid"] = uuid
    LOGGER.info("终审请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContract(uid):
    """
    终审信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 957')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContract"
    LOGGER.info("终审信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("终审信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContracts(begindate, contractnumber, enddate, lable, name, pagecurrent, pagesize, phone, state, username):
    """
    终审列表查询
    :param contractnumber: 合同编号,string
    :param state: 状态,string
    :param enddate: 结束时间,string
    :param lable: 标签,string
    :param pagecurrent: 当前页,number
    :param begindate: 开始时间,string
    :param phone: 电话号码,string
    :param username: 用户名,string
    :param pagesize: 页面大小,number
    :param name: 编号等一系列东西,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 958')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
    LOGGER.info("终审列表查询请求地址:【{}】".format(requesturl))
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
    LOGGER.info("终审列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_after_viewAuditMonitors(enddate, pagecurrent, pagesize, qifascore, searchwhere, startdate):
    """
    贷后列表
    :param pagecurrent: 当前页(Y),number
    :param enddate: 结束日期,string
    :param startdate: 开始日期,string
    :param pagesize: 页面大小(Y),number
    :param qifascore: 启发分数状态,string
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 959')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 960')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 961')
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


def test_api_78dk_platform_om_contract_viewContracts(begindate, enddate, name, orderstate, pagecurrent, pagesize):
    """
    合同列表查询（申请列表）-v1.4.0
    :param name: 组合查询字段,string
    :param pagesize: 页面大小,number
    :param begindate: 开始时间,string
    :param orderstate: 订单状态,string
    :param enddate: 结束时间,string
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 962')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContracts"
    LOGGER.info("合同列表查询（申请列表）-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("合同列表查询（申请列表）-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同列表查询（申请列表）-v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewContract(uid):
    """
    合同详情查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 963')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContract"
    LOGGER.info("合同详情查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("合同详情查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同详情查询请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 964')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 965')
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
    :param pagesize: 每页条数,number
    :param name: 编号什么的,string
    :param pagecurrent: 当前页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 966')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 967')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 968')
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
    :param begindate: 开始时候,number
    :param name: 组合查询字段,string
    :param orderstate: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 969')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 970')
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


def test_api_78dk_platform_om_contract_saveErpInfo(contractuuid, erpinfonumber):
    """
    保存合同ERP信息
    :param erpinfonumber: ERP编号,string
    :param contractuuid: 合同 UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 971')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/saveErpInfo"
    LOGGER.info("保存合同ERP信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["erpInfoNumber"] = erpinfonumber
    LOGGER.info("保存合同ERP信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存合同ERP信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_trans_findTransLogList(begindate, enddate, pagecurrent, pagesize, searchwhere, transstate, transtype):
    """
    交易流水列表
    :param pagecurrent: 当前页（Y）,number
    :param enddate: 结束日期,string
    :param searchwhere: 查询条件,string
    :param transtype: 交易类型,string
    :param transstate: 交易状态,string
    :param begindate: 开始日期,string
    :param pagesize: 页面大小（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 972')
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


def test_api_78dk_platform_om_hmaw_offlineBalanceInit(contractnumber, number, pagecurrent, pagesize):
    """
    手动还款结余计算初始化
    :param pagesize: 每页行数（Y）,number
    :param number: 期数（Y）,number
    :param contractnumber: 合同编号（Y）,string
    :param pagecurrent: 页码（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 973')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/offlineBalanceInit"
    LOGGER.info("手动还款结余计算初始化请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["number"] = number
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("手动还款结余计算初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动还款结余计算初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_hmaw_addRepayManualApply(actualamt, billperiod, contractuuid, optway, shouldrepayamt, userbilluuid):
    """
    添加手动还款申请
    :param actualamt: 还款金额（Y）,string
    :param billperiod: 期数（Y）,number
    :param contractuuid: 合同uuid（Y）,string
    :param optway: 还款方式（Y）,string
    :param shouldrepayamt: 应还金额,string
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 974')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/addRepayManualApply"
    LOGGER.info("添加手动还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["billPeriod"] = billperiod
    params["contractUuid"] = contractuuid
    params["optWay"] = optway
    params["shouldRepayAmt"] = shouldrepayamt
    params["userBillUuid"] = userbilluuid
    LOGGER.info("添加手动还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加手动还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_hmaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    """
    获取手动扣款列表
    :param paystate: 支付状态,string
    :param pagesize: 每页行数（Y）,number
    :param pagecurrent: 页码（Y）,number
    :param begindate: 开始时间,string
    :param overduestate: 预期状态,string
    :param enddate: 结束时间,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 975')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findRepayCommons"
    LOGGER.info("获取手动扣款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["overdueState"] = overduestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["payState"] = paystate
    params["searchWhereOr"] = searchwhereor
    LOGGER.info("获取手动扣款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手动扣款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_hmaw_findManuelHistoryList(billperiod, contractuuid, pagecurrent, pagesize):
    """
    获取手动扣款历史记录
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :param billperiod: 账单期数（Y）,number
    :param contractuuid: 合同UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 976')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findManuelHistoryList"
    LOGGER.info("获取手动扣款历史记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["billPeriod"] = billperiod
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("获取手动扣款历史记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手动扣款历史记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceInit(contractnumber):
    """
    提前还款结余计算初始化
    :param contractnumber: 合同编号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 977')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceInit"
    LOGGER.info("提前还款结余计算初始化请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    LOGGER.info("提前还款结余计算初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还款结余计算初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceRefresh(contractnumber, optway, prepaymenthandlingfeeremission, repayamt):
    """
    提前还款结余计算刷新接口
    :param repayamt: 还款金额（Y）,string
    :param optway: 还款方式（Y）,string
    :param prepaymenthandlingfeeremission: 提前还款手续费 减免金额（Y）,string
    :param contractnumber: 合同编号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 978')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceRefresh"
    LOGGER.info("提前还款结余计算刷新接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["optWay"] = optway
    params["prepaymentHandlingFeeRemission"] = prepaymenthandlingfeeremission
    params["repayAmt"] = repayamt
    LOGGER.info("提前还款结余计算刷新接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还款结余计算刷新接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_adaw_addRepayManualApply(actualamt, actualrepaydate, bankseqid, contractuuid, optway, prepaymenthandlingfee, reliefamt, remarks, urls):
    """
    添加提前还款申请
    :param optway: 还款方式（Y）,string
    :param bankseqid: 银行流水编号（Y）,string
    :param actualamt: 实际金额（Y）,string
    :param remarks: 备注或意见（Y）,string
    :param contractuuid: 合同UUID （Y）,string
    :param reliefamt: 减免金额（Y）,string
    :param actualrepaydate: 反款日期（N）,string
    :param urls: 图片列表（Y）,string
    :param prepaymenthandlingfee: 提前还款手续费（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 979')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/addRepayManualApply"
    LOGGER.info("添加提前还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["actualRepayDate"] = actualrepaydate
    params["bankSeqId"] = bankseqid
    params["contractUuid"] = contractuuid
    params["optWay"] = optway
    params["prepaymentHandlingFee"] = prepaymenthandlingfee
    params["reliefAmt"] = reliefamt
    params["remarks"] = remarks
    params["urls"] = urls
    LOGGER.info("添加提前还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加提前还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_adaw_findRepayPrepayments(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    """
    获取提前还款列表
    :param paystate: 还款状态,string
    :param overduestate: 预期状态,string
    :param enddate: 结束时间,string
    :param searchwhereor: 文字信息,string
    :param pagecurrent: 页码（Y）,number
    :param begindate: 开始时间,string
    :param pagesize: 每页条数（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 980')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/findRepayPrepayments"
    LOGGER.info("获取提前还款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["overdueState"] = overduestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["payState"] = paystate
    params["searchWhereOr"] = searchwhereor
    LOGGER.info("获取提前还款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取提前还款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_ulaw_addRepayManualApply(actualamt, bankseqid, billperiod, contractuuid, optway, remarks, urls):
    """
    添加线下还款申请
    :param urls: 图片路径（Y）,string
    :param optway: 还款状态（Y）,string
    :param billperiod: 期数（Y）,number
    :param bankseqid: 银行流水编号（Y）,string
    :param remarks: 备注或意见（Y）,string
    :param actualamt: 实际金额（Y）,string
    :param contractuuid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 981')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/addRepayManualApply"
    LOGGER.info("添加线下还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["bankSeqId"] = bankseqid
    params["billPeriod"] = billperiod
    params["contractUuid"] = contractuuid
    params["optWay"] = optway
    params["remarks"] = remarks
    params["urls"] = urls
    LOGGER.info("添加线下还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加线下还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_ulaw_offlineBalanceInit(contractnumber, number):
    """
    线下还款结余计算初始化
    :param contractnumber: 合同编号（Y）,string
    :param number: 期数（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 982')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/offlineBalanceInit"
    LOGGER.info("线下还款结余计算初始化请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["number"] = number
    LOGGER.info("线下还款结余计算初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线下还款结余计算初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_ulaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    """
    获取线下还款列表
    :param pagecurrent: 页码（Y）,number
    :param begindate: 开始时间,string
    :param paystate: 支付状态,string
    :param enddate: 结束时间,string
    :param pagesize: 每页条数（Y）,number
    :param overduestate: 预期状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 983')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/findRepayCommons"
    LOGGER.info("获取线下还款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["overdueState"] = overduestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["payState"] = paystate
    params["searchWhereOr"] = searchwhereor
    LOGGER.info("获取线下还款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取线下还款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_lm_loanOperation(bankseqid, contractuuid, loanamount, remarks, urls):
    """
    放款操作
    :param contractuuid: 合同UUID,string
    :param loanamount: 放款金额,string
    :param remarks: 备注,string
    :param bankseqid: 银行流水,string
    :param urls: 图片url,array<string>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 984')
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
    :param searchwhere: 查询条件,string
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 985')
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


def test_api_78dk_platform_file_download(filename, urlstr):
    """
    文件下载
    :param filename: 文件名称,string
    :param urlstr: 文件路径,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 986')
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


def test_api_78dk_platform_tm_incoming_findTemplateDictionaries():
    """
    查询所有模板配置字典
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 987')
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
    :param producttemplateuuid: 模板UUID,string
    :param pagesize: 页面大小,number
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 988')
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
    :param name: 模板名称,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 989')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 990')
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
    :param remark: 备注,string
    :param sysdata: 进件配置项,array<number>
    :param templatename: 模板名称,string
    :param producttemplateuuid: 模板UUID,string
    :param templatetype: 模板类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 991')
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


def test_api_78dk_platform_common_findQiniuToken(type):
    """
    获取七牛tocken
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 992')
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


def test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid):
    """
    删除进件模板
    :param producttemplateuuid: 模板UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 993')
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


def test_api_78dk_platform_common_viewImageUrl(qiniukey, type):
    """
    获取图片url
    :param qiniukey: 七牛key,string
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 994')
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


def test_api_78dk_platform_tm_first_viewContractImages(contractuuid):
    """
    审核详情-影像资料v1.4.0
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 995')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractImages"
    LOGGER.info("审核详情-影像资料v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("审核详情-影像资料v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核详情-影像资料v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewMxInfo(contractuuid, type):
    """
    查询魔蝎报告
    :param type: 报告类型,string
    :param contractuuid: 合同id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 996')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 997')
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


def test_api_78dk_bm_viewUserBill(contractuuid, pagecurrent, pagesize):
    """
    个人账单--v1.5
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :param contractuuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 998')
    requesturl = baseUrl + "/api/78dk/bm/viewUserBill"
    LOGGER.info("个人账单--v1.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("个人账单--v1.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("个人账单--v1.5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_bm_viewBillList(contractnumber, merchantname, pagecurrent, pagesize, state, usermobile, username):
    """
    账单列表
    :param usermobile: 手机号,string
    :param merchantname: 商户,string
    :param username: 姓名,string
    :param contractnumber: 订单编号,string
    :param state: 还款状态,string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 999')
    requesturl = baseUrl + "/api/78dk/bm/viewBillList"
    LOGGER.info("账单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractNumber"] = contractnumber
    params["merchantName"] = merchantname
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["state"] = state
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("账单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单列表请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1000')
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
    :param username: 用户名称,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param contractnumber: 合同编号,string
    :param merchantname: 商户明朝,string
    :param phone: 电话号码,string
    :param loanstate: 放款类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1001')
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
    :param remarks: 备注（Y）,string
    :param urlname: 图片名称（Y）,string
    :param loanamount: 放款金额（Y）,string
    :param contractuuid: 合同uuid（Y）,string
    :param url: 图片路径（Y）,string
    :param bankseqid: 银行流水,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1002')
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
    放款列表
    :param pagesize: 页面大小（Y）,number
    :param enddate: 结束时间,string
    :param username: 用户名称,string
    :param phone: 手机号,string
    :param loanstate: 放款类型,string
    :param pagecurrent: 当前页（Y）,number
    :param merchantname: 商户名称,string
    :param begindate: 开始时间,string
    :param contractnumber: 合同编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1003')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewLoans"
    LOGGER.info("放款列表请求地址:【{}】".format(requesturl))
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
    LOGGER.info("放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_lm_viewUserBill(begindate, enddate, name, orderstate, pagecurrent, pagesize, state, uuid):
    """
    账单信息
    :param pagesize: 页面大小（Y）,number
    :param state: 状态 all为全部 pass为通过的 fail为没有通过的,string
    :param orderstate: 订单状态,string
    :param uuid: 合同uuid（Y）,string
    :param name: 名称,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param pagecurrent: 当前页（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1004')
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
    :param enddate: 结束时间,number
    :param merchantname: 商户名称,string
    :param begindate: 开始时间,string
    :param contractnumber: 合同编号,string
    :param username: 客户名称,string
    :param phone: 客户电话,string
    :param loanstate: 放款状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1005')
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
    查看放款详情-v1.5..0
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1006')
    requesturl = baseUrl + "/api/78dk/platform/lm/viewLoanDetil"
    LOGGER.info("查看放款详情-v1.5..0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查看放款详情-v1.5..0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看放款详情-v1.5..0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1282')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1283')
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


def test_api_78dk_platform_om_repayment_findRepaymentList(applyoptname, auditoptname, auditstate, contractnumber, lastpaydatebegintime, lastpaydateendtime, overduestate, pagecurrent, pagesize, paystate, usermobile, username):
    """
    还款列表--v1.5.0
    :param applyoptname: 提交人,string
    :param auditoptname: 审核人,string
    :param overduestate: 逾期状态,string
    :param lastpaydateendtime: 结束时间,string
    :param usermobile: 手机号,string
    :param pagesize: 页面大小,number
    :param paystate: 还款状态,string
    :param lastpaydatebegintime: 开始时间,string
    :param username: 借款人,string
    :param auditstate: 审核状态,string
    :param pagecurrent: 当前页,number
    :param contractnumber: 订单编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1284')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findRepaymentList"
    LOGGER.info("还款列表--v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyOptName"] = applyoptname
    params["auditOptName"] = auditoptname
    params["auditState"] = auditstate
    params["contractNumber"] = contractnumber
    params["lastPayDateBeginTime"] = lastpaydatebegintime
    params["lastPayDateEndTime"] = lastpaydateendtime
    params["overdueState"] = overduestate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["payState"] = paystate
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("还款列表--v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款列表--v1.5.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1285')
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


def test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid, merchantuuid, name, remark):
    """
    新增商户BD信息
    :param remark: BD备注,string
    :param merchantuuid: 商户UUID,string
    :param name: BD姓名,string
    :param bdinfouuid: BD UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1286')
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


def test_api_78dk_platform_om_bd_findBdInfoList(bdstate, enddate, pagecurrent, pagesize, searchwhere, startdate):
    """
    BD列表
    :param pagesize: ,number
    :param pagecurrent: ,number
    :param bdstate: ,string
    :param enddate: ,string
    :param searchwhere: ,string
    :param startdate: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1289')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/findBdInfoList"
    LOGGER.info("BD列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdState"] = bdstate
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("BD列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_addBdInfo(channeluuid, email, mobile, name):
    """
    BD新增
    :param email: 邮箱,string
    :param name: 名称,string
    :param channeluuid: 渠道uuid,string
    :param mobile: 电话,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1290')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/addBdInfo"
    LOGGER.info("BD新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["email"] = email
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("BD新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_bd_replaceBdInfoMerchant(merchantuuids, newddinfouuid, oldddinfouuid):
    """
    BD替换
    :param merchantuuids: 选中的商户UID,array<object>
    :param oldddinfouuid: 老BDUUID,string
    :param newddinfouuid: 新BDUUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1291')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1292')
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
    BD统计-v1.4.0
    :param startdate: 开始时间,string
    :param searchwhere: 查询条件,string
    :param pagesize: 每页几条,number
    :param bdstate: BD状态,string
    :param enddate: 结束时间,string
    :param pagecurrent: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1293')
    requesturl = baseUrl + "/api/78dk/platform/om/bd/bdTj"
    LOGGER.info("BD统计-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["bdState"] = bdstate
    params["endDate"] = enddate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    params["startDate"] = startdate
    LOGGER.info("BD统计-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD统计-v1.4.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1294')
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


def test_api_78dk_platform_tm_machine_resultMachine(uuid):
    """
    机审详情
    :param uuid: 订单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1295')
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


def test_api_78dk_platform_tm_bd_viewBdInfo(uid):
    """
    查询BD信息
    :param uid: 合同uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1297')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1298')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1299')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1300')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1301')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1302')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1303')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1304')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1305')
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
    :param windcontroldatasource: 风控数据源,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1306')
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


def test_api_78dk_platform_om_repayment_addRepayUnderLineApply(actualamt, actualrepaydate, picturelist, remarks, shouldrepayamt, userbilluuid):
    """
    手动还款（线下还款）-提交审核申请
    :param shouldrepayamt: 应还金额,string
    :param actualamt: 实际还款金额,string
    :param picturelist: 还款凭证 图片列表,array<object>
    :param actualrepaydate: 实际还款时间,string
    :param remarks: 手动还款原因,string
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1307')
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


def test_api_78dk_platform_tm_js_viewJSInfo(uid):
    """
    查询商户结算信息（废弃）
    :param uid: 合同uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1309')
    requesturl = baseUrl + "/api/78dk/platform/tm/js/viewJSInfo"
    LOGGER.info("查询商户结算信息（废弃）请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询商户结算信息（废弃）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户结算信息（废弃）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid, merchantuuid, name, remark):
    """
    修改商户BD信息
    :param remark: BD备注,string
    :param merchantuuid: 商户UUID,string
    :param bdinfouuid: BD UUID,string
    :param name: BD姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1310')
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


def test_api_78dk_platform_om_repayment_findRepayment(userbilluuid):
    """
    还款基本信息--v1.5.0
    :param userbilluuid: 用户账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1312')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findRepayment"
    LOGGER.info("还款基本信息--v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("还款基本信息--v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款基本信息--v1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt, shouldrepayamt, userbilluuid):
    """
    手动代扣-提交申请
    :param actualamt: 实际还款金额,string
    :param shouldrepayamt: 应还金额,string
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1313')
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


def test_api_78dk_platform_om_repayment_findOneRepayBill(userbilluuid):
    """
    查询还款账单（手动还款和手动代扣弹窗页面顶部公用)
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1314')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/findOneRepayBill"
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询还款账单（手动还款和手动代扣弹窗页面顶部公用)请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1315')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1316')
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


def test_api_78dk_platform_tm_operate_operationalCheck(begindate, enddate, name, pagecurrent, pagesize, phone, state, uuid):
    """
    运营审核列表查询-v1.5.0
    :param uuid: 合同号,string
    :param name: 姓名,string
    :param enddate: 结束时间,string
    :param begindate: 开始时间,string
    :param pagecurrent: 当前页,number
    :param phone: 电话,string
    :param pagesize: 页面大小,number
    :param state: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1319')
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


def test_api_78dk_platform_tm_operate_operationalsave(checkstate, message, uuid):
    """
    运营审核
    :param message: 审核人提交信息,string
    :param uuid: 合同号,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1320')
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


def test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid):
    """
    运营审批信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1323')
    requesturl = baseUrl + "/api/78dk/platform/tm/operate/viewOperateCheckContract"
    LOGGER.info("运营审批信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("运营审批信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营审批信息查询请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1324')
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


def test_api_78dk_platform_tm_operate_operationAllsave(begindate, checkstate, enddate, message, name, pagecurrent, phone, state, uuid):
    """
    运营审核-批量
    :param phone: 电话,string
    :param pagecurrent: 总计条数,
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :param name: 姓名,string
    :param state: 订单状态(pending),string
    :param begindate: 开始时间,string
    :param uuid: 合同号,string
    :param enddate: 结束时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1325')
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


def test_api_78dk_platform_mm_base_store_uploadImageRoleList(imagelist):
    """
    门店影像资料上传-v1.4
    :param imagelist: 影像资料集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1341')
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


def test_api_78dk_platform_mm_base_store_freeze(type, uid):
    """
    冻结门店/解冻-v1.4
    :param uid: 门店Uuid(Y),string
    :param type: 冻结或者解冻,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1342')
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


def test_api_78dk_platform_mm_base_storeExamine(ispass, message, uid):
    """
    门店审核-v1.4
    :param ispass: 是否通过(Y),string
    :param message: 审核信息,string
    :param uid: 门店iuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1343')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/storeExamine"
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


def test_api_78dk_platform_mm_base_store_addStoreBusiness(discountpercent, list, uid, workpercent):
    """
    门店业务信息-新增或修改-v1.4
    :param discountpercent: 贴息占比,number
    :param uid: 门店id,string
    :param workpercent: 工作占比,number
    :param list: 商品数据,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1344')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/addStoreBusiness"
    LOGGER.info("门店业务信息-新增或修改-v1.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountPercent"] = discountpercent
    params["list"] = list
    params["uid"] = uid
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1345')
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


def test_api_78dk_platform_mm_base_store_updateStoreBusiness(discountpercent, uid, workpercent):
    """
    门店业务信息-编辑
    :param discountpercent: 贴息占比,number
    :param uid: 门店id,string
    :param workpercent: 工作占比,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1346')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStoreBusiness"
    LOGGER.info("门店业务信息-编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["discountPercent"] = discountpercent
    params["uid"] = uid
    params["workPercent"] = workpercent
    LOGGER.info("门店业务信息-编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店业务信息-编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_updateStoreBusinessProduct(amount, cycle, productname, uid):
    """
    门店业务信息商品-新增
    :param productname: 商品名字,number
    :param uid: 门店id,string
    :param amount: 金额,number
    :param cycle: 周期,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1347')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStoreBusinessProduct"
    LOGGER.info("门店业务信息商品-新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["cycle"] = cycle
    params["productName"] = productname
    params["uid"] = uid
    LOGGER.info("门店业务信息商品-新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店业务信息商品-新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_deleteStoreBusinessProduct(uid):
    """
    门店业务信息商品-删除
    :param uid: 门店业务商品uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1348')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteStoreBusinessProduct"
    LOGGER.info("门店业务信息商品-删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("门店业务信息商品-删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店业务信息商品-删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_unbind_wechart(list, uid):
    """
    微信解绑-v1.4
    :param list: ,array<object>
    :param uid: 商户Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1349')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1350')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1351')
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


def test_api_78dk_platform_om_repayment_downRepaymentList(applyoptname, auditoptname, auditstate, contractnumber, lastpaydatebegintime, lastpaydateendtime, overduestate, paystate, usermobile, username):
    """
    还款列表导出-v1.4.0
    :param overduestate: 逾期状态,string
    :param applyoptname: 提交人,string
    :param auditoptname: 审核人,string
    :param lastpaydatebegintime: 开始时间,string
    :param paystate: 还款状态,string
    :param usermobile: 手机号,string
    :param lastpaydateendtime: 结束时间,string
    :param contractnumber: 订单编号,string
    :param username: 借款人,string
    :param auditstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1375')
    requesturl = baseUrl + "/api/78dk/platform/om/repayment/downRepaymentList"
    LOGGER.info("还款列表导出-v1.4.0请求地址:【{}】".format(requesturl))
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
    LOGGER.info("还款列表导出-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款列表导出-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_downOperationalCheck(begindate, enddate, name, phone, state, uuid):
    """
    运营列表导出-v1.4.0
    :param enddate: 结束时间,string
    :param state: 状态,string
    :param phone: 电话,string
    :param name: 姓名,string
    :param uuid: 合同编号,string
    :param begindate: 开始时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1376')
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


def test_api_78dk_platform_mm_base_bu(uid):
    """
    查询商户业BD操作日志
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1377')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/bu"
    LOGGER.info("查询商户业BD操作日志请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询商户业BD操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户业BD操作日志请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_deleteImageRole(imagelist):
    """
    门店影像删除-v1.4.0
    :param imagelist: 影像资料集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1378')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteImageRole"
    LOGGER.info("门店影像删除-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["imageList"] = imagelist
    LOGGER.info("门店影像删除-v1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店影像删除-v1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_examine_reject(uid):
    """
    打回
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1392')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/reject"
    LOGGER.info("打回请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("打回请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("打回请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1393')
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


def test_api_78dk_platform_mm_base_bd_listDbLogs(uid):
    """
    查询商户业BD操作日志-v1.4
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1398')
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


def test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent, list, storeuuid, workpercent):
    """
    门店业务信息-新增或修改-v1.4
    :param storeuuid: 门店id,string
    :param workpercent: 工作占比,number
    :param discountpercent: 贴息占比,number
    :param list: 商品数据,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1403')
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


def test_api_78dk_platform_mm_base_store_storeExamine(ispass, message, uid):
    """
    门店审核-v1.4
    :param uid: 门店iuid(Y),string
    :param ispass: 是否通过(Y),string
    :param message: 审核信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1405')
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


def test_api_78dk_platform_om_bd_queryBdInfoLog(bdinfouuid):
    """
    BD操作日志查询--v1.5.0
    :param bdinfouuid: uuid,BD列表查询到的bdInfoUuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1512')
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


def test_api_78dk_platform_mm_base_repulse(uid):
    """
    查看被打回的模块1.5.1
    :param uid: 商户uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1513')
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


def test_api_78dk_platform_product_base_saveProductEarlySettle(earlysettledays, earlysettlefredays, earlysettlefrerate, earlysettleinterest, earlysettlesupport, earlysettlevoidmode, productdetailuuid, productearlysettleuuid):
    """
    产品提前结清信息保存（新增、修改）-v1.5.0
    :param earlysettledays: 放款多少天后可提前结清,number
    :param earlysettlefredays: 免收周期（天）,number
    :param earlysettlefrerate: 超出后手续费率,number
    :param earlysettleinterest: 提前结清利息收取方式,string
    :param earlysettlesupport: 是否支持提前结清,string
    :param earlysettlevoidmode: 提前结清免收手续费方式,string
    :param productdetailuuid: 产品uuid,string
    :param productearlysettleuuid: 产品提前结清uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1514')
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


def test_api_78dk_platform_product_base_viewProductEarlySettle(productdetailuuid):
    """
    查询产品提前结清模块信息-v1.5.0
    :param productdetailuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1515')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductEarlySettle"
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


def test_api_78dk_platform_ap_repayment_advancePayment(paydate, remarks, urls, userbilluuid):
    """
    提前还清-v1.5.0
    :param paydate: 还款时间,string
    :param remarks: 还款备注,string
    :param urls: 还款凭证key,string
    :param userbilluuid: 账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1546')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1547')
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
    未结清列表--v1.5.0
    :param uid: 账单uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1548')
    requesturl = baseUrl + "/api/78dk/platform/ap/repayment/findRepaymentList"
    LOGGER.info("未结清列表--v1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("未结清列表--v1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("未结清列表--v1.5.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1573')
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


def test_api_78dk_collection_addMessage(communicatee, condition, file, overduereason, remark, replyrepaytime, useruuid):
    """
    信息提交
    :param condition: 沟通情况,string
    :param replyrepaytime: 承诺还款时间,string
    :param file: 文件,string
    :param communicatee: 沟通对象,string
    :param remark: 备注,string
    :param useruuid: 客户UUID,string
    :param overduereason: 逾期原因,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1619')
    requesturl = baseUrl + "/api/78dk/collection/addMessage"
    LOGGER.info("信息提交请求地址:【{}】".format(requesturl))
    params = dict()
    params["communicatee"] = communicatee
    params["condition"] = condition
    params["file"] = file
    params["overdueReason"] = overduereason
    params["remark"] = remark
    params["replyRepayTime"] = replyrepaytime
    params["userUuid"] = useruuid
    LOGGER.info("信息提交请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("信息提交请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_addFile(file):
    """
    上传文件
    :param file: 文件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1620')
    requesturl = baseUrl + "/api/78dk/collection/addFile"
    LOGGER.info("上传文件请求地址:【{}】".format(requesturl))
    params = dict()
    params["file"] = file
    LOGGER.info("上传文件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("上传文件请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_queryFile(urgentrecalluuid):
    """
    下载文件
    :param urgentrecalluuid: 催收UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1621')
    requesturl = baseUrl + "/api/78dk/collection/queryFile"
    LOGGER.info("下载文件请求地址:【{}】".format(requesturl))
    params = dict()
    params["urgentRecallUuid"] = urgentrecalluuid
    LOGGER.info("下载文件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载文件请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_queryHistory(useruuid):
    """
    催收记录列表
    :param useruuid: 客户UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1622')
    requesturl = baseUrl + "/api/78dk/collection/queryHistory"
    LOGGER.info("催收记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuid"] = useruuid
    LOGGER.info("催收记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("催收记录列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_queryContactsOverdueLoan(useruuid):
    """
    联系人逾期贷款信息
    :param useruuid: 用户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1623')
    requesturl = baseUrl + "/api/78dk/collection/queryContactsOverdueLoan"
    LOGGER.info("联系人逾期贷款信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuid"] = useruuid
    LOGGER.info("联系人逾期贷款信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("联系人逾期贷款信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_queryOverdueLoan(useruuid):
    """
    逾期贷款信息
    :param useruuid: 用户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1624')
    requesturl = baseUrl + "/api/78dk/collection/queryOverdueLoan"
    LOGGER.info("逾期贷款信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuid"] = useruuid
    LOGGER.info("逾期贷款信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期贷款信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_collection_queryUserAndImageInfo(useruuid):
    """
    客户信息影像资料
    :param useruuid: 用户uuid,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1625')
    requesturl = baseUrl + "/api/78dk/collection/queryUserAndImageInfo"
    LOGGER.info("客户信息影像资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["userUuid"] = useruuid
    LOGGER.info("客户信息影像资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客户信息影像资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewMerchantList(auditstate, contractstatus, freezestate, name, openclosestate, overquotastatus, pagecurrent, pagesize):
    """
    查询商户列表-v1.5.2
    :param pagesize: 分页大小(Y),number
    :param name: 商户简称(N),string
    :param pagecurrent: 当前页(Y),number
    :param openclosestate: 开关状态,string
    :param auditstate: 审核状态,string
    :param contractstatus: 合同状态,string
    :param freezestate: 使用状态,string
    :param overquotastatus: 保证金状态【是否需要补缴】,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1657')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
    LOGGER.info("查询商户列表-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["contractStatus"] = contractstatus
    params["freezeState"] = freezestate
    params["name"] = name
    params["openCloseState"] = openclosestate
    params["overQuotaStatus"] = overquotastatus
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询商户列表-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户列表-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewStoreList(auditstate, freezestate, managername, name, pagecurrent, pagesize, sign, uid):
    """
    查询门店列表-v1.5.2
    :param pagesize: 分页大小(Y),number
    :param uid: 商户Uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :param name: 门店名称,string
    :param auditstate: 审核状态,string
    :param freezestate: 冻结状态,string
    :param managername: 门店负责人,string
    :param sign: 租赁状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1658')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
    LOGGER.info("查询门店列表-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditState"] = auditstate
    params["freezeState"] = freezestate
    params["managerName"] = managername
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["sign"] = sign
    params["uid"] = uid
    LOGGER.info("查询门店列表-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店列表-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1659')
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


def test_api_78dk_platform_urge_addMessage(communicatee, condition, datalist, overduereason, remark, replyrepaytime, useruuid):
    """
    电话催收信息提交-v1.5.2
    :param condition: 沟通情况,string
    :param replyrepaytime: 承诺还款时间,string
    :param datalist: 文件,array<object>
    :param communicatee: 沟通对象,string
    :param remark: 备注,string
    :param useruuid: 客户UUID,string
    :param overduereason: 逾期原因,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1660')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1661')
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
    :param useruuid: 客户UUID,string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1662')
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
    联系人逾期贷款信息-v1.5.2
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1663')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryContactsOverdueLoan"
    LOGGER.info("联系人逾期贷款信息-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("联系人逾期贷款信息-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("联系人逾期贷款信息-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryOverdueLoan(uid):
    """
    逾期贷款信息-v1.5.2
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1664')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryOverdueLoan"
    LOGGER.info("逾期贷款信息-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("逾期贷款信息-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期贷款信息-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_queryUserInfo(uid):
    """
    客户信息-v1.5.2
    :param uid: 合同uuid,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1665')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryUserInfo"
    LOGGER.info("客户信息-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("客户信息-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("客户信息-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_findBond(merchantuuid, pagecurrent, pagesize):
    """
    商户保证金缴纳记录查询-v1.5.2
    :param merchantuuid: 商户UUID（y）,string
    :param pagecurrent: 当前页（y）,number
    :param pagesize: 每页几条（y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1666')
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
    :param deductionamount: 保证金扣除金额,string
    :param deductiondate: 保证金扣除时间,string
    :param merchantuuid: 商户UUID（Y）,string
    :param payamount: 缴纳金额,string
    :param paydate: 缴纳时间,string
    :param poolamount: 退回保证池金额,string
    :param pooldate: 退回保证池时间,string
    :param returnamount: 退还商户金额,string
    :param returndate: 退还商户时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1667')
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


def test_api_78dk_platform_prompt_urge_overdue_user(currentpage, currenturge, idcard, loandatebegin, loandateend, mobile, name, overduedaybegin, overduedayend, overduestage, pagesize, repaymentdatebegin, repaymentdateend, totalpage, urgeuuid):
    """
    逾期用户列表v1.5.2
    :param currenturge: 催收员是否是  当前用户,string
    :param idcard: 身份证号,string
    :param loandatebegin: 贷款日期开始,string
    :param loandateend: 贷款日期结束,string
    :param urgeuuid: 催收uuid,string
    :param name: 客户姓名,string
    :param overduedaybegin: 逾期天数开始,string
    :param overduedayend: 逾期天数结束,string
    :param overduestage: 逾期阶段,string
    :param mobile: 手机号,string
    :param repaymentdatebegin: 还款日期开始,string
    :param repaymentdateend: 还款日期结束,string
    :param totalpage: 总页数,number
    :param currentpage: 当前页,number
    :param pagesize: 每页几条,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1668')
    requesturl = baseUrl + "/api/78dk/platform/prompt/urge/overdue/user"
    LOGGER.info("逾期用户列表v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["currentUrge"] = currenturge
    params["idCard"] = idcard
    params["loanDateBegin"] = loandatebegin
    params["loanDateEnd"] = loandateend
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
    LOGGER.info("逾期用户列表v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期用户列表v1.5.2请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1669')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1670')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1671')
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
    :param email: 员工邮箱（备用）,string
    :param mobile: 员工手机号,string
    :param name: 员工姓名,string
    :param pagecurrent: 当前页,number
    :param pagesize: 每页几条,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1672')
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
    :param collectionuuid: 催收人员uuid,string
    :param divisionstate: 分案状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1673')
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


def test_api_78dk_platform_urge_queryMailList(uid):
    """
    通讯录信息-v1.5.2
    :param uid: 用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1674')
    requesturl = baseUrl + "/api/78dk/platform/urge/queryMailList"
    LOGGER.info("通讯录信息-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("通讯录信息-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通讯录信息-v1.5.2请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1675')
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


def test_api_78dk_platform_mm_base_store_saveImagesAndChange(images):
    """
    门店影像图片信息保存-1.5.2
    :param images: 图片集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1676')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveImagesAndChange"
    LOGGER.info("门店影像图片信息保存-1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["images"] = images
    LOGGER.info("门店影像图片信息保存-1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店影像图片信息保存-1.5.2请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1677')
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


def test_api_78dk_platform_mm_viewImageByMerchantUuid(merchantuuid):
    """
    查询商户图片-v1.5.2
    :param merchantuuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1678')
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageByMerchantUuid"
    LOGGER.info("查询商户图片-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    LOGGER.info("查询商户图片-v1.5.2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户图片-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_trans_downTransLogList(begindate, enddate, searchwhereor, transstate, transtype):
    """
    下载交易流水
    :param transstate: 交易状态,string
    :param searchwhereor: 查询条件,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param transtype: 交易类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1793')
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


