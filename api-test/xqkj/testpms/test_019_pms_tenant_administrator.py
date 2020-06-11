#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-15 下午 6:00
@Author     : 闫红
@File       : test_019_pms_tenant_administrator.py
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
tenant_name = '机构' + str(MD.number(1)) + loginAction.sign
phone = fake.phone_number()
email = fake.email()
administrator_name = '机构管理员'+str(MD.number(1))+loginAction.sign


class test_019_pms_tenant_administrator(TestBaseCase):
    def test_001_backstage_tenant_config_tenant_list_all(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 机构管理员列表查询，查询所有机构
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(name='', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_002_backstage_tenant_config_tenant_list_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 机构管理员列表查询，查询不存在的机构
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(name='99999', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_003_backstage_tenant_config_tenant_list_(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 机构管理员列表查询，查询已知机构
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(name='消费分期', currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityContain(json.loads(rs)['data']['objs'], '消费分期')

    def test_004_backstage_tenant_config_tenant_list_overlong(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 机构管理员列表查询，条件超过255位
        """
        tenant_name = MD.words_cn(256)
        rs = PmsAction.test_backstage_tenant_config_tenant_list(name=tenant_name, currentpage=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_005_backstage_system_and_tenant_add(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统，新增机构，为机构管理员接口准备数据
        """
        sys_name = '系统'+fake.word() + loginAction.sign
        sys_host = 'test.'+MD.words_en_lower(3)+loginAction.sign + '78dk.com'
        sys_secret = loginAction.sign+MD.words_en_lower(7)
        sys_uuid = loginAction.sign+MD.words_en_lower(7)
        rs = PmsAction.test_backstage_system_add(businesssystemuuid=sys_uuid, host=sys_host, name=sys_name,
                                                 secret=sys_secret)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        business_id = pq.get_business_id('系统')
        PmsAction.test_backstage_tenant_add(name=tenant_name, systemid=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_006_backstage_tenant_administrator_list_no(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 未新增管理员，查询机构管理员
        """
        tenantid = pq.get_tenantid('系统', '机构')
        rs = PmsAction.test_backstage_tenant_administrator_list(tenantid=tenantid,currentpage=1,name='',pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_007_backstage_tenant_administrator_list_overlong(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 未新增管理员，关键字名称超长，查询管理员
        """
        tenantid = pq.get_tenantid('系统', '机构')
        name = MD.words_cn(256)
        rs = PmsAction.test_backstage_tenant_administrator_list(tenantid=tenantid,currentpage=1,name=name,pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_008_backstage_tenant_administrator_get_system_name_and_tenant_name(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 根据机构Id获取机构名称和系统名称
        """
        tenantid = pq.get_tenantid('系统', '机构')
        rs = PmsAction.test_backstage_tenant_administrator_get_system_name_and_tenant_name(tenantid)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityContain(json.loads(rs)['data'], '系统')
        Assertion.verityContain(json.loads(rs)['data'], '机构')

    def test_009_backstage_tenant_administrator_get_system_name_and_tenant_name_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 根据机构Id获取机构名称和系统名称,查询不存在的机构id
        """
        tenantid = -1
        rs = PmsAction.test_backstage_tenant_administrator_get_system_name_and_tenant_name(tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_010_backstage_tenant_administrator_get_system_name_and_tenant_name_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 根据机构Id获取机构名称和系统名称,查询id超长
        """
        tenantid = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_get_system_name_and_tenant_name(tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_011_backstage_tenant_administrator_add(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增
        """
        tenantid = pq.get_tenantid('系统', '机构')
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name, email=email, tenantid=tenantid)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')

    def test_012_backstage_tenant_administrator_add_duplicate_email(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增,除邮箱外，name、电话均可以相同，验证邮箱重复
        """
        tenantid = pq.get_tenantid('系统', '机构')
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name, email=email, tenantid=tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_013_backstage_tenant_administrator_add_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增,机构id不存在
        """
        tenantid = -1
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name, email=email, tenantid=tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_014_backstage_tenant_administrator_add_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增,机构id超长
        """
        tenantid = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name, email=email, tenantid=tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_015_backstage_tenant_administrator_add_email(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增,email不符合格式
        """
        tenantid = pq.get_tenantid('系统', '机构')
        error_email = 222
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name, email=error_email, tenantid=tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_016_backstage_tenant_administrator_add_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员新增,名字超长
        """
        tenantid = pq.get_tenantid('系统', '机构')
        email1 = fake.email()
        administrator_name1 = '机构管理员'+str(MD.number(255))
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone, name=administrator_name1, email=email1, tenantid=tenantid)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_017_backstage_tenant_administrator_edit(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 编辑机构管理员，被锁定
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_edit(name='编辑'+administrator_name, email=email, phone=phone,id= tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '锁定')

    def test_018_backstage_tenant_administrator_info(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理详情获取
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_info(id=tenant_adm_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityContain(json.loads(rs)['data'], '机构管理员')

    def test_019_backstage_tenant_administrator_info_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理详情获取,不存在的id
        """
        tenant_adm_id = -1
        rs = PmsAction.test_backstage_tenant_administrator_info(id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_020_backstage_tenant_administrator_info_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理详情获取,id超长
        """
        tenant_adm_id = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_info(id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_021_backstage_tenant_administrator_change_state_to_enabled(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,执为enabled
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='enabled',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '锁定')

    def test_022_backstage_tenant_administrator_change_state_to_disabled(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,执为disabled
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='disabled',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '锁定')

    def test_023_backstage_tenant_administrator_change_state_disabled_to_enabled(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,执为disabled
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='enabled',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '锁定')

    def test_024_backstage_tenant_administrator_change_state_unknown(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,执为unknown
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='unknown',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '错误')

    def test_025_backstage_tenant_administrator_change_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,不存在的id
        """
        tenant_adm_id = -1
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='enabled',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_026_backstage_tenant_administrator_change_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理状态管理,id超长
        """
        tenant_adm_id = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_change_state(changeto='enabled',id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_027_backstage_tenant_administrator_resert_password(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员密码重置
        """
        tenant_adm_id = pq.get_tenant_adm_id(business_name='系统',tenant_name='机构',adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_resert_password(id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityContain(json.loads(rs)['msg'], '锁定')

    def test_028_backstage_tenant_administrator_resert_password_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员密码重置,id不存在
        """
        tenant_adm_id = -1
        rs = PmsAction.test_backstage_tenant_administrator_resert_password(id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_029_backstage_tenant_administrator_resert_password_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员密码重置,id超长
        """
        tenant_adm_id = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_resert_password(id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_031_backstage_tenant_add(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 为“消费分期”系统新增机构，为机构管理员接口准备数据
        """
        business_id = pq.get_business_id('消费分期')
        rs = PmsAction.test_backstage_tenant_add(name=tenant_name, systemid=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_032_backstage_tenant_administrator_add(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 新增管理员，为机构管理员接口准备数据
        """
        tenantid = pq.get_tenantid('消费分期', '机构')
        rs = PmsAction.test_backstage_tenant_administrator_add(phone=phone,name=administrator_name,email=email,tenantid=tenantid)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_033_backstage_tenant_administrator_edit(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 编辑管理员
        """
        time.sleep(30)
        tenant_adm_id = pq.get_tenant_adm_id(business_name='消费分期',tenant_name='机构',adm_name='机构管理员')
        email1=fake.email()
        phone1=fake.phone_number()
        rs = PmsAction.test_backstage_tenant_administrator_edit(name='编辑'+administrator_name,email=email1,phone=phone1,id=tenant_adm_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_034_backstage_tenant_administrator_edit_not_exist(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 编辑管理员,id不存在
        """
        tenant_adm_id = -1
        rs = PmsAction.test_backstage_tenant_administrator_edit(name='编辑'+administrator_name,email=email,phone=phone,id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_035_backstage_tenant_administrator_edit_overlong(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 编辑管理员,id超长
        """
        tenant_adm_id = MD.number(256)
        rs = PmsAction.test_backstage_tenant_administrator_edit(name='编辑'+administrator_name,email=email,phone=phone,id=tenant_adm_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_036_backstage_tenant_administrator_resert_password(self):
        """
        Time       :2019-07-16
        author     : 闫红
        desc       : 机构管理员密码重置
        """
        time.sleep(30)
        tenant_adm_id = pq.get_tenant_adm_id(business_name='消费分期', tenant_name='机构', adm_name='机构管理员')
        rs = PmsAction.test_backstage_tenant_administrator_resert_password(id=tenant_adm_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
