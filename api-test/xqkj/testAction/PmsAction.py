#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : PmsAction.py
@desc       : 项目：xqkj 模块：pms 接口方法封装
"""

from xqkj.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('pms_apiURL', 'xqkj')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_pms_login()
API_TEST_HEADERS['token'] = LICENCES


def test_platform_tenant_add(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    1.机构新增
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param signature: 签名,string
    :param obj: 业务消息体,object
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1204')
    requesturl = baseUrl + "/platform/tenant/add"
    LOGGER.info("1.机构新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("1.机构新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.机构新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_tenant_edit(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    2.机构编辑
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1205')
    requesturl = baseUrl + "/platform/tenant/edit"
    LOGGER.info("2.机构编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("2.机构编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2.机构编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_tenant_change_state(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    3.机构状态管理
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1206')
    requesturl = baseUrl + "/platform/tenant/change_state"
    LOGGER.info("3.机构状态管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("3.机构状态管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3.机构状态管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_admin_add(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    1.机构管理员增加
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1207')
    requesturl = baseUrl + "/platform/admin/add"
    LOGGER.info("1.机构管理员增加请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("1.机构管理员增加请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.机构管理员增加请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_admin_edit(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    2.机构管理员编辑
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1208')
    requesturl = baseUrl + "/platform/admin/edit"
    LOGGER.info("2.机构管理员编辑请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("2.机构管理员编辑请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2.机构管理员编辑请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_admin_change_state(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    3.机构管理员状态管理
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1209')
    requesturl = baseUrl + "/platform/admin/change_state"
    LOGGER.info("3.机构管理员状态管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("3.机构管理员状态管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3.机构管理员状态管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_permission_set(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    1.机构权限重设
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1210')
    requesturl = baseUrl + "/platform/permission/set"
    LOGGER.info("1.机构权限重设请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("1.机构权限重设请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.机构权限重设请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_config_set(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    1.设置配置项的值
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1211')
    requesturl = baseUrl + "/platform/config/set"
    LOGGER.info("1.设置配置项的值请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("1.设置配置项的值请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.设置配置项的值请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_all_query(businesssystemuuid, nonce, signature, timestamp):
    """
    1.全量配置查询接口
    :param timestamp: 时间戳,number
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param signature: 签名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1212')
    requesturl = baseUrl + "/platform/all/query"
    LOGGER.info("1.全量配置查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("1.全量配置查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.全量配置查询接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_platform_admin_reset_password(businesssystemuuid, nonce, obj, signature, timestamp):
    """
    4.机构管理员密码重置
    :param businesssystemuuid: 业务系统唯一标识,string
    :param nonce: 随机串,string
    :param obj: 业务消息体,object
    :param signature: 签名,string
    :param timestamp: 时间戳,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1213')
    requesturl = baseUrl + "/platform/admin/reset_password"
    LOGGER.info("4.机构管理员密码重置请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["nonce"] = nonce
    params["obj"] = obj
    params["signature"] = signature
    params["timestamp"] = timestamp
    LOGGER.info("4.机构管理员密码重置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4.机构管理员密码重置请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_login(email, password):
    """
    登陆请求
    :param password: 密码,string
    :param email: 登录名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1214')
    requesturl = baseUrl + "/login"
    LOGGER.info("登陆请求请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["password"] = password
    LOGGER.info("登陆请求请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆请求请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_findpassword(email):
    """
    提交密码找回请求
    :param email: 邮箱地址,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1215')
    requesturl = baseUrl + "/findpassword"
    LOGGER.info("提交密码找回请求请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    LOGGER.info("提交密码找回请求请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交密码找回请求请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_validatekey(key):
    """
    检测Key是否有效接口
    :param key: 重置密码标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1216')
    requesturl = baseUrl + "/validatekey"
    LOGGER.info("检测Key是否有效接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    LOGGER.info("检测Key是否有效接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("检测Key是否有效接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_reset(key, password):
    """
    密码重置接口
    :param key: 重置密码标识,string
    :param password: 密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1217')
    requesturl = baseUrl + "/reset"
    LOGGER.info("密码重置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    params["password"] = password
    LOGGER.info("密码重置接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("密码重置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_list(currentpage, name, pagesize):
    """
    列表查询接口
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :param name: 系统名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1218')
    requesturl = baseUrl + "/backstage/system/list"
    LOGGER.info("列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_chage_state(changeto, id):
    """
    系统状态管理接口
    :param changeto: 变更为指定状态,string
    :param id: 业务系统Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1219')
    requesturl = baseUrl + "/backstage/system/chage_state"
    LOGGER.info("系统状态管理接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["changeTo"] = changeto
    params["id"] = id
    LOGGER.info("系统状态管理接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("系统状态管理接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_add(businesssystemuuid, host, name, secret):
    """
    新增系统接口
    :param name: 业务系统名称,string
    :param businesssystemuuid: 业务系统标识,string
    :param secret: 业务系统密钥,string
    :param host: 业务系统地址,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1220')
    requesturl = baseUrl + "/backstage/system/add"
    LOGGER.info("新增系统接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["host"] = host
    params["name"] = name
    params["secret"] = secret
    LOGGER.info("新增系统接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增系统接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_info(id):
    """
    系统详情接口
    :param id: 系统id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1221')
    requesturl = baseUrl + "/backstage/system/info"
    LOGGER.info("系统详情接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("系统详情接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("系统详情接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_edit(businesssystemuuid, host, id, name, secret):
    """
    编辑系统接口
    :param host: 业务系统地址,string
    :param secret: 业务系统密钥,string
    :param id: 业务系统id,number
    :param name: 业务系统名称,string
    :param businesssystemuuid: 业务系统标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1222')
    requesturl = baseUrl + "/backstage/system/edit"
    LOGGER.info("编辑系统接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessSystemUuid"] = businesssystemuuid
    params["host"] = host
    params["id"] = id
    params["name"] = name
    params["secret"] = secret
    LOGGER.info("编辑系统接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑系统接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_permission_info(id):
    """
    权限查询接口
    :param id: 业务系统id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1223')
    requesturl = baseUrl + "/backstage/system/permission/info"
    LOGGER.info("权限查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("权限查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("权限查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_permission_set(id, permissions):
    """
    权限编辑接口
    :param id: 业务系统id,number
    :param permissions: 系统权限,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1224')
    requesturl = baseUrl + "/backstage/system/permission/set"
    LOGGER.info("权限编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["permissions"] = permissions
    LOGGER.info("权限编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("权限编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_config_info(id):
    """
    配置查询接口
    :param id: 业务系统id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1225')
    requesturl = baseUrl + "/backstage/system/config/info"
    LOGGER.info("配置查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("配置查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("配置查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_system_list(currentpage, name, pagesize):
    """
    系统列表查询接口-机构管理
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :param name: 系统名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1226')
    requesturl = baseUrl + "/backstage/tenant/system/list"
    LOGGER.info("系统列表查询接口-机构管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("系统列表查询接口-机构管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("系统列表查询接口-机构管理请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_list(currentpage, name, pagesize, systemid):
    """
    机构列表查询接口
    :param pagesize: 每页条数,number
    :param currentpage: 当前页码,number
    :param systemid: 系统Id,number
    :param name: 机构名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1227')
    requesturl = baseUrl + "/backstage/tenant/list"
    LOGGER.info("机构列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["systemId"] = systemid
    LOGGER.info("机构列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_change_state(changeto, id):
    """
    机构状态管理接口
    :param changeto: 变更为指定状态,string
    :param id: 机构id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1228')
    requesturl = baseUrl + "/backstage/tenant/change_state"
    LOGGER.info("机构状态管理接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["changeTo"] = changeto
    params["id"] = id
    LOGGER.info("机构状态管理接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构状态管理接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_add(name, systemid):
    """
    机构新增接口
    :param name: 机构名称,string
    :param systemid: 系统id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1229')
    requesturl = baseUrl + "/backstage/tenant/add"
    LOGGER.info("机构新增接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["systemId"] = systemid
    LOGGER.info("机构新增接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构新增接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_edit(id, name):
    """
    机构编辑接口
    :param id: 机构id,number
    :param name: 机构名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1230')
    requesturl = baseUrl + "/backstage/tenant/edit"
    LOGGER.info("机构编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["name"] = name
    LOGGER.info("机构编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_info(id):
    """
    机构详情获取接口
    :param id: 机构id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1231')
    requesturl = baseUrl + "/backstage/tenant/info"
    LOGGER.info("机构详情获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("机构详情获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构详情获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_permission_tenant_list(currentpage, name, pagesize):
    """
    机构列表查询接口
    :param name: 系统或机构名称,string
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1232')
    requesturl = baseUrl + "/backstage/tenant_permission/tenant/list"
    LOGGER.info("机构列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("机构列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_permission_info(id):
    """
    机构权限获取接口
    :param id: 机构Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1233')
    requesturl = baseUrl + "/backstage/tenant_permission/info"
    LOGGER.info("机构权限获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("机构权限获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构权限获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_permission_set(id, permissions):
    """
    机构权限设置接口
    :param permissions: 权限列表,array<string>
    :param id: 机构id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1234')
    requesturl = baseUrl + "/backstage/tenant_permission/set"
    LOGGER.info("机构权限设置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["permissions"] = permissions
    LOGGER.info("机构权限设置接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构权限设置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_config_tenant_list(currentpage, name, pagesize):
    """
    机构列表查询取接口
    :param name: 系统或机构名称,string
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1235')
    requesturl = baseUrl + "/backstage/tenant_config/tenant/list"
    LOGGER.info("机构列表查询取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("机构列表查询取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构列表查询取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_config_info(id):
    """
    机构配置获取接口
    :param id: 机构Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1236')
    requesturl = baseUrl + "/backstage/tenant_config/info"
    LOGGER.info("机构配置获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("机构配置获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构配置获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_config_set(configs, id):
    """
    机构配置设置接口
    :param configs: 配置集合,array<object>
    :param id: 机构Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1237')
    requesturl = baseUrl + "/backstage/tenant_config/set"
    LOGGER.info("机构配置设置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["configs"] = configs
    params["id"] = id
    LOGGER.info("机构配置设置接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构配置设置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_list(currentpage, name, pagesize, tenantid):
    """
    机构管理员列表查询接口
    :param tenantid: 机构Id,number
    :param currentpage: 当前页码,number
    :param name: 管理员名称,string
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1238')
    requesturl = baseUrl + "/backstage/tenant_administrator/list"
    LOGGER.info("机构管理员列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["tenantId"] = tenantid
    LOGGER.info("机构管理员列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理员列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_resert_password(id):
    """
    机构管理员密码重置接口
    :param id: 用户Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1239')
    requesturl = baseUrl + "/backstage/tenant_administrator/resert_password"
    LOGGER.info("机构管理员密码重置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("机构管理员密码重置接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理员密码重置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_change_state(changeto, id):
    """
    机构管理状态管理接口
    :param changeto: 变更为指定状态,string
    :param id: 用户Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1240')
    requesturl = baseUrl + "/backstage/tenant_administrator/change_state"
    LOGGER.info("机构管理状态管理接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["changeTo"] = changeto
    params["id"] = id
    LOGGER.info("机构管理状态管理接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理状态管理接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_add(email, name, phone, tenantid):
    """
    机构管理员新增接口
    :param phone: 管理员电话,string
    :param name: 管理员姓名,string
    :param email: 管理员邮箱,string
    :param tenantid: 机构ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1241')
    requesturl = baseUrl + "/backstage/tenant_administrator/add"
    LOGGER.info("机构管理员新增接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["name"] = name
    params["phone"] = phone
    params["tenantId"] = tenantid
    LOGGER.info("机构管理员新增接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理员新增接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_edit(email, id, name, phone):
    """
    机构管理员编辑接口
    :param name: 姓名,string
    :param email: 管理员邮箱,string
    :param id: 管理员Id,number
    :param phone: 管理员电话,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1242')
    requesturl = baseUrl + "/backstage/tenant_administrator/edit"
    LOGGER.info("机构管理员编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["id"] = id
    params["name"] = name
    params["phone"] = phone
    LOGGER.info("机构管理员编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理员编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_info(id):
    """
    机构管理详情获取接口
    :param id: 管理员ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1243')
    requesturl = baseUrl + "/backstage/tenant_administrator/info"
    LOGGER.info("机构管理详情获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("机构管理详情获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构管理详情获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_list(currentpage, name, pagesize):
    """
    用户列表查询接口
    :param name: 用户名称,string
    :param pagesize: 每页条数,number
    :param currentpage: 当前页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1244')
    requesturl = baseUrl + "/backstage/user/list"
    LOGGER.info("用户列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("用户列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_change_state(changeto, id):
    """
    用户状态管理接口
    :param id: 用户Id,number
    :param changeto: 变更为指定状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1245')
    requesturl = baseUrl + "/backstage/user/change_state"
    LOGGER.info("用户状态管理接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["changeTo"] = changeto
    params["id"] = id
    LOGGER.info("用户状态管理接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户状态管理接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_add(email, realname, roleid):
    """
    用户新增接口
    :param email: 用户邮箱,string
    :param roleid: 角色ID,number
    :param realname: 用户姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1246')
    requesturl = baseUrl + "/backstage/user/add"
    LOGGER.info("用户新增接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["realname"] = realname
    params["roleId"] = roleid
    LOGGER.info("用户新增接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户新增接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_edit(email, id, realname, roleid):
    """
    用户详情编辑接口
    :param id: 用户ID,number
    :param roleid: 角色Id,number
    :param realname: 姓名,string
    :param email: 邮箱,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1247')
    requesturl = baseUrl + "/backstage/user/edit"
    LOGGER.info("用户详情编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    params["id"] = id
    params["realname"] = realname
    params["roleId"] = roleid
    LOGGER.info("用户详情编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户详情编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_info(id):
    """
    用户详情获取接口
    :param id: 用户ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1248')
    requesturl = baseUrl + "/backstage/user/info"
    LOGGER.info("用户详情获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("用户详情获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户详情获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_role_list(currentpage, name, pagesize):
    """
    角色列表查询接口
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :param name: 角色名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1249')
    requesturl = baseUrl + "/backstage/role/list"
    LOGGER.info("角色列表查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("角色列表查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色列表查询接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_role_add(name, permissionids):
    """
    角色新增接口
    :param name: 角色名称,string
    :param permissionids: 选中的权限Id集合,array<number>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1250')
    requesturl = baseUrl + "/backstage/role/add"
    LOGGER.info("角色新增接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["permissionIds"] = permissionids
    LOGGER.info("角色新增接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色新增接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_role_edit(id, name, permissionids):
    """
    角色编辑接口
    :param permissionids: 角色拥有的权限Id集合,array<number>
    :param name: 角色名称,string
    :param id: 角色Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1251')
    requesturl = baseUrl + "/backstage/role/edit"
    LOGGER.info("角色编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["name"] = name
    params["permissionIds"] = permissionids
    LOGGER.info("角色编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_role_info(id):
    """
    角色详情获取接口
    :param id: 角色Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1252')
    requesturl = baseUrl + "/backstage/role/info"
    LOGGER.info("角色详情获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("角色详情获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色详情获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_genuuid():
    """
    全局UUID生成接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1253')
    requesturl = baseUrl + "/backstage/system/genuuid"
    LOGGER.info("全局UUID生成接口请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("全局UUID生成接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全局UUID生成接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_config_set(configs, id):
    """
    配置编辑接口
    :param id: 业务系统id,number
    :param configs: 系统配置,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1254')
    requesturl = baseUrl + "/backstage/system/config/set"
    LOGGER.info("配置编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["configs"] = configs
    params["id"] = id
    LOGGER.info("配置编辑接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("配置编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_get_system_name(id):
    """
    系统名称获取接口
    :param id: 系统id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1255')
    requesturl = baseUrl + "/backstage/tenant/get_system_name"
    LOGGER.info("系统名称获取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("系统名称获取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("系统名称获取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_tenant_list(currentpage, name, pagesize):
    """
    机构列表查询取接口
    :param name: 系统或机构名称,string
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1256')
    requesturl = baseUrl + "/backstage/tenant_administrator/tenant/list"
    LOGGER.info("机构列表查询取接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("机构列表查询取接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机构列表查询取接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_administrator_get_system_name_and_tenant_name(id):
    """
    根据机构Id获取机构名称和系统名称的接口
    :param id: 机构id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1257')
    requesturl = baseUrl + "/backstage/tenant_administrator/get_system_name_and_tenant_name"
    LOGGER.info("根据机构Id获取机构名称和系统名称的接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("根据机构Id获取机构名称和系统名称的接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据机构Id获取机构名称和系统名称的接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_user_role_list():
    """
    获取角色list
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1258')
    requesturl = baseUrl + "/backstage/user/role/list"
    LOGGER.info("获取角色list请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取角色list请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取角色list请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_role_permissions():
    """
    获取所有权限的集合-与编辑页面共用
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1259')
    requesturl = baseUrl + "/backstage/role/permissions"
    LOGGER.info("获取所有权限的集合-与编辑页面共用请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取所有权限的集合-与编辑页面共用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有权限的集合-与编辑页面共用请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_message_list(currentpage, name, pagesize, synchronizestate):
    """
    同步日志列表查询方法
    :param pagesize: 每页条数,number
    :param synchronizestate: 同步状态,string
    :param currentpage: 当前页码,number
    :param name: 系统名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1260')
    requesturl = baseUrl + "/backstage/message/list"
    LOGGER.info("同步日志列表查询方法请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["name"] = name
    params["pageSize"] = pagesize
    params["synchronizeState"] = synchronizestate
    LOGGER.info("同步日志列表查询方法请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同步日志列表查询方法请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


