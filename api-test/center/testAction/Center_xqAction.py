#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Center_xqAction.py
@desc       : 项目：center 模块：center_xq 接口方法封装
"""

from center.testAction import encryption
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('center_xq_apiURL', 'center')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
appkey = '1552893617253867'


def test_api_v2_1326(apiname, urladdress, taskid):
    """
    学信网获取报告
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param taskid: 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1326')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("学信网获取报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["taskId"] = taskid
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("学信网获取报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网获取报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1327(apiname, urladdress, code, password, school, username):
    """
    学信网登录授权
    :param school: 学校,string
    :param code: 图片验证码,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param password: 密码,string
    :param username: 账号,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1327')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("学信网登录授权请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["code"] = code
    params["password"] = password
    params["school"] = school
    params["username"] = username
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("学信网登录授权请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网登录授权请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1328(apiname, urladdress, basicinfo, ids):
    """
    机审接口
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param basicinfo: 基本信息,array<string>
    :param ids: task_id的数组,array<string>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1328')
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


def test_api_v2_1329(apiname, urladdress, code, password, school, taskid, username):
    """
    学信网登录授权
    :param school: 学校,string
    :param code: 图片验证码,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param password: 密码,string
    :param username: 账号,string
    :param taskid: 任务id,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1329')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("学信网登录授权请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["code"] = code
    params["password"] = password
    params["school"] = school
    params["taskId"] = taskid
    params["username"] = username
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("学信网登录授权请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("学信网登录授权请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1331(apiname, urladdress, bucket):
    """
    获取七牛上传token
    :param bucket: 七牛存储空间名字,string
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1331')
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


def test_api_v2_1332(apiname, urladdress, baseurl, qiniupickey):
    """
    获取七牛图片地址
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param baseurl: bucket绑定的域名,string
    :param qiniupickey: 私有空间文件key,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1332')
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


def test_api_v2_1333(acctname, apiname, contentid, liceneceno, phone, urladdress):
    """
    查询用户是否已经签署某份合同
    :param acctname: 姓名,string
    :param apiname: 接口标识,string
    :param contentid: 合同编号,string
    :param liceneceno: 身份证号,string
    :param phone: 电话号,string
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1333')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("查询用户是否已经签署某份合同请求地址:【{}】".format(requesturl))
    params = dict()
    params["AcctName"] = acctname
    params["ApiName"] = apiname
    params["ContentId"] = contentid
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


def test_api_v2_1334(apiname, clientrole, contentid, urladdress):
    """
    接入方签章（公司签章、投资人签章、担保公司签章）
    :param apiname: 接口标识,string
    :param clientrole: 客户角色,string
    :param contentid: 合同编号,array<object>
    :param urladdress: 项目域名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1334')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("接入方签章（公司签章、投资人签章、担保公司签章）请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["ClientRole"] = clientrole
    params["ContentId"] = contentid
    params["UrlAddress"] = urladdress
    LOGGER.info("接入方签章（公司签章、投资人签章、担保公司签章）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("接入方签章（公司签章、投资人签章、担保公司签章）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1335(apiname, contractid, urladdress):
    """
    合同归档
    :param urladdress: 项目域名,string
    :param contractid: 合同编号,string
    :param apiname: 接口标识,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1335')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("合同归档请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["ContractId"] = contractid
    params["UrlAddress"] = urladdress
    LOGGER.info("合同归档请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("合同归档请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1336(apiname, urladdress, mobile, taskid, type):
    """
    获取风控报告（京东、淘宝、支付宝、运营商）
    :param apiname: 接口标识,string
    :param urladdress: 项目域名,string
    :param mobile: 手机号,string
    :param taskid: 唯一标识id,string
    :param type: 报告类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1336')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("获取风控报告（京东、淘宝、支付宝、运营商）请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["mobile"] = mobile
    params["taskId"] = taskid
    params["type"] = type
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("获取风控报告（京东、淘宝、支付宝、运营商）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取风控报告（京东、淘宝、支付宝、运营商）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_v2_1402(apiname, urladdress, number):
    """
    根据银行卡前六位获取银行名字
    :param apiname: 接口标识,string
    :param urladdress: 项目,string
    :param number: 银行卡前六位,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1402')
    requesturl = baseUrl + "/api/v2"
    LOGGER.info("根据银行卡前六位获取银行名字请求地址:【{}】".format(requesturl))
    params = dict()
    params["ApiName"] = apiname
    params["UrlAddress"] = urladdress
    params["number"] = number
    params = encryption.get_encryption_param(params, appkey)
    LOGGER.info("根据银行卡前六位获取银行名字请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据银行卡前六位获取银行名字请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


