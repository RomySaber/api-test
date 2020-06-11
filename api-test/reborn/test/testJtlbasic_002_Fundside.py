#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from reborn.testAction import PlatformAction as JtlbasicAction, loginAction

fake = Factory().create('zh_CN')
# 资方名
FundSidename = fake.name_male() + '资方名'
FundSidenamedele = fake.name_male() + '资方名dele'
# 资金包名
FundPackagename = fake.name_male() + '资金包名'
# 产品使用资金包
pFundSidename = fake.name_male() + '资方名'
pFundPackagename = fake.name_male() + '资金包名'


# 资方管理相关接口

class testJtlbasic_002_Fundside(TestBaseCase):
    def test_01api_78dk_platform_fund_fundSide_saveFundSide(self):
        # 添加资方
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidename, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_fund_fundSide_updateFundSide(self):
        # 编辑资方
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_updateFundSide(name=FundSidename,
                                                                                 fundsideuuid=fundside_uuid,
                                                                                 state='enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_03api_78dk_platform_fund_fundSide_viewFundSide(self):
        # 查询资方
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_viewFundSide(fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundSidename)

    def test_04api_78dk_platform_fund_fundSide_viewFundSides(self):
        # 资方列表
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_viewFundSides(pagecurrent=1, name=FundSidename,
                                                                                pagesize=10, state='enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 资金包相关管理 需要先有资方
    def test_05api_78dk_platform_fund_fundPackage_saveFundPackage(self):
        # 添加资金包
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)  # 资方uuid
        res = JtlbasicAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(amount=300000,
                                                                                     name=FundPackagename,
                                                                                     state='enabled',
                                                                                     fundsideuuid=fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_fund_fundPackage_updateFundPackage(self):
        # 编辑资金包
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        sql = 'name="' + FundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_fund_fundPackage_updateFundPackage(
            fundpackageuuid=fund_package_uuid, state='enabled',
            amount=500000, fundsideuuid=fundside_uuid,
            name=FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_07api_78dk_platform_fund_fundPackage_viewFundPackage(self):
        # 查询资金包
        sql = 'name="' + FundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_fund_fundPackage_viewFundPackage(fund_package_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundPackagename)

    def test_08api_78dk_platform_fund_fundPackage_viewFundPackages(self):
        # 查询资金包列表
        res = JtlbasicAction.test_api_78dk_platform_fund_fundPackage_viewFundPackages(pagecurrent=1, pagesize=10,
                                                                                      name=FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_09api_78dk_platform_fund_fundSide_deleteFundSide(self):
        # 删除资方 FundSidenamedele
        # 添加资方
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidenamedele, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # 删除资方
        sql = 'name="' + FundSidenamedele + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_deleteFundSide(fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
