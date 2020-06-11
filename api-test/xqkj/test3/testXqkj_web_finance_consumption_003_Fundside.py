#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-14 下午 2:27
@Author     : 罗林
@File       : testXqkj_web_finance_consumption_003_Fundside.py
@desc       :  资金管理流程自动化测试用例
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
# 资方名
FundSidename = fake.name() + '资方名' + loginAction.sign
# 资金包名
FundPackagename = fake.name() + '资金包名' + loginAction.sign


class testXqkj_web_finance_consumption_003_Fundside(TestBaseCase):
    def test_01_api_78dk_platform_fund_fundSide_saveFundSide_is_none(self):
        # 添加资方 ,name为空
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide('', 'enabled')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'name不能为空!')
        
    # def test_02_api_78dk_platform_fund_fundSide_saveFundSide_256name(self):
    #     # 添加资方 ,name为空
    #     res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide(''.join(fake.words(nb=128)), 'enabled')
    #     Assertion.verity(json.loads(res)['code'], '20000')
    #     Assertion.verity(json.loads(res)['msg'], 'name不能为空!')

    def test_03_api_78dk_platform_fund_fundSide_saveFundSide(self):
        # 添加资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidename, 'enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_04_api_78dk_platform_fund_fundSide_saveFundSide_name_exits(self):
        # 添加资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_saveFundSide(FundSidename, 'enabled')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '已存在资方名称 [{}]，请换个资方名称!'.format(FundSidename))

    def test_05_api_78dk_platform_fund_fundSide_viewFundSides_all(self):
        # 资方列表
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSides(
            pagecurrent=1, name='', pagesize=10, state='enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])

    def test_06_api_78dk_platform_fund_fundSide_viewFundSides(self):
        # 资方列表
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSides(
            pagecurrent=1, name=FundSidename, pagesize=10, state='enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['totalCount'], 1)
        Assertion.verity(json.loads(res)['data']['totalPage'], 1)
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])
        Assertion.verity(json.loads(res)['data']['dataList'][0]['name'], FundSidename)
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'fundSideUuid')
        global fundside_uuid
        fundside_uuid = json.loads(res)['data']['dataList'][0]['fundSideUuid']

    def test_07_api_78dk_platform_fund_fundSide_viewFundSide(self):
        # 查询资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSide(fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundSidename)
        Assertion.verity(json.loads(res)['data']['fundSideUuid'], fundside_uuid)

    def test_08_api_78dk_platform_fund_fundSide_viewFundSide_error(self):
        # 查询资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSide('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_09_api_78dk_platform_fund_fundSide_viewFundSide_not_exits(self):
        # 查询资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_viewFundSide('1234564')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['stateName'], '')

    def test_10_api_78dk_platform_fund_fundSide_updateFundSide(self):
        # 编辑资方
        res = PlatformAction.test_api_78dk_platform_fund_fundSide_updateFundSide(
            name=FundSidename, fundsideuuid=fundside_uuid, state='enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_11_api_78dk_platform_fund_fundPackage_saveFundPackage_name_is_none(self):
        # 添加资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
            amount=300000, name='', state='enabled', fundsideuuid=fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'name不能为空!')

    def test_12_api_78dk_platform_fund_fundPackage_saveFundPackage_amount_is_none(self):
        # 添加资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
            amount='', name=FundPackagename, state='enabled', fundsideuuid=fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '总额度不能为空,')

    def test_13_api_78dk_platform_fund_fundPackage_saveFundPackage_fundside_uuid_is_none(self):
        # 添加资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
            amount=300000, name=FundPackagename, state='enabled', fundsideuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'fundSideUuid不能为空!')

    def test_14_api_78dk_platform_fund_fundPackage_saveFundPackage(self):
        # 添加资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
            amount=300000000000000000000000, name=FundPackagename, state='enabled', fundsideuuid=fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '插入资金包发生失败!')

    # def test_15_api_78dk_platform_fund_fundPackage_saveFundPackage_256name(self):
    #     # 添加资金包
    #     res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
    #         amount=300000, name=''.join(fake.words(nb=128)), state='enabled', fundsideuuid=fundside_uuid)
    #     Assertion.verity(json.loads(res)['code'], '20000')
    #     Assertion.verity(json.loads(res)['msg'], '插入资金包发生失败!')

    def test_16_api_78dk_platform_fund_fundPackage_saveFundPackage(self):
        # 添加资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(
            amount=300000, name=FundPackagename, state='enabled', fundsideuuid=fundside_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_17_api_78dk_platform_fund_fundPackage_viewFundPackages(self):
        # 查询资金包列表
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackages(
            pagecurrent=1, pagesize=10, name=FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['totalCount'], 1)
        Assertion.verity(json.loads(res)['data']['totalPage'], 1)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['name'], FundPackagename)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['fundSideName'], FundSidename)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['fundSideUuid'], fundside_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'fundPackageUuid')
        global_dict.set(fundPackageUuid=json.loads(res)['data']['dataList'][0]['fundPackageUuid'])

    def test_18_api_78dk_platform_fund_fundPackage_viewFundPackages_all(self):
        # 查询资金包列表
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackages(
            pagecurrent=1, pagesize=10, name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'fundSideName')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'fundPackageUuid')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'fundSideUuid')

    def test_19_api_78dk_platform_fund_fundPackage_viewFundPackage(self):
        # 查询资金包
        global fund_package_uuid
        fund_package_uuid = global_dict.get('fundPackageUuid')
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackage(fund_package_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], FundPackagename)
        Assertion.verity(json.loads(res)['data']['fundSideName'], FundSidename)
        Assertion.verity(json.loads(res)['data']['fundPackageUuid'], fund_package_uuid)
        Assertion.verity(json.loads(res)['data']['fundSideUuid'], fundside_uuid)

    def test_20_api_78dk_platform_fund_fundPackage_viewFundPackage_error(self):
        # 查询资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_viewFundPackage('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_21_api_78dk_platform_fund_fundPackage_updateFundPackage(self):
        # 编辑资金包
        res = PlatformAction.test_api_78dk_platform_fund_fundPackage_updateFundPackage(
            fundpackageuuid=fund_package_uuid, state='enabled', amount=500000,
            fundsideuuid=fundside_uuid, name=FundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
