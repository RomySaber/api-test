#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-12 下午 6:08
@Author     : 闫红
@File       : test_017_pms_role.py
@desc       : 角色管理员接口测试用例
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData as MD
from xqkj.query import PlatformSystem_query as pq
from xqkj.testAction import PmsAction
from xqkj.testAction import loginAction

fake = Factory().create('zh_CN')
role_name = '角色' + fake.word() + loginAction.sign
user_name = fake.name() + loginAction.sign
email = loginAction.sign + fake.email()
phone = fake.phone_number()


class test_017_pms_role(TestBaseCase):
    def test_001_backstage_role_list_name_none(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色列表查询接口(缺少 角色名称name,查询所有)
        """
        rs = PmsAction.test_backstage_role_list(currentpage=1, name='', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityNotNone(json.loads(rs)['data']['objs'], '断言不为空')

    def test_002_backstage_role_list_name_not_exits(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色列表查询接口,查询不存在的角色
        """
        rs = PmsAction.test_backstage_role_list(currentpage=1, name='1', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityNone(json.loads(rs)['data']['objs'], '断言为空')

    def test_003_backstage_role_add(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色新增接口，name为“角色”开头,只授一个权限
        """
        permissionids = pq.get_permission_id()
        rs = PmsAction.test_backstage_role_add(permissionids=permissionids, name=role_name)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_004_backstage_role_list_name(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色列表查询接口，查询新增的角色【name为“角色”开头】
        """
        rs = PmsAction.test_backstage_role_list(currentpage=1, name='角色', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['name'], '角色')
        global role_id
        role_id = json.loads(rs)['data']['objs'][0]['id']

    def test_005_backstage_role_info_one(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色详情获取接口，正常获取，断言授权
        """
        role_id = pq.get_role_id('角色')
        rs = PmsAction.test_backstage_role_info(role_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['name'], '角色')
        Assertion.verity(len(json.loads(rs)['data']['permissionIds']), 1)

    def test_006_backstage_role_add_name_over_long(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色新增接口，name超过255
        """
        global permissionids
        permissionids = pq.get_permission_id()
        name = '角色'+MD.words_cn(254)
        rs = PmsAction.test_backstage_role_add(permissionids=permissionids, name=name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_007_backstage_role_edit(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色编辑接口,正常编辑
        """
        role_id = pq.get_role_id('角色')
        permissionids = pq.get_permission_id()
        rs = PmsAction.test_backstage_role_edit(id=role_id, name='编辑' + role_name, permissionids=permissionids)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_008_backstage_role_edit_not_exist(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : 角色编辑接口 ,编辑不存在的角色
        """
        role_id = 9999999
        permissionids = pq.get_permission_id()
        rs = PmsAction.test_backstage_role_edit(id=role_id, name='编辑' + role_name, permissionids=permissionids)
        self.assertNotEqual(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "角色不存在")

    def test_009_backstage_role_edit_name_overlong(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : 角色编辑接口 ,编辑name超长
        """
        role_id = pq.get_role_id('角色')
        permissionids = pq.get_permission_id()
        name = MD.words_cn(256)
        rs = PmsAction.test_backstage_role_edit(id=role_id, name='编辑' + name + role_name, permissionids=permissionids)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_010_backstage_role_permissions_list(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : permissionids传入非字符
        """
        role_id = pq.get_role_id('角色')
        permissionids = pq.get_permission_ids()
        rs = PmsAction.test_backstage_role_edit(id=role_id, name='编辑' + role_name, permissionids=permissionids)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_011_backstage_role_permissions_str(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : 授所有权限
        """
        role_id = pq.get_role_id('角色')
        permissionids = pq.get_permission_ids_to_str()
        rs = PmsAction.test_backstage_role_edit(id=role_id, name='编辑' + role_name, permissionids=permissionids)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_012_backstage_role_info_all(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色详情获取接口，正常获取
        """
        role_id = pq.get_role_id('角色')
        rs = PmsAction.test_backstage_role_info(role_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['name'], '角色')
        Assertion.verity(len(json.loads(rs)['data']['permissionIds']), 8)

    def test_013_backstage_role_permissions(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 获取所有权限的集合
        """
        rs = PmsAction.test_backstage_role_permissions()
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data'], 'id')
        Assertion.verityContain(json.loads(rs)['data'], 'name')

    def test_014_backstage_role_info_id_none(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色详情获取接口，获取不存在的角色详情
        """
        rs = PmsAction.test_backstage_role_info(id='')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_015_backstage_role_info_id_is_num(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : 角色详情获取接口，ID为数字
        """
        rs = PmsAction.test_backstage_role_info(id=99999)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_016_backstage_role_info(self):
        """
        Time       :2019-07-10
        author     : 闫红
        desc       : 角色详情获取接口，正常获取
        """
        role_id = pq.get_role_id('角色')
        rs = PmsAction.test_backstage_role_info(role_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['name'], '角色')
