#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Center_spaiderasAction.py
@desc       : 项目：center 模块：center_spaideras 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('center_spaideras_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_api_v2_2175(apiname, urladdress, useridentity):
    """
    获取二维码
    :param urladdress: 项目域名,string
    :param apiname: 接口标识,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2175')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    LOGGER.info("获取二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2176(apiname, urladdress, useridentity, reqid):
    """
    获取二维码被扫描状态
    :param apiname: 接口标识,string
    :param reqid: 请求id,string
    :param useridentity: 用户唯一标志,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2176')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取二维码被扫描状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["reqId"] = reqid
    LOGGER.info("获取二维码被扫描状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码被扫描状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2177(apiname, urladdress, useridentity, reqid, type):
    """
    获取短信验证码
    :param apiname: 接口标识,string
    :param useridentity: 用户唯一标志,string
    :param type: 类型（qr/ac）,string
    :param urladdress: 项目域名,string
    :param reqid: 请求ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2177')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2178(apiname, urladdress, useridentity, code, name, password, reqid, type):
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2178')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2179(apiname, urladdress, useridentity, name, password):
    """
    账号密码登陆
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标志,string
    :param name: 用户名,string
    :param password: 密码,string
    :param apiname: 接口标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2179')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("账号密码登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["name"] = name
    params["password"] = password
    LOGGER.info("账号密码登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2180():
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2180')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2181(apiname, urladdress, useridentity, phone):
    """
    获取手机号码类型
    :param phone: 手机号码,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param apiname: 接口标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2181')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取手机号码类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone"] = phone
    LOGGER.info("获取手机号码类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手机号码类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2182(apiname, urladdress, useridentity, phone, phone_type):
    """
    初始化配置
    :param phone_type: 手机号码类型,string
    :param phone: 手机号,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param apiname: 接口标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2182')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("初始化配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone"] = phone
    params["phone_type"] = phone_type
    LOGGER.info("初始化配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初始化配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2183(apiname, urladdress, useridentity, phone, phone_type, reqid):
    """
    获取短信验证码
    :param phone: 电话,string
    :param useridentity: 用户唯一标识,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param phone_type: 手机号码类型,string
    :param reqid: 请求ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2183')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2184(apiname, urladdress, useridentity, phone_type, reqid):
    """
    获取图片验证码
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param phone_type: 类型,string
    :param useridentity: 用户唯一标识,string
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2184')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2185(apiname, urladdress, useridentity, password, phone, phone_type, piccode, randompassword, reqid):
    """
    登录
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param phone: 电话,string
    :param reqid: 请求ID,string
    :param randompassword: 短信验证码,string
    :param useridentity: 用户唯一标识,string
    :param piccode: 图片验证码,string
    :param phone_type: 号码类型,string
    :param password: 登录密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2185')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["picCode"] = piccode
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2186(apiname, urladdress, useridentity, phone, phone_type, reqid):
    """
    获取二次短信验证码接口
    :param urladdress: 项目域名,string
    :param apiname: 接口标识,string
    :param useridentity: 用户唯一标识,string
    :param phone: 电话号码,string
    :param phone_type: 类型,string
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2186')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取二次短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取二次短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二次短信验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2187(apiname, urladdress, useridentity, code, idcard, name, password, phone, phone_type, piccode, reqid):
    """
    二次验证码提交验证
    :param reqid: 请求id,string
    :param apiname: 接口标识,string
    :param password: 服务密码,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param name: 真实姓名,string
    :param phone_type: 类型,string
    :param code: 短信验证码,string
    :param phone: 电话号码,string
    :param piccode: 图片验证码,string
    :param idcard: 身份证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2187')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("二次验证码提交验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["idcard"] = idcard
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["piccode"] = piccode
    params["reqId"] = reqid
    LOGGER.info("二次验证码提交验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("二次验证码提交验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2188(apiname, urladdress, useridentity, phone_type, reqid):
    """
    获取二次图片验证码接口
    :param reqid: 请求id,string
    :param phone_type: 手机类型,string
    :param urladdress: 项目域名,string
    :param apiname: 接口标识,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2188')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取二次图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取二次图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二次图片验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v1_aiCallback_2189(status, taskid):
    """
    AI回调接口中心通知接口
    :param taskid: 请求id,string
    :param status: 状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2189')
    requesturl = baseUrl + "/api/v1/aiCallback"
    LOGGER.info("AI回调接口中心通知接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("AI回调接口中心通知接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("AI回调接口中心通知接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2190(apiname, urladdress, useridentity, reqid):
    """
    获取图片验证码
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param reqid: 请求Id,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2190')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["reqId"] = reqid
    LOGGER.info("获取图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2191(apiname, urladdress, useridentity, code, name, password, reqid, school):
    """
    账号密码学校名称登录
    :param urladdress: 项目域名,string
    :param password: 密码,string
    :param reqid: 请求ID(非必填),string
    :param apiname: 接口标识,string
    :param name: 用户名,string
    :param school: 学校名称,string
    :param useridentity: 用户唯一标识,string
    :param code: 图片验证码（非必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2191')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("账号密码学校名称登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["school"] = school
    LOGGER.info("账号密码学校名称登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码学校名称登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v1_aiCallback_2192(appkey, status, taskid):
    """
    AI回调接口中心通知接口
    :param taskid: 请求id,string
    :param status: 状态,string
    :param appkey: 项目标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2192')
    requesturl = baseUrl + "/api/v1/aiCallback"
    LOGGER.info("AI回调接口中心通知接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["appkey"] = appkey
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("AI回调接口中心通知接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("AI回调接口中心通知接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2202(apiname, urladdress, useridentity):
    """
    获取项目相关配置数据
    :param apiname: ApiName,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2202')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取项目相关配置数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    LOGGER.info("获取项目相关配置数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取项目相关配置数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2205(apiname, urladdress, useridentity, code, name, password, reqid, school):
    """
    账号密码学校名称登录
    :param urladdress: 项目域名,string
    :param password: 密码,string
    :param apiname: 接口标识,string
    :param name: 用户名,string
    :param school: 学校名称,string
    :param useridentity: 用户唯一标识,string
    :param code: 图片验证码（非必填）,string
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2205')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("账号密码学校名称登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["school"] = school
    LOGGER.info("账号密码学校名称登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码学校名称登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v1_aiCallback_2551(signature, status, taskid):
    """
    AI回调接口中心通知接口
    :param taskid: 请求id,string
    :param status: 状态,string
    :param signature: 签名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2551')
    requesturl = baseUrl + "/api/v1/aiCallback"
    LOGGER.info("AI回调接口中心通知接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["signature"] = signature
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("AI回调接口中心通知接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("AI回调接口中心通知接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v1_getUnEncryptDataByTaskId_2552(taskid):
    """
    获取没有脱敏报告数据
    :param taskid: taskId,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2552')
    requesturl = baseUrl + "/api/v1/getUnEncryptDataByTaskId"
    LOGGER.info("获取没有脱敏报告数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["taskId"] = taskid
    LOGGER.info("获取没有脱敏报告数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取没有脱敏报告数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2556(apiname, urladdress, useridentity, code, idcard, name, password, phone, phone_type, piccode, reqid):
    """
    验证二次验证码
    :param reqid: 请求id,string
    :param apiname: 接口标识,string
    :param password: 服务密码,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param name: 真实姓名,string
    :param phone_type: 类型,string
    :param phone: 电话号码,string
    :param piccode: 图片验证码,string
    :param idcard: 身份证,string
    :param code: 短信验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2556')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证二次验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["idcard"] = idcard
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["piccode"] = piccode
    params["reqId"] = reqid
    LOGGER.info("验证二次验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证二次验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2557(apiname, urladdress, useridentity, phone_type, piccode, reqid):
    """
    验证二次图片验证码（只限移动）
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param phone_type: 类型,string
    :param reqid: 请求id,string
    :param piccode: 图片验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2557')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证二次图片验证码（只限移动）请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone_type"] = phone_type
    params["piccode"] = piccode
    params["reqId"] = reqid
    LOGGER.info("验证二次图片验证码（只限移动）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证二次图片验证码（只限移动）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2564(apiname, urladdress, useridentity, is_loan_scene, user_mobile, user_name):
    """
    更新用户借贷信息
    :param apiname: ApiName,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param is_loan_scene: 是否借贷场景,number
    :param user_mobile: 借贷人电话号码,string
    :param user_name: 借贷用户姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2564')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("更新用户借贷信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["is_loan_scene"] = is_loan_scene
    params["user_mobile"] = user_mobile
    params["user_name"] = user_name
    LOGGER.info("更新用户借贷信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新用户借贷信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2578(apiname, urladdress, useridentity, phone, phone_type):
    """
    发送短信
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param phone: 手机号码,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2578')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("发送短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone"] = phone
    params["phone_type"] = phone_type
    LOGGER.info("发送短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2579(apiname, urladdress, useridentity, code, phone, phone_type, reqid):
    """
    验证短信登录
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param code: 短信验证码,string
    :param phone: 手机号码,string
    :param phone_type: 运营商类型,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2579')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证短信登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("验证短信登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2580(apiname, urladdress, useridentity, password, phone, phone_type):
    """
    账号密码登录
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param password: 运营商密码,string
    :param phone: 手机号码,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2580')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("账号密码登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    LOGGER.info("账号密码登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2581(apiname, urladdress, useridentity, phone_type, reqid):
    """
    获取通话详单二次校验方式
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param phone_type: 运营商类型,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2581')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取通话详单二次校验方式请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取通话详单二次校验方式请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取通话详单二次校验方式请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2582(apiname, urladdress, useridentity, idcard6, phone_type, reqid):
    """
    校验身份证号码后六位
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param idcard6: 身份证号码后六位,string
    :param phone_type: 运营商类型,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2582')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("校验身份证号码后六位请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["idcard6"] = idcard6
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("校验身份证号码后六位请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("校验身份证号码后六位请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2583(apiname, urladdress, useridentity, phone_type, pic_position, reqid, slip_x):
    """
    验证滑块验证码
    :param slip_x: 滑块偏移量与原图比率,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param phone_type: 运营商类型,string
    :param pic_position: 第几个图片1，2，3，4，5,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2583')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证滑块验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["phone_type"] = phone_type
    params["pic_position"] = pic_position
    params["reqId"] = reqid
    params["slip_x"] = slip_x
    LOGGER.info("验证滑块验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证滑块验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_2584(apiname, urladdress, useridentity, code, password, phone_type, reqid):
    """
    验证短信
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param code: 短信验证码,string
    :param password: 移动才填入（运营商密码）,string
    :param phone_type: 运营商类型,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2584')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("验证短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["UserIdentity"] = useridentity
    params["code"] = code
    params["password"] = password
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("验证短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


