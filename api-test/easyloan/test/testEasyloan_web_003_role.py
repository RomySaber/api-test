#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-28 下午 4:52
@Author     : 罗林
@File       : testEasyloan_web_003_role.py
@desc       : 系统管理接口测试用例   （暂停用）
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_webAction as ew, loginAction as la

f = Factory().create('zh_CN')
role_name = 'role' + la.sign
addAdmin_email = la.sign + f.email()
addAdmin_password = '123456'
addAdmin_phone = f.phone_number()
addAdmin_name = la.sign + f.name()
org_name = la.sign + f.company()
org_address = la.sign + f.street_name()


class testEasyloan_web_003_role(TestBaseCase):
    def test_001_api_78dk_web_role_queryRoleList(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 分页查询
        """
        rs = ew.test_api_78dk_web_role_queryRoleList(currentpage=1, pagesize=10, codeno='', sysroleuuid='')
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_002_api_78dk_web_role_addRole(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-新增
        """
        rs = ew.test_api_78dk_web_role_addRole(seq=11, name=role_name, codeno='100011')
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_003_api_78dk_web_role_updateRole(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-新增
        """
        seq, codeno, sysroleuuid, name = eq.get_info('sys_role', 'seq,code_no,sys_role_uuid,name',
                                                     'name="{}"'.format(role_name))
        rs = ew.test_api_78dk_web_role_updateRole(seq=seq, codeno=codeno, sysroleuuid=sysroleuuid, name=name)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_004_api_78dk_web_role_updateRole(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-编辑
        """
        seq, codeno, sysroleuuid, name = eq.get_info('sys_role', 'seq,code_no,sys_role_uuid,name',
                                                     'name="{}"'.format(role_name))
        rs = ew.test_api_78dk_web_role_updateRole(seq=seq, codeno=codeno, sysroleuuid=sysroleuuid, name=name)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_005_api_78dk_web_role_queryRole(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-详情
        """
        sysroleuuid = eq.get_info('sys_role', 'sys_role_uuid')[0]
        rs = ew.test_api_78dk_web_role_queryRole(sysroleuuid=sysroleuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_006_api_78dk_web_role_delRole(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-删除
        """
        sysroleuuid = eq.get_info('sys_role', 'sys_role_uuid', 'name="{}"'.format(role_name))[0]
        rs = ew.test_api_78dk_web_role_delRole(sysroleuuid=sysroleuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_007_api_78dk_web_role_dropDown(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 岗位-删除
        """
        rs = ew.test_api_78dk_web_role_dropDown()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "codeNo")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "sysRoleUuid")

    def test_008_api_78dk_web_admin_queryAdminList(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 分页查询
        """
        rs = ew.test_api_78dk_web_admin_queryAdminList(codeno='', sysorganizationuuid='', sysroleuuid='', phone='',
                                                       name='', currentpage=1, pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "currentPage")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "orgName")

    @unittest.skip('需要调试')
    def test_009_api_78dk_web_admin_addAdmin(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 用户-新增
        """
        uuidlist = [{"status": 0, "sysAdminUuid": '', "sysOrganizationUuid": "d37ed2e35a1549d79ef75ceaecdb1447",
                     "sysRoleUuid": "4ea1007388bd4528bbfd32567b4ac87d"}]
        rs = ew.test_api_78dk_web_admin_addAdmin(
            email=addAdmin_email, username=addAdmin_email, volk='汉族', sex='男',
            password=addAdmin_password, phone=addAdmin_phone, uuidlist=uuidlist,
            name=addAdmin_name, status=0)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_010_api_78dk_web_admin_updateAdmin(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 用户-编辑
        """
        sysadminuuid = eq.get_info('sys_admin', 'sys_admin_uuid', 'email="{}"'.format(addAdmin_email))[0]
        uuidlist = [
            {"status": 0, "sysAdminUuid": sysadminuuid, "sysOrganizationUuid": "d37ed2e35a1549d79ef75ceaecdb1447",
             "sysRoleUuid": "4ea1007388bd4528bbfd32567b4ac87d"}]
        rs = ew.test_api_78dk_web_admin_updateAdmin(
            email=addAdmin_email, volk='汉族', sex='男', sysadminuuid=sysadminuuid,
            password=addAdmin_password, phone=addAdmin_phone, uuidlist=uuidlist,
            status=0)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_011_api_78dk_web_admin_queryAdmin(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 用户-详情
        """
        sysadminuuid = eq.get_info('sys_admin', 'sys_admin_uuid')[0]
        rs = ew.test_api_78dk_web_admin_queryAdmin(sysadminuuid=sysadminuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "email")
        ass.verityContain(json.loads(rs)['data'], "uuidList")
        ass.verityContain(json.loads(rs)['data'], "sysOrganizationUuid")
        # ass.verityContain(json.loads(rs)['data'], "orgName")
        ass.verityContain(json.loads(rs)['data'], "status")
        ass.verityContain(json.loads(rs)['data'], "sysAdminUuid")

    @unittest.skip('需要调试')
    def test_012_api_78dk_web_admin_resetPw(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 重置密码
        """
        sysadminuuid = eq.get_info('sys_admin', 'sys_admin_uuid', 'email="{}"'.format(addAdmin_email))[0]
        rs = ew.test_api_78dk_web_admin_resetPw(sysadminuuid=sysadminuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_013_api_78dk_web_admin_resetPw(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 重置密码
        """
        rs = ew.test_api_78dk_web_admin_resetPw(sysadminuuid='')
        ass.verity(json.loads(rs)['code'], "S0006")
        ass.verity(json.loads(rs)['msg'], "员工uuid为空！")

    def test_014_api_78dk_web_admin_delAdmin(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 用户-删除
        """
        rs = ew.test_api_78dk_web_admin_delAdmin(sysadminuuid='')
        ass.verity(json.loads(rs)['code'], "S0006")
        ass.verity(json.loads(rs)['msg'], "员工uuid为空！")

    @unittest.skip('需要调试')
    def test_015_api_78dk_web_admin_delAdmin(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 用户-删除
        """
        sysadminuuid = eq.get_info('sys_admin', 'sys_admin_uuid', 'email="{}"'.format(addAdmin_email))[0]
        rs = ew.test_api_78dk_web_admin_delAdmin(sysadminuuid=sysadminuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_016_api_78dk_web_org_dropDown(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 列表
        """
        rs = ew.test_api_78dk_web_org_dropDown()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "level")
        ass.verityContain(json.loads(rs)['data'], "orgAddress")
        ass.verityContain(json.loads(rs)['data'], "orgStatus")
        ass.verityContain(json.loads(rs)['data'], "sysOrganizationUuid")
        ass.verityContain(json.loads(rs)['data'], "puuid")

    def test_017_api_78dk_web_org_tree(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 树
        """
        rs = ew.test_api_78dk_web_org_tree()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "puuid")
        ass.verityContain(json.loads(rs)['data'], "text")
        ass.verityContain(json.loads(rs)['data'], "uuid")

    @unittest.skip('需要调试')
    def test_018_api_78dk_web_resource_menu(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 查看可见资源
        """
        rs = ew.test_api_78dk_web_resource_menu()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "attributes")
        ass.verityContain(json.loads(rs)['data'], "puuid")
        ass.verityContain(json.loads(rs)['data'], "uuid")

    @unittest.skip('需要调试')
    def test_019_api_78dk_web_org_addOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-新增
        """
        puuid = eq.get_info('sys_organization', 'puuid', 'level=1')[0]
        rs = ew.test_api_78dk_web_org_addOrg(orgmainuser=addAdmin_name, province=510000, orgaddress=org_address,
                                             level=2, orgphone=addAdmin_phone, puuid=puuid, region=510107,
                                             name=org_name,
                                             city=510100, orgstatus=0)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_020_api_78dk_web_org_updateOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-编辑
        """
        sysorganizationuuid = eq.get_info('sys_organization', 'sys_organization_uuid',
                                          'name like "%{}%"'.format(la.sign))[0]
        rs = ew.test_api_78dk_web_org_updateOrg(orgmainuser=addAdmin_name, province=510000, orgaddress=org_address,
                                                orgphone=addAdmin_phone, region=510107, name=org_name,
                                                city=510100, orgstatus=0, sysorganizationuuid=sysorganizationuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('需要调试')
    def test_021_api_78dk_web_org_queryOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-详情
        """
        sysorganizationuuid = eq.get_info('sys_organization', 'sys_organization_uuid',
                                          'name like "%{}%"'.format(la.sign))[0]
        rs = ew.test_api_78dk_web_org_queryOrg(sysorganizationuuid=sysorganizationuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data']['name'], org_name)
        ass.verityContain(json.loads(rs)['data']['orgAddress'], org_address)
        ass.verityContain(json.loads(rs)['data']['orgMainUser'], addAdmin_name)
        ass.verityContain(json.loads(rs)['data']['orgPhone'], addAdmin_phone)

    def test_022_api_78dk_web_org_queryOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-详情
        """
        rs = ew.test_api_78dk_web_org_queryOrg(sysorganizationuuid='')
        ass.verity(json.loads(rs)['code'], "S0006")
        ass.verity(json.loads(rs)['msg'], "uuid为空！")

    def test_023_api_78dk_web_org_delOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-删除
        """
        rs = ew.test_api_78dk_web_org_delOrg(sysorganizationuuid='')
        ass.verity(json.loads(rs)['code'], "S0006")
        ass.verity(json.loads(rs)['msg'], "uuid为空！")

    @unittest.skip('需要调试')
    def test_024_api_78dk_web_org_delOrg(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-删除
        """
        sysorganizationuuid = eq.get_info('sys_organization', 'sys_organization_uuid',
                                          'name like "%{}%"'.format(la.sign))[0]
        rs = ew.test_api_78dk_web_org_delOrg(sysorganizationuuid=sysorganizationuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_025_delete_org(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 组织-删除
        """
        eq.delete_info('sys_organization', 'name like "%{}%"'.format(la.sign))
