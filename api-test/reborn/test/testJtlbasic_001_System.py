#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from reborn.testAction import PlatformAction as JtlbasicAction, loginAction

fake = Factory().create('zh_CN')
name = fake.name_male()
name = name + 'test'
idcard = fake.ssn(min_age=18, max_age=20)
phone = fake.ean8()
email = fake.email()
phone = '135' + phone

# 删除用户
name1 = fake.name_male()
name1 = name1 + 'dele'
phone1 = fake.ean8()
email1 = fake.email()
phone1 = '135' + phone1

# 清除用户权限
name2 = fake.name_male()
name2 = name2 + 'clear'
phone2 = fake.ean8()
email2 = fake.email()
phone2 = '135' + phone2

# 修改用户信息
name3 = fake.name_male()
name3 = name3 + 'modify'
phone3 = fake.ean8()
email3 = fake.email()
phone3 = '135' + phone3

# 新增用户测试--非email
name4 = fake.name_male()
name4 = name4 + 'testmail'
phone4 = fake.ean8()
email4 = fake.email()
phone4 = '135' + phone4

# 新增报表
name_report = fake.name_male() + 'vcvdsfsdfsdfdsfsdfdsfxx报表'
address_report = 'www.baidu.com'


class testJtlbasic_001_System(TestBaseCase):
    def test_01api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email, name=name, mobile=phone)
        print(res)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_sys_user_viewSystemUserList(self):
        # 查询用户列表
        res = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList(name, 1, 10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['name'], name)

    def test_03api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 不修改任何东西
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email, mobile=phone,
                                                                               platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_19api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 email
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email3, mobile=phone,
                                                                               platformuserprofileuuid=user_uuid)
        print(json.loads(res2))
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_20api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 phone
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email, mobile=phone3,
                                                                               platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_21api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 name
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name3, email=email, mobile=phone,
                                                                               platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_22api_78dk_platform_sys_user_updateSystemUser(self):
        # 修改用户 name  phone
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name3 + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email, mobile=phone,
                                                                               platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_04api_78dk_platform_sys_user_viewSystemUser(self):
        # 查询用户
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')
        # Assertion.verity(json.loads(res2)['data']['name'],name)

    def test_05api_78dk_platform_sys_user_updateUserPass(self):
        # 修改密码
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_updateUserPass(password='1', passwordrepeat='1',
                                                                            email=email, uid=user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_sys_user_updateSystemUserState_dimission(self):
        # 状态修改为离职dimission
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_dimission')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_07api_78dk_platform_sys_user_login2(self):
        # 离职状态  用户登录
        res = JtlbasicAction.test_api_78dk_platform_sys_user_login(email, '123456')
        print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '你已经离职，不能再登陆')

    def test_08api_78dk_platform_sys_user_updateSystemUserState_enabled(self):
        # 状态修改为user_state_enabled 启用
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid, 'user_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # def test_7api_78dk_platform_sys_user_updateSystemUserState_enabled (self):
    #     # 状态修改为启用enabled
    #     # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
    #     # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
    #     sql = 'name="' + name + '" and state ="enabled"'
    #     user_uuid = MysqlClent.select_one(loginAction.DB,'Tbl_PlatformUserProfile',sql,'platform_user_profile_uuid')
    #     res = JtlbasicAction.test_api_78dk_platform_sys_user_updateSystemUserState(user_uuid,'enabled')
    #     Assertion.verity(json.loads(res)['code'],'10000')
    #     Assertion.verity(json.loads(res)['msg'],'成功')

    def test_09api_78dk_platform_sys_user_login(self):
        # 启用 用户登录成功
        res = JtlbasicAction.test_api_78dk_platform_sys_user_login(email, '1')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_10api_78dk_platform_sys_user_loginpasserror(self):
        # 用户登录  密码错误
        res = JtlbasicAction.test_api_78dk_platform_sys_user_login(email, '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_11api_78dk_platform_sys_user_loginusererror(self):
        # 用户登录  账号错误
        res = JtlbasicAction.test_api_78dk_platform_sys_user_login('eed@qq.com', '1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_12api_78dk_platform_sys_user_resetUserPass(self):
        # 重置密码
        # res1 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUserList('蛋蛋',1,10)  # 调用根据名称查询用户列表接口
        # user_uuid = json.loads(res1)['data']['dataList']['platformUserProfileUuid']  # 获取用户uuid
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_resetUserPass(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_13api_78dk_platform_sys_privilege_saveUserPrivilege(self):
        # 新增/修改权限
        sql = 'name="' + name + '" and state ="enabled"'
        print(name)
        platform_privilege_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
                                                        'platform_privilege_uuid', 'name="信审管理" and state ="enabled"')
        platform_user_profile_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile',
                                                           'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(platform_privilege_uuid,
                                                                                    platform_user_profile_uuid)
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '成功')

    def test_14api_78dk_platform_sys_privilege_viewUserPrivilegeList(self):
        # 查询权限
        sql = 'name="' + name + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(platformuseruuid=user_uuid,
                                                                                        permissiontype='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # print(json.loads(res)['data'])
        # Assertion.verity(json.loads(res)['data']['name'],['蛋蛋'])

    def test_15api_78dk_platform_sys_user_deleteSystemUser(self):
        # 删除用户
        JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email1, name=name1, mobile=phone1)
        sql = 'name="' + name1 + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_deleteSystemUser(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_16api_78dk_platform_sys_user_deleteSystemUserlogin(self):
        # 删除用户, 进行登录
        sql = 'name="' + name1 + '" and state ="disabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        JtlbasicAction.test_api_78dk_platform_sys_user_updateUserPass(email1, '123456', '123456', user_uuid)
        res = JtlbasicAction.test_api_78dk_platform_sys_user_login(email1, '123456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_17api_78dk_platform_sys_privilege_clearUserPrivilege(self):
        # 清除用户权限
        JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email2, phone2, name2)
        sql = 'name="' + name2 + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        platform_privilege_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
                                                        'platform_privilege_uuid', 'name="产品管理" and state ="enabled"')
        res = JtlbasicAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(platform_privilege_uuid, user_uuid)
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '成功')
        res = JtlbasicAction.test_api_78dk_platform_sys_privilege_clearUserPrivilege(user_uuid)
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '成功')

    def test_18api_78dk_platform_sys_user_viewSystemUser(self):
        #  清除用户权限 查询用户
        sql = 'name="' + name2 + '" and state ="enabled"'
        user_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformUserProfile', 'platform_user_profile_uuid', sql)
        res2 = JtlbasicAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        # print(json.loads(res2))
        # Assertion.verity(json.loads(res2)['code'], '10000')
        # Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_23api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增 相同email,phone,name用户
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email, name=name, mobile=phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email))

    def test_24api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增 相同phone,name用户
        # email3 = fake.email()
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=fake.email(), name=name, mobile=phone)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机号【{}】已经存在!'.format(phone))

    def test_25api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增 相同name用户
        # phone1 = fake.ean8()
        # phone1 = + phone1
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=fake.email(), name=name,
                                                                            mobile='135' + fake.ean8())
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_26api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户不是email
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email='gggggggggg', name=name4,
                                                                            mobile=phone4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_27api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 10
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='1354323456',
                                                                            name=name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_28api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 12
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='135432345665',
                                                                            name=name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_29api_78dk_platform_sys_user_saveSystemUser(self):
        # 新增用户 手机号错误 12
        res = JtlbasicAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='43543234566',
                                                                            name=name4)
        # print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_30api_78dk_platform_sys_privilege_saveMenu(self):
        # 保存一个菜单
        # {'platformPrivilegeUuid': '菜单uuid（N）', 'name': '菜单名称（Y）', 'url': '菜单路径（Y）'}
        res = JtlbasicAction.test_api_78dk_platform_sys_privilege_saveMenu(url=address_report,
                                                                           platformprivilegeuuid='123',
                                                                           name=name_report)
        sql = 'name="' + name_report + '" and state ="enabled"'
        platformPrivilegeUuid = MysqlClent.select_one(loginAction.DB, 'Tbl_PlatformPrivilege',
                                                      'platform_privilege_uuid', sql)

        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['data']['permissionTypeName'], '权限类型')
        # Assertion.verity(json.loads(res)['data']['url'], '菜单url')
        Assertion.verity(json.loads(res)['data']['platformPrivilegeUuid'], platformPrivilegeUuid)
        # Assertion.verity(json.loads(res)['data']['permissionType'], '权限类型')
        # Assertion.verity(json.loads(res)['data']['name'], '菜单名称')
