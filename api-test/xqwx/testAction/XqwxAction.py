#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : XqwxAction.py
@desc       : 项目：xqwx 模块：xqwx 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('xqwx_apiURL', 'xqwx')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_user_login(id, phone, verifycode):
    """
    登录
    :param verifycode: 验证码,string
    :param phone: 手机号,string
    :param id: userInfo中的微信信息id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1704')
    requesturl = baseUrl + "/user/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["phone"] = phone
    params["verifyCode"] = verifycode
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_changePhone(code, newphone):
    """
    更换手机号
    :param newphone: 新手机号码,string
    :param code: 验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1705')
    requesturl = baseUrl + "/user/changePhone"
    LOGGER.info("更换手机号请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["newPhone"] = newphone
    LOGGER.info("更换手机号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更换手机号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_validateCode(code, phone, type):
    """
    验证手机与验证码是否匹配
    :param phone: 手机号,string
    :param code: 验证码,string
    :param type: 验证码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1706')
    requesturl = baseUrl + "/common/validateCode"
    LOGGER.info("验证手机与验证码是否匹配请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["type"] = type
    LOGGER.info("验证手机与验证码是否匹配请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证手机与验证码是否匹配请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_info():
    """
    获取用户信息接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1707')
    requesturl = baseUrl + "/user/info"
    LOGGER.info("获取用户信息接口请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取用户信息接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取用户信息接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_getVerifyCode(code, phone, type):
    """
    获取验证码
    :param phone: 手机号,string
    :param type: 短信类型,string
    :param code: 图片验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1708')
    requesturl = baseUrl + "/common/getVerifyCode"
    LOGGER.info("获取验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["type"] = type
    LOGGER.info("获取验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_getVerifyPic():
    """
    获取图片验证码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1709')
    requesturl = baseUrl + "/common/getVerifyPic"
    LOGGER.info("获取图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_verify_t():
    """
    验证token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1710')
    requesturl = baseUrl + "/verify_t"
    LOGGER.info("验证token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("验证token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证token请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_report_list(page, size, status):
    """
    获取购买记录
    :param page: 请求页,number
    :param status: 订单状态,number
    :param size: 请求数据量,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1711')
    requesturl = baseUrl + "/common/report/list"
    LOGGER.info("获取购买记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    params["status"] = status
    LOGGER.info("获取购买记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取购买记录请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_report_total():
    """
    获取购买数量
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1712')
    requesturl = baseUrl + "/common/report/total"
    LOGGER.info("获取购买数量请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取购买数量请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取购买数量请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_users(page, size):
    """
    历史查询人
    :param size: 单页数据量,number
    :param page: 请求页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1713')
    requesturl = baseUrl + "/report/users"
    LOGGER.info("历史查询人请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    LOGGER.info("历史查询人请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史查询人请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_history(page, size, types):
    """
    历史查询报告
    :param size: 单页数据量,number
    :param types: 需要查询的报给类型,array<number>
    :param page: 查询页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1714')
    requesturl = baseUrl + "/report/history"
    LOGGER.info("历史查询报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    params["types"] = types
    LOGGER.info("历史查询报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史查询报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_push(param, remark, tid, type):
    """
    保存报告信息
    :param param: 报告填入的参数,string
    :param remark: 其它说明,string
    :param type: 报告类型,number
    :param tid: 报告对应的task_id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1715')
    requesturl = baseUrl + "/report/push"
    LOGGER.info("保存报告信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["param"] = param
    params["remark"] = remark
    params["tid"] = tid
    params["type"] = type
    LOGGER.info("保存报告信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存报告信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_detail(id):
    """
    报告详情-加强版
    :param id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1716')
    requesturl = baseUrl + "/report/detail"
    LOGGER.info("报告详情-加强版请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("报告详情-加强版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告详情-加强版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_addUser(idcard, name, phone, remark):
    """
    历史查询人—新增
    :param remark: 备注,string
    :param name: 查询人姓名,string
    :param idcard: 查询人身份证,string
    :param phone: 查询人号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1717')
    requesturl = baseUrl + "/report/addUser"
    LOGGER.info("历史查询人—新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["phone"] = phone
    params["remark"] = remark
    LOGGER.info("历史查询人—新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("历史查询人—新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_pay_getGoods():
    """
    获取商品价格
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1718')
    requesturl = baseUrl + "/report/pay/getGoods"
    LOGGER.info("获取商品价格请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取商品价格请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取商品价格请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_pay_getParam(id, isfirst):
    """
    获取支付参数
    :param isfirst: 发起支付类型,number
    :param id: 报告 id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1719')
    requesturl = baseUrl + "/report/pay/getParam"
    LOGGER.info("获取支付参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["isFirst"] = isfirst
    LOGGER.info("获取支付参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取支付参数请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneRefreshSms(phone, phone_type, reqid):
    """
    3、刷新手机验证码接口
    :param phone: 手机号,string
    :param phone_type: 运营商类型,string
    :param reqid: 前面返回的reqId,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1720')
    requesturl = baseUrl + "/report/ai/phoneRefreshSms"
    LOGGER.info("3、刷新手机验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("3、刷新手机验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、刷新手机验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneConfig(phone, phone_type):
    """
    2、获取手机初始化配置
    :param phone: 电话号码,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1721')
    requesturl = baseUrl + "/report/ai/phoneConfig"
    LOGGER.info("2、获取手机初始化配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["phone_type"] = phone_type
    LOGGER.info("2、获取手机初始化配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、获取手机初始化配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneType(phone):
    """
    1、获取手机号类型
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1722')
    requesturl = baseUrl + "/report/ai/phoneType"
    LOGGER.info("1、获取手机号类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    LOGGER.info("1、获取手机号类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、获取手机号类型请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneRefreshPic(phone_type, reqid):
    """
    4、刷新手机图片验证码
    :param reqid: 任务的reqId,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1723')
    requesturl = baseUrl + "/report/ai/phoneRefreshPic"
    LOGGER.info("4、刷新手机图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("4、刷新手机图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、刷新手机图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneLogin():
    """
    运营商账号密码提交
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1724')
    requesturl = baseUrl + "/report/ai/phoneLogin"
    LOGGER.info("运营商账号密码提交请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("运营商账号密码提交请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营商账号密码提交请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneGetStatus(phone_type, reqid):
    """
    6、获取任务状态
    :param reqid: 前面获取到的任务id,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1725')
    requesturl = baseUrl + "/report/ai/phoneGetStatus"
    LOGGER.info("6、获取任务状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("6、获取任务状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、获取任务状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phoneGetResult(phone_type, reqid):
    """
    7、获取运营商采集数据
    :param phone_type: 运营商类型,string
    :param reqid: 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1726')
    requesturl = baseUrl + "/report/ai/phoneGetResult"
    LOGGER.info("7、获取运营商采集数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("7、获取运营商采集数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("7、获取运营商采集数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_getReportScore(id):
    """
    8、获取报告分数
    :param id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1727')
    requesturl = baseUrl + "/report/ai/getReportScore"
    LOGGER.info("8、获取报告分数请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("8、获取报告分数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("8、获取报告分数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_callback_report(signature, status, taskid):
    """
    报告结果通知
    :param status: 报告状态,string
    :param taskid: 任务id,string
    :param signature: 签名串,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1728')
    requesturl = baseUrl + "/report/callback/report"
    LOGGER.info("报告结果通知请求地址:【{}】".format(requesturl))
    params = dict()
    params["signature"] = signature
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("报告结果通知请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告结果通知请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_report_price():
    """
    获取商品价格
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1729')
    requesturl = baseUrl + "/common/report/price"
    LOGGER.info("获取商品价格请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取商品价格请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取商品价格请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_getShareConf(url):
    """
    获取分享参数
    :param url: 需要分享的url,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1730')
    requesturl = baseUrl + "/common/getShareConf"
    LOGGER.info("获取分享参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["url"] = url
    LOGGER.info("获取分享参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取分享参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_news_list(currentpage, pagesize, type):
    """
    资讯列表
    :param type: 数据类型,string
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1731')
    requesturl = baseUrl + "/news/list"
    LOGGER.info("资讯列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["type"] = type
    LOGGER.info("资讯列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资讯列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_news_info(articleinfouuid):
    """
    咨询详情
    :param articleinfouuid: 从列表中获取的资讯ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1732')
    requesturl = baseUrl + "/news/info"
    LOGGER.info("咨询详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("咨询详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("咨询详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_list(page, size, types):
    """
    获取历史列表
    :param size: 单页数据量,number
    :param types: 请求的报告类型,array<number>
    :param page: 请求页数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1733')
    requesturl = baseUrl + "/report/list"
    LOGGER.info("获取历史列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    params["types"] = types
    LOGGER.info("获取历史列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取历史列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_applyTd(idcard, name, phone, type, verifycode):
    """
    黑名单/多头
    :param idcard: 身份证,string
    :param verifycode: 验证码,string
    :param name: 姓名,string
    :param type: 报告类型,number
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1734')
    requesturl = baseUrl + "/report/applyTd"
    LOGGER.info("黑名单/多头请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["phone"] = phone
    params["type"] = type
    params["verifyCode"] = verifycode
    LOGGER.info("黑名单/多头请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("黑名单/多头请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_jlogin(name, parent_id, password):
    """
    京东-账号密码登陆接口
    :param name: 账户名,string
    :param parent_id: 父级报告id,number
    :param password: 密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1735')
    requesturl = baseUrl + "/report/business/jlogin"
    LOGGER.info("京东-账号密码登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["parent_id"] = parent_id
    params["password"] = password
    LOGGER.info("京东-账号密码登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("京东-账号密码登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_jgetqrcode():
    """
    获取京东二维码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1736')
    requesturl = baseUrl + "/report/business/jgetqrcode"
    LOGGER.info("获取京东二维码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取京东二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取京东二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_jverifyqrcode(parent_id, reqid):
    """
    验证京东二维码是否已扫描，并获取信息
    :param parent_id: 父级报告id,number
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1737')
    requesturl = baseUrl + "/report/business/jverifyqrcode"
    LOGGER.info("验证京东二维码是否已扫描，并获取信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["parent_id"] = parent_id
    params["reqId"] = reqid
    LOGGER.info("验证京东二维码是否已扫描，并获取信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证京东二维码是否已扫描，并获取信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_jverifycode(code, name, parent_id, password, reqid, type):
    """
    验证短信验证码
    :param code: 验证码,string
    :param name: 登陆用户名,string
    :param parent_id: 父级报告id,number
    :param password: 登陆密码,string
    :param reqid: 从登陆接口拿取,string
    :param type: 类型：账户登陆-ac ; 二维码登陆-qr,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1738')
    requesturl = baseUrl + "/report/business/jverifycode"
    LOGGER.info("验证短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["parent_id"] = parent_id
    params["password"] = password
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("验证短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_jgetcode():
    """
    京东-获取短信验证码接口
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1739')
    requesturl = baseUrl + "/report/business/jgetcode"
    LOGGER.info("京东-获取短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("京东-获取短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("京东-获取短信验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tlogin(name, parent_id, password):
    """
    淘宝-账号密码登陆接口
    :param name: 账户名,string
    :param password: 密码,string
    :param parent_id: 父级报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1740')
    requesturl = baseUrl + "/report/business/tlogin"
    LOGGER.info("淘宝-账号密码登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["parent_id"] = parent_id
    params["password"] = password
    LOGGER.info("淘宝-账号密码登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝-账号密码登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tgetqrcode():
    """
    获取淘宝二维码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1741')
    requesturl = baseUrl + "/report/business/tgetqrcode"
    LOGGER.info("获取淘宝二维码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取淘宝二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取淘宝二维码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tverifyqrcode(parent_id, reqid):
    """
    验证淘宝二维码是否已扫描，并获取信息
    :param reqid: 请求id,string
    :param parent_id: 父级报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1742')
    requesturl = baseUrl + "/report/business/tverifyqrcode"
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["parent_id"] = parent_id
    params["reqId"] = reqid
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tverifycode(code, name, parent_id, password, reqid, type):
    """
    验证短信验证码
    :param code: 验证码,string
    :param name: 登陆用户名,string
    :param parent_id: 父级报告id,number
    :param password: 登陆密码,string
    :param reqid: 从登陆接口拿取,string
    :param type: 类型：账户登陆-ac ; 二维码登陆-qr,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1743')
    requesturl = baseUrl + "/report/business/tverifycode"
    LOGGER.info("验证短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["parent_id"] = parent_id
    params["password"] = password
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("验证短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tgetcode(reqid, type):
    """
    淘宝-获取短信验证码接口
    :param reqid: 请求ID,string
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1744')
    requesturl = baseUrl + "/report/business/tgetcode"
    LOGGER.info("淘宝-获取短信验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("淘宝-获取短信验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝-获取短信验证码接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_history(idcard, name, noauth, phone, type):
    """
    查询最新的历史报告
    :param name: 真实名字,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param type: 报告类型,number
    :param phone: 电话号码,string
    :param idcard: 身份证号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1745')
    requesturl = baseUrl + "/h5/report/history"
    LOGGER.info("查询最新的历史报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["noauth"] = noauth
    params["phone"] = phone
    params["type"] = type
    LOGGER.info("查询最新的历史报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询最新的历史报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_login(idcard, name, noauth, password, phone, phone_type, piccode, randompassword, reqid, type):
    """
    运营商登录接口
    :param piccode: 图片验证码,string
    :param phone: 电话号码,string
    :param reqid: “获取运营商短信验证码”接口获得的请求ID,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param password: 运营商登陆密码,string
    :param idcard: 身份证,string
    :param type: 报告类型,number
    :param randompassword: 运营商下发的短信样验证码,string
    :param name: 姓名,string
    :param phone_type: 号码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1746')
    requesturl = baseUrl + "/h5/report/login"
    LOGGER.info("运营商登录接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["noauth"] = noauth
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["picCode"] = piccode
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("运营商登录接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("运营商登录接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_phoneConfig(noauth, phone, phone_type):
    """
    获取手机号码初始化配置
    :param phone_type: 电话号码类型,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone: 电话号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1747')
    requesturl = baseUrl + "/h5/report/phoneConfig"
    LOGGER.info("获取手机号码初始化配置请求地址:【{}】".format(requesturl))
    params = dict()
    params["noauth"] = noauth
    params["phone"] = phone
    params["phone_type"] = phone_type
    LOGGER.info("获取手机号码初始化配置请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手机号码初始化配置请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_phoneType(noauth, phone):
    """
    获取手机号码类型
    :param phone: 电话号码,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1748')
    requesturl = baseUrl + "/h5/report/phoneType"
    LOGGER.info("获取手机号码类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["noauth"] = noauth
    params["phone"] = phone
    LOGGER.info("获取手机号码类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取手机号码类型请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_phoneRefreshPic(noauth, phone_type, reqid):
    """
    获取运营商图片验证码
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone_type: 号码类型,string
    :param reqid: "获取手机号码初始化配置"接口获取,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1749')
    requesturl = baseUrl + "/h5/report/phoneRefreshPic"
    LOGGER.info("获取运营商图片验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["noauth"] = noauth
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取运营商图片验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取运营商图片验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_phoneRefreshSms(noauth, phone, phone_type, reqid):
    """
    获取运营商短信验证码
    :param reqid: "获取手机号码初始化配置"接口获取,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone: 手机号,string
    :param phone_type: 号码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1750')
    requesturl = baseUrl + "/h5/report/phoneRefreshSms"
    LOGGER.info("获取运营商短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["noauth"] = noauth
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取运营商短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取运营商短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_getReportScore(id, noauth):
    """
    获取报告分数
    :param id: 报告ID,number
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1751')
    requesturl = baseUrl + "/h5/report/getReportScore"
    LOGGER.info("获取报告分数请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["noauth"] = noauth
    LOGGER.info("获取报告分数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报告分数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_detail(id, noauth):
    """
    获取报告详情
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1752')
    requesturl = baseUrl + "/h5/report/detail"
    LOGGER.info("获取报告详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["noauth"] = noauth
    LOGGER.info("获取报告详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报告详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_getStatus(id, noauth):
    """
    轮询获取报告状态
    :param id: 报告id,number
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1753')
    requesturl = baseUrl + "/h5/report/getStatus"
    LOGGER.info("轮询获取报告状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["noauth"] = noauth
    LOGGER.info("轮询获取报告状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("轮询获取报告状态请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_reportPrice():
    """
    获取报告价格
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1754')
    requesturl = baseUrl + "/h5/report/reportPrice"
    LOGGER.info("获取报告价格请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取报告价格请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报告价格请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_callback(status, taskid):
    """
    AI回调接口
    :param status: 状态,string
    :param taskid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1755')
    requesturl = baseUrl + "/h5/report/callback"
    LOGGER.info("AI回调接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["status"] = status
    params["taskId"] = taskid
    LOGGER.info("AI回调接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("AI回调接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_list(max_xqc_id):
    """
    报告接口
    :param max_xqc_id: 最大的数据id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1756')
    requesturl = baseUrl + "/h5/report/list"
    LOGGER.info("报告接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["max_xqc_id"] = max_xqc_id
    LOGGER.info("报告接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_payh5_payStatus(no):
    """
    获取支付状态
    :param no: 订单no,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1757')
    requesturl = baseUrl + "/payh5/payStatus"
    LOGGER.info("获取支付状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["no"] = no
    LOGGER.info("获取支付状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取支付状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_payh5_alipay_getParam(id, phone):
    """
    支付宝提交订单
    :param phone: 手机号,string
    :param id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1758')
    requesturl = baseUrl + "/payh5/alipay/getParam"
    LOGGER.info("支付宝提交订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["phone"] = phone
    LOGGER.info("支付宝提交订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("支付宝提交订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_payh5_wechat_getParam(id, phone, scene_info):
    """
    微信提交订单
    :param phone: 手机号,string
    :param id: 生成报告id,number
    :param scene_info: 场景信息,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1759')
    requesturl = baseUrl + "/payh5/wechat/getParam"
    LOGGER.info("微信提交订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["phone"] = phone
    params["scene_info"] = scene_info
    LOGGER.info("微信提交订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("微信提交订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phonesecondverify(code, idcard, name, password, phone, phone_type, piccode, reqid):
    """
    二次验证码提交接口
    :param code: 必填  短信验证码,string
    :param idcard: 身份证号码,string
    :param name: 真实姓名,string
    :param password: 服务密码,string
    :param phone: 手机号码,string
    :param phone_type: 必填  号码类型,string
    :param piccode: 图片验证码,string
    :param reqid: 必填 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1809')
    requesturl = baseUrl + "/report/ai/phonesecondverify"
    LOGGER.info("二次验证码提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["idcard"] = idcard
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["piccode"] = piccode
    params["reqId"] = reqid
    LOGGER.info("二次验证码提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("二次验证码提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phonepicsecond(phone_type, reqid):
    """
    获取二次图片验证码接口
    :param phone_type: 必填 号码类型,string
    :param reqid: 必填 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1810')
    requesturl = baseUrl + "/report/ai/phonepicsecond"
    LOGGER.info("获取二次图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取二次图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二次图片验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_phonesmssecond(phone, phone_type, reqid):
    """
    获取二次短信验证码接口
    :param phone: （电信必填）号码,string
    :param phone_type: 号码类型,string
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1811')
    requesturl = baseUrl + "/report/ai/phonesmssecond"
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


def test_report_ai_phonestatus(phone_type, reqid):
    """
    获取运营商任务当前状态接口
    :param phone_type: 必传 号码类型,string
    :param reqid: 必传 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1812')
    requesturl = baseUrl + "/report/ai/phonestatus"
    LOGGER.info("获取运营商任务当前状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取运营商任务当前状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取运营商任务当前状态接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_secondSendCode(code, idcard, name, password, phone, phone_type, report_type, reqid, type):
    """
    二次验证码提交接口
    :param code: 短信or图片验证码,string
    :param idcard: 身份证号码,string
    :param name: 真实姓名,string
    :param password: 服务密码,string
    :param phone: 手机号码,string
    :param phone_type: 必填  号码类型,string
    :param reqid: 必填 请求id,string
    :param type: 验证码类型,string
    :param report_type: 报告类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2150')
    requesturl = baseUrl + "/report/ai/secondSendCode"
    LOGGER.info("二次验证码提交接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["idcard"] = idcard
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["phone_type"] = phone_type
    params["report_type"] = report_type
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("二次验证码提交接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("二次验证码提交接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_secondPic(phone_type, reqid):
    """
    获取二次图片验证码接口
    :param phone_type: 必填 号码类型,string
    :param reqid: 必填 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2151')
    requesturl = baseUrl + "/report/ai/secondPic"
    LOGGER.info("获取二次图片验证码接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone_type"] = phone_type
    params["reqId"] = reqid
    LOGGER.info("获取二次图片验证码接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取二次图片验证码接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_secondSms(phone, phone_type, reqid):
    """
    获取二次短信验证码接口
    :param phone: 手机号码,string
    :param phone_type: 号码类型,string
    :param reqid: 请求id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2152')
    requesturl = baseUrl + "/report/ai/secondSms"
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


def test_channel_apply():
    """
    申请代理
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2193')
    requesturl = baseUrl + "/channel/apply"
    LOGGER.info("申请代理请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("申请代理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请代理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_apply(invented_code, name, phone, verifycode, wechat_number):
    """
    申请代理
    :param invented_code: 邀请码,string
    :param name: 姓名,string
    :param phone: 手机号,string
    :param verifycode: 验证码,string
    :param wechat_number: 微信号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2195')
    requesturl = baseUrl + "/channel/agent/apply"
    LOGGER.info("申请代理请求地址:【{}】".format(requesturl))
    params = dict()
    params["invented_code"] = invented_code
    params["name"] = name
    params["phone"] = phone
    params["verifyCode"] = verifycode
    params["wechat_number"] = wechat_number
    LOGGER.info("申请代理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请代理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_agentBasic():
    """
    个人基础信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2196')
    requesturl = baseUrl + "/channel/agent/agentBasic"
    LOGGER.info("个人基础信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("个人基础信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("个人基础信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_rewardList(page, size):
    """
    平台奖励金列表
    :param page: 页码,number
    :param size: 步长,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2197')
    requesturl = baseUrl + "/channel/agent/rewardList"
    LOGGER.info("平台奖励金列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    LOGGER.info("平台奖励金列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("平台奖励金列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_cashList(page, size):
    """
    提现记录列表
    :param size: 步长,number
    :param page: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2198')
    requesturl = baseUrl + "/channel/agent/cashList"
    LOGGER.info("提现记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    LOGGER.info("提现记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提现记录列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_cashApply():
    """
    申请提现
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2199')
    requesturl = baseUrl + "/channel/agent/cashApply"
    LOGGER.info("申请提现请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("申请提现请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请提现请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_orderList(page, size):
    """
    订单提成列表
    :param size: 步长,number
    :param page: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2200')
    requesturl = baseUrl + "/channel/agent/orderList"
    LOGGER.info("订单提成列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    LOGGER.info("订单提成列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单提成列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_inventList(page, size):
    """
    邀请记录列表
    :param size: 步长,number
    :param page: 页码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2201')
    requesturl = baseUrl + "/channel/agent/inventList"
    LOGGER.info("邀请记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    LOGGER.info("邀请记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("邀请记录列表请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_channel_agent_getStatus():
    """
    代理状态获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2217')
    requesturl = baseUrl + "/channel/agent/getStatus"
    LOGGER.info("代理状态获取请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("代理状态获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("代理状态获取请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_getWaitPaymentReport():
    """
    获取最新一条待支付报告
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2549')
    requesturl = baseUrl + "/report/getWaitPaymentReport"
    LOGGER.info("获取最新一条待支付报告请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取最新一条待支付报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取最新一条待支付报告请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_insertReportComment(comment_content, comment_status, report_id):
    """
    报告评论API
    :param comment_content: 评论内容(可以为空),string
    :param comment_status: 评论状态:1喜欢(点赞)2不喜欢(踩),number
    :param report_id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2550')
    requesturl = baseUrl + "/report/insertReportComment"
    LOGGER.info("报告评论API请求地址:【{}】".format(requesturl))
    params = dict()
    params["comment_content"] = comment_content
    params["comment_status"] = comment_status
    params["report_id"] = report_id
    LOGGER.info("报告评论API请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告评论API请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_insertReportComment(comment_content, comment_status, noauth, report_id):
    """
    报告评论API
    :param comment_content: 评论内容(可以为空),string
    :param comment_status: 评论状态:1喜欢(点赞)2不喜欢(踩),number
    :param report_id: 报告id(注意此处为加密过的),number
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2553')
    requesturl = baseUrl + "/h5/report/insertReportComment"
    LOGGER.info("报告评论API请求地址:【{}】".format(requesturl))
    params = dict()
    params["comment_content"] = comment_content
    params["comment_status"] = comment_status
    params["noauth"] = noauth
    params["report_id"] = report_id
    LOGGER.info("报告评论API请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告评论API请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_updateIsNotice(report_id):
    """
    更新加强版报告中电商入参是否弹过认证失败窗口的状态
    :param report_id: 加强版报告的电商子报告的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2565')
    requesturl = baseUrl + "/report/updateIsNotice"
    LOGGER.info("更新加强版报告中电商入参是否弹过认证失败窗口的状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["report_id"] = report_id
    LOGGER.info("更新加强版报告中电商入参是否弹过认证失败窗口的状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更新加强版报告中电商入参是否弹过认证失败窗口的状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_ai_compiledReportSubmit(idcard, name, phone, taskid, type):
    """
    报告提交接口(综合报告类型3,4创建)
    :param idcard: 身份证号,string
    :param name: 姓名,string
    :param phone: 运营商账号,number
    :param taskid: 请求的task_Id,string
    :param type: 报告类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3185')
    requesturl = baseUrl + "/report/ai/compiledReportSubmit"
    LOGGER.info("报告提交接口(综合报告类型3,4创建)请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["phone"] = phone
    params["taskId"] = taskid
    params["type"] = type
    LOGGER.info("报告提交接口(综合报告类型3,4创建)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告提交接口(综合报告类型3,4创建)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_businessReportSubmit(name, parentid, taskid, type):
    """
    报告提交接口(电商报告类型1,2创建)
    :param name: 昵称或者登录名,string
    :param parentid: 电商入参的报告父级id,number
    :param taskid: 报告唯一请求id,string
    :param type: 报告类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3186')
    requesturl = baseUrl + "/report/business/businessReportSubmit"
    LOGGER.info("报告提交接口(电商报告类型1,2创建)请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["parentId"] = parentid
    params["taskId"] = taskid
    params["type"] = type
    LOGGER.info("报告提交接口(电商报告类型1,2创建)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告提交接口(电商报告类型1,2创建)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_yysReportSubmitH5(idcard, name, noauth, phone, taskid, type):
    """
    h5报告提交接口(yys报告类型3,4创建)
    :param idcard: 身份证号,string
    :param name: 姓名,string
    :param phone: 运营商账号,
    :param taskid: taskId,string
    :param type: 报告类型,number
    :param noauth: 约定的header参数,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3187')
    requesturl = baseUrl + "/h5/report/yysReportSubmitH5"
    LOGGER.info("h5报告提交接口(yys报告类型3,4创建)请求地址:【{}】".format(requesturl))
    params = dict()
    params["idcard"] = idcard
    params["name"] = name
    params["noauth"] = noauth
    params["phone"] = phone
    params["taskId"] = taskid
    params["type"] = type
    LOGGER.info("h5报告提交接口(yys报告类型3,4创建)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("h5报告提交接口(yys报告类型3,4创建)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_getUid(noauth, phone):
    """
    h5根据手机号获取uid
    :param phone: 运营商账号,
    :param noauth: 约定的header参数,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3188')
    requesturl = baseUrl + "/h5/report/getUid"
    LOGGER.info("h5根据手机号获取uid请求地址:【{}】".format(requesturl))
    params = dict()
    params["noauth"] = noauth
    params["phone"] = phone
    LOGGER.info("h5根据手机号获取uid请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("h5根据手机号获取uid请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


