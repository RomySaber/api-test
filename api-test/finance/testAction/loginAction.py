#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/18 0018 上午 11:33
@Author     : 罗林
@File       : loginAction.py
@desc       :  获取登录信息
"""

import hashlib, requests

import os

from common.myCommon.GlobalDict import GlobalDict
from common.myCommon.Logger import getlog
from common.myConfig import MysqlConfig as ms
from common.myConfig import ConfigUtils as conf


financeUser = 'luolin@78dk.com'
financePasswd = '12345678'
manageUser = 'hejuncheng@78dk.com'
managePasswd = '12345678'
finance_URL = ms.get('finance_apiURL', 'finance')
manage_URL = ms.get('manage_apiURL', 'finance')
clapp_URL = ms.get('clapp_apiURL', 'finance')
LOGGER = getlog(__name__)
API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}
rq = requests.Session()
sign = conf.get('report', 'sign')
companyName = '富勤金融'
global_dict = GlobalDict(os.path.dirname(__file__), 'finance_data')


def test_finance_login():
    # 获取finance登录后的licences
    url = finance_URL + '/user/login'
    querystring = {"userName": financeUser, "password": financePasswd}
    response = rq.post(url, headers=API_TEST_HEADERS, params=querystring)
    LOGGER.info("licences:【{}】".format(response.json()["data"]["licences"]))
    return response.json()["data"]["licences"]


def test_manage_login():
    # 获取manage登录后的licence
    url = manage_URL + '/login'
    querystring = {"account": manageUser, "password": managePasswd}
    response = rq.post(url, headers=API_TEST_HEADERS, params=querystring)
    LOGGER.info("licences:【{}】".format(response.json()["data"]["licence"]))
    return response.json()["data"]["licence"]


def test_clapp_login():
    # app 登录，返回token
    url = clapp_URL + '/login'
    md5str = ''
    seq = {"appversion": "", "deviceversion": "", "phone": financeUser, "pwd": financePasswd,
           "signature": md5str, "sysname": "", "sysversion": "", "uuid": ""}
    querystring = getsignature(seq)
    print(seq)
    response = rq.post(url, headers=API_TEST_HEADERS, params=querystring)
    print(response.text)
    LOGGER.info("token:【{}】".format(response.json()["data"]["token"]))
    return response.json()["data"]["token"]


def getsignature(querystring):
    #  获取APP的 参数签名
    if 'signature' in querystring:
        del querystring['signature']
    seq = []
    for k, v in querystring.items():
        str1 = '{0}={1}'.format(k, v)
        seq.append(str1)
    # 对list排序
    seq.sort()
    # 转换字符串并添加md5值
    signature_str = '&'.join(seq) + '6156731e7d6f4447b63b7fa3bac246cb'
    LOGGER.debug("请求参数格式化：【{}】".format(signature_str))
    # 获取字符串MD5
    md5str = hashlib.md5(signature_str.encode("utf-8")).hexdigest()
    querystring['signature'] = md5str
    return querystring


def test_cldp_login():
    pass


def test_applicationserver_login():
    pass


if __name__ == '__main__':
    test_finance_login()
