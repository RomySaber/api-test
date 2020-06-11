#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-17 下午 5:42
@Author     : 罗林
@File       : test_99_Del_testdata.py
@desc       :  删除测试数据
"""
import os

from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import ManageSql
from finance.mysqlQuery import FinanceSql
from finance.testAction import loginAction


class testClapp(TestBaseCase):
    def test_001_del_manage_user(self):
        # 删除新增的公司和账号
        ManageSql.del_user()

    def test_002_del_manage_info(self):
        # 删除新增的公司和账号
        ManageSql.del_manage_user()

    def test_003_del_manage_db(self):
        # 删除新增的公司和账号
        ManageSql.drop_db()

    def test_004_del_risks(self):
        # 删除风险点
        FinanceSql.del_risks()

    def test_005_del_group(self):
        # 删除分组
        FinanceSql.del_group()

    def test_006_del_gps(self):
        # 删除gps
        FinanceSql.del_gps()

    def test_007_del_finance(self):
        # 删除financeid
        FinanceSql.del_finance()

    def test_008_del_user(self):
        # 删除financeid
        FinanceSql.del_user()

    def test_009_del_role(self):
        # 删除角色
        FinanceSql.del_role()

    def test_010_del_org(self):
        # 删除组织机构信息
        FinanceSql.del_org()

    def test_011_del_json_file(self):
        os.remove(os.path.join(os.path.dirname(loginAction.__file__), 'finance_data.json'))
