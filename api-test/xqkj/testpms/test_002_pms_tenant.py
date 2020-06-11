#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-09 上午 10:50
@Author     : songchao
@File       : test_002_pms_tenant.py
@desc       : 1.机构管理相关接口
              2.机构权限管理相关接口
              3.机构配置项目管理相关接口
"""

import json

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.testAction import PmsAction
from xqkj.testAction import loginAction
from  xqkj.query import  pms_query
from xqkj.testAction import specialAction

system_name = '7777' + loginAction.sign
business_system_uuid = '7777'
tenant_name='8888'+ loginAction.sign
global_dict = loginAction.global_dict


class test_002_pms_tenant(TestBaseCase):
    #机构管理相关用例
    def test_001_backstage_system_add(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 系统新增
        """
        rs = PmsAction.test_backstage_system_add(name=system_name, businesssystemuuid=business_system_uuid, secret='7777',host='test2.finanecorar.78dk.com')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        id = pms_query.select_PassWordReset_key('Tbl_Business_System', 'id',
                                                 'host="test2.finanecorar.78dk.com"')
        global_dict.set(system_id=id)

    def test_002_backstage_tenant_add(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 机构新增
        """
        global system_id
        system_id=global_dict.get('system_id')
        rs = PmsAction.test_backstage_tenant_add(name=tenant_name, systemid=system_id)
        rs1=PmsAction.test_backstage_tenant_add(name='song', systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        id=pms_query.select_PassWordReset_key('Tbl_Tenant', 'id',
                                                  'name="{}"'.format(tenant_name))
        id1=pms_query.select_PassWordReset_key('Tbl_Tenant', 'id',
                                                  'name="song"')
        global_dict.set(tenantuuid=id)
        global_dict.set(tenantuuid1=id1)


    def test_003_backstage_tenant_system_list_name_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 系统列表查询接口-机构管理(缺少 系统名称name)
        """
        rs = PmsAction.test_backstage_tenant_system_list(currentpage=1, name='', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'], 'businessSystemState')
        Assertion.verityContain(json.loads(rs)['data'], 'businessSystemUuid')

    def test_004_backstage_tenant_system_list_name_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 系统列表查询接口-机构管理(没有的 系统名称name)
        """
        rs = PmsAction.test_backstage_tenant_system_list(currentpage=1, name='12', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 0)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 0)
        Assertion.verityNotContain(json.loads(rs)['data'], 'businessSystemState')
        Assertion.verityNotContain(json.loads(rs)['data'], 'system_id')


    def test_005_backstage_tenant_system_list_normal(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 系统列表查询接口-机构管理(指定 系统名称name)
        """
        rs = PmsAction.test_backstage_tenant_system_list(currentpage=1, name=system_name, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['id'], int(system_id))
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'], system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['host'], 'test2.finanecorar.78dk.com')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['businessSystemState'], 'enabled')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'businessSystemUuid')

    def test_006_backstage_tenant_system_list_dimname(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 系统列表查询接口-机构管理(模糊查询 系统名称name)
        """
        rs = PmsAction.test_backstage_tenant_system_list(currentpage=1, name='77', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['id'], int(system_id))
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'], system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['host'], 'test2.finanecorar.78dk.com')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['businessSystemState'], 'enabled')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'businessSystemUuid')

    def test_007_backstage_tenant_list_name_none(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 机构列表查询接口(缺少 机构名称	name，查询所有)
        """
        #system_id = global_dict.get('system_id')
        rs = PmsAction.test_backstage_tenant_list(currentpage=1, name='', pagesize=10, systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 2)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'id')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'], tenant_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['systemName'], system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['tenantState'], 'enabled')

    def test_008_backstage_tenant_list_systemid_none(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 机构列表查询接口(缺少 系统Idsystemid)
        """
        rs = PmsAction.test_backstage_tenant_list(currentpage=1, name=tenant_name, pagesize=10, systemid='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "系统不存在")

    def test_009_backstage_tenant_list_normal(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 指定机构列表查询接口
        """
        #system_id = global_dict.get('system_id')
        rs = PmsAction.test_backstage_tenant_list(currentpage=1, name=tenant_name, pagesize=10, systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'id')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'], tenant_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['systemName'], system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['tenantState'], 'enabled')

    def test_010_backstage_tenant_list_errorname(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 机构列表查询接口_没有的机构
        """
        rs = PmsAction.test_backstage_tenant_list(currentpage=1, name='23', pagesize=10, systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 0)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 0)
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'id')

    def test_011_backstage_tenant_list_dimname(self):
        """
        Time       :2019-07-09
        author     : songchao
        desc       : 机构列表查询接口_模糊查询名称
        """
        rs = PmsAction.test_backstage_tenant_list(currentpage=1, name='88', pagesize=10, systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'id')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'], tenant_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['systemName'], system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['tenantState'], 'enabled')


    def test_012_backstage_tenant_change_state_enabled(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(enabled，正常设置)
        """
        global tenant_id
        tenant_id = loginAction.global_dict.get('tenantuuid')
        rs = PmsAction.test_backstage_tenant_change_state(changeto='enabled', id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_013_backstage_tenant_change_state_disabled(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(disabled正常设置)
        """
        rs = PmsAction.test_backstage_tenant_change_state(changeto='disabled', id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_014_backstage_tenant_change_state_id_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(enabled，id为空)
        """
        rs = PmsAction.test_backstage_tenant_change_state(changeto='enabled', id='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_015_backstage_tenant_change_state_id_error(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(enabled，id错误)
        """
        rs=PmsAction.test_backstage_tenant_change_state(changeto='enabled', id='889088')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_016_backstage_tenant_change_state_changeto_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(changeto为空)
        """
        rs = PmsAction.test_backstage_tenant_change_state(changeto='', id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "状态值错误")

    def test_017_backstage_tenant_change_state_changeto_error(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构状态管理接口(changeto错误)
        """
        rs = PmsAction.test_backstage_tenant_change_state(changeto='iui', id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "状态值错误")



    def test_018_backstage_tenant_add_name_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构新增接口(缺少 机构名称name)
        """
        rs = PmsAction.test_backstage_tenant_add(name='', systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构名称不能为空")

    def test_019_backstage_tenant_add_systemid_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构新增接口(缺少 系统id systemid)
        """
        rs = PmsAction.test_backstage_tenant_add(name=tenant_name, systemid='')
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "系统不存在")

    def test_020_backstage_tenant_add_name_repeat(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构新增接口(机构名称name重复)
        """
        rs = PmsAction.test_backstage_tenant_add(name=tenant_name, systemid=system_id)
        Assertion.verity(json.loads(rs)['code'], 10003)
        Assertion.verity(json.loads(rs)['msg'], "系统下已经存在该机构名称")

    def test_021_backstage_tenant_add_systemid_error(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构新增接口(系统id错误)
        """
        rs = PmsAction.test_backstage_tenant_add(name=tenant_name, systemid='999999')
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "系统不存在")

    def test_022_backstage_tenant_get_system_name_id_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 系统名称获取(缺少 系统id)
        """
        rs = PmsAction.test_backstage_tenant_get_system_name('')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "系统不存在")

    def test_023_backstage_tenant_get_system_name_id_error(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 系统名称获取(系统id错误)
        """
        rs = PmsAction.test_backstage_tenant_get_system_name('898989')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "系统不存在")

    def test_024_backstage_tenant_get_system_name(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 正常系统名称获取
        """
        rs = PmsAction.test_backstage_tenant_get_system_name(system_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['systemName'], system_name)

    def test_025backstage_tenant_info_before(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构详情获取接口（正常）
        """
        rs = PmsAction.test_backstage_tenant_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['name'], tenant_name)
        Assertion.verity(json.loads(rs)['data']['systemName'], system_name)

    def test_026_backstage_tenant_edit(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 正常机构编辑接口
        """
        rs = PmsAction.test_backstage_tenant_edit(id=tenant_id, name='编辑' + tenant_name)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")


    def test_027_backstage_tenant_edit_id_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构编辑接口（id为空）
        """
        rs = PmsAction.test_backstage_tenant_edit(id='', name='编辑' + tenant_name)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_028_backstage_tenant_edit_id_error(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构编辑接口（id错误）
        """
        rs = PmsAction.test_backstage_tenant_edit(id='898988', name='编辑' + tenant_name)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_029_backstage_tenant_edit_name_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构编辑接口（name为空）
        """
        rs = PmsAction.test_backstage_tenant_edit(id=tenant_id, name='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构姓名不能为空")


    def test_030_backstage_tenant_edit_name_noedit(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构编辑接口（name不修改保存）
        """
        rs = PmsAction.test_backstage_tenant_edit(id=tenant_id, name='编辑' + tenant_name)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_031_backstage_tenant_edit_name_repeat(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构编辑接口（name重复）
        """
        rs = PmsAction.test_backstage_tenant_edit(id=tenant_id, name='song')
        Assertion.verity(json.loads(rs)['code'], 10003)
        Assertion.verity(json.loads(rs)['msg'], "系统下已经存在该机构名称")


    def test_032_backstage_tenant_info_id_none(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构详情获取接口（id为空）
        """
        rs = PmsAction.test_backstage_tenant_info(id='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")


    def test_033_backstage_tenant_info_after(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构详情获取接口（编辑后详情）
        """
        rs = PmsAction.test_backstage_tenant_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['name'], '编辑' + tenant_name)
        Assertion.verity(json.loads(rs)['data']['systemName'], system_name)

    def test_034_backstage_tenant_info_after(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构详情获取接口（id错误）
        """
        rs = PmsAction.test_backstage_tenant_info(id='6787688')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    # 机构配置项目管理接口

    def test_035_backstage_tenant_permission_tenant_list_tenant_namenone(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(姓名为空查询全部)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'], 'totalCount')
        Assertion.verityContain(json.loads(rs)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'tenantState')

    def test_036_backstage_tenant_permission_tenant_list_tenant_name(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(机构姓名为具体名字)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='song', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '1')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '1')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['name'],'song')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['systemName'],system_name)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['tenantState'],'enabled')

    def test_037_backstage_tenant_permission_tenant_list_tenant_nameerror(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(机构姓名系统姓名都不能查询出数据)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='dsadew', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '0')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '0')
        Assertion.verityContain(json.loads(rs)['data'],'objs')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'name')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'systemName')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'tenantState')

    def test_038_backstage_tenant_permission_tenant_list_tenant_namemohu(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(机构姓名模糊查询出数据)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='so', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'],'song')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['systemName'],system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['tenantState'],'enabled')

    def test_039_backstage_tenant_permission_tenant_list_tenant_namejinyong(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(机构姓名查询已经被禁用的机构)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='编辑' + tenant_name, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '0')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '0')
        Assertion.verityContain(json.loads(rs)['data'], 'objs')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'name')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'systemName')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'tenantState')

    def test_040_backstage_tenant_permission_tenant_list_system_name(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(系统姓名为具体名字)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name=system_name, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'],'totalCount')
        Assertion.verityContain(json.loads(rs)['data'],'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'tenantState')

    def test_041_backstage_tenant_permission_tenant_list_system_namemohu(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构权限管理_机构列表查询接口(系统姓名模糊查询)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='77', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'],'totalCount')
        Assertion.verityContain(json.loads(rs)['data'],'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'tenantState')

    def test_042_backstage_system_permission_add(self):
        """
            Time       :2019-07-10
            author     : songchao
            desc       : 新增配置，权限数据
        """
        permissions=[{"key": "123", "des": "456"}, {"key": "444", "des": "555"}]
        configs=[{"key": "444", "des": "555"},{"key": "666", "des": "777"}]
        rs=specialAction.test_backstage_system_permission_set(id=system_id, permissions=permissions)
        rs1=specialAction.test_backstage_system_config_set(id=system_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs1)['code'], 10000)
        Assertion.verity(json.loads(rs1)['msg'], "SUCCESS")



    def test_043_backstage_tenant_permission_info_no(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取的接口
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'456')
        Assertion.verity(json.loads(rs)['data'][0]['isHave'],'no')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'123')

    def test_044_backstage_tenant_permission_info_id_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取_id为空
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_045_backstage_tenant_permission_info_id_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取_id错误
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id='9999999')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_046_backstage_tenant_permission_info_id_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取_id传非数字
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id='99999@9f9')
        Assertion.verity(json.loads(rs)['code'], 40000)

    def test_047_backstage_tenant_permission_set_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_权限设置为空保存
        """
        permissions = []
        rs = specialAction.test_backstage_tenant_permission_set(id=tenant_id, permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_048_backstage_tenant_permission_info_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取的接口_权限设置为空保存后，查看权限是否变化
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'456')
        Assertion.verity(json.loads(rs)['data'][0]['isHave'],'no')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'123')


    def test_049_backstage_tenant_permission_set(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_正常
        """
        permissions = ['123','444']
        rs = specialAction.test_backstage_tenant_permission_set(id=tenant_id, permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_050_backstage_tenant_permission_info_yes(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取的接口_权限设置后查看权限变化
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'456')
        Assertion.verity(json.loads(rs)['data'][0]['isHave'],'yes')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'123')

    def test_051_backstage_tenant_permission_set_remove(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_权限空，权限取消
        """
        permissions = []
        rs = specialAction.test_backstage_tenant_permission_set(id=tenant_id, permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_052_backstage_tenant_permission_info_remove(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_正常机构权限获取的接口_权限取消后查看是否没有权限
        """
        rs = PmsAction.test_backstage_tenant_permission_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'456')
        Assertion.verity(json.loads(rs)['data'][0]['isHave'],'no')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'123')

    def test_053_backstage_tenant_permission_set_id_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_id错误
        """
        permissions = ['123','444']
        rs = specialAction.test_backstage_tenant_permission_set(id='7898', permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_054_backstage_tenant_permission_set_id_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_id为空
        """
        permissions = ['123','444']
        rs = specialAction.test_backstage_tenant_permission_set(id='', permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_055_backstage_tenant_permission_set_id_nonumer(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构权限管理_机构权限设置接口_id非数字
        """
        permissions = ['123','444']
        rs = specialAction.test_backstage_tenant_permission_set(id='asdad', permissions=permissions)
        Assertion.verity(json.loads(rs)['code'], 40000)
        Assertion.verity(json.loads(rs)['msg'], "系统内部异常")



# 机构配置项目管理接口
    def test_056_backstage_tenant_config_tenant_list_namenone(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(姓名为空查询全部)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name='', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'], 'totalCount')
        Assertion.verityContain(json.loads(rs)['data'], 'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0], 'tenantState')

    def test_057_backstage_tenant_config_tenant_list_tenant_name(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(机构姓名为具体名字)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name='song', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '1')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '1')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['name'],'song')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['systemName'],system_name)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0]['tenantState'],'enabled')

    def test_058_backstage_tenant_config_tenant_list_tenant_nameerror(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(机构姓名系统姓名都不能查询出数据)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name='dsadew', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '0')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '0')
        Assertion.verityContain(json.loads(rs)['data'],'objs')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'name')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'systemName')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'],'tenantState')

    def test_059_backstage_tenant_config_tenant_list_tenant_namemohu(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(机构姓名模糊查询出数据)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name='so', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verity(json.loads(rs)['data']['totalCount'], 1)
        Assertion.verity(json.loads(rs)['data']['totalPage'], 1)
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['name'],'song')
        Assertion.verity(json.loads(rs)['data']['objs'][0]['systemName'],system_name)
        Assertion.verity(json.loads(rs)['data']['objs'][0]['tenantState'],'enabled')

    def test_060_backstage_tenant_config_tenant_list_tenant_namejinyong(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(机构姓名查询已经被禁用的机构)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name='编辑' + tenant_name, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data']['totalCount'], '0')
        Assertion.verityContain(json.loads(rs)['data']['totalPage'], '0')
        Assertion.verityContain(json.loads(rs)['data'], 'objs')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'name')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'systemName')
        Assertion.verityNotContain(json.loads(rs)['data']['objs'], 'tenantState')

    def test_061_backstage_tenant_config_tenant_list_system_name(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(系统姓名为具体名字)
        """
        rs = PmsAction.test_backstage_tenant_config_tenant_list(currentpage=1, name=system_name, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'],'totalCount')
        Assertion.verityContain(json.loads(rs)['data'],'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'tenantState')

    def test_062_backstage_tenant_config_tenant_list_system_namemohu(self):
        """
        Time       :2019-07-10
        author     : songchao
        desc       : 机构配置项目管理_机构列表查询取接口(系统姓名模糊查询)
        """
        rs = PmsAction.test_backstage_tenant_permission_tenant_list(currentpage=1, name='77', pagesize=10)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data']['currentPage'], 1)
        Assertion.verity(json.loads(rs)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(rs)['data'],'totalCount')
        Assertion.verityContain(json.loads(rs)['data'],'totalPage')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'id')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'name')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'systemName')
        Assertion.verityContain(json.loads(rs)['data']['objs'][0],'tenantState')


    def test_063_backstage_tenant_config_info_no(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口
        """
        rs = PmsAction.test_backstage_tenant_config_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'555')
        Assertion.verityContain(json.loads(rs)['data'][0],'value')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'444')

    def test_064_backstage_tenant_config_info_id_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口_id为空
        """
        rs = PmsAction.test_backstage_tenant_config_info(id='')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_065_backstage_tenant_config_info_id_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口_id错误
        """
        rs = PmsAction.test_backstage_tenant_config_info(id='9999999')
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_066_backstage_tenant_config_info_id_nonumber(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口_id传非数字
        """
        rs = PmsAction.test_backstage_tenant_config_info(id='99999@9f9')
        Assertion.verity(json.loads(rs)['code'], 40000)





    def test_067_backstage_tenant_config_set(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_正常
        """
        configs = [{"key": "444", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id=tenant_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_068_backstage_tenant_config_info_yes(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口_权限设置后查看权限变化
        """
        rs = PmsAction.test_backstage_tenant_config_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'],'555')
        Assertion.verity(json.loads(rs)['data'][0]['value'],'sc')
        Assertion.verity(json.loads(rs)['data'][0]['key'],'444')

    def test_069_backstage_tenant_config_set_remove(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置清空
        """
        configs = []
        rs = specialAction.test_backstage_tenant_config_set(id=tenant_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_070_backstage_tenant_config_info_remove(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置获取接口_配置清空后检查
        """
        rs = PmsAction.test_backstage_tenant_config_info(id=tenant_id)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verity(json.loads(rs)['data'][0]['des'], '555')
        Assertion.verity(json.loads(rs)['data'][0]['value'], None)
        Assertion.verity(json.loads(rs)['data'][0]['key'], '444')


    def test_071_backstage_tenant_config_set_value_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中vlue为空
        """
        configs =[{"key": "444", "value": ""}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id=tenant_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "机构配置设置不规范")

    def test_072_backstage_tenant_config_set_key_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中key为空
        """
        configs =[{"key": "", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id=tenant_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "机构配置设置不规范")



    def test_073_backstage_tenant_config_set_key_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中key错误
        """
        configs = [{"key": "asdasd", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id=tenant_id, configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10002)
        Assertion.verity(json.loads(rs)['msg'], "机构配置设置不规范")


    def test_074_backstage_tenant_config_set_id_none(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中id为空
        """
        configs = [{"key": "444", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id='', configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_075_backstage_tenant_config_set_id_error(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中id错误
        """
        configs = [{"key": "444", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id='9889999', configs=configs)
        Assertion.verity(json.loads(rs)['code'], 10001)
        Assertion.verity(json.loads(rs)['msg'], "机构不存在")

    def test_076_backstage_tenant_config_set_id_nonumber(self):
        """
        Time       :2019-07-11
        author     : songchao
        desc       : 机构配置项目管理_机构配置设置接口_配置中id非数字
        """
        configs = [{"key": "444", "value": "sc"}, {"key": "666", "value": "sc1"}]
        rs = specialAction.test_backstage_tenant_config_set(id='afa', configs=configs)
        Assertion.verity(json.loads(rs)['code'], 40000)
        Assertion.verity(json.loads(rs)['msg'], "系统内部异常")










