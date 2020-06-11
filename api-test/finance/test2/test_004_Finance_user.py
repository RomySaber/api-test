#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-17 下午 5:20
@Author     : 罗林
@File       : test_004_Finance_user.py
@desc       :  用户管理自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import FinanceSql
from finance.testAction import FinanceAction
from finance.testAction import loginAction

fake = Faker(locale='zh_CN')
user_name = fake.company_prefix() + loginAction.sign
phone = fake.phone_number()
email = loginAction.sign + fake.email()


class test_004_Finance_user(TestBaseCase):
    def test_001_userManage_getUsers(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword='')
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'account')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'name')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'phone')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'email')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'orgName')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'role')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'statusCode')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'status')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'canLock')

    def test_002_userManage_getCreateUserInitData(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :新增用户基础数据获取
        """
        rs1 = FinanceAction.test_userManage_getCreateUserInitData()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'description')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'name')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'orgCode')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'parentId')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'checked')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'roleName')

    def test_003_userManage_saveUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :新增用户基础数据获取
        """
        global role_id, org_code, org_code_one
        role_id = loginAction.global_dict.get("role_id")
        org_code = loginAction.global_dict.get("org_code")
        org_code_one = loginAction.global_dict.get("org_code_one")
        rs1 = FinanceAction.test_userManage_saveUser(
            phone=phone, userid='', name=user_name, roleid=role_id, orgcode=org_code, email=email)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_004_userManage_getUsers_two(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword='')
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'account')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'name')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'phone')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'email')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'orgName')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'role')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'statusCode')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'status')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'canLock')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'canLock')
        Assertion.verityContain(json.loads(rs1)['data']['record'], user_name)

    def test_005_userManage_getUsers_search(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword=user_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        global user_id
        user_id = json.loads(rs1)['data']['record'][0]['id']
        Assertion.verity(json.loads(rs1)['data']['record'][0]['account'], phone)
        Assertion.verity(json.loads(rs1)['data']['record'][0]['email'], email)
        Assertion.verity(json.loads(rs1)['data']['record'][0]['name'], user_name)
        Assertion.verity(json.loads(rs1)['data']['record'][0]['phone'], phone)
        Assertion.verity(json.loads(rs1)['data']['record'][0]['status'], '未激活')
        Assertion.verity(json.loads(rs1)['data']['record'][0]['statusCode'], 0)
        Assertion.verity(json.loads(rs1)['data']['record'][0]['canLock'], True)

    def test_006_userManage_getUserDetailByid(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :编辑页面数据获取
        """
        rs1 = FinanceAction.test_userManage_getUserDetailByid(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['email'], email)
        Assertion.verity(json.loads(rs1)['data']['id'], user_id)
        Assertion.verity(json.loads(rs1)['data']['name'], user_name)
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code)
        Assertion.verity(json.loads(rs1)['data']['phone'], phone)
        Assertion.verity(json.loads(rs1)['data']['roleId'], int(role_id))
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'count')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'description')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'dto')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'name')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'offLineCount')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'onLineCount')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'orgCode')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'parentId')
        Assertion.verityContain(json.loads(rs1)['data']['orgs'], 'parentName')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'checked')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['roles'], 'roleName')

    def test_007_userManage_modifyUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :编辑页面数据获取
        """
        rs1 = FinanceAction.test_userManage_modifyUser(
            email=email, roleid=role_id, name=user_name, orgcode=org_code, userid=user_id, phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data'], '用户信息修改成功！')

    def test_008_user_showPassword(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :finance查看用户密码
        """
        rs1 = FinanceAction.test_user_showPassword(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['id'], user_id)
        Assertion.verity(json.loads(rs1)['data']['phone'], phone)
        Assertion.verity(json.loads(rs1)['data']['pwd'], FinanceSql.get_user_passwd(user_id))

    def test_009_user_activation(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       : 激活用户
        """
        rs1 = FinanceAction.test_user_activation(
            pwd=loginAction.financePasswd, phone=phone, security=FinanceSql.get_user_passwd(user_id))
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_010_activate_user(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       : 激活用户
        """
        FinanceSql.activate_user(user_id)

    def test_011_user_login(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :用户登陆
        """
        rs1 = FinanceAction.test_user_login(password=loginAction.financePasswd, username=phone)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_012_userManage_getPersonalmsg(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取登陆用户信息
        """
        rs1 = FinanceAction.test_userManage_getPersonalmsg(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_013_userManage_getUsers_search_two(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword=user_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        for i in range(len(json.loads(rs1)['data']['record'])):
            if json.loads(rs1)['data']['record'][i]['id'] == user_id:
                Assertion.verity(json.loads(rs1)['data']['record'][i]['status'], '正常')

    def test_014_userManage_lockUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :锁定一个用户
        """
        rs1 = FinanceAction.test_userManage_lockUser(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data'], user_id)

    def test_015_userManage_getUsers_search_thr(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword=user_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        for i in range(len(json.loads(rs1)['data']['record'])):
            if json.loads(rs1)['data']['record'][i]['id'] == user_id:
                Assertion.verity(json.loads(rs1)['data']['record'][i]['status'], '被锁定')

    def test_016_userManage_unlockUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :解锁一个用户
        """
        rs1 = FinanceAction.test_userManage_unlockUser(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data'], user_id)

    def test_017_userManage_getUsers_search_four(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword=user_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        for i in range(len(json.loads(rs1)['data']['record'])):
            if json.loads(rs1)['data']['record'][i]['id'] == user_id:
                Assertion.verity(json.loads(rs1)['data']['record'][i]['status'], '正常')

    def test_018_userManage_deleteUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :删除用户
        """
        rs1 = FinanceAction.test_userManage_deleteUser(user_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_019_userManage_getUsers_search_five(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :系统用户列表
        """
        rs1 = FinanceAction.test_userManage_getUsers(pagenum=1, pagesize=10, keyword='')
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verityNotContain(json.loads(rs1)['data'], user_name)

    def test_020_user_getMessageCount(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取用户的提示消息数量
        """
        rs1 = FinanceAction.test_user_getMessageCount()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_021_user_getWarnManner(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :查询消息推送设置
        """
        rs1 = FinanceAction.test_user_getWarnManner()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        global manner_data
        manner_data = json.loads(rs1)['data']
        Assertion.verityContain(json.loads(rs1)['data'], 'warnManner')
        Assertion.verityContain(json.loads(rs1)['data'], 'code')
        Assertion.verityContain(json.loads(rs1)['data'], 'name')
        Assertion.verityContain(json.loads(rs1)['data'], 'push')
        Assertion.verityContain(json.loads(rs1)['data'], 'warnType')
        Assertion.verityContain(json.loads(rs1)['data'], 'warnTypeName')

    def test_022_user_saveWarnManner(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :保存报警设置
        """
        manners = list()
        for m_data in manner_data:
            manner = {"id": m_data['id'], "warnManner": "Html,App,SMS", "warnType": m_data['warnType'],
                      "warnTypeName": m_data["warnTypeName"], "mannerName": "网页提醒,app提醒,短信提醒"}
            manners.append(manner)
        rs1 = FinanceAction.test_user_saveWarnManner(manners=manners)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
    #
    # def test_023_user_updatePassword(self):
    #     """
    #     Time       :2019-06-18
    #     author     : 罗林
    #     desc       :用户修改密码
    #     """
    #     rs1 = FinanceAction.test_user_updatePassword(
    #         oldpassword=loginAction.financePasswd, newpassword=loginAction.financePasswd)
    #     Assertion.verity(json.loads(rs1)['code'], 'F2000')
    #     Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_024_user_getMoudels(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :模块权限
        """
        rs1 = FinanceAction.test_user_getMoudels()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_025_user_getMessages_all(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取用户的提示消息
        """
        rs1 = FinanceAction.test_user_getMessages(page=1, orgcode=org_code_one, begin='', keywords='', size=10, status=2)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_026_user_getMessages_read(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取用户的提示消息
        """
        rs1 = FinanceAction.test_user_getMessages(page=1, orgcode=org_code_one, begin='', keywords='', size=10, status=1)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_027_user_getMessages_not_read(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取用户的提示消息
        """
        rs1 = FinanceAction.test_user_getMessages(page=1, orgcode=org_code_one, begin='', keywords='', size=10, status=0)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
    #
    # def test_028_user_readMessage(self):
    #     """
    #     Time       :2019-06-18
    #     author     : 罗林
    #     desc       :将用户的消息设置为已读
    #     """
    #     rs1 = FinanceAction.test_user_readMessage(messageid='')
    #     Assertion.verity(json.loads(rs1)['code'], 'F2000')
    #     Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_029_user_getUser(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取登陆用户信息
        """
        rs1 = FinanceAction.test_user_getUser()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['email'], loginAction.financeUser)
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code_one)
