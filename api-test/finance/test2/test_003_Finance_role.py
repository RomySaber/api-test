#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-17 下午 5:20
@Author     : 罗林
@File       : test_003_Finance_role.py
@desc       :  角色管理自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import FinanceSql
from finance.testAction import FinanceAction
from finance.testAction import loginAction

fake = Faker(locale='zh_CN')
org_name = fake.company_prefix() + loginAction.sign
del_org_name = fake.company_prefix() + loginAction.sign

role_name = fake.word() + loginAction.sign
del_role_name = fake.word() + loginAction.sign


class test_003_Finance_role(TestBaseCase):
    def test_001_role_getRoles(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取角色列表
        """
        rs1 = FinanceAction.test_role_getRoles(pagenum=1, pagesize=10)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'orgCode')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'remark')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'count')

    def test_002_role_addRole(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :新增角色数据
        """
        global org_code
        org_code = loginAction.global_dict.get('org_code_one')
        rs1 = FinanceAction.test_role_addRole(orgcode=org_code, count='', remark=fake.text(20), id='', name=role_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code)
        Assertion.verity(json.loads(rs1)['data']['name'], role_name)
        global role_id
        role_id = json.loads(rs1)['data']['id']
        loginAction.global_dict.set(role_id=json.loads(rs1)['data']['id'])

    def test_003_role_addRole_del_role(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :新增角色数据
        """
        global org_code
        org_code = loginAction.global_dict.get('org_code_one')
        rs1 = FinanceAction.test_role_addRole(orgcode=org_code, count='', remark=fake.text(20), id='',
                                              name=del_role_name)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code)
        Assertion.verity(json.loads(rs1)['data']['name'], del_role_name)
        global del_role_id
        del_role_id = json.loads(rs1)['data']['id']

    def test_004_role_getRoleMoudelTree(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取角色模块树
        """
        rs1 = FinanceAction.test_role_getRoleMoudelTree(roleid=role_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verityContain(json.loads(rs1)['data'], 'id')
        Assertion.verityContain(json.loads(rs1)['data'], 'name')
        Assertion.verityContain(json.loads(rs1)['data'], 'parentId')
        Assertion.verityContain(json.loads(rs1)['data'], 'component')
        Assertion.verityContain(json.loads(rs1)['data'], 'directHave')
        Assertion.verityContain(json.loads(rs1)['data'], 'children')

    def test_005_role_saveRoleMoudels(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :保存角色权限
        """
        rolemoudellist = [{"id": 1, "directHave": "true", "parentId": 0},
                          {"id": 7, "directHave": "true", "parentId": 5},
                          {"id": 8, "directHave": "true", "parentId": 5},
                          {"id": 16, "directHave": "true", "parentId": 5},
                          {"id": 17, "directHave": "true", "parentId": 5},
                          {"id": 18, "directHave": "true", "parentId": 5},
                          {"id": 22, "directHave": "true", "parentId": 5},
                          {"id": 23, "directHave": "true", "parentId": 5},
                          {"id": 9, "directHave": "true", "parentId": 6},
                          {"id": 10, "directHave": "true", "parentId": 6},
                          {"id": 14, "directHave": "true", "parentId": 3},
                          {"id": 15, "directHave": "true", "parentId": 3},
                          {"id": 11, "directHave": "true", "parentId": 4},
                          {"id": 12, "directHave": "true", "parentId": 4},
                          {"id": 13, "directHave": "true", "parentId": 4},
                          {"id": 20, "directHave": "true", "parentId": 19},
                          {"id": 21, "directHave": "true", "parentId": 19},
                          {"id": 24, "directHave": "true", "parentId": 19},
                          {"id": 25, "directHave": "true", "parentId": 19}]
        rs1 = FinanceAction.test_role_saveRoleMoudels(rolemoudellist=str(rolemoudellist), roleid=role_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_006_role_getRoles_two(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取角色列表
        """
        rs1 = FinanceAction.test_role_getRoles(pagenum=1, pagesize=10)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'orgCode')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'remark')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'count')
        Assertion.verityContain(json.loads(rs1)['data']['record'], role_name)
        Assertion.verityContain(json.loads(rs1)['data']['record'], del_role_name)
        for record in json.loads(rs1)['data']['record']:
            Assertion.verityContain(record['count'], str(FinanceSql.get_role_count(record['id'])))

    def test_007_role_getDetail(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取角色
        """
        rs1 = FinanceAction.test_role_getDetail(role_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['count'], FinanceSql.get_role_count(role_id))
        Assertion.verity(json.loads(rs1)['data']['id'], role_id)
        Assertion.verity(json.loads(rs1)['data']['name'], role_name)
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code)

    def test_008_role_updateRole(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :修改角色数据
        """
        rs1 = FinanceAction.test_role_updateRole(
            id=role_id, orgcode=org_code, remark=fake.text(100), name=role_name, count='')
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['id'], role_id)
        Assertion.verity(json.loads(rs1)['data']['name'], role_name)
        Assertion.verity(json.loads(rs1)['data']['orgCode'], org_code)

    def test_009_role_deleteRole(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :删除一个角色
        """
        rs1 = FinanceAction.test_role_deleteRole(del_role_id)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')

    def test_010_role_getRoles_thr(self):
        """
        Time       :2019-06-18
        author     : 罗林
        desc       :获取角色列表
        """
        rs1 = FinanceAction.test_role_getRoles(pagenum=1, pagesize=10)
        Assertion.verity(json.loads(rs1)['code'], 'F2000')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['pageNum'], 1)
        Assertion.verity(json.loads(rs1)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs1)['data'], 'total')
        Assertion.verityContain(json.loads(rs1)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs1)['data'], 'record')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'id')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'orgCode')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'remark')
        Assertion.verityContain(json.loads(rs1)['data']['record'], 'count')
        Assertion.verityContain(json.loads(rs1)['data']['record'], role_name)
        Assertion.verityNotContain(json.loads(rs1)['data']['record'], del_role_name)
        for record in json.loads(rs1)['data']['record']:
            Assertion.verityContain(record['count'], str(FinanceSql.get_role_count(record['id'])))
