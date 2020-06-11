#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-02 下午 2:41
@Author     : 罗林
@File       : test_001_Manage.py
@desc       : manage自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import ManageSql
from finance.testAction import ManageAction, loginAction

f = Faker(locale='zh_CN')
comp_name = f.company_prefix() + loginAction.sign
linkman = f.name() + loginAction.sign
linkphone = f.phone_number()
email = loginAction.sign + f.email()


class test_001_Manage(TestBaseCase):
    def test_001_company_list(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :获取企业管理列表
        """
        rs1 = ManageAction.test_company_list(1, 10)
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_002_company_save(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :保存企业
        """
        rs = ManageAction.test_company_save(id='', name=comp_name, description='', linkman=linkman, linkphone=linkphone,
                                            licencecode='', licencefileid=38)
        Assertion.verity(json.loads(rs)['message'], '请求成功')

    def test_003_company_detail(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :获取企业详情
        """
        com_id = ManageSql.get_company_id(comp_name)
        rs2 = ManageAction.test_company_detail(com_id)
        Assertion.verity(json.loads(rs2)['message'], '请求成功')
        Assertion.verity(json.loads(rs2)['data']['companyName'], comp_name)

    def test_004_company_lock(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :停用企业
        """
        com_id = ManageSql.get_company_id(comp_name)
        rs3 = ManageAction.test_company_lock(com_id)
        Assertion.verity(json.loads(rs3)['message'], '请求成功')

    def test_005_company_unlock(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :启用企业
        """
        com_id = ManageSql.get_company_id(comp_name)
        rs4 = ManageAction.test_company_unlock(com_id)
        Assertion.verity(json.loads(rs4)['message'], '请求成功')

    def test_006_company_update(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :编辑企业
        """
        com_id = ManageSql.get_company_id(comp_name)
        licence_id = ManageSql.get_licence_file_id(comp_name)
        rs5 = ManageAction.test_company_update(id=com_id, name=comp_name, description='apitest-company',
                                               linkman=linkman, linkphone=linkphone,
                                               licencecode=licence_id, licencefileid=38)
        Assertion.verity(json.loads(rs5)['message'], '请求成功')

    def test_007_cuser_list(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :获取管理员列表
        """
        rs1 = ManageAction.test_cuser_list(pagenum=1, pagesize=10)
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_008_cuser_save(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :添加管理员
        """
        com_id = ManageSql.get_company_id(comp_name)
        rs3 = ManageAction.test_cuser_save(id='', companyid=com_id, username=linkman, userphone=linkphone,
                                           useremail=email)
        Assertion.verity(json.loads(rs3)['message'], '请求成功')

    def test_009_cuser_update(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :编辑管理员
        """
        user_id = ManageSql.get_user_id(email)
        com_id = ManageSql.get_company_id(comp_name)
        rs5 = ManageAction.test_cuser_update(id=user_id, companyid=com_id, username=linkman, userphone=linkphone,
                                             useremail=email)
        Assertion.verity(json.loads(rs5)['message'], '请求成功')

    def test_010_cuser_lock(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :锁定管理员
        """
        ManageSql.activate_user(email)
        user_id = ManageSql.get_user_id(email)
        rs6 = ManageAction.test_cuser_lock(user_id)
        Assertion.verity(json.loads(rs6)['message'], '请求成功')

    def test_011_cuser_unlock(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :解锁管理员
        """
        user_id = ManageSql.get_user_id(email)
        rs7 = ManageAction.test_cuser_unlock(user_id)
        Assertion.verity(json.loads(rs7)['message'], '请求成功')

    def test_012_cuser_detail(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :获取管理员详情
        """
        user_id = ManageSql.get_user_id(email)
        rs8 = ManageAction.test_cuser_detail(user_id)
        Assertion.verity(json.loads(rs8)['message'], '请求成功')

    def test_013_cuser_delete(self):
        """
        Time       :2019-04-02
        author     : 罗林
        desc       :删除管理员
        """
        user_id = ManageSql.get_user_id(email)
        rs9 = ManageAction.test_cuser_delete(id=user_id, state='', pagesize=10, currentpage=1)
        Assertion.verity(json.loads(rs9)['message'], '请求成功')

    def test_014_manage_save(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :新增运营人员
        """
        rs1 = ManageAction.test_manage_save(id='', managename=linkman, managephone=linkphone, manageemail=email,
                                            roleid=2)
        Assertion.verity(json.loads(rs1)['message'], '请求成功')

    def test_015_manage_sendActiveEmail(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :给运营人员发送激活邮件
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs2 = ManageAction.test_manage_sendActiveEmail(manage_user_id)
        Assertion.verity(json.loads(rs2)['message'], '请求成功')

    def test_016_manage_roles(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       :获取角色列表
        """
        rs3 = ManageAction.test_manage_roles()
        Assertion.verity(json.loads(rs3)['message'], '请求成功')

    def test_017_manage_list(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 获取运营人员列表
        """
        rs4 = ManageAction.test_manage_list(1, 10)
        Assertion.verity(json.loads(rs4)['message'], '请求成功')

    def test_018_manage_update(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 编辑运营人员
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs5 = ManageAction.test_manage_update(id=manage_user_id, managename=linkman, managephone=linkphone,
                                              manageemail=email, roleid=2)
        Assertion.verity(json.loads(rs5)['message'], '请求成功')

    def test_019_manage_lock(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 锁定运营人员
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs6 = ManageAction.test_manage_lock(manage_user_id)
        Assertion.verity(json.loads(rs6)['message'], '请求成功')

    def test_020_manage_unlock(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 解锁运营人员
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs7 = ManageAction.test_manage_unlock(manage_user_id)
        Assertion.verity(json.loads(rs7)['message'], '请求成功')

    def test_021_manage_detail(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 获取运营人员详情
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs8 = ManageAction.test_manage_detail(manage_user_id)
        Assertion.verity(json.loads(rs8)['message'], '请求成功')

    def test_022_manage_detail(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 获取运营人员详情
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs8 = ManageAction.test_manage_detail(manage_user_id)
        Assertion.verity(json.loads(rs8)['message'], '请求成功')
        Assertion.verity(json.loads(rs8)['data']['email'], email)

    def test_023_login(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 运营人员登录
        """
        ManageSql.activate_manage_user(linkman)
        rs1 = ManageAction.test_login(email, '12345678')
        Assertion.verity(json.loads(rs1)['message'], '请求成功')
        Assertion.verity(json.loads(rs1)['data']['email'], email)

    def test_024_manage_delete(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 删除运营人员
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs9 = ManageAction.test_manage_delete(manage_user_id)
        Assertion.verity(json.loads(rs9)['message'], '请求成功')

    def test_025_updatePassword(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 运营人员修改密码
        """
        manage_user_id = ManageSql.get_manage_user_id(linkman)
        rs2 = ManageAction.test_updatePassword(manage_user_id, '12345678')
        Assertion.verity(json.loads(rs2)['message'], '请求成功')

    def test_026_logout(self):
        """
        Time       :2019-04-03
        author     : 罗林
        desc       : 运营人员退出登录
        """
        rs3 = ManageAction.test_logout()
        Assertion.verity(json.loads(rs3)['message'], '请求成功')
