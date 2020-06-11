#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : WebAction.py
@desc       : 项目：qiloan 模块：web 接口方法封装
"""

from qiloan.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('web_apiURL', 'qiloan')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_web_login()


def test_api_78dk_web_globalQuota_queryGlobalQuotaList():
    """
    全局额度列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1434')
    requesturl = baseUrl + "/api/78dk/web/globalQuota/queryGlobalQuotaList"
    LOGGER.info("全局额度列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("全局额度列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全局额度列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_queryProductList(currentpage, pagesize, productname, productstate):
    """
    产品管理列表
    :param productname: 产品名称,string
    :param productstate: 产品状态,string
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1435')
    requesturl = baseUrl + "/api/78dk/web/sys/product/queryProductList"
    LOGGER.info("产品管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["productName"] = productname
    params["productState"] = productstate
    LOGGER.info("产品管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("产品管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryOrderList(applydateend, applydatestart, currentpage, machinecheckresult, orderstate, ordertype, pagesize, usermobile, username):
    """
    订单列表
    :param machinecheckresult: 机审结果,string
    :param applydateend: 申请结束时间,string
    :param applydatestart: 申请开始时间,string
    :param orderstate: 订单状态,string
    :param ordertype: 订单类型,string
    :param usermobile: 手机号码,string
    :param username: 姓名,string
    :param pagesize: 页面大小（Y）,string
    :param currentpage: 当前页（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1436')
    requesturl = baseUrl + "/api/78dk/web/loan/queryOrderList"
    LOGGER.info("订单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyDateEnd"] = applydateend
    params["applyDateStart"] = applydatestart
    params["currentPage"] = currentpage
    params["machineCheckResult"] = machinecheckresult
    params["orderState"] = orderstate
    params["orderType"] = ordertype
    params["pageSize"] = pagesize
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("订单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("订单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryOrderDetil(orderinfouuid):
    """
    查看详情
    :param orderinfouuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1437')
    requesturl = baseUrl + "/api/78dk/web/loan/queryOrderDetil"
    LOGGER.info("查看详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("查看详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_delProduct(sysproductuuid):
    """
    删除产品
    :param sysproductuuid: 产品uuid  (Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1438')
    requesturl = baseUrl + "/api/78dk/web/sys/product/delProduct"
    LOGGER.info("删除产品请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysProductUuid"] = sysproductuuid
    LOGGER.info("删除产品请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除产品请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_addProduct(headfeerate, loanperiods, penaltyrate, productname):
    """
    新增产品
    :param productname: 产品名称（Y）,string
    :param penaltyrate: 逾期费率(日)(Y),number
    :param headfeerate: 服务费利率(日)（Y）,number
    :param loanperiods: 借款期限（天）（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1439')
    requesturl = baseUrl + "/api/78dk/web/sys/product/addProduct"
    LOGGER.info("新增产品请求地址:【{}】".format(requesturl))
    params = dict()
    params["headFeeRate"] = headfeerate
    params["loanPeriods"] = loanperiods
    params["penaltyRate"] = penaltyrate
    params["productName"] = productname
    LOGGER.info("新增产品请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增产品请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_enableOrDisableProduct(productstate, sysproductuuid):
    """
    禁用/启用
    :param productstate: 产品状态(Y),string
    :param sysproductuuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1440')
    requesturl = baseUrl + "/api/78dk/web/sys/product/enableOrDisableProduct"
    LOGGER.info("禁用/启用请求地址:【{}】".format(requesturl))
    params = dict()
    params["productState"] = productstate
    params["sysProductUuid"] = sysproductuuid
    LOGGER.info("禁用/启用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("禁用/启用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_updateProduct(headfeerate, loanperiods, penaltyrate, productname, sysproductuuid):
    """
    编辑产品
    :param penaltyrate: 逾期费率(日)(Y),string
    :param loanperiods: 借款期限（天）(Y),number
    :param headfeerate: 服务费利率(日)(Y),number
    :param productname: 产品名称(Y),string
    :param sysproductuuid: 产品uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1441')
    requesturl = baseUrl + "/api/78dk/web/sys/product/updateProduct"
    LOGGER.info("编辑产品请求地址:【{}】".format(requesturl))
    params = dict()
    params["headFeeRate"] = headfeerate
    params["loanPeriods"] = loanperiods
    params["penaltyRate"] = penaltyrate
    params["productName"] = productname
    params["sysProductUuid"] = sysproductuuid
    LOGGER.info("编辑产品请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑产品请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_updateDictionary(dicttype, dicttypename, sysdicttypeuuid):
    """
    修改字典类型
    :param sysdicttypeuuid: 字典类型uuid(Y),string
    :param dicttype: 字典类型(Y),string
    :param dicttypename: 数据字典名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1442')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/updateDictionary"
    LOGGER.info("修改字典类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictType"] = dicttype
    params["dictTypeName"] = dicttypename
    params["sysDictTypeUuid"] = sysdicttypeuuid
    LOGGER.info("修改字典类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改字典类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_enableOrDisableDic(dictitemstate, sysdictionaryitemuuid):
    """
    启用/禁用字典条目
    :param sysdictionaryitemuuid: 字典条目uuid(Y),string
    :param dictitemstate: 字典条目状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1443')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/enableOrDisableDic"
    LOGGER.info("启用/禁用字典条目请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictItemState"] = dictitemstate
    params["sysDictionaryItemUuid"] = sysdictionaryitemuuid
    LOGGER.info("启用/禁用字典条目请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("启用/禁用字典条目请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_queryDictionaryList(currentpage, dicttype, dicttypename, pagesize):
    """
    字典管理一级列表
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param dicttypename: 数据字典名称,string
    :param dicttype: 字典类型,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1444')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/queryDictionaryList"
    LOGGER.info("字典管理一级列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["dictType"] = dicttype
    params["dictTypeName"] = dicttypename
    params["pageSize"] = pagesize
    LOGGER.info("字典管理一级列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典管理一级列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_addDictionary(dicttype, dicttypename):
    """
    新增字典类型
    :param dicttype: 字典类型(Y),string
    :param dicttypename: 数据字典名称(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1445')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/addDictionary"
    LOGGER.info("新增字典类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictType"] = dicttype
    params["dictTypeName"] = dicttypename
    LOGGER.info("新增字典类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增字典类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_appendDictionary(dictitemstate, dictname, sysdicttypeuuid):
    """
    添加字典条目
    :param dictitemstate: 字典条目状态(Y),string
    :param dictname: 字典条目名称(Y),string
    :param sysdicttypeuuid: 字典类型uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1446')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/appendDictionary"
    LOGGER.info("添加字典条目请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictItemState"] = dictitemstate
    params["dictName"] = dictname
    params["sysDictTypeUuid"] = sysdicttypeuuid
    LOGGER.info("添加字典条目请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("添加字典条目请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_delRole(sysroleuuid):
    """
    删除角色
    :param sysroleuuid: 角色_uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1447')
    requesturl = baseUrl + "/api/78dk/web/sys/role/delRole"
    LOGGER.info("删除角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("删除角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_addRole(resourcelist, rolename, roleremark, rolestate):
    """
    新增角色
    :param resourcelist: 资源列表(Y),array<string>
    :param rolestate: 角色状态(Y),string
    :param rolename: 角色名称(Y),string
    :param roleremark: 角色备注(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1448')
    requesturl = baseUrl + "/api/78dk/web/sys/role/addRole"
    LOGGER.info("新增角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["resourceList"] = resourcelist
    params["roleName"] = rolename
    params["roleRemark"] = roleremark
    params["roleState"] = rolestate
    LOGGER.info("新增角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_enableOrDisableRole(rolestate, sysroleuuid):
    """
    禁用/启用
    :param sysroleuuid: 角色uuid(Y),string
    :param rolestate: 角色状态(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1449')
    requesturl = baseUrl + "/api/78dk/web/sys/role/enableOrDisableRole"
    LOGGER.info("禁用/启用请求地址:【{}】".format(requesturl))
    params = dict()
    params["roleState"] = rolestate
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("禁用/启用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("禁用/启用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_updateRole(resourcelist, rolename, roleremark, rolestate, sysroleuuid):
    """
    编辑角色
    :param resourcelist: 资源列表(Y),array<string>
    :param rolename: 角色名称(Y),string
    :param roleremark: 角色备注(Y),string
    :param rolestate: 角色状态(Y),string
    :param sysroleuuid: 角色_uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1450')
    requesturl = baseUrl + "/api/78dk/web/sys/role/updateRole"
    LOGGER.info("编辑角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["resourceList"] = resourcelist
    params["roleName"] = rolename
    params["roleRemark"] = roleremark
    params["roleState"] = rolestate
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("编辑角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_queryRoleList(currentpage, pagesize, rolename, rolestate):
    """
    角色管理列表
    :param rolename: 角色名称,string
    :param rolestate: 角色状态,string
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1451')
    requesturl = baseUrl + "/api/78dk/web/sys/role/queryRoleList"
    LOGGER.info("角色管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["roleName"] = rolename
    params["roleState"] = rolestate
    LOGGER.info("角色管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("角色管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_bank_updateBankCard(banklogo, bankname, cardcolor, sysbankcarduuid, waterphoto):
    """
    修改银行卡
    :param sysbankcarduuid: 银行卡库uuid(Y),string
    :param banklogo: 银行llogo(Y),string
    :param bankname: 银行名称(Y),string
    :param cardcolor: 卡片背景色(Y),string
    :param waterphoto: 水印图片(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1452')
    requesturl = baseUrl + "/api/78dk/web/sys/bank/updateBankCard"
    LOGGER.info("修改银行卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankLogo"] = banklogo
    params["bankName"] = bankname
    params["cardColor"] = cardcolor
    params["sysBankCardUuid"] = sysbankcarduuid
    params["waterPhoto"] = waterphoto
    LOGGER.info("修改银行卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改银行卡请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_bank_addBandCard(banklogo, bankname, cardcolor, waterphoto):
    """
    新增银行卡
    :param cardcolor: 卡片背景色(Y),string
    :param banklogo: 银行llogo(Y),string
    :param bankname: 银行名称(Y),string
    :param waterphoto: 水印图片(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1453')
    requesturl = baseUrl + "/api/78dk/web/sys/bank/addBandCard"
    LOGGER.info("新增银行卡请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankLogo"] = banklogo
    params["bankName"] = bankname
    params["cardColor"] = cardcolor
    params["waterPhoto"] = waterphoto
    LOGGER.info("新增银行卡请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增银行卡请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_bank_queryBankList(bankname, currentpage, pagesize):
    """
    银行UI库列表
    :param currentpage: 当前页(Y),number
    :param pagesize: 每页大小(Y),number
    :param bankname: 银行名称,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1454')
    requesturl = baseUrl + "/api/78dk/web/sys/bank/queryBankList"
    LOGGER.info("银行UI库列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["bankName"] = bankname
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    LOGGER.info("银行UI库列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行UI库列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryAuditOrderHistory(orderinfouuid):
    """
    审核历史记录
    :param orderinfouuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1455')
    requesturl = baseUrl + "/api/78dk/web/loan/queryAuditOrderHistory"
    LOGGER.info("审核历史记录请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("审核历史记录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核历史记录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_auditOrder(auditresult, orderinfouuid, remark):
    """
    审核
    :param auditresult: 审核结果（Y）,string
    :param remark: 备注,string
    :param orderinfouuid: 订单UUID（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1456')
    requesturl = baseUrl + "/api/78dk/web/loan/auditOrder"
    LOGGER.info("审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditResult"] = auditresult
    params["orderInfoUuid"] = orderinfouuid
    params["remark"] = remark
    LOGGER.info("审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryMachineCheckDetil(orderinfouuid):
    """
    机审详情
    :param orderinfouuid: 订单uuid(Y)（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1457')
    requesturl = baseUrl + "/api/78dk/web/loan/queryMachineCheckDetil"
    LOGGER.info("机审详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("机审详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("机审详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryMachineScoreDetil(orderinfouuid):
    """
    评分详情
    :param orderinfouuid: 订单uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1458')
    requesturl = baseUrl + "/api/78dk/web/loan/queryMachineScoreDetil"
    LOGGER.info("评分详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("评分详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("评分详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryRiskWaitAuditList(applydateend, applydatestart, currentpage, pagesize, usermobile, username):
    """
    风控待审核
    :param applydateend: 申请结束时间,string
    :param applydatestart: 申请开始时间,string
    :param usermobile: 手机号码,string
    :param username: 姓名,string
    :param currentpage: 当前页(Y),string
    :param pagesize: 页面大小(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1459')
    requesturl = baseUrl + "/api/78dk/web/loan/queryRiskWaitAuditList"
    LOGGER.info("风控待审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyDateEnd"] = applydateend
    params["applyDateStart"] = applydatestart
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("风控待审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控待审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_queryRiskAlreadyAuditList(auditdateend, auditdatestart, auditresult, currentpage, orderstate, pagesize, usermobile, username):
    """
    风控已审核
    :param auditdateend: 审核结束时间,string
    :param auditdatestart: 审核开始时间,string
    :param auditresult: 审核结果,string
    :param orderstate: 订单状态,string
    :param currentpage: 当前页(Y),string
    :param pagesize: 页面大小(Y),string
    :param usermobile: 手机号,string
    :param username: 姓名,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1460')
    requesturl = baseUrl + "/api/78dk/web/loan/queryRiskAlreadyAuditList"
    LOGGER.info("风控已审核请求地址:【{}】".format(requesturl))
    params = dict()
    params["auditDateEnd"] = auditdateend
    params["auditDateStart"] = auditdatestart
    params["auditResult"] = auditresult
    params["currentPage"] = currentpage
    params["orderState"] = orderstate
    params["pageSize"] = pagesize
    params["userMobile"] = usermobile
    params["userName"] = username
    LOGGER.info("风控已审核请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("风控已审核请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_queryDictionaryListTwo(sysdicttypeuuid):
    """
    字典管理二级列表
    :param sysdicttypeuuid: 字典类型uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1461')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/queryDictionaryListTwo"
    LOGGER.info("字典管理二级列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysDictTypeUuid"] = sysdicttypeuuid
    LOGGER.info("字典管理二级列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("字典管理二级列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_delUser(sysadminuuid):
    """
    删除用户
    :param sysadminuuid: web用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1462')
    requesturl = baseUrl + "/api/78dk/web/sys/user/delUser"
    LOGGER.info("删除用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("删除用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_addUser(adminstate, name, password, phone, sysroleuuid, username):
    """
    新增用户
    :param username: 账号(Y),string
    :param sysroleuuid: 角色(Y),string
    :param adminstate: 用户状态(Y),string
    :param phone: 手机号(Y),string
    :param name: 姓名(Y),string
    :param password: 密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1463')
    requesturl = baseUrl + "/api/78dk/web/sys/user/addUser"
    LOGGER.info("新增用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["adminState"] = adminstate
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["sysRoleUuid"] = sysroleuuid
    params["username"] = username
    LOGGER.info("新增用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_queryUserList(adminstate, currentpage, pagesize, username):
    """
    用户管理列表
    :param adminstate: 用户状态,number
    :param currentpage: 当前页面数（Y）,number
    :param pagesize: 每页大小(Y),number
    :param username: 账号,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1464')
    requesturl = baseUrl + "/api/78dk/web/sys/user/queryUserList"
    LOGGER.info("用户管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["adminState"] = adminstate
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["username"] = username
    LOGGER.info("用户管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_enableOrDisableUser(adminstate, sysadminuuid):
    """
    禁用/启用
    :param adminstate: 用户状态,string
    :param sysadminuuid: web用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1465')
    requesturl = baseUrl + "/api/78dk/web/sys/user/enableOrDisableUser"
    LOGGER.info("禁用/启用请求地址:【{}】".format(requesturl))
    params = dict()
    params["adminState"] = adminstate
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("禁用/启用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("禁用/启用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_updateUser(adminstate, name, password, phone, sysadminuuid, sysroleuuid, username):
    """
    编辑用户
    :param adminstate: 用户状态(Y),string
    :param name: 姓名(Y),string
    :param password: 密码(N),string
    :param phone: 手机号(Y),string
    :param sysadminuuid: web用户uuid(Y),string
    :param sysroleuuid: 角色(Y),string
    :param username: 账号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1466')
    requesturl = baseUrl + "/api/78dk/web/sys/user/updateUser"
    LOGGER.info("编辑用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["adminState"] = adminstate
    params["name"] = name
    params["password"] = password
    params["phone"] = phone
    params["sysAdminUuid"] = sysadminuuid
    params["sysRoleUuid"] = sysroleuuid
    params["username"] = username
    LOGGER.info("编辑用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("编辑用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_vipClient_queryClientList(certify, currentpage, mobile, name, pagesize):
    """
    会员管理列表
    :param name: 姓名,string
    :param mobile: 手机号,string
    :param certify: 状态,string
    :param currentpage: 当前页面数（必填）,number
    :param pagesize: 当前展现条数（必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1467')
    requesturl = baseUrl + "/api/78dk/web/vipClient/queryClientList"
    LOGGER.info("会员管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["certify"] = certify
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("会员管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("会员管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_vipClient_queryClient(clientbaseuuid):
    """
    详情查看
    :param clientbaseuuid: 客户Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1468')
    requesturl = baseUrl + "/api/78dk/web/vipClient/queryClient"
    LOGGER.info("详情查看请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    LOGGER.info("详情查看请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("详情查看请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_getLoanList(applytimebegin, applytimeend, currentpage, mobile, name, pagesize):
    """
    获取放款列表接口
    :param applytimebegin: 申请开始时间,string
    :param applytimeend: 申请结束时间,string
    :param mobile: 手机号,string
    :param name: 姓名,string
    :param pagesize: 页大小（必填）,
    :param currentpage: 当前页 （必填）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1469')
    requesturl = baseUrl + "/api/78dk/web/loan/getLoanList"
    LOGGER.info("获取放款列表接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyTimeBegin"] = applytimebegin
    params["applyTimeEnd"] = applytimeend
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["name"] = name
    params["pageSize"] = pagesize
    LOGGER.info("获取放款列表接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取放款列表接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_SaveConfirmLoan(orderinfouuid):
    """
    确认放款接口
    :param orderinfouuid: 订单uuid（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1470')
    requesturl = baseUrl + "/api/78dk/web/loan/SaveConfirmLoan"
    LOGGER.info("确认放款接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("确认放款接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("确认放款接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_globalQuota_updateGlobalQuota(datalist):
    """
    全局额度保存
    :param datalist: ,array<object>
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1471')
    requesturl = baseUrl + "/api/78dk/web/globalQuota/updateGlobalQuota"
    LOGGER.info("全局额度保存请求地址:【{}】".format(requesturl))
    params = dict()
    params["dataList"] = datalist
    LOGGER.info("全局额度保存请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("全局额度保存请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_queryProductList():
    """
    查询产品列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1472')
    requesturl = baseUrl + "/api/78dk/web/common/queryProductList"
    LOGGER.info("查询产品列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询产品列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_tree():
    """
    资源树
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1473')
    requesturl = baseUrl + "/api/78dk/web/sys/role/tree"
    LOGGER.info("资源树请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("资源树请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("资源树请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_handQuota_queryHandQuotaList(currentpage, mobile, name, pagesize, quotalevel):
    """
    手动配置列表
    :param mobile: 手机号,string
    :param name: 姓名,string
    :param quotalevel: 额度等级,string
    :param currentpage: 当前页数（Y）,number
    :param pagesize: 每页条数（Y）,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1474')
    requesturl = baseUrl + "/api/78dk/web/handQuota/queryHandQuotaList"
    LOGGER.info("手动配置列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["name"] = name
    params["pageSize"] = pagesize
    params["quotaLevel"] = quotalevel
    LOGGER.info("手动配置列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动配置列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_handQuota_updateHandQuota(clientbaseuuid, productlist, quotaamount):
    """
    手动配置调额
    :param productlist: 期限列表,array<object>
    :param quotaamount: 额度,number
    :param clientbaseuuid: 用户uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1475')
    requesturl = baseUrl + "/api/78dk/web/handQuota/updateHandQuota"
    LOGGER.info("手动配置调额请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    params["productList"] = productlist
    params["quotaAmount"] = quotaamount
    LOGGER.info("手动配置调额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("手动配置调额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_homePage_queryTotalAmount():
    """
    首页-查询总额
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1476')
    requesturl = baseUrl + "/api/78dk/web/homePage/queryTotalAmount"
    LOGGER.info("首页-查询总额请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("首页-查询总额请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页-查询总额请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_queryReport(clientbaseuuid, type):
    """
    查看报告
    :param clientbaseuuid: 客户uuid(Y),string
    :param type: 报告类型(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1477')
    requesturl = baseUrl + "/api/78dk/web/common/queryReport"
    LOGGER.info("查看报告请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    params["type"] = type
    LOGGER.info("查看报告请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看报告请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_SaveRemit(orderinfouuid, type):
    """
    打款接口（根据type区分成功失败）
    :param orderinfouuid: 订单uuid（必填）,string
    :param type: 操作类型，枚举（success 成功，fail 失败）（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1478')
    requesturl = baseUrl + "/api/78dk/web/loan/SaveRemit"
    LOGGER.info("打款接口（根据type区分成功失败）请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    params["type"] = type
    LOGGER.info("打款接口（根据type区分成功失败）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("打款接口（根据type区分成功失败）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_homePage_readMsg(noticemsguuid):
    """
    首页-读取消息
    :param noticemsguuid: 消息uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1479')
    requesturl = baseUrl + "/api/78dk/web/homePage/readMsg"
    LOGGER.info("首页-读取消息请求地址:【{}】".format(requesturl))
    params = dict()
    params["noticeMsgUuid"] = noticemsguuid
    LOGGER.info("首页-读取消息请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页-读取消息请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_homePage_queryMsgList():
    """
    首页-消息列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1480')
    requesturl = baseUrl + "/api/78dk/web/homePage/queryMsgList"
    LOGGER.info("首页-消息列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("首页-消息列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("首页-消息列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_repay_getRepayList(currentpage, mobile, name, overduestate, pagesize, repaydatebegin, repaydateend):
    """
    获取还款列表
    :param repaydatebegin: 还款时间开始,string
    :param repaydateend: 还款时间结束,string
    :param mobile: ,string
    :param name: ,string
    :param overduestate: 逾期状态，枚举 （yes 是 ，no 否）,string
    :param currentpage: 当前页（必填）,
    :param pagesize: 页大小（必填）,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1481')
    requesturl = baseUrl + "/api/78dk/web/repay/getRepayList"
    LOGGER.info("获取还款列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["name"] = name
    params["overdueState"] = overduestate
    params["pageSize"] = pagesize
    params["repayDateBegin"] = repaydatebegin
    params["repayDateEnd"] = repaydateend
    LOGGER.info("获取还款列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取还款列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_repay_SaveRepaySettle(orderinfouuid):
    """
    结清接口
    :param orderinfouuid: 订单uuid（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1482')
    requesturl = baseUrl + "/api/78dk/web/repay/SaveRepaySettle"
    LOGGER.info("结清接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("结清接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("结清接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_repay_getOverdueList(applytimebegin, applytimeend, currentpage, mobile, name, orderstate, pagesize):
    """
    获取逾期订单列表
    :param applytimebegin: 申请时间开始,string
    :param applytimeend: 申请时间结束,string
    :param mobile: ,string
    :param name: ,string
    :param pagesize: 页大小（必填）,
    :param currentpage: 当前页（必填）,
    :param orderstate: 订单状态,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1483')
    requesturl = baseUrl + "/api/78dk/web/repay/getOverdueList"
    LOGGER.info("获取逾期订单列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyTimeBegin"] = applytimebegin
    params["applyTimeEnd"] = applytimeend
    params["currentPage"] = currentpage
    params["mobile"] = mobile
    params["name"] = name
    params["orderState"] = orderstate
    params["pageSize"] = pagesize
    LOGGER.info("获取逾期订单列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取逾期订单列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_vipClient_getMailList(clientbaseuuid):
    """
    获取通讯录接口
    :param clientbaseuuid: 客户Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1484')
    requesturl = baseUrl + "/api/78dk/web/vipClient/getMailList"
    LOGGER.info("获取通讯录接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    LOGGER.info("获取通讯录接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取通讯录接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_user_login(password, username):
    """
    登陆
    :param password: 密码(Y),string
    :param username: 帐号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1485')
    requesturl = baseUrl + "/api/78dk/web/user/login"
    LOGGER.info("登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["password"] = password
    params["username"] = username
    LOGGER.info("登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_user_updatePassword(newpassword, oldpassword):
    """
    修改密码
    :param newpassword: 新密码（Y）,string
    :param oldpassword: 旧密码（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1486')
    requesturl = baseUrl + "/api/78dk/web/user/updatePassword"
    LOGGER.info("修改密码请求地址:【{}】".format(requesturl))
    params = dict()
    params["newPassword"] = newpassword
    params["oldPassword"] = oldpassword
    LOGGER.info("修改密码请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("修改密码请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_user_loginOut():
    """
    退出登录
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1487')
    requesturl = baseUrl + "/api/78dk/web/user/loginOut"
    LOGGER.info("退出登录请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("退出登录请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("退出登录请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_vipClient_getBorrowRecordList(clientbaseuuid, currentpage, pagesize):
    """
    获取借款记录列表
    :param clientbaseuuid: 客户Uuid,string
    :param pagesize: 页大小,number
    :param currentpage: 当前页,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1488')
    requesturl = baseUrl + "/api/78dk/web/vipClient/getBorrowRecordList"
    LOGGER.info("获取借款记录列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    LOGGER.info("获取借款记录列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取借款记录列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_vipClient_getReportIsHaveState(clientbaseuuid):
    """
    获取报告有无状态接口
    :param clientbaseuuid: 客户Uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1489')
    requesturl = baseUrl + "/api/78dk/web/vipClient/getReportIsHaveState"
    LOGGER.info("获取报告有无状态接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    LOGGER.info("获取报告有无状态接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取报告有无状态接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_queryQiNiuToken(type):
    """
    获取七牛token
    :param type: string,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1490')
    requesturl = baseUrl + "/api/78dk/web/common/queryQiNiuToken"
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


def test_api_78dk_web_handQuota_queryQuotaList(clientbaseuuid):
    """
    可选额度列表
    :param clientbaseuuid: 用户uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1491')
    requesturl = baseUrl + "/api/78dk/web/handQuota/queryQuotaList"
    LOGGER.info("可选额度列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["clientBaseUuid"] = clientbaseuuid
    LOGGER.info("可选额度列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("可选额度列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_loan_getLoanOrderInfo(orderinfouuid):
    """
    查看订单信息接口
    :param orderinfouuid: 订单uuid（必填）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1492')
    requesturl = baseUrl + "/api/78dk/web/loan/getLoanOrderInfo"
    LOGGER.info("查看订单信息接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderInfoUuid"] = orderinfouuid
    LOGGER.info("查看订单信息接口请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查看订单信息接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_queryRole(sysroleuuid):
    """
    查询角色
    :param sysroleuuid: 角色_uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1493')
    requesturl = baseUrl + "/api/78dk/web/sys/role/queryRole"
    LOGGER.info("查询角色请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysRoleUuid"] = sysroleuuid
    LOGGER.info("查询角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_getImgUrl(key):
    """
    获取图片url地址
    :param key: 七牛key,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1494')
    requesturl = baseUrl + "/api/78dk/web/common/getImgUrl"
    LOGGER.info("获取图片url地址请求地址:【{}】".format(requesturl))
    params = dict()
    params["key"] = key
    LOGGER.info("获取图片url地址请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取图片url地址请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_role_queryRoleNameList():
    """
    查询所有角色
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1495')
    requesturl = baseUrl + "/api/78dk/web/sys/role/queryRoleNameList"
    LOGGER.info("查询所有角色请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("查询所有角色请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询所有角色请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_bank_queryBank(sysbankcarduuid):
    """
    银行卡库查询
    :param sysbankcarduuid: 银行卡库uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1496')
    requesturl = baseUrl + "/api/78dk/web/sys/bank/queryBank"
    LOGGER.info("银行卡库查询请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysBankCardUuid"] = sysbankcarduuid
    LOGGER.info("银行卡库查询请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("银行卡库查询请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_queryDicItemList(dicttypecode):
    """
    根据字典类型code查询字典条目列表（弃用）
    :param dicttypecode: 字典类型编号(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1497')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/queryDicItemList"
    LOGGER.info("根据字典类型code查询字典条目列表（弃用）请求地址:【{}】".format(requesturl))
    params = dict()
    params["dictTypeCode"] = dicttypecode
    LOGGER.info("根据字典类型code查询字典条目列表（弃用）请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("根据字典类型code查询字典条目列表（弃用）请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_product_queryProduct(sysproductuuid):
    """
    查询产品
    :param sysproductuuid: 产品uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1498')
    requesturl = baseUrl + "/api/78dk/web/sys/product/queryProduct"
    LOGGER.info("查询产品请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysProductUuid"] = sysproductuuid
    LOGGER.info("查询产品请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询产品请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_dictionary_queryDicType(sysdicttypeuuid):
    """
    查询字典类型
    :param sysdicttypeuuid: 字典类型uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1499')
    requesturl = baseUrl + "/api/78dk/web/sys/dictionary/queryDicType"
    LOGGER.info("查询字典类型请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysDictTypeUuid"] = sysdicttypeuuid
    LOGGER.info("查询字典类型请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询字典类型请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_sys_user_queryUser(sysadminuuid):
    """
    查询用户
    :param sysadminuuid: web用户uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1500')
    requesturl = baseUrl + "/api/78dk/web/sys/user/queryUser"
    LOGGER.info("查询用户请求地址:【{}】".format(requesturl))
    params = dict()
    params["sysAdminUuid"] = sysadminuuid
    LOGGER.info("查询用户请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("查询用户请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_common_uploadImg(file, type):
    """
    上传七牛图片
    :param file: 文件,object
    :param type: string,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1501')
    requesturl = baseUrl + "/api/78dk/web/common/uploadImg"
    LOGGER.info("上传七牛图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["file"] = file
    params["type"] = type
    LOGGER.info("上传七牛图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("上传七牛图片请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_link_saveLink(expirednum, linkname, opeoriginalurluuid, remark):
    """
    新建链接
    :param expirednum: 有效期,number
    :param linkname: 链接名称（Y）,string
    :param opeoriginalurluuid: 原始链接uuid,string
    :param remark: 备注（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1679')
    requesturl = baseUrl + "/api/78dk/web/link/saveLink"
    LOGGER.info("新建链接请求地址:【{}】".format(requesturl))
    params = dict()
    params["expiredNum"] = expirednum
    params["linkName"] = linkname
    params["opeOriginalUrlUuid"] = opeoriginalurluuid
    params["remark"] = remark
    LOGGER.info("新建链接请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新建链接请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_link_queryLinkPage(currentpage, linkname, pagesize, state):
    """
    链接管理列表
    :param currentpage: 当前页数（Y）,number
    :param linkname: 链接名称,string
    :param pagesize: 每页条数（Y）,number
    :param state: 状态,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1680')
    requesturl = baseUrl + "/api/78dk/web/link/queryLinkPage"
    LOGGER.info("链接管理列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["linkName"] = linkname
    params["pageSize"] = pagesize
    params["state"] = state
    LOGGER.info("链接管理列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("链接管理列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_link_queryRegisterPage(currentpage, opepromotionlinkuuid):
    """
    链接数据-注册详情
    :param currentpage: 当前页（Y）,number
    :param opepromotionlinkuuid: 推广链接uuid（Y）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1681')
    requesturl = baseUrl + "/api/78dk/web/link/queryRegisterPage"
    LOGGER.info("链接数据-注册详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["currentPage"] = currentpage
    params["opePromotionLinkUuid"] = opepromotionlinkuuid
    LOGGER.info("链接数据-注册详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("链接数据-注册详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_web_link_queryOriginalUrlList():
    """
    原始页面下拉列表
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1686')
    requesturl = baseUrl + "/api/78dk/web/link/queryOriginalUrlList"
    LOGGER.info("原始页面下拉列表请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("原始页面下拉列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("原始页面下拉列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


