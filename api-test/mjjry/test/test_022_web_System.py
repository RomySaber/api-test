#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-06-11 下午 3:33
@Author     : 罗林
@File       : test_022_web_System.py
@desc       : 系统管理自动化测试用例
"""

import json
from faker import Factory
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from mjjry.query import xqkj_query
from mjjry.testAction import WebAction
from mjjry.testAction import loginAction
from mjjry.testAction import specialAction


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


class test_022_web_System(TestBaseCase):
    def test_001_api_78dk_platform_sys_user_saveSystemUser(self):
        """
        新增系统用户
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email, name=name, mobile=phone))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_002_api_78dk_platform_sys_user_viewSystemUserList_name_none(self):
        """
        查询用户列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sys_user_viewSystemUserList(name='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_sys_user_viewSystemUserList_not_exits(self):
        """
        查询用户列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sys_user_viewSystemUserList(name=''.join(fake.words(nb=128)),
                                                                         pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_api_78dk_platform_sys_user_viewSystemUserList(self):
        """
        查询用户列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sys_user_viewSystemUserList(name=name, pagesize=20, pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['dataList'][0]['name'], name)
        global user_uuid
        user_uuid = res['data']['dataList'][0]['platformUserProfileUuid']

    def test_005_api_78dk_platform_sys_user_viewSystemUser_none(self):
        """
        查询用户
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_viewSystemUser('')
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '您提交的参数异常')

    def test_006_api_78dk_platform_sys_user_viewSystemUser(self):
        """
        查询用户
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_007_api_78dk_platform_sys_user_updateSystemUser(self):
        """
        修改用户 不修改任何东西
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email, mobile=phone,
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_008_api_78dk_platform_sys_user_updateUserPass(self):
        """
        修改密码
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_updateUserPass(password='1', passwordrepeat='1',
                                                                       email=email, uid=user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_009_api_78dk_platform_sys_user_updateSystemUser_10_phone(self):
        """
        修改用户 phone
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email,
                                                                          mobile='1234567890',
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '手机格式不合法,')

    def test_010_api_78dk_platform_sys_user_updateSystemUser_12_phone(self):
        """
        修改用户 phone
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email,
                                                                          mobile='1234567890',
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '20000')
        Assertion.verity(json.loads(res2)['msg'], '手机格式不合法,')

    def test_011_api_78dk_platform_sys_user_updateSystemUser_phone(self):
        """
        修改用户 phone
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email, mobile=phone3,
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_012_api_78dk_platform_sys_user_updateSystemUser_name(self):
        """
        修改用户 name
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name3, email=email, mobile=phone,
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_013_api_78dk_platform_sys_user_updateSystemUser_name_phone(self):
        """
        修改用户 name  phone
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name4, email=email, mobile=phone4,
                                                                          platformuserprofileuuid=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_014_api_78dk_platform_sys_user_updateSystemUser_mail(self):
        """
        修改用户 email
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_updateSystemUser(name=name, email=email3, mobile=phone4,
                                                                          platformuserprofileuuid=user_uuid)
        print(json.loads(res2))
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_015_api_78dk_platform_sys_user_updateSystemUserState_dimission(self):
        """
        态修改为离职dimission
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_updateSystemUserState(uid=user_uuid,
                                                                              updatestate='user_state_dimission')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_016_api_78dk_platform_sys_user_viewSystemUser_dimission(self):
        """
        查询用户
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_viewSystemUser(paramsingle=user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_017_api_78dk_platform_sys_user_login_dimission(self):
        """
        离职状态  用户登录
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_login(email=email, password='123456')
        print(json.loads(res))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_018_api_78dk_platform_sys_user_saveSystemUser_dimission_phone_exit(self):
        """
        新增 与离职状态相同email,phone,name用户
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email3, name=name, mobile=phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email3))

    def test_019_api_78dk_platform_sys_user_updateSystemUserState_enabled(self):
        """
        状态修改为user_state_enabled 启用
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_updateSystemUserState(uid=user_uuid,
                                                                              updatestate='user_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_020_api_78dk_platform_sys_user_login(self):
        """
        启用 用户登录成功
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_login(email=email, password='1')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_021_api_78dk_platform_sys_user_login_passerror(self):
        """
        用户登录  密码错误
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_login(email=email, password='1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_022_api_78dk_platform_sys_user_login_usererror(self):
        """
        用户登录  账号错误
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_login(email='eed@qq.com', password='1235456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_023_api_78dk_platform_sys_user_login_not_privilege(self):
        """
        没有权限  用户登录
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_login(email=email, password='123456')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '用户名或密码不正确!')

    def test_024_api_78dk_platform_sys_user_resetUserPass(self):
        """
        重置密码
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_resetUserPass(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_025_api_78dk_platform_sys_privilege_saveUserPrivilege_one_privilege(self):
        """
        新增/修改权限
        :return:
        """
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
        """
        新增/修改权限
        :return:
        """
        privilege_uuids = xqkj_query.get_tbl_infos('Tbl_PlatformPrivilege', 'platform_privilege_uuid',
                                                   'state ="enabled"')
        user_uuid1 = xqkj_query.get_info('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                         'name="{}"'.format(name), 'state ="enabled"')[0]
        privilege = [{"platformPrivilegeUuid": uid, "platformUserUuid": user_uuid1} for uid in privilege_uuids]
        res = specialAction.test_api_78dk_platform_sys_privilege_saveUserPrivilege(privilege)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_027_api_78dk_platform_sys_privilege_saveUserPrivilege(self):
        """
        新增/修改权限
        :return:
        """
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
        """
        查询权限
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(platformuseruuid=user_uuid,
                                                                                   permissiontype='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_sys_privilege_clearUserPrivilege(self):
        """
        清除用户权限
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_privilege_clearUserPrivilege(user_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_030_api_78dk_platform_sys_user_viewSystemUser(self):
        """
        清除用户权限 查询用户
        :return:
        """
        res2 = WebAction.test_api_78dk_platform_sys_user_viewSystemUser(user_uuid)
        Assertion.verity(json.loads(res2)['code'], '10000')
        Assertion.verity(json.loads(res2)['msg'], '成功')

    def test_031_api_78dk_platform_sys_user_saveSystemUser_mail_exit(self):
        """
        新增 相同phone,name用户
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email3, name=name, mobile=phone)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱【{}】已经存在!'.format(email3))

    def test_032_api_78dk_platform_sys_user_saveSystemUser(self):
        """
        新增用户不是email
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email='gggggggggg', name=name4,
                                                                       mobile=phone4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_033_api_78dk_platform_sys_user_saveSystemUser_phone_ten(self):
        """
        新增用户 手机号错误 10
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='1354323456',
                                                                       name=name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_034_api_78dk_platform_sys_user_saveSystemUser_12_phone(self):
        """
        新增用户 手机号错误 12
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='135432345665',
                                                                       name=name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_035_api_78dk_platform_sys_user_saveSystemUser_phone_error(self):
        """
        新增用户 手机号格式错误 11
        :return:
        """
        res = WebAction.test_api_78dk_platform_sys_user_saveSystemUser(email=email4, mobile='43543234566',
                                                                       name=name4)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_036_api_78dk_platform_common_findQiniuToken_none(self):
        """
        获取七牛tocken
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_findQiniuToken('')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_037_api_78dk_platform_common_findQiniuToken_error(self):
        """
        获取七牛tocken
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_findQiniuToken('123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_038_api_78dk_platform_common_viewImageUrl(self):
        """
        获取图片url
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_viewImageUrl(qiniukey='', type='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_039_api_78dk_platform_file_download(self):
        """
        文件下载
        :return:
        """
        WebAction.test_api_78dk_platform_file_download(filename='', urlstr='')
