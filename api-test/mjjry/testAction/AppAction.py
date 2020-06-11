#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppAction.py
@desc       : 项目：mjjry 模块：app 接口方法封装
"""

from mjjry.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('app_apiURL', 'mjjry')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_app_login()
API_TEST_HEADERS['authorization'] = LICENCES


def test_api_78dk_app_process_getStoreAndProduct(isdiscount, storeuuid):
    """
    查询门店及商品V1.0.0
    :param storeuuid: 门店Uuid(Y),string
    :param isdiscount: 是否贴息(Y),boolean
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1831')
    requesturl = baseUrl + "/api/78dk/app/process/getStoreAndProduct"
    LOGGER.info("查询门店及商品V1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["storeUuid"] = storeuuid
    LOGGER.info("查询门店及商品V1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店及商品V1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getCodeUrl():
    """
    获取商户二维码前缀V1.4.0
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1832')
    requesturl = baseUrl + "/api/78dk/app/process/getCodeUrl"
    LOGGER.info("获取商户二维码前缀V1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取商户二维码前缀V1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取商户二维码前缀V1.4.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1833')
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
    :param productdetailuuid: 产品Uuid(Y),string
    :param isdiscount: 是否贴息(Y),boolean
    :param loanamount: 申请金额(Y),number
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1834')
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


def test_api_78dk_app_process_createContract(isdiscount, loanamount, placeordergpsuuid, productdetailconfiguuid, productdetailuuid, projectname, sauuid, storeuuid):
    """
    下一步-创建订单V1.4.0（美佳1.0.0）v1.0.4
    :param placeordergpsuuid: 定位信息UUID(N),string
    :param productdetailuuid: 产品Uuid(Y),string
    :param isdiscount: 是否贴息(Y),boolean
    :param loanamount: 分期金额(Y),number
    :param projectname: 项目名称（Y）,string
    :param sauuid: SA线下业务员,string
    :param productdetailconfiguuid: 期数Uuid(Y),string
    :param storeuuid: 门店Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1835')
    requesturl = baseUrl + "/api/78dk/app/process/createContract"
    LOGGER.info("下一步-创建订单V1.4.0（美佳1.0.0）v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["isDiscount"] = isdiscount
    params["loanAmount"] = loanamount
    params["placeOrderGpsUuid"] = placeordergpsuuid
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["productDetailUuid"] = productdetailuuid
    params["projectName"] = projectname
    params["saUuid"] = sauuid
    params["storeUuid"] = storeuuid
    LOGGER.info("下一步-创建订单V1.4.0（美佳1.0.0）v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下一步-创建订单V1.4.0（美佳1.0.0）v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress, gpscity, gpsdetail, gpsinfolat, gpsinfolon, gpsprovince, gpsregion):
    """
    保存位置信息V1.4.0
    :param gpsinfolat: gps维度(Y),string
    :param gpsprovince: gps解析信息-省(N),string
    :param gpsregion: gps解析信息-县(N),string
    :param gpsdetail: gps解析信息-详细地址(N),string
    :param gpscity: gps解析信息-市(N),string
    :param gpsinfolon: gps经度(Y),string
    :param gpsaddress: gps解析完整地址(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1836')
    requesturl = baseUrl + "/api/78dk/app/process/saveUserPlaceOrderGps"
    LOGGER.info("保存位置信息V1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["gpsAddress"] = gpsaddress
    params["gpsCity"] = gpscity
    params["gpsDetail"] = gpsdetail
    params["gpsInfoLat"] = gpsinfolat
    params["gpsInfoLon"] = gpsinfolon
    params["gpsProvince"] = gpsprovince
    params["gpsRegion"] = gpsregion
    LOGGER.info("保存位置信息V1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存位置信息V1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveOrcInfo(contractuuid, firstkey, note, result, secondkey, thirdkey):
    """
    保存人脸识别结果---美佳v1.0.5
    :param secondkey: 第二张图片key(Y),string
    :param firstkey: 第一张图片key(Y),string
    :param thirdkey: 第三张图片key(Y),string
    :param note: faceID返回结果(Y),string
    :param contractuuid: 如果是被驳回的，必须添加这个参数---美佳v1.0.5,string
    :param result: 认证结果，1成功，0失败，必填,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1837')
    requesturl = baseUrl + "/api/78dk/app/process/saveOrcInfo"
    LOGGER.info("保存人脸识别结果---美佳v1.0.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["firstKey"] = firstkey
    params["note"] = note
    params["result"] = result
    params["secondKey"] = secondkey
    params["thirdKey"] = thirdkey
    LOGGER.info("保存人脸识别结果---美佳v1.0.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存人脸识别结果---美佳v1.0.5请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_saveIdCardInfo(cardscanidcardno, cardscanname, frontkey, frontnote, oppositekey, oppositenote):
    """
    保存身份证信息
    :param cardscanname: 名字(Y),string
    :param frontkey: 身份证正面照key(Y),string
    :param cardscanidcardno: 身份证号码(Y),string
    :param oppositenote: 身份证反面照faceID返回结果(Y),string
    :param frontnote: 身份证正面照faceID返回结果(Y),string
    :param oppositekey: 身份证反面照key(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1838')
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


def test_api_78dk_app_process_getNewestIdCardInfo(contractuuid):
    """
    查询身份证信息(最近)---美佳v1.0.4修改
    :param contractuuid: 如果是被驳回的页面，需要这个参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1839')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestIdCardInfo"
    LOGGER.info("查询身份证信息(最近)---美佳v1.0.4修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询身份证信息(最近)---美佳v1.0.4修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询身份证信息(最近)---美佳v1.0.4修改请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1840')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1841')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1842')
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
    绑定银行卡1-输入银行卡信息V1.5.0改
    :param bankcardmobile: 银行卡预留手机号(Y),string
    :param billemail: 账单邮箱(N),string
    :param bankcardno: 银行卡号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1843')
    requesturl = baseUrl + "/api/78dk/app/process/saveBankCardInfo"
    LOGGER.info("绑定银行卡1-输入银行卡信息V1.5.0改请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankCardMobile"] = bankcardmobile
    params["bankCardNo"] = bankcardno
    params["billEmail"] = billemail
    LOGGER.info("绑定银行卡1-输入银行卡信息V1.5.0改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("绑定银行卡1-输入银行卡信息V1.5.0改请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1844')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1845')
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


def test_api_78dk_app_process_savePersonInfo(contactlist, contractuuid, datumtypeeducationid, datumtypehousingid, datumtypemarryid, email, iswork, livecity, livecityname, livedetail, liveprovince, liveprovincename, liveregion, liveregionname):
    """
    保存基本信息
    :param liveprovince: 居住地址-省编码(Y),number
    :param livecity: 居住地址-市编码(Y),number
    :param liveregionname: 居住地址-区名称(Y),string
    :param contractuuid: 订单uuid,string
    :param iswork: 是否有工作(Y ),number
    :param datumtypeeducationid: 学历(Y),number
    :param datumtypehousingid: 住房类型(Y),number
    :param datumtypemarryid: 婚姻状况(Y),number
    :param contactlist: 联系人信息列表,array<object>
    :param liveregion: 居住地址-区编码(Y),number
    :param livedetail: 居住地址-详细地址(Y),string
    :param livecityname: 居住地址-市名称(Y),string
    :param email: 邮箱(Y ),string
    :param liveprovincename: 居住地址-省名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1846')
    requesturl = baseUrl + "/api/78dk/app/process/savePersonInfo"
    LOGGER.info("保存基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["contactList"] = contactlist
    params["contractUuid"] = contractuuid
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


def test_api_78dk_app_process_getNewestPersonInfo(contractuuid):
    """
    查询基本信息(最近)---美佳v1.0.4修改
    :param contractuuid: 如果是被驳回的页面，需要添加这个数据,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1847')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestPersonInfo"
    LOGGER.info("查询基本信息(最近)---美佳v1.0.4修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询基本信息(最近)---美佳v1.0.4修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询基本信息(最近)---美佳v1.0.4修改请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1848')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1849')
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
    保存工作信息V1.4.0
    :param companyregionname: 单位地址-县名称(Y),string
    :param datumtypeworktimeid: 工作时间(Y),number
    :param position: 职位(Y),string
    :param scaleid: 单位规模(Y),number
    :param workphone: 工作电话(Y),string
    :param companyname: 单位名称(Y),string
    :param companycity: 单位地址-市编码(Y),number
    :param companyprovincename: 单位地址-省名称(Y),string
    :param companyregion: 单位地址-县编码(Y),number
    :param companycityname: 单位地址-市名称(Y),string
    :param datumtypeincomeid: 薪资(Y),number
    :param companyprovince: 单位地址-省编码(Y),number
    :param companydetail: 单位地址-详细地址(Y),string
    :param propertiesid: 单位性质(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1850')
    requesturl = baseUrl + "/api/78dk/app/process/saveWorkInfo"
    LOGGER.info("保存工作信息V1.4.0请求地址:【{}】".format(requesturl))
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
    LOGGER.info("保存工作信息V1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存工作信息V1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getNewestWorkInfo(contractuuid):
    """
    查询工作信息(最近)---美佳V1.0.4
    :param contractuuid: 如果是被驳回的页面，需要这个参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1851')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestWorkInfo"
    LOGGER.info("查询工作信息(最近)---美佳V1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询工作信息(最近)---美佳V1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询工作信息(最近)---美佳V1.0.4请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1852')
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


def test_api_78dk_app_process_saveContractImages(contractimagelist):
    """
    保存影像资料（美佳v1.0.0）
    :param contractimagelist: 影像资料列表,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1853')
    requesturl = baseUrl + "/api/78dk/app/process/saveContractImages"
    LOGGER.info("保存影像资料（美佳v1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractImageList"] = contractimagelist
    LOGGER.info("保存影像资料（美佳v1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存影像资料（美佳v1.0.0）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getContractImages(contractuuid):
    """
    查询影像资料(当前订单)---美佳v1.0.4修改
    :param contractuuid: 如果是被驳回的页面，需要添加这个参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1854')
    requesturl = baseUrl + "/api/78dk/app/process/getContractImages"
    LOGGER.info("查询影像资料(当前订单)---美佳v1.0.4修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询影像资料(当前订单)---美佳v1.0.4修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询影像资料(当前订单)---美佳v1.0.4修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getSpecialInfo():
    """
    查询特别信息认证进度V1.5.0
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1855')
    requesturl = baseUrl + "/api/78dk/app/process/getSpecialInfo"
    LOGGER.info("查询特别信息认证进度V1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询特别信息认证进度V1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询特别信息认证进度V1.5.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1856')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1857')
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
    :param taskid: taskId(N),string
    :param account: 帐号(Y),string
    :param school: 学校名称(Y),string
    :param vcode: 验证码(Y),string
    :param password: 密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1858')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1859')
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
    提交申请v1.0.0
    :param productdetailconfiguuid: 产品分期方案Uuid(N),string
    :param loanamount: 分期金额(N),number
    :param repaymentdate: 自定义还款日,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1860')
    requesturl = baseUrl + "/api/78dk/app/process/submitApply"
    LOGGER.info("提交申请v1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanAmount"] = loanamount
    params["productDetailConfigUuid"] = productdetailconfiguuid
    params["repaymentDate"] = repaymentdate
    LOGGER.info("提交申请v1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交申请v1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_repayPlanCalculator(isdiscount, loanamount, productdetailconfiguuid, productdetailuuid, repaymentdate, storeuuid):
    """
    还款计划试算
    :param repaymentdate: 自定义还款日（N）,number
    :param loanamount: 申请金额(Y),number
    :param isdiscount: 是否贴息(Y),boolean
    :param productdetailconfiguuid: 期数uuid(Y),string
    :param storeuuid: 门店Uuid(Y),string
    :param productdetailuuid: 产品Uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1861')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1862')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1863')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1864')
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


def test_api_78dk_app_common_getCites(parent):
    """
    获取城市列表
    :param parent: 父级地区编码,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1865')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1866')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1867')
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
    :param channelno: 应用平台渠道号(Y),string
    :param currentversnumb: APP当前版本号(Y),string
    :param platform: 平台(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1868')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1869')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1870')
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


def test_api_78dk_app_common_idCardInit():
    """
    初始化(获取身份认证)
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1871')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1872')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1873')
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
    :param paraminfo: 订单UUID（Y）,string
    :param pagesize: 每页条数(Y),number
    :param pagecurrent: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1874')
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
    申请详情V1.4.0
    :param loanorderuuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1875')
    requesturl = baseUrl + "/api/78dk/app/perCenter/loanDatail"
    LOGGER.info("申请详情V1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["loanOrderUuid"] = loanorderuuid
    LOGGER.info("申请详情V1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请详情V1.4.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1876')
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
    分期列表V1.4.0（美佳1.0.0）1.0.4
    :param pagesize: 每页条数(Y),number
    :param pagecurrent: 当前页数(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1877')
    requesturl = baseUrl + "/api/78dk/app/perCenter/viewByStagesLists"
    LOGGER.info("分期列表V1.4.0（美佳1.0.0）1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageCurrent"] = pagecurrent
    params["pageSize"] = pagesize
    LOGGER.info("分期列表V1.4.0（美佳1.0.0）1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("分期列表V1.4.0（美佳1.0.0）1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_takeGoods(contractuuid):
    """
    确认收货V1.4.0
    :param contractuuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1878')
    requesturl = baseUrl + "/api/78dk/app/perCenter/takeGoods"
    LOGGER.info("确认收货V1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("确认收货V1.4.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认收货V1.4.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_getTakeGoodsContent(contractuuid):
    """
    获取确认收货协议参数V1.40
    :param contractuuid: 订单uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1879')
    requesturl = baseUrl + "/api/78dk/app/perCenter/getTakeGoodsContent"
    LOGGER.info("获取确认收货协议参数V1.40请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("获取确认收货协议参数V1.40请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取确认收货协议参数V1.40请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1880')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1881')
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
    :param vercode: 验证码（新手机号）（Y）,number
    :param mobile: 新手机号（Y）,string
    :param idcard: 身份证号码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1882')
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
    :param pagecurrent: 当前页(Y),number
    :param pagesize: 页面大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1883')
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
    我的账单v1.0.0
    :param contractuuid: 合同uuid,string
    :param billdate: 账单时间(N),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1884')
    requesturl = baseUrl + "/api/78dk/app/bill/getMyBill"
    LOGGER.info("我的账单v1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["billDate"] = billdate
    params["contractUuid"] = contractuuid
    LOGGER.info("我的账单v1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("我的账单v1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_getBillDetail(userbilluuid):
    """
    账单明细v1.0.0（美佳1.0.0）
    :param userbilluuid: 账单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1885')
    requesturl = baseUrl + "/api/78dk/app/bill/getBillDetail"
    LOGGER.info("账单明细v1.0.0（美佳1.0.0）请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("账单明细v1.0.0（美佳1.0.0）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("账单明细v1.0.0（美佳1.0.0）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_immediateRepayment(userbankcarduuid, userbilluuid):
    """
    立刻还款V1.5.0
    :param userbilluuid: 账单Uuid,string
    :param userbankcarduuid: 银行卡信息UUID,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1886')
    requesturl = baseUrl + "/api/78dk/app/bill/immediateRepayment"
    LOGGER.info("立刻还款V1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBankCardUuid"] = userbankcarduuid
    params["userBillUuid"] = userbilluuid
    LOGGER.info("立刻还款V1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("立刻还款V1.5.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_paymentStatus(contractuuid):
    """
    还款状态v1.5.0（作废，合并到我的账单接口中去了）
    :param contractuuid: 合同Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1887')
    requesturl = baseUrl + "/api/78dk/app/bill/paymentStatus"
    LOGGER.info("还款状态v1.5.0（作废，合并到我的账单接口中去了）请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("还款状态v1.5.0（作废，合并到我的账单接口中去了）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("还款状态v1.5.0（作废，合并到我的账单接口中去了）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_bill_repaymentDetail(userbilluuid):
    """
    查询还款信息V1.5.0
    :param userbilluuid: 账单Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1888')
    requesturl = baseUrl + "/api/78dk/app/bill/repaymentDetail"
    LOGGER.info("查询还款信息V1.5.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["userBillUuid"] = userbilluuid
    LOGGER.info("查询还款信息V1.5.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询还款信息V1.5.0请求参数：【{}】".format(params))
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1889')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1890')
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
    :param registersource: 注册来源（N）,string
    :param mobile: 手机号（Y）,string
    :param mobilename: 注册时手机名字（N）,string
    :param password: 密码（Y）,string
    :param mobilenetwork: 注册是手机网络（N）,string
    :param vercode: 验证码（Y）,string
    :param mobileversion: 注册时手机版本号（N）,string
    :param appversion: 注册时APP版本号（N）,string
    :param mobileuuid: 手机唯一标识UUID（Y）,string
    :param mobilesystem: 手机系统（N）,string
    :param ipaddress: 注册时IP地址（N）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1891')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1892')
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
    :param mobile: 手机号（Y）,string
    :param jgpushid: 极光id编号（Y）,string
    :param password: 密码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1893')
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
    :param mobile: 手机号（Y）,string
    :param vercode: 验证码（Y）,number
    :param jgpushid: 极光id编号（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1894')
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1895')
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


def test_api_78dk_app_common_userInfo():
    """
    用户信息-v1.0.0
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1896')
    requesturl = baseUrl + "/api/78dk/app/common/userInfo"
    LOGGER.info("用户信息-v1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("用户信息-v1.0.0请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户信息-v1.0.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2153')
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


def test_api_78dk_app_process_saveCallList(paramlist):
    """
    保存通话详单（美佳v1.0.0-作废）
    :param paramlist: 请求参数List,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2158')
    requesturl = baseUrl + "/api/78dk/app/process/saveCallList"
    LOGGER.info("保存通话详单（美佳v1.0.0-作废）请求地址:【{}】".format(requesturl))
    params = dict()
    params["paramList"] = paramlist
    LOGGER.info("保存通话详单（美佳v1.0.0-作废）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存通话详单（美佳v1.0.0-作废）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
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
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2162')
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


def test_api_78dk_app_process_querySaList():
    """
    获取所有SA在职人员v1.0.4
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2218')
    requesturl = baseUrl + "/api/78dk/app/process/querySaList"
    LOGGER.info("获取所有SA在职人员v1.0.4请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取所有SA在职人员v1.0.4请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取所有SA在职人员v1.0.4请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_perCenter_findRejectModel(contractuuid):
    """
    根据订单查询被驳回的模块--美佳v1.0.5
    :param contractuuid: 订单uid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2223')
    requesturl = baseUrl + "/api/78dk/app/perCenter/findRejectModel"
    LOGGER.info("根据订单查询被驳回的模块--美佳v1.0.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("根据订单查询被驳回的模块--美佳v1.0.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据订单查询被驳回的模块--美佳v1.0.5请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_getNewestIdCardHandle(contractuuid):
    """
    查询身份证信息(手持)---美佳v1.0.4修改
    :param contractuuid: 如果是被驳回的页面，需添加这个参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2224')
    requesturl = baseUrl + "/api/78dk/app/process/getNewestIdCardHandle"
    LOGGER.info("查询身份证信息(手持)---美佳v1.0.4修改请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询身份证信息(手持)---美佳v1.0.4修改请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询身份证信息(手持)---美佳v1.0.4修改请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_findOrcInfo(contractuuid):
    """
    查询人脸识别结果---美佳v1.0.5
    :param contractuuid: 订单uid，被驳回的数据需要这个参数,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2554')
    requesturl = baseUrl + "/api/78dk/app/process/findOrcInfo"
    LOGGER.info("查询人脸识别结果---美佳v1.0.5请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    LOGGER.info("查询人脸识别结果---美佳v1.0.5请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询人脸识别结果---美佳v1.0.5请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_mask_product_getProductList(type):
    """
    产品列表--首页和分类列表共用
    :param type: 选填，产品分类，QD去痘，ZG整骨，SL瘦脸，MJ美甲,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2568')
    requesturl = baseUrl + "/api/78dk/app/mask/product/getProductList"
    LOGGER.info("产品列表--首页和分类列表共用请求地址:【{}】".format(requesturl))
    params = dict()
    params["type"] = type
    LOGGER.info("产品列表--首页和分类列表共用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品列表--首页和分类列表共用请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_mask_product_getProductInfo(id):
    """
    产品详情
    :param id: 产品的id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2569')
    requesturl = baseUrl + "/api/78dk/app/mask/product/getProductInfo"
    LOGGER.info("产品详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    LOGGER.info("产品详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品详情请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_mask_subscribe_getSubscribeList():
    """
    查看我的预约
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2570')
    requesturl = baseUrl + "/api/78dk/app/mask/subscribe/getSubscribeList"
    LOGGER.info("查看我的预约请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查看我的预约请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看我的预约请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_mask_subscribe_subscribe(productid, subscribetime):
    """
    预约
    :param subscribetime: 预约的时间，这个时间是完整的时间，yyyy-MM-dd HH:ss:mm,string
    :param productid: 产品id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2571')
    requesturl = baseUrl + "/api/78dk/app/mask/subscribe/subscribe"
    LOGGER.info("预约请求地址:【{}】".format(requesturl))
    params = dict()
    params["productId"] = productid
    params["subscribeTime"] = subscribetime
    LOGGER.info("预约请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("预约请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_authOrization(usermobile):
    """
    爬虫接口中心授权
    :param usermobile: 借贷人电话号码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2827')
    requesturl = baseUrl + "/api/78dk/app/process/authOrization"
    LOGGER.info("爬虫接口中心授权请求地址:【{}】".format(requesturl))
    params = dict()
    params["userMobile"] = usermobile
    LOGGER.info("爬虫接口中心授权请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("爬虫接口中心授权请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_app_process_centerCallback(data, message, result, task_id, timestamp, type, user_id):
    """
    爬虫接口中心回调
    :param data: 报告数据,string
    :param message: 描述失败的原因,string
    :param result: /通过result字段区分成功或失败。,string
    :param task_id: 任务标识,string
    :param timestamp: 回调时间,number
    :param type: 报告类型,string
    :param user_id: 用户标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2828')
    requesturl = baseUrl + "/api/78dk/app/process/centerCallback"
    LOGGER.info("爬虫接口中心回调请求地址:【{}】".format(requesturl))
    params = dict()
    params["data"] = data
    params["message"] = message
    params["result"] = result
    params["task_id"] = task_id
    params["timestamp"] = timestamp
    params["type"] = type
    params["user_id"] = user_id
    LOGGER.info("爬虫接口中心回调请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("爬虫接口中心回调请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


