#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : ShtAction.py
@desc       : 项目：xqkj 模块：sht 接口方法封装
"""

from xqkj.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('sht_apiURL', 'xqkj')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_sht_login()
API_TEST_HEADERS['token'] = LICENCES


def test_api_78dk_sht_login_login(code, name, phone, url):
    """
    登录
    :param code: 微信获取的code（Y）,string
    :param phone: 手机号,string
    :param name: 微信昵称（Y）,string
    :param url: 头像url(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1352')
    requesturl = baseUrl + "/api/78dk/sht/login/login"
    LOGGER.info("登录请求地址:【{}】".format(requesturl))
    params = dict()
    params["code"] = code
    params["name"] = name
    params["phone"] = phone
    params["url"] = url
    LOGGER.info("登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_merchant_findState():
    """
    查询用户对应商户状态
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1353')
    requesturl = baseUrl + "/api/78dk/sht/merchant/findState"
    LOGGER.info("查询用户对应商户状态请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询用户对应商户状态请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户对应商户状态请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_merchant_signing(merchantname, signname, signphone):
    """
    立即签约
    :param merchantname: 公司名称,string
    :param signname: 申请人姓名,string
    :param signphone: 申请人电话,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1354')
    requesturl = baseUrl + "/api/78dk/sht/merchant/signing"
    LOGGER.info("立即签约请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantName"] = merchantname
    params["signName"] = signname
    params["signPhone"] = signphone
    params["token"] = LICENCES
    LOGGER.info("立即签约请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("立即签约请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_merchant_binding(bindingnumber, merchantname):
    """
    商户绑定
    :param merchantname: 商户名称,string
    :param bindingnumber: 绑定编号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1355')
    requesturl = baseUrl + "/api/78dk/sht/merchant/binding"
    LOGGER.info("商户绑定请求地址:【{}】".format(requesturl))
    params = dict()
    params["bindingNumber"] = bindingnumber
    params["merchantName"] = merchantname
    params["token"] = LICENCES
    LOGGER.info("商户绑定请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户绑定请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_modifyMerchantInfo(city, installmentcooperationorgs, name, organizationcode, papermergen, province, shswdjz, shyyzz, shzzjgdm, socialunifiedcreditcode, taxregistrationnumber, tradefirst, tradesecond, uuid):
    """
    保存商户基础信息
    :param organizationcode: 组织机构代码,string
    :param socialunifiedcreditcode: 统一社会信用代码,string
    :param province: 省代码,string
    :param city: 城市代码,string
    :param name: 商户名,string
    :param taxregistrationnumber: 税务登记证号码,string
    :param tradesecond: 所属行业(第二级ID),number
    :param tradefirst: 所属行业(第一级ID),number
    :param shswdjz: 税务登记证图片,string
    :param shyyzz: 营业执照图片,string
    :param installmentcooperationorgs: 合作分期机构,array<object>
    :param papermergen: 是否三证合一,boolean
    :param shzzjgdm: 组织机构代码证图片,string
    :param uuid: uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1356')
    requesturl = baseUrl + "/api/78dk/sht/mm/modifyMerchantInfo"
    LOGGER.info("保存商户基础信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["city"] = city
    params["installmentCooperationOrgs"] = installmentcooperationorgs
    params["name"] = name
    params["organizationCode"] = organizationcode
    params["paperMergen"] = papermergen
    params["province"] = province
    params["shswdjz"] = shswdjz
    params["shyyzz"] = shyyzz
    params["shzzjgdm"] = shzzjgdm
    params["socialUnifiedCreditCode"] = socialunifiedcreditcode
    params["taxRegistrationNumber"] = taxregistrationnumber
    params["tradeFirst"] = tradefirst
    params["tradeSecond"] = tradesecond
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("保存商户基础信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存商户基础信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_findMerchantSummary(uuid):
    """
    商户信息详情列表
    :param uuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1357')
    requesturl = baseUrl + "/api/78dk/sht/mm/findMerchantSummary"
    LOGGER.info("商户信息详情列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("商户信息详情列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户信息详情列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_submitMerchant(uuid):
    """
    提交审核
    :param uuid: 商户uuid,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1358')
    requesturl = baseUrl + "/api/78dk/sht/mm/submitMerchant"
    LOGGER.info("提交审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("提交审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_findMerchantInfo(uuid):
    """
    查看商户基础信息
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1359')
    requesturl = baseUrl + "/api/78dk/sht/mm/findMerchantInfo"
    LOGGER.info("查看商户基础信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看商户基础信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看商户基础信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_common_queryTrade():
    """
    查询行业字典
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1362')
    requesturl = baseUrl + "/api/78dk/sht/common/queryTrade"
    LOGGER.info("查询行业字典请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询行业字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询行业字典请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountname, accountnumber, accountopeningbank, accounttype, branchname, shyhkfm, shyhkzm, shzm, uuid):
    """
    保存商户帐户信息
    :param accountopeningbank: 开户行名称,array<string>
    :param shzm: 开户许可证,string
    :param accountnumber: 银行卡号,string
    :param accountname: 开户人姓名,string
    :param uuid: ,string
    :param accounttype: 帐户类型,string
    :param branchname: 支行名称,string
    :param shyhkfm: 银行卡反面,string
    :param shyhkzm: 银行卡正面,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1364')
    requesturl = baseUrl + "/api/78dk/sht/mm/base/business/modifyAccountInfo"
    LOGGER.info("保存商户帐户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["accountName"] = accountname
    params["accountNumber"] = accountnumber
    params["accountOpeningBank"] = accountopeningbank
    params["accountType"] = accounttype
    params["branchName"] = branchname
    params["shyhkfm"] = shyhkfm
    params["shyhkzm"] = shyhkzm
    params["shzm"] = shzm
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("保存商户帐户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存商户帐户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_base_legal_findLegalPerson(uuid):
    """
    查看商户法人信息
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1365')
    requesturl = baseUrl + "/api/78dk/sht/mm/base/legal/findLegalPerson"
    LOGGER.info("查看商户法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看商户法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看商户法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_deleteMerchantImg(imageuuid, uuid):
    """
    删除一张图片
    :param imageuuid: 需要删除的图片的uuid,string
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1366')
    requesturl = baseUrl + "/api/78dk/sht/mm/deleteMerchantImg"
    LOGGER.info("删除一张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["imageUuid"] = imageuuid
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("删除一张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除一张图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_base_business_findAccountInfo(uuid):
    """
    查看商户帐户信息
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1367')
    requesturl = baseUrl + "/api/78dk/sht/mm/base/business/findAccountInfo"
    LOGGER.info("查看商户帐户信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看商户帐户信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看商户帐户信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_base_legal_modifyLegalPerson(cardnumber, mobile, name, shfrsfzf, shfrsfzfsc, shfrsfzz, uuid):
    """
    保存商户法人信息
    :param name: 法人姓名,string
    :param cardnumber: 法人身份证号,string
    :param shfrsfzf: 身份证反面,string
    :param mobile: 法人联系电话,string
    :param uuid: ,string
    :param shfrsfzfsc: 身份证手持,string
    :param shfrsfzz: 身份证正面,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1368')
    requesturl = baseUrl + "/api/78dk/sht/mm/base/legal/modifyLegalPerson"
    LOGGER.info("保存商户法人信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNumber"] = cardnumber
    params["mobile"] = mobile
    params["name"] = name
    params["shfrsfzf"] = shfrsfzf
    params["shfrsfzfsc"] = shfrsfzfsc
    params["shfrsfzz"] = shfrsfzz
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("保存商户法人信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存商户法人信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_queryMerchantImg(uuid):
    """
    查看商户补充图片
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1369')
    requesturl = baseUrl + "/api/78dk/sht/mm/queryMerchantImg"
    LOGGER.info("查看商户补充图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看商户补充图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看商户补充图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_common_queryAccountType():
    """
    查询帐户类型字典
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1370')
    requesturl = baseUrl + "/api/78dk/sht/common/queryAccountType"
    LOGGER.info("查询帐户类型字典请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询帐户类型字典请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询帐户类型字典请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_product_queryProducts(pagenum, pagesize, uuid):
    """
    查看商品列表
    :param pagesize: 可不填，默认10,number
    :param pagenum: 可不填，默认1,number
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1371')
    requesturl = baseUrl + "/api/78dk/sht/product/queryProducts"
    LOGGER.info("查看商品列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看商品列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看商品列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_bm_findBillDetail(orderuuid):
    """
    查看订单详情
    :param orderuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1372')
    requesturl = baseUrl + "/api/78dk/sht/bm/findBillDetail"
    LOGGER.info("查看订单详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderUuid"] = orderuuid
    params["token"] = LICENCES
    LOGGER.info("查看订单详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看订单详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_bm_queryBills(pagenum, pagesize, storeuuid):
    """
    查看门店下的订单
    :param pagenum: 可不填，默认1,
    :param pagesize: 可不填，默认10,
    :param storeuuid: 门店的uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1374')
    requesturl = baseUrl + "/api/78dk/sht/bm/queryBills"
    LOGGER.info("查看门店下的订单请求地址:【{}】".format(requesturl))
    params = dict()
    params["pageNum"] = pagenum
    params["pageSize"] = pagesize
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查看门店下的订单请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看门店下的订单请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_qrCode_showQRs(storeuuid):
    """
    查询二维码
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1379')
    requesturl = baseUrl + "/api/78dk/sht/qrCode/showQRs"
    LOGGER.info("查询二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查询二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询二维码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_qrCode_downloadQR(storeuuid):
    """
    下载二维码
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1380')
    requesturl = baseUrl + "/api/78dk/sht/qrCode/downloadQR"
    LOGGER.info("下载二维码请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    LOGGER.info("下载二维码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("下载二维码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht__store_modifyStoreBasic(area, email, employeesnum, idcardnumber, leasetimebegin, leasetimeend, managername, managerphone, storeaddress, storecity, storecitycode, storename, storeprovince, storeprovincecode, storeregion, storeregioncode, storeuuid):
    """
    新增（修改）门店基本信息
    :param employeesnum: 员工数量,number
    :param storeaddress: 门店详细地址,string
    :param storeuuid: 门店uuid,string
    :param storecitycode: 市代码,number
    :param storename: 门店名字,string
    :param storeregioncode: 区代码,number
    :param storeprovince: 门店位置（省）,string
    :param area: 门店租赁面积,string
    :param managerphone: 负责人电话,string
    :param idcardnumber: 身份证,string
    :param leasetimeend: 租赁到期日,string
    :param email: 业务邮箱,string
    :param storeregion: 门店位置（区）,string
    :param leasetimebegin: 租赁起始日,string
    :param storeprovincecode: 省代码,number
    :param storecity: 门店位置（市）,string
    :param managername: 负责人,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1381')
    requesturl = baseUrl + "/api/78dk/sht//store/modifyStoreBasic"
    LOGGER.info("新增（修改）门店基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["area"] = area
    params["email"] = email
    params["employeesNum"] = employeesnum
    params["idcardNumber"] = idcardnumber
    params["leaseTimeBegin"] = leasetimebegin
    params["leaseTimeEnd"] = leasetimeend
    params["managerName"] = managername
    params["managerPhone"] = managerphone
    params["storeAddress"] = storeaddress
    params["storeCity"] = storecity
    params["storeCityCode"] = storecitycode
    params["storeName"] = storename
    params["storeProvince"] = storeprovince
    params["storeProvinceCode"] = storeprovincecode
    params["storeRegion"] = storeregion
    params["storeRegionCode"] = storeregioncode
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("新增（修改）门店基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增（修改）门店基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_modifyStorebusiness(businessuuid, discountpercent, storebusinessproducts, storeuuid, workpercent):
    """
    新增（修改）门店业务信息
    :param discountpercent: 愿意贴息值,number
    :param storeuuid: 门店uuid,string
    :param storebusinessproducts: 商品价目表,array<object>
    :param businessuuid: 有--修改，无--新增,
    :param workpercent: 客户有无工作占比,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1382')
    requesturl = baseUrl + "/api/78dk/sht/store/modifyStorebusiness"
    LOGGER.info("新增（修改）门店业务信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["businessUuid"] = businessuuid
    params["discountPercent"] = discountpercent
    params["storeBusinessProducts"] = storebusinessproducts
    params["storeUuid"] = storeuuid
    params["workPercent"] = workpercent
    LOGGER.info("新增（修改）门店业务信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增（修改）门店业务信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_submitStore(storeuuid):
    """
    提交门店信息
    :param storeuuid: 门店uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1383')
    requesturl = baseUrl + "/api/78dk/sht/store/submitStore"
    LOGGER.info("提交门店信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("提交门店信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("提交门店信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_queryMerchantAccount(merchantuuid, storeuuid):
    """
    查询该商户被绑定的账号
    :param storeuuid: ,
    :param merchantuuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1384')
    requesturl = baseUrl + "/api/78dk/sht/store/queryMerchantAccount"
    LOGGER.info("查询该商户被绑定的账号请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查询该商户被绑定的账号请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询该商户被绑定的账号请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_findStorebusiness(storeuuid):
    """
    查询门店业务信息
    :param storeuuid: 门店uuid,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1385')
    requesturl = baseUrl + "/api/78dk/sht/store/findStorebusiness"
    LOGGER.info("查询门店业务信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查询门店业务信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店业务信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_findStoreBasic(storeuuid):
    """
    查询门店基本信息
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1386')
    requesturl = baseUrl + "/api/78dk/sht/store/findStoreBasic"
    LOGGER.info("查询门店基本信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查询门店基本信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店基本信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_queryStorePics(storeuuid):
    """
    查询门店证照信息
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1387')
    requesturl = baseUrl + "/api/78dk/sht/store/queryStorePics"
    LOGGER.info("查询门店证照信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("查询门店证照信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店证照信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_divideStore(storeuuid, useruuids):
    """
    门店分配
    :param useruuids: ,array<string>
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1388')
    requesturl = baseUrl + "/api/78dk/sht/store/divideStore"
    LOGGER.info("门店分配请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["userUuids"] = useruuids
    params["token"] = LICENCES
    LOGGER.info("门店分配请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("门店分配请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_queryStoreList(uuid):
    """
    查询门店列表
    :param uuid: 商户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1389')
    requesturl = baseUrl + "/api/78dk/sht/store/queryStoreList"
    LOGGER.info("查询门店列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查询门店列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询门店列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_saveStoreImg(key, storeuuid):
    """
    保存单张图片
    :param storeuuid: ,
    :param key: 图片分类,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1390')
    requesturl = baseUrl + "/api/78dk/sht/store/saveStoreImg"
    LOGGER.info("保存单张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("保存单张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存单张图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_deleteStoreImg(imageuuid, storeuuid):
    """
    删除单张图片
    :param imageuuid: 需要删除的图片的七牛id,
    :param storeuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1391')
    requesturl = baseUrl + "/api/78dk/sht/store/deleteStoreImg"
    LOGGER.info("删除单张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["imageUuid"] = imageuuid
    params["storeUuid"] = storeuuid
    params["token"] = LICENCES
    LOGGER.info("删除单张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除单张图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_findLegalPerson(merchantuuid):
    """
    同法人
    :param merchantuuid: ,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1394')
    requesturl = baseUrl + "/api/78dk/sht/store/findLegalPerson"
    LOGGER.info("同法人请求地址:【{}】".format(requesturl))
    params = dict()
    params["merchantUuid"] = merchantuuid
    params["token"] = LICENCES
    LOGGER.info("同法人请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("同法人请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_common_queryProvinceCitys():
    """
    查询省市
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1395')
    requesturl = baseUrl + "/api/78dk/sht/common/queryProvinceCitys"
    LOGGER.info("查询省市请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询省市请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询省市请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_common_queryProvinceCityRegions():
    """
    查询省市区
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1396')
    requesturl = baseUrl + "/api/78dk/sht/common/queryProvinceCityRegions"
    LOGGER.info("查询省市区请求地址:【{}】".format(requesturl))
    params = dict()
    params["token"] = LICENCES
    LOGGER.info("查询省市区请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询省市区请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_saveMerchantImg(key, uuid):
    """
    保存一张图片
    :param uuid: ,string
    :param key: 图片分类,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1401')
    requesturl = baseUrl + "/api/78dk/sht/mm/saveMerchantImg"
    LOGGER.info("保存一张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("保存一张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存一张图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_bm_queryStores(uuid):
    """
    查看门店
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1404')
    requesturl = baseUrl + "/api/78dk/sht/bm/queryStores"
    LOGGER.info("查看门店请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看门店请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看门店请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_base_store_queryStores(uuid):
    """
    查看门店
    :param uuid: ,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1502')
    requesturl = baseUrl + "/api/78dk/sht/mm/base/store/queryStores"
    LOGGER.info("查看门店请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["token"] = LICENCES
    LOGGER.info("查看门店请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看门店请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


