#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@Author     : QA 
@File       : AppAction.py
@desc       : 项目：financeCloud 模块：app 接口方法封装
"""

from financeCloud.testAction import loginAction
import requests, json, time
from common.myCommon import Assertion
from common.myConfig import ConfigUtils
from common.myCommon.Logger import getlog
from common.mydb import MysqlClent
from common.myConfig import MysqlConfig


TIMEOUT = ConfigUtils.getint('report', 'time_out')
baseUrl = MysqlConfig.get('app_apiURL', 'financeCloud')
LOGGER = getlog(__name__)
rq = requests.Session()
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
LICENCES = loginAction.test_app_login()


def test_order_takeGoods(orderid):
    """
    用户确认收货
    :param orderid: 订单id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3194')
    requesturl = baseUrl + "/order/takeGoods"
    LOGGER.info("用户确认收货请求地址:【{}】".format(requesturl))
    params = dict()
    params["orderId"] = orderid
    LOGGER.info("用户确认收货请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("用户确认收货请求参数：【{}】".format(params))
    response = rq.get(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepayOnline_submit(billid, cardid, repayamount, repaytime, sourcepackage, type, userid):
    """
    线上还款申请
    :param userid: 用户id,number
    :param billid: 账单id，多条账单id用逗号分隔（月账单为空）,string
    :param cardid: 银行卡id,number
    :param repayamount: 还款金额,number
    :param repaytime: 还款时间,string
    :param sourcepackage: 1表示还当前剩余应还，2表示从【未出账单】中进入还款（普通账单为空）,number
    :param type: 还款类型、1普通账单 2月账单,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3271')
    requesturl = baseUrl + "/repay/accountrepayOnline/submit"
    LOGGER.info("线上还款申请请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["cardId"] = cardid
    params["repayAmount"] = repayamount
    params["repayTime"] = repaytime
    params["sourcePackage"] = sourcepackage
    params["type"] = type
    params["userId"] = userid
    LOGGER.info("线上还款申请请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线上还款申请请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


def test_repay_accountrepayOnline_callback(billid, cardid, issuccess, repayamount, sourcepackage, type, userid):
    """
    线上还款回调
    :param billid: 账单id,账单id，多条账单id用逗号分隔（月账单为空）,string
    :param cardid: 银行卡id,number
    :param issuccess: 还款是否成功（1成功，2失败）,number
    :param repayamount: 还款金额,number
    :param sourcepackage: 1表示还当前剩余应还，2表示从【未出账单】中进入还款（普通账单为空）,number
    :param type: 还款类型、1普通账单 2月账单,number
    :param userid: 用户id,number
    :return: response.text
    """
    start_time = time.time()
    MysqlClent.update(MysqlClent.get_conn(), 't_rap', 'is_exe = "Y"', 'id = 3272')
    requesturl = baseUrl + "/repay/accountrepayOnline/callback"
    LOGGER.info("线上还款回调请求地址:【{}】".format(requesturl))
    params = dict()
    params["billId"] = billid
    params["cardId"] = cardid
    params["isSuccess"] = issuccess
    params["repayAmount"] = repayamount
    params["sourcePackage"] = sourcepackage
    params["type"] = type
    params["userId"] = userid
    LOGGER.info("线上还款回调请求头参数：【{}】".format(API_TEST_HEADERS))
    LOGGER.info("线上还款回调请求参数：【{}】".format(params))
    response = rq.post(requesturl, data=json.dumps(params), headers=API_TEST_HEADERS, timeout=TIMEOUT)
    LOGGER.info("请求结果参数：【{}】".format(response.text))
    Assertion.verity(response.status_code, 200, "状态码检查")
    LOGGER.info("请求接口耗时：【{}】".format(time.time() - start_time))
    return response.text


