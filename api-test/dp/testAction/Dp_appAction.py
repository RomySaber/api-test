#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Dp_appAction.py
@desc       : 项目：dp 模块：dp_app 接口方法封装
"""

from dp.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('dp_app_apiURL', 'dp')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_dp_app_login()
API_TEST_HEADERS['token'] = LICENCES


def test_login_getLoginState(tvid):
    """
    获取登陆状态接口
    :param tvid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1061')
    requesturl = baseUrl + "/login/getLoginState"
    LOGGER.info("获取登陆状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["tvid"] = tvid
    LOGGER.info("获取登陆状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取登陆状态接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_login(tvid, username, userpassword):
    """
    手机登陆接口
    :param tvid: ,string
    :param username: ,string
    :param userpassword: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1062')
    requesturl = baseUrl + "/login"
    LOGGER.info("手机登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["tvId"] = tvid
    params["userName"] = username
    params["userPassword"] = userpassword
    LOGGER.info("手机登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手机登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_logout(tvid, username):
    """
    注销登陆接口
    :param tvid: ,string
    :param username: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1063')
    requesturl = baseUrl + "/logout"
    LOGGER.info("注销登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["tvId"] = tvid
    params["userName"] = username
    params["token"] = LICENCES
    LOGGER.info("注销登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注销登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_login_getQRCodeData():
    """
    获取二维码数据接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1064')
    requesturl = baseUrl + "/login/getQRCodeData"
    LOGGER.info("获取二维码数据接口请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取二维码数据接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码数据接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getMonitorUserOrgSubList(orgparentid, userid):
    """
    获取用户分公司列表-有数据的
    :param userid: ,string
    :param orgparentid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1065')
    requesturl = baseUrl + "/monitor/getMonitorUserOrgSubList"
    LOGGER.info("获取用户分公司列表-有数据的请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgParentId"] = orgparentid
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取用户分公司列表-有数据的请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户分公司列表-有数据的请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getOrgMonitorCarList(orgid, orgtype, userid):
    """
    获取机构下车辆信息
    :param userid: ,string
    :param orgid: ,string
    :param orgtype: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1066')
    requesturl = baseUrl + "/monitor/getOrgMonitorCarList"
    LOGGER.info("获取机构下车辆信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgId"] = orgid
    params["orgType"] = orgtype
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取机构下车辆信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取机构下车辆信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getOrgMonitorCarCount(orgid, orgtype, userid):
    """
    获取机构下监控车辆统计
    :param orgid: ,string
    :param orgtype: ,string
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1067')
    requesturl = baseUrl + "/monitor/getOrgMonitorCarCount"
    LOGGER.info("获取机构下监控车辆统计请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgId"] = orgid
    params["orgType"] = orgtype
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取机构下监控车辆统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取机构下监控车辆统计请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_track_getOrgRegionWarnCarList(orgid, userid):
    """
    获取大区下报警车辆列表（含轨迹）
    :param orgid: ,number
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1068')
    requesturl = baseUrl + "/track/getOrgRegionWarnCarList"
    LOGGER.info("获取大区下报警车辆列表（含轨迹）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgId"] = orgid
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取大区下报警车辆列表（含轨迹）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取大区下报警车辆列表（含轨迹）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_system_getVersionInfo():
    """
    版本是否一致检查接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1069')
    requesturl = baseUrl + "/system/getVersionInfo"
    LOGGER.info("版本是否一致检查接口请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("版本是否一致检查接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本是否一致检查接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getLatestLocationList(userid):
    """
    实时监控-获取最新定位
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1070')
    requesturl = baseUrl + "/home/getLatestLocationList"
    LOGGER.info("实时监控-获取最新定位请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("实时监控-获取最新定位请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("实时监控-获取最新定位请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getMonitorCarCount(userid):
    """
    实时监控-获取监控车辆统计
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1071')
    requesturl = baseUrl + "/home/getMonitorCarCount"
    LOGGER.info("实时监控-获取监控车辆统计请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("实时监控-获取监控车辆统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("实时监控-获取监控车辆统计请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getWarnCarList(userid):
    """
    近七日风险车辆
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1072')
    requesturl = baseUrl + "/home/getWarnCarList"
    LOGGER.info("近七日风险车辆请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("近七日风险车辆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("近七日风险车辆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getWarnLatestList(userid):
    """
    最新报警
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1073')
    requesturl = baseUrl + "/home/getWarnLatestList"
    LOGGER.info("最新报警请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("最新报警请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("最新报警请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnlatest_getWarnLatestDetailList(orgregionid, userid):
    """
    获取大区下最新报警详情列表
    :param userid: ,number
    :param orgregionid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1074')
    requesturl = baseUrl + "/warnlatest/getWarnLatestDetailList"
    LOGGER.info("获取大区下最新报警详情列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgRegionId"] = orgregionid
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取大区下最新报警详情列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取大区下最新报警详情列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getWarnDistributionList(userid):
    """
    报警分布
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1075')
    requesturl = baseUrl + "/home/getWarnDistributionList"
    LOGGER.info("报警分布请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("报警分布请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报警分布请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getCarStatisticList(userid):
    """
    贷款增量和车辆增量
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1076')
    requesturl = baseUrl + "/home/getCarStatisticList"
    LOGGER.info("贷款增量和车辆增量请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("贷款增量和车辆增量请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款增量和车辆增量请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_home_getWarnTrendList(userid):
    """
    报警趋势
    :param userid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1077')
    requesturl = baseUrl + "/home/getWarnTrendList"
    LOGGER.info("报警趋势请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("报警趋势请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报警趋势请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_system_getIntervalFrontendConfig():
    """
    获取前端刷新频率配置
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1078')
    requesturl = baseUrl + "/system/getIntervalFrontendConfig"
    LOGGER.info("获取前端刷新频率配置请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取前端刷新频率配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取前端刷新频率配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_system_getFrontendGeneralConfig():
    """
    获取前端一般配置
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1079')
    requesturl = baseUrl + "/system/getFrontendGeneralConfig"
    LOGGER.info("获取前端一般配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("获取前端一般配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取前端一般配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_track_getTrackUserOrgRegionList(userid):
    """
    获取用户大区机构列表-有数据的
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1080')
    requesturl = baseUrl + "/track/getTrackUserOrgRegionList"
    LOGGER.info("获取用户大区机构列表-有数据的请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取用户大区机构列表-有数据的请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户大区机构列表-有数据的请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getMonitorUserOrgRegionList(userid):
    """
    获取用户大区机构列表-有数据的
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1081')
    requesturl = baseUrl + "/monitor/getMonitorUserOrgRegionList"
    LOGGER.info("获取用户大区机构列表-有数据的请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取用户大区机构列表-有数据的请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户大区机构列表-有数据的请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnlatest_getWarnUserOrgRegionList(userid):
    """
    获取用户大区机构列表-有数据的
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1082')
    requesturl = baseUrl + "/warnlatest/getWarnUserOrgRegionList"
    LOGGER.info("获取用户大区机构列表-有数据的请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取用户大区机构列表-有数据的请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户大区机构列表-有数据的请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_track_getWarnCarTrackList(carno):
    """
    获取风险车辆的轨迹
    :param carno: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1083')
    requesturl = baseUrl + "/track/getWarnCarTrackList"
    LOGGER.info("获取风险车辆的轨迹请求地址:【{}】".format(requesturl))
    params = dict()
    params["carNo"] = carno
    params["token"] = LICENCES
    LOGGER.info("获取风险车辆的轨迹请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风险车辆的轨迹请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_system_checkTokenIsValid():
    """
    检查token是否有效（用于登出等场景）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1084')
    requesturl = baseUrl + "/system/checkTokenIsValid"
    LOGGER.info("检查token是否有效（用于登出等场景）请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("检查token是否有效（用于登出等场景）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("检查token是否有效（用于登出等场景）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


