#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-17 上午 10:30
@Author     : 闫红
@File       : test_020_pms_user.py
@desc       : 机构管理员管理相关接口
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import PlatformSystem_query as pq
from xqkj.testAction import PmsAction
from xqkj.testAction import specialAction
from xqkj.testAction import loginAction
from common.myFile import MockData as MD
import time


fake = Factory().create('zh_CN')
user_name = '用户' + loginAction.sign
email = fake.email()


class test_020_pms_user(TestBaseCase):
    def test_001_backstage_user_list(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,查询所有
        """
        rs = PmsAction.test_backstage_user_list(name='', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_002_backstage_user_list_one(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,指定查询
        """
        rs = PmsAction.test_backstage_user_list(name='童超', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['objs'], '童超')

    def test_003_backstage_user_list_not_exist(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,查询不存在的用户
        """
        name = MD.words_cn(5)
        rs = PmsAction.test_backstage_user_list(name=name, currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_004_backstage_user_list_overlong(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,name超长
        """
        name = MD.words_cn(256)
        rs = PmsAction.test_backstage_user_list(name=name, currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_005_backstage_user_role_list(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取角色列表
        """
        rs = PmsAction.test_backstage_user_role_list()
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data'], '超级管理员')

    def test_006_backstage_user_add_over_10(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，姓名超过10位
        """
        role_id = pq.get_role_id('超级管理员')
        name = '用户'+str(MD.number(9))
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_007_backstage_user_add_overlong(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，姓名超长
        """
        role_id = pq.get_role_id('超级管理员')
        name = '用户'+str(MD.number(254))
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_008_backstage_user_add(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，正常新增
        """
        role_id = pq.get_role_id('超级管理员')
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=user_name)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_009_backstage_user_add_duplicate_name(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，新增相同name，新增成功
        """
        role_id = pq.get_role_id('超级管理员')
        email = fake.email()
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=user_name)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_010_backstage_user_list_before_edit(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,指定查询，新增后查询
        """
        rs = PmsAction.test_backstage_user_list(name=user_name, currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['objs'], user_name)

    def test_011_backstage_user_edit(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 编辑用户
        """
        role_id = pq.get_role_id('超级管理员')
        id = pq.get_user_id('用户test-API')
        rs=PmsAction.test_backstage_user_edit(id=id, roleid=role_id, realname='编辑'+loginAction.sign, email=email)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_012_backstage_user_list_after_edit(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户列表查询,指定查询，查询修改后用户
        """
        rs = PmsAction.test_backstage_user_list(name='编辑', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data']['objs'], '编辑')

    def test_013_backstage_user_add_duplicate_email(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，新增相同email，新增失败
        """
        role_id = pq.get_role_id('超级管理员')
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=user_name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_014_backstage_user_add_error_email(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，不合规email，新增失败
        """
        role_id = pq.get_role_id('超级管理员')
        email = MD.number(5)
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=user_name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_015_backstage_user_add_not_exist_role(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，不存在的角色
        """
        role_id = -1
        email = fake.email()
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname=user_name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_016_backstage_user_add_name_is_null(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，name为空，新增成功
        """
        role_id = pq.get_role_id('超级管理员')
        email = fake.email()
        rs = PmsAction.test_backstage_user_add(email=email, roleid=role_id, realname='')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_017_backstage_user_add_email_is_null(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，email为空，新增失败
        """
        role_id = pq.get_role_id('超级管理员')
        rs = PmsAction.test_backstage_user_add(email='', roleid=role_id, realname=user_name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_018_backstage_user_add_role_is_null(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，email为空，新增失败
        """
        email = fake.email()
        rs = PmsAction.test_backstage_user_add(email=email, roleid='', realname=user_name)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_019_backstage_user_add_all_is_null(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户新增，email、name均为空，新增失败
        """
        role_id = pq.get_role_id('超级管理员')
        rs = PmsAction.test_backstage_user_add(email='', roleid=role_id, realname='')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_020_backstage_user_info(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取用户详情
        """
        user_id = pq.get_user_id('test-API')
        rs = PmsAction.test_backstage_user_info(id=user_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data'], 'test-API')

    def test_021_backstage_user_info_not_exist(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取用户详情,id不存在
        """
        user_id = -1
        rs = PmsAction.test_backstage_user_info(id=user_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_022_backstage_user_info_is_19(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取用户详情,id长度19位
        """
        user_id = MD.number(19)
        rs = PmsAction.test_backstage_user_info(id=user_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_023_backstage_user_info_is_20(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取用户详情,id长度20位
        """
        user_id = MD.number(20)
        rs = PmsAction.test_backstage_user_info(id=user_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_024_backstage_user_info_is_21(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 获取用户详情,id长度21位
        """
        user_id = MD.number(21)
        rs = PmsAction.test_backstage_user_info(id=user_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_025_backstage_user_change_state_to_disabled(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户状态管理,执为disabled
        """
        user_id = pq.get_user_id('test-API')
        rs = PmsAction.test_backstage_user_change_state(id=user_id, changeto='disabled')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_026_backstage_user_change_state_to_enabled(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户状态管理,执为enabled
        """
        user_id = pq.get_user_id('test-API')
        rs = PmsAction.test_backstage_user_change_state(id=user_id, changeto='enabled')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_027_backstage_user_change_state_from_enabled_to_disabled(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户状态管理,执为enabled后可以再次执为disabled
        """
        user_id = pq.get_user_id('test-API')
        rs = PmsAction.test_backstage_user_change_state(id=user_id, changeto='disabled')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_028_backstage_user_change_state_to_unknown(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 用户状态管理,执为unknown
        """
        user_id = pq.get_user_id('test-API')
        rs = PmsAction.test_backstage_user_change_state(id=user_id, changeto='unknown')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")
