#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Center_xqcAction.py
@desc       : 项目：center 模块：center_xqc 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('center_xqc_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_user_login_1575(phone, verifycode):
    """
    登录
    :param verifycode: 验证码,string
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1575')
    requesturl = baseUrl + "/user/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["phone"] = phone
    params["verifyCode"] = verifycode
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_user_changePhone_1576(code, newphone):
    """
    更换手机号
    :param code: 验证码,string
    :param newphone: 新手机号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1576')
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


def test_common_validateCode_1577(code, phone, type):
    """
    验证手机与验证码是否匹配
    :param type: 验证码类型,string
    :param phone: 手机号,string
    :param code: 验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1577')
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


def test_user_info_1578(code, ocode):
    """
    获取当前用户信息
    :param code: 微信授权code,string
    :param ocode: openId,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1578')
    requesturl = baseUrl + "/user/info"
    LOGGER.info("获取当前用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["ocode"] = ocode
    LOGGER.info("获取当前用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取当前用户信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_getVerifyCode_1579(code, phone, type):
    """
    手机获取验证码
    :param type: 请求类型,string
    :param code: 图片验证码,string
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1579')
    requesturl = baseUrl + "/common/getVerifyCode"
    LOGGER.info("手机获取验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["phone"] = phone
    params["type"] = type
    LOGGER.info("手机获取验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手机获取验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_reportPrice_1580():
    """
    获取报告价格
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1580')
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


def test_common_report_list_1581(page, size, status):
    """
    获取购买记录
    :param page: 请求页,number
    :param size: 请求数据量,number
    :param status: 订单状态,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1581')
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


def test_report_users_1582(page, size):
    """
    历史查询人
    :param size: 单页数据量,number
    :param page: 请求页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1582')
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


def test_report_history_1583(page, size, types):
    """
    历史查询报告
    :param types: 需要查询的报给类型,array<number>
    :param page: 查询页,number
    :param size: 单页数据量,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1583')
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


def test_report_push_1584(param, remark, tid, type):
    """
    保存报告信息
    :param param: 报告填入的参数,string
    :param remark: 其它说明,string
    :param type: 报告类型,number
    :param tid: 报告对应的task_id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1584')
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


def test_report_detail_1585(id):
    """
    报告详情-基础版
    :param id: 报告id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1585')
    requesturl = baseUrl + "/report/detail"
    LOGGER.info("报告详情-基础版请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("报告详情-基础版请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告详情-基础版请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_addUser_1586(idcard, name, phone, remark):
    """
    历史查询人—新增
    :param phone: 查询人号码,string
    :param remark: 备注,string
    :param idcard: 查询人身份证,string
    :param name: 查询人姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1586')
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


def test_report_ai_phoneRefreshSms_1587(phone, phone_type, reqid):
    """
    3、刷新手机验证码接口
    :param reqid: 前面返回的reqId,string
    :param phone_type: 运营商类型,string
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1587')
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


def test_report_ai_phoneConfig_1588(phone, phone_type):
    """
    2、获取手机初始化配置
    :param phone: 电话号码,string
    :param phone_type: 运营商类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1588')
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


def test_report_ai_phoneType_1589(phone):
    """
    1、获取手机号类型
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1589')
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


def test_report_ai_phoneGetResult_1590(phone_type, reqid):
    """
    7、获取运营商采集数据
    :param phone_type: 运营商类型,string
    :param reqid: 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1590')
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


def test_report_ai_phoneLogin_1591(name, password, phone_type, piccode, randompassword, reqid):
    """
    5、账号密码登录提交
    :param piccode: 图片验证码,string
    :param name: 运营商账号,string
    :param reqid: 前面分配的任务id,string
    :param password: 运营商服务密码,string
    :param phone_type: 前面获取的手机类型,string
    :param randompassword: 随机手机验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1591')
    requesturl = baseUrl + "/report/ai/phoneLogin"
    LOGGER.info("5、账号密码登录提交请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    params["phone_type"] = phone_type
    params["picCode"] = piccode
    params["randomPassword"] = randompassword
    params["reqId"] = reqid
    LOGGER.info("5、账号密码登录提交请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、账号密码登录提交请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_callback_report_1592(signature, status, taskid):
    """
    报告结果通知
    :param signature: 签名串,string
    :param taskid: 任务id,string
    :param status: 报告状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1592')
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


def test_news_list_1593(currentpage, pagesize, type):
    """
    资讯列表
    :param currentpage: 当前页码,number
    :param pagesize: 每页条数,number
    :param type: 数据类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1593')
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


def test_common_getShareConf_1594(url):
    """
    获取分享参数
    :param url: 需要分享的url,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1594')
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


def test_news_info_1595(articleinfouuid):
    """
    咨询详情
    :param articleinfouuid: 从列表中获取的资讯ID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1595')
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


def test_report_business_tlogin_1600(name, password):
    """
    淘宝-账号密码登陆接口
    :param name: 账户名,string
    :param password: 密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1600')
    requesturl = baseUrl + "/report/business/tlogin"
    LOGGER.info("淘宝-账号密码登陆接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["password"] = password
    LOGGER.info("淘宝-账号密码登陆接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("淘宝-账号密码登陆接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tverifyqrcode_1601(reqid):
    """
    验证淘宝二维码是否已扫描，并获取信息
    :param reqid: 必填,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1601')
    requesturl = baseUrl + "/report/business/tverifyqrcode"
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["reqId"] = reqid
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证淘宝二维码是否已扫描，并获取信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tverifycode_1602(code, reqid, type):
    """
    验证短信验证码
    :param code: 验证码,string
    :param reqid: 从登陆接口拿取,string
    :param type: 类型：账户登陆-ac  ;  二维码登陆-qr,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1602')
    requesturl = baseUrl + "/report/business/tverifycode"
    LOGGER.info("验证短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["reqId"] = reqid
    params["type"] = type
    LOGGER.info("验证短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证短信验证码请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_report_business_tgetcode_1616(reqid, type):
    """
    淘宝-获取短信验证码接口
    :param reqid: 请求ID,string
    :param type: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1616')
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


def test_report_list_1642(page, size, types):
    """
    获取报告列表
    :param page: 请求页数,number
    :param size: 单页数据量,number
    :param types: 请求的报告类型,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1642')
    requesturl = baseUrl + "/report/list"
    LOGGER.info("获取报告列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["page"] = page
    params["size"] = size
    params["types"] = types
    LOGGER.info("获取报告列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报告列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_common_getVerifyCode_1643(code, phone, type):
    """
    获取验证码
    :param code: 传入才会验证，不传不验证,string
    :param phone: 手机号,string
    :param type: 请求类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1643')
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


def test_report_applyTd_1644(idcard, name, phone, type, verifycode):
    """
    黑名单/多头
    :param idcard: 身份证,string
    :param name: 姓名,string
    :param phone: 手机号,string
    :param verifycode: 验证码,string
    :param type: 报告类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1644')
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


def test_report_business_tverifycode_1687(code, name, password, reqid, type):
    """
    验证短信验证码
    :param code: 验证码,string
    :param reqid: 从登陆接口拿取,string
    :param type: 类型：账户登陆-ac  ;  二维码登陆-qr,string
    :param password: 登陆密码,string
    :param name: 登陆用户名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1687')
    requesturl = baseUrl + "/report/business/tverifycode"
    LOGGER.info("验证短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
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


def test_h5_report_phoneType_1688(noauth, phone):
    """
    获取手机号码类型
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone: 电话号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1688')
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


def test_h5_report_phoneConfig_1689(noauth, phone, phone_type):
    """
    获取手机号码初始化配置
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone: 电话号码,string
    :param phone_type: 电话号码类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1689')
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


def test_h5_report_list_1690(name, noauth, page, pagesize):
    """
    报告接口
    :param name: 姓名,string
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param page: 页码,number
    :param pagesize: 每页条数,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1690')
    requesturl = baseUrl + "/h5/report/list"
    LOGGER.info("报告接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["name"] = name
    params["noauth"] = noauth
    params["page"] = page
    params["pageSize"] = pagesize
    LOGGER.info("报告接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("报告接口请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_h5_report_list_1693(max_xqc_id):
    """
    报告接口
    :param max_xqc_id: 最大的数据id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1693')
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


def test_payh5_payStatus_1694(no):
    """
    获取支付状态
    :param no: 订单no,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1694')
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


def test_payh5_alipay_getParam_1695(id, phone):
    """
    支付宝提交订单
    :param id: 报告id,number
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1695')
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


def test_payh5_wechat_getParam_1696(id, phone, scene_info):
    """
    微信提交订单
    :param scene_info: 场景信息,string
    :param id: 生成报告id,number
    :param phone: 手机号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1696')
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


def test_h5_report_history_1698(idcard, name, noauth, phone, type):
    """
    查询最新的历史报告
    :param idcard: 身份证号码,string
    :param name: 真实名字,string
    :param phone: 电话号码,string
    :param type: 报告类型,number
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1698')
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


def test_h5_report_login_1699(idcard, name, noauth, password, phone, phone_type, piccode, randompassword, reqid, type):
    """
    运营商登录接口
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param idcard: 身份证,string
    :param name: 姓名,string
    :param password: 运营商登陆密码,string
    :param phone: 电话号码,string
    :param phone_type: 号码类型,string
    :param piccode: 图片验证码,string
    :param randompassword: 运营商下发的短信样验证码,string
    :param reqid: “获取运营商短信验证码”接口获得的请求ID,string
    :param type: 报告类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1699')
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


def test_h5_report_phoneRefreshPic_1700(noauth, phone_type, reqid):
    """
    获取运营商图片验证码
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone_type: 号码类型,string
    :param reqid: "获取手机号码初始化配置"接口获取,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1700')
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


def test_h5_report_phoneRefreshSms_1701(noauth, phone, phone_type, reqid):
    """
    获取运营商短信验证码
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :param phone: 手机号,string
    :param phone_type: 号码类型,string
    :param reqid: "获取手机号码初始化配置"接口获取,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1701')
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


def test_h5_report_callback_1702(status, taskid):
    """
    AI回调接口
    :param taskid: ,string
    :param status: 状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1702')
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


def test_h5_report_getStatus_1703(id, noauth):
    """
    轮询获取报告状态
    :param id: 报告id,number
    :param noauth: （注意：此为header头）用在第三方h5接入验证,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1703')
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


