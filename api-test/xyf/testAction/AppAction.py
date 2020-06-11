#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppAction.py
@desc       : 项目：xyf 模块：app 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('app_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_app_login()
API_TEST_HEADERS['authorization'] = LICENCES


def test_v5_jdgetqrcodes(reqid):
    """
    获取二维码
    :param reqid: 请求ID(可不传),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2636')
    requesturl = baseUrl + "/v5/jdgetqrcodes"
    LOGGER.info("获取二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("获取二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_jdverifyqrcodes(reqid):
    """
    获取二维码被扫描状态
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2637')
    requesturl = baseUrl + "/v5/jdverifyqrcodes"
    LOGGER.info("获取二维码被扫描状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("获取二维码被扫描状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码被扫描状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_jdgetcodes(reqid, type):
    """
    获取短信验证码
    :param reqid: ,
    :param type: 类型（qr/ac）,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2638')
    requesturl = baseUrl + "/v5/jdgetcodes"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["type"] = type
    params["token"] = LICENCES
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_jdverifycodes(code, name, password, reqid, type):
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2639')
    requesturl = baseUrl + "/v5/jdverifycodes"
    LOGGER.info("验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["type"] = type
    params["token"] = LICENCES
    LOGGER.info("验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_jdlogins(name, password, reqid):
    """
    账号密码登陆
    :param name: 用户名,string
    :param password: 密码,string
    :param reqid: 非必传,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2640')
    requesturl = baseUrl + "/v5/jdlogins"
    LOGGER.info("账号密码登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("账号密码登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tbgetqrcodes():
    """
    获取二维码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2641')
    requesturl = baseUrl + "/v5/tbgetqrcodes"
    LOGGER.info("获取二维码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tbverifyqrcodes():
    """
    获取二维码被扫描状态
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2642')
    requesturl = baseUrl + "/v5/tbverifyqrcodes"
    LOGGER.info("获取二维码被扫描状态请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取二维码被扫描状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二维码被扫描状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tbgetcodes():
    """
    获取短信验证码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2643')
    requesturl = baseUrl + "/v5/tbgetcodes"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tblogins():
    """
    账号密码登陆
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2644')
    requesturl = baseUrl + "/v5/tblogins"
    LOGGER.info("账号密码登陆请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("账号密码登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tbverifycodes():
    """
    验证短信码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2645')
    requesturl = baseUrl + "/v5/tbverifycodes"
    LOGGER.info("验证短信码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("验证短信码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phonetypes(phone):
    """
    获取手机号码类型
    :param phone: 手机号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2646')
    requesturl = baseUrl + "/v5/phonetypes"
    LOGGER.info("获取手机号码类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["token"] = LICENCES
    LOGGER.info("获取手机号码类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手机号码类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phoneconfigs(phone, phone_type):
    """
    初始化配置
    :param phone: 手机号,string
    :param phone_type: 手机号码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2647')
    requesturl = baseUrl + "/v5/phoneconfigs"
    LOGGER.info("初始化配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["token"] = LICENCES
    LOGGER.info("初始化配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初始化配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phonesms(phone, phone_type, reqid):
    """
    获取短信验证码
    :param phone: 电话,string
    :param reqid: 必传,string
    :param phone_type: 手机号码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2648')
    requesturl = baseUrl + "/v5/phonesms"
    LOGGER.info("获取短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("获取短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phonepics(phone_type, reqid):
    """
    获取图片验证码
    :param reqid: ,string
    :param phone_type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2649')
    requesturl = baseUrl + "/v5/phonepics"
    LOGGER.info("获取图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("获取图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phonelogins(password, phone, phone_type, piccode, randompassword, reqid):
    """
    登录
    :param piccode: 图片验证码,string
    :param phone_type: 号码类型,string
    :param reqid: 请求ID,string
    :param password: 登录密码,string
    :param randompassword: 短信验证码,string
    :param phone: 电话,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2650')
    requesturl = baseUrl + "/v5/phonelogins"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
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


def test_v5_phonestatus(phone_type, reqid):
    """
    获取爬虫当前任务状态
    :param phone_type: 号码类型,string
    :param reqid: 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2651')
    requesturl = baseUrl + "/v5/phonestatus"
    LOGGER.info("获取爬虫当前任务状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取爬虫当前任务状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取爬虫当前任务状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_phonesmsseconds(phone, phone_type, reqid):
    """
    获取二次短信验证码接口
    :param reqid: ,
    :param phone: 电话号码,string
    :param phone_type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2652')
    requesturl = baseUrl + "/v5/phonesmsseconds"
    LOGGER.info("获取二次短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
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


def test_v5_phonesecondveris(code, idcard, name, password, phone, phone_type, piccode, reqid):
    """
    二次验证码提交验证
    :param name: 真实姓名,string
    :param phone: 电话号码,string
    :param piccode: 图片验证码,string
    :param reqid: 请求id,string
    :param idcard: 身份证,string
    :param phone_type: 类型,string
    :param code: 短信验证码,string
    :param password: 服务密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2653')
    requesturl = baseUrl + "/v5/phonesecondveris"
    LOGGER.info("二次验证码提交验证请求地址:【{}】".format(requesturl))
    params = dict()
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


def test_v5_phonepicseconds(phone_type, reqid):
    """
    获取二次图片验证码接口
    :param reqid: 请求id,string
    :param phone_type: 手机类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2654')
    requesturl = baseUrl + "/v5/phonepicseconds"
    LOGGER.info("获取二次图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    params["token"] = LICENCES
    LOGGER.info("获取二次图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二次图片验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_aicallbacks(status, taskid):
    """
    回调接口
    :param status: 状态,string
    :param taskid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2655')
    requesturl = baseUrl + "/v5/aicallbacks"
    LOGGER.info("回调接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("回调接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("回调接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_spidercallbacks(data, task_id, type, user_id):
    """
    爬虫接口中心回调接口
    :param data: 具体参数,array<object>
    :param user_id: 用户唯一标识符,string
    :param task_id: 任务标识符,string
    :param type: 回调类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2656')
    requesturl = baseUrl + "/v5/spidercallbacks"
    LOGGER.info("爬虫接口中心回调接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["data"] = data
    params["task_id"] = task_id
    params["type"] = type
    params["user_id"] = user_id
    LOGGER.info("爬虫接口中心回调接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("爬虫接口中心回调接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xuexincodes(reqid, toekn):
    """
    图片验证码
    :param toekn: 用户唯一标识,string
    :param reqid: 必传,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2657')
    requesturl = baseUrl + "/v5/xuexincodes"
    LOGGER.info("图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["toekn"] = toekn
    LOGGER.info("图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xuexinlogins(code, name, password, reqid, school):
    """
    账号密码学校名称登录
    :param name: 用户名,string
    :param code: 图片验证码（根据第一次提交登陆信息判断是否必填）,string
    :param password: 密码,string
    :param school: 学校名称,string
    :param reqid: 请求ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2658')
    requesturl = baseUrl + "/v5/xuexinlogins"
    LOGGER.info("账号密码学校名称登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["password"] = password
    params["reqId"] = reqid
    params["school"] = school
    params["token"] = LICENCES
    LOGGER.info("账号密码学校名称登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账号密码学校名称登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditintroduces():
    """
    白条介绍页面
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2659')
    requesturl = baseUrl + "/v5/creditintroduces"
    LOGGER.info("白条介绍页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条介绍页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条介绍页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_othersupportbanks(source):
    """
    激活白条_查看支持银行
    :param source: 1表示从还款银行卡进入 2表示从任信花的收款银行卡进入 3表示从激活白条页面进入,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2660')
    requesturl = baseUrl + "/v5/othersupportbanks"
    LOGGER.info("激活白条_查看支持银行请求地址:【{}】".format(requesturl))
    params = dict()
    params["source"] = source
    params["token"] = LICENCES
    LOGGER.info("激活白条_查看支持银行请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_查看支持银行请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditclosenotices():
    """
    白条介绍页面_关闭白条激活申请未通过的通知
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2661')
    requesturl = baseUrl + "/v5/creditclosenotices"
    LOGGER.info("白条介绍页面_关闭白条激活申请未通过的通知请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条介绍页面_关闭白条激活申请未通过的通知请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条介绍页面_关闭白条激活申请未通过的通知请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firststillpictures(bucket, still_pic1, still_pic2, still_pic3, still_pic4, still_pic5):
    """
    激活白条_刷颜值_保存数据
    :param still_pic3: 点头图片名,string
    :param still_pic4: 最佳人像照片,string
    :param still_pic5: 全景照片,string
    :param still_pic1: 眨眼图片名,string
    :param bucket: 存储空间名,string
    :param still_pic2: 张嘴图片名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2662')
    requesturl = baseUrl + "/v5/firststillpictures"
    LOGGER.info("激活白条_刷颜值_保存数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["still_pic1"] = still_pic1
    params["still_pic2"] = still_pic2
    params["still_pic3"] = still_pic3
    params["still_pic4"] = still_pic4
    params["still_pic5"] = still_pic5
    params["token"] = LICENCES
    LOGGER.info("激活白条_刷颜值_保存数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_刷颜值_保存数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstcheckstills():
    """
    激活白条_刷颜值_验证用户是否已经人脸识别
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2663')
    requesturl = baseUrl + "/v5/firstcheckstills"
    LOGGER.info("激活白条_刷颜值_验证用户是否已经人脸识别请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("激活白条_刷颜值_验证用户是否已经人脸识别请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_刷颜值_验证用户是否已经人脸识别请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditsaveinfomations(emergency, emergencyname, emergencyphone, houseaddress, housecitycode, housecountrycode, houseprovincecode, relative, relativename, relativephone):
    """
    激活白条_完善资料_保存数据
    :param relative: 联系人1关系,string
    :param emergencyname: 联系人2姓名,string
    :param emergencyphone: 联系人2手机号,string
    :param relativename: 联系人1姓名,string
    :param emergency: 联系人2关系,string
    :param houseaddress: 住房地址_详细地址,string
    :param houseprovincecode: 住房地址_省份代码,string
    :param housecitycode: 住房地址_市代码,string
    :param relativephone: 联系人1手机号,string
    :param housecountrycode: 住房地址_区县代码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2664')
    requesturl = baseUrl + "/v5/creditsaveinfomations"
    LOGGER.info("激活白条_完善资料_保存数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["emergency"] = emergency
    params["emergencyName"] = emergencyname
    params["emergencyPhone"] = emergencyphone
    params["houseAddress"] = houseaddress
    params["houseCityCode"] = housecitycode
    params["houseCountryCode"] = housecountrycode
    params["houseProvinceCode"] = houseprovincecode
    params["relative"] = relative
    params["relativeName"] = relativename
    params["relativePhone"] = relativephone
    params["token"] = LICENCES
    LOGGER.info("激活白条_完善资料_保存数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_完善资料_保存数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditgetinfomations():
    """
    激活白条_完善资料_获取数据
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2665')
    requesturl = baseUrl + "/v5/creditgetinfomations"
    LOGGER.info("激活白条_完善资料_获取数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("激活白条_完善资料_获取数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_完善资料_获取数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourbankcardadds(bank_email, cardid, card_no, id_card, phone, real_name):
    """
    激活白条_添加银行卡接口
    :param cardid: 银行卡ID,string
    :param card_no: 银行卡号（必填）,string
    :param bank_email: 接收银行账单邮箱（选填）,string
    :param real_name: 真实姓名（必填）,string
    :param phone: 预留手机号（必填）,string
    :param id_card: 身份证号（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2666')
    requesturl = baseUrl + "/v5/ourbankcardadds"
    LOGGER.info("激活白条_添加银行卡接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["bank_email"] = bank_email
    params["cardId"] = cardid
    params["card_no"] = card_no
    params["id_card"] = id_card
    params["phone"] = phone
    params["real_name"] = real_name
    params["token"] = LICENCES
    LOGGER.info("激活白条_添加银行卡接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_添加银行卡接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotaauthenticates(bucket, idcard, nation, ocrback, ocrfront, picturename1, picturename2, picturename3, realname):
    """
    激活白条_身份认证_保存数据
    :param nation: 名族,string
    :param bucket: 七牛图片存储空间名字,string
    :param realname: 姓名,string
    :param picturename3: 截取人像图片上传七牛返回的key,string
    :param ocrfront: faceID接口身份证（人像面图片）识别返回的数据,string
    :param picturename1: 上传七牛的正面照图片名字,string
    :param ocrback: faceID接口身份证（国徽面图片）识别返回的数据,string
    :param picturename2: 上传七牛的反面照图片名字,string
    :param idcard: 身份证号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2667')
    requesturl = baseUrl + "/v5/quotaauthenticates"
    LOGGER.info("激活白条_身份认证_保存数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["idCard"] = idcard
    params["nation"] = nation
    params["ocrBack"] = ocrback
    params["ocrFront"] = ocrfront
    params["pictureName1"] = picturename1
    params["pictureName2"] = picturename2
    params["pictureName3"] = picturename3
    params["realName"] = realname
    params["token"] = LICENCES
    LOGGER.info("激活白条_身份认证_保存数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("激活白条_身份认证_保存数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotagetinfors(orderid):
    """
    身份认证_获取数据
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2668')
    requesturl = baseUrl + "/v5/quotagetinfors"
    LOGGER.info("身份认证_获取数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("身份认证_获取数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("身份认证_获取数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_merchantconfigures(merchantid, productsku):
    """
    H5获取商户配置
    :param merchantid: 商户ID,string
    :param productsku: 商品sku,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2669')
    requesturl = baseUrl + "/v5/merchantconfigures"
    LOGGER.info("H5获取商户配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantId"] = merchantid
    params["productSku"] = productsku
    LOGGER.info("H5获取商户配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("H5获取商户配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditxxwsearches():
    """
    学信网查询接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2670')
    requesturl = baseUrl + "/v5/creditxxwsearches"
    LOGGER.info("学信网查询接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("学信网查询接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网查询接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_othercheckrealnames():
    """
    检查用户是否实名
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2671')
    requesturl = baseUrl + "/v5/othercheckrealnames"
    LOGGER.info("检查用户是否实名请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("检查用户是否实名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("检查用户是否实名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotaxxws(password, username, verifycode):
    """
    申请额度_学信网认证
    :param password: 密码（加密）,string
    :param verifycode: 验证码（第一次登录不需要验证码，根据请求返回是否需要输入验证码）,string
    :param username: 手机号/生份证号/邮箱（加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2672')
    requesturl = baseUrl + "/v5/quotaxxws"
    LOGGER.info("申请额度_学信网认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["userName"] = username
    params["verifyCode"] = verifycode
    params["token"] = LICENCES
    LOGGER.info("申请额度_学信网认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请额度_学信网认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditdetails():
    """
    白条_结果详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2673')
    requesturl = baseUrl + "/v5/creditdetails"
    LOGGER.info("白条_结果详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_结果详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_结果详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotasaveinfos(address, citycode, countrycode, degreelevel, dormitoryaddress, emergency, emergencyname, emergencyphone, houseaddress, housecitycode, housecountrycode, housephone, houseprovincecode, housetype, marry, provincecode, qq, relative, relativename, relativephone, weixin):
    """
    额度激活_保存基本信息
    :param qq: QQ号码,string
    :param address: 学校地址_详细地址,string
    :param provincecode: 学校地址_省份代码,string
    :param emergencyphone: 紧急联系人手机号,string
    :param weixin: 微信,string
    :param housecitycode: 住房地址_市代码,string
    :param degreelevel: 学历,string
    :param emergency: 紧急联系人关系,string
    :param housetype: 住房类型,string
    :param relative: 亲属联系人1关系,string
    :param relativephone: 亲属联系人1手机号,string
    :param housecountrycode: 住房地址_区县代码,string
    :param houseaddress: 住房地址_详细地址,string
    :param countrycode: 学校地址_区代码,string
    :param housephone: 家庭电话,string
    :param emergencyname: 紧急联系人姓名,string
    :param citycode: 学校地址_城市代码,string
    :param relativename: 亲属联系人1姓名,string
    :param houseprovincecode: 住房地址_省份代码,string
    :param dormitoryaddress: 宿舍地址,string
    :param marry: 婚姻状况,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2674')
    requesturl = baseUrl + "/v5/quotasaveinfos"
    LOGGER.info("额度激活_保存基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["cityCode"] = citycode
    params["countryCode"] = countrycode
    params["degreeLevel"] = degreelevel
    params["dormitoryAddress"] = dormitoryaddress
    params["emergency"] = emergency
    params["emergencyName"] = emergencyname
    params["emergencyPhone"] = emergencyphone
    params["houseAddress"] = houseaddress
    params["houseCityCode"] = housecitycode
    params["houseCountryCode"] = housecountrycode
    params["housePhone"] = housephone
    params["houseProvinceCode"] = houseprovincecode
    params["houseType"] = housetype
    params["marry"] = marry
    params["provinceCode"] = provincecode
    params["qq"] = qq
    params["relative"] = relative
    params["relativeName"] = relativename
    params["relativePhone"] = relativephone
    params["weixin"] = weixin
    params["token"] = LICENCES
    LOGGER.info("额度激活_保存基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("额度激活_保存基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotaactivateds(bucket, picturename):
    """
    额度激活_拍摄在店照片
    :param bucket: 七牛图片存储空间名字,string
    :param picturename: 本人在店照片图片名字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2675')
    requesturl = baseUrl + "/v5/quotaactivateds"
    LOGGER.info("额度激活_拍摄在店照片请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["pictureName"] = picturename
    params["token"] = LICENCES
    LOGGER.info("额度激活_拍摄在店照片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("额度激活_拍摄在店照片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotagetcitylists():
    """
    额度激活_获取省市区列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2676')
    requesturl = baseUrl + "/v5/quotagetcitylists"
    LOGGER.info("额度激活_获取省市区列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("额度激活_获取省市区列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("额度激活_获取省市区列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotaauthenticatetwos(bucket, picturename3):
    """
    额度领取_手持身份证照片
    :param picturename3: 手持身份证照片名字,string
    :param bucket: 七牛图片存储空间名字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2677')
    requesturl = baseUrl + "/v5/quotaauthenticatetwos"
    LOGGER.info("额度领取_手持身份证照片请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["pictureName3"] = picturename3
    params["token"] = LICENCES
    LOGGER.info("额度领取_手持身份证照片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("额度领取_手持身份证照片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_othergetuserinfos():
    """
    授权协议获取用户信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2678')
    requesturl = baseUrl + "/v5/othergetuserinfos"
    LOGGER.info("授权协议获取用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("授权协议获取用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("授权协议获取用户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_fddsigns(orderid):
    """
    法大大文档签署接口
    :param orderid: 订单ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2679')
    requesturl = baseUrl + "/v5/fddsigns"
    LOGGER.info("法大大文档签署接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("法大大文档签署接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("法大大文档签署接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditzmfsearches():
    """
    芝麻分查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2680')
    requesturl = baseUrl + "/v5/creditzmfsearches"
    LOGGER.info("芝麻分查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("芝麻分查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("芝麻分查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_scancodeinputs(gps_latitude, gps_longitude, partnerid):
    """
    扫码
    :param gps_longitude: 经度,string
    :param partnerid: 扫描中抽取问号后的参数,string
    :param gps_latitude: 纬度,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2681')
    requesturl = baseUrl + "/v5/scancodeinputs"
    LOGGER.info("扫码请求地址:【{}】".format(requesturl))
    params = dict()
    params["gps_latitude"] = gps_latitude
    params["gps_longitude"] = gps_longitude
    params["partnerId"] = partnerid
    params["token"] = LICENCES
    LOGGER.info("扫码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("扫码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_scancreditpayments(nums, oldpassword, partnerid, summoney):
    """
    支付
    :param summoney: 付款金额,string
    :param nums: 请求次数,string
    :param partnerid: 扫描中抽取问号后的参数,string
    :param oldpassword: 支付密码(md5),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2682')
    requesturl = baseUrl + "/v5/scancreditpayments"
    LOGGER.info("支付请求地址:【{}】".format(requesturl))
    params = dict()
    params["nums"] = nums
    params["oldPassword"] = oldpassword
    params["partnerId"] = partnerid
    params["summoney"] = summoney
    params["token"] = LICENCES
    LOGGER.info("支付请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("支付请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditfirsts():
    """
    白条首页接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2683')
    requesturl = baseUrl + "/v5/creditfirsts"
    LOGGER.info("白条首页接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条首页接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条首页接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billrefundeds(billid, page):
    """
    账单_账单查询_还款明细/已还款
    :param page: 当前页数。默认1,
    :param billid: 账单ID。 不传获取未出账单的还款明细。 -1表示从账单首页顶部的还款记录进入,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2684')
    requesturl = baseUrl + "/v5/billrefundeds"
    LOGGER.info("账单_账单查询_还款明细/已还款请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("账单_账单查询_还款明细/已还款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_账单查询_还款明细/已还款请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_uploadmessages(content):
    """
    上传用户短信接口
    :param content: 短信内容，json格式,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2685')
    requesturl = baseUrl + "/v5/uploadmessages"
    LOGGER.info("上传用户短信接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["content"] = content
    params["token"] = LICENCES
    LOGGER.info("上传用户短信接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("上传用户短信接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstdetailsaves(city, gps_latitude, gps_longitude, merchantid, productnamedetail, productsku, repaybankid, repaymoney, repaynum):
    """
    分期详情点击下一步保存数据H5使用
    :param repaymoney: 申请分期金额,
    :param productsku: 商品sku,
    :param merchantid: 商户ID,
    :param repaybankid: 还款银行卡Id,
    :param productnamedetail: 商品具体名称,
    :param gps_longitude: GPS经度,
    :param city: 经纬度对应的城市,
    :param repaynum: 分期数,
    :param gps_latitude: GPS纬度,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2686')
    requesturl = baseUrl + "/v5/firstdetailsaves"
    LOGGER.info("分期详情点击下一步保存数据H5使用请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["gps_latitude"] = gps_latitude
    params["gps_longitude"] = gps_longitude
    params["merchantId"] = merchantid
    params["productNameDetail"] = productnamedetail
    params["productSku"] = productsku
    params["repayBankId"] = repaybankid
    params["repayMoney"] = repaymoney
    params["repayNum"] = repaynum
    params["token"] = LICENCES
    LOGGER.info("分期详情点击下一步保存数据H5使用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分期详情点击下一步保存数据H5使用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ournoticelists(id, page):
    """
    我的_消息列表
    :param page: 页码（不传默认为1）,
    :param id: 消息分类id,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2687')
    requesturl = baseUrl + "/v5/ournoticelists"
    LOGGER.info("我的_消息列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("我的_消息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_消息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ournoticepages():
    """
    我的_消息首页
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2688')
    requesturl = baseUrl + "/v5/ournoticepages"
    LOGGER.info("我的_消息首页请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("我的_消息首页请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_消息首页请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourfirsts():
    """
    我的首页
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2689')
    requesturl = baseUrl + "/v5/ourfirsts"
    LOGGER.info("我的首页请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("我的首页请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的首页请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_checkreports(withdraw):
    """
    特别信息认证状态
    :param withdraw: 是否二审退回  1-是 ；0：不是,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2690')
    requesturl = baseUrl + "/v5/checkreports"
    LOGGER.info("特别信息认证状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["withdraw"] = withdraw
    params["token"] = LICENCES
    LOGGER.info("特别信息认证状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("特别信息认证状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_checkfdds(orderid):
    """
    所有版本的增加接口-查询用户法大大签约是否成功
    :param orderid: 订单ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2691')
    requesturl = baseUrl + "/v5/checkfdds"
    LOGGER.info("所有版本的增加接口-查询用户法大大签约是否成功请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("所有版本的增加接口-查询用户法大大签约是否成功请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("所有版本的增加接口-查询用户法大大签约是否成功请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditzmfssaves(params):
    """
    白条_保存芝麻分
    :param params: 编码,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2692')
    requesturl = baseUrl + "/v5/creditzmfssaves"
    LOGGER.info("白条_保存芝麻分请求地址:【{}】".format(requesturl))
    params = dict()
    params["params"] = params
    params["token"] = LICENCES
    LOGGER.info("白条_保存芝麻分请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_保存芝麻分请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billdetails(billid, orderid, refundid):
    """
    账单详情
    :param billid: 账单id,number
    :param orderid: 订单id,number
    :param refundid: 付款id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2693')
    requesturl = baseUrl + "/v5/billdetails"
    LOGGER.info("账单详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["orderId"] = orderid
    params["refundId"] = refundid
    params["token"] = LICENCES
    LOGGER.info("账单详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashbills():
    """
    账单首页接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2694')
    requesturl = baseUrl + "/v5/cashbills"
    LOGGER.info("账单首页接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("账单首页接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单首页接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditzmfchecks():
    """
    查询用户是否已经查询芝麻分
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2695')
    requesturl = baseUrl + "/v5/creditzmfchecks"
    LOGGER.info("查询用户是否已经查询芝麻分请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询用户是否已经查询芝麻分请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户是否已经查询芝麻分请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankanswers(answer, id):
    """
    白条_央行征信_提交信用报告问题答案
    :param answer: 问题有五个答案，分别用1,2,3,4,5表示，中间用逗号,string
    :param id: 记录编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2696')
    requesturl = baseUrl + "/v5/creditbankanswers"
    LOGGER.info("白条_央行征信_提交信用报告问题答案请求地址:【{}】".format(requesturl))
    params = dict()
    params["answer"] = answer
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_提交信用报告问题答案请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_提交信用报告问题答案请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankreportas(id):
    """
    白条_央行征信_查看报告state=3
    :param id: 记录编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2697')
    requesturl = baseUrl + "/v5/creditbankreportas"
    LOGGER.info("白条_央行征信_查看报告state=3请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_查看报告state=3请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_查看报告state=3请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankreportbs(id, verifycode):
    """
    白条_央行征信_查看报告state=2
    :param verifycode: 短信验证码,string
    :param id: 记录编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2698')
    requesturl = baseUrl + "/v5/creditbankreportbs"
    LOGGER.info("白条_央行征信_查看报告state=2请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["verifyCode"] = verifycode
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_查看报告state=2请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_查看报告state=2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbanks(verifycode, account, id, password):
    """
    白条_央行征信_查询
    :param id: 记录编号（3.2接口返回的id）,number
    :param verifycode: 验证码,string
    :param account: 账号（加密）,string
    :param password: 密码（加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2699')
    requesturl = baseUrl + "/v5/creditbanks"
    LOGGER.info("白条_央行征信_查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["VerifyCode"] = verifycode
    params["account"] = account
    params["id"] = id
    params["password"] = password
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankverifycodes():
    """
    白条_央行征信_查询获取验证码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2700')
    requesturl = baseUrl + "/v5/creditbankverifycodes"
    LOGGER.info("白条_央行征信_查询获取验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_查询获取验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_查询获取验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankregs():
    """
    白条_央行征信_注册接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2701')
    requesturl = baseUrl + "/v5/creditbankregs"
    LOGGER.info("白条_央行征信_注册接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_注册接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_注册接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditbankquestions(id):
    """
    白条_央行征信_获取申请信用报告问题
    :param id: 记录编号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2702')
    requesturl = baseUrl + "/v5/creditbankquestions"
    LOGGER.info("白条_央行征信_获取申请信用报告问题请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["token"] = LICENCES
    LOGGER.info("白条_央行征信_获取申请信用报告问题请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_央行征信_获取申请信用报告问题请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditxxws(password, username, verifycode):
    """
    白条_学信网认证（单独认证）
    :param username: 手机号/生份证号/邮箱（加密）,string
    :param password: 密码（加密）,string
    :param verifycode: 验证码（第一次登录不需要验证码，根据请求返回是否需要输入验证码）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2703')
    requesturl = baseUrl + "/v5/creditxxws"
    LOGGER.info("白条_学信网认证（单独认证）请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["userName"] = username
    params["verifyCode"] = verifycode
    params["token"] = LICENCES
    LOGGER.info("白条_学信网认证（单独认证）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_学信网认证（单独认证）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditcgsxes():
    """
    白条_成功授信页面
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2704')
    requesturl = baseUrl + "/v5/creditcgsxes"
    LOGGER.info("白条_成功授信页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_成功授信页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_成功授信页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditsbgetcodes(citycode, provincecode, toke):
    """
    白条_查询社保_社保获取验证码
    :param citycode: 城市代码,string
    :param toke: 授权参数,string
    :param provincecode: 省份代码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2705')
    requesturl = baseUrl + "/v5/creditsbgetcodes"
    LOGGER.info("白条_查询社保_社保获取验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["cityCode"] = citycode
    params["provinceCode"] = provincecode
    params["toke"] = toke
    params["token"] = LICENCES
    LOGGER.info("白条_查询社保_社保获取验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_查询社保_社保获取验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditsblists():
    """
    白条_查询社保_获取参数
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2706')
    requesturl = baseUrl + "/v5/creditsblists"
    LOGGER.info("白条_查询社保_获取参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_查询社保_获取参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_查询社保_获取参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditzmfs():
    """
    白条_查询芝麻分
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2707')
    requesturl = baseUrl + "/v5/creditzmfs"
    LOGGER.info("白条_查询芝麻分请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_查询芝麻分请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_查询芝麻分请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditsbs(password, toke, username, verifycode):
    """
    白条_社保登录
    :param verifycode: 验证码,string
    :param password: 密码（加密）,string
    :param toke: 授权参数,string
    :param username: 登录名（加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2708')
    requesturl = baseUrl + "/v5/creditsbs"
    LOGGER.info("白条_社保登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["toke"] = toke
    params["userName"] = username
    params["verifyCode"] = verifycode
    params["token"] = LICENCES
    LOGGER.info("白条_社保登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_社保登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditsbreports():
    """
    白条_社保详情查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2709')
    requesturl = baseUrl + "/v5/creditsbreports"
    LOGGER.info("白条_社保详情查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("白条_社保详情查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("白条_社保详情查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstproductlists(categoryid, merchantid, page):
    """
    选择商品页面接口-H5使用
    :param page: 当前页数。默认1,number
    :param categoryid: 分类ID,number
    :param merchantid: 商户ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2710')
    requesturl = baseUrl + "/v5/firstproductlists"
    LOGGER.info("选择商品页面接口-H5使用请求地址:【{}】".format(requesturl))
    params = dict()
    params["categoryid"] = categoryid
    params["merchantId"] = merchantid
    params["page"] = page
    LOGGER.info("选择商品页面接口-H5使用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("选择商品页面接口-H5使用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstdetails(merchantid, orderid, productsku):
    """
    订单详情接口
    :param merchantid: 商户ID,number
    :param orderid: 订单ID,number
    :param productsku: 商品sku,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2711')
    requesturl = baseUrl + "/v5/firstdetails"
    LOGGER.info("订单详情接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantId"] = merchantid
    params["orderId"] = orderid
    params["productSku"] = productsku
    params["token"] = LICENCES
    LOGGER.info("订单详情接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单详情接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_fourpayalls(cardid, summoney):
    """
    一键还清接口-APP
    :param summoney: 付款金额,string
    :param cardid: 银行卡ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2712')
    requesturl = baseUrl + "/v5/fourpayalls"
    LOGGER.info("一键还清接口-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardId"] = cardid
    params["summoney"] = summoney
    params["token"] = LICENCES
    LOGGER.info("一键还清接口-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("一键还清接口-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_quotagetinfortwos():
    """
    基本信息获取数据接口-H5
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2713')
    requesturl = baseUrl + "/v5/quotagetinfortwos"
    LOGGER.info("基本信息获取数据接口-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("基本信息获取数据接口-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("基本信息获取数据接口-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_fourpayallpages():
    """
    提前还清页面接口-APP
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2714')
    requesturl = baseUrl + "/v5/fourpayallpages"
    LOGGER.info("提前还清页面接口-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("提前还清页面接口-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提前还清页面接口-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_fouridentifychecks(bucket, still_pic1, still_pic2, still_pic3, still_pic4, still_pic5):
    """
    活体检测数据上传接口-H5
    :param still_pic3: 点头图片名,string
    :param still_pic5: 全景照片,string
    :param still_pic1: 眨眼图片名,string
    :param still_pic4: 最佳人像照片,string
    :param still_pic2: 张嘴图片名,string
    :param bucket: 存储空间名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2715')
    requesturl = baseUrl + "/v5/fouridentifychecks"
    LOGGER.info("活体检测数据上传接口-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["still_pic1"] = still_pic1
    params["still_pic2"] = still_pic2
    params["still_pic3"] = still_pic3
    params["still_pic4"] = still_pic4
    params["still_pic5"] = still_pic5
    params["token"] = LICENCES
    LOGGER.info("活体检测数据上传接口-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("活体检测数据上传接口-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstconfirmphotosaves(orderid):
    """
    确认收货
    :param orderid: 订单ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2716')
    requesturl = baseUrl + "/v5/firstconfirmphotosaves"
    LOGGER.info("确认收货请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("确认收货请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认收货请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_foursavevisitelogs(flag, orderid, pageid):
    """
    进件资料记录进出时间接口-H5
    :param flag: 1为进入页面；2离开页面,number
    :param pageid: 页面id，具体数值查看产品文档。,number
    :param orderid: 订单号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2717')
    requesturl = baseUrl + "/v5/foursavevisitelogs"
    LOGGER.info("进件资料记录进出时间接口-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["flag"] = flag
    params["orderId"] = orderid
    params["pageId"] = pageid
    params["token"] = LICENCES
    LOGGER.info("进件资料记录进出时间接口-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("进件资料记录进出时间接口-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstpages(page):
    """
    首页接口
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2718')
    requesturl = baseUrl + "/v5/firstpages"
    LOGGER.info("首页接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("首页接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashbanklists(orderid):
    """
    收款银行卡列表-APP
    :param orderid: 订单ID。提现到银行卡页面需要传。,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2719')
    requesturl = baseUrl + "/v5/cashbanklists"
    LOGGER.info("收款银行卡列表-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("收款银行卡列表-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("收款银行卡列表-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstworkinfosaves(address, citycode, company, countrycode, department, income, industrycategory, position, provincecode, workemail, workphone, workyear):
    """
    首页_现金分期_工作信息保存-H5
    :param income: 月收入,string
    :param address: 单位地址_详细地址,string
    :param department: 部门,string
    :param workyear: 现在单位工作年限,number
    :param countrycode: 单位地址_区代码,string
    :param industrycategory: 行业类型,string
    :param provincecode: 单位地址_省份代码,string
    :param citycode: 单位地址_城市代码,string
    :param position: 职位,string
    :param company: 单位名,string
    :param workphone: 工作电话,string
    :param workemail: 工作邮箱,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2720')
    requesturl = baseUrl + "/v5/firstworkinfosaves"
    LOGGER.info("首页_现金分期_工作信息保存-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["cityCode"] = citycode
    params["company"] = company
    params["countryCode"] = countrycode
    params["department"] = department
    params["income"] = income
    params["industryCategory"] = industrycategory
    params["position"] = position
    params["provinceCode"] = provincecode
    params["workEmail"] = workemail
    params["workPhone"] = workphone
    params["workYear"] = workyear
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期_工作信息保存-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期_工作信息保存-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstworkinfos():
    """
    首页_现金分期_工作信息获取-H5
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2721')
    requesturl = baseUrl + "/v5/firstworkinfos"
    LOGGER.info("首页_现金分期_工作信息获取-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期_工作信息获取-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期_工作信息获取-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashconfirms(gps_latitude, gps_longitude, orderid, source):
    """
    首页_现金分期_提交申请-H5
    :param gps_longitude: GPS经度,number
    :param orderid: 订单ID,string
    :param source: 来源,number
    :param gps_latitude: GPS纬度,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2722')
    requesturl = baseUrl + "/v5/cashconfirms"
    LOGGER.info("首页_现金分期_提交申请-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["gps_latitude"] = gps_latitude
    params["gps_longitude"] = gps_longitude
    params["orderId"] = orderid
    params["source"] = source
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期_提交申请-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期_提交申请-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashstages():
    """
    首页_现金分期页面-H5
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2723')
    requesturl = baseUrl + "/v5/cashstages"
    LOGGER.info("首页_现金分期页面-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期页面-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期页面-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashclosenotices():
    """
    首页_现金分期页面_关闭审核未通过消息通知-H5
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2724')
    requesturl = baseUrl + "/v5/cashclosenotices"
    LOGGER.info("首页_现金分期页面_关闭审核未通过消息通知-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期页面_关闭审核未通过消息通知-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期页面_关闭审核未通过消息通知-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_creditzmfhtmls(merchantid, nextrouter, orderid, productsku):
    """
    芝麻分查询_H5
    :param orderid: 订单ID,number
    :param merchantid: 商户ID,number
    :param nextrouter: 跳转地址,string
    :param productsku: 商品sku,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2725')
    requesturl = baseUrl + "/v5/creditzmfhtmls"
    LOGGER.info("芝麻分查询_H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantId"] = merchantid
    params["nextRouter"] = nextrouter
    params["orderId"] = orderid
    params["productSku"] = productsku
    params["token"] = LICENCES
    LOGGER.info("芝麻分查询_H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("芝麻分查询_H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstgetxxinfos():
    """
    首页_H5_获取用户学信网帐号密码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2726')
    requesturl = baseUrl + "/v5/firstgetxxinfos"
    LOGGER.info("首页_H5_获取用户学信网帐号密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("首页_H5_获取用户学信网帐号密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5_获取用户学信网帐号密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstspecialinfosaves(bucket, carlicense, carnum, carphotoname, houseaddress, housenum, housephotoname):
    """
    首页_H5分期_特别信息保存
    :param carnum: 车牌号,string
    :param housenum: 房产证号,string
    :param housephotoname: 房产证照片名,string
    :param houseaddress: 产权地址,string
    :param carlicense: 车辆行驶证,string
    :param bucket: 七牛存储空间名,string
    :param carphotoname: 车辆行驶证照片名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2727')
    requesturl = baseUrl + "/v5/firstspecialinfosaves"
    LOGGER.info("首页_H5分期_特别信息保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["carLicense"] = carlicense
    params["carNum"] = carnum
    params["carPhotoName"] = carphotoname
    params["houseAddress"] = houseaddress
    params["houseNum"] = housenum
    params["housePhotoName"] = housephotoname
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_特别信息保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_特别信息保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstspecialinfos():
    """
    首页_H5分期_特别信息获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2728')
    requesturl = baseUrl + "/v5/firstspecialinfos"
    LOGGER.info("首页_H5分期_特别信息获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_特别信息获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_特别信息获取请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstextrainfosaves(extralist, orderid):
    """
    首页_H5分期_补充照片保存（补充材料）
    :param orderid: 订单ID,number
    :param extralist: 补充材料列表（json）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2729')
    requesturl = baseUrl + "/v5/firstextrainfosaves"
    LOGGER.info("首页_H5分期_补充照片保存（补充材料）请求地址:【{}】".format(requesturl))
    params = dict()
    params["extraList"] = extralist
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_补充照片保存（补充材料）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_补充照片保存（补充材料）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstextrainfos(orderid):
    """
    首页_H5分期_补充照片获取（补充材料）
    :param orderid: 订单ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2730')
    requesturl = baseUrl + "/v5/firstextrainfos"
    LOGGER.info("首页_H5分期_补充照片获取（补充材料）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_补充照片获取（补充材料）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_补充照片获取（补充材料）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstresultpages(orderid):
    """
    首页_H5分期_订单分期结果详情
    :param orderid: 订单Id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2731')
    requesturl = baseUrl + "/v5/firstresultpages"
    LOGGER.info("首页_H5分期_订单分期结果详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_订单分期结果详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_订单分期结果详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstconfirmphotoinfos(orderid):
    """
    首页_分期商品订单_确认收获_拍摄确认照片页面信息获取
    :param orderid: 订单ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2732')
    requesturl = baseUrl + "/v5/firstconfirmphotoinfos"
    LOGGER.info("首页_分期商品订单_确认收获_拍摄确认照片页面信息获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("首页_分期商品订单_确认收获_拍摄确认照片页面信息获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_分期商品订单_确认收获_拍摄确认照片页面信息获取请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstourorderlists(page):
    """
    首页_我的分期列表-APP
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2733')
    requesturl = baseUrl + "/v5/firstourorderlists"
    LOGGER.info("首页_我的分期列表-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("首页_我的分期列表-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_我的分期列表-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstcancelorders(orderid, reason):
    """
    首页_现金分期_取消提现-APP
    :param reason: 取消原因,string
    :param orderid: 订单ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2734')
    requesturl = baseUrl + "/v5/firstcancelorders"
    LOGGER.info("首页_现金分期_取消提现-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["reason"] = reason
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期_取消提现-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期_取消提现-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashgets(orderid, repaybankid):
    """
    首页_现金分期_提现到银行卡-APP
    :param orderid: 订单ID,number
    :param repaybankid: 收款银行卡ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2735')
    requesturl = baseUrl + "/v5/cashgets"
    LOGGER.info("首页_现金分期_提现到银行卡-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["repayBankId"] = repaybankid
    params["token"] = LICENCES
    LOGGER.info("首页_现金分期_提现到银行卡-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_现金分期_提现到银行卡-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashsavecheckrzs(status):
    """
    保存用户认证结果（借记卡,信用卡,芝麻分,电商,运营商)-H5
    :param status: 1借记卡认证通过； 2信用卡认证通过； 3芝麻分认证通过； 4电商认证通过； 5运营商认证通过,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2736')
    requesturl = baseUrl + "/v5/cashsavecheckrzs"
    LOGGER.info("保存用户认证结果（借记卡,信用卡,芝麻分,电商,运营商)-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["status"] = status
    params["token"] = LICENCES
    LOGGER.info("保存用户认证结果（借记卡,信用卡,芝麻分,电商,运营商)-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存用户认证结果（借记卡,信用卡,芝麻分,电商,运营商)-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashpayments(cardid, dkitemid, summoney):
    """
    普通账单_还款支付-APP
    :param cardid: 银行卡ID,number
    :param dkitemid: 分期还款计划ID。 多个用逗号分隔。如：34,35,26s,string
    :param summoney: 付款金额,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2737')
    requesturl = baseUrl + "/v5/cashpayments"
    LOGGER.info("普通账单_还款支付-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardId"] = cardid
    params["dkItemId"] = dkitemid
    params["summoney"] = summoney
    params["token"] = LICENCES
    LOGGER.info("普通账单_还款支付-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("普通账单_还款支付-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashpaymentpages():
    """
    普通账单还款页面-APP
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2738')
    requesturl = baseUrl + "/v5/cashpaymentpages"
    LOGGER.info("普通账单还款页面-APP请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("普通账单还款页面-APP请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("普通账单还款页面-APP请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_scanpayments(cardid, paytype, sourcepage, summoney):
    """
    月度账单还款
    :param summoney: 付款金额,string
    :param cardid: 银行卡ID,number
    :param sourcepage: 1表示还当前剩余应还，2表示从【未出账单】中进入还款,number
    :param paytype: 2账单还款,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2739')
    requesturl = baseUrl + "/v5/scanpayments"
    LOGGER.info("月度账单还款请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardId"] = cardid
    params["payType"] = paytype
    params["sourcePage"] = sourcepage
    params["summoney"] = summoney
    params["token"] = LICENCES
    LOGGER.info("月度账单还款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("月度账单还款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_cashcheckrzs():
    """
    查询用户是否已经认证借记卡,信用卡,芝麻分,电商,运营商-H5
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2740')
    requesturl = baseUrl + "/v5/cashcheckrzs"
    LOGGER.info("查询用户是否已经认证借记卡,信用卡,芝麻分,电商,运营商-H5请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询用户是否已经认证借记卡,信用卡,芝麻分,电商,运营商-H5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户是否已经认证借记卡,信用卡,芝麻分,电商,运营商-H5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_firstconfirmsaves(gps_latitude, gps_longitude, orderid, repaybankid, repaymoney, repaynum, source):
    """
    首页_H5分期_确认分期(提交申请)
    :param gps_longitude: GPS经度,number
    :param gps_latitude: GPS纬度,number
    :param source: 来源,number
    :param orderid: 订单ID,number
    :param repaybankid: 还款银行卡Id,number
    :param repaymoney: 申请分期金额,string
    :param repaynum: 分期数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2741')
    requesturl = baseUrl + "/v5/firstconfirmsaves"
    LOGGER.info("首页_H5分期_确认分期(提交申请)请求地址:【{}】".format(requesturl))
    params = dict()
    params["gps_latitude"] = gps_latitude
    params["gps_longitude"] = gps_longitude
    params["orderId"] = orderid
    params["repayBankId"] = repaybankid
    params["repayMoney"] = repaymoney
    params["repayNum"] = repaynum
    params["source"] = source
    params["token"] = LICENCES
    LOGGER.info("首页_H5分期_确认分期(提交申请)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页_H5分期_确认分期(提交申请)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_tests(content):
    """
    数据保存接口
    :param content: 需要保存的json数据,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2742')
    requesturl = baseUrl + "/v5/tests"
    LOGGER.info("数据保存接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["content"] = content
    LOGGER.info("数据保存接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("数据保存接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billlists(billid, page):
    """
    账单_账单查询
    :param billid: 账单ID,number
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2743')
    requesturl = baseUrl + "/v5/billlists"
    LOGGER.info("账单_账单查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("账单_账单查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_账单查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billhistorylists(page):
    """
    账单_历史账单页面
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2744')
    requesturl = baseUrl + "/v5/billhistorylists"
    LOGGER.info("账单_历史账单页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("账单_历史账单页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_历史账单页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billafters(page):
    """
    账单_未出账单页面
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2745')
    requesturl = baseUrl + "/v5/billafters"
    LOGGER.info("账单_未出账单页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["token"] = LICENCES
    LOGGER.info("账单_未出账单页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_未出账单页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billpaytypes(orderid, paytype):
    """
    账单_账单还款_选择支付方式
    :param paytype: 支付类型。 1分期支付；2还款,number
    :param orderid: 订单ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2746')
    requesturl = baseUrl + "/v5/billpaytypes"
    LOGGER.info("账单_账单还款_选择支付方式请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["payType"] = paytype
    params["token"] = LICENCES
    LOGGER.info("账单_账单还款_选择支付方式请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_账单还款_选择支付方式请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billpaypages(billid, billtype):
    """
    账单_还款页面
    :param billid: 账单ID（从【未出账单】中进入，不传）,number
    :param billtype: 类型（1从未出账单进入；2其它页面进入）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2747')
    requesturl = baseUrl + "/v5/billpaypages"
    LOGGER.info("账单_还款页面请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["billType"] = billtype
    params["token"] = LICENCES
    LOGGER.info("账单_还款页面请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单_还款页面请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billfirsts():
    """
    账单首页
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2748')
    requesturl = baseUrl + "/v5/billfirsts"
    LOGGER.info("账单首页请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("账单首页请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单首页请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_otherinitlogins():
    """
    初始化登陆，获取公钥（不加密）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2749')
    requesturl = baseUrl + "/v5/otherinitlogins"
    LOGGER.info("初始化登陆，获取公钥（不加密）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("初始化登陆，获取公钥（不加密）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初始化登陆，获取公钥（不加密）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_othersendsms():
    """
    发送短信
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2750')
    requesturl = baseUrl + "/v5/othersendsms"
    LOGGER.info("发送短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("发送短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_otherlogins(code, name, name2, phone, pwd, system, type, version):
    """
    普通登录
    :param pwd: 密码【账号密码登录】[MD5加密]（登录方法一）,string
    :param version: app版本号,string
    :param name: 设备名,string
    :param code: 短信验证码【短信登录】（登录方法二）s,string
    :param name2: 机型,string
    :param system: 系统版本（加密）[内容包含iOS 或android],string
    :param phone: 账号,string
    :param type: 设备号（加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2751')
    requesturl = baseUrl + "/v5/otherlogins"
    LOGGER.info("普通登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["name2"] = name2
    params["phone"] = phone
    params["pwd"] = pwd
    params["system"] = system
    params["type"] = type
    params["version"] = version
    LOGGER.info("普通登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("普通登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_otherregisters(code, name, name2, phone, pwd, system, type, version):
    """
    注册
    :param code: 短信验证码,string
    :param system: 系统（加密）[内容包含iOS 或android]s,string
    :param type: 设备号（加密）,string
    :param phone: 手机号,string
    :param version: app版本号,string
    :param name2: 机型,string
    :param pwd: 密码[MD5加密],string
    :param name: 设备名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2752')
    requesturl = baseUrl + "/v5/otherregisters"
    LOGGER.info("注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["name2"] = name2
    params["phone"] = phone
    params["pwd"] = pwd
    params["system"] = system
    params["type"] = type
    params["version"] = version
    LOGGER.info("注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_otherloginouts():
    """
    退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2753')
    requesturl = baseUrl + "/v5/otherloginouts"
    LOGGER.info("退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourcheckcodes(code, phone):
    """
    我的_账户与安全_修改支付密码_不记得_验证短信
    :param code: 短信验证码,string
    :param phone: 接收验证码的手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2754')
    requesturl = baseUrl + "/v5/ourcheckcodes"
    LOGGER.info("我的_账户与安全_修改支付密码_不记得_验证短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["token"] = LICENCES
    LOGGER.info("我的_账户与安全_修改支付密码_不记得_验证短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_账户与安全_修改支付密码_不记得_验证短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourcheckpaypws(oldpassword):
    """
    我的_账户与安全_修改支付密码_记得_验证支付密码
    :param oldpassword: 支付密码（MD5加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2755')
    requesturl = baseUrl + "/v5/ourcheckpaypws"
    LOGGER.info("我的_账户与安全_修改支付密码_记得_验证支付密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["oldPassword"] = oldpassword
    params["token"] = LICENCES
    LOGGER.info("我的_账户与安全_修改支付密码_记得_验证支付密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_账户与安全_修改支付密码_记得_验证支付密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourmodifypaypws(newpassword):
    """
    我的_账户与安全_修改支付密码_设置支付密码
    :param newpassword: 新支付密码（MD5加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2756')
    requesturl = baseUrl + "/v5/ourmodifypaypws"
    LOGGER.info("我的_账户与安全_修改支付密码_设置支付密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["newPassword"] = newpassword
    params["token"] = LICENCES
    LOGGER.info("我的_账户与安全_修改支付密码_设置支付密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_账户与安全_修改支付密码_设置支付密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourmodifyloginpws(code, newpassword, phone):
    """
    我的_账户与安全_修改登录密码
    :param phone: 手机号,string
    :param code: 验证码,string
    :param newpassword: 新密码（MD5加密）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2757')
    requesturl = baseUrl + "/v5/ourmodifyloginpws"
    LOGGER.info("我的_账户与安全_修改登录密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["newPassword"] = newpassword
    params["phone"] = phone
    params["token"] = LICENCES
    LOGGER.info("我的_账户与安全_修改登录密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_账户与安全_修改登录密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourbankcards():
    """
    我的_银行卡管理
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2758')
    requesturl = baseUrl + "/v5/ourbankcards"
    LOGGER.info("我的_银行卡管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("我的_银行卡管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_银行卡管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourbankcardsetautos(id, no_agree):
    """
    我的_银行卡管理_设置为自动还款卡
    :param id: 银行卡ID,number
    :param no_agree: 连连中银行签约的唯一编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2759')
    requesturl = baseUrl + "/v5/ourbankcardsetautos"
    LOGGER.info("我的_银行卡管理_设置为自动还款卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["no_agree"] = no_agree
    params["token"] = LICENCES
    LOGGER.info("我的_银行卡管理_设置为自动还款卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_银行卡管理_设置为自动还款卡请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourphonemodifies(code, phone):
    """
    我的_修改手机号
    :param phone: 新手机号,string
    :param code: 短信验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2760')
    requesturl = baseUrl + "/v5/ourphonemodifies"
    LOGGER.info("我的_修改手机号请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["token"] = LICENCES
    LOGGER.info("我的_修改手机号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_修改手机号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourphonecheckcodes(code, phone):
    """
    我的_修改手机号_验证原手机号短信验证码
    :param code: 短信验证码,string
    :param phone: 发送验证码的手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2761')
    requesturl = baseUrl + "/v5/ourphonecheckcodes"
    LOGGER.info("我的_修改手机号_验证原手机号短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["token"] = LICENCES
    LOGGER.info("我的_修改手机号_验证原手机号短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_修改手机号_验证原手机号短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourphonechecknames():
    """
    我的_修改手机号_验证用户是否实名
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2762')
    requesturl = baseUrl + "/v5/ourphonechecknames"
    LOGGER.info("我的_修改手机号_验证用户是否实名请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("我的_修改手机号_验证用户是否实名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_修改手机号_验证用户是否实名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourphonecheckcards(cardno, id, idcard):
    """
    我的_修改手机号_验证银行卡
    :param cardno: 银行卡号,string
    :param id: 银行卡ID,number
    :param idcard: 身份证号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2763')
    requesturl = baseUrl + "/v5/ourphonecheckcards"
    LOGGER.info("我的_修改手机号_验证银行卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNo"] = cardno
    params["id"] = id
    params["idCard"] = idcard
    params["token"] = LICENCES
    LOGGER.info("我的_修改手机号_验证银行卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_修改手机号_验证银行卡请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourmodifypics(bucket, userpicture):
    """
    我的_修改用户头像
    :param bucket: 七牛图片存储空间名字,string
    :param userpicture: 用户头像图片名字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2764')
    requesturl = baseUrl + "/v5/ourmodifypics"
    LOGGER.info("我的_修改用户头像请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["userPicture"] = userpicture
    params["token"] = LICENCES
    LOGGER.info("我的_修改用户头像请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_修改用户头像请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourfeedbacksaves(contact, detial):
    """
    我的_设置_反馈建议保存
    :param contact: 联系方式,string
    :param detial: 建议,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2765')
    requesturl = baseUrl + "/v5/ourfeedbacksaves"
    LOGGER.info("我的_设置_反馈建议保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["contact"] = contact
    params["detial"] = detial
    params["token"] = LICENCES
    LOGGER.info("我的_设置_反馈建议保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_设置_反馈建议保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_oursethelps(page):
    """
    我的_设置_帮助中心
    :param page: 当前页数。默认1,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2766')
    requesturl = baseUrl + "/v5/oursethelps"
    LOGGER.info("我的_设置_帮助中心请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    LOGGER.info("我的_设置_帮助中心请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_设置_帮助中心请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_oursethelpdetails(helpid):
    """
    我的_设置_帮助中心详情
    :param helpid: 文章ID,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2767')
    requesturl = baseUrl + "/v5/oursethelpdetails"
    LOGGER.info("我的_设置_帮助中心详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["helpId"] = helpid
    params["token"] = LICENCES
    LOGGER.info("我的_设置_帮助中心详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_设置_帮助中心详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_oursethelpchecks(helpid, ishelp):
    """
    我的_设置_帮助中心详情_是否对你有帮助
    :param helpid: 文章ID,number
    :param ishelp: 2有用；3无用,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2768')
    requesturl = baseUrl + "/v5/oursethelpchecks"
    LOGGER.info("我的_设置_帮助中心详情_是否对你有帮助请求地址:【{}】".format(requesturl))
    params = dict()
    params["helpId"] = helpid
    params["isHelp"] = ishelp
    params["token"] = LICENCES
    LOGGER.info("我的_设置_帮助中心详情_是否对你有帮助请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_设置_帮助中心详情_是否对你有帮助请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_ourcontracts():
    """
    我的_设置_服务合同
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2769')
    requesturl = baseUrl + "/v5/ourcontracts"
    LOGGER.info("我的_设置_服务合同请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("我的_设置_服务合同请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的_设置_服务合同请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_uploadalltelephones(contacts):
    """
    后台批量上传用户通讯录
    :param contacts: 通讯录信息 （json串）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2770')
    requesturl = baseUrl + "/v5/uploadalltelephones"
    LOGGER.info("后台批量上传用户通讯录请求地址:【{}】".format(requesturl))
    params = dict()
    params["contacts"] = contacts
    params["token"] = LICENCES
    LOGGER.info("后台批量上传用户通讯录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("后台批量上传用户通讯录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_otherversions(version):
    """
    版本管理
    :param version: app版本,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2771')
    requesturl = baseUrl + "/v5/otherversions"
    LOGGER.info("版本管理请求地址:【{}】".format(requesturl))
    params = dict()
    params["version"] = version
    LOGGER.info("版本管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("版本管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqcupdateorderstatus(orderid):
    """
    资料补录---获取进件配置
    :param orderid: 订单id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2773')
    requesturl = baseUrl + "/v5/xqcupdateorderstatus"
    LOGGER.info("资料补录---获取进件配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("资料补录---获取进件配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资料补录---获取进件配置请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqcqiniuvideos(bucket):
    """
    获取七牛上传token-视频
    :param bucket: 七牛空间名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2774')
    requesturl = baseUrl + "/v5/xqcqiniuvideos"
    LOGGER.info("获取七牛上传token-视频请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    LOGGER.info("获取七牛上传token-视频请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛上传token-视频请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_platpayments(cardid, orderid, summoney):
    """
    平台手续费支付接口
    :param cardid: 银行卡ID,string
    :param orderid: 订单ID,string
    :param summoney: 平台服务费付款金额,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2785')
    requesturl = baseUrl + "/v5/platpayments"
    LOGGER.info("平台手续费支付接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardId"] = cardid
    params["orderId"] = orderid
    params["summoney"] = summoney
    params["token"] = LICENCES
    LOGGER.info("平台手续费支付接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("平台手续费支付接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_spiderlogins():
    """
    爬虫登录接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2786')
    requesturl = baseUrl + "/v5/spiderlogins"
    LOGGER.info("爬虫登录接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("爬虫登录接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("爬虫登录接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqhupdateorderstatus(orderid):
    """
    资料补录---完成补充更新订单补录状态
    :param orderid: 订单id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2787')
    requesturl = baseUrl + "/v5/xqhupdateorderstatus"
    LOGGER.info("资料补录---完成补充更新订单补录状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("资料补录---完成补充更新订单补录状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资料补录---完成补充更新订单补录状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqhgetorderconfigs(orderid):
    """
    资料补录---获取进件配置
    :param orderid: 订单id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2788')
    requesturl = baseUrl + "/v5/xqhgetorderconfigs"
    LOGGER.info("资料补录---获取进件配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("资料补录---获取进件配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资料补录---获取进件配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqhqiniuvideos(bucket):
    """
    获取七牛上传token-视频
    :param bucket: 七牛空间名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2789')
    requesturl = baseUrl + "/v5/xqhqiniuvideos"
    LOGGER.info("获取七牛上传token-视频请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    LOGGER.info("获取七牛上传token-视频请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛上传token-视频请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqhplans(amount, merchantid, nums, productsku):
    """
    获取分期详情-还款计划
    :param amount: 总金额,number
    :param nums: 分期数,string
    :param productsku: 商品SKU,string
    :param merchantid: 商户ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2790')
    requesturl = baseUrl + "/v5/xqhplans"
    LOGGER.info("获取分期详情-还款计划请求地址:【{}】".format(requesturl))
    params = dict()
    params["amount"] = amount
    params["merchantId"] = merchantid
    params["nums"] = nums
    params["productSku"] = productsku
    params["token"] = LICENCES
    LOGGER.info("获取分期详情-还款计划请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取分期详情-还款计划请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_xqhsaveqiniuvideos(bucket, key, orderid):
    """
    保存录入视频接口
    :param orderid: 订单id,string
    :param key: 七牛视频上传成功的key,string
    :param bucket: 七牛bucket,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2791')
    requesturl = baseUrl + "/v5/xqhsaveqiniuvideos"
    LOGGER.info("保存录入视频接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["bucket"] = bucket
    params["key"] = key
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("保存录入视频接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存录入视频接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_sms_deliveries(data, phone, type):
    """
    发送短信
    :param data: 填充数据,string
    :param phone: 手机号,string
    :param type: 短信模板,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2824')
    requesturl = baseUrl + "/sms/deliveries"
    LOGGER.info("发送短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["data"] = data
    params["phone"] = phone
    params["type"] = type
    LOGGER.info("发送短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_deliversigns(orderid):
    """
    确认收货-签署交付确认书
    :param orderid: 订单ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2825')
    requesturl = baseUrl + "/v5/deliversigns"
    LOGGER.info("确认收货-签署交付确认书请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    params["token"] = LICENCES
    LOGGER.info("确认收货-签署交付确认书请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认收货-签署交付确认书请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_deliversignchecks(orderid):
    """
    确认收货-交付确认书检查是否签字
    :param orderid: 订单ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2826')
    requesturl = baseUrl + "/v5/deliversignchecks"
    LOGGER.info("确认收货-交付确认书检查是否签字请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("确认收货-交付确认书检查是否签字请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认收货-交付确认书检查是否签字请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_v5_billalls():
    """
    全部账单列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3189')
    requesturl = baseUrl + "/v5/billalls"
    LOGGER.info("全部账单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("全部账单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全部账单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


