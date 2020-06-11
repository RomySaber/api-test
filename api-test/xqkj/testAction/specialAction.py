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
from requests_toolbelt.multipart.encoder import MultipartEncoder

from common.myCommon import Assertion
from common.myCommon import TimeFormat
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent as ms
from xqkj.testAction import PmsAction
from xqkj.testAction import ShtAction
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction

LOGGER = getlog(__name__)
rq = requests.Session()


def test_api_78dk_platform_sys_privilege_saveUserPrivilege(params):
    """
    新增/修改权限
    platform_privilege_uuid = [
            {"platformPrivilegeUuid": platform_privilege_uuid0, "platformUserUuid": platform_user_profile_uuid},
            {"platformPrivilegeUuid": platform_privilege_uuid1, "platformUserUuid": platform_user_profile_uuid}]
    """
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 911')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
    PlatformAction.LOGGER.info("新增/修改权限请求地址:【{}】".format(requesturl))
    PlatformAction.LOGGER.info("新增/修改权限请求参数：【{}】".format(params))
    response = PlatformAction.rq.post(requesturl, data=json.dumps(params), headers=PlatformAction.API_TEST_HEADERS)
    PlatformAction.LOGGER.info("请求结果参数：【{}】".format(response.text))
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 866')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
    PlatformAction.LOGGER.info("保存商户贴息请求地址:【{}】".format(requesturl))
    PlatformAction.LOGGER.info("保存商户贴息请求参数：【{}】".format(params))
    response = PlatformAction.rq.post(requesturl, data=str(params), headers=PlatformAction.API_TEST_HEADERS)
    PlatformAction.LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    return response.text


