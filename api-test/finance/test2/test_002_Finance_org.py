#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-17 下午 5:19
@Author     : 罗林
@File       : test_002_Finance_org.py
@desc       :  org机构管理自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import FinanceAction
from finance.testAction import loginAction

fake = Faker(locale='zh_CN')
org_name = fake.company_prefix() + loginAction.sign
del_org_name = fake.company_prefix() + loginAction.sign


class test_002_Finance_org(TestBaseCase):
    def test_001_org_getOrgs(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_getOrgs()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_002_org_getCurrentOrgs(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_getCurrentOrgs()
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        global org_id_one
        org_id_one = json.loads(rs1)['data'][0]['orgId']
        global org_code_one
        org_code_one = json.loads(rs1)['data'][0]['orgCode']
        loginAction.global_dict.set(org_code_one=json.loads(rs1)['data'][0]['orgCode'])

    def test_003_org_addOrg(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_addOrg(
            description='', onlinecount='', count='', orgcode=org_code_one, offlinecount='', parentname='', id='',
            dto='', name=org_name, parentid=org_id_one)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        global org_id
        org_id = json.loads(rs1)['data']['id']
        global org_code
        org_code = json.loads(rs1)['data']['orgCode']
        loginAction.global_dict.set(org_code=json.loads(rs1)['data']['orgCode'])

    def test_004_org_addOrg_del_org(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_addOrg(
            description='', onlinecount='', count='', orgcode=org_code_one, offlinecount='', parentname='', id='',
            dto='', name=del_org_name, parentid=org_id_one)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        global del_org_id
        del_org_id = json.loads(rs1)['data']['id']

    def test_005_org_updateOrg(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_updateOrg(
            description=''.join(fake.words(nb=127)), onlinecount='', count='', orgcode=org_code, offlinecount='',
            parentname='', id=org_id, dto='', name=org_name, parentid=org_id_one)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['id'], org_id)
        Assertion.verity(json.loads(rs1)['data']['name'], org_name)
        Assertion.verity(json.loads(rs1)['data']['parentId'], org_id_one)

    def test_006_org_delete(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取当前用户能操作的组织机构
        """
        rs1 = FinanceAction.test_org_delete(del_org_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
