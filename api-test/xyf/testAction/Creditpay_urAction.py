#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : Creditpay_urAction.py
@desc       : 项目：xyf 模块：creditpay_ur 接口方法封装
"""

from xyf.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('creditpay_ur_apiURL', 'xyf')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_creditpay_ur_login()
API_TEST_HEADERS['myToken'] = LICENCES


def test_ui_user_findUserBill(cardno, currentpage, loantimebegin, loantimeend, pagesize, phone, realname, shouldrepaymentbegin, shouldrepaymentend, stage):
    """
    逾期用户-列表4.0.3.1
    :param loantimeend: 贷款结束日期,
    :param cardno: 身份证,
    :param loantimebegin: 贷款开始日期,
    :param phone: 电话,
    :param shouldrepaymentbegin: 应还开始时间,
    :param shouldrepaymentend: 应还结束时间,
    :param stage: 阶段,
    :param realname: 用户名字,
    :param pagesize: 一页数据条数,
    :param currentpage: 页码,
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2632')
    requesturl = baseUrl + "/ui/user/findUserBill"
    LOGGER.info("逾期用户-列表4.0.3.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["cardNo"] = cardno
    params["currentPage"] = currentpage
    params["loanTimeBegin"] = loantimebegin
    params["loanTimeEnd"] = loantimeend
    params["pageSize"] = pagesize
    params["phone"] = phone
    params["realName"] = realname
    params["shouldRepaymentBegin"] = shouldrepaymentbegin
    params["shouldRepaymentEnd"] = shouldrepaymentend
    params["stage"] = stage
    LOGGER.info("逾期用户-列表4.0.3.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("逾期用户-列表4.0.3.1请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_ui_user_getUserInfo(userid):
    """
    用户信息-4.0.3.1
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 2633')
    requesturl = baseUrl + "/ui/user/getUserInfo"
    LOGGER.info("用户信息-4.0.3.1请求地址:【{}】".format(requesturl))
    params = dict()
    params["userId"] = userid
    LOGGER.info("用户信息-4.0.3.1请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户信息-4.0.3.1请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


