#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-15 下午 4:25
@Author     : 闫红
@File       : test_018_pms_system.py
@desc       : 系统管理测试用例
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

businesssystemuuid = loginAction.sign+MD.words_en_lower(7)
secret = loginAction.sign+MD.words_en_lower(7)
fake = Factory().create('zh_CN')
host = 'test.'+MD.words_en_lower(3)+loginAction.sign + '78dk.com'
name = '系统' + fake.word() + loginAction.sign
key = 'system_'+str(MD.number(1))
des = '系统权限'+str(MD.number(1))


class test_018_pms_system(TestBaseCase):
    def test_001_backstage_system_add_all_null(self):
        """
        Time       :2019-07-12
        author     : 闫红
        desc       : 新增系统接口 (所有字段均为空)
        """
        rs = PmsAction.test_backstage_system_add(businesssystemuuid='', host='', name='',
                                                 secret='')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_002_backstage_system_add_duplicate_name(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (name相同)
        """
        rs = PmsAction.test_backstage_system_add(name='', businesssystemuuid=businesssystemuuid, host=host, secret=secret)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_003_backstage_system_add_duplicate_businesssystemuuid(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (businesssystemuuid相同)
        """
        rs = PmsAction.test_backstage_system_add(name=name, businesssystemuuid='', host=host, secret=secret)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_004_backstage_system_add_duplicate_host(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (host相同)
        """
        rs = PmsAction.test_backstage_system_add(name=name, businesssystemuuid=businesssystemuuid, host='', secret=secret)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], 'SUCCESS')

    def test_005_backstage_system_add(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (各项均填写正常值)
        """
        sys_name = '系统'+fake.word() + loginAction.sign
        sys_host = 'test.'+MD.words_en_lower(3)+loginAction.sign + '78dk.com'
        sys_secret = loginAction.sign+MD.words_en_lower(7)
        sys_uuid = loginAction.sign+MD.words_en_lower(7)
        rs = PmsAction.test_backstage_system_add(businesssystemuuid=sys_uuid, host=sys_host, name=sys_name,
                                                 secret=sys_secret)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_006_backstage_system_add_duplicate_secret(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (secret相同，可以新增相同系统秘钥)
        """
        rs = PmsAction.test_backstage_system_add(name=name, businesssystemuuid=businesssystemuuid, host=host, secret='')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')

    def test_007_backstage_system_add_overlong(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 新增系统接口 (name超长)
        """
        overlong_name='系统'+MD.words_cn(255)
        rs = PmsAction.test_backstage_system_add(businesssystemuuid=businesssystemuuid, host=host, name=overlong_name,
                                                 secret=secret)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_008_backstage_system_list_all(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 列表查询接口(所有系统列表)
        """
        rs = PmsAction.test_backstage_system_list(currentpage=1, pagesize=10, name='')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityContain(json.loads(rs)['data']['objs'], "businessSystemUuid")
        Assertion.verityContain(json.loads(rs)['data']['objs'], '系统')

    def test_009_backstage_system_list(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 列表查询接口，查询新增系统
        """
        rs = PmsAction.test_backstage_system_list(currentpage=1, pagesize=10, name='系统')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityContain(json.loads(rs)['data']['objs'], "businessSystemUuid")
        Assertion.verityContain(json.loads(rs)['data']['objs'], "系统")
        Assertion.verityNotNone(json.loads(rs)['data']['objs'][0]['id'])

    def test_010_backstage_system_list_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 列表查询接口，查询新增系统
        """
        rs = PmsAction.test_backstage_system_list(currentpage=1, pagesize=10, name=-1)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], 'SUCCESS')
        Assertion.verityNone(json.loads(rs)['data']['objs'])

    def test_011_backstage_system_chage_state_enabled(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口 （将新增系统状态由启用执为启用）
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_chage_state(changeto='enabled', id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_012_backstage_system_chage_state_disabled(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（将新增系统状态由启用执为停用）
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_chage_state(changeto='disabled', id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_013_backstage_system_chage_state_disabled_to_enabled(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（将新增系统状态由停用执为启用）
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_chage_state(changeto='enabled', id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_014_backstage_system_chage_state_to_enabled_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（不存在的系统状态执为启用）
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_chage_state(changeto='enabled', id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_015_backstage_system_chage_state_to_disabled_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（不存在的系统状态执为启用）
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_chage_state(changeto='disabled', id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_016_backstage_system_chage_state_to_unknown_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（不存在的系统状态执为unknown）
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_chage_state(changeto='unknown', id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_017_backstage_system_chage_state_to_unknown(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统状态管理接口（新增的系统，状态执为unknown）
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_chage_state(changeto='unknown', id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_018_backstage_system_genuuid(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 全局UUID生成接口
        """
        rs = PmsAction.test_backstage_system_genuuid()
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['uuid'])

    def test_019_backstage_system_info_id_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统详情接口(id为空)
        """
        rs = PmsAction.test_backstage_system_info(id='')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_020_backstage_system_info_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统详情接口(不存在的id)
        """
        id = -1
        rs = PmsAction.test_backstage_system_info(id=id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_021_backstage_system_info(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 系统详情接口，正常查询
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['businessSystemUuid'])

    def test_022_backstage_system_edit(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 编辑系统接口
        """
        business_id = pq.get_business_id('系统')
        print('第22条:',business_id)
        rs = PmsAction.test_backstage_system_edit(id=business_id, name='编辑'+name, businesssystemuuid=businesssystemuuid,
                                                  secret=secret, host=host)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_023_backstage_system_edit_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 编辑系统接口，不存在的系统
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_edit(id=business_id, name='编辑'+name, businesssystemuuid=businesssystemuuid,
                                                  secret=secret, host=host)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_024_backstage_system_edit_overlong(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 编辑系统接口，名字超长
        """
        business_id = pq.get_business_id('系统')
        overname = '编辑'+MD.words_cn(255)
        rs = PmsAction.test_backstage_system_edit(id=business_id, name=overname, businesssystemuuid=businesssystemuuid,
                                                  secret=secret, host=host)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_025_backstage_system_permission_info_id_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限查询接口，id为空
        """
        rs = PmsAction.test_backstage_system_permission_info(id='')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_026_backstage_system_permission_info(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限查询接口,查询新增系统的权限
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_permission_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNone(json.loads(rs)['data'])

    def test_027_backstage_system_permission_set_one(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限编辑接口，新增一个系统权限
        """
        business_id = pq.get_business_id('系统')
        permissions = [{'key': key, 'des': des}]
        rs = specialAction.test_backstage_system_permission_set(id=business_id, permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_028_backstage_system_permission_set_key(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限编辑接口，key非数字字母下划线
        """
        business_id = pq.get_business_id('系统')
        system_key='system-'+str(MD.number(1))
        permissions = [{'key': system_key, 'des': des}]
        rs = specialAction.test_backstage_system_permission_set(id=business_id, permissions=permissions)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_029_backstage_system_permission_set_des_isnone(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限编辑接口，des为空
        """
        business_id = pq.get_business_id('系统')
        syst_des = ''
        permissions = [{'key': key, 'des': syst_des}]
        rs = specialAction.test_backstage_system_permission_set(id=business_id, permissions=permissions)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_030_backstage_system_permission_info_not_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限查询接口,授权后查询新增系统的权限
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_permission_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data'])

    def test_031_backstage_system_permission_info_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限查询接口，查询不存在的系统权限详情
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_permission_info(id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_032_backstage_system_permission_set_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限编辑接口,清空系统权限
        """
        business_id = pq.get_business_id('系统')
        permissions = []
        rs = specialAction.test_backstage_system_permission_set(id=business_id, permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_033_backstage_system_permission_info_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 权限查询接口,清空系统权限后查询
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_permission_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNone(json.loads(rs)['data'])

    def test_034_backstage_system_config_info_id_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置查询接口，id为空
        """
        rs = PmsAction.test_backstage_system_config_info(id='')
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_035_backstage_system_config_info(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置查询接口，查询新增系统的配置
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_config_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotContain(json.loads(rs)['data'], "des")
        Assertion.verityNotContain(json.loads(rs)['data'], "key")

    def test_036_backstage_system_config_info_not_exist(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置查询接口，不存在的系统的配置
        """
        business_id = -1
        rs = PmsAction.test_backstage_system_config_info(id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_037_backstage_system_config_set_one(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置编辑接口,配置一个
        """
        business_id = pq.get_business_id('系统')
        configs = [{'key': key, 'des': des}]
        rs = specialAction.test_backstage_system_config_set(configs=configs, id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_038_backstage_system_config_info_one(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置查询接口，查询新增系统的这个一个配置
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_config_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityContain(json.loads(rs)['data'], "des")
        Assertion.verityContain(json.loads(rs)['data'], "key")

    def test_039_backstage_system_config_set_key_is_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置编辑接口,key为空
        """
        business_id = pq.get_business_id('系统')
        configs = [{'key': '', 'des': des}]
        rs = specialAction.test_backstage_system_config_set(configs=configs, id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_040_backstage_system_config_set_des_is_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置编辑接口,des为空
        """
        business_id = pq.get_business_id('系统')
        configs = [{'key': key, 'des': ''}]
        rs = specialAction.test_backstage_system_config_set(configs=configs, id=business_id)
        Assertion.verityNot(json.loads(rs)['code'], 10000)
        Assertion.verityNot(json.loads(rs)['msg'], "SUCCESS")

    def test_041_backstage_system_config_set_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置编辑接口，配置0个
        """
        business_id = pq.get_business_id('系统')
        configs = []
        rs = specialAction.test_backstage_system_config_set(configs=configs, id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_042_backstage_system_config_info_none(self):
        """
        Time       :2019-07-15
        author     : 闫红
        desc       : 配置查询接口，查询新增系统清空后的配置
        """
        business_id = pq.get_business_id('系统')
        rs = PmsAction.test_backstage_system_config_info(id=business_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotContain(json.loads(rs)['data'], "des")
        Assertion.verityNotContain(json.loads(rs)['data'], "key")
