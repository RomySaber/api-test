#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Dp_webAction.py
@desc       : 项目：dp 模块：dp_web 接口方法封装
"""

from dp.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('dp_web_apiURL', 'dp')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_dp_web_login()
API_TEST_HEADERS['token'] = LICENCES


def test_login(username, userpassword):
    """
    登陆
    :param username: ,string
    :param userpassword: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1085')
    requesturl = baseUrl + "/login"
    LOGGER.info("登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["userName"] = username
    params["userPassword"] = userpassword
    LOGGER.info("登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_updateAppUser(address, id, linkman, mobile, remark, username, userpassword):
    """
    App用户修改
    :param address: ,string
    :param linkman: ,string
    :param mobile: ,string
    :param remark: ,string
    :param username: ,string
    :param userpassword: ,string
    :param id: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1086')
    requesturl = baseUrl + "/appuser/updateAppUser"
    LOGGER.info("App用户修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["id"] = id
    params["linkman"] = linkman
    params["mobile"] = mobile
    params["remark"] = remark
    params["userName"] = username
    params["userPassword"] = userpassword
    params["token"] = LICENCES
    LOGGER.info("App用户修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("App用户修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_addAppUser(address, linkman, mobile, remark, username, userpassword):
    """
    App用户新增
    :param address: ,string
    :param linkman: ,string
    :param mobile: ,string
    :param remark: ,string
    :param username: ,string
    :param userpassword: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1087')
    requesturl = baseUrl + "/appuser/addAppUser"
    LOGGER.info("App用户新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["linkman"] = linkman
    params["mobile"] = mobile
    params["remark"] = remark
    params["userName"] = username
    params["userPassword"] = userpassword
    params["token"] = LICENCES
    LOGGER.info("App用户新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("App用户新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_deleteAppUser(id):
    """
    App用户删除
    :param id: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1088')
    requesturl = baseUrl + "/appuser/deleteAppUser"
    LOGGER.info("App用户删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("App用户删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("App用户删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_updateAppUserOrgRange(selectedorg, userid):
    """
    App用户数据范围(机构范围)修改
    :param userid: ,string
    :param selectedorg: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1089')
    requesturl = baseUrl + "/appuser/updateAppUserOrgRange"
    LOGGER.info("App用户数据范围(机构范围)修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["selectedOrg"] = selectedorg
    params["userId"] = userid
    LOGGER.info("App用户数据范围(机构范围)修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("App用户数据范围(机构范围)修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_getAppUserOrgList(userid):
    """
    获取App用户机构树列表
    :param userid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1090')
    requesturl = baseUrl + "/appuser/getAppUserOrgList"
    LOGGER.info("获取App用户机构树列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    params["token"] = LICENCES
    LOGGER.info("获取App用户机构树列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取App用户机构树列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_getOrgTreeAll():
    """
    获取全部机构树
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1091')
    requesturl = baseUrl + "/appuser/getOrgTreeAll"
    LOGGER.info("获取全部机构树请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("获取全部机构树请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取全部机构树请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_appuser_getAppUserList(currentpage, pagesize, searchkeyword):
    """
    获取App用户列表
    :param searchkeyword: ,string
    :param currentpage: ,string
    :param pagesize: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1092')
    requesturl = baseUrl + "/appuser/getAppUserList"
    LOGGER.info("获取App用户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["searchKeyWord"] = searchkeyword
    params["token"] = LICENCES
    LOGGER.info("获取App用户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取App用户列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_dataHandle_updateMonitorNow(id):
    """
    立即更新数据
    :param id: 自定义数据id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1516')
    requesturl = baseUrl + "/dataHandle/updateMonitorNow"
    LOGGER.info("立即更新数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("立即更新数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("立即更新数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_deleteWarnBlack(id):
    """
    删除最新报警车辆黑名单
    :param id: 黑名单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1517')
    requesturl = baseUrl + "/black/deleteWarnBlack"
    LOGGER.info("删除最新报警车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("删除最新报警车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除最新报警车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_deleteRiskBlack(id):
    """
    删除风险车辆黑名单
    :param id: 黑名单id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1518')
    requesturl = baseUrl + "/black/deleteRiskBlack"
    LOGGER.info("删除风险车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("删除风险车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除风险车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_searchWarn(keyword):
    """
    搜索最新报警车辆黑名单
    :param keyword: 查询关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1519')
    requesturl = baseUrl + "/black/searchWarn"
    LOGGER.info("搜索最新报警车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["token"] = LICENCES
    LOGGER.info("搜索最新报警车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("搜索最新报警车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_searchRisk(keyword):
    """
    搜索风险车辆黑名单
    :param keyword: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1520')
    requesturl = baseUrl + "/black/searchRisk"
    LOGGER.info("搜索风险车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["token"] = LICENCES
    LOGGER.info("搜索风险车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("搜索风险车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_addWarnBlack(carid, carno, orgcode, orgname, userid, username):
    """
    新增最新报警车辆黑名单
    :param userid: ,number
    :param carid: ,number
    :param carno: ,string
    :param orgcode: ,string
    :param orgname: ,string
    :param username: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1521')
    requesturl = baseUrl + "/black/addWarnBlack"
    LOGGER.info("新增最新报警车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["carNo"] = carno
    params["orgCode"] = orgcode
    params["orgName"] = orgname
    params["userId"] = userid
    params["userName"] = username
    params["token"] = LICENCES
    LOGGER.info("新增最新报警车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增最新报警车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_addRiskBlack(carid, carno, orgcode, orgname, userid, username):
    """
    新增风险车辆黑名单
    :param username: ,string
    :param userid: ,number
    :param carid: ,number
    :param carno: ,string
    :param orgcode: ,string
    :param orgname: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1522')
    requesturl = baseUrl + "/black/addRiskBlack"
    LOGGER.info("新增风险车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["carNo"] = carno
    params["orgCode"] = orgcode
    params["orgName"] = orgname
    params["userId"] = userid
    params["userName"] = username
    params["token"] = LICENCES
    LOGGER.info("新增风险车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增风险车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_showWarnBlackList():
    """
    查询最新报警车辆黑名单列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1523')
    requesturl = baseUrl + "/black/showWarnBlackList"
    LOGGER.info("查询最新报警车辆黑名单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询最新报警车辆黑名单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询最新报警车辆黑名单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_showRiskBlackList():
    """
    查询风险车辆黑名单列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1524')
    requesturl = baseUrl + "/black/showRiskBlackList"
    LOGGER.info("查询风险车辆黑名单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询风险车辆黑名单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询风险车辆黑名单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_associateCarNums(keyword, orgcode):
    """
    模糊匹配车牌
    :param keyword: ,string
    :param orgcode: 组织机构编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1525')
    requesturl = baseUrl + "/black/associateCarNums"
    LOGGER.info("模糊匹配车牌请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["orgCode"] = orgcode
    params["token"] = LICENCES
    LOGGER.info("模糊匹配车牌请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("模糊匹配车牌请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getWarnDistributionList(currentpage, pagesize, username):
    """
    获取报警分布自定义数据列表
    :param username: 账号,string
    :param pagesize: 页大小（必填）,number
    :param currentpage: 当前页（必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1530')
    requesturl = baseUrl + "/custom/getWarnDistributionList"
    LOGGER.info("获取报警分布自定义数据列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("获取报警分布自定义数据列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警分布自定义数据列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_deleteWarnDistribution(id):
    """
    删除报警分布自定义数据
    :param id: 自定义数据Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1531')
    requesturl = baseUrl + "/custom/deleteWarnDistribution"
    LOGGER.info("删除报警分布自定义数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("删除报警分布自定义数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除报警分布自定义数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getRealWarnDistribution(userid):
    """
    获取报警分布真实数据
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1532')
    requesturl = baseUrl + "/custom/getRealWarnDistribution"
    LOGGER.info("获取报警分布真实数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取报警分布真实数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警分布真实数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getWarnDistribution(id):
    """
    获取报警分布自定义数据（编辑用）
    :param id: 自定义数据Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1533')
    requesturl = baseUrl + "/custom/getWarnDistribution"
    LOGGER.info("获取报警分布自定义数据（编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("获取报警分布自定义数据（编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警分布自定义数据（编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_saveWarnDistribution(devicedistanceexception, devicewarn, nothomecompany, offlinewarn, overduewarn, railwarn, stationexception, userid):
    """
    保存报警分布自定义数据（添加和编辑用）
    :param userid: 用户Id（必填）,number
    :param stationexception: 停车异常（必填）,number
    :param devicedistanceexception: 设备距离异常（必填）,number
    :param devicewarn: 设备报警	（必填）,number
    :param nothomecompany: 未回家/公司（必填）,number
    :param offlinewarn: 离线报警	（必填）,number
    :param overduewarn: 逾期报警（必填）,number
    :param railwarn: 围栏报警（必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1534')
    requesturl = baseUrl + "/custom/saveWarnDistribution"
    LOGGER.info("保存报警分布自定义数据（添加和编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceDistanceException"] = devicedistanceexception
    params["deviceWarn"] = devicewarn
    params["notHomeCompany"] = nothomecompany
    params["offlineWarn"] = offlinewarn
    params["overdueWarn"] = overduewarn
    params["railWarn"] = railwarn
    params["stationException"] = stationexception
    params["userId"] = userid
    LOGGER.info("保存报警分布自定义数据（添加和编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存报警分布自定义数据（添加和编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getUserAccountList(type):
    """
    获取用户账户列表（报警分布，车辆和贷款增量，报警趋势公用）
    :param type: 查询类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1535')
    requesturl = baseUrl + "/custom/getUserAccountList"
    LOGGER.info("获取用户账户列表（报警分布，车辆和贷款增量，报警趋势公用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    LOGGER.info("获取用户账户列表（报警分布，车辆和贷款增量，报警趋势公用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户账户列表（报警分布，车辆和贷款增量，报警趋势公用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_deleteCarStatistic(userid):
    """
    删除车辆和贷款自定义数据
    :param userid: 用户Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1536')
    requesturl = baseUrl + "/custom/deleteCarStatistic"
    LOGGER.info("删除车辆和贷款自定义数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("删除车辆和贷款自定义数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除车辆和贷款自定义数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getCarStatisticList(currentpage, pagesize, username):
    """
    获取车辆和贷款自定义数据列表
    :param username: 账号,string
    :param pagesize: 页大小（必填）,number
    :param currentpage: 当前页（必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1537')
    requesturl = baseUrl + "/custom/getCarStatisticList"
    LOGGER.info("获取车辆和贷款自定义数据列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("获取车辆和贷款自定义数据列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆和贷款自定义数据列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getRealCarStatisticList(userid):
    """
    获取车辆和贷款真实数据列表
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1538')
    requesturl = baseUrl + "/custom/getRealCarStatisticList"
    LOGGER.info("获取车辆和贷款真实数据列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取车辆和贷款真实数据列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆和贷款真实数据列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_saveCarStatistic(caraddcount, countday, countdaystr, loanaddcount, userid):
    """
    保存车辆和贷款自定义数据（添加和编辑用）
    :param loanaddcount: 贷款增量（必填）,number
    :param caraddcount: 车辆增量（必填）,number
    :param userid: 用户Id（必填）,number
    :param countday: 统计日,number
    :param countdaystr: 统计日字符串（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1539')
    requesturl = baseUrl + "/custom/saveCarStatistic"
    LOGGER.info("保存车辆和贷款自定义数据（添加和编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["carAddCount"] = caraddcount
    params["countDay"] = countday
    params["countDayStr"] = countdaystr
    params["loanAddCount"] = loanaddcount
    params["userId"] = userid
    LOGGER.info("保存车辆和贷款自定义数据（添加和编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存车辆和贷款自定义数据（添加和编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getCarStatistic(userid):
    """
    获取车辆和贷款自定义数据（编辑用）
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1540')
    requesturl = baseUrl + "/custom/getCarStatistic"
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_deleteWarnTrend(userid):
    """
    删除报警趋势自定义数据
    :param userid: 用户Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1541')
    requesturl = baseUrl + "/custom/deleteWarnTrend"
    LOGGER.info("删除报警趋势自定义数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("删除报警趋势自定义数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除报警趋势自定义数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getRealWarnTrendList(userid):
    """
    获取报警趋势真实数据列表
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1542')
    requesturl = baseUrl + "/custom/getRealWarnTrendList"
    LOGGER.info("获取报警趋势真实数据列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取报警趋势真实数据列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警趋势真实数据列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getWarnTrendList(currentpage, pagesize, username):
    """
    获取报警趋势自定义数据列表
    :param username: 账号,string
    :param pagesize: 页大小（必填）,number
    :param currentpage: 当前页（必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1543')
    requesturl = baseUrl + "/custom/getWarnTrendList"
    LOGGER.info("获取报警趋势自定义数据列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userName"] = username
    LOGGER.info("获取报警趋势自定义数据列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警趋势自定义数据列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_saveWarnTrend(countday, countdaystr, userid, warntrendpercent):
    """
    保存报警趋势自定义数据（添加和编辑用）
    :param countday: 统计日,number
    :param warntrendpercent: 报警趋势百分比（必填）,number
    :param userid: 用户Id（必填）,number
    :param countdaystr: 统计日字符串（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1544')
    requesturl = baseUrl + "/custom/saveWarnTrend"
    LOGGER.info("保存报警趋势自定义数据（添加和编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["countDay"] = countday
    params["countDayStr"] = countdaystr
    params["userId"] = userid
    params["warnTrendPercent"] = warntrendpercent
    LOGGER.info("保存报警趋势自定义数据（添加和编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存报警趋势自定义数据（添加和编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getWarnTrend(userid):
    """
    获取报警趋势自定义数据（编辑用）
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1545')
    requesturl = baseUrl + "/custom/getWarnTrend"
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_deleteBlack(id, type):
    """
    删除车辆黑名单
    :param id: 黑名单id,
    :param type: 报警、风险类别,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1549')
    requesturl = baseUrl + "/black/deleteBlack"
    LOGGER.info("删除车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["type"] = type
    params["token"] = LICENCES
    LOGGER.info("删除车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_addBlack(carid, carno, orgcode, orgname, type, userid, username):
    """
    新增车辆黑名单
    :param userid: ,number
    :param carid: ,number
    :param carno: ,string
    :param orgcode: ,string
    :param orgname: ,string
    :param username: ,string
    :param type: 报警类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1550')
    requesturl = baseUrl + "/black/addBlack"
    LOGGER.info("新增车辆黑名单请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["carNo"] = carno
    params["orgCode"] = orgcode
    params["orgName"] = orgname
    params["type"] = type
    params["userId"] = userid
    params["userName"] = username
    params["token"] = LICENCES
    LOGGER.info("新增车辆黑名单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增车辆黑名单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_queryBlackList(currentpage, keyword, pagesize, type):
    """
    查询车辆黑名单列表
    :param keyword: 选填，有-搜索，无-所有,string
    :param type: ,string
    :param pagesize: ,number
    :param currentpage: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1551')
    requesturl = baseUrl + "/black/queryBlackList"
    LOGGER.info("查询车辆黑名单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["keyword"] = keyword
    params["pageSize"] = pagesize
    params["type"] = type
    params["token"] = LICENCES
    LOGGER.info("查询车辆黑名单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询车辆黑名单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_black_queryAllUsers():
    """
    查询所有用户
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1552')
    requesturl = baseUrl + "/black/queryAllUsers"
    LOGGER.info("查询所有用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询所有用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询所有用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_dataUpdate_updateMonitorNow():
    """
    立即更新数据
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1553')
    requesturl = baseUrl + "/dataUpdate/updateMonitorNow"
    LOGGER.info("立即更新数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("立即更新数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("立即更新数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_dataUpdate_findState():
    """
    查询更新状态
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1554')
    requesturl = baseUrl + "/dataUpdate/findState"
    LOGGER.info("查询更新状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询更新状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询更新状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getCarStatisticEditList(userid):
    """
    获取车辆和贷款自定义数据（编辑用）
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1560')
    requesturl = baseUrl + "/custom/getCarStatisticEditList"
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆和贷款自定义数据（编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_custom_getWarnTrendEditList(userid):
    """
    获取报警趋势自定义数据（编辑用）
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1561')
    requesturl = baseUrl + "/custom/getWarnTrendEditList"
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警趋势自定义数据（编辑用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


