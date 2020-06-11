#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : FinanceAction.py
@desc       : 项目：finance 模块：finance 接口方法封装
"""

from finance.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('finance_apiURL', 'finance')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_finance_login()


def test_historyTrack_getFinanceByCarNo(carno):
    """
    车牌号查车贷数据
    :param carno: 车牌号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 147')
    requesturl = baseUrl + "/historyTrack/getFinanceByCarNo"
    LOGGER.info("车牌号查车贷数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["carNo"] = carno
    params["licences"] = LICENCES
    LOGGER.info("车牌号查车贷数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车牌号查车贷数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_showPassword(id):
    """
    finance查看用户密码
    :param id: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 148')
    requesturl = baseUrl + "/user/showPassword"
    LOGGER.info("finance查看用户密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("finance查看用户密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("finance查看用户密码请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_saveUser(email, name, orgcode, phone, roleid, userid):
    """
    新增用户保存
    :param phone: 电话，唯一,必填参数,string
    :param userid: 用户ID，编辑数据需要,integer
    :param name: 姓名,必填参数,string
    :param roleid: 角色id,必填参数,integer
    :param orgcode: 组织机构编号,必填参数,string
    :param email: 邮箱，唯一,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 149')
    requesturl = baseUrl + "/userManage/saveUser"
    LOGGER.info("新增用户保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["name"] = name
    params["orgCode"] = orgcode
    params["phone"] = phone
    params["roleid"] = roleid
    params["userid"] = userid
    params["licences"] = LICENCES
    LOGGER.info("新增用户保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_login(password, username):
    """
    用户登陆
    :param password: 用户登陆密码,必填参数,string
    :param username: 用户名，可输入邮箱地址或手机号码作为用户名,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 150')
    requesturl = baseUrl + "/user/login"
    LOGGER.info("用户登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["userName"] = username
    LOGGER.info("用户登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_save(borrowdate, borrownum, borrowtype, borrowtypename, broadendays, buytime, candelete, carengine, carmodel, carno, carshelf, cartype, companyaddress, companycoord, deletemessage, finance, gpscount, id, orgcode, orgname, owner, owneraddress, ownercoord, ownermoble, pledge, repaymanner, repaymannername, repaystatus, repaystatusname):
    """
    添加车贷数据
    :param pledge: 抵押方式，0为不抵押，1为抵押车,integer
    :param id: ,integer
    :param candelete: 是否允许被删除,boolean
    :param repaymanner: 还款方式,必填参数,string
    :param borrowdate: 贷款时间,string
    :param broadendays: 放款天数,integer
    :param borrownum: 贷款金额,必填参数,string
    :param carengine: 发动机号,string
    :param repaystatusname: 还款状态，文字版,string
    :param ownercoord: 家庭地址坐标,必填参数,string
    :param owner: 车主,必填参数,string
    :param repaystatus: 还款状态,string
    :param borrowtype: 贷款性质,必填参数,string
    :param borrowtypename: 贷款性质，文字版,string
    :param companyaddress: 公司地址,必填参数,string
    :param carmodel: 车型,必填参数,string
    :param companycoord: 公司地址坐标,必填参数,string
    :param gpscount: 被绑定的GPS数量,integer
    :param carshelf: 车架号,string
    :param deletemessage: ,string
    :param carno: 车牌号,必填参数,string
    :param orgcode: 组织机构,必填参数,string
    :param finance: ,string
    :param owneraddress: 家庭住址,必填参数,string
    :param cartype: 车品牌,必填参数,string
    :param ownermoble: 车主电话,必填参数,string
    :param buytime: 购车时间,string
    :param orgname: 机构名称,string
    :param repaymannername: 还款方式，文字版,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 151')
    requesturl = baseUrl + "/finance/save"
    LOGGER.info("添加车贷数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["borrowDate"] = borrowdate
    params["borrowNum"] = borrownum
    params["borrowType"] = borrowtype
    params["borrowTypeName"] = borrowtypename
    params["broadenDays"] = broadendays
    params["buyTime"] = buytime
    params["canDelete"] = candelete
    params["carEngine"] = carengine
    params["carModel"] = carmodel
    params["carNo"] = carno
    params["carShelf"] = carshelf
    params["carType"] = cartype
    params["companyAddress"] = companyaddress
    params["companyCoord"] = companycoord
    params["deleteMessage"] = deletemessage
    params["finance"] = finance
    params["gpsCount"] = gpscount
    params["id"] = id
    params["orgCode"] = orgcode
    params["orgName"] = orgname
    params["owner"] = owner
    params["ownerAddress"] = owneraddress
    params["ownerCoord"] = ownercoord
    params["ownerMoble"] = ownermoble
    params["pledge"] = pledge
    params["rePayManner"] = repaymanner
    params["rePayMannerName"] = repaymannername
    params["rePayStatus"] = repaystatus
    params["rePayStatusName"] = repaystatusname
    params["licences"] = LICENCES
    LOGGER.info("添加车贷数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加车贷数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_activation(phone, pwd, security):
    """
    用户激活
    :param pwd: 要保存的密码,string
    :param phone: 要保存的密码,string
    :param security: 初始密码,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 152')
    requesturl = baseUrl + "/user/activation"
    LOGGER.info("用户激活请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["pwd"] = pwd
    params["security"] = security
    LOGGER.info("用户激活请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户激活请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_getRisks(begin, keywords, orgcode, page, size):
    """
    获取风险点信息列表
    :param orgcode: 查询(组织机构),传入orgCode为查询风险点列表，不传入orgCode为查询统计信息,string
    :param keywords: 查询关键字,string
    :param page: 查询(页数，从1开始),integer
    :param begin: ,integer
    :param size: 查询(每页数量),integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 153')
    requesturl = baseUrl + "/risk/getRisks"
    LOGGER.info("获取风险点信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["licences"] = LICENCES
    LOGGER.info("获取风险点信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风险点信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_delete(id, orgcode):
    """
    删除一个风险点
    :param orgcode: 要删除的风险点的机构代码,必填参数,string
    :param id: 查询的关键字,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 154')
    requesturl = baseUrl + "/risk/delete"
    LOGGER.info("删除一个风险点请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("删除一个风险点请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一个风险点请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_save(risk):
    """
    saveRisk
    :param risk: 风险点信息,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 155')
    requesturl = baseUrl + "/risk/save"
    LOGGER.info("saveRisk请求地址:【{}】".format(requesturl))
    params = dict()
    params["risk"] = risk
    params["licences"] = LICENCES
    LOGGER.info("saveRisk请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("saveRisk请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_getOrgs():
    """
    获取组织机构
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 156')
    requesturl = baseUrl + "/risk/getOrgs"
    LOGGER.info("获取组织机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取组织机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取组织机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_getRules():
    """
    获取报警规则
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 157')
    requesturl = baseUrl + "/risk/getRules"
    LOGGER.info("获取报警规则请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取报警规则请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警规则请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_getDetail(id):
    """
    获取风险点详细信息
    :param id: 查询的关键字,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 158')
    requesturl = baseUrl + "/risk/getDetail"
    LOGGER.info("获取风险点详细信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取风险点详细信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风险点详细信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_risk_getRiskType():
    """
    获取风险点类型
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 159')
    requesturl = baseUrl + "/risk/getRiskType"
    LOGGER.info("获取风险点类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取风险点类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风险点类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnDist_getWarnIntervals(keyword, pagenum, pagesize, warnstatus):
    """
    获取设备距离报警记录
    :param pagenum: 页码,必填参数,integer
    :param pagesize: 每页数量,必填参数,integer
    :param warnstatus: 报警处理状态（0：未处理，1：已处理）,必填参数,string
    :param keyword: 查询关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 160')
    requesturl = baseUrl + "/warnDist/getWarnIntervals"
    LOGGER.info("获取设备距离报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("获取设备距离报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备距离报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnDist_getHandleWarnMessage(warnid):
    """
    处理报警信息页面初始化数据
    :param warnid: 报警信息的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 161')
    requesturl = baseUrl + "/warnDist/getHandleWarnMessage"
    LOGGER.info("处理报警信息页面初始化数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("处理报警信息页面初始化数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("处理报警信息页面初始化数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnDist_getDeviceWarnIntervalDetail(warnid):
    """
    查看设备距离报警信息
    :param warnid: 报警信息的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 162')
    requesturl = baseUrl + "/warnDist/getDeviceWarnIntervalDetail"
    LOGGER.info("查看设备距离报警信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("查看设备距离报警信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看设备距离报警信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnDist_doHandleWarn(feedbackcode, otherremark, remark, warncode, warnid):
    """
    执行报警信息处理
    :param warncode: 风险情况类型,必填参数,string
    :param feedbackcode: 情况反馈类型,必填参数,string
    :param remark: 备注,必填参数,string
    :param warnid: 报警记录id,必填参数,integer
    :param otherremark: 其它反馈类型补充说明,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 163')
    requesturl = baseUrl + "/warnDist/doHandleWarn"
    LOGGER.info("执行报警信息处理请求地址:【{}】".format(requesturl))
    params = dict()
    params["feedbackCode"] = feedbackcode
    params["otherRemark"] = otherremark
    params["remark"] = remark
    params["warnCode"] = warncode
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("执行报警信息处理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("执行报警信息处理请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_moveGpsToGroup(gpsid, groupid):
    """
    移动GPS到某个分组
    :param groupid: gps所属新分组对应的ID,必填参数,integer
    :param gpsid: 设备ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 164')
    requesturl = baseUrl + "/monitor/moveGpsToGroup"
    LOGGER.info("移动GPS到某个分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsId"] = gpsid
    params["groupId"] = groupid
    params["licences"] = LICENCES
    LOGGER.info("移动GPS到某个分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("移动GPS到某个分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_updateGroup(groupid, groupname):
    """
    修改分组
    :param groupid: 待修改分组ID,必填参数,integer
    :param groupname: 新的分组名称,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 165')
    requesturl = baseUrl + "/monitor/updateGroup"
    LOGGER.info("修改分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["groupName"] = groupname
    params["licences"] = LICENCES
    LOGGER.info("修改分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getGpsByOrg(groupid, keywords, linestatus, orgcode, pagenum, pagesize):
    """
    获取gps信息列表(刷新机构内部的gps列表)
    :param orgcode: 查询(组织机构)，必填,必填参数,string
    :param pagenum: 页码,integer
    :param pagesize: 每页数量,integer
    :param keywords: 查询关键字,string
    :param linestatus: 在线状态, 0:离线，1:在线，2:无线,必填参数,integer
    :param groupid: 分组ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 166')
    requesturl = baseUrl + "/monitor/getGpsByOrg"
    LOGGER.info("获取gps信息列表(刷新机构内部的gps列表)请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keywords"] = keywords
    params["lineStatus"] = linestatus
    params["orgCode"] = orgcode
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("获取gps信息列表(刷新机构内部的gps列表)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取gps信息列表(刷新机构内部的gps列表)请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getCurrentOrgs():
    """
    获取当前登录用户的组织机构树形信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 167')
    requesturl = baseUrl + "/monitor/getCurrentOrgs"
    LOGGER.info("获取当前登录用户的组织机构树形信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取当前登录用户的组织机构树形信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前登录用户的组织机构树形信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_deleteGroup(groupid):
    """
    删除分组
    :param groupid: 待删除分组ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 168')
    requesturl = baseUrl + "/monitor/deleteGroup"
    LOGGER.info("删除分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["licences"] = LICENCES
    LOGGER.info("删除分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getGpsLocationByGps(gpscodes):
    """
    查询实时消息(刷新地图上的GPS信号)
    :param gpscodes: 要查询的设备编号格式code1,code2,code3,...(这里的gpsCode为GPS设备列表中的gpsCode),必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 169')
    requesturl = baseUrl + "/monitor/getGpsLocationByGps"
    LOGGER.info("查询实时消息(刷新地图上的GPS信号)请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsCodes"] = gpscodes
    params["licences"] = LICENCES
    LOGGER.info("查询实时消息(刷新地图上的GPS信号)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询实时消息(刷新地图上的GPS信号)请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getGroups(keywords, linestatus, orgcode):
    """
    获取当前用户能操作的分组
    :param linestatus: 在线状态, 0:离线，1:在线，2:无线,必填参数,ref
    :param keywords: 机构编号,string
    :param orgcode: 机构编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 170')
    requesturl = baseUrl + "/monitor/getGroups"
    LOGGER.info("获取当前用户能操作的分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["keywords"] = keywords
    params["lineStatus"] = linestatus
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("获取当前用户能操作的分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前用户能操作的分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getOrgsStatistic(begin, keywords, orgcode, page, size):
    """
    获取组织机构统计(刷新机构统计总数)
    :param size: 每页的数量,integer
    :param keywords: 查询关键字,string
    :param page: 查询的页数，page从1开始,integer
    :param orgcode: 查询(组织机构),string
    :param begin: ,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 171')
    requesturl = baseUrl + "/monitor/getOrgsStatistic"
    LOGGER.info("获取组织机构统计(刷新机构统计总数)请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["licences"] = LICENCES
    LOGGER.info("获取组织机构统计(刷新机构统计总数)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取组织机构统计(刷新机构统计总数)请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_addGroup(groupname, orgcode):
    """
    新增分组
    :param groupname: 分组名称,必填参数,string
    :param orgcode: 分组名称,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 172')
    requesturl = baseUrl + "/monitor/addGroup"
    LOGGER.info("新增分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupName"] = groupname
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("新增分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_gpsRealTime(gpscode):
    """
    获取gps详细(用于地图展开)
    :param gpscode: gps的编号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 173')
    requesturl = baseUrl + "/monitor/gpsRealTime"
    LOGGER.info("获取gps详细(用于地图展开)请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsCode"] = gpscode
    params["licences"] = LICENCES
    LOGGER.info("获取gps详细(用于地图展开)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取gps详细(用于地图展开)请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getOrgCountByCode(begin, keywords, orgcode, page, size):
    """
    查询某个机构的GPS统计数据(带关键字)
    :param size: ,ref
    :param orgcode: 设备ID,必填参数,string
    :param begin: ,integer
    :param keywords: gps所属新分组对应的ID,string
    :param page: ,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 174')
    requesturl = baseUrl + "/monitor/getOrgCountByCode"
    LOGGER.info("查询某个机构的GPS统计数据(带关键字)请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["licences"] = LICENCES
    LOGGER.info("查询某个机构的GPS统计数据(带关键字)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询某个机构的GPS统计数据(带关键字)请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warn_getRiskDetail(riskid):
    """
    根据ID获取风险点详情
    :param riskid: 风险点ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 175')
    requesturl = baseUrl + "/warn/getRiskDetail"
    LOGGER.info("根据ID获取风险点详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["riskid"] = riskid
    params["licences"] = LICENCES
    LOGGER.info("根据ID获取风险点详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据ID获取风险点详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warn_getHandleWarnMessage(warnid):
    """
    处理报警信息页面初始化数据
    :param warnid: 报警信息的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 176')
    requesturl = baseUrl + "/warn/getHandleWarnMessage"
    LOGGER.info("处理报警信息页面初始化数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("处理报警信息页面初始化数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("处理报警信息页面初始化数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warn_getWarnDetailById():
    """
    获取报警详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 177')
    requesturl = baseUrl + "/warn/getWarnDetailById"
    LOGGER.info("获取报警详情请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取报警详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warn_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    获取设备报警记录
    :param pagenum: 页码,必填参数,integer
    :param pagesize: 每页数量,必填参数,integer
    :param warnstatus: 报警处理状态（0：未处理，1：已处理）,必填参数,string
    :param keyword: 查询关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 178')
    requesturl = baseUrl + "/warn/getWarns"
    LOGGER.info("获取设备报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("获取设备报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warn_doHandleWarn(feedbackcode, otherremark, remark, warncode, warnid):
    """
    执行报警信息处理
    :param warncode: 风险情况类型,必填参数,string
    :param feedbackcode: 情况反馈类型,必填参数,string
    :param otherremark: 其它反馈类型补充说明,string
    :param remark: 备注,必填参数,string
    :param warnid: 报警记录id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 179')
    requesturl = baseUrl + "/warn/doHandleWarn"
    LOGGER.info("执行报警信息处理请求地址:【{}】".format(requesturl))
    params = dict()
    params["feedbackCode"] = feedbackcode
    params["otherRemark"] = otherremark
    params["remark"] = remark
    params["warnCode"] = warncode
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("执行报警信息处理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("执行报警信息处理请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_save(devicecode, id, moudelcode, orgcode, sms, storagetime, typecode):
    """
    保存设备记录
    :param orgcode: 组织机构Code,必填参数,string
    :param typecode: GPS类型Code,必填参数,string
    :param id: 设备id（仅编辑设备时需要）,integer
    :param moudelcode: GPS型号Code,必填参数,string
    :param devicecode: GPS设备号,必填参数,string
    :param storagetime: 入库时间,必填参数,string
    :param sms: GPS设备卡号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 180')
    requesturl = baseUrl + "/device/save"
    LOGGER.info("保存设备记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceCode"] = devicecode
    params["id"] = id
    params["moudelCode"] = moudelcode
    params["orgCode"] = orgcode
    params["sms"] = sms
    params["storageTime"] = storagetime
    params["typeCode"] = typecode
    params["licences"] = LICENCES
    LOGGER.info("保存设备记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存设备记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_getDeviceMoudel(devicetype):
    """
    获取设备型号信息
    :param devicetype: 设备类型,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 181')
    requesturl = baseUrl + "/device/getDeviceMoudel"
    LOGGER.info("获取设备型号信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceType"] = devicetype
    params["licences"] = LICENCES
    LOGGER.info("获取设备型号信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备型号信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_getDeviceType():
    """
    获取设备类型信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 182')
    requesturl = baseUrl + "/device/getDeviceType"
    LOGGER.info("获取设备类型信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取设备类型信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备类型信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_delete(id):
    """
    删除设备记录
    :param id: 设备记录ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 183')
    requesturl = baseUrl + "/device/delete"
    LOGGER.info("删除设备记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("删除设备记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除设备记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_update(devicecode, id, moudelcode, orgcode, sms, storagetime, typecode):
    """
    更新设备记录
    :param storagetime: 入库时间,必填参数,string
    :param devicecode: GPS设备号,必填参数,string
    :param id: 设备id（仅编辑设备时需要）,integer
    :param moudelcode: GPS型号Code,必填参数,string
    :param orgcode: 组织机构Code,必填参数,string
    :param sms: GPS设备卡号,必填参数,string
    :param typecode: GPS类型Code,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 184')
    requesturl = baseUrl + "/device/update"
    LOGGER.info("更新设备记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceCode"] = devicecode
    params["id"] = id
    params["moudelCode"] = moudelcode
    params["orgCode"] = orgcode
    params["sms"] = sms
    params["storageTime"] = storagetime
    params["typeCode"] = typecode
    params["licences"] = LICENCES
    LOGGER.info("更新设备记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新设备记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_getLowerOrg():
    """
    获取机构信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 185')
    requesturl = baseUrl + "/device/getLowerOrg"
    LOGGER.info("获取机构信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_list(devicecode, pagenum, pagesize):
    """
    设备列表
    :param devicecode: 设备号,string
    :param pagesize: 每页数量,必填参数,integer
    :param pagenum: 页码,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 186')
    requesturl = baseUrl + "/device/list"
    LOGGER.info("设备列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceCode"] = devicecode
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("设备列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设备列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_device_detail(id):
    """
    获取设备详情
    :param id: 设备记录ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 187')
    requesturl = baseUrl + "/device/detail"
    LOGGER.info("获取设备详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取设备详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnStop_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    获取设备报警记录
    :param keyword: 查询关键字,string
    :param warnstatus: 报警处理状态（0：未处理，1：已处理）,必填参数,string
    :param pagesize: 每页数量,必填参数,integer
    :param pagenum: 页码,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 188')
    requesturl = baseUrl + "/warnStop/getWarns"
    LOGGER.info("获取设备报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("获取设备报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnStop_saveThreshold(id, thresholdhour, thresholdminute):
    """
    获取停车异常报警阀值
    :param id: id,integer
    :param thresholdminute: 阀值分钟数,必填参数,integer
    :param thresholdhour: 阀值小时数,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 189')
    requesturl = baseUrl + "/warnStop/saveThreshold"
    LOGGER.info("获取停车异常报警阀值请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["thresholdHour"] = thresholdhour
    params["thresholdMinute"] = thresholdminute
    params["licences"] = LICENCES
    LOGGER.info("获取停车异常报警阀值请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取停车异常报警阀值请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnStop_getThreshold():
    """
    获取停车异常报警阀值
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 190')
    requesturl = baseUrl + "/warnStop/getThreshold"
    LOGGER.info("获取停车异常报警阀值请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取停车异常报警阀值请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取停车异常报警阀值请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_org_getOrgs():
    """
    获取组织机构
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 191')
    requesturl = baseUrl + "/org/getOrgs"
    LOGGER.info("获取组织机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取组织机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取组织机构请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_org_addOrg(count, description, dto, id, name, offlinecount, onlinecount, orgcode, parentid, parentname):
    """
    新增机构
    :param description: 描述,integer
    :param onlinecount: ,integer
    :param count: ,integer
    :param orgcode: 机构编号,string
    :param offlinecount: ,integer
    :param parentname: 父节点名称，当查询的机构不是顶级机构时，将上级机构名称赋予查询的最顶级机构,string
    :param id: ,integer
    :param dto: ,array
    :param name: 名称,integer
    :param parentid: 父节点id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 192')
    requesturl = baseUrl + "/org/addOrg"
    LOGGER.info("新增机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["count"] = count
    params["description"] = description
    params["dto"] = dto
    params["id"] = id
    params["name"] = name
    params["offLineCount"] = offlinecount
    params["onLineCount"] = onlinecount
    params["orgCode"] = orgcode
    params["parentId"] = parentid
    params["parentName"] = parentname
    params["licences"] = LICENCES
    LOGGER.info("新增机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_org_delete(id):
    """
    删除机构
    :param id: 父节点id,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 193')
    requesturl = baseUrl + "/org/delete"
    LOGGER.info("删除机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("删除机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_org_getCurrentOrgs():
    """
    获取当前用户能操作的组织机构
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 194')
    requesturl = baseUrl + "/org/getCurrentOrgs"
    LOGGER.info("获取当前用户能操作的组织机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取当前用户能操作的组织机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前用户能操作的组织机构请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_org_updateOrg(count, description, dto, id, name, offlinecount, onlinecount, orgcode, parentid, parentname):
    """
    修改机构
    :param parentid: 父节点id,integer
    :param count: ,integer
    :param description: 描述,integer
    :param orgcode: 机构编号,string
    :param offlinecount: ,integer
    :param name: 名称,integer
    :param id: id,integer
    :param parentname: 父节点名称，当查询的机构不是顶级机构时，将上级机构名称赋予查询的最顶级机构,string
    :param dto: ,array
    :param onlinecount: ,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 195')
    requesturl = baseUrl + "/org/updateOrg"
    LOGGER.info("修改机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["count"] = count
    params["description"] = description
    params["dto"] = dto
    params["id"] = id
    params["name"] = name
    params["offLineCount"] = offlinecount
    params["onLineCount"] = onlinecount
    params["orgCode"] = orgcode
    params["parentId"] = parentid
    params["parentName"] = parentname
    params["licences"] = LICENCES
    LOGGER.info("修改机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_customerMessage(fid):
    """
    车辆档案--停车统计--车主信息
    :param fid: 关联车牌号码对应id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 196')
    requesturl = baseUrl + "/historyCarRecord/customerMessage"
    LOGGER.info("车辆档案--停车统计--车主信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("车辆档案--停车统计--车主信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆档案--停车统计--车主信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getGpsByFid(fid, type):
    """
    查询设备信息
    :param fid: 车辆id,number
    :param type: 查询方式，0查询全部设备，1 只获取有线设备,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 197')
    requesturl = baseUrl + "/historyCarRecord/getGpsByFid"
    LOGGER.info("查询设备信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["type"] = type
    params["licences"] = LICENCES
    LOGGER.info("查询设备信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询设备信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getCarInit(fid):
    """
    获取车辆设备页面初始化数据
    :param fid: 关联车牌号码对应id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 198')
    requesturl = baseUrl + "/historyCarRecord/getCarInit"
    LOGGER.info("获取车辆设备页面初始化数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("获取车辆设备页面初始化数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆设备页面初始化数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_quantumLocation(endtime, fid, gpscode, starttime):
    """
    车辆档案--停车统计--时间分布
    :param fid: 关联车牌号码对应id,必填参数,integer
    :param starttime: 开始时间,必填参数,string
    :param gpscode: gps编号,必填参数,string
    :param endtime: 结束时间,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 199')
    requesturl = baseUrl + "/historyCarRecord/quantumLocation"
    LOGGER.info("车辆档案--停车统计--时间分布请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["fid"] = fid
    params["gpsCode"] = gpscode
    params["startTime"] = starttime
    params["licences"] = LICENCES
    LOGGER.info("车辆档案--停车统计--时间分布请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆档案--停车统计--时间分布请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getCarLocations(fid):
    """
    获取该车辆的实时定位数据
    :param fid: 关联车牌号码对应id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 200')
    requesturl = baseUrl + "/historyCarRecord/getCarLocations"
    LOGGER.info("获取该车辆的实时定位数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("获取该车辆的实时定位数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取该车辆的实时定位数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_listLocation(begin, endtime, fid, gpscode, keywords, orgcode, page, size, starttime, stationtimes):
    """
    车辆档案--停车统计--常停地址
    :param fid: 关联车牌号码对应id,必填参数,integer
    :param stationtimes: 停车次数，此为累计总停车次数,必填参数,integer
    :param orgcode: 要查询的组织机构(部分接口使用),string
    :param size: 查询(每页数量),integer
    :param starttime: 开始时间,必填参数,string
    :param page: 查询(页数，从1开始),integer
    :param begin: ,integer
    :param keywords: 查询关键字,string
    :param gpscode: gps编号,必填参数,string
    :param endtime: 结束时间,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 201')
    requesturl = baseUrl + "/historyCarRecord/listLocation"
    LOGGER.info("车辆档案--停车统计--常停地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["endTime"] = endtime
    params["fid"] = fid
    params["gpsCode"] = gpscode
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["startTime"] = starttime
    params["stationTimes"] = stationtimes
    params["licences"] = LICENCES
    LOGGER.info("车辆档案--停车统计--常停地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆档案--停车统计--常停地址请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_stationDetail(begin, endtime, fid, gpscode, keywords, orgcode, page, size, starttime, timecast):
    """
    车辆档案--停车统计--停车明细
    :param gpscode: gps编号,必填参数,string
    :param endtime: 结束时间,必填参数,string
    :param starttime: 开始时间,必填参数,string
    :param timecast: 停车时长,integer
    :param page: 页码,必填参数,integer
    :param orgcode: 要查询的组织机构(部分接口使用),string
    :param keywords: 查询关键字,string
    :param begin: ,integer
    :param fid: fid,必填参数,integer
    :param size: 每页显示记录数,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 202')
    requesturl = baseUrl + "/historyCarRecord/stationDetail"
    LOGGER.info("车辆档案--停车统计--停车明细请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["endTime"] = endtime
    params["fid"] = fid
    params["gpsCode"] = gpscode
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["startTime"] = starttime
    params["timeCast"] = timecast
    params["licences"] = LICENCES
    LOGGER.info("车辆档案--停车统计--停车明细请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆档案--停车统计--停车明细请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getCarWarn(fid, pagenum, pagesize):
    """
    获取车辆的报警记录
    :param pagenum: 页码,必填参数,integer
    :param fid: 关联车牌号码对应id,必填参数,integer
    :param pagesize: 每页显示记录数,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 203')
    requesturl = baseUrl + "/historyCarRecord/getCarWarn"
    LOGGER.info("获取车辆的报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("获取车辆的报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆的报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getCarWarnCount(fid):
    """
    获取车辆设备的报警统计信息
    :param fid: 关联车牌号码对应id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 204')
    requesturl = baseUrl + "/historyCarRecord/getCarWarnCount"
    LOGGER.info("获取车辆设备的报警统计信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("获取车辆设备的报警统计信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆设备的报警统计信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_test_test():
    """
    test
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 205')
    requesturl = baseUrl + "/test/test"
    LOGGER.info("test请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("test请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("test请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_test_getAllLocation(code, end, start):
    """
    数据查询
    :param start: 开始时间,string
    :param end: 结束时间,string
    :param code: id,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 206')
    requesturl = baseUrl + "/test/getAllLocation"
    LOGGER.info("数据查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["end"] = end
    params["start"] = start
    LOGGER.info("数据查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("数据查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_test_testElasticSearch(gpscode):
    """
    向es查询数据
    :param gpscode: id,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 207')
    requesturl = baseUrl + "/test/testElasticSearch"
    LOGGER.info("向es查询数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsCode"] = gpscode
    LOGGER.info("向es查询数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("向es查询数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOfflineThreshold_saveNewThreshold(wireid, wiredthresholdhour, wiredthresholdminute, wirelessid, wirelessthresholdhour, wirelessthresholdminute):
    """
    saveNewThreshold
    :param wireid: 阈值ID,integer
    :param wiredthresholdhour: 有线时间小时部分,必填参数,integer
    :param wirelessthresholdminute: 无线时间小时部分,必填参数,integer
    :param wirelessid: ,integer
    :param wiredthresholdminute: 有线时间分钟部分,必填参数,integer
    :param wirelessthresholdhour: 无线时间小时部分,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 208')
    requesturl = baseUrl + "/warnOfflineThreshold/saveNewThreshold"
    LOGGER.info("saveNewThreshold请求地址:【{}】".format(requesturl))
    params = dict()
    params["wireId"] = wireid
    params["wiredThresholdHour"] = wiredthresholdhour
    params["wiredThresholdMinute"] = wiredthresholdminute
    params["wirelessId"] = wirelessid
    params["wirelessThresholdHour"] = wirelessthresholdhour
    params["wirelessThresholdMinute"] = wirelessthresholdminute
    params["licences"] = LICENCES
    LOGGER.info("saveNewThreshold请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("saveNewThreshold请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOfflineThreshold_getWarnOfflineThreshold():
    """
    获取当前企业的阈值
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 209')
    requesturl = baseUrl + "/warnOfflineThreshold/getWarnOfflineThreshold"
    LOGGER.info("获取当前企业的阈值请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取当前企业的阈值请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前企业的阈值请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOffline_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    获取离线报警记录
    :param pagesize: 每页数量,必填参数,integer
    :param warnstatus: 报警处理状态（0：未处理，1：已处理）,必填参数,string
    :param keyword: 查询关键字,string
    :param pagenum: 页码,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 210')
    requesturl = baseUrl + "/warnOffline/getWarns"
    LOGGER.info("获取离线报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("获取离线报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取离线报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOffline_getFinanceById(financeid):
    """
    获取车辆和GPS列表
    :param financeid: 车辆id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 211')
    requesturl = baseUrl + "/warnOffline/getFinanceById"
    LOGGER.info("获取车辆和GPS列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["licences"] = LICENCES
    LOGGER.info("获取车辆和GPS列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆和GPS列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOffline_getHandleWarnMessage(warnid):
    """
    处理报警信息页面初始化数据
    :param warnid: 报警信息的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 212')
    requesturl = baseUrl + "/warnOffline/getHandleWarnMessage"
    LOGGER.info("处理报警信息页面初始化数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("处理报警信息页面初始化数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("处理报警信息页面初始化数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOffline_doHandleWarn(feedbackcode, otherremark, remark, warncode, warnid):
    """
    执行报警信息处理
    :param otherremark: 其它反馈类型补充说明,string
    :param remark: 备注,必填参数,string
    :param feedbackcode: 情况反馈类型,必填参数,string
    :param warnid: 报警记录id,必填参数,integer
    :param warncode: 风险情况类型,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 213')
    requesturl = baseUrl + "/warnOffline/doHandleWarn"
    LOGGER.info("执行报警信息处理请求地址:【{}】".format(requesturl))
    params = dict()
    params["feedbackCode"] = feedbackcode
    params["otherRemark"] = otherremark
    params["remark"] = remark
    params["warnCode"] = warncode
    params["warnid"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("执行报警信息处理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("执行报警信息处理请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOffline_getOfflinePoint(gpscode, timecast):
    """
    通过gpsId和离线时长查询离线点
    :param gpscode: gpsId,必填参数,string
    :param timecast: 离线时长,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 214')
    requesturl = baseUrl + "/warnOffline/getOfflinePoint"
    LOGGER.info("通过gpsId和离线时长查询离线点请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsCode"] = gpscode
    params["timeCast"] = timecast
    params["licences"] = LICENCES
    LOGGER.info("通过gpsId和离线时长查询离线点请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过gpsId和离线时长查询离线点请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getOrgs():
    """
    查找组织机构
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 215')
    requesturl = baseUrl + "/finance/getOrgs"
    LOGGER.info("查找组织机构请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("查找组织机构请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查找组织机构请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getRepayStatus(level):
    """
    查找还款状态
    :param level: 字典优先级,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 216')
    requesturl = baseUrl + "/finance/getRepayStatus"
    LOGGER.info("查找还款状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["level"] = level
    params["licences"] = LICENCES
    LOGGER.info("查找还款状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查找还款状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getFinances():
    """
    获取车贷列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 217')
    requesturl = baseUrl + "/finance/getFinances"
    LOGGER.info("获取车贷列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取车贷列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车贷列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getBorrowType():
    """
    查找贷款性质
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 218')
    requesturl = baseUrl + "/finance/getBorrowType"
    LOGGER.info("查找贷款性质请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("查找贷款性质请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查找贷款性质请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_alreadyHasCar(carno, financeid):
    """
    查看车牌号是否重复
    :param financeid: 车贷id,integer
    :param carno: 车牌号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 219')
    requesturl = baseUrl + "/finance/alreadyHasCar"
    LOGGER.info("查看车牌号是否重复请求地址:【{}】".format(requesturl))
    params = dict()
    params["carNo"] = carno
    params["financeId"] = financeid
    params["licences"] = LICENCES
    LOGGER.info("查看车牌号是否重复请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看车牌号是否重复请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getRepayManner():
    """
    查找还款方式
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 220')
    requesturl = baseUrl + "/finance/getRepayManner"
    LOGGER.info("查找还款方式请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("查找还款方式请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查找还款方式请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_deleteById(id, orgcode):
    """
    删除
    :param id: 车牌号,必填参数,integer
    :param orgcode: 删除的车贷数据的组织机构,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 221')
    requesturl = baseUrl + "/finance/deleteById"
    LOGGER.info("删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_updatePasswordBySecurity(password, security, username):
    """
    根据验证码修改用户密码
    :param username: 用户的帐号,可以输入邮箱或手机号,必填参数,string
    :param password: 密码,重新设置的密码,必填参数,string
    :param security: 验证码,用户通过手机或邮箱接收到的验证码,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 222')
    requesturl = baseUrl + "/user/updatePasswordBySecurity"
    LOGGER.info("根据验证码修改用户密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["security"] = security
    params["userName"] = username
    LOGGER.info("根据验证码修改用户密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据验证码修改用户密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getMessageCount():
    """
    获取用户的提示消息数量
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 223')
    requesturl = baseUrl + "/user/getMessageCount"
    LOGGER.info("获取用户的提示消息数量请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取用户的提示消息数量请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户的提示消息数量请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_saveWarnManner(manners):
    """
    保存报警设置
    :param manners: 策略方式，字符串格式的manner数组，数据格式参考 getWarnManner的返回值,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 224')
    requesturl = baseUrl + "/user/saveWarnManner"
    LOGGER.info("保存报警设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["manners"] = manners
    params["licences"] = LICENCES
    LOGGER.info("保存报警设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存报警设置请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_updatePassword(newpassword, oldpassword):
    """
    用户修改密码
    :param oldpassword: 旧密码,必填参数,string
    :param newpassword: 新密码,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 225')
    requesturl = baseUrl + "/user/updatePassword"
    LOGGER.info("用户修改密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["newPassword"] = newpassword
    params["oldPassword"] = oldpassword
    params["licences"] = LICENCES
    LOGGER.info("用户修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getMoudels():
    """
    模块权限
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 226')
    requesturl = baseUrl + "/user/getMoudels"
    LOGGER.info("模块权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("模块权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("模块权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getMessages(begin, keywords, orgcode, page, size, status):
    """
    获取用户的提示消息
    :param page: 查询(页数，从1开始),integer
    :param orgcode: 要查询的组织机构(部分接口使用),string
    :param begin: ,integer
    :param keywords: 查询关键字,string
    :param size: 查询(每页数量),integer
    :param status: 消息状态，0为未读1为已读,2为查询全部，不设置则默认为0,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 227')
    requesturl = baseUrl + "/user/getMessages"
    LOGGER.info("获取用户的提示消息请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["status"] = status
    params["licences"] = LICENCES
    LOGGER.info("获取用户的提示消息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户的提示消息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_sendPhoneSecurity(phone):
    """
    发送修改手机号的验证码
    :param phone: 新的手机号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 228')
    requesturl = baseUrl + "/user/sendPhoneSecurity"
    LOGGER.info("发送修改手机号的验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["licences"] = LICENCES
    LOGGER.info("发送修改手机号的验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送修改手机号的验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_readMessage(messageid):
    """
    将用户的消息设置为已读，可同时修改多条
    :param messageid: 消息id，使用,进行多条记录的拼接，拼接格式: id1,id2,id3,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 229')
    requesturl = baseUrl + "/user/readMessage"
    LOGGER.info("将用户的消息设置为已读，可同时修改多条请求地址:【{}】".format(requesturl))
    params = dict()
    params["messageId"] = messageid
    params["licences"] = LICENCES
    LOGGER.info("将用户的消息设置为已读，可同时修改多条请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("将用户的消息设置为已读，可同时修改多条请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getMannerType():
    """
    获取报警设置
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 230')
    requesturl = baseUrl + "/user/getMannerType"
    LOGGER.info("获取报警设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取报警设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报警设置请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getUser():
    """
    获取登陆用户信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 231')
    requesturl = baseUrl + "/user/getUser"
    LOGGER.info("获取登陆用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取登陆用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取登陆用户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_getWarnManner():
    """
    查询消息推送设置
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 232')
    requesturl = baseUrl + "/user/getWarnManner"
    LOGGER.info("查询消息推送设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("查询消息推送设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询消息推送设置请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_logout():
    """
    退出登陆
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 233')
    requesturl = baseUrl + "/user/logout"
    LOGGER.info("退出登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("退出登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_installCarSearchAssociate(keyword, orgcode):
    """
    安装车辆搜索联想
    :param keyword: 联想的关键字,string
    :param orgcode: 组织机构代码,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 234')
    requesturl = baseUrl + "/install/installCarSearchAssociate"
    LOGGER.info("安装车辆搜索联想请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("安装车辆搜索联想请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("安装车辆搜索联想请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getGpsMoudel(gpstype):
    """
    获取GPS型号
    :param gpstype: gpsTye(有线，无线),必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 235')
    requesturl = baseUrl + "/install/getGpsMoudel"
    LOGGER.info("获取GPS型号请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsType"] = gpstype
    params["licences"] = LICENCES
    LOGGER.info("获取GPS型号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取GPS型号请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_findGpsInstallRecord(keyword, pagenum, pagesize):
    """
    Gps安装记录列表
    :param keyword: 查询关键字,string
    :param pagesize: 每页数量,必填参数,integer
    :param pagenum: 页码,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 236')
    requesturl = baseUrl + "/install/findGpsInstallRecord"
    LOGGER.info("Gps安装记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("Gps安装记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("Gps安装记录列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getGpsInstallDetail(id):
    """
    获取GPS安装记录详情
    :param id: GPS安装记录ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 237')
    requesturl = baseUrl + "/install/getGpsInstallDetail"
    LOGGER.info("获取GPS安装记录详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取GPS安装记录详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取GPS安装记录详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_saveGpsInstallRecord(financeid, gpsid, id, installer, place, time):
    """
    保存GPS安装记录
    :param time: 安装时间,必填参数,string
    :param id: GPS安装记录ID，编辑数据需要,integer
    :param gpsid: GPS记录ID,必填参数,integer
    :param place: 安装地点,必填参数,string
    :param financeid: 车牌号码记录对应id,必填参数,integer
    :param installer: 安装师傅,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 238')
    requesturl = baseUrl + "/install/saveGpsInstallRecord"
    LOGGER.info("保存GPS安装记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["gpsId"] = gpsid
    params["id"] = id
    params["installer"] = installer
    params["place"] = place
    params["time"] = time
    params["licences"] = LICENCES
    LOGGER.info("保存GPS安装记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存GPS安装记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_dismantle(id):
    """
    拆机，将gps安装记录拆除
    :param id: GPS安装记录ID,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 239')
    requesturl = baseUrl + "/install/dismantle"
    LOGGER.info("拆机，将gps安装记录拆除请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("拆机，将gps安装记录拆除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("拆机，将gps安装记录拆除请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getLowerOrg():
    """
    获取机构信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 240')
    requesturl = baseUrl + "/install/getLowerOrg"
    LOGGER.info("获取机构信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取机构信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取机构信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getGpsType():
    """
    获取GPS类型
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 241')
    requesturl = baseUrl + "/install/getGpsType"
    LOGGER.info("获取GPS类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取GPS类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取GPS类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_updateGpsInstallRecord(financeid, gpsid, id, installer, place, time):
    """
    更新GPS安装记录
    :param gpsid: GPS记录ID,必填参数,integer
    :param place: 安装地点,必填参数,string
    :param financeid: 车牌号码记录对应id,必填参数,integer
    :param installer: 安装师傅,必填参数,string
    :param time: 安装时间,必填参数,string
    :param id: GPS安装记录ID，编辑数据需要,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 242')
    requesturl = baseUrl + "/install/updateGpsInstallRecord"
    LOGGER.info("更新GPS安装记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["gpsId"] = gpsid
    params["id"] = id
    params["installer"] = installer
    params["place"] = place
    params["time"] = time
    params["licences"] = LICENCES
    LOGGER.info("更新GPS安装记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新GPS安装记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getDeviceByOrgCode(gpsid, orgcode):
    """
    根据所在机构获取GPS设备信息
    :param gpsid: GPS设备记录ID, 编辑的时候需要（该ID已在获取安装记录详情接口返回值中）,integer
    :param orgcode: 组织机构Code,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 243')
    requesturl = baseUrl + "/install/getDeviceByOrgCode"
    LOGGER.info("根据所在机构获取GPS设备信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsId"] = gpsid
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("根据所在机构获取GPS设备信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据所在机构获取GPS设备信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_deleteRecord(id):
    """
    删除安装记录，安装记录出错了，将错误数据删除
    :param id: GPS安装记录ID,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 244')
    requesturl = baseUrl + "/install/deleteRecord"
    LOGGER.info("删除安装记录，安装记录出错了，将错误数据删除请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("删除安装记录，安装记录出错了，将错误数据删除请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除安装记录，安装记录出错了，将错误数据删除请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_install_getDevice(keyword, orgcode):
    """
    获取GPS设备
    :param keyword: 查询关键字,必填参数,string
    :param orgcode: 组织机构Code,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 245')
    requesturl = baseUrl + "/install/getDevice"
    LOGGER.info("获取GPS设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("获取GPS设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取GPS设备请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_unlockUser(id):
    """
    解锁一个用户
    :param id: 解锁用户的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 246')
    requesturl = baseUrl + "/userManage/unlockUser"
    LOGGER.info("解锁一个用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("解锁一个用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("解锁一个用户请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_modifyUser(email, name, orgcode, phone, roleid, userid):
    """
    编辑用户保存
    :param email: 邮箱，唯一,必填参数,string
    :param roleid: 角色id,必填参数,integer
    :param name: 姓名,必填参数,string
    :param orgcode: 组织机构编号,必填参数,string
    :param userid: 用户ID，编辑数据需要,integer
    :param phone: 电话，唯一,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 247')
    requesturl = baseUrl + "/userManage/modifyUser"
    LOGGER.info("编辑用户保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["name"] = name
    params["orgCode"] = orgcode
    params["phone"] = phone
    params["roleid"] = roleid
    params["userid"] = userid
    params["licences"] = LICENCES
    LOGGER.info("编辑用户保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑用户保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_lockUser(id):
    """
    锁定一个用户
    :param id: 锁定用户的id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 248')
    requesturl = baseUrl + "/userManage/lockUser"
    LOGGER.info("锁定一个用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("锁定一个用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("锁定一个用户请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_deleteUser(userid):
    """
    删除用户
    :param userid: 用户ID,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 249')
    requesturl = baseUrl + "/userManage/deleteUser"
    LOGGER.info("删除用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["userid"] = userid
    params["licences"] = LICENCES
    LOGGER.info("删除用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除用户请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_getUserDetailByid(id):
    """
    编辑页面数据获取
    :param id: 用户id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 250')
    requesturl = baseUrl + "/userManage/getUserDetailByid"
    LOGGER.info("编辑页面数据获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("编辑页面数据获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑页面数据获取请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_getCreateUserInitData():
    """
    新增用户基础数据获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 251')
    requesturl = baseUrl + "/userManage/getCreateUserInitData"
    LOGGER.info("新增用户基础数据获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("新增用户基础数据获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户基础数据获取请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_pwdModifyPrecheck(key):
    """
    设置与修改密码连接有效期验证
    :param key: 修改密码连接对应的key,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 252')
    requesturl = baseUrl + "/userManage/pwdModifyPrecheck"
    LOGGER.info("设置与修改密码连接有效期验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    LOGGER.info("设置与修改密码连接有效期验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设置与修改密码连接有效期验证请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_getPersonalmsg(userid):
    """
    获取个人资料
    :param userid: 用户ID,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 253')
    requesturl = baseUrl + "/userManage/getPersonalmsg"
    LOGGER.info("获取个人资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["userid"] = userid
    params["licences"] = LICENCES
    LOGGER.info("获取个人资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取个人资料请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_pwdModifySendEmail(userid):
    """
    密码重置邮件发送
    :param userid: 用户id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 254')
    requesturl = baseUrl + "/userManage/pwdModifySendEmail"
    LOGGER.info("密码重置邮件发送请求地址:【{}】".format(requesturl))
    params = dict()
    params["userid"] = userid
    params["licences"] = LICENCES
    LOGGER.info("密码重置邮件发送请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("密码重置邮件发送请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_pwdModifyExecute(cachekey, pwd, userid):
    """
    执行密码修改
    :param pwd: 密码,必填参数,string
    :param cachekey: cacheKey,必填参数,string
    :param userid: 用户id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 255')
    requesturl = baseUrl + "/userManage/pwdModifyExecute"
    LOGGER.info("执行密码修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["cacheKey"] = cachekey
    params["pwd"] = pwd
    params["userid"] = userid
    LOGGER.info("执行密码修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("执行密码修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_update_updateGpsLocation():
    """
    updateGpsLocation
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 256')
    requesturl = baseUrl + "/update/updateGpsLocation"
    LOGGER.info("updateGpsLocation请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("updateGpsLocation请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("updateGpsLocation请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getWarnDetailById(warnid):
    """
    根据报警记录ID获取报警记录详情
    :param warnid: 风险点ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 257')
    requesturl = baseUrl + "/historyTrack/getWarnDetailById"
    LOGGER.info("根据报警记录ID获取报警记录详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["warnId"] = warnid
    params["licences"] = LICENCES
    LOGGER.info("根据报警记录ID获取报警记录详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据报警记录ID获取报警记录详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getHistoryLocation(id):
    """
    获取历史轨迹定位信息(单条记录，返回所有字段)
    :param id: 定位的id,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 258')
    requesturl = baseUrl + "/historyTrack/getHistoryLocation"
    LOGGER.info("获取历史轨迹定位信息(单条记录，返回所有字段)请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取历史轨迹定位信息(单条记录，返回所有字段)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取历史轨迹定位信息(单条记录，返回所有字段)请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getFinanceById(id):
    """
    根据financeId查询用户的车贷数据
    :param id: gps编号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 259')
    requesturl = baseUrl + "/historyTrack/getFinanceById"
    LOGGER.info("根据financeId查询用户的车贷数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("根据financeId查询用户的车贷数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据financeId查询用户的车贷数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getStationByGpsId(endtime, fid, gpsids, starttime, timecast):
    """
    根据gpsId查询相关的停车数据，查询所有
    :param timecast: 停车时长,ref
    :param gpsids: gps编号,必填参数,string
    :param starttime: 开始时间,string
    :param endtime: 结束时间,string
    :param fid: fid,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 260')
    requesturl = baseUrl + "/historyTrack/getStationByGpsId"
    LOGGER.info("根据gpsId查询相关的停车数据，查询所有请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["fid"] = fid
    params["gpsIds"] = gpsids
    params["startTime"] = starttime
    params["timeCast"] = timecast
    params["licences"] = LICENCES
    LOGGER.info("根据gpsId查询相关的停车数据，查询所有请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据gpsId查询相关的停车数据，查询所有请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getGpsByFinanceId(fid):
    """
    根据financeId查询绑定的GPS信息
    :param fid: 车贷数据id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 261')
    requesturl = baseUrl + "/historyTrack/getGpsByFinanceId"
    LOGGER.info("根据financeId查询绑定的GPS信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("根据financeId查询绑定的GPS信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据financeId查询绑定的GPS信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getRisksByOrgCode(orgcode):
    """
    通过车贷id查询相关的所有风险点
    :param orgcode: 组织机构,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 262')
    requesturl = baseUrl + "/historyTrack/getRisksByOrgCode"
    LOGGER.info("通过车贷id查询相关的所有风险点请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("通过车贷id查询相关的所有风险点请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("通过车贷id查询相关的所有风险点请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getFinanceByGpsCode(gpscode):
    """
    根据financeId查询用户的车贷数据
    :param gpscode: gps编号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 263')
    requesturl = baseUrl + "/historyTrack/getFinanceByGpsCode"
    LOGGER.info("根据financeId查询用户的车贷数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsCode"] = gpscode
    params["licences"] = LICENCES
    LOGGER.info("根据financeId查询用户的车贷数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据financeId查询用户的车贷数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getWarnsByGpsId(endtime, gpsids, starttime):
    """
    根据gpsid查询相关报警信息，可查询多个设备
    :param endtime: 结束时间,string
    :param gpsids: gps编号,必填参数,string
    :param starttime: 开始时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 264')
    requesturl = baseUrl + "/historyTrack/getWarnsByGpsId"
    LOGGER.info("根据gpsid查询相关报警信息，可查询多个设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["gpsIds"] = gpsids
    params["startTime"] = starttime
    params["licences"] = LICENCES
    LOGGER.info("根据gpsid查询相关报警信息，可查询多个设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据gpsid查询相关报警信息，可查询多个设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getRiskDtoById(id):
    """
    根据id查询风险点详情
    :param id: 风险点id,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 265')
    requesturl = baseUrl + "/historyTrack/getRiskDtoById"
    LOGGER.info("根据id查询风险点详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("根据id查询风险点详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据id查询风险点详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getHistoryLocationByPage(begin, endtime, gpscode, keywords, orgcode, page, size, starttime, timecast, tracktype):
    """
    获取历史轨迹(多条记录，分页查询)
    :param begin: ,integer
    :param endtime: 结束时间,string
    :param gpscode: gps编号,必填参数,string
    :param keywords: 查询关键字,string
    :param orgcode: 要查询的组织机构(部分接口使用),string
    :param page: 页数，从1开始,ref
    :param size: 页容量,ref
    :param starttime: 开始时间,string
    :param timecast: 时间间隔,必填参数,ref
    :param tracktype: 定位类型，1为GPS定位0为基站定位,null为所有,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 266')
    requesturl = baseUrl + "/historyTrack/getHistoryLocationByPage"
    LOGGER.info("获取历史轨迹(多条记录，分页查询)请求地址:【{}】".format(requesturl))
    params = dict()
    params["begin"] = begin
    params["endTime"] = endtime
    params["gpsCode"] = gpscode
    params["keywords"] = keywords
    params["orgCode"] = orgcode
    params["page"] = page
    params["size"] = size
    params["startTime"] = starttime
    params["timeCast"] = timecast
    params["trackType"] = tracktype
    params["licences"] = LICENCES
    LOGGER.info("获取历史轨迹(多条记录，分页查询)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取历史轨迹(多条记录，分页查询)请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyTrack_getHistoryTrack(endtime, gpscode, starttime, timecast, tracktype):
    """
    获取历史轨迹定位信息(全部，只返回定位相关)
    :param starttime: 开始时间，默认当天0点,string
    :param tracktype: 定位类型，1为GPS定位0为基站定位,null为所有,ref
    :param gpscode: gps编号,可用,分隔查询多个轨迹,必填参数,string
    :param timecast: 时间间隔,必填参数,ref
    :param endtime: 结束时间，默认至当前时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 267')
    requesturl = baseUrl + "/historyTrack/getHistoryTrack"
    LOGGER.info("获取历史轨迹定位信息(全部，只返回定位相关)请求地址:【{}】".format(requesturl))
    params = dict()
    params["endTime"] = endtime
    params["gpsCode"] = gpscode
    params["startTime"] = starttime
    params["timeCast"] = timecast
    params["trackType"] = tracktype
    params["licences"] = LICENCES
    LOGGER.info("获取历史轨迹定位信息(全部，只返回定位相关)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取历史轨迹定位信息(全部，只返回定位相关)请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnGeo_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    获取设备报警记录
    :param keyword: 查询关键字,string
    :param pagesize: 每页数量,必填参数,integer
    :param pagenum: 页码,必填参数,integer
    :param warnstatus: 报警处理状态（0：未处理，1：已处理）,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 268')
    requesturl = baseUrl + "/warnGeo/getWarns"
    LOGGER.info("获取设备报警记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("获取设备报警记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备报警记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_getRoleMoudels(roleid):
    """
    获取角色模块
    :param roleid: 角色id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 269')
    requesturl = baseUrl + "/role/getRoleMoudels"
    LOGGER.info("获取角色模块请求地址:【{}】".format(requesturl))
    params = dict()
    params["roleid"] = roleid
    params["licences"] = LICENCES
    LOGGER.info("获取角色模块请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色模块请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_updateRole(count, id, name, orgcode, remark):
    """
    修改角色数据
    :param id: id,integer
    :param orgcode: 机构代码,string
    :param remark: 描述,必填参数,string
    :param name: 角色名,必填参数,string
    :param count: ,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 270')
    requesturl = baseUrl + "/role/updateRole"
    LOGGER.info("修改角色数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["count"] = count
    params["id"] = id
    params["name"] = name
    params["orgCode"] = orgcode
    params["remark"] = remark
    params["licences"] = LICENCES
    LOGGER.info("修改角色数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改角色数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_getRoles(pagenum, pagesize):
    """
    获取角色列表
    :param pagenum: 页码,必填参数,ref
    :param pagesize: 每页展示记录数,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 271')
    requesturl = baseUrl + "/role/getRoles"
    LOGGER.info("获取角色列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("获取角色列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_deleteRole(id):
    """
    删除一个角色
    :param id: id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 272')
    requesturl = baseUrl + "/role/deleteRole"
    LOGGER.info("删除一个角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("删除一个角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一个角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_getRoleMoudelTree(roleid):
    """
    获取角色模块树
    :param roleid: 角色id,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 273')
    requesturl = baseUrl + "/role/getRoleMoudelTree"
    LOGGER.info("获取角色模块树请求地址:【{}】".format(requesturl))
    params = dict()
    params["roleid"] = roleid
    params["licences"] = LICENCES
    LOGGER.info("获取角色模块树请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色模块树请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_saveRoleMoudels(roleid, rolemoudellist):
    """
    保存角色权限
    :param rolemoudellist: json数据,必填参数,string
    :param roleid: roleId,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 274')
    requesturl = baseUrl + "/role/saveRoleMoudels"
    LOGGER.info("保存角色权限请求地址:【{}】".format(requesturl))
    params = dict()
    params["roleId"] = roleid
    params["roleMoudelList"] = rolemoudellist
    params["licences"] = LICENCES
    LOGGER.info("保存角色权限请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存角色权限请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_getDetail(id):
    """
    获取角色
    :param id: 页码,必填参数,ref
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 275')
    requesturl = baseUrl + "/role/getDetail"
    LOGGER.info("获取角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_role_addRole(count, id, name, orgcode, remark):
    """
    新增角色数据
    :param orgcode: 机构代码,string
    :param count: ,integer
    :param remark: 描述,必填参数,string
    :param id: ,integer
    :param name: 角色名,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 276')
    requesturl = baseUrl + "/role/addRole"
    LOGGER.info("新增角色数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["count"] = count
    params["id"] = id
    params["name"] = name
    params["orgCode"] = orgcode
    params["remark"] = remark
    params["licences"] = LICENCES
    LOGGER.info("新增角色数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增角色数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_addMoudel(component, dbname, id, jdbchost, jdbcpassword, jdbcuser, name, parentid, pattern, remark, type):
    """
    addMoudel
    :param pattern: pattern,string
    :param type: type,integer
    :param jdbcuser: jdbcuser,string
    :param jdbcpassword: jdbcpassword,string
    :param id: id,integer
    :param parentid: parentId,integer
    :param component: component,string
    :param jdbchost: jdbchost,string
    :param dbname: dbname,string
    :param name: name,string
    :param remark: remark,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 277')
    requesturl = baseUrl + "/manage/addMoudel"
    LOGGER.info("addMoudel请求地址:【{}】".format(requesturl))
    params = dict()
    params["component"] = component
    params["dbname"] = dbname
    params["id"] = id
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["name"] = name
    params["parentId"] = parentid
    params["pattern"] = pattern
    params["remark"] = remark
    params["type"] = type
    LOGGER.info("addMoudel请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("addMoudel请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_createSuperAdmin(companyid, dbname, email, jdbchost, jdbcpassword, jdbcuser, name, orgcode, phone):
    """
    createSuperAdmin
    :param jdbcuser: jdbcuser,string
    :param companyid: companyId,integer
    :param phone: phone,string
    :param jdbchost: jdbchost,string
    :param email: email,string
    :param name: name,string
    :param jdbcpassword: jdbcpassword,string
    :param orgcode: orgCode,string
    :param dbname: dbname,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 278')
    requesturl = baseUrl + "/manage/createSuperAdmin"
    LOGGER.info("createSuperAdmin请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["dbname"] = dbname
    params["email"] = email
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["name"] = name
    params["orgCode"] = orgcode
    params["phone"] = phone
    LOGGER.info("createSuperAdmin请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("createSuperAdmin请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_reSendEmail(companyid, companyuserid, dbname, jdbchost, jdbcpassword, jdbcuser, userid):
    """
    reSendEmail
    :param userid: userId,integer
    :param jdbchost: jdbchost,string
    :param dbname: dbname,string
    :param companyid: companyId,integer
    :param jdbcpassword: jdbcpassword,string
    :param companyuserid: companyUserId,integer
    :param jdbcuser: jdbcuser,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 279')
    requesturl = baseUrl + "/manage/reSendEmail"
    LOGGER.info("reSendEmail请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["companyUserId"] = companyuserid
    params["dbname"] = dbname
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["userId"] = userid
    LOGGER.info("reSendEmail请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("reSendEmail请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_updateSuperAdmin(dbname, email, id, jdbchost, jdbcpassword, jdbcuser, name, phone):
    """
    updateSuperAdmin
    :param dbname: dbname,string
    :param jdbchost: jdbchost,string
    :param name: name,string
    :param email: email,string
    :param jdbcuser: jdbcuser,string
    :param jdbcpassword: jdbcpassword,string
    :param id: id,integer
    :param phone: phone,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 280')
    requesturl = baseUrl + "/manage/updateSuperAdmin"
    LOGGER.info("updateSuperAdmin请求地址:【{}】".format(requesturl))
    params = dict()
    params["dbname"] = dbname
    params["email"] = email
    params["id"] = id
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["name"] = name
    params["phone"] = phone
    LOGGER.info("updateSuperAdmin请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("updateSuperAdmin请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_delmoudel(dbname, id, jdbchost, jdbcpassword, jdbcuser):
    """
    delMoudel
    :param jdbcpassword: jdbcpassword,string
    :param jdbcuser: jdbcuser,string
    :param id: id,integer
    :param dbname: dbname,string
    :param jdbchost: jdbchost,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 281')
    requesturl = baseUrl + "/manage/delmoudel"
    LOGGER.info("delMoudel请求地址:【{}】".format(requesturl))
    params = dict()
    params["dbname"] = dbname
    params["id"] = id
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    LOGGER.info("delMoudel请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("delMoudel请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_delSuperAdmin(companyid, dbname, jdbchost, jdbcpassword, jdbcuser, userid):
    """
    delSuperAdmin
    :param dbname: dbname,string
    :param jdbcpassword: jdbcpassword,string
    :param jdbcuser: jdbcuser,string
    :param userid: userId,integer
    :param jdbchost: jdbchost,string
    :param companyid: companyId,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 282')
    requesturl = baseUrl + "/manage/delSuperAdmin"
    LOGGER.info("delSuperAdmin请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["dbname"] = dbname
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["userId"] = userid
    LOGGER.info("delSuperAdmin请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("delSuperAdmin请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_unlockUser(dbname, jdbchost, jdbcpassword, jdbcuser, userid):
    """
    unlockUser
    :param jdbcpassword: jdbcpassword,string
    :param userid: userId,integer
    :param jdbcuser: jdbcuser,string
    :param jdbchost: jdbchost,string
    :param dbname: dbname,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 283')
    requesturl = baseUrl + "/manage/unlockUser"
    LOGGER.info("unlockUser请求地址:【{}】".format(requesturl))
    params = dict()
    params["dbname"] = dbname
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["userId"] = userid
    LOGGER.info("unlockUser请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("unlockUser请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_lockCompanyAfterLogoutUsers(companyid):
    """
    lockCompanyAfterLogoutUsers
    :param companyid: companyId,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 284')
    requesturl = baseUrl + "/manage/lockCompanyAfterLogoutUsers"
    LOGGER.info("lockCompanyAfterLogoutUsers请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    LOGGER.info("lockCompanyAfterLogoutUsers请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("lockCompanyAfterLogoutUsers请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_updateRootOrg(code, dbname, description, id, jdbchost, jdbcpassword, jdbcuser, name):
    """
    updateRootOrg
    :param dbname: dbname,string
    :param code: code,string
    :param name: name,string
    :param description: description,string
    :param jdbcuser: jdbcuser,string
    :param jdbchost: jdbchost,string
    :param id: id,integer
    :param jdbcpassword: jdbcpassword,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 285')
    requesturl = baseUrl + "/manage/updateRootOrg"
    LOGGER.info("updateRootOrg请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["dbname"] = dbname
    params["description"] = description
    params["id"] = id
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["name"] = name
    LOGGER.info("updateRootOrg请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("updateRootOrg请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_lockUser(companyid, dbname, jdbchost, jdbcpassword, jdbcuser, userid):
    """
    lockUser
    :param companyid: companyId,integer
    :param dbname: dbname,string
    :param jdbcuser: jdbcuser,string
    :param jdbcpassword: jdbcpassword,string
    :param jdbchost: jdbchost,string
    :param userid: userId,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 286')
    requesturl = baseUrl + "/manage/lockUser"
    LOGGER.info("lockUser请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["dbname"] = dbname
    params["jdbchost"] = jdbchost
    params["jdbcpassword"] = jdbcpassword
    params["jdbcuser"] = jdbcuser
    params["userId"] = userid
    LOGGER.info("lockUser请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("lockUser请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_monitor_getWarns(id, pagenum, pagesize):
    """
    查询报警列表
    :param pagenum: 页数,number
    :param pagesize: 每页条数,number
    :param id: gps的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 287')
    requesturl = baseUrl + "/monitor/getWarns"
    LOGGER.info("查询报警列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("查询报警列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询报警列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnhb_saveThreshold(threshold):
    """
    未回家/公司阀值设置
    :param threshold: 阀值,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 288')
    requesturl = baseUrl + "/warnhb/saveThreshold"
    LOGGER.info("未回家/公司阀值设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["threshold"] = threshold
    params["licences"] = LICENCES
    LOGGER.info("未回家/公司阀值设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("未回家/公司阀值设置请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnhb_getThreshold():
    """
    未回家/公司阀值获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 289')
    requesturl = baseUrl + "/warnhb/getThreshold"
    LOGGER.info("未回家/公司阀值获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("未回家/公司阀值获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("未回家/公司阀值获取请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnhb_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    查询未回家/公司报警
    :param warnstatus: 报警状态,string
    :param pagesize: 每页条数,number
    :param pagenum: 页数,number
    :param keyword: 查询关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 290')
    requesturl = baseUrl + "/warnhb/getWarns"
    LOGGER.info("查询未回家/公司报警请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("查询未回家/公司报警请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询未回家/公司报警请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnhb_getStations(id):
    """
    查询停车记录
    :param id: 报警id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 291')
    requesturl = baseUrl + "/warnhb/getStations"
    LOGGER.info("查询停车记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("查询停车记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询停车记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnhb_getFinanceInfo(financeid):
    """
    查询用户住址信息
    :param financeid: 车贷数据id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 292')
    requesturl = baseUrl + "/warnhb/getFinanceInfo"
    LOGGER.info("查询用户住址信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["licences"] = LICENCES
    LOGGER.info("查询用户住址信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户住址信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_warnOver_getWarns(keyword, pagenum, pagesize, warnstatus):
    """
    查询逾期报警
    :param warnstatus: 报警状态,string
    :param keyword: 查询关键字,string
    :param pagesize: 每页条数,number
    :param pagenum: 页数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 293')
    requesturl = baseUrl + "/warnOver/getWarns"
    LOGGER.info("查询逾期报警请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["warnStatus"] = warnstatus
    params["licences"] = LICENCES
    LOGGER.info("查询逾期报警请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询逾期报警请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_payOver(borrowdate, date, id):
    """
    还款完成
    :param date: 还款完成时间,string
    :param id: id,number
    :param borrowdate: 放款时间,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 294')
    requesturl = baseUrl + "/finance/payOver"
    LOGGER.info("还款完成请求地址:【{}】".format(requesturl))
    params = dict()
    params["borrowDate"] = borrowdate
    params["date"] = date
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("还款完成请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款完成请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_overDue(borrowdate, date, id, isoverdue, overdue):
    """
    逾期设置
    :param date: 逾期日期,string
    :param id: id,number
    :param overdue: 是否逾期,number
    :param borrowdate: 放款日期,string
    :param isoverdue: 是否已经存在逾期记录，用于解决并发BUG,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 295')
    requesturl = baseUrl + "/finance/overDue"
    LOGGER.info("逾期设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["borrowDate"] = borrowdate
    params["date"] = date
    params["id"] = id
    params["isOverdue"] = isoverdue
    params["overdue"] = overdue
    params["licences"] = LICENCES
    LOGGER.info("逾期设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期设置请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_finance_getDetail(id):
    """
    获取车贷数据详情
    :param id: 每页的数据量,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 296')
    requesturl = baseUrl + "/finance/getDetail"
    LOGGER.info("获取车贷数据详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("获取车贷数据详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车贷数据详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_getCarFinance(fid):
    """
    获取车辆的车贷数据
    :param fid: 关联车牌号码对应id,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 297')
    requesturl = baseUrl + "/historyCarRecord/getCarFinance"
    LOGGER.info("获取车辆的车贷数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["fid"] = fid
    params["licences"] = LICENCES
    LOGGER.info("获取车辆的车贷数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取车辆的车贷数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_sendPasswordSecurity(username):
    """
    发送修改密码的验证码
    :param username: 用户的帐户,可以是邮箱或手机号,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 298')
    requesturl = baseUrl + "/user/sendPasswordSecurity"
    LOGGER.info("发送修改密码的验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["userName"] = username
    LOGGER.info("发送修改密码的验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送修改密码的验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_updatePhoneBySecurity(password, phone, security):
    """
    根据验证码修改手机号
    :param security: 验证码,必填参数,string
    :param phone: 用户需要变更的新手机号,必填参数,string
    :param password: 用户的登陆密码,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 299')
    requesturl = baseUrl + "/user/updatePhoneBySecurity"
    LOGGER.info("根据验证码修改手机号请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["phone"] = phone
    params["security"] = security
    params["licences"] = LICENCES
    LOGGER.info("根据验证码修改手机号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据验证码修改手机号请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_showPassword(companyid, id):
    """
    mange查看用户密码
    :param id: 用户id,number
    :param companyid: 用户所在公司id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 300')
    requesturl = baseUrl + "/cuser/showPassword"
    LOGGER.info("mange查看用户密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["id"] = id
    params["licences"] = LICENCES
    LOGGER.info("mange查看用户密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("mange查看用户密码请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_userManage_getUsers(keyword, pagenum, pagesize):
    """
    系统用户列表
    :param pagenum: 页码,必填参数,integer
    :param pagesize: 每页显示数量,必填参数,integer
    :param keyword: 用户名或电话号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 301')
    requesturl = baseUrl + "/userManage/getUsers"
    LOGGER.info("系统用户列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("系统用户列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("系统用户列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_updateGroup(groupid, groupname):
    """
    修改分组
    :param groupid: 待修改分组ID,必填参数,number
    :param groupname: 新的分组名称,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 302')
    requesturl = baseUrl + "/realtime/updateGroup"
    LOGGER.info("修改分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["groupName"] = groupname
    params["licences"] = LICENCES
    LOGGER.info("修改分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_deleteGroup(groupid):
    """
    删除分组
    :param groupid: 待删除分组ID,必填参数,integer
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 303')
    requesturl = baseUrl + "/realtime/deleteGroup"
    LOGGER.info("删除分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["licences"] = LICENCES
    LOGGER.info("删除分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_addGroup(groupname, orgcode):
    """
    新增分组
    :param groupname: 分组名称,必填参数,string
    :param orgcode: 分组名称,必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 304')
    requesturl = baseUrl + "/realtime/addGroup"
    LOGGER.info("新增分组请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupName"] = groupname
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("新增分组请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增分组请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getOrg():
    """
    获取当前登录用户的组织机构树形信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 305')
    requesturl = baseUrl + "/realtime/getOrg"
    LOGGER.info("获取当前登录用户的组织机构树形信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["licences"] = LICENCES
    LOGGER.info("获取当前登录用户的组织机构树形信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前登录用户的组织机构树形信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_associate(keyword):
    """
    全局联想搜索
    :param keyword: 关键字，必填参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 306')
    requesturl = baseUrl + "/realtime/associate"
    LOGGER.info("全局联想搜索请求地址:【{}】".format(requesturl))
    params = dict()
    params["keyWord"] = keyword
    params["licences"] = LICENCES
    LOGGER.info("全局联想搜索请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全局联想搜索请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getDeviceList(devicecondition, deviceorder, groupid, linestatus, orgcode, type):
    """
    查询分组,按设备显示
    :param devicecondition: 设备查询条件，WARN只查看报警, UNACTIVE 只看未激活，NULL查询全部，必填,string
    :param deviceorder: 排序，CAR按车贷记录创建时间，NO按车牌号,string
    :param linestatus: 设备状态，0离线1在线2无线，99全部,number
    :param orgcode: 机构编号，必填,string
    :param type: 查询类型，0 查询全部分组的所有数据，1 查询指定的一个分组的数据，必填,number
    :param groupid: 分组id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 307')
    requesturl = baseUrl + "/realtime/getDeviceList"
    LOGGER.info("查询分组,按设备显示请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceCondition"] = devicecondition
    params["deviceOrder"] = deviceorder
    params["groupId"] = groupid
    params["lineStatus"] = linestatus
    params["orgCode"] = orgcode
    params["type"] = type
    params["licences"] = LICENCES
    LOGGER.info("查询分组,按设备显示请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询分组,按设备显示请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getCarList(devicecondition, deviceorder, groupid, linestatus, orgcode, type):
    """
    查询分组,按车辆查询
    :param devicecondition: 设备查询条件，WARN只查看报警, OVERDUE 只看逾期，NULL查询全部，必填,string
    :param deviceorder: 排序，CAR按车贷记录创建时间，NO按车牌号,string
    :param linestatus: 设备状态，0离线1在线，99全部,number
    :param orgcode: 机构编号，必填,string
    :param type: 查询类型，0 查询全部分组的所有数据，1 查询指定的一个分组的数据，必填,number
    :param groupid: 分组id，type=1时有效,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 308')
    requesturl = baseUrl + "/realtime/getCarList"
    LOGGER.info("查询分组,按车辆查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["deviceCondition"] = devicecondition
    params["deviceOrder"] = deviceorder
    params["groupId"] = groupid
    params["lineStatus"] = linestatus
    params["orgCode"] = orgcode
    params["type"] = type
    params["licences"] = LICENCES
    LOGGER.info("查询分组,按车辆查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询分组,按车辆查询请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getDeviceByCar(financeid):
    """
    查询同车设备
    :param financeid: 车辆id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 309')
    requesturl = baseUrl + "/realtime/getDeviceByCar"
    LOGGER.info("查询同车设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["licences"] = LICENCES
    LOGGER.info("查询同车设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询同车设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_carRelationChange(financelist, groupid):
    """
    车辆转移
    :param financelist: 车辆id,string
    :param groupid: 分组id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 310')
    requesturl = baseUrl + "/realtime/carRelationChange"
    LOGGER.info("车辆转移请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeList"] = financelist
    params["groupId"] = groupid
    params["licences"] = LICENCES
    LOGGER.info("车辆转移请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("车辆转移请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getWarnsByDevice(gpsid):
    """
    查看设备报警
    :param gpsid: 设备id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 311')
    requesturl = baseUrl + "/realtime/getWarnsByDevice"
    LOGGER.info("查看设备报警请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsId"] = gpsid
    params["licences"] = LICENCES
    LOGGER.info("查看设备报警请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看设备报警请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getDeviceLocation(gpsid):
    """
    获取设备详情
    :param gpsid: 设备id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 312')
    requesturl = baseUrl + "/realtime/getDeviceLocation"
    LOGGER.info("获取设备详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsId"] = gpsid
    params["licences"] = LICENCES
    LOGGER.info("获取设备详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取设备详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getWarnsByCar(financeid, pagenum, pagesize):
    """
    查看车辆报警
    :param financeid: 车辆id,number
    :param pagesize: ,number
    :param pagenum: ,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 313')
    requesturl = baseUrl + "/realtime/getWarnsByCar"
    LOGGER.info("查看车辆报警请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licences"] = LICENCES
    LOGGER.info("查看车辆报警请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看车辆报警请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_mainDevice(financeid, gpsid):
    """
    设置主设备
    :param financeid: 车辆id,number
    :param gpsid: 设备id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 314')
    requesturl = baseUrl + "/realtime/mainDevice"
    LOGGER.info("设置主设备请求地址:【{}】".format(requesturl))
    params = dict()
    params["financeId"] = financeid
    params["gpsId"] = gpsid
    params["licences"] = LICENCES
    LOGGER.info("设置主设备请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设置主设备请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_historyCarRecord_addRemark(device):
    """
    设备备注设置
    :param device: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 315')
    requesturl = baseUrl + "/historyCarRecord/addRemark"
    LOGGER.info("设备备注设置请求地址:【{}】".format(requesturl))
    params = dict()
    params["device"] = device
    params["licences"] = LICENCES
    LOGGER.info("设备备注设置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设备备注设置请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_findGroups(orgcode):
    """
    查询分组列表
    :param orgcode: 机构编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 316')
    requesturl = baseUrl + "/realtime/findGroups"
    LOGGER.info("查询分组列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["orgCode"] = orgcode
    params["licences"] = LICENCES
    LOGGER.info("查询分组列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询分组列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_realtime_getCarByGroup(groupid, keyword, orgcode, pagenum, pagesize, type):
    """
    查询分组下的车辆
    :param groupid: 分组id，如果type=0时，groupId需要为null,number
    :param type: 查询类型，1 查询分组下的数据，0查询全部数据,number
    :param orgcode: 机构编号，如果type=0，需要添加rogCode,string
    :param pagenum: 分页数,number
    :param pagesize: 分页大小,number
    :param keyword: 查询关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 317')
    requesturl = baseUrl + "/realtime/getCarByGroup"
    LOGGER.info("查询分组下的车辆请求地址:【{}】".format(requesturl))
    params = dict()
    params["groupId"] = groupid
    params["keyWord"] = keyword
    params["orgCode"] = orgcode
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["type"] = type
    params["licences"] = LICENCES
    LOGGER.info("查询分组下的车辆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询分组下的车辆请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


