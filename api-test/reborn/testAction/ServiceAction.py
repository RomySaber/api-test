#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
"""
@Time       : 2019-06-03 18:05:28
@Author     : QA 
@File       : ServiceAction.py
@desc       : 项目：reborn 模块：service 接口方法封装
"""

from reborn.testAction import loginAction
import requests, json
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent as ms
from common.myConfig import MysqlConfig


baseUrl = MysqlConfig.get('service_apiURL', 'reborn')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_service_login()
API_TEST_HEADERS['mytoken'] = LICENCES


def test_api_78dk_platform_cm_base_deleteOperator(uid):
    """
    删除渠道
    :param uid: 渠道编号uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1222')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/deleteOperator"
    LOGGER.info("删除渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_viewChannel(uid):
    """
    查询渠道
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1223')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannel"
    LOGGER.info("查询渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_saveChannel(city, name, province, region, shortname, parentchanneluuid):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1224')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/saveChannel"
    LOGGER.info("添加渠道请求地址:【{}】".format(requesturl))
    params = {"city": city, "name": name, "province": province, "region": region, "shortName": shortname, "parentChannelUuid": parentchanneluuid}
    LOGGER.info("添加渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_updateChannel(channeluuid, city, name, note, province, region, shortname, operatoruuid):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1225')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/updateChannel"
    LOGGER.info("编辑渠道请求地址:【{}】".format(requesturl))
    params = {"channelUuid": channeluuid, "city": city, "name": name, "note": note, "province": province, "region": region, "shortName": shortname, "operatorUuid": operatoruuid}
    LOGGER.info("编辑渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_examine_examine(isadopt, message, uid):
    """
    渠道审核
    :param isadopt: 是否通过(Y),boolean
    :param message: 审核人填写信息(N),string
    :param uid: 审核的渠道id(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1226')
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/examine"
    LOGGER.info("渠道审核请求地址:【{}】".format(requesturl))
    params = {"isAdopt": isadopt, "message": message, "uid": uid}
    LOGGER.info("渠道审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_viewChannels(pagesize, name, pagecurrent):
    """
    渠道列表
    :param pagesize: 每页大小(Y),string
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1227')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannels"
    LOGGER.info("渠道列表请求地址:【{}】".format(requesturl))
    params = {"pageSize": pagesize, "name": name, "pageCurrent": pagecurrent}
    LOGGER.info("渠道列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_updateFreezeState(uid, updatestate):
    """
    冻结渠道
    :param uid: 渠道id,string
    :param updatestate: 冻结状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1228')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateFreezeState"
    LOGGER.info("冻结渠道请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("冻结渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("冻结渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_updateOpenCloseState(uid, updatestate):
    """
    渠道开关
    :param uid: 渠道uuid,string
    :param updatestate: 开关状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1229')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/updateOpenCloseState"
    LOGGER.info("渠道开关请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("渠道开关请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道开关请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_examine_viewExamineChannels(name, pagecurrent, pagesize):
    """
    渠道审核列表
    :param name: 渠道名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1230')
    requesturl = baseUrl + "/api/78dk/platform/cm/examine/viewExamineChannels"
    LOGGER.info("渠道审核列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("渠道审核列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道审核列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_state_viewStateChannels(name, pagecurrent, pagesize, openclosestate, freezestate, auditstate):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1231')
    requesturl = baseUrl + "/api/78dk/platform/cm/state/viewStateChannels"
    LOGGER.info("渠道状态列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "openCloseState": openclosestate, "freezeState": freezestate, "auditState": auditstate}
    LOGGER.info("渠道状态列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("渠道状态列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_deleteBusinessInfor(uid):
    """
    删除机构
    :param uid: 删除机构的uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1232')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_viewBusinessInforByChannel(uid):
    """
    根据渠道Uid查询机构
    :param uid: 渠道uuid（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1233')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/viewBusinessInforByChannel"
    LOGGER.info("根据渠道Uid查询机构请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, channelormerchantuuid, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1234')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/saveBusinessInfor"
    LOGGER.info("添加机构请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("添加机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, channelormerchantuuid, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1235')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/business/updateBusinessInfor"
    LOGGER.info("编辑机构请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("编辑机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_deleteOperator(uid):
    """
    删除操作员
    :param uid: 渠道操作员uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1236')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/deleteOperator"
    LOGGER.info("删除操作员请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_viewOperator(uid):
    """
    查询操作员
    :param uid: 渠道操作员uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1237')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/viewOperator"
    LOGGER.info("查询操作员请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_operator_saveOperator(mail, mobile, name, password, salt, title, channelormerchantuuid):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1238')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/saveOperator"
    LOGGER.info("添加操作员请求地址:【{}】".format(requesturl))
    params = {"mail": mail, "mobile": mobile, "name": name, "password": password, "salt": salt, "title": title, "channelOrMerchantUuid": channelormerchantuuid}
    LOGGER.info("添加操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1239')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/updateOperator"
    LOGGER.info("编辑操作员请求地址:【{}】".format(requesturl))
    params = {"channelOrMerchantUuid": channelormerchantuuid, "mail": mail, "mobile": mobile, "name": name, "operatorUuid": operatoruuid, "password": password, "salt": salt, "title": title}
    LOGGER.info("编辑操作员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑操作员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_deleteClearingAccount(uid):
    """
    删除渠道结算账户信息
    :param uid: 渠道法人代表uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1240')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/deleteClearingAccount"
    LOGGER.info("删除渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(uid):
    """
    根据渠道Uid查询渠道结算
    :param uid: 渠道uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1241')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/viewClearingAccountByChannel"
    LOGGER.info("根据渠道Uid查询渠道结算请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询渠道结算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询渠道结算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1242')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/saveClearingAccount"
    LOGGER.info("添加渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("添加渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1243')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/updateClearingAccount"
    LOGGER.info("编辑渠道结算账户信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("编辑渠道结算账户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道结算账户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_deleteLegalPerson(uid):
    """
    删除渠道法人代表
    :param uid: 结算信息id(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1244')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/deleteLegalPerson"
    LOGGER.info("删除渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(uid):
    """
    根据渠道Uid查询渠道法人代表
    :param uid: 渠道UUid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1245')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/viewLegalPersonByChannel"
    LOGGER.info("根据渠道Uid查询渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据渠道Uid查询渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据渠道Uid查询渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1246')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
    LOGGER.info("添加渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("添加渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1247')
    requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/updateLegalPerson"
    LOGGER.info("编辑渠道法人代表请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("编辑渠道法人代表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑渠道法人代表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewProvinceLists(paramsingle):
    """
    省级下拉
    :param paramsingle: 查询条件(N),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1248')
    requesturl = baseUrl + "/api/78dk/platform/common/viewProvinceLists"
    LOGGER.info("省级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("省级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("省级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewRegionLists(paramsingle):
    """
    区/县级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1249')
    requesturl = baseUrl + "/api/78dk/platform/common/viewRegionLists"
    LOGGER.info("区/县级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("区/县级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("区/县级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_common_viewCityLists(paramsingle):
    """
    市级下拉
    :param paramsingle: 上级编码(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1250')
    requesturl = baseUrl + "/api/78dk/platform/common/viewCityLists"
    LOGGER.info("市级下拉请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("市级下拉请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("市级下拉请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_deleteFundSide(uid):
    """
    删除资方
    :param uid: 资方uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1251')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/deleteFundSide"
    LOGGER.info("删除资方请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_viewFundSide(uid):
    """
    查询资方
    :param uid: 资方id(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1252')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSide"
    LOGGER.info("查询资方请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_saveFundSide(name, state):
    """
    添加资方
    :param name: 资方名称(Y),string
    :param state: 资方状态(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1253')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/saveFundSide"
    LOGGER.info("添加资方请求地址:【{}】".format(requesturl))
    params = {"name": name, "state": state}
    LOGGER.info("添加资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundSide_updateFundSide(fundsideuuid, name, state):
    """
    编辑资方
    :param fundsideuuid: 资方uuid(Y),string
    :param name: 资方名称(Y),string
    :param state: 资方状态(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1254')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/updateFundSide"
    LOGGER.info("编辑资方请求地址:【{}】".format(requesturl))
    params = {"fundSideUuid": fundsideuuid, "name": name, "state": state}
    LOGGER.info("编辑资方请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑资方请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1255')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSides"
    LOGGER.info("资方列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("资方列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资方列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_deleteFundPackage(uid):
    """
    删除资金包
    :param uid: 资金包uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1256')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/deleteFundPackage"
    LOGGER.info("删除资金包请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackage(uid):
    """
    查询资金包
    :param uid: 资金包uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1257')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackage"
    LOGGER.info("查询资金包请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_saveFundPackage(amount, name, state, fundsideuuid):
    """
    添加资金包
    :param amount: 总额度(Y),number
    :param name: 资金包名称(Y),string
    :param state: 数据状态(Y),string
    :param fundsideuuid: 资方uuid(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1258')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/saveFundPackage"
    LOGGER.info("添加资金包请求地址:【{}】".format(requesturl))
    params = {"amount": amount, "name": name, "state": state, "fundSideUuid": fundsideuuid}
    LOGGER.info("添加资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_updateFundPackage(amount, fundpackageuuid, name, state, fundsideuuid):
    """
    编辑资金包
    :param amount: 总额度(Y),number
    :param fundpackageuuid: 资金包uuid(Y),string
    :param name: 资金包名称(Y),string
    :param state: 数据状态(Y),string
    :param fundsideuuid: 资方uuid,
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1259')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/updateFundPackage"
    LOGGER.info("编辑资金包请求地址:【{}】".format(requesturl))
    params = {"amount": amount, "fundPackageUuid": fundpackageuuid, "name": name, "state": state, "fundSideUuid": fundsideuuid}
    LOGGER.info("编辑资金包请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑资金包请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_fund_fundPackage_viewFundPackages(name, pagecurrent, pagesize):
    """
    资金包列表查询
    :param name: 资金包名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1260')
    requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("资金包列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_deleteProduct(uid):
    """
    删除产品模版
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1261')
    requesturl = baseUrl + "/api/78dk/platform/product/base/deleteProduct"
    LOGGER.info("删除产品模版请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_viewProductDetail(uid):
    """
    查询产品模版
    :param uid: 产品模版uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1262')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetail"
    LOGGER.info("查询产品模版请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_saveProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, firsthalfofthemonth, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state, fundpackageuuid, electroniccontracttemplateuuid, incomingpartstemplateuuid, machineaudittemplateuuid, loanmode):
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
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1263')
    requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
    LOGGER.info("添加产品模版请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle, "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee, "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth, "maxQuota": maxquota, "minQuota": minquota, "name": name, "overdueGracePeriod": overduegraceperiod, "overdueHandlingFeeRate": overduehandlingfeerate, "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs, "productState": productstate, "remark": remark, "repaymentDateType": repaymentdatetype, "repaymentMethod": repaymentmethod, "secondHalfOfTheMonth": secondhalfofthemonth, "state": state, "fundPackageUuid": fundpackageuuid, "electronicContractTemplateUuid": electroniccontracttemplateuuid, "incomingPartsTemplateUuid": incomingpartstemplateuuid, "machineAuditTemplateUuid": machineaudittemplateuuid, "loanMode": loanmode}
    LOGGER.info("添加产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_updateProduct(discountrate, earlyrepaymentfreecycle, earlyrepaymenthandlingfee, earlyrepaymentsupport, firsthalfofthemonth, maxquota, minquota, name, overduegraceperiod, overduehandlingfeerate, overdueprincipalrate, productconfigs, productdetailuuid, productstate, remark, repaymentdatetype, repaymentmethod, secondhalfofthemonth, state, fundpackageuuid, incomingpartstemplateuuid, machineaudittemplateuuid, electroniccontracttemplateuuid, loanmode):
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
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1264')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
    LOGGER.info("编辑产品模版请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle, "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee, "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth, "maxQuota": maxquota, "minQuota": minquota, "name": name, "overdueGracePeriod": overduegraceperiod, "overdueHandlingFeeRate": overduehandlingfeerate, "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs, "productDetailUuid": productdetailuuid, "productState": productstate, "remark": remark, "repaymentDateType": repaymentdatetype, "repaymentMethod": repaymentmethod, "secondHalfOfTheMonth": secondhalfofthemonth, "state": state, "fundPackageUuid": fundpackageuuid, "incomingPartsTemplateUuid": incomingpartstemplateuuid, "machineAuditTemplateUuid": machineaudittemplateuuid, "electronicContractTemplateUuid": electroniccontracttemplateuuid, "loanMode": loanmode}
    LOGGER.info("编辑产品模版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑产品模版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_viewProductDetails(name, pagecurrent, pagesize):
    """
    产品列表
    :param name: 名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1265')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetails"
    LOGGER.info("产品列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("产品列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_base_updateProductState(uuid, productstate):
    """
    修改产品状态
    :param uuid: 产品uuid,string
    :param productstate: 产品状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1266')
    requesturl = baseUrl + "/api/78dk/platform/product/base/updateProductState"
    LOGGER.info("修改产品状态请求地址:【{}】".format(requesturl))
    params = {"uuid": uuid, "productState": productstate}
    LOGGER.info("修改产品状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改产品状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1267')
    requesturl = baseUrl + "/api/78dk/platform/product/base/viewFundPackages"
    LOGGER.info("资金包列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("资金包列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资金包列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewProductTemplateList(paramsingle):
    """
    根据模板类型获取具体模板信息
    :param paramsingle: 模板细分类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1268')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductTemplateList"
    LOGGER.info("根据模板类型获取具体模板信息请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("根据模板类型获取具体模板信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据模板类型获取具体模板信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_bindProductMerchant(merchanttx, merchantuuids, productuuid):
    """
    绑定产品和商户关系
    :param merchanttx: 贴息比例,array<object>
    :param merchantuuids: 商户uuid(Y),string
    :param productuuid: 商户uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1269')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/bindProductMerchant"
    LOGGER.info("绑定产品和商户关系请求地址:【{}】".format(requesturl))
    params = {"merchantTX": merchanttx, "merchantUuids": merchantuuids, "productUuid": productuuid}
    LOGGER.info("绑定产品和商户关系请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定产品和商户关系请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_saveMerchantTX(discountrate, merchantuuid, period, productdetailconfiguuid, rate):
    """
    保存商户贴息
    :param discountrate: 商户贴息率,string
    :param merchantuuid: 商户uuid,string
    :param period: 分期数,string
    :param productdetailconfiguuid: 产品分期uuid,string
    :param rate: 月利率,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1270')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    params = {"discountRate": discountrate, "merchantUuid": merchantuuid, "period": period, "productDetailConfigUuid": productdetailconfiguuid, "rate": rate}
    LOGGER.info("保存商户贴息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存商户贴息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_findMerchantTX(merchantuuid, productuuid):
    """
    查询商户贴息
    :param merchantuuid: 商户uuid,string
    :param productuuid: 产品uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1271')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/findMerchantTX"
    LOGGER.info("查询商户贴息请求地址:【{}】".format(requesturl))
    params = {"merchantUuid": merchantuuid, "productUuid": productuuid}
    LOGGER.info("查询商户贴息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户贴息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1272')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewNotInMerchantsByPuid"
    LOGGER.info("根据产品id查询不相关的商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid}
    LOGGER.info("根据产品id查询不相关的商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品id查询不相关的商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1273')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewInMerchantsByPuid"
    LOGGER.info("根据产品id查询相关的商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid}
    LOGGER.info("根据产品id查询相关的商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品id查询相关的商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_unBindProductMerchant(merchantuuids, productuuid):
    """
    解绑产品和商户关系
    :param merchantuuids: 商户uuid,string
    :param productuuid: 产品uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1274')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/unBindProductMerchant"
    LOGGER.info("解绑产品和商户关系请求地址:【{}】".format(requesturl))
    params = {"merchantUuids": merchantuuids, "productUuid": productuuid}
    LOGGER.info("解绑产品和商户关系请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("解绑产品和商户关系请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_viewProductDetails(name, pagecurrent, pagesize):
    """
    查看产品信息列表
    :param name: ,string
    :param pagecurrent: ,number
    :param pagesize: ,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1275')
    requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductDetails"
    LOGGER.info("查看产品信息列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查看产品信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看产品信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_updateMerchant(merchantuuid, name, note, parentmerchantuuid, shortname, channeluuid):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1276')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
    LOGGER.info("修改基本信息请求地址:【{}】".format(requesturl))
    params = {"merchantUuid": merchantuuid, "name": name, "note": note, "parentMerchantUuid": parentmerchantuuid, "shortName": shortname, "channelUuid": channeluuid}
    LOGGER.info("修改基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_deleteMerchant(uid):
    """
    删除基本信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1277')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/deleteMerchant"
    LOGGER.info("删除基本信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_saveMerchant(name, note, parentmerchantuuid, shortname, channeluuid):
    """
    新增基本信息
    :param name: 商户名称(Y),string
    :param note: 商户描述/备注(N),string
    :param parentmerchantuuid: 父级商户Uuid(N),string
    :param shortname: 商户简称(Y),string
    :param channeluuid: 渠道Uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1278')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
    LOGGER.info("新增基本信息请求地址:【{}】".format(requesturl))
    params = {"name": name, "note": note, "parentMerchantUuid": parentmerchantuuid, "shortName": shortname, "channelUuid": channeluuid}
    LOGGER.info("新增基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_viewMerchant(uid):
    """
    查询基本信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1279')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
    LOGGER.info("查询基本信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_viewMerchantList(name, pagecurrent, pagesize):
    """
    查询商户列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1280')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
    LOGGER.info("查询商户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_updateFreezeState(uid, updatestate):
    """
    下架状态
    :param uid: 商户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1281')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateFreezeState"
    LOGGER.info("下架状态请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("下架状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下架状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_updateOpenCloseState(uid, updatestate):
    """
    商户归档
    :param uid: 商户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1282')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/updateOpenCloseState"
    LOGGER.info("商户归档请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("商户归档请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户归档请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_examine_merchanrExamine(ispass, message, uid):
    """
    商户审核
    :param ispass: 是否通过(Y),string
    :param message: 审核信息,string
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1283')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/merchanrExamine"
    LOGGER.info("商户审核请求地址:【{}】".format(requesturl))
    params = {"isPass": ispass, "message": message, "uid": uid}
    LOGGER.info("商户审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_examine_viewExamineMerchantList(name, pagecurrent, pagesize):
    """
    查询商户审核列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1284')
    requesturl = baseUrl + "/api/78dk/platform/mm/examine/viewExamineMerchantList"
    LOGGER.info("查询商户审核列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户审核列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户审核列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_state_viewStateMerchantList(name, pagecurrent, pagesize):
    """
    查询商户状态列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1285')
    requesturl = baseUrl + "/api/78dk/platform/mm/state/viewStateMerchantList"
    LOGGER.info("查询商户状态列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询商户状态列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询商户状态列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_saveContractImages(key, merchantuuid, url):
    """
    影像资料保存
    :param key: 图片配置key(Y),string
    :param merchantuuid: 商户Uuid(Y),string
    :param url: 图片相对URL(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1286')
    requesturl = baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存请求地址:【{}】".format(requesturl))
    params = {"key": key, "merchantUuid": merchantuuid, "url": url}
    LOGGER.info("影像资料保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_viewImageRoleList(uid, subdivisiontype):
    """
    影像资料权限
    :param uid: 商户Uuid(Y),string
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1287')
    requesturl = baseUrl + "/api/78dk/platform/mm/viewImageRoleList"
    LOGGER.info("影像资料权限请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "subdivisionType": subdivisiontype}
    LOGGER.info("影像资料权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("影像资料权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_updateBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, channelormerchantuuid, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, businessprovincename, businesscityname, businessregionname, businesscity, businessprovince, businessregion, documentcity, documentcityname, documentprovince, documentprovincename, documentregion, documentregionname):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1288')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/updateBusinessInfor"
    LOGGER.info("修改机构信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname, "businessCity": businesscity, "businessProvince": businessprovince, "businessRegion": businessregion, "documentCity": documentcity, "documentCityName": documentcityname, "documentProvince": documentprovince, "documentProvinceName": documentprovincename, "documentRegion": documentregion, "documentRegionName": documentregionname}
    LOGGER.info("修改机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_deleteBusinessInfor(uid):
    """
    删除机构信息
    :param uid: 商户机构Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1289')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/deleteBusinessInfor"
    LOGGER.info("删除机构信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_saveBusinessInfor(businessaddress, businessaddressgpsloction, businessaddresszipcode, businesshoursendtime, businesshoursstarttime, businessinformationuuid, businessregistrationnumber, channelormerchantuuid, documentaddress, email, organizationcode, socialunifiedcreditcode, storerentalendtime, storerentalstarttime, taxregistrationnumber, documentprovince, documentcity, documentregion, documentprovincename, documentcityname, documentregionname, businessprovince, businesscity, businessregion, businessprovincename, businesscityname, businessregionname):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1290')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/saveBusinessInfor"
    LOGGER.info("新增机构信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "businessAddressZipCode": businessaddresszipcode, "businessHoursEndTime": businesshoursendtime, "businessHoursStartTime": businesshoursstarttime, "businessInformationUuid": businessinformationuuid, "businessRegistrationNumber": businessregistrationnumber, "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress, "email": email, "organizationCode": organizationcode, "socialUnifiedCreditCode": socialunifiedcreditcode, "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime, "taxRegistrationNumber": taxregistrationnumber, "documentProvince": documentprovince, "documentCity": documentcity, "documentRegion": documentregion, "documentProvinceName": documentprovincename, "documentCityName": documentcityname, "documentRegionName": documentregionname, "businessProvince": businessprovince, "businessCity": businesscity, "businessRegion": businessregion, "businessProvinceName": businessprovincename, "businessCityName": businesscityname, "businessRegionName": businessregionname}
    LOGGER.info("新增机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(uid):
    """
    根据商户Uuid查询机构信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1291')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/business/viewBusinessInforByMerchant"
    LOGGER.info("根据商户Uuid查询机构信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1292')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/updateLegalPerson"
    LOGGER.info("修改法人信息请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("修改法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_deleteLegalPerson(uid):
    """
    删除法人信息
    :param uid: ,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1293')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/deleteLegalPerson"
    LOGGER.info("删除法人信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1294')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/saveLegalPerson"
    LOGGER.info("新增法人信息请求地址:【{}】".format(requesturl))
    params = {"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid, "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name}
    LOGGER.info("新增法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(uid):
    """
    根据商户Uuid查询法人信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1295')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/viewLegalPersonByMerchant"
    LOGGER.info("根据商户Uuid查询法人信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1296')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/updateClearingAccount"
    LOGGER.info("修改结算信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("修改结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_deleteClearingAccount(uid):
    """
    删除结算信息
    :param uid: 商户结算Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1297')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/deleteClearingAccount"
    LOGGER.info("删除结算信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1298')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/saveClearingAccount"
    LOGGER.info("新增结算信息请求地址:【{}】".format(requesturl))
    params = {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank, "accountType": accounttype, "branchName": branchname, "chamberlainIdCard": chamberlainidcard, "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid, "lineNumber": linenumber, "phone": phone, "province": province, "region": region}
    LOGGER.info("新增结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(uid):
    """
    根据商户Uuid查询结算信息
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1299')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/viewClearingAccountByMerchant"
    LOGGER.info("根据商户Uuid查询结算信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询结算信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询结算信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_updateStore(businessaddress, businessaddressgpsloction, managername, managerphone, merchantuuid, stormuuid, province, city, region, provincename, cityname, regionname, storename):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1300')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStore"
    LOGGER.info("修改门店信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "managerName": managername, "managerPhone": managerphone, "merchantUuid": merchantuuid, "stormUuid": stormuuid, "province": province, "city": city, "region": region, "provinceName": provincename, "cityName": cityname, "regionName": regionname, "storeName": storename}
    LOGGER.info("修改门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_deleteStore(uid):
    """
    删除门店信息
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1301')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteStore"
    LOGGER.info("删除门店信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_saveStore(businessaddress, businessaddressgpsloction, managername, managerphone, merchantuuid, stormuuid, storename, province, city, region, provincename, cityname, regionname):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1302')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
    LOGGER.info("新增门店信息请求地址:【{}】".format(requesturl))
    params = {"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction, "managerName": managername, "managerPhone": managerphone, "merchantUuid": merchantuuid, "stormUuid": stormuuid, "storeName": storename, "province": province, "city": city, "region": region, "provinceName": provincename, "cityName": cityname, "regionName": regionname}
    LOGGER.info("新增门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_viewStore(uid):
    """
    查询门店信息
    :param uid: 门店Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1303')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStore"
    LOGGER.info("查询门店信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_viewStoreList(name, pagecurrent, pagesize):
    """
    查询门店列表
    :param name: 商户Uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1304')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
    LOGGER.info("查询门店列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_base_store_uploadQrcode(storeuuid):
    """
    下载门店二维码
    :param storeuuid: 门店uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1305')
    requesturl = baseUrl + "/api/78dk/platform/mm/base/store/uploadQrcode"
    LOGGER.info("下载门店二维码请求地址:【{}】".format(requesturl))
    params = {"storeUuid": storeuuid}
    LOGGER.info("下载门店二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载门店二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_merchantMoneyEnlarge(uid, zoomcoefficient):
    """
    修改预授信放大系数
    :param uid: 商户额度Uuid(Y),string
    :param zoomcoefficient: 预授信额度放大系数(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1306')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/merchantMoneyEnlarge"
    LOGGER.info("修改预授信放大系数请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("修改预授信放大系数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改预授信放大系数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1307')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
    LOGGER.info("修改额度管理请求地址:【{}】".format(requesturl))
    params = {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum, "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("修改额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_deleteMerchantMoney(uid):
    """
    删除额度管理
    :param uid: 商户额度Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1308')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/deleteMerchantMoney"
    LOGGER.info("删除额度管理请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1309')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
    LOGGER.info("新增额度管理请求地址:【{}】".format(requesturl))
    params = {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum, "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient}
    LOGGER.info("新增额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(uid):
    """
    根据商户Uuid查询额度管理
    :param uid: 商户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1310')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyByMerchant"
    LOGGER.info("根据商户Uuid查询额度管理请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("根据商户Uuid查询额度管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据商户Uuid查询额度管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_money_viewMerchantMoneyList(name, pagecurrent, pagesize):
    """
    风险控制列表
    :param name: 商户名称(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1311')
    requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyList"
    LOGGER.info("风险控制列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("风险控制列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风险控制列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_range_deleteMerchantManagementRange(uid):
    """
    商户经营范围删除
    :param uid: 商户经营范围uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1312')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/deleteMerchantManagementRange"
    LOGGER.info("商户经营范围删除请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("商户经营范围删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户经营范围删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1313')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/addMerchantManagementRange"
    LOGGER.info("商户经营范围新增请求地址:【{}】".format(requesturl))
    params = {"city": city, "cityName": cityname, "created": created, "merchantUuid": merchantuuid, "province": province, "provinceName": provincename, "updated": updated}
    LOGGER.info("商户经营范围新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户经营范围新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_range_findMMRByMerchantUuid(uid):
    """
    通过商户uuid查询商户经营范围
    :param uid: 商户的uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1314')
    requesturl = baseUrl + "/api/78dk/platform/mm/range/findMMRByMerchantUuid"
    LOGGER.info("通过商户uuid查询商户经营范围请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("通过商户uuid查询商户经营范围请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过商户uuid查询商户经营范围请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(platformprivilegeuuid, platformuseruuid):
    """
    新增/修改权限
    :param platformprivilegeuuid: 权限UUid(Y),string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1315')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
    LOGGER.info("新增/修改权限请求地址:【{}】".format(requesturl))
    params = {"platformPrivilegeUuid": platformprivilegeuuid, "platformUserUuid": platformuseruuid}
    LOGGER.info("新增/修改权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增/修改权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(permissiontype, platformuseruuid):
    """
    查询权限
    :param permissiontype: 权限类型,string
    :param platformuseruuid: 用户UUid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1316')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewUserPrivilegeList"
    LOGGER.info("查询权限请求地址:【{}】".format(requesturl))
    params = {"permissionType": permissiontype, "platformUserUuid": platformuseruuid}
    LOGGER.info("查询权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_clearUserPrivilege(uid):
    """
    清除用户权限
    :param uid: 用户uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1317')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/clearUserPrivilege"
    LOGGER.info("清除用户权限请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("清除用户权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("清除用户权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_deleteMenu(uid):
    """
    删除一个菜单
    :param uid: 数据UUId,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1318')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/deleteMenu"
    LOGGER.info("删除一个菜单请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除一个菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一个菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_saveMenu(name, url, platformprivilegeuuid):
    """
    保存一个菜单
    :param name: 菜单名称（Y）,string
    :param url: 菜单路径（Y）,string
    :param platformprivilegeuuid: 菜单uuid（N）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1319')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveMenu"
    LOGGER.info("保存一个菜单请求地址:【{}】".format(requesturl))
    params = {"name": name, "url": url, "platformPrivilegeUuid": platformprivilegeuuid}
    LOGGER.info("保存一个菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存一个菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_privilege_viewMenus(paramsingle):
    """
    查询所有菜单
    :param paramsingle: 菜单类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1320')
    requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewMenus"
    LOGGER.info("查询所有菜单请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("查询所有菜单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询所有菜单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1321')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUser"
    LOGGER.info("修改用户请求地址:【{}】".format(requesturl))
    params = {"email": email, "mobile": mobile, "name": name, "platformUserProfileUuid": platformuserprofileuuid}
    LOGGER.info("修改用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_deleteSystemUser(uid):
    """
    删除用户
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1322')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/deleteSystemUser"
    LOGGER.info("删除用户请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_saveSystemUser(email, mobile, name):
    """
    新增用户
    :param email: 用户邮箱(Y),string
    :param mobile: 用户手机(Y),string
    :param name: 用户姓名(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1323')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/saveSystemUser"
    LOGGER.info("新增用户请求地址:【{}】".format(requesturl))
    params = {"email": email, "mobile": mobile, "name": name}
    LOGGER.info("新增用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUser(paramsingle):
    """
    查询用户
    :param paramsingle: 用户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1324')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUser"
    LOGGER.info("查询用户请求地址:【{}】".format(requesturl))
    params = {"paramSingle": paramsingle}
    LOGGER.info("查询用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_login(email, password):
    """
    用户登陆
    :param email: 用户帐户(Y),string
    :param password: 用户密码(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1325')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = {"email": email, "password": password}
    LOGGER.info("用户登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_viewSystemUserList(name, pagecurrent, pagesize):
    """
    查询用户列表
    :param name: 用户姓名(N),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 分页大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1326')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUserList"
    LOGGER.info("查询用户列表请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询用户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_resetUserPass(uid):
    """
    重置密码
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1327')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/resetUserPass"
    LOGGER.info("重置密码请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("重置密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重置密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_updateSystemUserState(uid, updatestate):
    """
    状态修改
    :param uid: 用户Uuid(Y),string
    :param updatestate: 修改状态(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1328')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUserState"
    LOGGER.info("状态修改请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "updateState": updatestate}
    LOGGER.info("状态修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("状态修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_sys_user_updateUserPass(passwordrepeat, email, password, uid):
    """
    修改密码
    :param passwordrepeat: 用户密码重复(N),string
    :param email: 用户邮箱(Y),string
    :param password: 用户密码(Y),string
    :param uid: 用户Uuid(Y),string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1329')
    requesturl = baseUrl + "/api/78dk/platform/sys/user/updateUserPass"
    LOGGER.info("修改密码请求地址:【{}】".format(requesturl))
    params = {"passwordRepeat": passwordrepeat, "email": email, "password": password, "uid": uid}
    LOGGER.info("修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_FileUploadController_handlerFileUpload():
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1330')
    requesturl = baseUrl + "/FileUploadController/handlerFileUpload"
    LOGGER.info("图片上传请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("图片上传请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("图片上传请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_firstCheck(message, uuid, checkstate):
    """
    初审
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1331')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/firstCheck"
    LOGGER.info("初审请求地址:【{}】".format(requesturl))
    params = {"message": message, "uuid": uuid, "checkState": checkstate}
    LOGGER.info("初审请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContract(uid):
    """
    初审信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1332')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
    LOGGER.info("初审信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("初审信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewFirstCheckContracts(name, pagecurrent, pagesize, state):
    """
    初审列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1333')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
    LOGGER.info("初审列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("初审列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初审列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewTongdunInfo(uid):
    """
    同盾信息查询
    :param uid: 同盾uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1334')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("同盾信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewImageDataConfig(subdivisiontype):
    """
    查询影像列表
    :param subdivisiontype: 产品类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1335')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewImageDataConfig"
    LOGGER.info("查询影像列表请求地址:【{}】".format(requesturl))
    params = {"subdivisionType": subdivisiontype}
    LOGGER.info("查询影像列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询影像列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_selectCanAuditCheck(uid, checktype):
    """
    是否有权限审核
    :param uid: 合同uuid,string
    :param checktype: 数据类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1336')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/selectCanAuditCheck"
    LOGGER.info("是否有权限审核请求地址:【{}】".format(requesturl))
    params = {"uid": uid, "checkType": checktype}
    LOGGER.info("是否有权限审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("是否有权限审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewBaiDuInfo(uid):
    """
    查询百度接口
    :param uid: 百度uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1337')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewBaiDuInfo"
    LOGGER.info("查询百度接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询百度接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询百度接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_saveSupplementImage(backgroundsupplementimages, contractuuid, supplementimagetype, auditchecktype):
    """
    提交或编辑补录资料
    :param backgroundsupplementimages: 补录资料实体,array<object>
    :param contractuuid: 合同UUID,string
    :param supplementimagetype: 后台编辑或提交类型,string
    :param auditchecktype: 审核类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1338')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/saveSupplementImage"
    LOGGER.info("提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = {"backGroundSupplementImages": backgroundsupplementimages, "contractUuid": contractuuid, "supplementImageType": supplementimagetype, "auditCheckType": auditchecktype}
    LOGGER.info("提交或编辑补录资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交或编辑补录资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_getSupplementImages(uid):
    """
    查询用户能补录的图片资料
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1339')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getSupplementImages"
    LOGGER.info("查询用户能补录的图片资料请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询用户能补录的图片资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户能补录的图片资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_passContract(audituuid, contractuuid, description, supplementimagerequires, auditchecktype):
    """
    打回初审的合同(现在支持电核和终审)
    :param audituuid: 审核员UUID,string
    :param contractuuid: 合同UUID,string
    :param description: 补录说明,string
    :param supplementimagerequires: 补录资料要求实体,array<object>
    :param auditchecktype: 审核类型,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1340')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/passContract"
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求地址:【{}】".format(requesturl))
    params = {"auditUuid": audituuid, "contractUuid": contractuuid, "description": description, "supplementImageRequires": supplementimagerequires, "auditCheckType": auditchecktype}
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("打回初审的合同(现在支持电核和终审)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_delAuditComment(uid):
    """
    删除一条评论
    :param uid: 评论uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1341')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/delAuditComment"
    LOGGER.info("删除一条评论请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_findAuditCommentList(contractuuid, pagecurrent, pagesize):
    """
    查询评论列表
    :param contractuuid: 合同 UUID,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1342')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findAuditCommentList"
    LOGGER.info("查询评论列表请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询评论列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询评论列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1343')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addAuditComment"
    LOGGER.info("添加一条评论请求地址:【{}】".format(requesturl))
    params = {"auditCommentAttachments": auditcommentattachments, "comment": comment, "contractUuid": contractuuid, "replyAuditCommentUuid": replyauditcommentuuid}
    LOGGER.info("添加一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1344')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/editAuditComment"
    LOGGER.info("编辑一条评论请求地址:【{}】".format(requesturl))
    params = {"auditCommentAttachments": auditcommentattachments, "auditCommentUuid": auditcommentuuid, "comment": comment, "contractUuid": contractuuid, "replyAuditCommentUuid": replyauditcommentuuid}
    LOGGER.info("编辑一条评论请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑一条评论请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewTencentInfo(uid):
    """
    查询腾讯接口
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1345')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTencentInfo"
    LOGGER.info("查询腾讯接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询腾讯接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询腾讯接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_updateContractInfoSignState(uid):
    """
    修改合同状态为重签
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1346')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/updateContractInfoSignState"
    LOGGER.info("修改合同状态为重签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("修改合同状态为重签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改合同状态为重签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(uid):
    """
    修改法大大合同签署状态 修改为重签
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1347')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/findContractInfoSignStateWeb"
    LOGGER.info("修改法大大合同签署状态 修改为重签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("修改法大大合同签署状态 修改为重签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改法大大合同签署状态 修改为重签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogs(uuid, pagecurrent, pagesize):
    """
    查询合同操作日志
    :param uuid: 合同uuid(Y),string
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1348')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogs"
    LOGGER.info("查询合同操作日志请求地址:【{}】".format(requesturl))
    params = {"uuid": uuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("查询合同操作日志请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同操作日志请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_deleteContractCustomerLabel(uid):
    """
    删除客户标签
    :param uid: 标签uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1349')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/deleteContractCustomerLabel"
    LOGGER.info("删除客户标签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_addContractCustomerLabel(contractuuid, labelcontent):
    """
    新增客户标签
    :param contractuuid: 合同 uuid,string
    :param labelcontent: 标签内容,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1350')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/addContractCustomerLabel"
    LOGGER.info("新增客户标签请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "labelContent": labelcontent}
    LOGGER.info("新增客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractLabels(uid):
    """
    通过合同UUID查询对应的客户标签
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1351')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractLabels"
    LOGGER.info("通过合同UUID查询对应的客户标签请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("通过合同UUID查询对应的客户标签请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过合同UUID查询对应的客户标签请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_viewContractOperationLogInfo(contractoperationloguuid, contractuuid):
    """
    查询操作日志详情
    :param contractoperationloguuid: 操作记录UUID,string
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1352')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/viewContractOperationLogInfo"
    LOGGER.info("查询操作日志详情请求地址:【{}】".format(requesturl))
    params = {"contractOperationLogUuid": contractoperationloguuid, "contractUuid": contractuuid}
    LOGGER.info("查询操作日志详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询操作日志详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_first_getErpInfo(uid):
    """
    查询erp系统信息
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1353')
    requesturl = baseUrl + "/api/78dk/platform/tm/first/getErpInfo"
    LOGGER.info("查询erp系统信息请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询erp系统信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询erp系统信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_telephoneCheck(checkstate, message, uuid):
    """
    电核
    :param checkstate: 审核状态,string
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1354')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/telephoneCheck"
    LOGGER.info("电核请求地址:【{}】".format(requesturl))
    params = {"checkState": checkstate, "message": message, "uuid": uuid}
    LOGGER.info("电核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid):
    """
    电核信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1355')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
    LOGGER.info("电核信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("电核信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(name, pagecurrent, pagesize, state):
    """
    电核列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1356')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContracts"
    LOGGER.info("电核列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("电核列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("电核列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(answer, contractuuid, groupname, question, risktype, state, telephonecheckfeedbackuuid, groupsort, questionsort):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1357')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/addTelephoneCheckInfos"
    LOGGER.info("批量添加电核资料请求地址:【{}】".format(requesturl))
    params = {"answer": answer, "contractUuid": contractuuid, "groupName": groupname, "question": question, "riskType": risktype, "state": state, "telephoneCheckFeedbackUuid": telephonecheckfeedbackuuid, "groupSort": groupsort, "questionSort": questionsort}
    LOGGER.info("批量添加电核资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("批量添加电核资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(uid):
    """
    查询合同已经填写的电核问题列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1358')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询合同已经填写的电核问题列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid):
    """
    删除电核资料
    :param uid: 电核资料uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1359')
    requesturl = baseUrl + "/api/78dk/platform/tm/telephone/deleteTelephoneCheckInfo"
    LOGGER.info("删除电核资料请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("删除电核资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除电核资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFDDInfo(uid):
    """
    法大大信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1360')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("法大大信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_finalCheck(message, uuid, checkstate):
    """
    终审
    :param message: 审核人提交信息,string
    :param uuid: 合同uuid,string
    :param checkstate: 审核状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1361')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/finalCheck"
    LOGGER.info("终审请求地址:【{}】".format(requesturl))
    params = {"message": message, "uuid": uuid, "checkState": checkstate}
    LOGGER.info("终审请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContract(uid):
    """
    终审信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1362')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContract"
    LOGGER.info("终审信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("终审信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_final_viewFinalCheckContracts(name, pagecurrent, pagesize, state):
    """
    终审列表查询
    :param name: 编号等一系列东西,string
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param state: 状态,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1363')
    requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
    LOGGER.info("终审列表查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state}
    LOGGER.info("终审列表查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("终审列表查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1364')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewAuditMonitors"
    LOGGER.info("贷后列表请求地址:【{}】".format(requesturl))
    params = {"endDate": enddate, "pageCurrent": pagecurrent, "pageSize": pagesize, "qifaScore": qifascore, "searchWhere": searchwhere, "startDate": startdate}
    LOGGER.info("贷后列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷后列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_after_viewReportContract(uid):
    """
    查询报告内容
    :param uid: 报告UUID,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1365')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewReportContract"
    LOGGER.info("查询报告内容请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询报告内容请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询报告内容请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_tm_after_viewContractTongDuns(uid):
    """
    查询贷后所用同盾报告列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1366')
    requesturl = baseUrl + "/api/78dk/platform/tm/after/viewContractTongDuns"
    LOGGER.info("查询贷后所用同盾报告列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询贷后所用同盾报告列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询贷后所用同盾报告列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewContracts(name, pagecurrent, pagesize, begindate, enddate, orderstate):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1367')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContracts"
    LOGGER.info("合同列表查询（申请列表）请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "begindate": begindate, "enddate": enddate, "orderState": orderstate}
    LOGGER.info("合同列表查询（申请列表）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同列表查询（申请列表）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewContract(uid):
    """
    合同详情查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1368')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewContract"
    LOGGER.info("合同详情查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("合同详情查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同详情查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTongdunInfo(uid):
    """
    同盾信息查询
    :param uid: 同盾id,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1369')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTongdunInfo"
    LOGGER.info("同盾信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("同盾信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同盾信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewFDDInfo(uid):
    """
    法大大信息查询
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1370')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewFDDInfo"
    LOGGER.info("法大大信息查询请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("法大大信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewUserBill(name, pagecurrent, pagesize):
    """
    账单信息查询
    :param name: 编号什么的,string
    :param pagecurrent: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1371')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewUserBill"
    LOGGER.info("账单信息查询请求地址:【{}】".format(requesturl))
    params = {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("账单信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid):
    """
    查询合同已经填写的电核问题列表
    :param uid: 合同uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1372')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTelephoneCheckInfosByContractUuid"
    LOGGER.info("查询合同已经填写的电核问题列表请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询合同已经填写的电核问题列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询合同已经填写的电核问题列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewBaiDuInfo(uid):
    """
    查询百度接口
    :param uid: 百度报告uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1373')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewBaiDuInfo"
    LOGGER.info("查询百度接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询百度接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询百度接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1374')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "name": name, "orderState": orderstate}
    LOGGER.info("导出申请列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出申请列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_viewTencentInfo(uid):
    """
    查询腾讯接口
    :param uid: 腾讯uuid,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1375')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/viewTencentInfo"
    LOGGER.info("查询腾讯接口请求地址:【{}】".format(requesturl))
    params = {"uid": uid}
    LOGGER.info("查询腾讯接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询腾讯接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_saveErpInfo(contractuuid, erpinfonumber):
    """
    保存合同ERP信息
    :param contractuuid: 合同 UUID,string
    :param erpinfonumber: ERP编号,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1376')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/saveErpInfo"
    LOGGER.info("保存合同ERP信息请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "erpInfoNumber": erpinfonumber}
    LOGGER.info("保存合同ERP信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存合同ERP信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_contract_getErpInfoByPhone(contractuuid, phone):
    """
    根据手机号码查询ERP编号
    :param contractuuid: 合同uuid（Y）,string
    :param phone: 手机号（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1377')
    requesturl = baseUrl + "/api/78dk/platform/om/contract/getErpInfoByPhone"
    LOGGER.info("根据手机号码查询ERP编号请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "phone": phone}
    LOGGER.info("根据手机号码查询ERP编号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据手机号码查询ERP编号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_trans_findTransLogList(enddate, pagecurrent, pagesize, searchwhere, begindate, transstate, transtype):
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1378')
    requesturl = baseUrl + "/api/78dk/platform/om/trans/findTransLogList"
    LOGGER.info("交易流水列表请求地址:【{}】".format(requesturl))
    params = {"enddate": enddate, "pageCurrent": pagecurrent, "pageSize": pagesize, "searchWhere": searchwhere, "begindate": begindate, "transState": transstate, "transType": transtype}
    LOGGER.info("交易流水列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("交易流水列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_offlineBalanceInit(contractnumber, number, pagecurrent, pagesize):
    """
    手动还款 结余计算 初始化
    :param contractnumber: 合同编号（Y）,string
    :param number: 期数（Y）,number
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1379')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/offlineBalanceInit"
    LOGGER.info("手动还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "number": number, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("手动还款 结余计算 初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动还款 结余计算 初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_addRepayManualApply(actualamt, billperiod, contractuuid, optway):
    """
    添加 手动还款申请
    :param actualamt: 还款金额（Y）,string
    :param billperiod: 期数（Y）,number
    :param contractuuid: 合同uuid（Y）,string
    :param optway: 还款方式（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1380')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/addRepayManualApply"
    LOGGER.info("添加 手动还款申请请求地址:【{}】".format(requesturl))
    params = {"actualAmt": actualamt, "billPeriod": billperiod, "contractUuid": contractuuid, "optWay": optway}
    LOGGER.info("添加 手动还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加 手动还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    """
    获取 手动扣款 列表
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param overduestate: 预期状态,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :param paystate: 支付状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1381')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findRepayCommons"
    LOGGER.info("获取 手动扣款 列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取 手动扣款 列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取 手动扣款 列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_hmaw_findManuelHistoryList(billperiod, contractuuid, pagecurrent, pagesize):
    """
    获取 手动扣款历史记录
    :param billperiod: 账单期数（Y）,number
    :param contractuuid: 合同UUID（Y）,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页行数（Y）,number
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1382')
    requesturl = baseUrl + "/api/78dk/platform/om/hmaw/findManuelHistoryList"
    LOGGER.info("获取 手动扣款历史记录请求地址:【{}】".format(requesturl))
    params = {"billPeriod": billperiod, "contractUuid": contractuuid, "pageCurrent": pagecurrent, "pageSize": pagesize}
    LOGGER.info("获取 手动扣款历史记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取 手动扣款历史记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceInit(contractnumber):
    """
    提前还款 结余计算 初始化
    :param contractnumber: 合同编号（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1383')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceInit"
    LOGGER.info("提前还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber}
    LOGGER.info("提前还款 结余计算 初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还款 结余计算 初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_adaw_prepaymentBalanceRefresh(contractnumber, optway, prepaymenthandlingfeeremission, repayamt):
    """
    提前还款 结余计算 刷新接口
    :param contractnumber: 合同编号（Y）,string
    :param optway: 还款方式（Y）,string
    :param prepaymenthandlingfeeremission: 提前还款手续费 减免金额（Y）,string
    :param repayamt: 还款金额（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1384')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/adaw/prepaymentBalanceRefresh"
    LOGGER.info("提前还款 结余计算 刷新接口请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "optWay": optway, "prepaymentHandlingFeeRemission": prepaymenthandlingfeeremission, "repayAmt": repayamt}
    LOGGER.info("提前还款 结余计算 刷新接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还款 结余计算 刷新接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_adaw_addRepayManualApply(contractuuid, optway, reliefamt, actualamt, bankseqid, remarks, urls, actualrepaydate, prepaymenthandlingfee):
    """
    添加 提前还款申请
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1385')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/addRepayManualApply"
    LOGGER.info("添加 提前还款申请请求地址:【{}】".format(requesturl))
    params = {"contractUuid": contractuuid, "optWay": optway, "reliefAmt": reliefamt, "actualAmt": actualamt, "bankSeqId": bankseqid, "remarks": remarks, "urls": urls, "actualRepayDate": actualrepaydate, "prepaymentHandlingFee": prepaymenthandlingfee}
    LOGGER.info("添加 提前还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加 提前还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1386')
    requesturl = baseUrl + "/api/78dk/platform/om/adaw/findRepayPrepayments"
    LOGGER.info("获取提前还款列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取提前还款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取提前还款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_addRepayManualApply(actualamt, bankseqid, billperiod, contractuuid, optway, remarks, urls):
    """
    添加 线下还款申请
    :param actualamt: 实际金额（Y）,string
    :param bankseqid: 银行流水编号（Y）,string
    :param billperiod: 期数（Y）,number
    :param contractuuid: 合同uuid（Y）,string
    :param optway: 还款状态（Y）,string
    :param remarks: 备注或意见（Y）,string
    :param urls: 图片路径（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1387')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/addRepayManualApply"
    LOGGER.info("添加 线下还款申请请求地址:【{}】".format(requesturl))
    params = {"actualAmt": actualamt, "bankSeqId": bankseqid, "billPeriod": billperiod, "contractUuid": contractuuid, "optWay": optway, "remarks": remarks, "urls": urls}
    LOGGER.info("添加 线下还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加 线下还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_offlineBalanceInit(contractnumber, number):
    """
    线下还款 结余计算 初始化
    :param contractnumber: 合同编号（Y）,string
    :param number: 期数（Y）,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1388')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/offlineBalanceInit"
    LOGGER.info("线下还款 结余计算 初始化请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "number": number}
    LOGGER.info("线下还款 结余计算 初始化请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线下还款 结余计算 初始化请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_ulaw_findRepayCommons(begindate, enddate, overduestate, pagecurrent, pagesize, paystate, searchwhereor):
    """
    获取 线下还款列表
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param overduestate: 预期状态,string
    :param pagecurrent: 页码（Y）,number
    :param pagesize: 每页条数（Y）,number
    :param paystate: 支付状态,string
    :param searchwhereor: 文字信息,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1389')
    requesturl = baseUrl + "/api/78dk/platform/om/ulaw/findRepayCommons"
    LOGGER.info("获取 线下还款列表请求地址:【{}】".format(requesturl))
    params = {"begindate": begindate, "enddate": enddate, "overdueState": overduestate, "pageCurrent": pagecurrent, "pageSize": pagesize, "payState": paystate, "searchWhereOr": searchwhereor}
    LOGGER.info("获取 线下还款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取 线下还款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1390')
    requesturl = baseUrl + "/api/78dk/platform/om/lm/loanOperation"
    LOGGER.info("放款操作请求地址:【{}】".format(requesturl))
    params = {"bankSeqId": bankseqid, "contractUuid": contractuuid, "loanAmount": loanamount, "remarks": remarks, "urls": urls}
    LOGGER.info("放款操作请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款操作请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_om_lm_findLoanModeList(pagecurrent, pagesize, searchwhere):
    """
    查询线下放款列表
    :param pagecurrent: 当前页,number
    :param pagesize: 页面大小,number
    :param searchwhere: 查询条件,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1391')
    requesturl = baseUrl + "/api/78dk/platform/om/lm/findLoanModeList"
    LOGGER.info("查询线下放款列表请求地址:【{}】".format(requesturl))
    params = {"pageCurrent": pagecurrent, "pageSize": pagesize, "searchWhere": searchwhere}
    LOGGER.info("查询线下放款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询线下放款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_file_download(urlstr, filename):
    """
    文件下载
    :param urlstr: 文件路径,string
    :param filename: 文件名称,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1392')
    requesturl = baseUrl + "/api/78dk/platform/file/download"
    LOGGER.info("文件下载请求地址:【{}】".format(requesturl))
    params = {"urlStr": urlstr, "filename": filename}
    LOGGER.info("文件下载请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文件下载请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1393')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/saveSupplementImage"
    LOGGER.info("BD后台提交或编辑补录资料请求地址:【{}】".format(requesturl))
    params = {"auditCheckType": auditchecktype, "auditUuid": audituuid, "backGroundSupplementImages": backgroundsupplementimages, "bdid": bdid, "contractNumber": contractnumber, "contractUuid": contractuuid, "supplementImageType": supplementimagetype}
    LOGGER.info("BD后台提交或编辑补录资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD后台提交或编辑补录资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1394')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/findContractList"
    LOGGER.info("BD查询合同信息列表请求地址:【{}】".format(requesturl))
    params = {"auditUuid": audituuid, "pageCurrent": pagecurrent, "pageSize": pagesize, "searchWhere": searchwhere}
    LOGGER.info("BD查询合同信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD查询合同信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_jtl_bdc_findContractImages(contractnumber, audituuid):
    """
    BD查询影像资料
    :param contractnumber: 合同编号,string
    :param audituuid: 审核人员编号,string
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1395')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/findContractImages"
    LOGGER.info("BD查询影像资料请求地址:【{}】".format(requesturl))
    params = {"contractNumber": contractnumber, "auditUuid": audituuid}
    LOGGER.info("BD查询影像资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("BD查询影像资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_jtl_bdc_getUploadToken():
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1396')
    requesturl = baseUrl + "/api/78dk/platform/jtl/bdc/getUploadToken"
    LOGGER.info("查询七牛上传token与域名请求地址:【{}】".format(requesturl))
    params = {}
    LOGGER.info("查询七牛上传token与域名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询七牛上传token与域名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


