#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-13 下午 4:41
@Author     : 罗林
@File       : testXqkj_web_finance_consumption_002_Merchant.py
@desc       : 商户管理流程自动化测试用例
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
# 商户名称
merchantname = loginAction.sign + fake.company()
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = '15388188697'
cardnumber = fake.credit_card_number(card_type=None)
store_name = loginAction.sign + fake.company_prefix()


class testXqkj_web_finance_consumption_002_Merchant(TestBaseCase):
    def test_001_api_78dk_platform_mm_base_saveMerchant(self):
        # 新增商户基本信息
        global channelid
        channelid = global_dict.get('channelid')
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name=merchantname, parentmerchantuuid='', shortname=merchantname + '商户简称',
            channeluuid=channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'merchantUuid')
        global_dict.set(merchantUuid=res['data']['merchantUuid'])

    def test_002_api_78dk_platform_mm_base_viewMerchant(self):
        # 查询基本信息
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_base_viewMerchant(channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_mm_base_viewMerchantList(self):
        # 查询商户列表
        global merchant_uuid
        merchant_uuid = global_dict.get('merchantUuid')
        res = PlatformAction.test_api_78dk_platform_mm_base_viewMerchantList(
            pagecurrent=1, pagesize=10, name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantName'], merchantname)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['freezeState'], 'normal')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['openCloseState'], 'open')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['channelUuid'], channelid)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantUuid'], merchant_uuid)

    def test_004_api_78dk_platform_mm_base_viewMerchantList_all(self):
        # 查询商户列表
        res = PlatformAction.test_api_78dk_platform_mm_base_viewMerchantList(pagecurrent=1, pagesize=10, name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'auditState')

    def test_005_api_78dk_platform_mm_base_updateMerchant(self):
        # 修改基本信息
        res = PlatformAction.test_api_78dk_platform_mm_base_updateMerchant(
            merchantuuid=merchant_uuid, note='', parentmerchantuuid='', name=merchantname,
            channeluuid=channelid, shortname=merchantname + '商户简称')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_006_api_78dk_platform_mm_state_viewStateMerchantList_all(self):
        # 查询商户状态列表
        res = PlatformAction.test_api_78dk_platform_mm_state_viewStateMerchantList(
            name='', pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'auditState')

    def test_007_api_78dk_platform_mm_state_viewStateMerchantList(self):
        # 查询商户状态列表
        res = PlatformAction.test_api_78dk_platform_mm_state_viewStateMerchantList(
            pagecurrent=1, pagesize=10, name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_008_api_78dk_platform_mm_state_viewStateMerchantList_not_exist(self):
        # 查询商户状态列表
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = PlatformAction.test_api_78dk_platform_mm_state_viewStateMerchantList(
            pagecurrent=1, pagesize=10, name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityList(json.loads(res)['data']['dataList'], [])

    def test_009_api_78dk_platform_mm_examine_viewExamineMerchantList_all(self):
        # 查询商户审核列表
        res = PlatformAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(
            pagesize=10, pagecurrent=1, name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'auditState')

    def test_010_api_78dk_platform_mm_examine_viewExamineMerchantList(self):
        # 查询商户审核列表
        res = PlatformAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(
            pagesize=10, pagecurrent=1, name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantName'], merchantname)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['freezeState'], 'normal')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['openCloseState'], 'open')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['channelUuid'], channelid)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantUuid'], merchant_uuid)

    def test_011_api_78dk_platform_mm_examine_viewExamineMerchantList_not_exist(self):
        # 查询商户审核列表
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = PlatformAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(
            pagesize=10, pagecurrent=1, name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityList(json.loads(res)['data']['dataList'], [])

    def test_012_api_78dk_platform_mm_examine_merchanrExamine_fail(self):
        # 商户审核fail
        res = PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine(
            ispass='fail', message='不通过', uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_013_api_78dk_platform_mm_base_store_saveStore_examine_fail(self):
        # 商户审核fail为商户新增门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址', businessaddressgpsloction='', managername=store_name, managerphone=mobile,
            merchantuuid=merchant_uuid, storeuuid="", storename='', province=510000, city=510100,
            region=510104, provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_014_api_78dk_platform_mm_examine_merchanrExamine_pass(self):
        # 商户审核pass
        xqkj_query.update_info('Tbl_MerchantProfile', 'audit_state="pending_review"',
                               'merchant_uuid="{}"'.format(merchant_uuid))
        res = PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine(
            ispass='pass', message='通过', uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_015_api_78dk_platform_mm_state_updateOpenCloseState_close(self):
        # 修改商户开关为close
        res = PlatformAction.test_api_78dk_platform_mm_state_updateOpenCloseState(
            uid=merchant_uuid, updatestate='close')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_016_api_78dk_platform_mm_base_store_saveStore_State_close(self):
        # 商户开关为close 为商户新增门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址', businessaddressgpsloction='', managername=store_name, managerphone=mobile,
            merchantuuid=merchant_uuid, storeuuid="", storename='', province=510000, city=510100,
            region=510104, provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_017_api_78dk_platform_mm_state_updateOpenCloseState_open(self):
        # 修改商户开关为open
        res = PlatformAction.test_api_78dk_platform_mm_state_updateOpenCloseState(uid=merchant_uuid, updatestate='open')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_018_api_78dk_platform_mm_state_updateFreezeState_freeze(self):
        # 修改商户冻结状态为freeze
        res = PlatformAction.test_api_78dk_platform_mm_state_updateFreezeState(uid=merchant_uuid, updatestate='freeze')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_019_api_78dk_platform_mm_base_store_saveStore_State_freeze(self):
        # 商户冻结状态为freeze 为商户新增门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址', businessaddressgpsloction='', managername=store_name, managerphone=mobile,
            merchantuuid=merchant_uuid, storeuuid="", storename='', province=510000, city=510100,
            region=510104, provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_020_api_78dk_platform_mm_state_updateFreezeState_normal(self):
        # 修改商户冻结状态为normal
        res = PlatformAction.test_api_78dk_platform_mm_state_updateFreezeState(uid=merchant_uuid, updatestate='normal')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_021_api_78dk_platform_mm_money_saveMerchantMoney(self):
        # 新增额度管理
        res = PlatformAction.test_api_78dk_platform_mm_money_saveMerchantMoney(
            amountday=150000, amountmonth=3000000, amountsingle=30000, amountsum=5000000,
            merchantuuid=merchant_uuid, moneyconfiguuid='', zoomcoefficient=0.5)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_022_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self):
        # 根据商户Uuid查询额度管理
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['merchantUuid'], merchant_uuid)
        Assertion.verity(json.loads(res)['data']['zoomCoefficient'], 0.5)
        Assertion.verityContain(json.loads(res)['data'], 'moneyConfigUuid')
        global money_config_uuid
        money_config_uuid = json.loads(res)['data']['moneyConfigUuid']

    def test_023_api_78dk_platform_mm_money_updateMerchantMoney(self):
        # 修改额度管理
        res = PlatformAction.test_api_78dk_platform_mm_money_updateMerchantMoney(
            amountday=10000, amountmonth=300000, amountsingle=10000, amountsum=500000,
            merchantuuid=merchant_uuid, moneyconfiguuid=money_config_uuid, zoomcoefficient=1.5)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_024_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self):
        # 根据商户Uuid查询额度管理
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['merchantUuid'], merchant_uuid)
        Assertion.verity(json.loads(res)['data']['zoomCoefficient'], 1.5)
        Assertion.verity(json.loads(res)['data']['moneyConfigUuid'], money_config_uuid)

    def test_025_api_78dk_platform_mm_money_viewMerchantMoneyList_all(self):
        # 风险控制列表
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(pagecurrent=1, pagesize=10, name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')

    def test_026_api_78dk_platform_mm_money_viewMerchantMoneyList_not_exits(self):
        # 风险控制列表
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(
            pagecurrent=1, pagesize=10, name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityNone(json.loads(res)['data']['dataList'])
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')

    def test_027_api_78dk_platform_mm_money_viewMerchantMoneyList(self):
        # 风险控制列表
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(
            pagecurrent=1, pagesize=10, name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['totalCount'], 1)
        Assertion.verity(json.loads(res)['data']['totalPage'], 1)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantName'], merchantname)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantUuid'], merchant_uuid)

    def test_028_api_78dk_platform_mm_money_merchantMoneyEnlarge(self):
        # 修改预授信放大系数
        res = PlatformAction.test_api_78dk_platform_mm_money_merchantMoneyEnlarge(
            uid=money_config_uuid, zoomcoefficient=2)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_mm_base_saveMerchant_not_name(self):
        # 新增商户基本信息失败，没有商户名称
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name='', parentmerchantuuid='', shortname=merchantname + '商户简称',
            channeluuid=channelid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'Name不能为空!')

    def test_030_api_78dk_platform_mm_base_saveMerchant_not_shortname(self):
        # 新增商户基本信息失败，没有商户简称
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name=merchantname, parentmerchantuuid='', shortname='',
            channeluuid=channelid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'ShortName不能为空!')

    def test_031_api_78dk_platform_mm_base_saveMerchant_not_channeluuid(self):
        # 新增商户基本信息失败，没有所属渠道
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name=merchantname, parentmerchantuuid='', shortname=merchantname + '商户简称', channeluuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'ChannelUuid不能为空!')

    def test_032_api_78dk_platform_mm_base_legal_saveLegalPerson_not_name(self):
        # 添加法人信息,缺少法人姓名
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile=mobile, name='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'Name不能为空!')

    def test_033_api_78dk_platform_mm_base_legal_saveLegalPerson_not_mobile(self):
        # 添加法人信息，缺少法人电话
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile='', name=name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_034_api_78dk_platform_mm_base_legal_saveLegalPerson_not_cardnumber(self):
        # 添加法人信息，缺少法人身份证
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber='', channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile=mobile, name=name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'CardNumber不能为空!')

    def test_035_api_78dk_platform_mm_base_legal_saveLegalPerson_error_mobile(self):
        # 添加法人信息，法人电话不是1开头或非11位数字
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile='234567890123',
            name=name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    # def test_036_api_78dk_platform_mm_base_legal_saveLegalPerson_error_cardnumber(self):
    #     # 添加法人信息，法人身份证格式错误
    #     res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
    #         cardnumber='格式错误2', channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile=mobile, name=name)
    #     Assertion.verity(json.loads(res)['code'], '20000')
    #     Assertion.verity(json.loads(res)['msg'], '法人身份证格式错误')

    def test_037_api_78dk_platform_mm_base_legal_saveLegalPerson(self):
        # 添加法人信息，法人身份证格式错误
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=merchant_uuid, legalpersonuuid='', mobile=mobile, name=name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_038_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant_not_uuid(self):
        # 根据商户Uuid查询法人信息
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_039_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(self):
        # 根据商户Uuid查询法人信息
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'legalPersonUuid')
        global merchantLegalPersonUuid
        merchantLegalPersonUuid = json.loads(res)['data']['legalPersonUuid']

    def test_040_api_78dk_platform_mm_base_legal_updateLegalPerson(self):
        # 修改商户法人信息
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_updateLegalPerson(
            channelormerchantuuid=merchant_uuid, mobile=mobile, legalpersonuuid=merchantLegalPersonUuid, name=name,
            cardnumber=cardnumber)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_041_api_78dk_platform_mm_base_clear_saveClearingAccount(self):
        # 为商户添加结算信息
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_saveClearingAccount(
            accountname=name, accountnumber='6011826564542944', accountopeningbank='农业银行',
            accounttype='public_accounts', branchname='支行名称', chamberlainidcard='431081199812097872',
            channelormerchantuuid=merchant_uuid, city='510100', clearingaccountuuid='', linenumber='6756765756',
            phone=mobile, province='510000', region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_042_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(self):
        # 查询商户结算信息
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_043_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(self):
        # 查询商户结算信息
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'clearingAccountUuid')
        global clearing_account_uuid
        clearing_account_uuid = json.loads(res)['data']['clearingAccountUuid']

    def test_044_api_78dk_platform_mm_base_clear_updateClearingAccount(self):
        # 修改商户结算信息
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_updateClearingAccount(
            accountname=name, accountnumber='6011826564542944', accountopeningbank='农业银行',
            accounttype='public_accounts', branchname='支行名称', chamberlainidcard='431081199812097872',
            channelormerchantuuid=merchant_uuid, city='510100', clearingaccountuuid=clearing_account_uuid,
            linenumber='6756765756', phone='15179366892', province='510000', region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_045_api_78dk_platform_mm_base_business_saveBusinessInfor(self):
        # 新增机构信息
        res = PlatformAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor(
            businessaddress='天府软件园', businessaddressgpsloction='', businessaddresszipcode='000000',
            businesshoursendtime='18:30', businesshoursstarttime='08:30', businessinformationuuid='',
            businessregistrationnumber='', channelormerchantuuid=merchant_uuid, documentaddress='天府软件园',
            email=email, organizationcode="567657675765", socialunifiedcreditcode="34534543534",
            storerentalendtime='2019-01-12', storerentalstarttime='2018-01-12', taxregistrationnumber='34543543543',
            documentprovince="510000", documentcity="510100", documentregion="510104", documentregionname='',
            businessprovince="510000", businesscity="510100", businessregion="510104", businessprovincename='',
            businesscityname='', businessregionname='', documentprovincename='', documentcityname=''
        )
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_046_api_i78dk_platform_mm_base_business_viewBusinessInfor(self):
        # 根据商户Uuid查询机构信息
        res = PlatformAction.test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'businessInformationUuid')
        global businessInformationUuid
        businessInformationUuid = json.loads(res)['data']['businessInformationUuid']

    def test_047_api_78dk_platform_mm_base_business_updateBusinessInfor(self):
        # 修改机构信息
        res = PlatformAction.test_api_78dk_platform_mm_base_business_updateBusinessInfor(
            businessaddress='天府软件园', businessaddressgpsloction='', businessaddresszipcode='000000',
            businesshoursendtime='18:30', businesshoursstarttime='08:30',
            businessinformationuuid=businessInformationUuid, businessregistrationnumber='',
            channelormerchantuuid=merchant_uuid, documentaddress='天府软件园', email=email,
            organizationcode="567657675765", socialunifiedcreditcode="34534543534", storerentalendtime='2019-01-12',
            storerentalstarttime='2018-01-12', taxregistrationnumber='34543543543',
            documentprovince="510000", documentcity="510100", documentregion="510104", documentregionname='',
            businessprovince="510000", businesscity="510100", businessregion="510104", businessprovincename='',
            businesscityname='', businessregionname='', documentprovincename='', documentcityname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_048_api_78dk_platform_mm_base_store_saveStore(self):
        # 为商户新增门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址', businessaddressgpsloction='', managername=store_name, managerphone=mobile,
            merchantuuid=merchant_uuid, storeuuid="", storename='', province=510000, city=510100,
            region=510104, provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_049_api_78dk_platform_mm_base_store_viewStore(self):
        # 查询门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_viewStore(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['storeUuid'], merchant_uuid)

    def test_050_api_78dk_platform_mm_base_store_viewStoreList(self):
        # 查询商户门店列表
        res = PlatformAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name=store_name, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)

    def test_051_api_78dk_platform_mm_base_store_updateStore(self):
        # 修改门店
        global store_uuid
        sql = 'manager_name="' + store_name + '" and state ="enabled"'
        store_uuid = xqkj_query.get_info('Tbl_Store', 'store_uuid', sql)[0]
        global_dict.set(store_uuid=xqkj_query.get_info('Tbl_Store', 'store_uuid', sql)[0])
        res = PlatformAction.test_api_78dk_platform_mm_base_store_updateStore(
            businessaddress='经营地址', businessaddressgpsloction='GPS地址', managername=store_name,
            managerphone='18911390729', merchantuuid=merchant_uuid, storeuuid=store_uuid, province=510000,
            city=510100, region=510104, provincename='', cityname='', regionname='', storename='storeNamebbbbbbbbb')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_052_api_78dk_platform_mm_saveContractImages(self):
        # 影像资料保存
        res = PlatformAction.test_api_78dk_platform_mm_saveContractImages(merchantuuid=merchant_uuid, key='', url='')
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '成功')

    # def test_053_api_78dk_platform_mm_base_store_uploadQrcode(self):
    #     # 下载门店二维
    #     res = PlatformAction.test_api_78dk_platform_mm_base_store_uploadQrcode(store_uuid)
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')

    def test_054_api_78dk_platform_mm_base_store_saveStore(self):
        # 已有门店的商户再新增门店
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址', businessaddressgpsloction='', managername=store_name, managerphone=mobile,
            merchantuuid=merchant_uuid, storeuuid="", storename='', province=510000, city=510100,
            region=510104, provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
