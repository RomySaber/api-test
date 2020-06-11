#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Easyloan_appAction.py
@desc       : 项目：easyloan 模块：easyloan_app 接口方法封装
"""

from easyloan.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('easyloan_app_apiURL', 'easyloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_easyloan_app_login()
API_TEST_HEADERS['Authorization'] = LICENCES


def test_api_78dk_clientapp_login_retrievedPw(mobile, password, verificationcode):
    """
    找回密码
    :param password: 密码（Y）,string
    :param mobile: 账号（Y）,string
    :param verificationcode: 验证码（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 684')
    requesturl = baseUrl + "/api/78dk/clientapp/login/retrievedPw"
    LOGGER.info("找回密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["password"] = password
    params["verificationCode"] = verificationcode
    LOGGER.info("找回密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("找回密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_login_register(invitemobile, mobile, password, verificationcode):
    """
    注册
    :param verificationcode: 验证码（Y）,number
    :param mobile: 账号（Y）,string
    :param password: 密码（Y）,string
    :param invitemobile: 邀请人手机号（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 685')
    requesturl = baseUrl + "/api/78dk/clientapp/login/register"
    LOGGER.info("注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["inviteMobile"] = invitemobile
    params["mobile"] = mobile
    params["password"] = password
    params["verificationCode"] = verificationcode
    LOGGER.info("注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_login_smsLogin(mobile, verificationcode):
    """
    短信登录
    :param mobile: 手机号（Y）,string
    :param verificationcode: 验证码（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 686')
    requesturl = baseUrl + "/api/78dk/clientapp/login/smsLogin"
    LOGGER.info("短信登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["verificationCode"] = verificationcode
    LOGGER.info("短信登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("短信登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_login_pwLogin(mobile, password):
    """
    密码登录
    :param password: 账号（Y）,string
    :param mobile: 密码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 687')
    requesturl = baseUrl + "/api/78dk/clientapp/login/pwLogin"
    LOGGER.info("密码登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["password"] = password
    LOGGER.info("密码登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("密码登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_login_loginOut():
    """
    退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 688')
    requesturl = baseUrl + "/api/78dk/clientapp/login/loginOut"
    LOGGER.info("退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_login_fastRegister(mobile, qrno, vercode):
    """
    快速注册
    :param vercode: 验证码(Y),string
    :param qrno: 二维码编号(Y),string
    :param mobile: 手机号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 689')
    requesturl = baseUrl + "/api/78dk/clientapp/login/fastRegister"
    LOGGER.info("快速注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["qrNo"] = qrno
    params["verCode"] = vercode
    LOGGER.info("快速注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("快速注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_headPhotoManag_addOrUpHeadPhoto(headpic):
    """
    1.头像添加/修改
    :param headpic: 头像(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 690')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/headPhotoManag/addOrUpHeadPhoto"
    LOGGER.info("1.头像添加/修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["headPic"] = headpic
    LOGGER.info("1.头像添加/修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.头像添加/修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_payManag_queryBorrowRecord():
    """
    1.借款交易记录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 691')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/payManag/queryBorrowRecord"
    LOGGER.info("1.借款交易记录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1.借款交易记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.借款交易记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_payManag_queryRepaymentRecord():
    """
    2.还款管理
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 692')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/payManag/queryRepaymentRecord"
    LOGGER.info("2.还款管理请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("2.还款管理请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2.还款管理请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_payManag_rueryRecharge():
    """
    3.充值记录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 693')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/payManag/rueryRecharge"
    LOGGER.info("3.充值记录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("3.充值记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3.充值记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_payManag_queryWithdrawalRecord():
    """
    4.提现记录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 694')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/payManag/queryWithdrawalRecord"
    LOGGER.info("4.提现记录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4.提现记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4.提现记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_balance_queryBalance(loantradingflowuuid):
    """
    1.显示余额
    :param loantradingflowuuid: 交易流水uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 695')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/balance/queryBalance"
    LOGGER.info("1.显示余额请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanTradingFlowUuid"] = loantradingflowuuid
    LOGGER.info("1.显示余额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.显示余额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_pay_addPromPay(bank, cardno, clientbaseuuid, clientcardsuuid):
    """
    1.立即充值
    :param clientbaseuuid: 客户Uuid(Y),string
    :param cardno: 卡号(Y),string
    :param clientcardsuuid: 客户银行卡Uuid(Y),string
    :param bank: 银行名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 696')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/pay/addPromPay"
    LOGGER.info("1.立即充值请求地址:【{}】".format(requesturl))
    params = dict()
    params["bank"] = bank
    params["cardNo"] = cardno
    params["clientBaseUuid"] = clientbaseuuid
    params["clientCardsUuid"] = clientcardsuuid
    LOGGER.info("1.立即充值请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.立即充值请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_borrowOrder_queryBorOrderList(currentpage, pagesize):
    """
    1.借款订单
    :param currentpage: 当前页数(Y正整数),number
    :param pagesize: 每页条数(Y正整数),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 697')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/borrowOrder/queryBorOrderList"
    LOGGER.info("1.借款订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    LOGGER.info("1.借款订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.借款订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_deposit_connect():
    """
    1.提现跳转
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 698')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/deposit/connect"
    LOGGER.info("1.提现跳转请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1.提现跳转请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.提现跳转请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_accountSafe_updatePassword(newpassword, oldpassword):
    """
    1.修改密码
    :param oldpassword: 老密码(Y),string
    :param newpassword: 新密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 699')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/accountSafe/updatePassword"
    LOGGER.info("1.修改密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["newPassword"] = newpassword
    params["oldPassword"] = oldpassword
    LOGGER.info("1.修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1.修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_myCenter_borrowContract_queryBorContractList():
    """
    贷款合同列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 700')
    requesturl = baseUrl + "/api/78dk/clientapp/myCenter/borrowContract/queryBorContractList"
    LOGGER.info("贷款合同列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("贷款合同列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款合同列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_tools_loanCalc_calc(loanamount, loanterm, productdetailuuid):
    """
    1、贷款计算
    :param productdetailuuid: 产品uuid,string
    :param loanterm: 期数,number
    :param loanamount: 金额,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 701')
    requesturl = baseUrl + "/api/78dk/clientapp/tools/loanCalc/calc"
    LOGGER.info("1、贷款计算请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanAmount"] = loanamount
    params["loanTerm"] = loanterm
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("1、贷款计算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、贷款计算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_tools_carEva_carTypeEva(brandid, carcode, citycode, entrancetype, miles, modelname, oncardate, provincecode):
    """
    1、车型估价
    :param carcode: 车辆编码(Y),string
    :param modelname: 车辆名称(Y),string
    :param citycode: 城市编码(Y),string
    :param brandid: 车辆品牌id(Y),string
    :param miles: 公里数(Y),number
    :param oncardate: 上牌时间(Y 时间戳),string
    :param entrancetype: 接口调用入口，1=首页-车辆评估，2=提交借款申请流程(Y),number
    :param provincecode: 省份编码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 702')
    requesturl = baseUrl + "/api/78dk/clientapp/tools/carEva/carTypeEva"
    LOGGER.info("1、车型估价请求地址:【{}】".format(requesturl))
    params = dict()
    params["brandId"] = brandid
    params["carCode"] = carcode
    params["cityCode"] = citycode
    params["entranceType"] = entrancetype
    params["miles"] = miles
    params["modelName"] = modelname
    params["onCarDate"] = oncardate
    params["provinceCode"] = provincecode
    LOGGER.info("1、车型估价请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、车型估价请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_tools_carEva_vinEva(citycode, entrancetype, miles, oncardate, vincode):
    """
    2、VIN估价
    :param citycode: 地区编码(Y),string
    :param miles: 公里数(Y),number
    :param oncardate: 上牌时间(Y 时间戳),string
    :param vincode: VIN码(Y),string
    :param entrancetype: 接口调用入口，1=首页-车辆评估，2=提交借款申请流程（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 703')
    requesturl = baseUrl + "/api/78dk/clientapp/tools/carEva/vinEva"
    LOGGER.info("2、VIN估价请求地址:【{}】".format(requesturl))
    params = dict()
    params["cityCode"] = citycode
    params["entranceType"] = entrancetype
    params["miles"] = miles
    params["onCarDate"] = oncardate
    params["vinCode"] = vincode
    LOGGER.info("2、VIN估价请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、VIN估价请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_queryAuthPro():
    """
    1、认证进度
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 704')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/queryAuthPro"
    LOGGER.info("1、认证进度请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1、认证进度请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、认证进度请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_addCarInfo(brandid, brandname, city, modelid, modelname, registertime, seriesid, seriesname, vehicleauthuuid):
    """
    2、车辆认证
    :param brandid: 车辆品牌id(Y),number
    :param seriesname: 车系名称(Y),string
    :param registertime: 车辆登记日期(Y)-时间戳（单位：毫秒）,number
    :param modelid: 车型id(Y),number
    :param seriesid: 车系id(Y),string
    :param modelname: 车型名称(Y),string
    :param city: 城市编码(Y),string
    :param vehicleauthuuid: 车辆认证uuid(N)(修改时传值),string
    :param brandname: 车辆品牌名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 705')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/addCarInfo"
    LOGGER.info("2、车辆认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["brandId"] = brandid
    params["brandName"] = brandname
    params["city"] = city
    params["modelId"] = modelid
    params["modelName"] = modelname
    params["registerTime"] = registertime
    params["seriesId"] = seriesid
    params["seriesName"] = seriesname
    params["vehicleAuthUuid"] = vehicleauthuuid
    LOGGER.info("2、车辆认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、车辆认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_addIdCardIfo(cardaddress, day, idcard, idcarda, idcardb, issuingbody, month, name, nation, sex, validitybegin, validityend, year):
    """
    3、保存身份认证信息
    :param idcardb: 身份证反面(Y),string
    :param month: 出生月份,number
    :param issuingbody: 签发机构,string
    :param cardaddress: 身份证地址(Y),string
    :param day: 出生天,number
    :param sex: 性别,string
    :param idcard: 身份证号(Y),string
    :param nation: 名族,string
    :param name: 姓名(Y),string
    :param year: 出生年份,number
    :param validityend: 有效结束日期,number
    :param idcarda: 身份证正面(Y),string
    :param validitybegin: 有效开始日期,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 706')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/addIdCardIfo"
    LOGGER.info("3、保存身份认证信息请求地址:【{}】".format(requesturl))
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
    LOGGER.info("3、保存身份认证信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、保存身份认证信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_queryFaceResult(biztoken, meglivedata, signversion):
    """
    5、人脸识别结果
    :param biztoken: 通过”App-GetBizToken“ API接口获取到的biz_token,string
    :param signversion: 签名算法版本号,string
    :param meglivedata: 由FaceID MegLiveStill SDK 3.0及以上版本生成的数据（File文件）,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 707')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/queryFaceResult"
    LOGGER.info("5、人脸识别结果请求地址:【{}】".format(requesturl))
    params = dict()
    params["bizToken"] = biztoken
    params["megliveData"] = meglivedata
    params["signVersion"] = signversion
    LOGGER.info("5、人脸识别结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、人脸识别结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_queryIdCardIfo():
    """
    4、查询身份认证信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 708')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/queryIdCardIfo"
    LOGGER.info("4、查询身份认证信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4、查询身份认证信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、查询身份认证信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_queryCarInfo():
    """
    6、车辆认证查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 709')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/queryCarInfo"
    LOGGER.info("6、车辆认证查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("6、车辆认证查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、车辆认证查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_auth_messAuth_addBankCard(bank, cardno, mobile):
    """
    7、银行卡认证
    :param bank: 名称(Y),string
    :param cardno: 银行卡号(Y),string
    :param mobile: 预留手机号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 710')
    requesturl = baseUrl + "/api/78dk/clientapp/auth/messAuth/addBankCard"
    LOGGER.info("7、银行卡认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["bank"] = bank
    params["cardNo"] = cardno
    params["mobile"] = mobile
    LOGGER.info("7、银行卡认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("7、银行卡认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_queryCanLoan():
    """
    1、是否可以借款
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 711')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/queryCanLoan"
    LOGGER.info("1、是否可以借款请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1、是否可以借款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、是否可以借款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_submitApply(applyamount, city, loanterm, loanuse, productdetailuuid):
    """
    3、提交申请
    :param productdetailuuid: 产品uuid(Y),string
    :param loanterm: 借款期限(Y),number
    :param city: 城市code(Y),string
    :param loanuse: 借款用途(Y),string
    :param applyamount: 借款金额(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 712')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/submitApply"
    LOGGER.info("3、提交申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyAmount"] = applyamount
    params["city"] = city
    params["loanTerm"] = loanterm
    params["loanUse"] = loanuse
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("3、提交申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、提交申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_queryApplyState():
    """
    2、审核状态查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 713')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/queryApplyState"
    LOGGER.info("2、审核状态查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("2、审核状态查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、审核状态查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_querySignConResult():
    """
    _16、签约结果查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 714')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/querySignConResult"
    LOGGER.info("_16、签约结果查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_16、签约结果查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_16、签约结果查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_queryLoanPro():
    """
    _17、产品列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 715')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/queryLoanPro"
    LOGGER.info("_17、产品列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_17、产品列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_17、产品列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_queryPeriod(productdetailuuid):
    """
    _18、期数列表
    :param productdetailuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 716')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/queryPeriod"
    LOGGER.info("_18、期数列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("_18、期数列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_18、期数列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_loanApply_querySignUrl():
    """
    _19、获取签约地址
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 717')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/loanApply/querySignUrl"
    LOGGER.info("_19、获取签约地址请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_19、获取签约地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_19、获取签约地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryLoanInfoAll():
    """
    4、借款详情查询（ALL--作废）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 718')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryLoanInfoAll"
    LOGGER.info("4、借款详情查询（ALL--作废）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4、借款详情查询（ALL--作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、借款详情查询（ALL--作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_addLoanInfoAll(perfectinfodto):
    """
    5、借款详情保存（ALL--作废）
    :param perfectinfodto: 请求对象,object
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 719')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/addLoanInfoAll"
    LOGGER.info("5、借款详情保存（ALL--作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["perfectInfoDTO"] = perfectinfodto
    LOGGER.info("5、借款详情保存（ALL--作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、借款详情保存（ALL--作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_querySelfInfo():
    """
    6、个人信息查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 720')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/querySelfInfo"
    LOGGER.info("6、个人信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("6、个人信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、个人信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_updateSelfInfo(address, education, housenature, idcard, marriage, name, province, region, spouseidcard, spousename):
    """
    7、完善个人信息
    :param province: 省(Y 字典编码),string
    :param housenature: 住房性质(Y),string
    :param address: 详细地址(Y),string
    :param marriage: 婚姻状况(Y),string
    :param idcard: 身份证号码（Y）,string
    :param spouseidcard: 配偶身份证(已婚必填),string
    :param name: 姓名(Y 字典编码),string
    :param spousename: 配偶姓名(已婚必填),string
    :param education: 学历（Y）,string
    :param region: 县(Y 字典编码),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 721')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/updateSelfInfo"
    LOGGER.info("7、完善个人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["education"] = education
    params["houseNature"] = housenature
    params["idcard"] = idcard
    params["marriage"] = marriage
    params["name"] = name
    params["province"] = province
    params["region"] = region
    params["spouseIdcard"] = spouseidcard
    params["spouseName"] = spousename
    LOGGER.info("7、完善个人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("7、完善个人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryLoanInfo():
    """
    8、借款信息查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 722')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryLoanInfo"
    LOGGER.info("8、借款信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("8、借款信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("8、借款信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_updateLoanInfo(applyamount, city, cityname, loanterm, loanuse, payment, productdetailuuid, replaytype, storename, storeuuid):
    """
    9、借款信息修改
    :param loanterm: 借款期限(Y),number
    :param storename: 申请门店,string
    :param applyamount: 借款金额(Y),number
    :param loanuse: 借款用途(Y),string
    :param payment: 还款来源,string
    :param replaytype: 申请还款方式,string
    :param productdetailuuid: 还款方式uuid,string
    :param storeuuid: 门店uuid,string
    :param cityname: 城市名称,string
    :param city: 城市id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 723')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/updateLoanInfo"
    LOGGER.info("9、借款信息修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyAmount"] = applyamount
    params["city"] = city
    params["cityName"] = cityname
    params["loanTerm"] = loanterm
    params["loanUse"] = loanuse
    params["payment"] = payment
    params["productDetailUuid"] = productdetailuuid
    params["replayType"] = replaytype
    params["storeName"] = storename
    params["storeUuid"] = storeuuid
    LOGGER.info("9、借款信息修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("9、借款信息修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryWorkInfo():
    """
    _10、职业信息查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 724')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryWorkInfo"
    LOGGER.info("_10、职业信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_10、职业信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_10、职业信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_addUpWorkInfo(address, city, clientworkuuid, name, position, province, region, workage, worknature):
    """
    _11、职业信息保存或修改
    :param city: 市/区编码(Y),string
    :param name: 单位名称(Y),string
    :param worknature: 工作性质(Y),string
    :param position: 职务(Y),string
    :param workage: 工作年限,string
    :param clientworkuuid: 用户单位uuid-为空时为保存(N),string
    :param address: 单位地址(Y),string
    :param province: 省编码(Y),string
    :param region: 县编码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 725')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/addUpWorkInfo"
    LOGGER.info("_11、职业信息保存或修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["city"] = city
    params["clientWorkUuid"] = clientworkuuid
    params["name"] = name
    params["position"] = position
    params["province"] = province
    params["region"] = region
    params["workAge"] = workage
    params["workNature"] = worknature
    LOGGER.info("_11、职业信息保存或修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_11、职业信息保存或修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryContractList():
    """
    _12、联系人信息查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 726')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryContractList"
    LOGGER.info("_12、联系人信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_12、联系人信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_12、联系人信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_addContracts(paramlist):
    """
    _13、联系人信息保存
    :param paramlist: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 727')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/addContracts"
    LOGGER.info("_13、联系人信息保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramList"] = paramlist
    LOGGER.info("_13、联系人信息保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_13、联系人信息保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_addLoanFile(paramlist):
    """
    _14、借款资料保存
    :param paramlist: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 728')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/addLoanFile"
    LOGGER.info("_14、借款资料保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramList"] = paramlist
    LOGGER.info("_14、借款资料保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_14、借款资料保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryLoanFile():
    """
    _15、借款资料查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 729')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryLoanFile"
    LOGGER.info("_15、借款资料查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_15、借款资料查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_15、借款资料查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_infoSure():
    """
    _16、完善信息确认
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 730')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/infoSure"
    LOGGER.info("_16、完善信息确认请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("_16、完善信息确认请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("_16、完善信息确认请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_city_queryCityList():
    """
    1、城市列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 731')
    requesturl = baseUrl + "/api/78dk/clientapp/common/city/queryCityList"
    LOGGER.info("1、城市列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1、城市列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、城市列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_car_queryCarTypeList(brandname):
    """
    1、车辆品牌列表
    :param brandname: 品牌名称(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 732')
    requesturl = baseUrl + "/api/78dk/clientapp/common/car/queryCarTypeList"
    LOGGER.info("1、车辆品牌列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["brandName"] = brandname
    LOGGER.info("1、车辆品牌列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、车辆品牌列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_car_queryCarModelList(brandid):
    """
    2、车系列表
    :param brandid: 车辆品牌id(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 733')
    requesturl = baseUrl + "/api/78dk/clientapp/common/car/queryCarModelList"
    LOGGER.info("2、车系列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["brandId"] = brandid
    LOGGER.info("2、车系列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、车系列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_car_queryCarlList(seriesid):
    """
    3、车辆列表
    :param seriesid: 车系id(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 734')
    requesturl = baseUrl + "/api/78dk/clientapp/common/car/queryCarlList"
    LOGGER.info("3、车辆列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["seriesId"] = seriesid
    LOGGER.info("3、车辆列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、车辆列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_gps_addGpsInfo(address, city, lat, lng, province, region):
    """
    1、GPS数据上传
    :param province: 省,string
    :param address: 解析地址,string
    :param lng: 经度,string
    :param city: 市/区,string
    :param lat: 纬度,string
    :param region: 县,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 735')
    requesturl = baseUrl + "/api/78dk/clientapp/common/gps/addGpsInfo"
    LOGGER.info("1、GPS数据上传请求地址:【{}】".format(requesturl))
    params = dict()
    params["address"] = address
    params["city"] = city
    params["lat"] = lat
    params["lng"] = lng
    params["province"] = province
    params["region"] = region
    LOGGER.info("1、GPS数据上传请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、GPS数据上传请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_dict_queryDictList(dicttypecode):
    """
    1、下拉字典列表
    :param dicttypecode: 字典类型编码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 736')
    requesturl = baseUrl + "/api/78dk/clientapp/common/dict/queryDictList"
    LOGGER.info("1、下拉字典列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictTypeCode"] = dicttypecode
    LOGGER.info("1、下拉字典列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、下拉字典列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_dict_queryProductList():
    """
    2、获取产品及期数列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 737')
    requesturl = baseUrl + "/api/78dk/clientapp/common/dict/queryProductList"
    LOGGER.info("2、获取产品及期数列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("2、获取产品及期数列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、获取产品及期数列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sms_sendValidate(mobile, type):
    """
    1、短信验证码
    :param type: 类型（Y 1-注册 2-短信登陆 3-重置密码）,string
    :param mobile: 手机号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 738')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sms/sendValidate"
    LOGGER.info("1、短信验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["type"] = type
    LOGGER.info("1、短信验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、短信验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sms_sendCodeVer(mobile, picvercode, type, verid):
    """
    2、短信验证码（需校验）
    :param type: 类型（Y 1-注册 2-短信登陆 3-重置密码）,string
    :param picvercode: 验证码code,string
    :param mobile: 手机号,string
    :param verid: 验证码id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 739')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sms/sendCodeVer"
    LOGGER.info("2、短信验证码（需校验）请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["picVerCode"] = picvercode
    params["type"] = type
    params["verId"] = verid
    LOGGER.info("2、短信验证码（需校验）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、短信验证码（需校验）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_qiniu_queryQiNiuToken():
    """
    1、七牛云上传token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 740')
    requesturl = baseUrl + "/api/78dk/clientapp/common/qiniu/queryQiNiuToken"
    LOGGER.info("1、七牛云上传token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1、七牛云上传token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、七牛云上传token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_picCode_getPicVerCode():
    """
    获取图形验证码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 741')
    requesturl = baseUrl + "/api/78dk/clientapp/common/picCode/getPicVerCode"
    LOGGER.info("获取图形验证码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取图形验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图形验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sys_versionUp():
    """
    2、版本升级（普通）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 742')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sys/versionUp"
    LOGGER.info("2、版本升级（普通）请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("2、版本升级（普通）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、版本升级（普通）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sys_iosOnline():
    """
    3、ios上架标识
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 743')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sys/iosOnline"
    LOGGER.info("3、ios上架标识请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("3、ios上架标识请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、ios上架标识请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sys_androidIsOnline():
    """
    4、andriod上架标识
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 744')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sys/androidIsOnline"
    LOGGER.info("4、andriod上架标识请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4、andriod上架标识请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、andriod上架标识请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_sys_getVersionMess():
    """
    5、版本信息获取
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 745')
    requesturl = baseUrl + "/api/78dk/clientapp/common/sys/getVersionMess"
    LOGGER.info("5、版本信息获取请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("5、版本信息获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、版本信息获取请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_userInfo_queryUserInfo():
    """
    1、个人综合信息查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 746')
    requesturl = baseUrl + "/api/78dk/clientapp/common/userInfo/queryUserInfo"
    LOGGER.info("1、个人综合信息查询请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("1、个人综合信息查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、个人综合信息查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_userInfo_queryUserAgreement():
    """
    2、借款协议
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 747')
    requesturl = baseUrl + "/api/78dk/clientapp/common/userInfo/queryUserAgreement"
    LOGGER.info("2、借款协议请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("2、借款协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、借款协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_userInfo_uploadAddressBook(addressbookjson):
    """
    3、上传通讯录
    :param addressbookjson: 通讯录json字符串,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 748')
    requesturl = baseUrl + "/api/78dk/clientapp/common/userInfo/uploadAddressBook"
    LOGGER.info("3、上传通讯录请求地址:【{}】".format(requesturl))
    params = dict()
    params["addressBookJson"] = addressbookjson
    LOGGER.info("3、上传通讯录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、上传通讯录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_homePage_banner_queryBannerList():
    """
    查询首页banner图列表(暂未使用)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 749')
    requesturl = baseUrl + "/api/78dk/clientapp/homePage/banner/queryBannerList"
    LOGGER.info("查询首页banner图列表(暂未使用)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询首页banner图列表(暂未使用)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询首页banner图列表(暂未使用)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_homePage_homeOrder_queryOrderState():
    """
    订单状态
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 750')
    requesturl = baseUrl + "/api/78dk/clientapp/homePage/homeOrder/queryOrderState"
    LOGGER.info("订单状态请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("订单状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_upsetFingerCode(fingercode):
    """
    1、新增/修改指纹密码
    :param fingercode: 指纹code(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 751')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/upsetFingerCode"
    LOGGER.info("1、新增/修改指纹密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["fingerCode"] = fingercode
    LOGGER.info("1、新增/修改指纹密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("1、新增/修改指纹密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_upsetGestureCode(gesturecode):
    """
    2、新增/修改手势密码
    :param gesturecode: 手势码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 752')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/upsetGestureCode"
    LOGGER.info("2、新增/修改手势密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["gestureCode"] = gesturecode
    LOGGER.info("2、新增/修改手势密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("2、新增/修改手势密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_delFingerCode():
    """
    3、删除指纹密码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 753')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/delFingerCode"
    LOGGER.info("3、删除指纹密码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("3、删除指纹密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3、删除指纹密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_delGestureCode():
    """
    4、删除手势密码
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 754')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/delGestureCode"
    LOGGER.info("4、删除手势密码请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4、删除手势密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4、删除手势密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_fingerCodeLogin(fingercode, mobile):
    """
    5、指纹登录
    :param fingercode: 指纹code(Y),string
    :param mobile: 登录手机号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 755')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/fingerCodeLogin"
    LOGGER.info("5、指纹登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["fingerCode"] = fingercode
    params["mobile"] = mobile
    LOGGER.info("5、指纹登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("5、指纹登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_fingerGesture_gestureCodeLogin(gesturecode, mobile):
    """
    6、手势登录
    :param mobile: 登录手机号(Y),string
    :param gesturecode: 手势code(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 756')
    requesturl = baseUrl + "/api/78dk/clientapp/fingerGesture/gestureCodeLogin"
    LOGGER.info("6、手势登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["gestureCode"] = gesturecode
    params["mobile"] = mobile
    LOGGER.info("6、手势登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("6、手势登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_product_productdetail_queryRepaymentMehodList():
    """
    3，查询回款方式列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1558')
    requesturl = baseUrl + "/api/78dk/clientapp/product/productdetail/queryRepaymentMehodList"
    LOGGER.info("3，查询回款方式列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("3，查询回款方式列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("3，查询回款方式列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_common_userInfo_getInviteUrl():
    """
    获得个人邀请地址
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1574')
    requesturl = baseUrl + "/api/78dk/clientapp/common/userInfo/getInviteUrl"
    LOGGER.info("获得个人邀请地址请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获得个人邀请地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获得个人邀请地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryCityAndIndex(city):
    """
    17、城市、门店以及城市索引查询
    :param city: 城市名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1596')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryCityAndIndex"
    LOGGER.info("17、城市、门店以及城市索引查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    LOGGER.info("17、城市、门店以及城市索引查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("17、城市、门店以及城市索引查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryStoreInfoByCityCode(id):
    """
    18、根据城市ID查询门店
    :param id: 城市编码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1597')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryStoreInfoByCityCode"
    LOGGER.info("18、根据城市ID查询门店请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("18、根据城市ID查询门店请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("18、根据城市ID查询门店请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_tools_carEva_vehicleInformation():
    """
    4，填写资料_车辆评估数据
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1599')
    requesturl = baseUrl + "/api/78dk/clientapp/tools/carEva/vehicleInformation"
    LOGGER.info("4，填写资料_车辆评估数据请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("4，填写资料_车辆评估数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("4，填写资料_车辆评估数据请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_clientapp_loan_perfectInfo_queryreplayType(repaymentmethod):
    """
    19、申请还款方式查询
    :param repaymentmethod: 回款方式,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1603')
    requesturl = baseUrl + "/api/78dk/clientapp/loan/perfectInfo/queryreplayType"
    LOGGER.info("19、申请还款方式查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["repaymentMethod"] = repaymentmethod
    LOGGER.info("19、申请还款方式查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("19、申请还款方式查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


