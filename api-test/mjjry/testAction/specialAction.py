#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-15 下午 4:13
@Author     : 罗林
@File       : specialAction.py
@desc       :  参数为非通用接口
"""

import copy
import json
import time
import requests

from common.myCommon import Assertion
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent as ms
from mjjry.testAction import WebAction
from mjjry.testAction import AppAction

LOGGER = getlog(__name__)
rq = requests.Session()


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(params):
    """
    新增/修改权限
    platform_privilege_uuid = [
            {"platformPrivilegeUuid": platform_privilege_uuid0, "platformUserUuid": platform_user_profile_uuid},
            {"platformPrivilegeUuid": platform_privilege_uuid1, "platformUserUuid": platform_user_profile_uuid}]
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2012')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
    WebAction.LOGGER.info("新增/修改权限请求地址:【{}】".format(requesturl))
    WebAction.LOGGER.info("新增/修改权限请求参数：【{}】".format(params))
    response = WebAction.rq.post(requesturl, data=json.dumps(params), headers=WebAction.API_TEST_HEADERS)
    WebAction.LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_product_pmm_saveMerchantTX(params):
    """
    保存商户贴息
    :param params: [{"rate": rate, "merchantUuid": merchantuuid,
    "productDetailConfigUuid": productdetailconfiguuid, "
    discountRate": discountrate, "period": period}]
    :return: response.text
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1946')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    WebAction.LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    WebAction.LOGGER.info("保存商户贴息请求参数：【{}】".format(params))
    response = WebAction.rq.post(requesturl, data=str(params), headers=WebAction.API_TEST_HEADERS)
    WebAction.LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_api_78dk_platform_mm_saveContractImages(images):
    """
    影像资料保存-v1.4
    :param images: 图片数组,array<object>
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1961')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存-v1.5.1请求地址:【{}】".format(requesturl))
    LOGGER.info("影像资料保存-v1.5.1请求头参数：【{}】".format(WebAction.API_TEST_HEADERS))
    LOGGER.info("影像资料保存-v1.5.1请求参数：【{}】".format(images))
    response = rq.post(requesturl, data=json.dumps(images), headers=WebAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_showSupplementImage(contractuuid):
    """
    展示补录的图片资料 V1.3 新增
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2051')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/tm/first/showSupplementImage"
    LOGGER.info("展示补录的图片资料 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = WebAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    # del my_API_TEST_HEADERS['mytoken']
    LOGGER.info("展示补录的图片资料 V1.3 新增请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("展示补录的图片资料 V1.3 新增请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_xuexinreport(contractuuid):
    """
    学信网报告 V1.3 新增
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2048')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/tm/first/xuexinreport"
    LOGGER.info("学信网报告 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = WebAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    LOGGER.info("学信网报告 V1.3 新增请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("学信网报告 V1.3 新增请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid):
    """
    商户结算信息查询接口 - V1.3 新增
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2047')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/tm/first/businessbillinginformation"
    LOGGER.info("商户结算信息查询接口 - V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = WebAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    LOGGER.info("商户结算信息查询接口 - V1.3 新增请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("商户结算信息查询接口 - V1.3 新增请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_first_queryElectronuclearRemark(contractuuid):
    """
    电核备注 - 查询接口 V1.3 新增
    :param contractuuid: 合同UUID,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2052')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/tm/first/queryElectronuclearRemark"
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = WebAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_downContracts(begindate, enddate, name, orderstate):
    """
    导出申请列表-v1.4.0
    :param enddate: 结束时间,number
    :param begindate: 开始时候,number
    :param name: 组合查询字段,string
    :param orderstate: 订单状态,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2089')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["orderState"] = orderstate
    params["MyToken"] = WebAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    LOGGER.info("导出申请列表-v1.4.0请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("导出申请列表-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=params, headers=my_API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1884')
    requesturl = AppAction.baseUrl + "/api/78dk/app/bill/getMyBill"
    LOGGER.info("我的账单v1.0.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["billDate"] = billdate
    params["contractUuid"] = contractuuid
    my_API_TEST_HEADERS = copy.deepcopy(AppAction.API_TEST_HEADERS)
    LOGGER.info("我的账单v1.0.0请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("我的账单v1.0.0请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_urge_addMessage(communicatee, condition, datalist, overduereason, remark, replyrepaytime,
                                           useruuid):
    """
    电话催收信息提交-v1.5.2
    :param useruuid: 客户UUID,string
    :param remark: 备注,string
    :param datalist: 文件,array<object>
    :param replyrepaytime: 承诺还款时间,string
    :param condition: 沟通情况,string
    :param overduereason: 逾期原因,string
    :param communicatee: 沟通对象,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2126')
    requesturl = WebAction.baseUrl + "/api/78dk/platform/urge/addMessage"
    LOGGER.info("电话催收信息提交-v1.5.2请求地址:【{}】".format(requesturl))
    params = dict()
    params["communicatee"] = communicatee
    params["condition"] = condition
    params["dataList"] = datalist
    params["overdueReason"] = overduereason
    params["remark"] = remark
    params["replyRepayTime"] = replyrepaytime
    params["userUuid"] = useruuid
    my_API_TEST_HEADERS = copy.deepcopy(WebAction.API_TEST_HEADERS)
    LOGGER.info("电话催收信息提交-v1.5.2请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("电话催收信息提交-v1.5.2请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=params, headers=my_API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2828')
    requesturl = AppAction.baseUrl + "/api/78dk/app/process/centerCallback"
    LOGGER.info("爬虫接口中心回调请求地址:【{}】".format(requesturl))
    params = dict()
    params["data"] = data
    params["message"] = message
    params["result"] = result
    params["task_id"] = task_id
    params["timestamp"] = timestamp
    params["type"] = type
    params["user_id"] = user_id
    LOGGER.info("爬虫接口中心回调请求头参数：【{}】".format(AppAction.API_TEST_HEADERS))
    LOGGER.info("爬虫接口中心回调请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=AppAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 201, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text