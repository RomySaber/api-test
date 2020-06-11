#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Center_qdAction.py
@desc       : 项目：center 模块：center_qd 接口方法封装
"""

from center.testAction import encryption
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('center_qd_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_api_v2_1565(apiname, urladdress, bucket):
    """
    获取七牛上传token
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param bucket: 七牛存储空间名字,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1565')
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


def test_api_v2_1566(apiname, urladdress, baseurl, qiniupickey):
    """
    获取七牛图片地址
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param baseurl: bucket绑定的域名,string
    :param qiniupickey: 私有空间文件key,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1566')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取七牛图片地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["baseUrl"] = baseurl
    params["qiniuPicKey"] = qiniupickey
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取七牛图片地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛图片地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1567(apiname, datas, phone, type, urladdress):
    """
    短信接口
    :param apiname: 接口标识,string
    :param datas: 模版变量值,string
    :param phone: 手机,string
    :param type: 短信类型,number
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1567')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("短信接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["Datas"] = datas
    params["Phone"] = phone
    params["Type"] = type
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("短信接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("短信接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1568(apiname, urladdress, mobile, taskid, type):
    """
    获取风控报告
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param mobile: 手机号,string
    :param taskid: 唯一标识id,string
    :param type: 报告类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1568')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取风控报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["mobile"] = mobile
    params["taskId"] = taskid
    params["type"] = type
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取风控报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风控报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1569(acctname, apiname, appname, email, liceneceno, phone, phoneone, phonetwo, urladdress):
    """
    获取同盾报告接口
    :param acctname: 姓名,string
    :param apiname: 接口标识,string
    :param appname: 同盾应用,string
    :param email: 邮箱,string
    :param liceneceno: 身份证号,string
    :param phone: 用户手机号,string
    :param phoneone: 第一联系人手机号,string
    :param phonetwo: 第二联系人手机号,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1569')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取同盾报告接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["AppName"] = appname
    params["Email"] = email
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["PhoneOne"] = phoneone
    params["PhoneTwo"] = phonetwo
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取同盾报告接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取同盾报告接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1570(apiname, urladdress, basicinfo, ids):
    """
    机审接口
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param basicinfo: 基础信息,array<object>
    :param ids: 报告id,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1570')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("机审接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["basicInfo"] = basicinfo
    params["ids"] = ids
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("机审接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机审接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1571(acctname, apiname, bankno, liceneceno, phone, urladdress):
    """
    银行卡四要素验证
    :param acctname: 姓名,string
    :param apiname: 接口标识,string
    :param bankno: 银行卡号,string
    :param liceneceno: 身份证号,string
    :param phone: 手机号,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1571')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("银行卡四要素验证请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["BankNo"] = bankno
    params["LiceneceNo"] = liceneceno
    params["Phone"] = phone
    params["UrlAddress"] = urladdress
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("银行卡四要素验证请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡四要素验证请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1572(apiname, urladdress, card):
    """
    银行卡信息获取
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param card: 银行卡号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1572')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("银行卡信息获取请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["card"] = card
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("银行卡信息获取请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡信息获取请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


