#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : YyglAction.py
@desc       : 项目：easyloan 模块：yygl 接口方法封装
"""

from easyloan.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('yygl_apiURL', 'easyloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_yygl_login()


def test_api_manage_versionManage_queryVersionLists(channelno, currentpage, pagesize):
    """
    版本列表
    :param channelno: 渠道编号(Y),string
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 673')
    requesturl = baseUrl + "/api/manage/versionManage/queryVersionLists"
    LOGGER.info("版本列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelNo"] = channelno
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    LOGGER.info("版本列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_user_login(loginid, password):
    """
    登录
    :param loginid: 账号(Y),string
    :param password: 密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 674')
    requesturl = baseUrl + "/api/manage/user/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["loginId"] = loginid
    params["password"] = password
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_versionManage_addVersion(channelno, forcedupgradedescribe, forcedupgradetitle, forcedrupgradversnumb, platform, regularupgradversnumb, regularupgradedescribe, regularupgradetitle, status, upgradeaddress, versionnumber):
    """
    版本新增
    :param channelno: 渠道编号(Y),string
    :param forcedupgradedescribe: 强制升级描述(Y),string
    :param forcedupgradetitle: 强制升级标题(Y),string
    :param forcedrupgradversnumb: 强制升级版本号(Y),string
    :param status: 是否自动发布(0否，1是)(Y),string
    :param platform: 平台（1：iOS，2：Android）(Y),string
    :param regularupgradversnumb: 普通升级版本号(Y),string
    :param regularupgradedescribe: 普通升级描述(Y),string
    :param regularupgradetitle: 普通升级标题(Y),string
    :param upgradeaddress: 升级地址(Y),string
    :param versionnumber: 展示版本号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 675')
    requesturl = baseUrl + "/api/manage/versionManage/addVersion"
    LOGGER.info("版本新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelNo"] = channelno
    params["forcedUpgradeDescribe"] = forcedupgradedescribe
    params["forcedUpgradeTitle"] = forcedupgradetitle
    params["forcedrUpgradVersNumb"] = forcedrupgradversnumb
    params["platform"] = platform
    params["regularUpgradVersNumb"] = regularupgradversnumb
    params["regularUpgradeDescribe"] = regularupgradedescribe
    params["regularUpgradeTitle"] = regularupgradetitle
    params["status"] = status
    params["upgradeAddress"] = upgradeaddress
    params["versionNumber"] = versionnumber
    LOGGER.info("版本新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_versionManage_queryVersionDetails(versionuuid):
    """
    版本详情
    :param versionuuid: 版本uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 676')
    requesturl = baseUrl + "/api/manage/versionManage/queryVersionDetails"
    LOGGER.info("版本详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["versionUuid"] = versionuuid
    LOGGER.info("版本详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_external_version_isUpgrade(mykey, channelno, currentversnumb, platform):
    """
    是否需要升级版本
    :param platform: 平台(Y),string
    :param channelno: 渠道号(Y),string
    :param currentversnumb: APP当前版本号(Y),string
    :param mykey: 在hearder里面(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 677')
    requesturl = baseUrl + "/api/external/version/isUpgrade"
    LOGGER.info("是否需要升级版本请求地址:【{}】".format(requesturl))
    params = dict()
    params["MyKey"] = mykey
    params["channelNo"] = channelno
    params["currentVersNumb"] = currentversnumb
    params["platform"] = platform
    LOGGER.info("是否需要升级版本请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("是否需要升级版本请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_versionManage_queryFlowList(currentpage, ordertype, pagesize, status, versionuuid):
    """
    版本历史-分页查询
    :param currentpage: 当前页数(Y),number
    :param ordertype: 排序方式(N),number
    :param pagesize: 每页大小(Y),number
    :param status: 发布状态(N),string
    :param versionuuid: 版本uuid(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 678')
    requesturl = baseUrl + "/api/manage/versionManage/queryFlowList"
    LOGGER.info("版本历史-分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["orderType"] = ordertype
    params["pageSize"] = pagesize
    params["status"] = status
    params["versionUuid"] = versionuuid
    LOGGER.info("版本历史-分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本历史-分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_versionManage_VersionIssue(versionuuid):
    """
    版本发布
    :param versionuuid: 版本uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 679')
    requesturl = baseUrl + "/api/manage/versionManage/VersionIssue"
    LOGGER.info("版本发布请求地址:【{}】".format(requesturl))
    params = dict()
    params["versionUuid"] = versionuuid
    LOGGER.info("版本发布请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本发布请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_versionManage_updateVersion(forcedupgradedescribe, forcedupgradetitle, forcedrupgradversnumb, regularupgradversnumb, regularupgradedescribe, regularupgradetitle, status, upgradeaddress, versionnumber, versionuuid):
    """
    版本更新
    :param forcedupgradedescribe: 强制升级描述(Y),string
    :param forcedupgradetitle: 强制升级标题(Y),string
    :param forcedrupgradversnumb: 强制升级版本号(Y),string
    :param status: 是否自动发布(0否，1是)(Y),string
    :param regularupgradversnumb: 普通升级版本号(Y),string
    :param regularupgradedescribe: 普通升级描述(Y),string
    :param regularupgradetitle: 普通升级标题(Y),string
    :param upgradeaddress: 升级地址(Y),string
    :param versionnumber: 展示版本号(Y),string
    :param versionuuid: 版本uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 680')
    requesturl = baseUrl + "/api/manage/versionManage/updateVersion"
    LOGGER.info("版本更新请求地址:【{}】".format(requesturl))
    params = dict()
    params["forcedUpgradeDescribe"] = forcedupgradedescribe
    params["forcedUpgradeTitle"] = forcedupgradetitle
    params["forcedrUpgradVersNumb"] = forcedrupgradversnumb
    params["regularUpgradVersNumb"] = regularupgradversnumb
    params["regularUpgradeDescribe"] = regularupgradedescribe
    params["regularUpgradeTitle"] = regularupgradetitle
    params["status"] = status
    params["upgradeAddress"] = upgradeaddress
    params["versionNumber"] = versionnumber
    params["versionUuid"] = versionuuid
    LOGGER.info("版本更新请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本更新请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_user_logout(mytoken):
    """
    登出
    :param mytoken: 登陆返回的用户token，存在hearder里面,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 681')
    requesturl = baseUrl + "/api/manage/user/logout"
    LOGGER.info("登出请求地址:【{}】".format(requesturl))
    params = dict()
    params["MyToken"] = mytoken
    LOGGER.info("登出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登出请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_dictionary_getAllChannels(platform):
    """
    获取所有的渠道
    :param platform: 平台（1 iOS、2 Android）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 682')
    requesturl = baseUrl + "/api/manage/dictionary/getAllChannels"
    LOGGER.info("获取所有的渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["platform"] = platform
    LOGGER.info("获取所有的渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有的渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_manage_dictionary_getChannels(platform):
    """
    获取对应平台的渠道
    :param platform: 平台（1 iOS、2 Android）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 683')
    requesturl = baseUrl + "/api/manage/dictionary/getChannels"
    LOGGER.info("获取对应平台的渠道请求地址:【{}】".format(requesturl))
    params = dict()
    params["platform"] = platform
    LOGGER.info("获取对应平台的渠道请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取对应平台的渠道请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