def test_backstage_system_permission_set(id, permissions):
    """
    权限编辑接口
    :param id: 业务系统id,number
    :param permissions: 系统权限,array<object>
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1224')
    requesturl = PmsAction.baseUrl + "/backstage/system/permission/set"
    LOGGER.info("权限编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["permissions"] = permissions
    LOGGER.info("权限编辑接口请求头参数：【{}】".format(PmsAction.API_TEST_HEADERS))
    LOGGER.info("权限编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=PmsAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_system_config_set(id, configs):
    """
    配置编辑接口
    :param id: 业务系统id,number
    :param configs: 系统配置,array<object>
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1254')
    requesturl = PmsAction.baseUrl + "/backstage/system/config/set"
    LOGGER.info("配置编辑接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["id"] = id
    params["configs"] = configs
    LOGGER.info("配置编辑接口请求头参数：【{}】".format(PmsAction.API_TEST_HEADERS))
    LOGGER.info("配置编辑接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=PmsAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_permission_set(permissions, id):
    """
    机构权限设置接口
    :param permissions: 权限列表,array<string>
    :param id: 机构id,number
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1234')
    requesturl = PmsAction.baseUrl + "/backstage/tenant_permission/set"
    LOGGER.info("机构权限设置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["permissions"] = permissions
    params["id"] = id
    payload = """
    ------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; 
    name=\"id\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\n
    Content-Disposition: form-data; name=\"permissions\"\r\n\r\n
    {}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--
    """.format(params["id"], ','.join(params["permissions"]))
    my_API_TEST_HEADERS = copy.deepcopy(PmsAction.API_TEST_HEADERS)
    my_API_TEST_HEADERS["Content-Type"] = "multipart/`; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
    LOGGER.info("机构权限设置接口请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("机构权限设置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=payload, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_backstage_tenant_config_set(configs, id):
    """
    机构配置设置接口
    :param configs: 配置集合,array<object>
    :param id: 机构Id,number
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1237')
    requesturl = PmsAction.baseUrl + "/backstage/tenant_config/set"
    LOGGER.info("机构配置设置接口请求地址:【{}】".format(requesturl))
    params = dict()
    params["configs"] = configs
    params["id"] = id
    LOGGER.info("机构配置设置接口请求头参数：【{}】".format(PmsAction.API_TEST_HEADERS))
    LOGGER.info("机构配置设置接口请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=PmsAction.API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1302')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/tm/first/showSupplementImage"
    LOGGER.info("展示补录的图片资料 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = PlatformAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(PlatformAction.API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1299')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/tm/first/xuexinreport"
    LOGGER.info("学信网报告 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = PlatformAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(PlatformAction.API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1298')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/tm/first/businessbillinginformation"
    LOGGER.info("商户结算信息查询接口 - V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = PlatformAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(PlatformAction.API_TEST_HEADERS)
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
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1303')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/tm/first/queryElectronuclearRemark"
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求地址:【{}】".format(requesturl))
    params = dict()
    params["contractUuid"] = contractuuid
    params["MyToken"] = PlatformAction.LICENCES
    my_API_TEST_HEADERS = copy.deepcopy(PlatformAction.API_TEST_HEADERS)
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求头参数：【{}】".format(my_API_TEST_HEADERS))
    LOGGER.info("电核备注 - 查询接口 V1.3 新增请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=my_API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_tm_operate_downOperationalCheck(begindate, enddate, name, phone, state, uuid):
    """
    运营列表导出-v1.4.0
    :param begindate: 开始时间,string
    :param enddate: 结束时间,string
    :param name: 姓名,string
    :param phone: 电话,string
    :param state: 状态,string
    :param uuid: 合同编号,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1376')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/tm/operate/downOperationalCheck"
    LOGGER.info("运营列表导出-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["begindate"] = begindate
    params["enddate"] = enddate
    params["name"] = name
    params["phone"] = phone
    params["state"] = state
    params["uuid"] = uuid
    params["MyToken"] = PlatformAction.LICENCES
    LOGGER.info("运营列表导出-v1.4.0请求头参数：【{}】".format(PlatformAction.API_TEST_HEADERS))
    LOGGER.info("运营列表导出-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=PlatformAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_repayment_downRepaymentList(applyoptname, auditoptname, auditstate, contractnumber,
                                                          lastpaydatebegintime, lastpaydateendtime, overduestate,
                                                          paystate, usermobile, username):
    """
    还款列表导出-v1.4.0
    :param applyoptname: 提交人,string
    :param auditoptname: 审核人,string
    :param auditstate: 审核状态,string
    :param contractnumber: 订单编号,string
    :param lastpaydatebegintime: 开始时间,string
    :param lastpaydateendtime: 结束时间,string
    :param overduestate: 逾期状态,string
    :param paystate: 还款状态,string
    :param usermobile: 手机号,string
    :param username: 借款人,string
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1375')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/om/repayment/downRepaymentList"
    LOGGER.info("还款列表导出-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["applyOptName"] = applyoptname
    params["auditOptName"] = auditoptname
    params["auditState"] = auditstate
    params["contractNumber"] = contractnumber
    params["lastPayDateBeginTime"] = lastpaydatebegintime
    params["lastPayDateEndTime"] = lastpaydateendtime
    params["overdueState"] = overduestate
    params["payState"] = paystate
    params["userMobile"] = usermobile
    params["userName"] = username
    params["MyToken"] = PlatformAction.LICENCES
    LOGGER.info("还款列表导出-v1.4.0请求头参数：【{}】".format(PlatformAction.API_TEST_HEADERS))
    LOGGER.info("还款列表导出-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=PlatformAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_om_contract_downContracts(orderstate, enddate, name, begindate):
    """
    导出申请列表-v1.4.0
    :param orderstate: 订单状态,string
    :param enddate: 结束时间,number
    :param name: 组合查询字段,string
    :param begindate: 开始时候,number
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 969')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/om/contract/downContracts"
    LOGGER.info("导出申请列表-v1.4.0请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderState"] = orderstate
    params["enddate"] = enddate
    params["name"] = name
    params["begindate"] = begindate
    params["MyToken"] = PlatformAction.LICENCES
    LOGGER.info("导出申请列表-v1.4.0请求头参数：【{}】".format(PlatformAction.API_TEST_HEADERS))
    LOGGER.info("导出申请列表-v1.4.0请求参数：【{}】".format(params))
    response = rq.get(requesturl, params=params, headers=PlatformAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_store_saveStoreImg(storeuuid, key, image_path):
    """
    保存单张图片
    :param storeuuid: 门店UUID
    :param key: 图片分类
    :param image_path: 图片地址
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1390')
    requesturl = ShtAction.baseUrl + "/api/78dk/sht/store/saveStoreImg"
    LOGGER.info("保存单张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["storeUuid"] = storeuuid
    params["key"] = key
    params["token"] = ShtAction.LICENCES
    fl = open(image_path, 'rb')
    API_TEST_HEADERS = {"Cache-Control": "no-cache"}
    multipart_encoder = MultipartEncoder(
        fields={'file': (image_path, fl, 'image/jpg'), 'key': key, 'token': ShtAction.LICENCES},
        boundary=TimeFormat.get_now_time_13())
    API_TEST_HEADERS['Content-Type'] = multipart_encoder.content_type
    API_TEST_HEADERS['token'] = ShtAction.LICENCES
    LOGGER.info("保存单张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("保存单张图片请求参数：【{0}】，请求文件地址：【{1}】".format(params, image_path))
    response = rq.post(requesturl, params=params, data=multipart_encoder, headers=API_TEST_HEADERS)
    fl.close()
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_sht_mm_saveMerchantImg(uuid, key, image_path):
    """
    商户通商户信息接口，保存单张图片
    :param uuid: 商户UUID
    :param key: 图片分类
    :param image_path: 图片地址
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1401')
    requesturl = ShtAction.baseUrl + "/api/78dk/sht/mm/saveMerchantImg"
    LOGGER.info("商户通商户信息接口，保存单张图片请求地址:【{}】".format(requesturl))
    params = dict()
    params["uuid"] = uuid
    params["key"] = key
    params["token"] = ShtAction.LICENCES
    fl = open(image_path, 'rb')
    API_TEST_HEADERS = {"Cache-Control": "no-cache"}
    multipart_encoder = MultipartEncoder(
        fields={'file': (image_path, fl, 'image/jpg'), 'key': key, 'token': ShtAction.LICENCES},
        boundary=TimeFormat.get_now_time_13())
    API_TEST_HEADERS['Content-Type'] = multipart_encoder.content_type
    API_TEST_HEADERS['token'] = ShtAction.LICENCES
    LOGGER.info("商户通商户信息接口，保存单张图片请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("商户通商户信息接口，保存单张图片请求参数：【{0}】，请求文件地址：【{1}】".format(params, image_path))
    response = rq.post(requesturl, params=params, data=multipart_encoder, headers=API_TEST_HEADERS)
    fl.close()
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_platform_mm_saveContractImages(images):
    """
    影像资料保存-v1.4
    :param images: 图片数组,array<object>
    :return: response.text
    """
    start_time = time.time()
    ms.update(ms.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 882')
    requesturl = PlatformAction.baseUrl + "/api/78dk/platform/mm/saveContractImages"
    LOGGER.info("影像资料保存-v1.4请求地址:【{}】".format(requesturl))
    LOGGER.info("影像资料保存-v1.4请求头参数：【{}】".format(PlatformAction.API_TEST_HEADERS))
    LOGGER.info("影像资料保存-v1.4请求参数：【{}】".format(images))
    response = rq.post(requesturl, data=json.dumps(images), headers=PlatformAction.API_TEST_HEADERS)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text
