#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-11 下午 18:00
@Author     : 罗林
@File       : test_005_DelTestData.py
@desc       : 删除测试数据
"""


from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import pms_query
from xqkj.testAction import loginAction


class test_005_DelTestData(TestBaseCase):

    def test_001_del_system(self):
        #删除系统测试数据
        systemid=loginAction.global_dict.get('system_id')
        pms_query.delete_info('Tbl_Business_System','id="{}"'.format(systemid))

    def test_002_del_tenant(self):
        #删除机构测试数据
        tenantuuid=loginAction.global_dict.get('tenantuuid')
        tenantuuid1 = loginAction.global_dict.get('tenantuuid1')
        pms_query.delete_info('Tbl_Tenant','id="{}"'.format(tenantuuid))
        pms_query.delete_info('Tbl_Tenant', 'id="{}"'.format(tenantuuid1))

    def test_003_del_system_permission(self):
        #删除系统权限测试数据
        systemid = loginAction.global_dict.get('system_id')
        pms_query.delete_info('Tbl_Business_System_Permission','business_system_id="{}"'.format(systemid))

    def test_004_del_system_config(self):
        #删除系统配置测试数据
        systemid = loginAction.global_dict.get('system_id')
        pms_query.delete_info('Tbl_Business_System_Config', 'business_system_id="{}"'.format(systemid))


    def test_005_del_tenant_permission(self):
        #删除机构权限测试数据
        tenantuuid = loginAction.global_dict.get('tenantuuid')
        pms_query.delete_info('Tbl_Tenant_Permission','tenant_id="{}"'.format(tenantuuid))

    def test_006_del_tenant_config(self):
        #删除机构配置测试数据
        tenantuuid = loginAction.global_dict.get('tenantuuid')
        pms_query.delete_info('Tbl_Tenant_Config', 'tenant_id="{}"'.format(tenantuuid))




