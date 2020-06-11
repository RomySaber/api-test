#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppAction.py
@desc       : 项目：qiloan 模块：app 接口方法封装
"""

from qiloan.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('app_apiURL', 'qiloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_app_login()


def test_api_78dk_app_login_register(mobile, vercode):
    """
    注册
    :param mobile: 手机号(Y),string
    :param vercode: 验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1406')
    requesturl = baseUrl + "/api/78dk/app/login/register"
    LOGGER.info("注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_sign(code, mobile):
    """
    登录
    :param code: 验证码（Y）,string
    :param mobile: 手机号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1407')
    requesturl = baseUrl + "/api/78dk/app/login/sign"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["mobile"] = mobile
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_sms(mobile, type):
    """
    发送验证码
    :param mobile: 手机号（Y）,string
    :param type: 类型（Y 1-注册 2-短信登陆）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1408')
    requesturl = baseUrl + "/api/78dk/app/login/sms"
    LOGGER.info("发送验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["type"] = type
    LOGGER.info("发送验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_addAuthUserInfo(address, cardaddress, city, companyname, companyproperty, day, education, idcard, idcarda, idcardb, issuingbody, jobstate, marriage, month, name, nation, province, region, scale, sex, validitybegin, validityend, workage, year):
    """
    身份证资料保存并实名认证
    :param city: 市y,string
    :param address: 详细地址Y,string
    :param companyname: 公司名称(jobState为2时，需要填写),string
    :param companyproperty: 公司性质(jobState为2时，需要填写),string
    :param education: 学历Y,string
    :param idcard: 身份证号Y,string
    :param idcarda: 身份证正面Y,string
    :param idcardb: 身份证反面Y,string
    :param jobstate: 有无工作（0未选择,1无工作 2有工作）Y,string
    :param marriage: 婚姻状况Y,string
    :param name: 姓名Y,string
    :param province: 省Y,string
    :param region: 区/县Y,string
    :param scale: 单位规模(jobState为0时，需要填写),string
    :param workage: 现单位工作年限(jobState为2时，需要填写),string
    :param year: 出生年份Y,number
    :param cardaddress: 身份证地址Y,string
    :param day: 出生天Y,number
    :param issuingbody: 签发机构Y,string
    :param month: 出生月份Y,number
    :param nation: 名族Y,string
    :param sex: 性别Y,string
    :param validitybegin: 有效开始日期Y,string
    :param validityend: 有效结束日期Y,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1409')
    requesturl = baseUrl + "/api/78dk/app/auth/addAuthUserInfo"
    LOGGER.info("身份证资料保存并实名认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["cardAddress"] = cardaddress
    params["city"] = city
    params["companyName"] = companyname
    params["companyProperty"] = companyproperty
    params["day"] = day
    params["education"] = education
    params["idcard"] = idcard
    params["idcardA"] = idcarda
    params["idcardB"] = idcardb
    params["issuingBody"] = issuingbody
    params["jobState"] = jobstate
    params["marriage"] = marriage
    params["month"] = month
    params["name"] = name
    params["nation"] = nation
    params["province"] = province
    params["region"] = region
    params["scale"] = scale
    params["sex"] = sex
    params["validityBegin"] = validitybegin
    params["validityEnd"] = validityend
    params["workAge"] = workage
    params["year"] = year
    LOGGER.info("身份证资料保存并实名认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("身份证资料保存并实名认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_addBankCard(bank, cardno, mobile, sysbankcarduuid, username):
    """
    银行卡认证
    :param bank: 银行名称(Y),string
    :param cardno: 银行卡号(Y),string
    :param mobile: 预留手机号(Y),string
    :param sysbankcarduuid: 银行卡Ui uuidY,string
    :param username: 姓名Y,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1410')
    requesturl = baseUrl + "/api/78dk/app/auth/addBankCard"
    LOGGER.info("银行卡认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["bank"] = bank
    params["cardNo"] = cardno
    params["mobile"] = mobile
    params["sysBankCardUuid"] = sysbankcarduuid
    params["userName"] = username
    LOGGER.info("银行卡认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_addContacts(contacts):
    """
    添加联系人
    :param contacts: 联系人数组,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1411')
    requesturl = baseUrl + "/api/78dk/app/auth/addContacts"
    LOGGER.info("添加联系人请求地址:【{}】".format(requesturl))
    params = dict()
    params["contacts"] = contacts
    LOGGER.info("添加联系人请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加联系人请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_queryLoanOrder():
    """
    我的申请
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1412')
    requesturl = baseUrl + "/api/78dk/app/loan/queryLoanOrder"
    LOGGER.info("我的申请请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("我的申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_result():
    """
    查询认证结果
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1413')
    requesturl = baseUrl + "/api/78dk/app/auth/result"
    LOGGER.info("查询认证结果请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询认证结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询认证结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_detailClient():
    """
    个人详情
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1414')
    requesturl = baseUrl + "/api/78dk/app/base/detailClient"
    LOGGER.info("个人详情请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("个人详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("个人详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_portrait(headpic):
    """
    头像保存
    :param headpic: 七牛返回的key值,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1415')
    requesturl = baseUrl + "/api/78dk/app/base/portrait"
    LOGGER.info("头像保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["headPic"] = headpic
    LOGGER.info("头像保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("头像保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_queryBill():
    """
    账单查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1416')
    requesturl = baseUrl + "/api/78dk/app/loan/queryBill"
    LOGGER.info("账单查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("账单查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_base_queryQuota():
    """
    用户额度
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1417')
    requesturl = baseUrl + "/api/78dk/app/base/queryQuota"
    LOGGER.info("用户额度请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户额度请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户额度请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_calculation(headfeerate, loanamount, loanperiods):
    """
    借款计算
    :param loanamount: 借款金额,string
    :param loanperiods: 借款期限（天）,number
    :param headfeerate: 服务费率,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1418')
    requesturl = baseUrl + "/api/78dk/app/loan/calculation"
    LOGGER.info("借款计算请求地址:【{}】".format(requesturl))
    params = dict()
    params["headFeeRate"] = headfeerate
    params["loanAmount"] = loanamount
    params["loanPeriods"] = loanperiods
    LOGGER.info("借款计算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("借款计算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_addLoanOrder(city, facepic, facescore, loanamount, loanperiods, sysproductuuid):
    """
    订单保存
    :param loanamount: 借款金额,string
    :param loanperiods: 期限,number
    :param city: 城市（地级市名称:成都市）,string
    :param facepic: 人脸识别照片,string
    :param sysproductuuid: 产品UUID,string
    :param facescore: 人脸识别值,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1419')
    requesturl = baseUrl + "/api/78dk/app/loan/addLoanOrder"
    LOGGER.info("订单保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["facePic"] = facepic
    params["faceScore"] = facescore
    params["loanAmount"] = loanamount
    params["loanPeriods"] = loanperiods
    params["sysProductUuid"] = sysproductuuid
    LOGGER.info("订单保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_loan_resultFlag():
    """
    判断是否可以借款
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1420')
    requesturl = baseUrl + "/api/78dk/app/loan/resultFlag"
    LOGGER.info("判断是否可以借款请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("判断是否可以借款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("判断是否可以借款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_mobleFlag(mobile):
    """
    登录判断手机号
    :param mobile: 手机号,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1421')
    requesturl = baseUrl + "/api/78dk/app/login/mobleFlag"
    LOGGER.info("登录判断手机号请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    LOGGER.info("登录判断手机号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录判断手机号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_queryContacts():
    """
    查询联系人
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1422')
    requesturl = baseUrl + "/api/78dk/app/auth/queryContacts"
    LOGGER.info("查询联系人请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询联系人请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询联系人请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_queryUserInfo():
    """
    查询身份证信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1423')
    requesturl = baseUrl + "/api/78dk/app/auth/queryUserInfo"
    LOGGER.info("查询身份证信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询身份证信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询身份证信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_queryBankCard():
    """
    银行卡列表、支持银行
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1424')
    requesturl = baseUrl + "/api/78dk/app/auth/queryBankCard"
    LOGGER.info("银行卡列表、支持银行请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("银行卡列表、支持银行请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡列表、支持银行请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_detailBankCard():
    """
    回显银行
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1425')
    requesturl = baseUrl + "/api/78dk/app/auth/detailBankCard"
    LOGGER.info("回显银行请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("回显银行请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("回显银行请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_addIdCardInfo(cardaddress, day, idcard, idcarda, idcardb, issuingbody, month, name, nation, sex, validitybegin, validityend, year):
    """
    身份证实名-ORC身份证信息保存
    :param cardaddress: 身份证地址Y,string
    :param day: 出生天Y,number
    :param idcard: 身份证号Y,string
    :param idcarda: 身份证正面Y,string
    :param idcardb: 身份证反面Y,string
    :param issuingbody: 签发机构Y,string
    :param month: 出生月份Y,number
    :param name: 姓名Y,string
    :param nation: 名族Y,string
    :param sex: 性别0男  1女 2其他Y,string
    :param validitybegin: 有效开始日期(yyyy-MM-dd)Y,string
    :param validityend: 有效结束日期(yyyy-MM-dd)Y,string
    :param year: 出生年份Y,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1426')
    requesturl = baseUrl + "/api/78dk/app/auth/addIdCardInfo"
    LOGGER.info("身份证实名-ORC身份证信息保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardAddress"] = cardaddress
    params["day"] = day
    params["idcard"] = idcard
    params["idcardA"] = idcarda
    params["idcardB"] = idcardb
    params["issuingBody"] = issuingbody
    params["month"] = month
    params["name"] = name
    params["nation"] = nation
    params["sex"] = sex
    params["validityBegin"] = validitybegin
    params["validityEnd"] = validityend
    params["year"] = year
    LOGGER.info("身份证实名-ORC身份证信息保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("身份证实名-ORC身份证信息保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_loginOut():
    """
    退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1427')
    requesturl = baseUrl + "/api/78dk/app/login/loginOut"
    LOGGER.info("退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_addRealUserInfo(address, cardaddress, city, companyname, companyproperty, day, education, idcard, idcarda, idcardb, issuingbody, jobstate, marriage, month, name, nation, province, region, scale, sex, validitybegin, validityend, workage, year):
    """
    身份证实名-实时保存
    :param address: 详细地址,string
    :param cardaddress: 身份证地址,string
    :param city: 市,string
    :param companyname: 公司名称,string
    :param companyproperty: 公司性质,string
    :param day: 出生天(day,month,year要么都没值，要么都有值),number
    :param education: 学历,string
    :param idcard: 身份证号,string
    :param idcarda: 身份证正面,string
    :param idcardb: 身份证反面,string
    :param issuingbody: 签发机构,string
    :param jobstate: 有无工作（0未选择,1无工作 2有工作）,string
    :param marriage: 婚姻状况,string
    :param month: 出生月份(day,month,year要么都没值，要么都有值),number
    :param name: 姓名,string
    :param nation: 名族,string
    :param province: 省,string
    :param region: 区/县,string
    :param scale: 单位规模,string
    :param sex: 性别,string
    :param validitybegin: 有效开始日期,string
    :param validityend: 有效结束日期,string
    :param workage: 现单位工作年限,string
    :param year: 出生年份(day,month,year要么都没值，要么都有值),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1428')
    requesturl = baseUrl + "/api/78dk/app/auth/addRealUserInfo"
    LOGGER.info("身份证实名-实时保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["cardAddress"] = cardaddress
    params["city"] = city
    params["companyName"] = companyname
    params["companyProperty"] = companyproperty
    params["day"] = day
    params["education"] = education
    params["idcard"] = idcard
    params["idcardA"] = idcarda
    params["idcardB"] = idcardb
    params["issuingBody"] = issuingbody
    params["jobState"] = jobstate
    params["marriage"] = marriage
    params["month"] = month
    params["name"] = name
    params["nation"] = nation
    params["province"] = province
    params["region"] = region
    params["scale"] = scale
    params["sex"] = sex
    params["validityBegin"] = validitybegin
    params["validityEnd"] = validityend
    params["workAge"] = workage
    params["year"] = year
    LOGGER.info("身份证实名-实时保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("身份证实名-实时保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_executeAuth(executetype):
    """
    执行运营商或电商认证
    :param executetype: 电商认证0，运营商认证1,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1429')
    requesturl = baseUrl + "/api/78dk/app/auth/executeAuth"
    LOGGER.info("执行运营商或电商认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["executeType"] = executetype
    LOGGER.info("执行运营商或电商认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("执行运营商或电商认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_uploadAddressBook(addressbookjson):
    """
    上传通讯录
    :param addressbookjson: 通讯录json数据,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1430')
    requesturl = baseUrl + "/api/78dk/app/common/uploadAddressBook"
    LOGGER.info("上传通讯录请求地址:【{}】".format(requesturl))
    params = dict()
    params["addressBookJson"] = addressbookjson
    LOGGER.info("上传通讯录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("上传通讯录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_queryDicItemName(dictcode):
    """
    根据字典条目Code返回字典条目名称
    :param dictcode: 字典条目编号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1431')
    requesturl = baseUrl + "/api/78dk/app/common/queryDicItemName"
    LOGGER.info("根据字典条目Code返回字典条目名称请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictCode"] = dictcode
    LOGGER.info("根据字典条目Code返回字典条目名称请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据字典条目Code返回字典条目名称请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_queryDicItemList(dicttypecode):
    """
    根据字典类型Code返回字典条目列表
    :param dicttypecode: 字典类型编号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1432')
    requesturl = baseUrl + "/api/78dk/app/common/queryDicItemList"
    LOGGER.info("根据字典类型Code返回字典条目列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictTypeCode"] = dicttypecode
    LOGGER.info("根据字典类型Code返回字典条目列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据字典类型Code返回字典条目列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_queryQiNiuToken(type):
    """
    获取七牛token
    :param type: string,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1433')
    requesturl = baseUrl + "/api/78dk/app/common/queryQiNiuToken"
    LOGGER.info("获取七牛token请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    LOGGER.info("获取七牛token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_auth_isDebitCard(cardno):
    """
    验证是否为借记卡
    :param cardno: 银行卡号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1529')
    requesturl = baseUrl + "/api/78dk/app/auth/isDebitCard"
    LOGGER.info("验证是否为借记卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNo"] = cardno
    LOGGER.info("验证是否为借记卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("验证是否为借记卡请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_h5_register(linkuuid, mobile, vercode):
    """
    H5注册
    :param mobile: 手机号(Y),string
    :param vercode: 验证码（Y）,string
    :param linkuuid: 链接uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1682')
    requesturl = baseUrl + "/api/78dk/app/h5/register"
    LOGGER.info("H5注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["linkUuid"] = linkuuid
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("H5注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("H5注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_h5_sendSms(mobile, picvercode, type, verid):
    """
    短信发送
    :param picvercode: 验证码code（Y）,string
    :param mobile: 手机号（Y）,string
    :param verid: 验证码id（Y）,string
    :param type: tc-弹窗,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1683')
    requesturl = baseUrl + "/api/78dk/app/h5/sendSms"
    LOGGER.info("短信发送请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["picVerCode"] = picvercode
    params["type"] = type
    params["verId"] = verid
    LOGGER.info("短信发送请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("短信发送请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getPicVerCode():
    """
    获取图形验证码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1684')
    requesturl = baseUrl + "/api/78dk/app/common/getPicVerCode"
    LOGGER.info("获取图形验证码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取图形验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图形验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_h5_clickAdd(linkuuid):
    """
    页面点击统计
    :param linkuuid: 链接uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1685')
    requesturl = baseUrl + "/api/78dk/app/h5/clickAdd"
    LOGGER.info("页面点击统计请求地址:【{}】".format(requesturl))
    params = dict()
    params["linkUuid"] = linkuuid
    LOGGER.info("页面点击统计请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("页面点击统计请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


