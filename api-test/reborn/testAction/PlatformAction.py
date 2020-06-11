#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : PlatformAction.py
@desc       : 项目：reborn 模块：platform 接口方法封装
"""

from reborn.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('platform_apiURL', 'reborn')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_platform_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_platform_cm_base_deleteOperator(uid):
    """
    删除渠道
    :param uid: 渠道编号uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 318')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/deleteOperator"
    LOGGER.info("删除渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_viewChannel(uid):
    """
    查询渠道
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 319')
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
    :param name: 渠道名称(Y),string
    :param province: 渠道所属省份(Y),number
    :param region: 所属大区(Y),number
    :param shortname: 渠道简称(Y),string
    :param parentchanneluuid: 父级uuid(N)不填则该渠道为根渠道,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 320')
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
    :param city: 渠道所属城市(Y),number
    :param name: 渠道名称(Y),string
    :param note: 备注 (N),string
    :param province: 渠道所属省份 (Y),number
    :param region: 所属大区(Y),number
    :param shortname: 渠道简称 (Y),string
    :param operatoruuid: 操作员(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 321')
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


def test_api_78dk_platform_cm_base_business_deleteBusinessInfor(uid):
    """
    删除机构
    :param uid: 删除机构的uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 322')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 323')
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
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessinformationuuid: 业务信息 uuid(N),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param documentaddress: 证件地址(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param documentprovince: 证件省id,number
    :param documentcity: 证件市id,number
    :param documentregion: 证件区id,number
    :param documentprovincename: 证件省名称,string
    :param documentcityname: 证件市名称,string
    :param documentregionname: 证件区名称,string
    :param businessprovince: 实际经营省id,number
    :param businesscity: 实际经营市id,number
    :param businessregion: 实际经营区id,number
    :param businessprovincename: 实际经营省名称,string
    :param businesscityname: 实际经营市名称,string
    :param businessregionname: 实际经营区名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 324')
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
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessinformationuuid: 业务信息 uuid(Y),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param documentaddress: 证件地址(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param socialunifiedcreditcode: 证社会统一征信代码-三合一后(Y),string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param documentprovince: 证件省id,number
    :param documentcity: 证件市id,number
    :param documentregion: 证件区id,number
    :param documentprovincename: 证件省名称,string
    :param documentcityname: 证件市名称,string
    :param documentregionname: 证件区名称,string
    :param businessprovince: 实际经营省id,number
    :param businesscity: 实际经营市id,number
    :param businessregion: 实际经营区id,number
    :param businessprovincename: 实际经营省名称,string
    :param businesscityname: 实际经营市名称,string
    :param businessregionname: 实际经营区名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 325')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 326')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 327')
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
    :param mail: 邮箱(Y),string
    :param mobile: 手机(Y),string
    :param name: 姓名(Y),string
    :param password: 密码(Y),string
    :param salt: 盐(Y),string
    :param title: 职务(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 328')
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
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param mail: 邮箱(Y),string
    :param mobile: 手机(Y),string
    :param name: 姓名(Y),string
    :param operatoruuid: 操作员uuid(Y),string
    :param password: 密码(Y),string
    :param salt: 盐(N),string
    :param title: 职务(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 329')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 330')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 331')
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
    :param accountname: 账户名称(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param accounttype: 账户类型(Y),string
    :param branchname: 支行名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param channelormerchantuuid: 渠道或者商户(Y),string
    :param city: 开户行地址-市(Y),number
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param linenumber: 联行行号(Y),string
    :param phone: 电话号码(Y),string
    :param province: 开户行地址-省(Y),number
    :param region: 开户行地址-区(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 332')
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
    :param accountname: 账户名称(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param accounttype: 账户类型(Y),string
    :param branchname: 支行名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param city: 开户行地址-市(Y),number
    :param clearingaccountuuid: 机构结算信息 UUID(Y),string
    :param linenumber: 联行行号(Y),string
    :param phone: 电话号码(Y),string
    :param province: 开户行地址-省(Y),number
    :param region: 开户行地址-区(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 333')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 334')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 335')
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


def test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    """
    添加渠道法人代表
    :param cardnumber: 证件号码(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param legalpersonuuid: 法人代表uuid(N),string
    :param mobile: 手机号码(Y),string
    :param name: 法人代表姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 336')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
    LOGGER.info("添加渠道法人代表请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("添加渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    """
    编辑渠道法人代表
    :param cardnumber: 证件号码(Y),string
    :param channelormerchantuuid: 渠道或者商户uuid(Y),string
    :param legalpersonuuid: 法人代表uuid(Y),string
    :param mobile: 手机号码(Y),string
    :param name: 法人代表姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 337')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/updateLegalPerson"
    LOGGER.info("编辑渠道法人代表请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("编辑渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_cm_examine_examine(isadopt, message, uid):
    """
    渠道审核
    :param isadopt: 是否通过(Y),boolean
    :param message: 审核人填写信息(N),string
    :param uid: 审核的渠道id(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 338')
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


def test_api_78dk_platform_fund_fundSide_deleteFundSide(uid):
    """
    删除资方
    :param uid: 资方uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 339')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 340')
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
    :param name: 资方名称(Y),string
    :param state: 资方状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 341')
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
    :param fundsideuuid: 资方uuid(Y),string
    :param name: 资方名称(Y),string
    :param state: 资方状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 342')
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


def test_api_78dk_platform_fund_fundPackage_deleteFundPackage(uid):
    """
    删除资金包
    :param uid: 资金包uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 343')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 344')
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
    :param name: 资金包名称(Y),string
    :param state: 数据状态(Y),string
    :param fundsideuuid: 资方uuid(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 345')
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
    :param amount: 总额度(Y),number
    :param fundpackageuuid: 资金包uuid(Y),string
    :param name: 资金包名称(Y),string
    :param state: 数据状态(Y),string
    :param fundsideuuid: 资方uuid,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 346')
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


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(platformprivilegeuuid, platformuseruuid):
    """
    新增/修改权限
    :param platformprivilegeuuid: 权限UUid(Y),string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 347')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 348')
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


def test_api_78dk_platform_sys_user_updateSystemUser(email, mobile, name, platformuserprofileuuid):
    """
    修改用户
    :param email: 用户邮箱(Y),string
    :param mobile: 用户手机(Y),string
    :param name: 用户姓名(Y),string
    :param platformuserprofileuuid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 349')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 350')
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
    :param mobile: 用户手机(Y),string
    :param name: 用户姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 351')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 352')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 353')
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


def test_api_78dk_platform_mm_base_updateMerchant(channeluuid, merchantuuid, name, note, parentmerchantuuid, shortname):
    """
    修改基本信息
    :param merchantuuid: 商户Uuid(Y),string
    :param name: 商户名称(Y),string
    :param note: 商户描述/备注(N),string
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param shortname: 商户简称(Y),string
    :param channeluuid: 渠道Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 354')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
    LOGGER.info("修改基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["merchantUuid"] = merchantuuid
    params["name"] = name
    params["note"] = note
    params["parentMerchantUuid"] = parentmerchantuuid
    params["shortName"] = shortname
    LOGGER.info("修改基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_deleteMerchant(uid):
    """
    删除基本信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 355')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/deleteMerchant"
    LOGGER.info("删除基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("删除基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_saveMerchant(channeluuid, name, note, parentmerchantuuid, shortname):
    """
    新增基本信息
    :param name: 商户名称(Y),string
    :param note: 商户描述/备注(N),string
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param shortname: 商户简称(Y),string
    :param channeluuid: 渠道Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 356')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
    LOGGER.info("新增基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelUuid"] = channeluuid
    params["name"] = name
    params["note"] = note
    params["parentMerchantUuid"] = parentmerchantuuid
    params["shortName"] = shortname
    LOGGER.info("新增基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_viewMerchant(uid):
    """
    查询基本信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 357')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
    LOGGER.info("查询基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    修改机构信息
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessinformationuuid: 业务信息 UUID(Y),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param documentaddress: 证件地址(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param socialunifiedcreditcode: 社会统一征信代码-三证合一后(Y),string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param businessprovincename: 实际经营省名称,string
    :param businesscityname: 实际经营市名称,string
    :param businessregionname: 实际经营区名称,string
    :param businesscity: 实际经营市id,number
    :param businessprovince: 实际经营省id,number
    :param businessregion: 实际经营区id,number
    :param documentcity: 证件市id,number
    :param documentcityname: 证件市名称,string
    :param documentprovince: 证件省id,number
    :param documentprovincename: 证件省名称,string
    :param documentregion: 证件区id,number
    :param documentregionname: 证件区名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 358')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/updateBusinessInfor"
    LOGGER.info("修改机构信息请求地址:【{}】".format(requesturl))
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
    LOGGER.info("修改机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改机构信息请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 359')
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


def test_api_78dk_platform_mm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesscity, businesscityname, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessprovince, businessprovincename, businessregion, businessregionname, businessregistrationnumber, channelormerchantuuid, documentaddress, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber):
    """
    新增机构信息
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param businessaddresszipcode: 实际经营地址邮编(Y),string
    :param businesshoursendtime: 每日结束营业时间(Y),string
    :param businesshoursstarttime: 每日开始营业时间(Y),string
    :param businessinformationuuid: 业务信息 UUID(N),string
    :param businessregistrationnumber: 工商登记号-三证合一前(N),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param documentaddress: 证件地址(Y),string
    :param email: 业务邮箱-用于对账等使用(Y),string
    :param organizationcode: 组织结构代码-三证合一前(Y),string
    :param socialunifiedcreditcode: 社会统一征信代码-三证合一后(Y),string
    :param storerentalendtime: 经营场所租赁结束时间(Y),string
    :param storerentalstarttime: 经营场所租赁开始时间(Y),string
    :param taxregistrationnumber: 税务登记号-三证合一前(Y),string
    :param documentprovince: 证件省id,number
    :param documentcity: 证件市id,number
    :param documentregion: 证件区id,number
    :param documentprovincename: 证件省名称,string
    :param documentcityname: 证件市名称,string
    :param documentregionname: 证件区名称,string
    :param businessprovince: 实际经营省id,number
    :param businesscity: 实际经营市id,number
    :param businessregion: 实际经营区id,number
    :param businessprovincename: 实际经营省名称,string
    :param businesscityname: 实际经营市名称,string
    :param businessregionname: 实际经营区名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 360')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/saveBusinessInfor"
    LOGGER.info("新增机构信息请求地址:【{}】".format(requesturl))
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
    LOGGER.info("新增机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(uid):
    """
    根据商户Uuid查询机构信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 361')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/viewBusinessInforByMerchant"
    LOGGER.info("根据商户Uuid查询机构信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_updateLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    """
    修改法人信息
    :param cardnumber: 证件号码(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param legalpersonuuid: 法人代表Uuid(Y),string
    :param mobile: 手机号码(Y),string
    :param name: 法人代表姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 362')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/updateLegalPerson"
    LOGGER.info("修改法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("修改法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法人信息请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 363')
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


def test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber, channelormerchantuuid, legalpersonuuid, mobile, name):
    """
    新增法人信息
    :param cardnumber: 证件号码(Y),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param legalpersonuuid: 法人代表Uuid(N),string
    :param mobile: 手机号码(Y),string
    :param name: 法人代表姓名(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 364')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/saveLegalPerson"
    LOGGER.info("新增法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["channelOrMerchantUuid"] = channelormerchantuuid
    params["legalPersonUuid"] = legalpersonuuid
    params["mobile"] = mobile
    params["name"] = name
    LOGGER.info("新增法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(uid):
    """
    根据商户Uuid查询法人信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 365')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/viewLegalPersonByMerchant"
    LOGGER.info("根据商户Uuid查询法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_updateClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    """
    修改结算信息
    :param accountname: 账户名称(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param accounttype: 账户类型(Y),string
    :param branchname: 支行名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param city: 市(Y),number
    :param clearingaccountuuid: 商户结算Uuid(Y),string
    :param linenumber: 联行行号(Y),string
    :param phone: 电话号码(Y),string
    :param province: 省(Y),number
    :param region: 区/县(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 366')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/updateClearingAccount"
    LOGGER.info("修改结算信息请求地址:【{}】".format(requesturl))
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
    LOGGER.info("修改结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改结算信息请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 367')
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


def test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname, accountnumber, accountopeningbank, accounttype, branchname, chamberlainidcard, channelormerchantuuid, city, clearingaccountuuid, linenumber, phone, province, region):
    """
    新增结算信息
    :param accountname: 账户名称(Y),string
    :param accountnumber: 结算账号(Y),string
    :param accountopeningbank: 开户银行(Y),string
    :param accounttype: 账户类型(Y),string
    :param branchname: 支行名称(Y),string
    :param chamberlainidcard: 收款人身份证号(N),string
    :param channelormerchantuuid: 商户Uuid(Y),string
    :param city: 市(Y),number
    :param clearingaccountuuid: 商户结算Uuid(N),string
    :param linenumber: 联行行号(Y),string
    :param phone: 电话号码(Y),string
    :param province: 省(Y),number
    :param region: 区/县(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 368')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/saveClearingAccount"
    LOGGER.info("新增结算信息请求地址:【{}】".format(requesturl))
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
    LOGGER.info("新增结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(uid):
    """
    根据商户Uuid查询结算信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 369')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/viewClearingAccountByMerchant"
    LOGGER.info("根据商户Uuid查询结算信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_updateStore(businessaddress, businessaddressgpsloction, city, cityname, managername, managerphone, merchantuuid, province, provincename, region, regionname, storename, stormuuid):
    """
    修改门店信息
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param managername: 门店负责人姓名(Y),string
    :param managerphone: 门店负责人电话(Y),string
    :param merchantuuid: 商户Uuid(Y),string
    :param stormuuid: 门店Uuid(Y),string
    :param province: 省id,number
    :param city: 市id,number
    :param region: 区id,number
    :param provincename: 省名称,string
    :param cityname: 市名称,string
    :param regionname: 区名称,string
    :param storename: 门店名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 370')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStore"
    LOGGER.info("修改门店信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["city"] = city
    params["cityName"] = cityname
    params["managerName"] = managername
    params["managerPhone"] = managerphone
    params["merchantUuid"] = merchantuuid
    params["province"] = province
    params["provinceName"] = provincename
    params["region"] = region
    params["regionName"] = regionname
    params["storeName"] = storename
    params["stormUuid"] = stormuuid
    LOGGER.info("修改门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改门店信息请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 371')
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


def test_api_78dk_platform_mm_base_store_saveStore(businessaddress, businessaddressgpsloction, city, cityname, managername, managerphone, merchantuuid, province, provincename, region, regionname, storename, stormuuid):
    """
    新增门店信息
    :param businessaddress: 实际经营地址(Y),string
    :param businessaddressgpsloction: 实际经营地址GPS位置(N),string
    :param managername: 门店负责人姓名(Y),string
    :param managerphone: 门店负责人电话(Y),string
    :param merchantuuid: 商户Uuid(Y),string
    :param stormuuid: 门店Uuid(N),string
    :param storename: 门店名称,string
    :param province: 省id,number
    :param city: 市id,number
    :param region: 区id,number
    :param provincename: 省名称,string
    :param cityname: 市名称,string
    :param regionname: 区名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 372')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
    LOGGER.info("新增门店信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessAddress"] = businessaddress
    params["businessAddressGpsLoction"] = businessaddressgpsloction
    params["city"] = city
    params["cityName"] = cityname
    params["managerName"] = managername
    params["managerPhone"] = managerphone
    params["merchantUuid"] = merchantuuid
    params["province"] = province
    params["provinceName"] = provincename
    params["region"] = region
    params["regionName"] = regionname
    params["storeName"] = storename
    params["stormUuid"] = stormuuid
    LOGGER.info("新增门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_base_store_viewStore(uid):
    """
    查询门店信息
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 373')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStore"
    LOGGER.info("查询门店信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店信息请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 374')
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


def test_api_78dk_platform_mm_money_updateMerchantMoney(amountday, amountmonth, amountsingle, amountsum, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    修改额度管理
    :param amountday: 总额度-日(Y),number
    :param amountmonth: 总额度-月(Y),number
    :param amountsingle: 单笔总额度-日(Y),number
    :param amountsum: 总额度(Y),number
    :param merchantuuid: 商户Uuid(Y),string
    :param moneyconfiguuid: 商户额度Uuid(Y),string
    :param zoomcoefficient: 预授信额度放大系数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 375')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
    LOGGER.info("修改额度管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("修改额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改额度管理请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 376')
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


def test_api_78dk_platform_mm_money_saveMerchantMoney(amountday, amountmonth, amountsingle, amountsum, merchantuuid, moneyconfiguuid, zoomcoefficient):
    """
    新增额度管理
    :param amountday: 总额度-日(Y),number
    :param amountmonth: 总额度-月(Y),number
    :param amountsingle: 总额度-单笔(Y),number
    :param amountsum: 总额度(Y),number
    :param merchantuuid: 商户Uuid(Y),string
    :param moneyconfiguuid: 商户额度Uuid(N),string
    :param zoomcoefficient: 预授信额度放大系数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 377')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
    LOGGER.info("新增额度管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["amountDay"] = amountday
    params["amountMonth"] = amountmonth
    params["amountSingle"] = amountsingle
    params["amountSum"] = amountsum
    params["merchantUuid"] = merchantuuid
    params["moneyConfigUuid"] = moneyconfiguuid
    params["zoomCoefficient"] = zoomcoefficient
    LOGGER.info("新增额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(uid):
    """
    根据商户Uuid查询额度管理
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 378')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyByMerchant"
    LOGGER.info("根据商户Uuid查询额度管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("根据商户Uuid查询额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询额度管理请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 379')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 380')
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
    :param uid: 渠道uuid,string
    :param updatestate: 开关状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 381')
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


def test_api_78dk_platform_common_viewProvinceLists(paramsingle):
    """
    省级下拉
    :param paramsingle: 查询条件(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 382')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 383')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 384')
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


def test_api_78dk_platform_product_base_deleteProduct(uid):
    """
    删除产品模版
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 385')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 386')
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


def test_api_78dk_platform_product_base_saveProduct(dischargemode, discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    添加产品模版
    :param discountrate: 商户最大贴息费率（Y）,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :param maxquota: 单笔额度上限（Y）,string
    :param minquota: 单笔额度下限（Y）,string
    :param name: 产品名称（Y）,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param productstate: 产品状态（Y）,string
    :param remark: 产品备注,string
    :param repaymentdatetype: 还款日类型（Y）,string
    :param repaymentmethod: 还款方式（Y）,string
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param fundpackageuuid: 资金包uuid,string
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param loanmode: 放款方式,string
    :param dischargemode: 支付方式,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 387')
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
    LOGGER.info("添加产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["dischargeMode"] = dischargemode
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


def test_api_78dk_platform_product_base_updateProduct(dischargemode, discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, electroniccontracttemplateuuid, firsthalfofthemonth, fundpackageuuid, incomingpartstemplateuuid, loanmode, machineaudittemplateuuid, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productdetailuuid, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state):
    """
    编辑产品模版
    :param discountrate: 商户最大贴息费率（Y）,string
    :param earlyrepaymentfreecycle: 提前还款-免收周期（Y）,number
    :param earlyrepaymenthandlingfee: 提前还款手续费率（Y）,string
    :param earlyrepaymentsupport: 是否支持提前还款（Y）,string
    :param firsthalfofthemonth: 第一固定还款日（Y）,number
    :param maxquota: 单笔额度上限（Y）,string
    :param minquota: 单笔额度下限（Y）,string
    :param name: 产品名称（Y）,string
    :param overduegraceperiod: 宽限期（Y）,number
    :param overduehandlingfeerate: 逾期手续费率 - 手续费（Y）,string
    :param overdueprincipalrate: 逾期手续费率 - 本金（Y）,string
    :param productconfigs: 产品分期方案（Y）,array<object>
    :param productdetailuuid: 产品UUID,string
    :param productstate: 产品状态（Y）,string
    :param remark: 产品备注,string
    :param repaymentdatetype: 还款日类型（Y）,string
    :param repaymentmethod: 还款方式（Y）,string
    :param secondhalfofthemonth: 第二固定还款日（Y）,number
    :param state: 数据状态 unknown: 未知, enabled : 可用, disabled: 禁用,string
    :param fundpackageuuid: 资金包uuid,string
    :param incomingpartstemplateuuid: 进件要素模板uuid,string
    :param machineaudittemplateuuid: 机审策略模板uuid,string
    :param electroniccontracttemplateuuid: 电子合同模板uuid,string
    :param loanmode: 放款方式,string
    :param dischargemode: 支付方式,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 388')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
    LOGGER.info("编辑产品模版请求地址:【{}】".format(requesturl))
    params = dict()
    params["dischargeMode"] = dischargemode
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


def test_api_78dk_platform_mm_base_viewMerchantList(name, pagecurrent, pagesize):
    """
    查询商户列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 389')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
    LOGGER.info("查询商户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_state_updateFreezeState(uid, updatestate):
    """
    下架状态
    :param uid: 商户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 390')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 391')
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


def test_api_78dk_platform_mm_examine_merchanrExamine(ispass, message, uid):
    """
    商户审核
    :param ispass: 是否通过(Y),string
    :param message: 审核信息,string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 392')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/merchanrExamine"
    LOGGER.info("商户审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["isPass"] = ispass
    params["message"] = message
    params["uid"] = uid
    LOGGER.info("商户审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_examine_viewExamineMerchantList(name, pagecurrent, pagesize):
    """
    查询商户审核列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 393')
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
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 394')
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


def test_api_78dk_platform_mm_base_store_viewStoreList(name, pagecurrent, pagesize):
    """
    查询门店列表
    :param name: 商户Uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 395')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
    LOGGER.info("查询门店列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("查询门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店列表请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 396')
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


def test_api_78dk_platform_cm_examine_viewExamineChannels(name, pagecurrent, pagesize):
    """
    渠道审核列表
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 397')
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
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param openclosestate: 冻结状态,string
    :param freezestate: 冻结状态,string
    :param auditstate: 审核状态,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 398')
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


def test_api_78dk_platform_fund_fundSide_viewFundSides(name, pagecurrent, pagesize, state):
    """
    资方列表
    :param name: 资方名称,string
    :param pagecurrent: 当前页码(Y),number
    :param pagesize: 页面大小(Y),number
    :param state: 资方状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 399')
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


def test_api_78dk_platform_fund_fundPackage_viewFundPackages(name, pagecurrent, pagesize):
    """
    资金包列表查询
    :param name: 资金包名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 400')
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


def test_api_78dk_platform_product_base_viewProductDetails(name, pagecurrent, pagesize):
    """
    产品列表
    :param name: 名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 401')
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


def test_api_78dk_platform_sys_user_resetUserPass(uid):
    """
    重置密码
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 402')
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
    :param uid: 用户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 403')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 404')
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


def test_api_78dk_platform_mm_money_viewMerchantMoneyList(name, pagecurrent, pagesize):
    """
    风险控制列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 405')
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


def test_api_78dk_platform_product_pmm_bindProductMerchant(merchanttx, merchantuuids, productuuid):
    """
    绑定产品和商户关系
    :param merchanttx: 贴息比例,array<object>
    :param merchantuuids: 商户uuid(Y),string
    :param productuuid: 商户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 406')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/bindProductMerchant"
    LOGGER.info("绑定产品和商户关系请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantTX"] = merchanttx
    params["merchantUuids"] = merchantuuids
    params["productUuid"] = productuuid
    LOGGER.info("绑定产品和商户关系请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定产品和商户关系请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_product_pmm_saveMerchantTX(customeravailable, discountrate, merchantuuid, period, productdetailconfiguuid, rate):
    """
    保存商户贴息
    :param discountrate: 商户贴息率,string
    :param merchantuuid: 商户uuid,string
    :param period: 分期数,string
    :param productdetailconfiguuid: 产品分期uuid,string
    :param rate: 月利率,string
    :param customeravailable: 分期是否对用户可用,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 407')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    params = dict()
    params["customerAvailable"] = customeravailable
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 408')
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
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :param uuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 409')
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
    :param name: 名称,string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :param uuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 410')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 411')
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
    :param pagecurrent: ,number
    :param pagesize: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 412')
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


def test_api_78dk_platform_product_base_updateProductState(productstate, uuid):
    """
    修改产品状态
    :param uuid: 产品uuid,string
    :param productstate: 产品状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 413')
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
    :param name: 资金包名称,string
    :param pagecurrent: 当前页,number
    :param pagesize: 每页显示条数,number
    :param state: 资金包状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 414')
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


def test_FileUploadController_handlerFileUpload():
    """
    图片上传
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 415')
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
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 416')
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
    初审信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 417')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
    LOGGER.info("初审信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("初审信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContracts(audituuid, enddate, name, orderstate, pagecurrent, pagesize, startdate, state):
    """
    初审列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :param audituuid: 审核人员uuid,string
    :param enddate: 结束日期,string
    :param orderstate: 订单状态,string
    :param startdate: 开始日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 418')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
    LOGGER.info("初审列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUUID"] = audituuid
    params["endDate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["startDate"] = startdate
    params["state"] = state
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
    :param uid: 同盾uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 419')
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


def test_api_78dk_platform_tm_telephone_telephoneCheck(checkstate, message, uuid):
    """
    电核
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 420')
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
    电核信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 421')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
    LOGGER.info("电核信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("电核信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(audituuid, enddate, name, orderstate, pagecurrent, pagesize, startdate, state):
    """
    电核列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :param audituuid: 审核人员uuid,string
    :param enddate: 结束日期,string
    :param orderstate: 订单状态,string
    :param startdate: 开始日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 422')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContracts"
    LOGGER.info("电核列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUUID"] = audituuid
    params["endDate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["startDate"] = startdate
    params["state"] = state
    LOGGER.info("电核列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核列表查询请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 423')
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
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 424')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 425')
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


def test_api_78dk_platform_tm_final_viewFinalCheckContracts(audituuid, enddate, name, orderstate, pagecurrent, pagesize, startdate, state):
    """
    终审列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :param audituuid: 审核人员uuid,string
    :param enddate: 结束日期,string
    :param orderstate: 订单状态,string
    :param startdate: 开始日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 426')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
    LOGGER.info("终审列表查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUUID"] = audituuid
    params["endDate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["startDate"] = startdate
    params["state"] = state
    LOGGER.info("终审列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_viewContracts(begindate, enddate, name, orderstate, pagecurrent, pagesize):
    """
    合同列表查询（申请列表）
    :param name: 组合查询字段,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param orderstate: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 427')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContracts"
    LOGGER.info("合同列表查询（申请列表）请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("合同列表查询（申请列表）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同列表查询（申请列表）请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 428')
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


def test_api_78dk_platform_mm_saveContractImages(key, merchantuuid, url):
    """
    影像资料保存
    :param key: 图片配置key(Y),string
    :param merchantuuid: 商户Uuid(Y),string
    :param url: 图片相对URL(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 429')
    requesturl = baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    params["merchantUuid"] = merchantuuid
    params["url"] = url
    LOGGER.info("影像资料保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_viewImageRoleList(subdivisiontype, uid):
    """
    影像资料权限
    :param uid: 商户Uuid(Y),string
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 430')
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageRoleList"
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


def test_api_78dk_platform_tm_first_viewImageDataConfig(subdivisiontype):
    """
    查询影像列表
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 431')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewImageDataConfig"
    LOGGER.info("查询影像列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["subdivisionType"] = subdivisiontype
    LOGGER.info("查询影像列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询影像列表请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 432')
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


def test_api_78dk_platform_om_contract_viewTongdunInfo(uid):
    """
    同盾信息查询
    :param uid: 同盾uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 433')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 434')
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
    :param pagecurrent: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 435')
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


def test_api_78dk_platform_mm_base_store_uploadQrcode(storeuuid):
    """
    下载门店二维码
    :param storeuuid: 门店uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 436')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/uploadQrcode"
    LOGGER.info("下载门店二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    LOGGER.info("下载门店二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载门店二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(answer, contractuuid, groupname, groupsort, question, questionsort, risktype, state, telephonecheckfeedbackuuid):
    """
    批量添加电核资料
    :param answer: 答案,string
    :param contractuuid: 合同UUID,string
    :param groupname: 分组名,string
    :param question: 问题,string
    :param risktype: 风险类型,string
    :param state: 数据状态,string
    :param telephonecheckfeedbackuuid: 电核uuid,string
    :param groupsort: 分组排序字段,number
    :param questionsort: 问题排序字段,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 437')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 438')
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


def test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid):
    """
    查询合同已经填写的电核问题列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 439')
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


def test_api_78dk_platform_om_trans_findTransLogList(begindate, enddate, pagecurrent, pagesize, searchwhere, transstate, transtype):
    """
    交易流水列表
    :param enddate: 结束日期,string
    :param pagecurrent: 当前页（Y）,number
    :param pagesize: 页面大小（Y）,number
    :param searchwhere: 查询条件,string
    :param begindate: 开始日期,string
    :param transstate: 交易状态,string
    :param transtype: 交易类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 440')
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


def test_api_78dk_platform_tm_first_viewBaiDuInfo(uid):
    """
    查询百度接口
    :param uid: 百度uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 441')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewBaiDuInfo"
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


def test_api_78dk_platform_om_contract_viewBaiDuInfo(uid):
    """
    查询百度接口
    :param uid: 百度报告uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 442')
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


def test_api_78dk_platform_sys_privilege_clearUserPrivilege(uid):
    """
    清除用户权限
    :param uid: 用户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 443')
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


def test_api_78dk_platform_om_hmaw_offlineBalanceInit(contractnumber, number, pagecurrent, pagesize):
    """
    手动还款结余计算初始化
    :param contractnumber: 合同编号（Y）,string
    :param number: 期数（Y）,number
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 444')
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


def test_api_78dk_platform_om_hmaw_addRepayManualApply(actualamt, billperiod, contractuuid, optway):
    """
    添加手动还款申请
    :param actualamt: 还款金额（Y）,string
    :param billperiod: 期数（Y）,number
    :param contractuuid: 合同uuid（Y）,string
    :param optway: 还款方式（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 445')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/addRepayManualApply"
    LOGGER.info("添加手动还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["actualAmt"] = actualamt
    params["billPeriod"] = billperiod
    params["contractUuid"] = contractuuid
    params["optWay"] = optway
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
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param overduestate: 预期状态,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :param paystate: 支付状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 446')
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
    :param billperiod: 账单期数（Y）,number
    :param contractuuid: 合同UUID（Y）,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 447')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 448')
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
    :param contractnumber: 合同编号（Y）,string
    :param optway: 还款方式（Y）,string
    :param prepaymenthandlingfeeremission: 提前还款手续费 减免金额（Y）,string
    :param repayamt: 还款金额（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 449')
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
    :param contractuuid: 合同UUID （Y）,string
    :param optway: 还款方式（Y）,string
    :param reliefamt: 减免金额（Y）,string
    :param actualamt: 实际金额（Y）,string
    :param bankseqid: 银行流水编号（Y）,string
    :param remarks: 备注或意见（Y）,string
    :param urls: 图片列表（Y）,string
    :param actualrepaydate: 反款日期（N）,string
    :param prepaymenthandlingfee: 提前还款手续费（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 450')
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
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param overduestate: 预期状态,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页条数（Y）,number
    :param paystate: 还款状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 451')
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
    :param actualamt: 实际金额（Y）,string
    :param bankseqid: 银行流水编号（Y）,string
    :param billperiod: 期数（Y）,number
    :param contractuuid: 合同uuid（Y）,string
    :param optway: 还款状态（Y）,string
    :param remarks: 备注或意见（Y）,string
    :param urls: 图片路径（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 452')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 453')
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
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param overduestate: 预期状态,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页条数（Y）,number
    :param paystate: 支付状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 454')
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


def test_api_78dk_platform_tm_first_saveSupplementImage(auditchecktype, backgroundsupplementimages, contractuuid, supplementimagetype):
    """
    提交或编辑补录资料
    :param backgroundsupplementimages: 补录资料实体,array<object>
    :param contractuuid: 合同UUID,string
    :param supplementimagetype: 后台编辑或提交类型,string
    :param auditchecktype: 审核类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 455')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveSupplementImage"
    LOGGER.info("提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["backGroundSupplementImages"] = backgroundsupplementimages
    params["contractUuid"] = contractuuid
    params["supplementImageType"] = supplementimagetype
    LOGGER.info("提交或编辑补录资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交或编辑补录资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_getSupplementImages(uid):
    """
    查询用户能补录的图片资料
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 456')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getSupplementImages"
    LOGGER.info("查询用户能补录的图片资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询用户能补录的图片资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户能补录的图片资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_passContract(auditchecktype, audituuid, contractuuid, description, supplementimagerequires):
    """
    打回初审的合同(现在支持电核和终审)
    :param audituuid: 审核员UUID,string
    :param contractuuid: 合同UUID,string
    :param description: 补录说明,string
    :param supplementimagerequires: 补录资料要求实体,array<object>
    :param auditchecktype: 审核类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 457')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/passContract"
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["auditUuid"] = audituuid
    params["contractUuid"] = contractuuid
    params["description"] = description
    params["supplementImageRequires"] = supplementimagerequires
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 458')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 459')
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
    :param auditcommentattachments: 附件集合,array<object>
    :param comment: 评论内容（Y）,string
    :param contractuuid: 合同 UUID（Y）,string
    :param replyauditcommentuuid: 回复评论的UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 460')
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
    :param auditcommentattachments: 附件集合,array<object>
    :param auditcommentuuid: 评论UUID （Y）,string
    :param comment: 评论内容（Y）,string
    :param contractuuid: 合同 UUID（Y）,string
    :param replyauditcommentuuid: 回复评论的UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 461')
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


def test_api_78dk_platform_om_contract_downContracts(begindate, enddate, name, orderstate):
    """
    导出申请列表
    :param begindate: 开始时候,number
    :param enddate: 结束时间,number
    :param name: 组合查询字段,string
    :param orderstate: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 462')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    LOGGER.info("导出申请列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出申请列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_file_download(filename, urlstr):
    """
    文件下载
    :param urlstr: 文件路径,string
    :param filename: 文件名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 463')
    requesturl = baseUrl + "/api/78dk/platform/file/download"
    LOGGER.info("文件下载请求地址:【{}】".format(requesturl))
    params = dict()
    params["filename"] = filename
    params["urlStr"] = urlstr
    LOGGER.info("文件下载请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文件下载请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_viewTencentInfo(uid):
    """
    查询腾讯接口
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 464')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTencentInfo"
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


def test_api_78dk_platform_om_contract_viewTencentInfo(uid):
    """
    查询腾讯接口
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 465')
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


def test_api_78dk_platform_sys_privilege_deleteMenu(uid):
    """
    删除一个菜单
    :param uid: 数据UUId,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 466')
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
    :param name: 菜单名称（Y）,string
    :param url: 菜单路径（Y）,string
    :param platformprivilegeuuid: 菜单uuid（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 467')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 468')
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


def test_api_78dk_platform_tm_first_updateContractInfoSignState(uid):
    """
    修改合同状态为重签
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 469')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/updateContractInfoSignState"
    LOGGER.info("修改合同状态为重签请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("修改合同状态为重签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改合同状态为重签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(uid):
    """
    修改法大大合同签署状态修改为重签
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 470')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findContractInfoSignStateWeb"
    LOGGER.info("修改法大大合同签署状态修改为重签请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("修改法大大合同签署状态修改为重签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法大大合同签署状态修改为重签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_after_viewAuditMonitors(enddate, pagecurrent, pagesize, qifascore, searchwhere, startdate):
    """
    贷后列表
    :param enddate: 结束日期,string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :param qifascore: 启发分数状态,string
    :param searchwhere: 查询条件,string
    :param startdate: 开始日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 471')
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


def test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid):
    """
    删除电核资料
    :param uid: 电核资料uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 472')
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


def test_api_78dk_platform_tm_first_viewContractOperationLogs(pagecurrent, pagesize, uuid):
    """
    查询合同操作日志
    :param uuid: 合同uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 473')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 474')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 475')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 476')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 477')
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


def test_api_78dk_platform_om_contract_saveErpInfo(contractuuid, erpinfonumber):
    """
    保存合同ERP信息
    :param contractuuid: 合同 UUID,string
    :param erpinfonumber: ERP编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 478')
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


def test_api_78dk_platform_product_pmm_viewProductTemplateList(paramsingle):
    """
    根据模板类型获取具体模板信息
    :param paramsingle: 模板细分类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 479')
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


def test_api_78dk_platform_tm_after_viewReportContract(uid):
    """
    查询报告内容
    :param uid: 报告UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 480')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 481')
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


def test_api_78dk_platform_om_lm_loanOperation(bankseqid, contractuuid, loanamount, remarks, urls):
    """
    放款操作
    :param bankseqid: 银行流水,string
    :param contractuuid: 合同UUID,string
    :param loanamount: 放款金额,string
    :param remarks: 备注,string
    :param urls: 图片url,array<string>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 482')
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
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 483')
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


def test_api_78dk_platform_mm_range_deleteMerchantManagementRange(uid):
    """
    商户经营范围删除
    :param uid: 商户经营范围uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 484')
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
    :param city: 市id,number
    :param cityname: 市名称,string
    :param created: 创建时间,string
    :param merchantuuid: 商户uuid,string
    :param province: 省id,number
    :param provincename: 省名称,string
    :param updated: 更新时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 485')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 486')
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


def test_api_78dk_platform_om_contract_getErpInfoByPhone(contractuuid, phone):
    """
    根据手机号码查询ERP编号
    :param contractuuid: 合同uuid（Y）,string
    :param phone: 手机号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 487')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/getErpInfoByPhone"
    LOGGER.info("根据手机号码查询ERP编号请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["phone"] = phone
    LOGGER.info("根据手机号码查询ERP编号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据手机号码查询ERP编号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_saveSupplementImage(auditchecktype, audituuid, backgroundsupplementimages, bdid, contractnumber, contractuuid, supplementimagetype):
    """
    BD后台提交或编辑补录资料
    :param auditchecktype: 审核类型,string
    :param audituuid: 审核人员UUID,string
    :param backgroundsupplementimages: 后台补录资料实体,array<object>
    :param bdid: 业务人员唯一标识,string
    :param contractnumber: 合同编号,string
    :param contractuuid: 合同UUID,string
    :param supplementimagetype: 后台编辑或提交类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 488')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/saveSupplementImage"
    LOGGER.info("BD后台提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditCheckType"] = auditchecktype
    params["auditUuid"] = audituuid
    params["backGroundSupplementImages"] = backgroundsupplementimages
    params["bdid"] = bdid
    params["contractNumber"] = contractnumber
    params["contractUuid"] = contractuuid
    params["supplementImageType"] = supplementimagetype
    LOGGER.info("BD后台提交或编辑补录资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD后台提交或编辑补录资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_findContractList(audituuid, pagecurrent, pagesize, searchwhere):
    """
    BD查询合同信息列表
    :param audituuid: 审核人员编号,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 489')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/findContractList"
    LOGGER.info("BD查询合同信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["searchWhere"] = searchwhere
    LOGGER.info("BD查询合同信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD查询合同信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_findContractImages(audituuid, contractnumber):
    """
    BD查询影像资料
    :param contractnumber: 合同编号,string
    :param audituuid: 审核人员编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 490')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/findContractImages"
    LOGGER.info("BD查询影像资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["contractNumber"] = contractnumber
    LOGGER.info("BD查询影像资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD查询影像资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_getUploadToken():
    """
    查询七牛上传token与域名
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 491')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/getUploadToken"
    LOGGER.info("查询七牛上传token与域名请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询七牛上传token与域名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询七牛上传token与域名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_getErpInfo(uid):
    """
    查询erp系统信息
    :param uid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 492')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getErpInfo"
    LOGGER.info("查询erp系统信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uid"] = uid
    LOGGER.info("查询erp系统信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询erp系统信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_generateTransLog(audituuid, bankprocdesc, bankremark, bankseqid, cardacctname, cardaccttype, cardid, cardlinenum, cardopeningbank, contractnumber, custid, loanstatus, transamt, transname, transobj):
    """
    第三方回调接口,出账生成交易流水
    :param audituuid: 审核人员uuid（鉴权标识）,string
    :param bankprocdesc: 银行处理结果描述,string
    :param bankremark: 银行备注,string
    :param bankseqid: 银行流水号,string
    :param cardacctname: 持卡人姓名,string
    :param cardaccttype: 银行账户类型,string
    :param cardid: 银行卡号,string
    :param cardlinenum: 银联行号,string
    :param cardopeningbank: 银行名称,string
    :param contractnumber: 合同编号,string
    :param custid: 操作员标识,string
    :param loanstatus: 放款状态,string
    :param transamt: 放款金额,string
    :param transname: 交易名称,string
    :param transobj: 交易对象,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1182')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/generateTransLog"
    LOGGER.info("第三方回调接口,出账生成交易流水请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["bankProcDesc"] = bankprocdesc
    params["bankRemark"] = bankremark
    params["bankSeqId"] = bankseqid
    params["cardAcctName"] = cardacctname
    params["cardAcctType"] = cardaccttype
    params["cardId"] = cardid
    params["cardLineNum"] = cardlinenum
    params["cardOpeningBank"] = cardopeningbank
    params["contractNumber"] = contractnumber
    params["custId"] = custid
    params["loanStatus"] = loanstatus
    params["transAmt"] = transamt
    params["transName"] = transname
    params["transObj"] = transobj
    LOGGER.info("第三方回调接口,出账生成交易流水请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("第三方回调接口,出账生成交易流水请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_bdFindSupplementImageRequireLatest(audituuid, contractnumber):
    """
    bd获取需要补录的图片
    :param audituuid: 鉴权UUID,string
    :param contractnumber: 合同编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1273')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/bdFindSupplementImageRequireLatest"
    LOGGER.info("bd获取需要补录的图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["contractNumber"] = contractnumber
    LOGGER.info("bd获取需要补录的图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd获取需要补录的图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdcbdSubmitSupplementImage(audituuid, contractnumber, imagelist):
    """
    bd提交需要补录的图片
    :param audituuid: 鉴权UUID,string
    :param contractnumber: 合同编号,string
    :param imagelist: 补录图片对象集合,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1274')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdcbdSubmitSupplementImage"
    LOGGER.info("bd提交需要补录的图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["contractNumber"] = contractnumber
    params["imageList"] = imagelist
    LOGGER.info("bd提交需要补录的图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd提交需要补录的图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_sys_user_findPlatformUserProfileListByExcep():
    """
    查询例外审批人员列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1330')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/findPlatformUserProfileListByExcep"
    LOGGER.info("查询例外审批人员列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询例外审批人员列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询例外审批人员列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_trans_downTransLogList(begindate, enddate, searchwhereor, transstate, transtype):
    """
    下载交易流水
    :param searchwhereor: 查询条件,string
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param transstate: 交易状态,string
    :param transtype: 交易类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1503')
    requesturl = baseUrl + "/api/78dk/platform/om/trans/downTransLogList"
    LOGGER.info("下载交易流水请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["searchWhereOr"] = searchwhereor
    params["transState"] = transstate
    params["transType"] = transtype
    LOGGER.info("下载交易流水请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载交易流水请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_auditAuthorize(authorizeaudituseruuid, contractuuid):
    """
    初审委托
    :param authorizeaudituseruuid: 被委托人UUID,string
    :param contractuuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1562')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/auditAuthorize"
    LOGGER.info("初审委托请求地址:【{}】".format(requesturl))
    params = dict()
    params["authorizeAuditUserUuid"] = authorizeaudituseruuid
    params["contractUuid"] = contractuuid
    LOGGER.info("初审委托请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审委托请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_telephone_auditAuthorize(authorizeaudituseruuid, contractuuid):
    """
    电审委托
    :param authorizeaudituseruuid: 被委托人UUID,string
    :param contractuuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1563')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/auditAuthorize"
    LOGGER.info("电审委托请求地址:【{}】".format(requesturl))
    params = dict()
    params["authorizeAuditUserUuid"] = authorizeaudituseruuid
    params["contractUuid"] = contractuuid
    LOGGER.info("电审委托请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电审委托请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_final_auditAuthorize(authorizeaudituseruuid, contractuuid):
    """
    终审委托
    :param authorizeaudituseruuid: 被委托人UUID,string
    :param contractuuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1564')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/auditAuthorize"
    LOGGER.info("终审委托请求地址:【{}】".format(requesturl))
    params = dict()
    params["authorizeAuditUserUuid"] = authorizeaudituseruuid
    params["contractUuid"] = contractuuid
    LOGGER.info("终审委托请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审委托请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_auditing_orderAuditing_rule_approve(orderid):
    """
    审核详情_认证信息
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1804')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1805')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1806')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1807')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1808')
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


def test_api_78dk_platform_tm_first_viewUserSupplementInfo(uuid):
    """
    查询客户补充资料(new)
    :param uuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1813')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewUserSupplementInfo"
    LOGGER.info("查询客户补充资料(new)请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    LOGGER.info("查询客户补充资料(new)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询客户补充资料(new)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_editUserSupplementInfo(careertype, contractuuid, education, houseage, houseright, housetype, houseuse, id, marriage, personsupplementaryinfouuid, renovationarea, renovationcontractdate, renovationcreated, renovationtotalprice, renovationunitprice, workaddress, workage, workincome, workindustry, workname, workposition, worktel, worktype):
    """
    编辑客户补充资料(new)
    :param careertype: 职业类型,string
    :param worktype: 现工作单位类型,string
    :param education: 学历,string
    :param houseage: 房龄（年）,number
    :param houseright: 房屋产权情况,string
    :param housetype: 房产类型,string
    :param houseuse: 房产使用情况,string
    :param id: ,number
    :param marriage: 婚姻情况,string
    :param personsupplementaryinfouuid: 补充资料uuid，有--新增，无--修改，必填,string
    :param renovationarea: 装修房屋面积（平米）,string
    :param renovationcreated: 装修开始日期,string
    :param renovationtotalprice: 装修总价（元）,string
    :param renovationunitprice: 装修单价（元）,string
    :param workaddress: 现工作单位地址,string
    :param workage: 现单位工作年限,number
    :param workincome: 月收入情况,number
    :param workindustry: 工作单位所属行业,string
    :param workname: 现工作单位名称,string
    :param workposition: 职位,string
    :param worktel: 现工作单位电话,string
    :param contractuuid: 合同uuid,string
    :param renovationcontractdate: 装修合同签署日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1814')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/editUserSupplementInfo"
    LOGGER.info("编辑客户补充资料(new)请求地址:【{}】".format(requesturl))
    params = dict()
    params["careerType"] = careertype
    params["contractUuid"] = contractuuid
    params["education"] = education
    params["houseAge"] = houseage
    params["houseRight"] = houseright
    params["houseType"] = housetype
    params["houseUse"] = houseuse
    params["id"] = id
    params["marriage"] = marriage
    params["personSupplementaryInfoUuid"] = personsupplementaryinfouuid
    params["renovationArea"] = renovationarea
    params["renovationContractDate"] = renovationcontractdate
    params["renovationCreated"] = renovationcreated
    params["renovationTotalPrice"] = renovationtotalprice
    params["renovationUnitPrice"] = renovationunitprice
    params["workAddress"] = workaddress
    params["workAge"] = workage
    params["workIncome"] = workincome
    params["workIndustry"] = workindustry
    params["workName"] = workname
    params["workPosition"] = workposition
    params["workTel"] = worktel
    params["workType"] = worktype
    LOGGER.info("编辑客户补充资料(new)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑客户补充资料(new)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_bdviewUserSupplementInfo(audituuid, contractuuid):
    """
    bd客户补充资料查看
    :param audituuid: 审核人员UUID,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2160')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/bdviewUserSupplementInfo"
    LOGGER.info("bd客户补充资料查看请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["contractUuid"] = contractuuid
    LOGGER.info("bd客户补充资料查看请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd客户补充资料查看请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_jtl_bdc_bdeditUserSupplementInfo(audituuid, contractuuid, education, houseage, houseright, housetype, houseuse, id, marriage, personsupplementaryinfouuid, renovationarea, renovationcontractdate, renovationcreated, renovationtotalprice, renovationunitprice, workaddress, workage, workincome, workindustry, workname, workposition, worktel, worktype):
    """
    bd客户资料保存或修改
    :param audituuid: 审核人员UUID,string
    :param contractuuid: 合同uuid,string
    :param education: 学历,string
    :param houseage: 房龄（年）,number
    :param houseright: 房屋产权情况,string
    :param housetype: 房产类型,string
    :param houseuse: 房产使用情况,string
    :param id: ,number
    :param marriage: 婚姻情况,string
    :param personsupplementaryinfouuid: 补充资料uuid，有--新增，无--修改,string
    :param renovationarea: 装修房屋面积（平米）,string
    :param renovationcreated: 装修开始日期,string
    :param renovationtotalprice: 装修总价（元）,string
    :param renovationunitprice: 装修单价（元）,string
    :param workaddress: 现工作单位地址,string
    :param workage: 现单位工作年限,string
    :param workincome: 月收入情况,number
    :param workindustry: 工作单位所属行业,string
    :param workname: 现工作单位名称,string
    :param workposition: 职位,string
    :param worktel: 现工作单位电话,string
    :param worktype: 现工作单位类型,string
    :param renovationcontractdate: 装修合同签署日期,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2161')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/bdeditUserSupplementInfo"
    LOGGER.info("bd客户资料保存或修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditUuid"] = audituuid
    params["contractUuid"] = contractuuid
    params["education"] = education
    params["houseAge"] = houseage
    params["houseRight"] = houseright
    params["houseType"] = housetype
    params["houseUse"] = houseuse
    params["id"] = id
    params["marriage"] = marriage
    params["personSupplementaryInfoUuid"] = personsupplementaryinfouuid
    params["renovationArea"] = renovationarea
    params["renovationContractDate"] = renovationcontractdate
    params["renovationCreated"] = renovationcreated
    params["renovationTotalPrice"] = renovationtotalprice
    params["renovationUnitPrice"] = renovationunitprice
    params["workAddress"] = workaddress
    params["workAge"] = workage
    params["workIncome"] = workincome
    params["workIndustry"] = workindustry
    params["workName"] = workname
    params["workPosition"] = workposition
    params["workTel"] = worktel
    params["workType"] = worktype
    LOGGER.info("bd客户资料保存或修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("bd客户资料保存或修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


