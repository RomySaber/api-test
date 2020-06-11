#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.mydb import MysqlClent
from common.myCommon.TestBaseCase import TestBaseCase
from common.myCommon import Assertion
import json
from faker import Factory
from xqkj.testAction import loginAction
from xqkj.testAction import PlatformAction

fake = Factory().create('zh_CN')
# 资方名
FundSidename = fake.name_male() + '资方名' + loginAction.sign
FundSidenamedele = fake.name_male() + '资方名dele' + loginAction.sign
# 资金包名
FundPackagename = fake.name_male() + '资金包名' + loginAction.sign
# 产品使用资金包
pFundSidename = fake.name_male() + '资方名'+ loginAction.sign
pFundPackagename = fake.name_male() + '资金包名' + loginAction.sign


# 资方管理相关接口

class testPlatform_002_Fundside(TestBaseCase):
    def test_01api_78dk_platform_fund_fundSide_saveFundSide(self):
        # 添加资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidename, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_fund_fundSide_updateFundSide(self):
        # 编辑资方
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_updateFundSide(FundSidename, fundside_uuid, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_03api_78dk_platform_fund_fundSide_viewFundSide(self):
        # 查询资方
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSide(fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundSidename)

    def test_04api_78dk_platform_fund_fundSide_viewFundSides(self):
        # 资方列表
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSides(1, FundSidename, 10, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 资金包相关管理 需要先有资方
    def test_05api_78dk_platform_fund_fundPackage_saveFundPackage(self):
        # 添加资金包
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)  # 资方uuid
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(300000, FundPackagename, 'enabled',
                                                                                     fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_fund_fundPackage_updateFundPackage(self):
        # 编辑资金包
        sql = 'name="' + FundSidename + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        sql = 'name="' + FundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_updateFundPackage(fund_package_uuid, 'enabled',
                                                                                       500000, fundside_uuid, FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_07api_78dk_platform_fund_fundPackage_viewFundPackage(self):
        # 查询资金包
        sql = 'name="' + FundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackage(fund_package_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundPackagename)

    def test_08api_78dk_platform_fund_fundPackage_viewFundPackages(self):
        # 查询资金包列表
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackages(1, 10, FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_09api_78dk_platform_fund_fundSide_deleteFundSide(self):
        # 删除资方 FundSidenamedele
        # 添加资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidenamedele, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # 删除资方
        sql = 'name="' + FundSidenamedele + '" and state ="enabled"'
        fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_deleteFundSide(fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_10api_78dk_platform_fund_fundPackage_deleteFundPackage(self):
        # 删除资金包
        sql = 'name="' + FundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_deleteFundPackage(fund_package_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
