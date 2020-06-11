#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction
from xqkj.testAction import specialAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
# 系统用户基本信息
name = loginAction.sign + fake.name_male()
idcard = fake.ssn(min_age=18, max_age=20)
email = loginAction.sign + fake.email()
phone = '131' + fake.ean8()

# 修改用户信息
name3 = loginAction.sign + 'modify' + fake.name_male()
phone3 = '131' + fake.ean8()
email3 = loginAction.sign + fake.email()

# 新增用户测试--非email
name4 = loginAction.sign + 'mail' + fake.name_male()
phone4 = '131' + fake.ean8()
email4 = loginAction.sign + fake.email()

# 新增报表
name_report = fake.name_male() + 'vcvdsfsdfsdfdsfsdfdsfxx报表'
address_report = 'www.baidu.com'


class testXqkj_web_finance_consumption_007_System(TestBaseCase):
    def test_001_api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增系统用户
        res = json.loads(
            PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email, name=name, mobile=phone))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_002_api_78dk_platform_sys_user_viewSystemUserList_name_none(self):
        # 查询用户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('', 1, 10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_sys_user_viewSystemUserList_not_exits(self):
        # 查询用户列表
        res = json.loads(
            PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList(''.join(fake.words(nb=128)), 1, 10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_api_78dk_platform_sys_user_viewSystemUserList(self):
        # 查询用户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList(name, 1, 10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['dataList'][0]['name'], name)
        global user_uuid
        user_uuid = res['data']['dataList'][0]['platformUserProfileUuid']

    def test_005_api_78dk_platform_sys_user_viewSystemUser_none(self):
        # 查询用户
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser('')
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '您提交的参数异常')

    def test_006_api_78dk_platform_sys_user_viewSystemUser(self):
        # 查询用户
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_007_api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 不修改任何东西
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_008_api_78dk_platform_sys_user_updateUserPass(self):
        # 修改密码
        res = PlatformAction.test_api_78dk_platform_sys_user_updateUserPass('1', '1', email, user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_009_api_78dk_platform_sys_user_updateSystemUser_10_phone(self):
        # 修改用户 phone
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, '1234567890', user_uuid)
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '手机格式不合法,')

    def test_010_api_78dk_platform_sys_user_updateSystemUser_12_phone(self):
        # 修改用户 phone
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, '123456789012', user_uuid)
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '手机格式不合法,')

    def test_011_api_78dk_platform_sys_user_updateSystemUser_phone(self):
        # 修改用户 phone
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone3, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_012_api_78dk_platform_sys_user_updateSystemUser_name(self):
        # 修改用户 name
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name3, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_013_api_78dk_platform_sys_user_updateSystemUser_name_phone(self):
        # 修改用户 name  phone
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_014_api_78dk_platform_sys_user_updateSystemUser_mail(self):
        # 修改用户 email
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email3, phone, user_uuid)
        print(json.loads(res2))
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_015_api_78dk_platform_sys_user_updateSystemUserState_dimission(self):
        # 状态修改为离职dimission
        res = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_dimission')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_016_api_78dk_platform_sys_user_viewSystemUser_dimission(self):
        # 查询用户
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_017_api_78dk_platform_sys_user_login_dimission(self):
        # 离职状态  用户登录
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '123456')
        print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_018_api_78dk_platform_sys_user_saveSystemUser_dimission_phone_exit(self):
        # 新增 与离职状态相同email,phone,name用户
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email3, name, phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email3))

    def test_019_api_78dk_platform_sys_user_updateSystemUserState_enabled(self):
        # 状态修改为user_state_enabled 启用
        res = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_020_api_78dk_platform_sys_user_login(self):
        # 启用 用户登录成功
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '1')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_021_api_78dk_platform_sys_user_login_passerror(self):
        # 用户登录  密码错误
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_022_api_78dk_platform_sys_user_login_usererror(self):
        # 用户登录  账号错误
        res = PlatformAction.test_api_78dk_platform_sys_user_login('eed@qq.com', '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_023_api_78dk_platform_sys_user_login_not_privilege(self):
        # 没有权限  用户登录
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '123456')
        print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_024_api_78dk_platform_sys_user_resetUserPass(self):
        # 重置密码
        res = PlatformAction.test_api_78dk_platform_sys_user_resetUserPass(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_025_api_78dk_platform_sys_privilege_saveUserPrivilege_one_privilege(self):
        # 新增/修改权限
        platform_privilege_uuid0 = xqkj_query.get_info('Tbl_PlatformPrivilege', 'platform_privilege_uuid',
                                                       'name="渠道管理"', 'state ="enabled"')[0]
        platform_user_profile_uuid = xqkj_query.get_info('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                                         'name="{}"'.format(name), 'state ="enabled"')[0]
        platform_privilege_uuid = [
            {"platformPrivilegeUuid": platform_privilege_uuid0, "platformUserUuid": platform_user_profile_uuid}]
        res = specialAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(platform_privilege_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_026_api_78dk_platform_sys_privilege_saveUserPrivilege_all_privilege(self):
        # 新增/修改权限
        privilege_uuids = xqkj_query.get_tbl_infos('Tbl_PlatformPrivilege', 'platform_privilege_uuid',
                                                   'state ="enabled"')
        user_uuid = xqkj_query.get_info('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                        'name="{}"'.format(name), 'state ="enabled"')[0]
        privilege = [{"platformPrivilegeUuid": uid, "platformUserUuid": user_uuid} for uid in privilege_uuids]
        res = specialAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(privilege)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_027_api_78dk_platform_sys_privilege_saveUserPrivilege(self):
        # 新增/修改权限
        platform_privilege_uuid0 = xqkj_query.get_info('Tbl_PlatformPrivilege', 'platform_privilege_uuid',
                                                       'name="渠道管理"', 'state ="enabled"')[0]
        platform_privilege_uuid1 = xqkj_query.get_info('Tbl_PlatformPrivilege', 'platform_privilege_uuid',
                                                       'name="渠道列表"', 'state ="enabled"')[0]
        platform_user_profile_uuid = xqkj_query.get_info('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                                         'name="{}"'.format(name), 'state ="enabled"')[0]
        platform_privilege_uuid = [
            {"platformPrivilegeUuid": platform_privilege_uuid0, "platformUserUuid": platform_user_profile_uuid},
            {"platformPrivilegeUuid": platform_privilege_uuid1, "platformUserUuid": platform_user_profile_uuid}]
        res = specialAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(platform_privilege_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_028_api_78dk_platform_sys_privilege_viewUserPrivilegeList(self):
        # 查询权限
        res = PlatformAction.test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(user_uuid, '')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_sys_privilege_clearUserPrivilege(self):
        # 清除用户权限
        res = PlatformAction.test_api_78dk_platform_sys_privilege_clearUserPrivilege(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_030_api_78dk_platform_sys_user_viewSystemUser(self):
        #  清除用户权限 查询用户
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_031_api_78dk_platform_sys_user_saveSystemUser_phone_exit(self):
        # 新增 相同email,phone,name用户
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email, name, phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机号【{}】已经存在!'.format(phone))

    def test_032_api_78dk_platform_sys_user_saveSystemUser_mail_exit(self):
        # 新增 相同phone,name用户
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email3, name, phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email3))

    def test_033_api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户不是email
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser('gggggggggg', name4, phone4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_034_api_78dk_platform_sys_user_saveSystemUser_phone_ten(self):
        # 新增用户 手机号错误 10
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '1354323456', name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_035_api_78dk_platform_sys_user_saveSystemUser_12_phone(self):
        # 新增用户 手机号错误 12
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '135432345665', name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_036_api_78dk_platform_sys_user_saveSystemUser_phone_error(self):
        # 新增用户 手机号格式错误 11
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '43543234566', name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

        # def test_037_api_78dk_platform_sys_privilege_saveMenu(self):
        #     # 保存一个菜单
        #     # {'platformPrivilegeUuid': '菜单uuid（N）', 'name': '菜单名称（Y）', 'url': '菜单路径（Y）'}
        #     res = PlatformAction.test_api_78dk_platform_sys_privilege_saveMenu(address_report, '123', name_report)
        #     sql = 'name="' + name_report + '" and state ="enabled"'
        #     platformPrivilegeUuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
        #                                                   'platform_privilege_uuid', sql)
        #
        #     Assertion.verity(json.loads(res)['msg'], '成功')
        #     Assertion.verity(json.loads(res)['code'], '10000')
        #     # Assertion.verity(json.loads(res)['data']['permissionTypeName'], '权限类型')
        #     # Assertion.verity(json.loads(res)['data']['url'], '菜单url')
        #     Assertion.verity(json.loads(res)['data']['platformPrivilegeUuid'], platformPrivilegeUuid)
        #     # Assertion.verity(json.loads(res)['data']['permissionType'], '权限类型')
        #     # Assertion.verity(json.loads(res)['data']['name'], '菜单名称')

    def test_038_api_78dk_platform_sys_user_deleteSystemUser(self):
        # 删除用户
        res = PlatformAction.test_api_78dk_platform_sys_user_deleteSystemUser(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_sys_user_deleteSystemUserlogin(self):
        # 删除用户, 进行登录
        PlatformAction.test_api_78dk_platform_sys_user_updateUserPass('123456', '123456', email, user_uuid)
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '123456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')
