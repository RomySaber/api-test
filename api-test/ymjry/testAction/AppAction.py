#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppAction.py
@desc       : 项目：ymjry 模块：app 接口方法封装
"""

from ymjry.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('app_apiURL', 'ymjry')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_app_login()
API_TEST_HEADERS['authorization'] = LICENCES


def test_api_78dk_app_process_getStoreAndProduct(isdiscount, storeuuid):
    """
    查询门店及商品-1.0.2有调整
    :param isdiscount: 是否贴息(Y),boolean
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2480')
    requesturl = baseUrl + "/api/78dk/app/process/getStoreAndProduct"
    LOGGER.info("查询门店及商品-1.0.2有调整请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["storeUuid"] = storeuuid
    LOGGER.info("查询门店及商品-1.0.2有调整请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店及商品-1.0.2有调整请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getCodeUrl():
    """
    获取商户二维码前缀
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2481')
    requesturl = baseUrl + "/api/78dk/app/process/getCodeUrl"
    LOGGER.info("获取商户二维码前缀请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取商户二维码前缀请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取商户二维码前缀请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getProductDetail(productdetailuuid):
    """
    根据产品uuid查询分期详情
    :param productdetailuuid: 产品Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2482')
    requesturl = baseUrl + "/api/78dk/app/process/getProductDetail"
    LOGGER.info("根据产品uuid查询分期详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["productDetailUuid"] = productdetailuuid
    LOGGER.info("根据产品uuid查询分期详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据产品uuid查询分期详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_loanCalculatorV2(isdiscount, loanamount, productdetailuuid, storeuuid):
    """
    贷款试算
    :param isdiscount: 是否贴息(Y),boolean
    :param productdetailuuid: 产品Uuid(Y),string
    :param loanamount: 申请金额(Y),number
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2483')
    requesturl = baseUrl + "/api/78dk/app/process/loanCalculatorV2"
    LOGGER.info("贷款试算请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["loanAmount"] = loanamount
    params["productDetailUuid"] = productdetailuuid
    params["storeUuid"] = storeuuid
    LOGGER.info("贷款试算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款试算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_createContract(isdiscount, loanamount, placeordergpsuuid, productdetailconfiguuid, productdetailuuid, projectname, sauuid, selectrepaydiscount, storeuuid):
    """
    下一步-创建订单-1.0.2有调整
    :param placeordergpsuuid: 定位信息UUID(N),string
    :param selectrepaydiscount: 是否选择还款优惠包（1.0.2新增）,string
    :param productdetailuuid: 产品Uuid(Y),string
    :param isdiscount: 是否贴息(Y),boolean
    :param loanamount: 分期金额(Y),number
    :param productdetailconfiguuid: 期数Uuid(Y),string
    :param storeuuid: 门店Uuid(Y),string
    :param sauuid: SA线下业务员,string
    :param projectname: 项目名称（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2484')
    requesturl = baseUrl + "/api/78dk/app/process/createContract"
    LOGGER.info("下一步-创建订单-1.0.2有调整请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["loanAmount"] = loanamount
    params["placeOrderGpsUuid"] = placeordergpsuuid
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["productDetailUuid"] = productdetailuuid
    params["projectName"] = projectname
    params["saUuid"] = sauuid
    params["selectRepayDiscount"] = selectrepaydiscount
    params["storeUuid"] = storeuuid
    LOGGER.info("下一步-创建订单-1.0.2有调整请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下一步-创建订单-1.0.2有调整请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress, gpscity, gpsdetail, gpsinfolat, gpsinfolon, gpsprovince, gpsregion):
    """
    保存位置信息
    :param gpsregion: gps解析信息-县(N),string
    :param gpsinfolat: gps维度(Y),string
    :param gpsprovince: gps解析信息-省(N),string
    :param gpsaddress: gps解析完整地址(Y),string
    :param gpsinfolon: gps经度(Y),string
    :param gpscity: gps解析信息-市(N),string
    :param gpsdetail: gps解析信息-详细地址(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2485')
    requesturl = baseUrl + "/api/78dk/app/process/saveUserPlaceOrderGps"
    LOGGER.info("保存位置信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsAddress"] = gpsaddress
    params["gpsCity"] = gpscity
    params["gpsDetail"] = gpsdetail
    params["gpsInfoLat"] = gpsinfolat
    params["gpsInfoLon"] = gpsinfolon
    params["gpsProvince"] = gpsprovince
    params["gpsRegion"] = gpsregion
    LOGGER.info("保存位置信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存位置信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveOrcInfo(authenticationstate, firstkey, note, secondkey, thirdkey):
    """
    保存人脸识别结果
    :param firstkey: 第一张图片key(Y),string
    :param thirdkey: 第三张图片key(Y),string
    :param secondkey: 第二张图片key(Y),string
    :param note: faceID返回结果(Y),string
    :param authenticationstate: 识别状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2486')
    requesturl = baseUrl + "/api/78dk/app/process/saveOrcInfo"
    LOGGER.info("保存人脸识别结果请求地址:【{}】".format(requesturl))
    params = dict()
    params["authenticationState"] = authenticationstate
    params["firstKey"] = firstkey
    params["note"] = note
    params["secondKey"] = secondkey
    params["thirdKey"] = thirdkey
    LOGGER.info("保存人脸识别结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存人脸识别结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveIdCardInfo(cardscanidcardno, cardscanname, frontkey, frontnote, oppositekey, oppositenote):
    """
    保存身份证信息
    :param oppositenote: 身份证反面照faceID返回结果(Y),string
    :param cardscanname: 名字(Y),string
    :param oppositekey: 身份证反面照key(Y),string
    :param frontkey: 身份证正面照key(Y),string
    :param frontnote: 身份证正面照faceID返回结果(Y),string
    :param cardscanidcardno: 身份证号码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2487')
    requesturl = baseUrl + "/api/78dk/app/process/saveIdCardInfo"
    LOGGER.info("保存身份证信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardScanIdcardNo"] = cardscanidcardno
    params["cardScanName"] = cardscanname
    params["frontKey"] = frontkey
    params["frontNote"] = frontnote
    params["oppositeKey"] = oppositekey
    params["oppositeNote"] = oppositenote
    LOGGER.info("保存身份证信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存身份证信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getNewestIdCardInfo():
    """
    查询身份证信息(最近)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2488')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestIdCardInfo"
    LOGGER.info("查询身份证信息(最近)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询身份证信息(最近)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询身份证信息(最近)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveHoldKey(holdkey):
    """
    保存手持身份证照片
    :param holdkey: 手持照key(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2489')
    requesturl = baseUrl + "/api/78dk/app/process/saveHoldKey"
    LOGGER.info("保存手持身份证照片请求地址:【{}】".format(requesturl))
    params = dict()
    params["holdKey"] = holdkey
    LOGGER.info("保存手持身份证照片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存手持身份证照片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getSupportBanks():
    """
    查询支持银行(弹窗描述)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2490')
    requesturl = baseUrl + "/api/78dk/app/process/getSupportBanks"
    LOGGER.info("查询支持银行(弹窗描述)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询支持银行(弹窗描述)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询支持银行(弹窗描述)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getBankCardInfo():
    """
    查询绑定的银行卡列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2491')
    requesturl = baseUrl + "/api/78dk/app/process/getBankCardInfo"
    LOGGER.info("查询绑定的银行卡列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询绑定的银行卡列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询绑定的银行卡列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveBankCardInfo(bankcardmobile, bankcardno, billemail):
    """
    绑定银行卡1-输入银行卡信息
    :param bankcardmobile: 银行卡预留手机号(Y),string
    :param billemail: 账单邮箱(N),string
    :param bankcardno: 银行卡号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2492')
    requesturl = baseUrl + "/api/78dk/app/process/saveBankCardInfo"
    LOGGER.info("绑定银行卡1-输入银行卡信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankCardMobile"] = bankcardmobile
    params["bankCardNo"] = bankcardno
    params["billEmail"] = billemail
    LOGGER.info("绑定银行卡1-输入银行卡信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定银行卡1-输入银行卡信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_choiceBankCard(userbankcarduuid):
    """
    选择还款银行卡
    :param userbankcarduuid: 银行卡Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2493')
    requesturl = baseUrl + "/api/78dk/app/process/choiceBankCard"
    LOGGER.info("选择还款银行卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBankCardUuid"] = userbankcarduuid
    LOGGER.info("选择还款银行卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("选择还款银行卡请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_validBankCardInfo(validcode):
    """
    绑定银行卡2-输入手机验证码
    :param validcode: 手机验证码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2494')
    requesturl = baseUrl + "/api/78dk/app/process/validBankCardInfo"
    LOGGER.info("绑定银行卡2-输入手机验证码请求地址:【{}】".format(requesturl))
    params = dict()
    params["validCode"] = validcode
    LOGGER.info("绑定银行卡2-输入手机验证码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定银行卡2-输入手机验证码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_savePersonInfo(contactlist, datumtypeeducationid, datumtypehousingid, datumtypemarryid, email, iswork, livecity, livecityname, livedetail, liveprovince, liveprovincename, liveregion, liveregionname):
    """
    保存基本信息
    :param livecity: 居住地址-市编码(Y),number
    :param livecityname: 居住地址-市名称(Y),string
    :param contactlist: 联系人信息列表,array<object>
    :param liveregionname: 居住地址-区名称(Y),string
    :param liveprovince: 居住地址-省编码(Y),number
    :param datumtypeeducationid: 学历(Y),number
    :param liveregion: 居住地址-区编码(Y),number
    :param livedetail: 居住地址-详细地址(Y),string
    :param liveprovincename: 居住地址-省名称(Y),string
    :param datumtypemarryid: 婚姻状况(Y),number
    :param datumtypehousingid: 住房类型(Y),number
    :param email: 邮箱(Y ),string
    :param iswork: 是否有工作(Y ),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2495')
    requesturl = baseUrl + "/api/78dk/app/process/savePersonInfo"
    LOGGER.info("保存基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["contactList"] = contactlist
    params["datumTypeEducationId"] = datumtypeeducationid
    params["datumTypeHousingId"] = datumtypehousingid
    params["datumTypeMarryId"] = datumtypemarryid
    params["email"] = email
    params["isWork"] = iswork
    params["liveCity"] = livecity
    params["liveCityName"] = livecityname
    params["liveDetail"] = livedetail
    params["liveProvince"] = liveprovince
    params["liveProvinceName"] = liveprovincename
    params["liveRegion"] = liveregion
    params["liveRegionName"] = liveregionname
    LOGGER.info("保存基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getNewestPersonInfo():
    """
    查询基本信息(最近)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2496')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestPersonInfo"
    LOGGER.info("查询基本信息(最近)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询基本信息(最近)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询基本信息(最近)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_sendVerifyEmail(email):
    """
    发送验证邮件
    :param email: 需要验证的邮件(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2497')
    requesturl = baseUrl + "/api/78dk/app/process/sendVerifyEmail"
    LOGGER.info("发送验证邮件请求地址:【{}】".format(requesturl))
    params = dict()
    params["email"] = email
    LOGGER.info("发送验证邮件请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送验证邮件请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_verifyEmailReturn(code, email):
    """
    邮件认证链接
    :param email: 验证邮箱,string
    :param code: 验证码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2498')
    requesturl = baseUrl + "/api/78dk/app/process/verifyEmailReturn"
    LOGGER.info("邮件认证链接请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["email"] = email
    LOGGER.info("邮件认证链接请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("邮件认证链接请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveWorkInfo(companycity, companycityname, companydetail, companyname, companyprovince, companyprovincename, companyregion, companyregionname, datumtypeincomeid, datumtypeworktimeid, position, propertiesid, scaleid, workphone):
    """
    保存工作信息
    :param companyname: 单位名称(Y),string
    :param companycityname: 单位地址-市名称(Y),string
    :param datumtypeincomeid: 薪资(Y),number
    :param propertiesid: 单位性质(Y),number
    :param scaleid: 单位规模(Y),number
    :param companyregion: 单位地址-县编码(Y),number
    :param companyprovincename: 单位地址-省名称(Y),string
    :param workphone: 工作电话(Y),string
    :param datumtypeworktimeid: 工作时间(Y),number
    :param position: 职位(Y),string
    :param companydetail: 单位地址-详细地址(Y),string
    :param companyregionname: 单位地址-县名称(Y),string
    :param companycity: 单位地址-市编码(Y),number
    :param companyprovince: 单位地址-省编码(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2499')
    requesturl = baseUrl + "/api/78dk/app/process/saveWorkInfo"
    LOGGER.info("保存工作信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyCity"] = companycity
    params["companyCityName"] = companycityname
    params["companyDetail"] = companydetail
    params["companyName"] = companyname
    params["companyProvince"] = companyprovince
    params["companyProvinceName"] = companyprovincename
    params["companyRegion"] = companyregion
    params["companyRegionName"] = companyregionname
    params["datumTypeIncomeId"] = datumtypeincomeid
    params["datumTypeWorktimeId"] = datumtypeworktimeid
    params["position"] = position
    params["propertiesId"] = propertiesid
    params["scaleId"] = scaleid
    params["workPhone"] = workphone
    LOGGER.info("保存工作信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存工作信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getNewestWorkInfo():
    """
    查询工作信息(最近)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2500')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestWorkInfo"
    LOGGER.info("查询工作信息(最近)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询工作信息(最近)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询工作信息(最近)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveUserMailListInfo(content):
    """
    保存用户通讯录信息
    :param content: 通讯录json字符串(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2501')
    requesturl = baseUrl + "/api/78dk/app/process/saveUserMailListInfo"
    LOGGER.info("保存用户通讯录信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["content"] = content
    LOGGER.info("保存用户通讯录信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存用户通讯录信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveCallList(paramlist):
    """
    保存通话详单
    :param paramlist: 请求参数List,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2502')
    requesturl = baseUrl + "/api/78dk/app/process/saveCallList"
    LOGGER.info("保存通话详单请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramList"] = paramlist
    LOGGER.info("保存通话详单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存通话详单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveContractImages(contractimagelist):
    """
    保存影像资料
    :param contractimagelist: 影像资料列表,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2503')
    requesturl = baseUrl + "/api/78dk/app/process/saveContractImages"
    LOGGER.info("保存影像资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractImageList"] = contractimagelist
    LOGGER.info("保存影像资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存影像资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getContractImages():
    """
    查询影像资料(当前订单)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2504')
    requesturl = baseUrl + "/api/78dk/app/process/getContractImages"
    LOGGER.info("查询影像资料(当前订单)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询影像资料(当前订单)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询影像资料(当前订单)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getSpecialInfo():
    """
    查询特别信息认证进度
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2505')
    requesturl = baseUrl + "/api/78dk/app/process/getSpecialInfo"
    LOGGER.info("查询特别信息认证进度请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询特别信息认证进度请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询特别信息认证进度请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_mxCallback(body):
    """
    (回调接口)接口中心-魔蝎
    :param body: 回调内容,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2506')
    requesturl = baseUrl + "/api/78dk/app/process/mxCallback"
    LOGGER.info("(回调接口)接口中心-魔蝎请求地址:【{}】".format(requesturl))
    params = dict()
    params["body"] = body
    LOGGER.info("(回调接口)接口中心-魔蝎请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("(回调接口)接口中心-魔蝎请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveContractSupplementImages(contractuuid, datalist):
    """
    保存补充资料
    :param contractuuid: 合同uuid,string
    :param datalist: 资料列表,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2507')
    requesturl = baseUrl + "/api/78dk/app/process/saveContractSupplementImages"
    LOGGER.info("保存补充资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["dataList"] = datalist
    LOGGER.info("保存补充资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存补充资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_verifySchool(account, password, school, taskid, vcode):
    """
    学信网认证
    :param account: 帐号(Y),string
    :param taskid: taskId(N),string
    :param school: 学校名称(Y),string
    :param vcode: 验证码(Y),string
    :param password: 密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2508')
    requesturl = baseUrl + "/api/78dk/app/process/verifySchool"
    LOGGER.info("学信网认证请求地址:【{}】".format(requesturl))
    params = dict()
    params["account"] = account
    params["password"] = password
    params["school"] = school
    params["taskId"] = taskid
    params["vcode"] = vcode
    LOGGER.info("学信网认证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网认证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getContractSupplementImages(contractuuid):
    """
    查询补充资料
    :param contractuuid: 合同uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2509')
    requesturl = baseUrl + "/api/78dk/app/process/getContractSupplementImages"
    LOGGER.info("查询补充资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询补充资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询补充资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_submitApply(loanamount, productdetailconfiguuid, repaymentdate):
    """
    提交申请
    :param productdetailconfiguuid: 产品分期方案Uuid(N),string
    :param loanamount: 分期金额(N),number
    :param repaymentdate: 自定义还款日,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2510')
    requesturl = baseUrl + "/api/78dk/app/process/submitApply"
    LOGGER.info("提交申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanAmount"] = loanamount
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["repaymentDate"] = repaymentdate
    LOGGER.info("提交申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_repayPlanCalculator(isdiscount, loanamount, productdetailconfiguuid, productdetailuuid, repaymentdate, storeuuid):
    """
    还款计划试算
    :param productdetailuuid: 产品Uuid(Y),string
    :param productdetailconfiguuid: 期数uuid(Y),string
    :param repaymentdate: 自定义还款日（N）,number
    :param loanamount: 申请金额(Y),number
    :param isdiscount: 是否贴息(Y),boolean
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2511')
    requesturl = baseUrl + "/api/78dk/app/process/repayPlanCalculator"
    LOGGER.info("还款计划试算请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["loanAmount"] = loanamount
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["productDetailUuid"] = productdetailuuid
    params["repaymentDate"] = repaymentdate
    params["storeUuid"] = storeuuid
    LOGGER.info("还款计划试算请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款计划试算请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getSignResult():
    """
    查询法大大签约结果
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2512')
    requesturl = baseUrl + "/api/78dk/app/process/getSignResult"
    LOGGER.info("查询法大大签约结果请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询法大大签约结果请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询法大大签约结果请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getSignUrl():
    """
    获取法大大签约地址
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2513')
    requesturl = baseUrl + "/api/78dk/app/process/getSignUrl"
    LOGGER.info("获取法大大签约地址请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取法大大签约地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取法大大签约地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_queryQiNiuToken():
    """
    获取七牛上传token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2514')
    requesturl = baseUrl + "/api/78dk/app/common/queryQiNiuToken"
    LOGGER.info("获取七牛上传token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取七牛上传token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛上传token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_queryQiNiuTokenVideo():
    """
    获取七牛视频上传token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2515')
    requesturl = baseUrl + "/api/78dk/app/common/queryQiNiuTokenVideo"
    LOGGER.info("获取七牛视频上传token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取七牛视频上传token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛视频上传token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getCites(parent):
    """
    获取城市列表
    :param parent: 父级地区编码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2516')
    requesturl = baseUrl + "/api/78dk/app/common/getCites"
    LOGGER.info("获取城市列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["parent"] = parent
    LOGGER.info("获取城市列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取城市列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getDictionaries(datumtype):
    """
    获取字典列表
    :param datumtype: 类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2517')
    requesturl = baseUrl + "/api/78dk/app/common/getDictionaries"
    LOGGER.info("获取字典列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["datumType"] = datumtype
    LOGGER.info("获取字典列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取字典列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getAllCites():
    """
    获取所有城市列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2518')
    requesturl = baseUrl + "/api/78dk/app/common/getAllCites"
    LOGGER.info("获取所有城市列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取所有城市列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有城市列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getVersionInfo(channelno, currentversnumb, platform):
    """
    获取版本信息
    :param platform: 平台(Y),number
    :param channelno: 应用平台渠道号(Y),string
    :param currentversnumb: APP当前版本号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2519')
    requesturl = baseUrl + "/api/78dk/app/common/getVersionInfo"
    LOGGER.info("获取版本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["channelNo"] = channelno
    params["currentVersNumb"] = currentversnumb
    params["platform"] = platform
    LOGGER.info("获取版本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取版本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getAppReview(platform):
    """
    获取app审核环境
    :param platform: APP类型,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2520')
    requesturl = baseUrl + "/api/78dk/app/common/getAppReview"
    LOGGER.info("获取app审核环境请求地址:【{}】".format(requesturl))
    params = dict()
    params["platform"] = platform
    LOGGER.info("获取app审核环境请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取app审核环境请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_Header(authorization):
    """
    用户token
    :param authorization: 用户token,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2521')
    requesturl = baseUrl + "/Header"
    LOGGER.info("用户token请求地址:【{}】".format(requesturl))
    params = dict()
    params["Authorization"] = authorization
    LOGGER.info("用户token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户token请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_userInfo():
    """
    用户信息
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2522')
    requesturl = baseUrl + "/api/78dk/app/common/userInfo"
    LOGGER.info("用户信息请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户信息请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_getDomainName():
    """
    获取项目域名
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2523')
    requesturl = baseUrl + "/api/78dk/app/common/getDomainName"
    LOGGER.info("获取项目域名请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取项目域名请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取项目域名请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_idCardInit():
    """
    初始化(获取身份认证)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2524')
    requesturl = baseUrl + "/api/78dk/app/common/idCardInit"
    LOGGER.info("初始化(获取身份认证)请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("初始化(获取身份认证)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("初始化(获取身份认证)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_renounceApplication(loanorderuuid):
    """
    放弃申请
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2525')
    requesturl = baseUrl + "/api/78dk/app/perCenter/renounceApplication"
    LOGGER.info("放弃申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("放弃申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("放弃申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_loanData(loanorderuuid):
    """
    贷款资料
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2526')
    requesturl = baseUrl + "/api/78dk/app/perCenter/loanData"
    LOGGER.info("贷款资料请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("贷款资料请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("贷款资料请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_repaymentFormLists(pagecurrent, pagesize, paraminfo):
    """
    还款计划列表
    :param pagesize: 每页条数(Y),number
    :param paraminfo: 订单UUID（Y）,string
    :param pagecurrent: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2527')
    requesturl = baseUrl + "/api/78dk/app/perCenter/repaymentFormLists"
    LOGGER.info("还款计划列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    params["paramInfo"] = paraminfo
    LOGGER.info("还款计划列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款计划列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_loanDatail(loanorderuuid):
    """
    申请详情
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2528')
    requesturl = baseUrl + "/api/78dk/app/perCenter/loanDatail"
    LOGGER.info("申请详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("申请详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_loanAgreement(loanorderuuid):
    """
    查看贷款协议
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2529')
    requesturl = baseUrl + "/api/78dk/app/perCenter/loanAgreement"
    LOGGER.info("查看贷款协议请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("查看贷款协议请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看贷款协议请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_viewByStagesLists(pagecurrent, pagesize):
    """
    分期列表
    :param pagesize: 每页条数(Y),number
    :param pagecurrent: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2530')
    requesturl = baseUrl + "/api/78dk/app/perCenter/viewByStagesLists"
    LOGGER.info("分期列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("分期列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分期列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_takeGoods(contractuuid):
    """
    确认收货
    :param contractuuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2531')
    requesturl = baseUrl + "/api/78dk/app/perCenter/takeGoods"
    LOGGER.info("确认收货请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("确认收货请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认收货请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_getTakeGoodsContent(contractuuid):
    """
    获取确认收货协议参数
    :param contractuuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2532')
    requesturl = baseUrl + "/api/78dk/app/perCenter/getTakeGoodsContent"
    LOGGER.info("获取确认收货协议参数请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("获取确认收货协议参数请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取确认收货协议参数请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_updatePw(password, vercode):
    """
    修改登录密码
    :param vercode: 验证码（Y）,number
    :param password: 新密码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2533')
    requesturl = baseUrl + "/api/78dk/app/login/updatePw"
    LOGGER.info("修改登录密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["verCode"] = vercode
    LOGGER.info("修改登录密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改登录密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_updateMobileSms(mobile, vercode):
    """
    更改手机号(可接受短信)
    :param vercode: 验证码（新手机号）（Y）,number
    :param mobile: 新手机号码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2534')
    requesturl = baseUrl + "/api/78dk/app/login/updateMobileSms"
    LOGGER.info("更改手机号(可接受短信)请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("更改手机号(可接受短信)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更改手机号(可接受短信)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_updateMobile(idcard, mobile, vercode):
    """
    更改手机号(无法接受短信)
    :param mobile: 新手机号（Y）,string
    :param vercode: 验证码（新手机号）（Y）,number
    :param idcard: 身份证号码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2535')
    requesturl = baseUrl + "/api/78dk/app/login/updateMobile"
    LOGGER.info("更改手机号(无法接受短信)请求地址:【{}】".format(requesturl))
    params = dict()
    params["idCard"] = idcard
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("更改手机号(无法接受短信)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("更改手机号(无法接受短信)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_getBillPage(pagecurrent, pagesize):
    """
    全部账单-分页查询
    :param pagesize: 页面大小(Y),number
    :param pagecurrent: 当前页(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2536')
    requesturl = baseUrl + "/api/78dk/app/bill/getBillPage"
    LOGGER.info("全部账单-分页查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("全部账单-分页查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全部账单-分页查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_getMyBill(billdate, contractuuid):
    """
    我的账单v1.1.0
    :param contractuuid: 合同uuid,string
    :param billdate: 账单时间(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2537')
    requesturl = baseUrl + "/api/78dk/app/bill/getMyBill"
    LOGGER.info("我的账单v1.1.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["billDate"] = billdate
    params["contractUuid"] = contractuuid
    LOGGER.info("我的账单v1.1.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的账单v1.1.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_getBillDetail(userbilluuid):
    """
    账单明细--v1.1.0
    :param userbilluuid: 账单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2538')
    requesturl = baseUrl + "/api/78dk/app/bill/getBillDetail"
    LOGGER.info("账单明细--v1.1.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("账单明细--v1.1.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单明细--v1.1.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_immediateRepayment(userbankcarduuid, userbilluuid):
    """
    立刻还款
    :param userbankcarduuid: 银行卡信息UUID,string
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2539')
    requesturl = baseUrl + "/api/78dk/app/bill/immediateRepayment"
    LOGGER.info("立刻还款请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBankCardUuid"] = userbankcarduuid
    params["userBillUuid"] = userbilluuid
    LOGGER.info("立刻还款请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("立刻还款请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_paymentStatus(contractuuid):
    """
    还款状态（作废，合并到我的账单接口中去了）
    :param contractuuid: 合同Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2540')
    requesturl = baseUrl + "/api/78dk/app/bill/paymentStatus"
    LOGGER.info("还款状态（作废，合并到我的账单接口中去了）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("还款状态（作废，合并到我的账单接口中去了）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款状态（作废，合并到我的账单接口中去了）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_repaymentDetail(userbilluuid):
    """
    查询还款信息
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2541')
    requesturl = baseUrl + "/api/78dk/app/bill/repaymentDetail"
    LOGGER.info("查询还款信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("查询还款信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询还款信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_retrievePw(mobile, vercode):
    """
    忘记密码
    :param vercode: 验证码（Y）,number
    :param mobile: 手机号码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2542')
    requesturl = baseUrl + "/api/78dk/app/login/retrievePw"
    LOGGER.info("忘记密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("忘记密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("忘记密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_newPw(mobile, password):
    """
    忘记密码(设置新密码)
    :param mobile: 手机号（Y）,string
    :param password: 新密码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2543')
    requesturl = baseUrl + "/api/78dk/app/login/newPw"
    LOGGER.info("忘记密码(设置新密码)请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["password"] = password
    LOGGER.info("忘记密码(设置新密码)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("忘记密码(设置新密码)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_register(appversion, ipaddress, mobile, mobilename, mobilenetwork, mobilesystem, mobileuuid, mobileversion, password, registersource, vercode):
    """
    注册
    :param mobilename: 注册时手机名字（N）,string
    :param mobileversion: 注册时手机版本号（N）,string
    :param vercode: 验证码（Y）,string
    :param mobilenetwork: 注册是手机网络（N）,string
    :param mobile: 手机号（Y）,string
    :param mobilesystem: 手机系统（N）,string
    :param mobileuuid: 手机唯一标识UUID（Y）,string
    :param password: 密码（Y）,string
    :param appversion: 注册时APP版本号（N）,string
    :param registersource: 注册来源（N）,string
    :param ipaddress: 注册时IP地址（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2544')
    requesturl = baseUrl + "/api/78dk/app/login/register"
    LOGGER.info("注册请求地址:【{}】".format(requesturl))
    params = dict()
    params["appVersion"] = appversion
    params["ipAddress"] = ipaddress
    params["mobile"] = mobile
    params["mobileName"] = mobilename
    params["mobileNetwork"] = mobilenetwork
    params["mobileSystem"] = mobilesystem
    params["mobileUuid"] = mobileuuid
    params["mobileVersion"] = mobileversion
    params["password"] = password
    params["registerSource"] = registersource
    params["verCode"] = vercode
    LOGGER.info("注册请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("注册请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_loginOut():
    """
    登出
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2545')
    requesturl = baseUrl + "/api/78dk/app/login/loginOut"
    LOGGER.info("登出请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("登出请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登出请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_pwLogin(jgpushid, mobile, password):
    """
    登录(密码)
    :param password: 密码（Y）,string
    :param mobile: 手机号（Y）,string
    :param jgpushid: 极光id编号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2546')
    requesturl = baseUrl + "/api/78dk/app/login/pwLogin"
    LOGGER.info("登录(密码)请求地址:【{}】".format(requesturl))
    params = dict()
    params["jgPushId"] = jgpushid
    params["mobile"] = mobile
    params["password"] = password
    LOGGER.info("登录(密码)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录(密码)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_login_smsLogin(jgpushid, mobile, vercode):
    """
    登录(短信)
    :param jgpushid: 极光id编号（Y）,string
    :param vercode: 验证码（Y）,number
    :param mobile: 手机号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2547')
    requesturl = baseUrl + "/api/78dk/app/login/smsLogin"
    LOGGER.info("登录(短信)请求地址:【{}】".format(requesturl))
    params = dict()
    params["jgPushId"] = jgpushid
    params["mobile"] = mobile
    params["verCode"] = vercode
    LOGGER.info("登录(短信)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录(短信)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_common_sms_sendValidate(mobile, type):
    """
    发送短信
    :param mobile: 手机号码（Y）,string
    :param type: 类型（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2548')
    requesturl = baseUrl + "/api/78dk/app/common/sms/sendValidate"
    LOGGER.info("发送短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["mobile"] = mobile
    params["type"] = type
    LOGGER.info("发送短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_deferredPayment(userbilluuid):
    """
    延期还款v1.0.2新增
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2562')
    requesturl = baseUrl + "/api/78dk/app/bill/deferredPayment"
    LOGGER.info("延期还款v1.0.2新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("延期还款v1.0.2新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("延期还款v1.0.2新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_querySaList():
    """
    获取所有SA在职人员v1.0.3新增
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2577')
    requesturl = baseUrl + "/api/78dk/app/process/querySaList"
    LOGGER.info("获取所有SA在职人员v1.0.3新增请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取所有SA在职人员v1.0.3新增请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有SA在职人员v1.0.3新增请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_repayBillOnline(billuuid, money, type):
    """
    线上还款(目前只支持连连主动支付)
    :param billuuid: 账单uuid,string
    :param money: 要还款的金额，可不传，如果不传金额为账单剩余未还金额,number
    :param type: 支付类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3193')
    requesturl = baseUrl + "/api/78dk/app/bill/repayBillOnline"
    LOGGER.info("线上还款(目前只支持连连主动支付)请求地址:【{}】".format(requesturl))
    params = dict()
    params["billUuid"] = billuuid
    params["money"] = money
    params["type"] = type
    LOGGER.info("线上还款(目前只支持连连主动支付)请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线上还款(目前只支持连连主动支付)请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


