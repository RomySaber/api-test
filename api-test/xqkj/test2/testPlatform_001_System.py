#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from xqkj.testAction import PlatformAction
from xqkj.testAction import loginAction
from xqkj.testAction import specialAction

fake = Factory().create('zh_CN')
name = fake.name_male()
name = loginAction.sign + name
idcard = fake.ssn(min_age=18, max_age=20)
email = fake.email()
phone = fake.phone_number()


# 修改用户信息
name3 = fake.name_male()
name3 = loginAction.sign + 'modify' + name3
phone3 = fake.phone_number()
email3 = fake.email()

# 新增用户测试--非email
name4 = fake.name_male()
name4 = loginAction.sign + 'mail' + name4
phone4 = fake.phone_number()
email4 = fake.email()


# # 新增报表
# name_report = fake.name_male() + 'vcvdsfsdfsdfdsfsdfdsfxx报表'
# address_report = 'www.baidu.com'


class testPlatform_001_System(TestBaseCase):
    def test_01api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email, name=name, mobile=phone)
        print(res)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_sys_user_viewSystemUserList(self):
        # 查询用户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList(name, 1, 10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['dataList'][0]['name'], name)
        global user_uuid
        user_uuid = res['data']['dataList'][0]['platformUserProfileUuid']

    def test_03api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 不修改任何东西
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_04api_78dk_platform_sys_user_viewSystemUser(self):
        # 查询用户
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')
        # Assertion.verity(json.loads(res2)['data']['name'],name)

    def test_05api_78dk_platform_sys_user_updateUserPass(self):
        # 修改密码
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_user_updateUserPass('1', '1', email, user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_sys_user_updateSystemUserState_dimission(self):
        # 状态修改为离职dimission
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_dimission')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_07api_78dk_platform_sys_user_login2(self):
        # 离职状态  用户登录
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '123456')
        print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '你已经离职，不能再登陆')

    def test_08api_78dk_platform_sys_user_updateSystemUserState_enabled(self):
        # 状态修改为user_state_enabled 启用
        # res1 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_09api_78dk_platform_sys_user_login(self):
        # 启用 用户登录成功
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '1')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_10api_78dk_platform_sys_user_loginpasserror(self):
        # 用户登录  密码错误
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_11api_78dk_platform_sys_user_loginusererror(self):
        # 用户登录  账号错误
        res = PlatformAction.test_api_78dk_platform_sys_user_login('eed@qq.com', '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_12api_78dk_platform_sys_user_resetUserPass(self):
        # 重置密码
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_user_resetUserPass(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_13api_78dk_platform_sys_privilege_saveUserPrivilege(self):
        # 新增/修改权限
        sql = 'name="' + name + '" and state ="enabled"'
        platform_privilege_uuid0 = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
                                                         'platform_privilege_uuid', 'name="渠道管理" and state ="enabled"')
        platform_privilege_uuid1 = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
                                                         'platform_privilege_uuid', 'name="渠道列表" and state ="enabled"')
        platform_user_profile_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile',
                                                           'platform_user_profile_uuid', sql)
        platform_privilege_uuid = [
            {"platformPrivilegeUuid": platform_privilege_uuid0, "platformUserUuid": platform_user_profile_uuid},
            {"platformPrivilegeUuid": platform_privilege_uuid1, "platformUserUuid": platform_user_profile_uuid}]
        res = specialAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(platform_privilege_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_14api_78dk_platform_sys_privilege_viewUserPrivilegeList(self):
        # 查询权限
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(user_uuid, '')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_15api_78dk_platform_sys_privilege_clearUserPrivilege(self):
        # 清除用户权限
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_privilege_clearUserPrivilege(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_16api_78dk_platform_sys_user_viewSystemUser(self):
        #  清除用户权限 查询用户
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_17api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 email
        # res1 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email3, phone, user_uuid)
        print(json.loads(res2))
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_18api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 phone
        # res1 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone3, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_19api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 name
        # res1 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name3, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_20api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 name  phone
        # res1 = PlatformAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        # sql = 'name="' + name3 + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = PlatformAction.test_api_78dk_platform_sys_user_updateSystemUser(name, email, phone, user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_21api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增 相同email,phone,name用户
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email, name, phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email))

    def test_22api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增 相同phone,name用户
        # email3 = fake.email()
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(fake.email(), name, phone)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机号【{}】已经存在!'.format(phone))

    def test_23api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户不是email
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser('gggggggggg', name4, phone4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,邮箱的格式不合法,')

    def test_24api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 10
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '1354323456', name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_25api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 12
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '135432345665', name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_26api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 12
        res = PlatformAction.test_api_78dk_platform_sys_user_saveSystemUser(email4, '43543234566', name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

        # def test_27api_78dk_platform_sys_privilege_saveMenu(self):
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

    def test_28api_78dk_platform_sys_user_deleteSystemUser(self):
        # 删除用户
        # sql = 'name="' + name + '" and state ="enabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_sys_user_deleteSystemUser(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_29api_78dk_platform_sys_user_deleteSystemUserlogin(self):
        # 删除用户, 进行登录
        # sql = 'name="' + name + '" and state ="disabled"'
        # user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        PlatformAction.test_api_78dk_platform_sys_user_updateUserPass(email, '123456', '123456', user_uuid)
        res = PlatformAction.test_api_78dk_platform_sys_user_login(email, '123456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')
             
    def test_30_delete_test_user(self):
        #  test-API
        user_uuids = MysqlClent.select(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                       'name like "%test-API%"')
        MysqlClent.delete(loginAction.DB, 'Tbl_PlatformUserProfile', 'name like "%test-API%"')
        for user_uuid in user_uuids:
            MysqlClent.delete(loginAction.DB, 'Tbl_PlatformUserPrivilegeRelation',
                              'platform_user_uuid="{}"'.format(user_uuid))
