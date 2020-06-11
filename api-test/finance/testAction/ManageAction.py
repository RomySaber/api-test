#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : ManageAction.py
@desc       : 项目：finance 模块：manage 接口方法封装
"""

from finance.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('manage_apiURL', 'finance')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_manage_login()


def test_checkPasswordUrl(key):
    """
    修改密码连接有效性验证
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1')
    requesturl = baseUrl + "/checkPasswordUrl"
    LOGGER.info("修改密码连接有效性验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    LOGGER.info("修改密码连接有效性验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改密码连接有效性验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_login(account, password):
    """
    登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2')
    requesturl = baseUrl + "/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["account"] = account
    params["password"] = password
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_logout():
    """
    登出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3')
    requesturl = baseUrl + "/logout"
    LOGGER.info("登出请求地址:【{}】".format(requesturl))
    params = dict()
    params["licence"] = LICENCES
    LOGGER.info("登出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登出请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_updatePassword(manageid, newpassword):
    """
    设置或更新密码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 4')
    requesturl = baseUrl + "/updatePassword"
    LOGGER.info("设置或更新密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["manageId"] = manageid
    params["newPassword"] = newpassword
    LOGGER.info("设置或更新密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("设置或更新密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_companies(orderid):
    """
    获取企业列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 5')
    requesturl = baseUrl + "/cuser/companies"
    LOGGER.info("获取企业列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("获取企业列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取企业列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_delete(currentpage, id, pagesize, state):
    """
    删除管理员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 6')
    requesturl = baseUrl + "/cuser/delete"
    LOGGER.info("删除管理员请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["id"] = id
    params["pageSize"] = pagesize
    params["state"] = state
    params["licence"] = LICENCES
    LOGGER.info("删除管理员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除管理员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_detail(companyuserid):
    """
    获取管理员详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 7')
    requesturl = baseUrl + "/cuser/detail"
    LOGGER.info("获取管理员详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyUserId"] = companyuserid
    params["licence"] = LICENCES
    LOGGER.info("获取管理员详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取管理员详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_list(pagenum, pagesize):
    """
    管理员列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 8')
    requesturl = baseUrl + "/cuser/list"
    LOGGER.info("管理员列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licence"] = LICENCES
    LOGGER.info("管理员列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("管理员列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_lock(id):
    """
    锁定管理员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 9')
    requesturl = baseUrl + "/cuser/lock"
    LOGGER.info("锁定管理员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("锁定管理员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("锁定管理员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_save(companyid, id, useremail, username, userphone):
    """
    添加管理员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 10')
    requesturl = baseUrl + "/cuser/save"
    LOGGER.info("添加管理员请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["id"] = id
    params["userEmail"] = useremail
    params["userName"] = username
    params["userPhone"] = userphone
    params["licence"] = LICENCES
    LOGGER.info("添加管理员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加管理员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_sendActiveEmail(id):
    """
    重发激活邮件
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 11')
    requesturl = baseUrl + "/cuser/sendActiveEmail"
    LOGGER.info("重发激活邮件请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("重发激活邮件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重发激活邮件请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_unlock(id):
    """
    解锁管理员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 12')
    requesturl = baseUrl + "/cuser/unlock"
    LOGGER.info("解锁管理员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("解锁管理员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("解锁管理员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_cuser_update(companyid, id, useremail, username, userphone):
    """
    编辑管理员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 13')
    requesturl = baseUrl + "/cuser/update"
    LOGGER.info("编辑管理员请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["id"] = id
    params["userEmail"] = useremail
    params["userName"] = username
    params["userPhone"] = userphone
    params["licence"] = LICENCES
    LOGGER.info("编辑管理员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑管理员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_delete(id):
    """
    删除运营人员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 14')
    requesturl = baseUrl + "/manage/delete"
    LOGGER.info("删除运营人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("删除运营人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除运营人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_detail(manageid):
    """
    获取运营人员详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 15')
    requesturl = baseUrl + "/manage/detail"
    LOGGER.info("获取运营人员详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["manageId"] = manageid
    params["licence"] = LICENCES
    LOGGER.info("获取运营人员详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取运营人员详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_list(pagenum, pagesize):
    """
    运营人员列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 16')
    requesturl = baseUrl + "/manage/list"
    LOGGER.info("运营人员列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licence"] = LICENCES
    LOGGER.info("运营人员列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营人员列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_lock(id):
    """
    锁定运营人员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 17')
    requesturl = baseUrl + "/manage/lock"
    LOGGER.info("锁定运营人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("锁定运营人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("锁定运营人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_roles():
    """
    获取角色列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 18')
    requesturl = baseUrl + "/manage/roles"
    LOGGER.info("获取角色列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["licence"] = LICENCES
    LOGGER.info("获取角色列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_save(id, manageemail, managename, managephone, roleid):
    """
    添加运营人员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 19')
    requesturl = baseUrl + "/manage/save"
    LOGGER.info("添加运营人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["manageEmail"] = manageemail
    params["manageName"] = managename
    params["managePhone"] = managephone
    params["roleId"] = roleid
    params["licence"] = LICENCES
    LOGGER.info("添加运营人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加运营人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_sendActiveEmail(id):
    """
    重发激活邮件
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 20')
    requesturl = baseUrl + "/manage/sendActiveEmail"
    LOGGER.info("重发激活邮件请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("重发激活邮件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("重发激活邮件请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_unlock(id):
    """
    解锁运营人员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 21')
    requesturl = baseUrl + "/manage/unlock"
    LOGGER.info("解锁运营人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["licence"] = LICENCES
    LOGGER.info("解锁运营人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("解锁运营人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_manage_update(id, manageemail, managename, managephone, roleid):
    """
    编辑运营人员
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 22')
    requesturl = baseUrl + "/manage/update"
    LOGGER.info("编辑运营人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["manageEmail"] = manageemail
    params["manageName"] = managename
    params["managePhone"] = managephone
    params["roleId"] = roleid
    params["licence"] = LICENCES
    LOGGER.info("编辑运营人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑运营人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_appLogin(account, appversion, deviceversion, sysname, sysversion):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 23')
    requesturl = baseUrl + "/open/appLogin"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["account"] = account
    params["appVersion"] = appversion
    params["deviceVersion"] = deviceversion
    params["sysName"] = sysname
    params["sysVersion"] = sysversion
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_checkAccount(email, phone):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 24')
    requesturl = baseUrl + "/open/checkAccount"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["phone"] = phone
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_createRelation(companyid, email, mobile, userid, username, userstatus, usertype):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 25')
    requesturl = baseUrl + "/open/createRelation"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["email"] = email
    params["mobile"] = mobile
    params["userId"] = userid
    params["userName"] = username
    params["userStatus"] = userstatus
    params["userType"] = usertype
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_deleteRelation(companyid, userid):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 26')
    requesturl = baseUrl + "/open/deleteRelation"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["userId"] = userid
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_getAllDataSource():
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 27')
    requesturl = baseUrl + "/open/getAllDataSource"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_getDataSource(companyid):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 28')
    requesturl = baseUrl + "/open/getDataSource"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_login(account):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 29')
    requesturl = baseUrl + "/open/login"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["account"] = account
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_queryCompanyMoudels(companyid):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 30')
    requesturl = baseUrl + "/open/queryCompanyMoudels"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_open_updateRelation(companyid, email, mobile, userid, username, userstatus, usertype):
    """
    
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 31')
    requesturl = baseUrl + "/open/updateRelation"
    LOGGER.info("请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["email"] = email
    params["mobile"] = mobile
    params["userId"] = userid
    params["userName"] = username
    params["userStatus"] = userstatus
    params["userType"] = usertype
    LOGGER.info("请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_detail(companyid):
    """
    获取企业详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 32')
    requesturl = baseUrl + "/company/detail"
    LOGGER.info("获取企业详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["licence"] = LICENCES
    LOGGER.info("获取企业详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取企业详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_list(pagenum, pagesize):
    """
    企业管理列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 33')
    requesturl = baseUrl + "/company/list"
    LOGGER.info("企业管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["licence"] = LICENCES
    LOGGER.info("企业管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("企业管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_lock(companyid):
    """
    停用企业
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 34')
    requesturl = baseUrl + "/company/lock"
    LOGGER.info("停用企业请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["licence"] = LICENCES
    LOGGER.info("停用企业请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("停用企业请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_save(description, id, licencecode, licencefileid, linkman, linkphone, name):
    """
    保存企业
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 35')
    requesturl = baseUrl + "/company/save"
    LOGGER.info("保存企业请求地址:【{}】".format(requesturl))
    params = dict()
    params["description"] = description
    params["id"] = id
    params["licenceCode"] = licencecode
    params["licenceFileId"] = licencefileid
    params["linkMan"] = linkman
    params["linkPhone"] = linkphone
    params["name"] = name
    params["licence"] = LICENCES
    LOGGER.info("保存企业请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存企业请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_unlock(companyid):
    """
    启用企业
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 36')
    requesturl = baseUrl + "/company/unlock"
    LOGGER.info("启用企业请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyId"] = companyid
    params["licence"] = LICENCES
    LOGGER.info("启用企业请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("启用企业请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_company_update(description, id, licencecode, licencefileid, linkman, linkphone, name):
    """
    编辑企业
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 37')
    requesturl = baseUrl + "/company/update"
    LOGGER.info("编辑企业请求地址:【{}】".format(requesturl))
    params = dict()
    params["description"] = description
    params["id"] = id
    params["licenceCode"] = licencecode
    params["licenceFileId"] = licencefileid
    params["linkMan"] = linkman
    params["linkPhone"] = linkphone
    params["name"] = name
    params["licence"] = LICENCES
    LOGGER.info("编辑企业请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑企业请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 76')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 77')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 78')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 79')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 80')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 81')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 82')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 83')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 84')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 85')
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


