#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Gw_webAction.py
@desc       : 项目：gw 模块：gw_web 接口方法封装
"""

import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('gw_web_apiURL', 'gw')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


def test_api_78dk_admin_login_pwLogin(loginname, password):
    """
    帐号登陆
    :param loginname: 登陆名称(Y),string
    :param password: 登陆密码(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1154')
    requesturl = baseUrl + "/api/78dk/admin/login/pwLogin"
    LOGGER.info("帐号登陆请求地址:【{}】".format(requesturl))
    params = dict()
    params["loginName"] = loginname
    params["password"] = password
    LOGGER.info("帐号登陆请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("帐号登陆请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_sys_updatePassword(newpassword, oldpassword):
    """
    修改密码
    :param newpassword: 新密码,string
    :param oldpassword: 旧密码,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1155')
    requesturl = baseUrl + "/api/78dk/admin/sys/updatePassword"
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


def test_api_78dk_admin_busiInfo_queryHCKJPage(companyname, currentpage, enddate, name, pagesize, phone, startdate, userscenario):
    """
    好车科技
    :param companyname: 公司名称,string
    :param currentpage: 当前页码(Y),number
    :param enddate: 结束时间(时间戳),number
    :param name: 姓名,string
    :param pagesize: 单页记录数(Y),number
    :param phone: 电话,string
    :param startdate: 开始时间(时间戳),number
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1156')
    requesturl = baseUrl + "/api/78dk/admin/busiInfo/queryHCKJPage"
    LOGGER.info("好车科技请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["name"] = name
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["startDate"] = startdate
    params["userScenario"] = userscenario
    LOGGER.info("好车科技请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("好车科技请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_busiInfo_queryXQXYPage(companyname, currentpage, enddate, name, pagesize, phone, startdate, userscenario):
    """
    小启信用
    :param companyname: 公司名称,string
    :param currentpage: 当前页码(Y),number
    :param enddate: 结束时间(时间戳),number
    :param name: 姓名,string
    :param pagesize: 单页记录数(Y),number
    :param phone: 电话,string
    :param startdate: 开始时间(时间戳),number
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1157')
    requesturl = baseUrl + "/api/78dk/admin/busiInfo/queryXQXYPage"
    LOGGER.info("小启信用请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["name"] = name
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["startDate"] = startdate
    params["userScenario"] = userscenario
    LOGGER.info("小启信用请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启信用请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_busiInfo_queryXQKCPage(companyname, currentpage, enddate, name, pagesize, phone, startdate, userscenario):
    """
    小启控车
    :param companyname: 公司名称,string
    :param currentpage: 当前页码(Y),number
    :param enddate: 结束时间(时间戳),number
    :param name: 姓名,string
    :param pagesize: 单页记录数(Y),number
    :param phone: 电话,string
    :param startdate: 开始时间(时间戳),number
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1158')
    requesturl = baseUrl + "/api/78dk/admin/busiInfo/queryXQKCPage"
    LOGGER.info("小启控车请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["name"] = name
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["startDate"] = startdate
    params["userScenario"] = userscenario
    LOGGER.info("小启控车请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启控车请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_busiInfo_queryXQJRYPage(companyname, currentpage, enddate, name, pagesize, phone, startdate, userscenario):
    """
    小启金融云
    :param companyname: 公司名称,string
    :param currentpage: 当前页码(Y),number
    :param enddate: 结束时间(时间戳),number
    :param name: 姓名,string
    :param pagesize: 单页记录数(Y),number
    :param phone: 电话,string
    :param startdate: 开始时间(时间戳),number
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1159')
    requesturl = baseUrl + "/api/78dk/admin/busiInfo/queryXQJRYPage"
    LOGGER.info("小启金融云请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["currentPage"] = currentpage
    params["endDate"] = enddate
    params["name"] = name
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["startDate"] = startdate
    params["userScenario"] = userscenario
    LOGGER.info("小启金融云请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("小启金融云请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_busiInfo_exportExcel(companyname, enddate, name, phone, productcode, startdate, userscenario):
    """
    导出数据
    :param companyname: 公司名称,string
    :param enddate: 结束时间(时间戳),number
    :param name: 姓名,string
    :param phone: 电话,string
    :param productcode: 产品code编码（Y）,string
    :param startdate: 开始时间(时间戳),number
    :param userscenario: 用户场景,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1160')
    requesturl = baseUrl + "/api/78dk/admin/busiInfo/exportExcel"
    LOGGER.info("导出数据请求地址:【{}】".format(requesturl))
    params = dict()
    params["companyName"] = companyname
    params["endDate"] = enddate
    params["name"] = name
    params["phone"] = phone
    params["productCode"] = productcode
    params["startDate"] = startdate
    params["userScenario"] = userscenario
    LOGGER.info("导出数据请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("导出数据请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_articleInfo_getArticleInfoPage(articleclassify, articleinfostate, currentpage, pagesize, title):
    """
    文章分页列表
    :param articleclassify: 类型（1-行业新闻 2-网站公告）,string
    :param articleinfostate: 文章状态（0-已发布 1-未发布）,string
    :param currentpage: 当前页码,number
    :param pagesize: 单页记录数,number
    :param title: 标题,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1161')
    requesturl = baseUrl + "/api/78dk/admin/articleInfo/getArticleInfoPage"
    LOGGER.info("文章分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleClassify"] = articleclassify
    params["articleInfoState"] = articleinfostate
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["title"] = title
    LOGGER.info("文章分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_articleInfo_upSetArticleInfo(articleclassify, articleinfostate, articleinfouuid, autopublish, digest, futext, logourl, reprinturl, sourcetype, subtitle, tag, title, top, type, videointroduce, videourl):
    """
    新增/修改文章
    :param articleclassify: 文章分类（1-行业新闻 2-网站公告）,string
    :param articleinfostate: 文章状态（0-已发布 1-未发布）,string
    :param articleinfouuid: 文章uuid（修改文章才传）,string
    :param autopublish: 自动发布（0-是 1-否）,string
    :param digest: 摘要,string
    :param futext: 内容编辑（type=1才传）,string
    :param logourl: logo图片,string
    :param reprinturl: 转载源（source_type=2才有值）,string
    :param sourcetype: 来源（1-原创 2-转载）,string
    :param subtitle: 副标题,string
    :param tag: 标签(多个用逗号隔开),string
    :param title: 标题,string
    :param top: 是否置顶（0-是 1-否）,string
    :param type: 文章类型（1-图文 2-视频）,string
    :param videointroduce: 视频介绍（type=2才传）,string
    :param videourl: 视频地址(type=2才传),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1162')
    requesturl = baseUrl + "/api/78dk/admin/articleInfo/upSetArticleInfo"
    LOGGER.info("新增/修改文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleClassify"] = articleclassify
    params["articleInfoState"] = articleinfostate
    params["articleInfoUuid"] = articleinfouuid
    params["autoPublish"] = autopublish
    params["digest"] = digest
    params["fuText"] = futext
    params["logoUrl"] = logourl
    params["reprintUrl"] = reprinturl
    params["sourceType"] = sourcetype
    params["subTitle"] = subtitle
    params["tag"] = tag
    params["title"] = title
    params["top"] = top
    params["type"] = type
    params["videoIntroduce"] = videointroduce
    params["videoUrl"] = videourl
    LOGGER.info("新增/修改文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增/修改文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_articleInfo_getArticleInfo(articleinfouuid):
    """
    获取文章详情
    :param articleinfouuid: 文章uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1163')
    requesturl = baseUrl + "/api/78dk/admin/articleInfo/getArticleInfo"
    LOGGER.info("获取文章详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("获取文章详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取文章详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_articleInfo_delArticleInfo(articleinfouuid):
    """
    删除文章
    :param articleinfouuid: 文章uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1164')
    requesturl = baseUrl + "/api/78dk/admin/articleInfo/delArticleInfo"
    LOGGER.info("删除文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("删除文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_articleInfo_publishAndUnder(articleinfouuid, status):
    """
    发布/下架文章
    :param articleinfouuid: 文章uuid(Y),string
    :param status: 0-已发布 1-未发布,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1165')
    requesturl = baseUrl + "/api/78dk/admin/articleInfo/publishAndUnder"
    LOGGER.info("发布/下架文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    params["status"] = status
    LOGGER.info("发布/下架文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发布/下架文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_common_getQiNiuToken():
    """
    获取七牛token
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1166')
    requesturl = baseUrl + "/api/78dk/admin/common/getQiNiuToken"
    LOGGER.info("获取七牛token请求地址:【{}】".format(requesturl))
    params = dict()
    LOGGER.info("获取七牛token请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取七牛token请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_xqcArticleInfo_getArticleInfoPage(articleclassify, articleinfostate, currentpage, pagesize, title):
    """
    文章分页列表
    :param currentpage: 当前页码,number
    :param articleclassify: 类型（3-小启头条 4-网贷咨询 5-实时热点）,string
    :param title: 标题,string
    :param pagesize: 单页记录数,number
    :param articleinfostate: 文章状态（0-已发布 1-未发布）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1505')
    requesturl = baseUrl + "/api/78dk/admin/xqcArticleInfo/getArticleInfoPage"
    LOGGER.info("文章分页列表请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleClassify"] = articleclassify
    params["articleInfoState"] = articleinfostate
    params["currentPage"] = currentpage
    params["pageSize"] = pagesize
    params["title"] = title
    LOGGER.info("文章分页列表请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("文章分页列表请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_xqcArticleInfo_getArticleInfo(articleinfouuid):
    """
    获取文章详情
    :param articleinfouuid: 文章uuid,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1506')
    requesturl = baseUrl + "/api/78dk/admin/xqcArticleInfo/getArticleInfo"
    LOGGER.info("获取文章详情请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("获取文章详情请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("获取文章详情请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_xqcArticleInfo_delArticleInfo(articleinfouuid):
    """
    删除文章
    :param articleinfouuid: 文章uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1507')
    requesturl = baseUrl + "/api/78dk/admin/xqcArticleInfo/delArticleInfo"
    LOGGER.info("删除文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    LOGGER.info("删除文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("删除文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_xqcArticleInfo_publishAndUnder(articleinfouuid, status):
    """
    发布/下架文章
    :param status: 0-已发布 1-未发布,string
    :param articleinfouuid: 文章uuid(Y),string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1508')
    requesturl = baseUrl + "/api/78dk/admin/xqcArticleInfo/publishAndUnder"
    LOGGER.info("发布/下架文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleInfoUuid"] = articleinfouuid
    params["status"] = status
    LOGGER.info("发布/下架文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("发布/下架文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_api_78dk_admin_xqcArticleInfo_upSetArticleInfo(articleclassify, articleinfostate, articleinfouuid, autopublish, bannerurl, digest, futext, logourl, reprinturl, sourcetype, subtitle, tag, title, top, type, videointroduce, videourl, wheelplay):
    """
    新增/修改文章
    :param articleinfostate: 文章状态（0-已发布 1-未发布）,string
    :param reprinturl: 转载源（source_type=2才有值）,string
    :param tag: 标签(多个用逗号隔开),string
    :param videourl: 视频地址(type=2才传),string
    :param articleclassify: 类型（3-小启头条 4-网贷咨询 5-实时热点）,string
    :param articleinfouuid: 文章uuid（修改文章才传）,string
    :param autopublish: 自动发布（0-是 1-否）,string
    :param videointroduce: 视频介绍（type=2才传）,string
    :param logourl: logo图片,string
    :param title: 标题,string
    :param type: 文章类型（1-图文 2-视频）,string
    :param futext: 内容编辑（type=1才传）,string
    :param digest: 摘要,string
    :param sourcetype: 来源（1-原创 2-转载）,string
    :param subtitle: 副标题,string
    :param top: 是否置顶（0-是 1-否）,string
    :param bannerurl: 轮播图url（）,string
    :param bannerurl: 轮播图url,string
    :param wheelplay: 是否轮播（0-是 1-否）,string
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 1526')
    requesturl = baseUrl + "/api/78dk/admin/xqcArticleInfo/upSetArticleInfo"
    LOGGER.info("新增/修改文章请求地址:【{}】".format(requesturl))
    params = dict()
    params["articleClassify"] = articleclassify
    params["articleInfoState"] = articleinfostate
    params["articleInfoUuid"] = articleinfouuid
    params["autoPublish"] = autopublish
    params["bannerUrl"] = bannerurl
    params["digest"] = digest
    params["fuText"] = futext
    params["logoUrl"] = logourl
    params["reprintUrl"] = reprinturl
    params["sourceType"] = sourcetype
    params["subTitle"] = subtitle
    params["tag"] = tag
    params["title"] = title
    params["top"] = top
    params["type"] = type
    params["videoIntroduce"] = videointroduce
    params["videoUrl"] = videourl
    params["wheelPlay"] = wheelplay
    LOGGER.info("新增/修改文章请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("新增/修改文章请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


