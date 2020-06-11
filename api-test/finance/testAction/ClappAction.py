#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : ClappAction.py
@desc       : 项目：finance 模块：clapp 接口方法封装
"""

from finance.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('clapp_apiURL', 'finance')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_clapp_login()


def test_login(appversion, deviceversion, phone, pwd, sysname, sysversion, uuid):
    """
    登录接口
    :param appversion: App版本号,string
    :param deviceversion: 设备类型,string
    :param sysname: 系统名,string
    :param pwd: 登录密码,string
    :param sysversion: 系统版本,string
    :param uuid: 设备唯一标识,string
    :param phone: 登录手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 108')
    requesturl = baseUrl + "/login"
    LOGGER.info("登录接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["appversion"] = appversion
    params["deviceversion"] = deviceversion
    params["phone"] = phone
    params["pwd"] = pwd
    params["sysname"] = sysname
    params["sysversion"] = sysversion
    params["uuid"] = uuid
    params = loginAction.getsignature(params)
    LOGGER.info("登录接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_organization_list():
    """
    组织列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 109')
    requesturl = baseUrl + "/organization/list"
    LOGGER.info("组织列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("组织列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("组织列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_list(filter, groupid, keyword, organizationid, pagenum, pagesize, sort, type):
    """
    监控首页列表
    :param keyword: 搜索关键词（可选,filter接口必填，getList接口无此参数）,number
    :param groupid: getList会用到，如果为空显示默认组,number
    :param pagesize: 每页条数，getList才会用到,number
    :param pagenum: 页数,getList才会用到,number
    :param organizationid: 组织机构ID,number
    :param type: 0-离线,1-在线,2-无线设备(可选)99-全部,number
    :param filter: 0-全部 1-只看报警 2-未激活 3-只看逾期,number
    :param sort: 0-安装时间降序 1-车牌升序,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 110')
    requesturl = baseUrl + "/device/list"
    LOGGER.info("监控首页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["filter"] = filter
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["sort"] = sort
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("监控首页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("监控首页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_more(groupid, keyword, pagenum, pagesize, type):
    """
    获取组内更多设备
    :param pagesize: 每页显示记录数,number
    :param groupid: 分组ID,number
    :param keyword: 搜索关键词（可选）,string
    :param type: 0-离线,1-在线,2-无线设备,number
    :param pagenum: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 111')
    requesturl = baseUrl + "/device/more"
    LOGGER.info("获取组内更多设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取组内更多设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取组内更多设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_caralldevice(carid):
    """
    获取同车设备
    :param carid: 车辆ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 112')
    requesturl = baseUrl + "/device/caralldevice"
    LOGGER.info("获取同车设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取同车设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取同车设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_tracklist(deviceid, endtime, positiontype, starttime):
    """
    获取设备轨迹
    :param endtime: ,number
    :param starttime: ,number
    :param deviceid: ,number
    :param positiontype: -1:全部；0:基站定位；1:GPS定位；2：WIFI定位；3：蓝牙定位,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 113')
    requesturl = baseUrl + "/device/tracklist"
    LOGGER.info("获取设备轨迹请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceId"] = deviceid
    params["endTime"] = endtime
    params["positionType"] = positiontype
    params["startTime"] = starttime
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备轨迹请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备轨迹请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_updateposition(deviceid):
    """
    获取设备最新状态
    :param deviceid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 114')
    requesturl = baseUrl + "/device/updateposition"
    LOGGER.info("获取设备最新状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceId"] = deviceid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备最新状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备最新状态请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userinfo():
    """
    获取我的信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 115')
    requesturl = baseUrl + "/userinfo"
    LOGGER.info("获取我的信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取我的信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取我的信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_notification_update(ison, notificationid):
    """
    修改通知设定
    :param notificationid: 通知的id,number
    :param ison: 修改至该状态,boolean
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 116')
    requesturl = baseUrl + "/notification/update"
    LOGGER.info("修改通知设定请求地址:【{}】".format(requesturl))
    params = dict()
    params["isOn"] = ison
    params["notificationId"] = notificationid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("修改通知设定请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改通知设定请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_logout():
    """
    退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 117')
    requesturl = baseUrl + "/logout"
    LOGGER.info("退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_list(devicenum, issolved, keyword, pagenum, pagesize, warningtype):
    """
    获取报警列表
    :param pagesize: 每页显示记录数,number
    :param issolved: 是否处理（可选）,boolean
    :param pagenum: 页码,number
    :param devicenum: 设备号(可选）,number
    :param warningtype: 报警类型,string
    :param keyword: 搜索文本（可选）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 118')
    requesturl = baseUrl + "/warning/list"
    LOGGER.info("获取报警列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceNum"] = devicenum
    params["isSolved"] = issolved
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warningType"] = warningtype
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取报警列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warningType_list():
    """
    获取报警类型
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 119')
    requesturl = baseUrl + "/warningType/list"
    LOGGER.info("获取报警类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取报警类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警类型请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_detail(warningid):
    """
    获取报警详情信息
    :param warningid: 报警id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 120')
    requesturl = baseUrl + "/warning/detail"
    LOGGER.info("获取报警详情信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["warningId"] = warningid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取报警详情信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警详情信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_mapinfo(warningid):
    """
    获取报警详情地图信息
    :param warningid: 报警id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 121')
    requesturl = baseUrl + "/warning/mapinfo"
    LOGGER.info("获取报警详情地图信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["warningId"] = warningid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取报警详情地图信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警详情地图信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_resolve(dangervalue, feedbackothertext, feedbackvalue, mark, warningid):
    """
    提交报警处理数据
    :param dangervalue: 风险评估枚举值,number
    :param warningid: 报警id,number
    :param feedbackvalue: 情况反馈枚举值,number
    :param mark: 备注,string
    :param feedbackothertext: 【其他】文本,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 122')
    requesturl = baseUrl + "/warning/resolve"
    LOGGER.info("提交报警处理数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["dangerValue"] = dangervalue
    params["feedbackOtherText"] = feedbackothertext
    params["feedbackValue"] = feedbackvalue
    params["mark"] = mark
    params["warningId"] = warningid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("提交报警处理数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交报警处理数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_handleinit(warnid):
    """
    动态获取情况反馈与风险等级
    :param warnid: 报警ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 123')
    requesturl = baseUrl + "/warning/handleinit"
    LOGGER.info("动态获取情况反馈与风险等级请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnId"] = warnid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("动态获取情况反馈与风险等级请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("动态获取情况反馈与风险等级请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_list(keyword, pagenum, pagesize, status, type):
    """
    设备首页列表
    :param pagesize: 不分页时，pageSize为空,number
    :param status: 设备状态,number
    :param type: 设备类型,number
    :param pagenum: 不分页时，pageNum为空,number
    :param keyword: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 124')
    requesturl = baseUrl + "/equipment/list"
    LOGGER.info("设备首页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["status"] = status
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("设备首页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设备首页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_update(id, instoragedate, model, no, organizationid, sim, type):
    """
    新增设备/编辑设备
    :param sim: sim卡号,string
    :param model: 设备型号,string
    :param organizationid: 所在机构Id,number
    :param type: 设备类型,number
    :param no: 设备编号,string
    :param id: 设备id,number
    :param instoragedate: 入库时间,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 125')
    requesturl = baseUrl + "/equipment/update"
    LOGGER.info("新增设备/编辑设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["inStorageDate"] = instoragedate
    params["model"] = model
    params["no"] = no
    params["organizationId"] = organizationid
    params["sim"] = sim
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("新增设备/编辑设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增设备/编辑设备请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_remove(id):
    """
    删除设备
    :param id: 设备id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 126')
    requesturl = baseUrl + "/equipment/remove"
    LOGGER.info("删除设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("删除设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除设备请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_list(keyword, pagenum, pagesize, status, type):
    """
    安装列表
    :param pagesize: 不分页时，pageSize为空,number
    :param type: 安装类型,number
    :param status: 安装状态,number
    :param pagenum: 不分页时，pageNum为空,number
    :param keyword: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 127')
    requesturl = baseUrl + "/install/list"
    LOGGER.info("安装列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["status"] = status
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("安装列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("安装列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_remove(id):
    """
    删除安装记录
    :param id: 安装记录ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 128')
    requesturl = baseUrl + "/install/remove"
    LOGGER.info("删除安装记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("删除安装记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除安装记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_uninstall(id):
    """
    拆机
    :param id: 设备记录ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 129')
    requesturl = baseUrl + "/install/uninstall"
    LOGGER.info("拆机请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("拆机请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("拆机请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_equipment_search(keyword, organizationid):
    """
    搜索设备
    :param keyword: ,string
    :param organizationid: 选中组织机构ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 130')
    requesturl = baseUrl + "/install/equipment/search"
    LOGGER.info("搜索设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["organizationId"] = organizationid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("搜索设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("搜索设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_car_search(keyword, organizationid):
    """
    搜索车辆
    :param keyword: ,string
    :param organizationid: 选中组织机构ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 131')
    requesturl = baseUrl + "/install/car/search"
    LOGGER.info("搜索车辆请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyword"] = keyword
    params["organizationId"] = organizationid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("搜索车辆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("搜索车辆请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_model(type):
    """
    获取设备型号
    :param type: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 132')
    requesturl = baseUrl + "/equipment/model"
    LOGGER.info("获取设备型号请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备型号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备型号请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_add(carid, equipmentids, username):
    """
    创建安装
    :param carid: 安装车辆id,number
    :param equipmentids: 安装设备id集合,string
    :param username: 安装师傅名字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 133')
    requesturl = baseUrl + "/install/add"
    LOGGER.info("创建安装请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["equipmentids"] = equipmentids
    params["username"] = username
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("创建安装请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("创建安装请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_detection(no):
    """
    定位
    :param no: 设备编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 134')
    requesturl = baseUrl + "/install/detection"
    LOGGER.info("定位请求地址:【{}】".format(requesturl))
    params = dict()
    params["no"] = no
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("定位请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("定位请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_update(date, id, imageid, position, username):
    """
    修改安装
    :param date: 安装日期,number
    :param position: 安装信息描述,string
    :param imageid: 安装图片ID,number
    :param username: 安装师傅,string
    :param id: 安装记录ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 135')
    requesturl = baseUrl + "/install/update"
    LOGGER.info("修改安装请求地址:【{}】".format(requesturl))
    params = dict()
    params["date"] = date
    params["id"] = id
    params["imageId"] = imageid
    params["position"] = position
    params["username"] = username
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("修改安装请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改安装请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_file_upload(file):
    """
    上传文件
    :param file: 文件，大小小于50M,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 136')
    requesturl = baseUrl + "/file/upload"
    LOGGER.info("上传文件请求地址:【{}】".format(requesturl))
    params = dict()
    params["file"] = file
    params["token"] = LICENCES
    LOGGER.info("上传文件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("上传文件请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warning_stationdetail(warnid):
    """
    未回家/公司获取停车记录
    :param warnid: 报警记录ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 137')
    requesturl = baseUrl + "/warning/stationdetail"
    LOGGER.info("未回家/公司获取停车记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnId"] = warnid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("未回家/公司获取停车记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("未回家/公司获取停车记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_details(id):
    """
    获取设备详情
    :param id: 设备id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 138')
    requesturl = baseUrl + "/equipment/details"
    LOGGER.info("获取设备详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("获取设备详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_sys_version():
    """
    获取最新版本信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 139')
    requesturl = baseUrl + "/sys/version"
    LOGGER.info("获取最新版本信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取最新版本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取最新版本信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_getGroups(keyword, organizationid, type):
    """
    获取监控分组
    :param keyword: 搜索关键词（可选）,number
    :param organizationid: 组织机构ID,number
    :param type: 0-离线,1-在线,2-无线设备(可选),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 140')
    requesturl = baseUrl + "/device/getGroups"
    LOGGER.info("获取监控分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取监控分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取监控分组请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_getDeviceList(groupid, keyword, organizationid, type):
    """
    获取设备列表
    :param groupid: 分组id,number
    :param keyword: 搜索关键词（可选）,number
    :param type: 0-离线,1-在线,2-无线设备(可选),number
    :param organizationid: 组织机构ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 141')
    requesturl = baseUrl + "/device/getDeviceList"
    LOGGER.info("获取设备列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_sys_uploadRegister(uuid):
    """
    更新registerId
    :param uuid: 极光注册别名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 142')
    requesturl = baseUrl + "/sys/uploadRegister"
    LOGGER.info("更新registerId请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("更新registerId请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新registerId请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_activation(appversion, deviceversion, phone, pwd, security, sysname, sysversion, uuid):
    """
    用户激活
    :param deviceversion: 设备类型,string
    :param phone: 登录手机号,string
    :param uuid: 设备唯一标识,string
    :param sysversion: 系统版本,string
    :param pwd: 登录密码,string
    :param security: 初始密码,string
    :param sysname: 系统名,string
    :param appversion: App版本号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 143')
    requesturl = baseUrl + "/user/activation"
    LOGGER.info("用户激活请求地址:【{}】".format(requesturl))
    params = dict()
    params["appversion"] = appversion
    params["deviceversion"] = deviceversion
    params["phone"] = phone
    params["pwd"] = pwd
    params["security"] = security
    params["sysname"] = sysname
    params["sysversion"] = sysversion
    params["uuid"] = uuid
    params = loginAction.getsignature(params)
    LOGGER.info("用户激活请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户激活请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_associate(keyword):
    """
    监控搜索(2.7新增)
    :param keyword: 搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 144')
    requesturl = baseUrl + "/device/associate"
    LOGGER.info("监控搜索(2.7新增)请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("监控搜索(2.7新增)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("监控搜索(2.7新增)请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_equipment_associate(keyword):
    """
    设备搜索
    :param keyword: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 145')
    requesturl = baseUrl + "/equipment/associate"
    LOGGER.info("设备搜索请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("设备搜索请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设备搜索请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_list(filter, groupid, keyword, organizationid, pagenum, pagesize, sort, type):
    """
    监控首页列表
    :param keyword: 搜索关键词（可选,filter接口必填，getList接口无此参数）,number
    :param groupid: getList会用到，如果为空显示默认组,number
    :param pagesize: 每页条数，getList才会用到,number
    :param pagenum: 页数,getList才会用到,number
    :param organizationid: 组织机构ID,number
    :param type: 0-离线,1-在线,2-无线设备(可选)99-全部,number
    :param filter: 0-全部 1-只看报警 2-未激活 3-只看逾期,number
    :param sort: 0-安装时间降序 1-车牌升序,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3323')
    requesturl = baseUrl + "/list"
    LOGGER.info("监控首页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["filter"] = filter
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["sort"] = sort
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("监控首页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("监控首页列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_more(groupid, keyword, pagenum, pagesize, type):
    """
    获取组内更多设备
    :param pagesize: 每页显示记录数,number
    :param groupid: 分组ID,number
    :param keyword: 搜索关键词（可选）,string
    :param type: 0-离线,1-在线,2-无线设备,number
    :param pagenum: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3324')
    requesturl = baseUrl + "/more"
    LOGGER.info("获取组内更多设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取组内更多设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取组内更多设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_caralldevice(carid):
    """
    获取同车设备
    :param carid: 车辆ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3325')
    requesturl = baseUrl + "/caralldevice"
    LOGGER.info("获取同车设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["carId"] = carid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取同车设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取同车设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_tracklist(deviceid, endtime, positiontype, starttime):
    """
    获取设备轨迹
    :param endtime: ,number
    :param starttime: ,number
    :param deviceid: ,number
    :param positiontype: -1:全部；0:基站定位；1:GPS定位；2：WIFI定位；3：蓝牙定位,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3326')
    requesturl = baseUrl + "/tracklist"
    LOGGER.info("获取设备轨迹请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceId"] = deviceid
    params["endTime"] = endtime
    params["positionType"] = positiontype
    params["startTime"] = starttime
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备轨迹请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备轨迹请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_updateposition(deviceid):
    """
    获取设备最新状态
    :param deviceid: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3327')
    requesturl = baseUrl + "/updateposition"
    LOGGER.info("获取设备最新状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceId"] = deviceid
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备最新状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备最新状态请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_getGroups(keyword, organizationid, type):
    """
    获取监控分组
    :param keyword: 搜索关键词（可选）,number
    :param organizationid: 组织机构ID,number
    :param type: 0-离线,1-在线,2-无线设备(可选),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3328')
    requesturl = baseUrl + "/getGroups"
    LOGGER.info("获取监控分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取监控分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取监控分组请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_getDeviceList(groupid, keyword, organizationid, type):
    """
    获取设备列表
    :param groupid: 分组id,number
    :param keyword: 搜索关键词（可选）,number
    :param type: 0-离线,1-在线,2-无线设备(可选),number
    :param organizationid: 组织机构ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3329')
    requesturl = baseUrl + "/getDeviceList"
    LOGGER.info("获取设备列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["organizationId"] = organizationid
    params["type"] = type
    params["token"] = LICENCES
    params = loginAction.getsignature(params)
    LOGGER.info("获取设备列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


