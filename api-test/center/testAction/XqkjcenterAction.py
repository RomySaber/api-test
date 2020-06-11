#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : XqkjcenterAction.py
@desc       : 项目：center 模块：xqkjcenter 接口方法封装
"""

from center.testAction import encryption
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('xqkjcenter_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_api_v2_89(acctname, apiname, liceneceno, phone, urladdress):
    """
    申请同盾报告
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_TDREPLY_BATCH”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param acctname: 姓名,AcctName,string（6）,参与签名，必输
    :param liceneceno: 身份证号,LiceneceNo,string（12）,参与签名，必输
    :param phone: 电话号,Phone,string（30）,参与签名，必输
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 89')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("申请同盾报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("申请同盾报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("申请同盾报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_90(apiname, reportid, urladdress):
    """
    查询用户同盾报告
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_TDREPORT_BATCH”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param reportid: 同盾报告ID,ReportId,string（12）,参与签名，必输
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 90')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("查询用户同盾报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["ReportId"] = reportid
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("查询用户同盾报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户同盾报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_91(acctname, apiname, bankcard, liceneceno, phone, urladdress, userid):
    """
    签约申请接口WEB_KQ_AUTH+WEB_KQ_VERIFY扣款：有两种方式（建议使用单笔代扣）协议支付:WEB_KQ_QPAY+WEB_KQ_PAYQUERY（商户类型Flag=2）单笔代扣：WEB_KQ_DDPUR+WEB_KQ_PAYQUERY（商户类型Flag=1）
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_KQ_AUTH”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param userid: 用户ID,UserId,string（64）,参与签名，必输。系统唯一
    :param bankcard: 用户银行卡号,BankCard,string（64）,参与签名，必输。
    :param acctname: 持卡人姓名,AcctName,string（64）,参与签名，必输。
    :param liceneceno: 身份证号码,LiceneceNo,string（64）,参与签名，必输。
    :param phone: 手机号,Phone,string（64）,参与签名，必输。
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 91')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("签约申请接口WEB_KQ_AUTH+WEB_KQ_VERIFY扣款：有两种方式（建议使用单笔代扣）协议支付:WEB_KQ_QPAY+WEB_KQ_PAYQUERY（商户类型Flag=2）单笔代扣：WEB_KQ_DDPUR+WEB_KQ_PAYQUERY（商户类型Flag=1）请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["BankCard"] = bankcard
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    params["UserId"] = userid
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("签约申请接口WEB_KQ_AUTH+WEB_KQ_VERIFY扣款：有两种方式（建议使用单笔代扣）协议支付:WEB_KQ_QPAY+WEB_KQ_PAYQUERY（商户类型Flag=2）单笔代扣：WEB_KQ_DDPUR+WEB_KQ_PAYQUERY（商户类型Flag=1）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约申请接口WEB_KQ_AUTH+WEB_KQ_VERIFY扣款：有两种方式（建议使用单笔代扣）协议支付:WEB_KQ_QPAY+WEB_KQ_PAYQUERY（商户类型Flag=2）单笔代扣：WEB_KQ_DDPUR+WEB_KQ_PAYQUERY（商户类型Flag=1）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_92(apiname, transactionid, urladdress, validcode):
    """
    签约短信验证接口
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_KQ_VERIFY”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param transactionid: 绑卡流水号,TransactionId,string（32）,参与签名，必输。上面接口返回的数据
    :param validcode: 手机验证码,ValidCode,string（12）,参与签名，必输
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 92')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("签约短信验证接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["TransactionId"] = transactionid
    params["UrlAddress"] = urladdress
    params["ValidCode"] = validcode
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("签约短信验证接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("签约短信验证接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_93(acctname, amount, apiname, bankcard, liceneceno, paytransactionid, paymentmark, phone, urladdress, userid):
    """
    单笔代扣接口
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_KQ_DDPUR”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param paytransactionid: 交易流水号,PayTransactionId,string（64）,参与签名，必输。
    :param userid: 用户ID,UserId,string（64）,参与签名，必输
    :param bankcard: 扣款银行卡号,BankCard,string（64）,参与签名，必输
    :param acctname: 持卡人姓名,AcctName,string（64）,参与签名，必输。
    :param liceneceno: 身份证号码,LiceneceNo,string（64）,参与签名，必输。
    :param phone: 手机号,Phone,string（64）,参与签名，必输。
    :param amount: 金额,Amount,float,参与签名，必输。 单位元，保留两位小数
    :param paymentmark: 备注,PaymentMark,string（64）,参与签名，必输。
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 93')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("单笔代扣接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["Amount"] = amount
    params["ApiName"] = apiname
    params["BankCard"] = bankcard
    params["LiceneceNo"] = liceneceno
    params["PayTransactionId"] = paytransactionid
    params["PaymentMark"] = paymentmark
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    params["UserId"] = userid
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("单笔代扣接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("单笔代扣接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_94(amount, apiname, bankcard, paytransactionid, paymentmark, phone, urladdress, userid):
    """
    协议支付接口（前提是用户银行卡已经绑定）
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_KQ_QPAY”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param userid: 用户ID,UserId,string（64）,参与签名，必输
    :param bankcard: 扣款银行卡号,BankCard,string（64）,参与签名，必输
    :param phone: 手机号,Phone,string（64）,参与签名，必输。
    :param amount: 金额,Amount,float,参与签名，必输。 单位元，保留两位小数
    :param paytransactionid: 交易流水号,PayTransactionId,string（64）,参与签名，必输。保证唯一性。
    :param paymentmark: 备注,PaymentMark,string（64）,参与签名，必输。
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 94')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("协议支付接口（前提是用户银行卡已经绑定）请求地址:【{}】".format(requesturl))
    params = dict()
    params["Amount"] = amount
    params["ApiName"] = apiname
    params["BankCard"] = bankcard
    params["PayTransactionId"] = paytransactionid
    params["PaymentMark"] = paymentmark
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    params["UserId"] = userid
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("协议支付接口（前提是用户银行卡已经绑定）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("协议支付接口（前提是用户银行卡已经绑定）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_95(apiname, flag, paytransactionid, txntype, urladdress):
    """
    单笔代扣、协议支付结果查询
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_KQ_PAYQUERY”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param paytransactionid: 交易流水号,PayTransactionId,string（64）,参与签名，必输
    :param txntype: 交易类型,TxnType,string(300),参与签名，必输
    :param flag: 商户类型,Flag,string(2),参与签名，必输。1表示单笔代扣查询；2表示协议支付查询
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 95')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("单笔代扣、协议支付结果查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["Flag"] = flag
    params["PayTransactionId"] = paytransactionid
    params["TxnType"] = txntype
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("单笔代扣、协议支付结果查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("单笔代扣、协议支付结果查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_96(apiname, urladdress, bucket):
    """
    获取七牛上传token
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_QINIU_TOKEN”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：dev.cloud.78dk.com
    :param bucket: 七牛存储空间名字,bucket,string（64）,参与签名，必输，如：weixin
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 96')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取七牛上传token请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["bucket"] = bucket
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取七牛上传token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛上传token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_97(apiname, urladdress, baseurl, qiniupickey):
    """
    获取图片下载私链
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_QINIU_GETPICTURE”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：dev.cloud.78dk.com
    :param baseurl: bucket绑定的域名,baseUrl,string（30）,参与签名，必输，如：http://images.yidong88.com/
    :param qiniupickey: ,私有空间文件key,qiniuPicKey,string（300）,参与签名，必输，如：-0Evidfzl2qYz2dUY6m4Z77uH4R_xdrHo-cOPpyL0Sl4TA56zCWtF0vW37AhkcST_1498125301
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 97')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取图片下载私链请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["baseUrl"] = baseurl
    params["qiniuPicKey"] = qiniupickey
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取图片下载私链请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片下载私链请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_98(acctname, apiname, content, liceneceno, phone, urladdress):
    """
    手动签署合同，返回法大大签署合同url。
    :param apiname: 接口标识,ApiName,string（32）,必输，取值：“WEB_FDD_SIGN”
    :param urladdress: 项目域名,UrlAddress,string（32）,必输，如：test2.xyf.78dk.com
    :param acctname: 姓名,AcctName,string（16）,必输
    :param liceneceno: 身份证号,LiceneceNo,string（32）,必输
    :param phone: 电话号,Phone,string（32）,必输
    :param content: 填充数据列表,Content,list,具体合同见下面说明。
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 98')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("手动签署合同，返回法大大签署合同url。请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["Content"] = content
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    LOGGER.info("手动签署合同，返回法大大签署合同url。请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动签署合同，返回法大大签署合同url。请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_99(acctname, apiname, contractid, liceneceno, phone, urladdress):
    """
    查询用户是否已经签署某份合同
    :param apiname: 接口标识,ApiName,string（30）,必输，取值：“WEB_FDD_SIGN_SEARCH”
    :param urladdress: 项目域名,UrlAddress,string（30）,必输，如：test2.xyf.78dk.com
    :param contractid: 合同编号,ContractId,string（60）,必输。如果是多个合同，请用&隔开。比如： XXXX_A&XXXX_B&XXXX_C
    :param acctname: 姓名,AcctName,string（16）,必输
    :param liceneceno: 身份证号,LiceneceNo,string（32）,必输
    :param phone: 电话号,Phone,string（32）,必输
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 99')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("查询用户是否已经签署某份合同请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["ContractId"] = contractid
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    LOGGER.info("查询用户是否已经签署某份合同请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户是否已经签署某份合同请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_100(apiname, clientrole, contractid, urladdress):
    """
    调签署接口（自动）。接入平台将合同签署状态更改为签署完成。
    :param apiname: 接口标识,string（30）,ApiName,必输，取值：“WEB_FDD_COMPANY_SIGN”
    :param urladdress: 项目域名,string（30）,UrlAddress,必输，如：test2.xyf.78dk.com
    :param contractid: 合同编号,string（60）,ContractId,必输
    :param clientrole: 客户角色,string（60）,ClientRole,必输。默认为1，1：公司签章（###） 2：担保公司签章（###） 3：投资人签章（###）
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 100')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("调签署接口（自动）。接入平台将合同签署状态更改为签署完成。请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["ClientRole"] = clientrole
    params["ContractId"] = contractid
    params["UrlAddress"] = urladdress
    LOGGER.info("调签署接口（自动）。接入平台将合同签署状态更改为签署完成。请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("调签署接口（自动）。接入平台将合同签署状态更改为签署完成。请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_101(apiname, contractid, urladdress):
    """
    接入平台将合同签署状态更改为签署完成。
    :param apiname: 接口标识,ApiName,string（30）,必输，取值：“WEB_FDD_SAVE”
    :param urladdress: 项目域名,UrlAddress,string（30）,必输，如：test2.xyf.78dk.com
    :param contractid: 合同编号,ContractId,string（60）,必输
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 101')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("接入平台将合同签署状态更改为签署完成。请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["ContractId"] = contractid
    params["UrlAddress"] = urladdress
    LOGGER.info("接入平台将合同签署状态更改为签署完成。请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("接入平台将合同签署状态更改为签署完成。请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_102(apiname, datas, phone, type, urladdress):
    """
    发送短信
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“WEB_JTLSENDMSG_BATCH”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：test2.xyf.78dk.com
    :param phone: 手机,Phone,string（12）,参与签名，必输
    :param type: 短信类型,Type,int（5）,参与签名，必输，见模版说明
    :param datas: 模版变量值,Datas,string（200）,不参与签名，见模版说明
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 102')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("发送短信请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["Datas"] = datas
    params["Phone"] = phone
    params["Type"] = type
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("发送短信请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发送短信请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_103(apiname, cardnum, name, urladdress):
    """
    根据传入的个人信息，获取在册的被执行信息
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“FK_CREDIT_DISHONEST”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：dev.78dk.com
    :param cardnum: 身份证号,Cardnum,string（11）,参与签名，必输，如：232330199308204414
    :param name: 姓名,Name,string（64）,参与签名，必输，如：谭伟东
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 103')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("根据传入的个人信息，获取在册的被执行信息请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["Cardnum"] = cardnum
    params["Name"] = name
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("根据传入的个人信息，获取在册的被执行信息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据传入的个人信息，获取在册的被执行信息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_104(apiname, urladdress, mobile, taskid, type):
    """
    根据传入task_id，获取对应风控报告。
    :param apiname: 接口标识,ApiName,string（30）,参与签名，必输，取值：“FK_REPORT”
    :param urladdress: 项目域名,UrlAddress,string（30）,参与签名，必输，如：dev.78dk.com
    :param taskid: 唯一标识id,taskId,string（30）,参与签名，必输，如：“jingdong_ughkjnlkjhkj&aslkdyu7fh”（第三方魔蝎报告没有_及前缀）
    :param type: 报告类型,type,string（30）,参与签名，必输，如：jingdong、taobao、alipay、carrier(运营商)
    :param mobile: 手机号,mobile,string（11）,参与签名，请求运营商类型时必输，如：“18284559877”
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 104')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("根据传入task_id，获取对应风控报告。请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["mobile"] = mobile
    params["taskId"] = taskid
    params["type"] = type
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("根据传入task_id，获取对应风控报告。请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据传入task_id，获取对应风控报告。请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_IP_api_faceId_ocridcard_105(image, project, returnportrait):
    """
    根据传入身份证图片，获取图片内容。
    :param project: 调用faceId接口的项目名字,project,string（10）,必输，如：“fuqin”
    :param image: 身份证照片,image,File,必输
    :param returnportrait: 身份证人像开关,returnPortrait,string（1）,0（不返回，默认值），1（返回），只在传入图片为身份证正面才起效
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 105')
    requesturl = baseUrl + "/IP/api/faceId/ocridcard"
    LOGGER.info("根据传入身份证图片，获取图片内容。请求地址:【{}】".format(requesturl))
    params = dict()
    params["image"] = image
    params["project"] = project
    params["returnPortrait"] = returnportrait
    LOGGER.info("根据传入身份证图片，获取图片内容。请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据传入身份证图片，获取图片内容。请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


