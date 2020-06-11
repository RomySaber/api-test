#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Center_meijiaAction.py
@desc       : 项目：center 模块：center_meijia 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('center_meijia_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_api_v2_2792(apiname, urladdress, useridentity):
    """
    获取二维码
    :param useridentity: 用户唯一标识,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2792')
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


def test_api_v2_2793(apiname, urladdress, useridentity, reqid):
    """
    获取二维码被扫描状态
    :param useridentity: 用户唯一标志,string
    :param reqid: 请求id,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2793')
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


def test_api_v2_2794(apiname, urladdress, useridentity, reqid, type):
    """
    获取短信验证码
    :param reqid: 请求ID,string
    :param type: 类型（qr/ac）,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标志,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2794')
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


def test_api_v2_2795(apiname, urladdress, useridentity, code, name, password, reqid, type):
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2795')
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


def test_api_v2_2796(apiname, urladdress, useridentity, name, password):
    """
    账号密码登陆
    :param name: 用户名,string
    :param password: 密码,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标志,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2796')
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


def test_api_v2_2797():
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2797')
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


def test_api_v2_2798(apiname, urladdress, useridentity, phone):
    """
    获取手机号码类型
    :param phone: 手机号码,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2798')
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


def test_api_v2_2799(apiname, urladdress, useridentity, phone, phone_type):
    """
    初始化配置
    :param phone_type: 手机号码类型,string
    :param phone: 手机号,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2799')
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


def test_api_v2_2800(apiname, urladdress, useridentity, phone, phone_type, reqid):
    """
    获取二次短信验证码接口
    :param phone_type: 类型,string
    :param reqid: 请求id,string
    :param phone: 电话号码,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2800')
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


def test_api_v2_2801(apiname, urladdress, useridentity, phone_type, reqid):
    """
    获取图片验证码
    :param phone_type: 类型,string
    :param reqid: 请求id,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2801')
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


def test_api_v2_2802(apiname, urladdress, useridentity, password, phone, phone_type, piccode, randompassword, reqid):
    """
    登录
    :param phone: 电话,string
    :param password: 登录密码,string
    :param randompassword: 短信验证码,string
    :param piccode: 图片验证码,string
    :param reqid: 请求ID,string
    :param phone_type: 号码类型,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2802')
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


def test_api_v2_2803(apiname, urladdress, useridentity, code, idcard, name, password, phone, phone_type, piccode, reqid):
    """
    二次验证码提交验证
    :param code: 短信验证码,string
    :param piccode: 图片验证码,string
    :param phone: 电话号码,string
    :param name: 真实姓名,string
    :param idcard: 身份证,string
    :param password: 服务密码,string
    :param phone_type: 类型,string
    :param reqid: 请求id,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2803')
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


def test_api_v2_2804(apiname, urladdress, useridentity, phone_type, reqid):
    """
    获取二次图片验证码接口
    :param reqid: 请求id,string
    :param phone_type: 手机类型,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2804')
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


def test_api_v1_aiCallback_2805(status, taskid):
    """
    AI回调接口中心通知接口
    :param status: 状态,string
    :param taskid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2805')
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


def test_api_v2_2806(apiname, urladdress, useridentity, reqid):
    """
    获取图片验证码
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param reqid: 请求Id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2806')
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


def test_api_v2_2807(apiname, urladdress, useridentity, code, name, password, reqid, school):
    """
    账号密码学校名称登录
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param useridentity: 用户唯一标识,string
    :param code: 图片验证码（非必填）,string
    :param name: 用户名,string
    :param password: 密码,string
    :param reqid: 请求ID(非必填),string
    :param school: 学校名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2807')
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


def test_api_weixin_login_2808(pwd, username):
    """
    登陆接口
    :param pwd: 密码,string
    :param username: 用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2808')
    requesturl = baseUrl + "/api/weixin/login"
    LOGGER.info("登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["pwd"] = pwd
    params["userName"] = username
    LOGGER.info("登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_findPassword_2809(mobile, pwd, vifcode):
    """
    找回密码
    :param pwd: 新密码,number
    :param vifcode: 验证码,number
    :param mobile: 手机号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2809')
    requesturl = baseUrl + "/api/weixin/findPassword"
    LOGGER.info("找回密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["pwd"] = pwd
    params["vifCode"] = vifcode
    LOGGER.info("找回密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("找回密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_sendMsg_2810(mobile):
    """
    获取验证码
    :param mobile: 手机号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2810')
    requesturl = baseUrl + "/api/weixin/sendMsg"
    LOGGER.info("获取验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    LOGGER.info("获取验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_getSaUser_2811(token, user):
    """
    获取SA人员
    :param token: 登录状态,string
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2811')
    requesturl = baseUrl + "/api/weixin/getSaUser"
    LOGGER.info("获取SA人员请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    params["user"] = user
    LOGGER.info("获取SA人员请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取SA人员请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_loanList_2812(loan_state, page, search_key, size, token, user):
    """
    放款信息列表
    :param token: 登陆状态,string
    :param loan_state: 放款状态,number
    :param search_key: 搜索条件,string
    :param size: 步长,number
    :param page: 页码,number
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2812')
    requesturl = baseUrl + "/api/weixin/loanList"
    LOGGER.info("放款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["loan_state"] = loan_state
    params["page"] = page
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("放款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_userBill_2813(contract_number, token, user):
    """
    全部账单
    :param token: ,
    :param contract_number: 合同编号,
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2813')
    requesturl = baseUrl + "/api/weixin/userBill"
    LOGGER.info("全部账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["contract_number"] = contract_number
    params["token"] = token
    params["user"] = user
    LOGGER.info("全部账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全部账单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_userList_2814(page, repayment_method, repayment_state, search_key, size, token, user):
    """
    账单信息列表
    :param token: 登陆状态,string
    :param page: 页码,
    :param repayment_state: 还款状态,
    :param repayment_method: 还款方式,
    :param search_key: 搜索条件,
    :param size: 步长,
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2814')
    requesturl = baseUrl + "/api/weixin/userList"
    LOGGER.info("账单信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["repayment_method"] = repayment_method
    params["repayment_state"] = repayment_state
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("账单信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentDetail_2815(token, user, user_bill_uuid):
    """
    还款信息详情
    :param token: 登陆状态,string
    :param user_bill_uuid: 账单id,
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2815')
    requesturl = baseUrl + "/api/weixin/repaymentDetail"
    LOGGER.info("还款信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    params["user"] = user
    params["user_bill_uuid"] = user_bill_uuid
    LOGGER.info("还款信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentList_2816(overdue_state, page, pay_state, search_key, size, token, user):
    """
    还款信息列表
    :param token: 登陆状态,string
    :param overdue_state: 逾期状态,
    :param pay_state: 还款状态,
    :param search_key: 搜索条件,
    :param page: 页码,
    :param size: 步长,
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2816')
    requesturl = baseUrl + "/api/weixin/repaymentList"
    LOGGER.info("还款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["overdue_state"] = overdue_state
    params["page"] = page
    params["pay_state"] = pay_state
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("还款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_merchantList_2817(freeze_state, keyword, open_close_state, page, page_size, token, user):
    """
    商户信息列表
    :param token: 登陆状态,string
    :param keyword: 搜索关键字,string
    :param freeze_state: 使用状态,string
    :param open_close_state: 开关状态,string
    :param page_size: 每页条数,number
    :param page: 页码,number
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2817')
    requesturl = baseUrl + "/api/weixin/merchantList"
    LOGGER.info("商户信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["open_close_state"] = open_close_state
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("商户信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeDetail_2818(id, token, user):
    """
    门店信息详情
    :param token: 登陆状态,string
    :param id: 门店id,number
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2818')
    requesturl = baseUrl + "/api/weixin/storeDetail"
    LOGGER.info("门店信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeList_2819(freeze_state, keyword, merchant_uuid, page, page_size, token, user):
    """
    门店列表
    :param token: 登陆状态,string
    :param freeze_state: 使用状态,string
    :param merchant_uuid: 商户uuid,number
    :param page_size: 每页条数,number
    :param page: 页码,number
    :param keyword: 模糊搜索关键字,string
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2819')
    requesturl = baseUrl + "/api/weixin/storeList"
    LOGGER.info("门店列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["merchant_uuid"] = merchant_uuid
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_userBill_2820(contract_number, token, user):
    """
    全部账单
    :param contract_number: 合同编号,
    :param token: ,
    :param user: 登录账号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2820')
    requesturl = baseUrl + "/api/weixin/userBill"
    LOGGER.info("全部账单请求地址:【{}】".format(requesturl))
    params = dict()
    params["contract_number"] = contract_number
    params["token"] = token
    params["user"] = user
    LOGGER.info("全部账单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全部账单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_login_3173(pwd, username):
    """
    登陆接口
    :param username: 用户名,string
    :param pwd: 密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3173')
    requesturl = baseUrl + "/api/weixin/login"
    LOGGER.info("登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["pwd"] = pwd
    params["userName"] = username
    LOGGER.info("登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_loanList_3174(loan_state, merchant, page, province, sa_id, search_key, size, token, user):
    """
    放款信息列表
    :param search_key: 搜索条件,string
    :param loan_state: 放款状态,number
    :param size: 步长,number
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param page: 页码,number
    :param province: 省份,number
    :param merchant: 商户名称,string
    :param sa_id: SA人员,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3174')
    requesturl = baseUrl + "/api/weixin/loanList"
    LOGGER.info("放款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["loan_state"] = loan_state
    params["merchant"] = merchant
    params["page"] = page
    params["province"] = province
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("放款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_loanDetail_3175(contract_number, token, user):
    """
    放款信息详情
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param contract_number: 合同编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3175')
    requesturl = baseUrl + "/api/weixin/loanDetail"
    LOGGER.info("放款信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["contract_number"] = contract_number
    params["token"] = token
    params["user"] = user
    LOGGER.info("放款信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_userList_3176(merchant, page, province, repayment_method, repayment_state, sa_id, search_key, size, token, user):
    """
    账单信息列表
    :param token: 登陆状态,string
    :param size: 步长,
    :param user: 登录账号,
    :param repayment_method: 还款方式,
    :param repayment_state: 还款状态,
    :param page: 页码,
    :param search_key: 搜索条件,
    :param province: 省份,number
    :param merchant: 商户名称,
    :param sa_id: SA人员,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3176')
    requesturl = baseUrl + "/api/weixin/userList"
    LOGGER.info("账单信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchant"] = merchant
    params["page"] = page
    params["province"] = province
    params["repayment_method"] = repayment_method
    params["repayment_state"] = repayment_state
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("账单信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentDetail_3177(token, user, user_bill_uuid):
    """
    还款信息详情
    :param token: 登陆状态,string
    :param user: 登录账号,
    :param user_bill_uuid: 账单id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3177')
    requesturl = baseUrl + "/api/weixin/repaymentDetail"
    LOGGER.info("还款信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    params["user"] = user
    params["user_bill_uuid"] = user_bill_uuid
    LOGGER.info("还款信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentList_3178(merchant, overdue_state, page, pay_state, province, sa_id, search_key, size, token, user):
    """
    还款信息列表
    :param page: 页码,
    :param size: 步长,
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param overdue_state: 逾期状态,
    :param pay_state: 还款状态,
    :param search_key: 搜索条件,
    :param province: 省份,number
    :param merchant: 商户名称,
    :param sa_id: SA人员,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3178')
    requesturl = baseUrl + "/api/weixin/repaymentList"
    LOGGER.info("还款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchant"] = merchant
    params["overdue_state"] = overdue_state
    params["page"] = page
    params["pay_state"] = pay_state
    params["province"] = province
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("还款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentDetail_3179(token, user, user_bill_uuid):
    """
    还款信息详情
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param user_bill_uuid: 账单id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3179')
    requesturl = baseUrl + "/api/weixin/repaymentDetail"
    LOGGER.info("还款信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    params["user"] = user
    params["user_bill_uuid"] = user_bill_uuid
    LOGGER.info("还款信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_merchantList_3180(freeze_state, keyword, open_close_state, page, page_size, token, user):
    """
    商户信息列表
    :param page_size: 每页条数,number
    :param keyword: 搜索关键字,string
    :param page: 页码,number
    :param token: 登陆状态,string
    :param user: 登录账号,
    :param open_close_state: 开关状态,string
    :param freeze_state: 使用状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3180')
    requesturl = baseUrl + "/api/weixin/merchantList"
    LOGGER.info("商户信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["open_close_state"] = open_close_state
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("商户信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_merchantDetail_3181(id, token, user):
    """
    商户信息详情
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param id: 商户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3181')
    requesturl = baseUrl + "/api/weixin/merchantDetail"
    LOGGER.info("商户信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = token
    params["user"] = user
    LOGGER.info("商户信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeDetail_3182(id, token, user):
    """
    门店信息详情
    :param token: 登陆状态,string
    :param user: 登录账号,
    :param id: 门店id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3182')
    requesturl = baseUrl + "/api/weixin/storeDetail"
    LOGGER.info("门店信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeList_3183(freeze_state, keyword, merchant_uuid, page, page_size, token, user):
    """
    门店列表
    :param user: 登录账号,
    :param page: 页码,number
    :param freeze_state: 使用状态,string
    :param merchant_uuid: 商户uuid,number
    :param token: 登陆状态,string
    :param page_size: 每页条数,number
    :param keyword: 模糊搜索关键字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3183')
    requesturl = baseUrl + "/api/weixin/storeList"
    LOGGER.info("门店列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["merchant_uuid"] = merchant_uuid
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2__3190(acctname, apiname, liceneceno, phone, urladdress):
    """
    小启报告
    :param acctname: 姓名,
    :param apiname: 接口标识:,
    :param liceneceno: 身份证,
    :param phone: 手机,
    :param urladdress: 项目域名,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3190')
    requesturl = baseUrl + "/api/v2/"
    LOGGER.info("小启报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    LOGGER.info("小启报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_findPassword_3297(mobile, pwd, vifcode):
    """
    找回密码
    :param mobile: 手机号,number
    :param pwd: 新密码,number
    :param vifcode: 验证码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3297')
    requesturl = baseUrl + "/api/weixin/findPassword"
    LOGGER.info("找回密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["pwd"] = pwd
    params["vifCode"] = vifcode
    LOGGER.info("找回密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("找回密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_loanList_3298(loan_state, merchant, page, province, sa_id, search_key, size, token, user):
    """
    放款信息列表
    :param loan_state: 放款状态,number
    :param size: 步长,number
    :param sa_id: SA人员,string
    :param page: 页码,number
    :param search_key: 搜索条件,string
    :param token: 登陆状态,string
    :param user: 登录账号,
    :param province: 省份,number
    :param merchant: 商户名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3298')
    requesturl = baseUrl + "/api/weixin/loanList"
    LOGGER.info("放款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["loan_state"] = loan_state
    params["merchant"] = merchant
    params["page"] = page
    params["province"] = province
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("放款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_loanDetail_3299(contract_number, token, user):
    """
    放款信息详情
    :param contract_number: 合同编号,string
    :param user: 登录账号,
    :param token: 登陆状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3299')
    requesturl = baseUrl + "/api/weixin/loanDetail"
    LOGGER.info("放款信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["contract_number"] = contract_number
    params["token"] = token
    params["user"] = user
    LOGGER.info("放款信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放款信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_userList_3300(merchant, page, province, repayment_method, repayment_state, sa_id, search_key, size, token, user):
    """
    账单信息列表
    :param repayment_method: 还款方式,
    :param repayment_state: 还款状态,
    :param province: 省份,number
    :param size: 步长,
    :param sa_id: SA人员,
    :param token: 登陆状态,string
    :param search_key: 搜索条件,
    :param user: 登录账号,
    :param page: 页码,
    :param merchant: 商户名称,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3300')
    requesturl = baseUrl + "/api/weixin/userList"
    LOGGER.info("账单信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchant"] = merchant
    params["page"] = page
    params["province"] = province
    params["repayment_method"] = repayment_method
    params["repayment_state"] = repayment_state
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("账单信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_repaymentList_3301(merchant, overdue_state, page, pay_state, province, sa_id, search_key, size, token, user):
    """
    还款信息列表
    :param overdue_state: 逾期状态,
    :param user: 登录账号,
    :param search_key: 搜索条件,
    :param size: 步长,
    :param pay_state: 还款状态,
    :param province: 省份,number
    :param merchant: 商户名称,
    :param sa_id: SA人员,
    :param page: 页码,
    :param token: 登陆状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3301')
    requesturl = baseUrl + "/api/weixin/repaymentList"
    LOGGER.info("还款信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchant"] = merchant
    params["overdue_state"] = overdue_state
    params["page"] = page
    params["pay_state"] = pay_state
    params["province"] = province
    params["sa_id"] = sa_id
    params["search_key"] = search_key
    params["size"] = size
    params["token"] = token
    params["user"] = user
    LOGGER.info("还款信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_getProvince_3302(token, user):
    """
    获取系统所有省份
    :param user: 登录账号,
    :param token: 登录状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3302')
    requesturl = baseUrl + "/api/weixin/getProvince"
    LOGGER.info("获取系统所有省份请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = token
    params["user"] = user
    LOGGER.info("获取系统所有省份请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取系统所有省份请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_merchantList_3303(freeze_state, keyword, open_close_state, page, page_size, token, user):
    """
    商户信息列表
    :param freeze_state: 使用状态,string
    :param user: 登录账号,
    :param keyword: 搜索关键字,string
    :param token: 登陆状态,string
    :param open_close_state: 开关状态,string
    :param page_size: 每页条数,number
    :param page: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3303')
    requesturl = baseUrl + "/api/weixin/merchantList"
    LOGGER.info("商户信息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["open_close_state"] = open_close_state
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("商户信息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户信息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeDetail_3304(id, token, user):
    """
    门店信息详情
    :param user: 登录账号,
    :param id: 门店id,number
    :param token: 登陆状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3304')
    requesturl = baseUrl + "/api/weixin/storeDetail"
    LOGGER.info("门店信息详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店信息详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店信息详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_weixin_storeList_3305(freeze_state, keyword, merchant_uuid, page, page_size, token, user):
    """
    门店列表
    :param page: 页码,number
    :param freeze_state: 使用状态,string
    :param user: 登录账号,
    :param token: 登陆状态,string
    :param keyword: 模糊搜索关键字,string
    :param page_size: 每页条数,number
    :param merchant_uuid: 商户uuid,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3305')
    requesturl = baseUrl + "/api/weixin/storeList"
    LOGGER.info("门店列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["freeze_state"] = freeze_state
    params["keyword"] = keyword
    params["merchant_uuid"] = merchant_uuid
    params["page"] = page
    params["page_size"] = page_size
    params["token"] = token
    params["user"] = user
    LOGGER.info("门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text
