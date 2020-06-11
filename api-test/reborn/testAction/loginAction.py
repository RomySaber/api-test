#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-03-20 下午 3:10
@Author     : 罗林
@File       : loginAction.py
@desc       : 
"""

import requests
import json
from common.myConfig import ConfigUtils as conf
from common.myConfig import MysqlConfig
from common.mydb import MysqlClent
from faker import Factory

fake = Factory().create('zh_CN')
nameadmin = fake.name_male() + 'stream管理员'
phoneadmin = fake.ean8()
emailadmin = fake.email()
phoneadmin = '135' + phoneadmin
DB = MysqlClent.get_conn('192.168.15.129', 3306, 'cgi78dkv23', 'cgi78dk', 'dfljlcl39*33$@e')
# baseUrl = "http://test.jtlservice.78dk.cgi78dkom"
baseUrl = MysqlConfig.get('platform_apiURL', 'reborn')
sign = conf.get('report', 'sign')


def login():
    # 管理员用户
    # 新增用户测试--非email
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    payload = {"email": "dd@78dk.com", "password": "1"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    token = r.json()['data']['token']
    API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache","mytoken": "{}".format(token)}
    # print(API_TEST_HEADERS)
    # 新增用户
    url = baseUrl + '/api/78dk/platform/sys/user/saveSystemUser'
    data = {"email":emailadmin,"mobile":phoneadmin,"name":nameadmin}
    requests.post(url, data=json.dumps(data), headers=API_TEST_HEADERS)
    # 权限
    url = baseUrl + '/api/78dk/platform/sys/privilege/saveUserPrivilege'
    sql = 'name="' + nameadmin + '" and state ="enabled"'
    userid = MysqlClent.select_one(DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
    data = [{"platformPrivilegeUuid":"1db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"6db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"7db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"8db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"2db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"11b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"10b0d9fb5d524a098810855385fb0001","platformUserUuid":userid},
    {"platformPrivilegeUuid":"9db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"10b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"3db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"12b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"4db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"13b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"14b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"5db0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"15b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"67b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"6db0d9fb5d524a098810855385fb0421","platformUserUuid":userid},
    {"platformPrivilegeUuid":"27b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"37b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"47b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"8db0d9fb5d524a098810855385fb0001","platformUserUuid":userid},
    {"platformPrivilegeUuid":"57b0d9fb5d524a098810855385fb042e","platformUserUuid":userid},
    {"platformPrivilegeUuid":"adb0d9fb5d524a098810855385fb0001","platformUserUuid":userid},
    {"platformPrivilegeUuid":"adb0d9fb5d524a098810855385fb0004","platformUserUuid":userid},
    {"platformPrivilegeUuid":"adb0d9fb5d524a098810855385fb0003","platformUserUuid":userid},
    {"platformPrivilegeUuid":"adb0d9fb5d524a098810855385fb0002","platformUserUuid":userid},
    {"platformPrivilegeUuid":"685424dff6b24278a77281f2367be331","platformUserUuid":userid},
    {"platformPrivilegeUuid":"02046fcfd57444adab4a00eacb821a52","platformUserUuid":userid}]  #预授信统计权限
    requests.post(url, data=json.dumps(data), headers=API_TEST_HEADERS)
    # 新用户重置密码
    url = baseUrl + '/api/78dk/platform/sys/user/updateUserPass'
    data = {"email": emailadmin, "password": '1', "passwordRepeat": '1', "uid": userid}
    requests.post(url, data=json.dumps(data), headers=API_TEST_HEADERS)
    # 新用户登录
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    payload = {"email":emailadmin,"password":"1"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    token = r.json()['data']['token']
    return token


def superadminlogin():
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    payload = {"email":"999@qq.com","password":"1"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    token = r.json()['data']['token']
    return token


# liaojie@hu.cn	云淑华stream管理员
def streamadminlogin():
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    payload = {"email":"dd@78dk.com","password":"1"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    token = r.json()['data']['token']
    return token


def test_platform_login():
    url = baseUrl + '/api/78dk/platform/sys/user/login'
    params = {"email": "dd@78dk.com", "password": "1"}
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(params), headers=headers)
    token = r.json()['data']['token']
    return token


def test_appserver_login():
    pass
    # url = base_url + '/api/78dk/platform/sys/user/login'
    # params = {"email": emailadmin, "password": "1"}
    # r = requests.post(url, data=params, headers=API_TEST_HEADERS)
    # return r.json()['data']['token']


def test_service_login():
    pass
