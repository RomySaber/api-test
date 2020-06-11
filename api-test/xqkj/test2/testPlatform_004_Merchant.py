#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from xqkj.test import case_stream
from xqkj.testAction import PlatformAction
from xqkj.testAction import loginAction

fake = Factory().create('zh_CN')
# 商户名称
merchantname = fake.company() + '门店' + loginAction.sign
# 拒绝商户名称
merchantnamefail = fake.company() + '拒绝' + loginAction.sign
# s删除机构 法人 结算的商户
merchantnamedele = fake.company() + '删除测试' + loginAction.sign

# 新增机构 email
email = fake.email()
# 删除机构email
emaildele = fake.email()

# 新增法人信息
name = fake.name_male() + loginAction.sign
# 删除法人信息
namedele = fake.name_male() + loginAction.sign

# 计算账户信息
account_name = fake.name_male() + loginAction.sign
# 删除结算账户信息
account_namedele = fake.name_male() + loginAction.sign

# 门店信息
st_name = fake.name_male() + loginAction.sign
# 删除门店信息
st_namedele = fake.name_male() + loginAction.sign

# 与产品绑定的商户
merchantname_stream = fake.company() + '流程' +loginAction.sign
email_stream = fake.email()
name_stream = fake.name_male()
account_name_stream = fake.name_male()
st_name_stream = fake.name_male()

channelname_stream = fake.company() + '渠道下级' + loginAction.sign
namecount_stream = fake.name_male() + loginAction.sign
# 渠道类
# 渠道名称
channelname3 = channelname_stream
merchant_dele_channelname = merchantnamedele


# 商户相关接口 需要先有渠道
class testPlatform_004_Merchant(TestBaseCase):
    def test_001_savechannel(self):
        case_stream.channel(channelname_stream, account_name_stream, namecount_stream, email_stream)

    def test_002_saveMerchant(self):
        case_stream.saveMerchant(channelname_stream, account_namedele, namedele,
                                 emaildele, merchantnamedele, st_namedele)

    def test_01api_78dk_platform_mm_base_saveMerchant(self):
        # 新增商户基本信息
        sql = 'name="' + channelname_stream + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_saveMerchant('备注', merchantname, '',
                                                                         merchantname + '商户简称', channelid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_mm_base_updateMerchant(self):
        time.sleep(1)
        # 修改商户基本信息
        sql = 'name="' + channelname3 + '" and state ="enabled"'
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_base_updateMerchant(merchantuuid=merchant_uuid, note='',
                                                                           parentmerchantuuid='',
                                                                           name=merchantname,
                                                                           channeluuid=channelid,
                                                                           shortname=merchantname + '商户简称')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_03api_78dk_platform_mm_base_viewMerchantList(self):
        # 查询商户列表
        res = PlatformAction.test_api_78dk_platform_mm_base_viewMerchantList(0, 10, merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_04api_78dk_platform_mm_examine_merchanrExamine_pass(self):
        # 商户审核pass
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine('pass', '通过', merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_05api_78dk_platform_mm_examine_merchanrExamine_fail(self):
        # 商户审核fail
        sql = 'name="' + channelname3 + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        Parentmerchantlid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        # 添加子级商户
        PlatformAction.test_api_78dk_platform_mm_base_saveMerchant('备注', merchantname, Parentmerchantlid,
                                                                   merchantname + '商户简称', channelid)
        sql1 = 'name="' + merchantnamefail + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine('fail', '不通过', merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_mm_base_viewMerchant(self):
        # 查询商户基本信息
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_base_viewMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['name'], merchantname)

    def test_07api_78dk_platform_mm_examine_viewExamineMerchantList(self):
        # 查询商户审核列表
        res = PlatformAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList('', 0, 10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_08api_78dk_platform_mm_state_viewStateMerchantList(self):
        # 查询商户状态列表
        res = PlatformAction.test_api_78dk_platform_mm_state_viewStateMerchantList('', 0, 10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_09api_78dk_platform_mm_state_updateOpenCloseState_close(self):
        # 修改商户开关为close
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_state_updateOpenCloseState(merchant_uuid, 'close')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_10api_78dk_platform_mm_state_updateOpenCloseState_open(self):
        # 修改商户开关为open
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_state_updateOpenCloseState(merchant_uuid, 'open')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_11api_78dk_platform_mm_state_updateFreezeState_freeze(self):
        # 修改商户冻结状态为freeze
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_state_updateFreezeState(merchant_uuid, 'freeze')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_12api_78dk_platform_mm_state_updateFreezeState_normal(self):
        # 修改商户冻结状态为normal
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_state_updateFreezeState(merchant_uuid, 'normal')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 商户机构相关接口
    # 需要先有商户
    # ----------------------------------------------------------------------------------------------
    # def test_13api_i78dk_platform_mm_base_business_saveBusinessInfor(self):
    #     # 新增机构
    #     sql1 = 'name="' + merchantname + '" and state ="enabled"'
    #     merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
    #     res = PlatformAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor(
    #         businessaddress='天府软件园', businessaddressgpsloction='天府软件园GPS地址', businessaddresszipcode='000000',
    #         businesshoursendtime='18:30', businesshoursstarttime='08:30', businessinformationuuid=merchant_uuid,
    #         businessregistrationnumber='443534534543', channelormerchantuuid=merchant_uuid, documentaddress='天府软件园',
    #         email=email_stream, organizationcode='567657675765', socialunifiedcreditcode='34534543534',
    #         storerentalendtime='2019-01-12', storerentalstarttime='2018-01-12', taxregistrationnumber='34543543543',
    #         documentprovince=510000, documentcity=510100, documentregion=510104, documentprovincename='',
    #         documentcityname='', documentregionname='', businessprovince=510000, businesscity=510100,
    #         businessregion=510104, businessprovincename='', businesscityname='', businessregionname='')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')

    def test_15api_i78dk_platform_mm_base_business_viewBusinessInfor(self):
        # 根据商户Uuid查询机构信息
        sql1 = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        res = PlatformAction.test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_16api_i78dk_platform_mm_base_business_deleteBusinessInfor(self):
        # 删除机构  emaildele
        # 新增商户
        sql = 'name="' + channelname3 + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        sql = 'name="' + merchantname + '" and state ="enabled"'
        Parentmerchantlid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        # 添加子级商户
        PlatformAction.test_api_78dk_platform_mm_base_saveMerchant('备注', merchantname, Parentmerchantlid,
                                                                   merchantname + '商户简称', channelid)
        # 新增机构
        sql1 = 'name="' + merchantnamedele + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
        print(merchant_uuid)
        PlatformAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor('天府软件园', '天府软件园GPS地址',
                                                                                 '000000', '18:30', '08:30', '',
                                                                                 '443534534543', merchant_uuid,
                                                                                 '天府软件园', email, '567657675765',
                                                                                 '34534543534', '2019-01-12',
                                                                                 '2018-01-12', '34543543543',
                                                                                 510000, 510100, 510104, 510000,
                                                                                 510100, 510104, '', '', '', '',
                                                                                 '', '')

    # 为商户添加法人信息
    # 需要先有商户
    # -----------------------------------------------------------------------------
    def test_17api_78dk_platform_mm_base_legal_saveLegalPerson(self):
        # 添加法人信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson('123456', merchant_uuid, '',
                                                                                  '18911390729', name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_18api_78dk_platform_mm_base_legal_updateLegalPerson(self):
        # 修改商户法人信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        sql = 'name="' + name + '" and state ="enabled"'
        legalperson_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_LegalPerson', 'legal_person_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_updateLegalPerson(merchant_uuid, '18911390729',
                                                                                    legalperson_uuid, name, '123456')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_19api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(self):
        # 根据商户Uuid查询法人信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_20api_78dk_platform_mm_base_legal_deleteLegalPerson(self):
        # 删除商户法人信息
        sql = 'name="' + namedele + '" and state ="enabled"'
        legalperson_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_LegalPerson', 'legal_person_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_legal_deleteLegalPerson(legalperson_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 商户结算相关接口需要先有商户
    # --------------------------------------------------------------------------------
    def test_21api_78dk_platform_mm_base_clear_saveClearingAccount(self):
        # 为商户添加结算信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname=account_name,
                                                                                      accountnumber='6011826564542944',
                                                                                      accountopeningbank='农业银行',
                                                                                      accounttype='public_accounts',
                                                                                      branchname='支行名称',
                                                                                      chamberlainidcard='431081199812097872',
                                                                                      channelormerchantuuid=merchant_uuid,
                                                                                      city='510100',
                                                                                      clearingaccountuuid='',
                                                                                      linenumber='6756765756',
                                                                                      phone='15179366892',
                                                                                      province='510000',
                                                                                      region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_22api_78dk_platform_mm_base_clear_updateClearingAccount(self):
        # 修改商户结算信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        sql = 'account_name="' + account_name + '" and state ="enabled"'
        clearing_account_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ClearingAccount', 'clearing_account_uuid',
                                                      sql)
        print(merchant_uuid, clearing_account_uuid)
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_updateClearingAccount(accountname=account_name,
                                                                                        accountnumber='6011826564542944',
                                                                                        accountopeningbank='农业银行',
                                                                                        accounttype='public_accounts',
                                                                                        branchname='支行名称',
                                                                                        chamberlainidcard='431081199812097872',
                                                                                        channelormerchantuuid=merchant_uuid,
                                                                                        city='510100',
                                                                                        clearingaccountuuid=clearing_account_uuid,
                                                                                        linenumber='6756765756',
                                                                                        phone='15179366892',
                                                                                        province='510000',
                                                                                        region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_23api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(self):
        # 查询商户结算信息
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_24api_78dk_platform_mm_base_clear_deleteClearingAccount(self):
        # 删除商户结算信息
        # 添加商户结算信息
        sql = 'account_name="' + account_namedele + '" and state ="enabled"'
        clearing_account_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ClearingAccount', 'clearing_account_uuid',
                                                      sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_clear_deleteClearingAccount(clearing_account_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 商户门店管理 需要先有商户
    # -----------------------------------------------------------------------------------------------------------
    def test_25api_78dk_platform_mm_base_store_saveStore(self):
        # 为商户新增门店
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                            businessaddressgpsloction='GPS地址',
                                                                            managername=st_name,
                                                                            managerphone='18911390729',
                                                                            merchantuuid=merchant_uuid,
                                                                            storeuuid="storeName5555555555",
                                                                            storename='',
                                                                            province=510000, city=510100, region=510104,
                                                                            provincename='', cityname='', regionname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_26api_78dk_platform_mm_base_store_updateStore(self):
        # 修改门店
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        sql = 'manager_name="' + st_name + '" and state ="enabled"'
        store_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_Store', 'store_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_store_updateStore(
            businessaddress='经营地址', businessaddressgpsloction='GPS地址', managername=st_name,
            managerphone='18911390729', merchantuuid=merchant_uuid, storeuuid=store_uuid, province=510000,
            city=510100, region=510104, provincename='', cityname='', regionname='', storename='storeNamebbbbbbbbb')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_27api_78dk_platform_mm_base_store_viewStore(self):
        # 查询门店
        sql = 'manager_name="' + st_name + '" and state ="enabled"'
        store_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_Store', 'store_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_store_viewStore(store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['storeUuid'], store_uuid)

    def test_28api_78dk_platform_mm_base_store_viewStoreList(self):
        # 查询商户门店列表
        res = PlatformAction.test_api_78dk_platform_mm_base_store_viewStoreList('', 1, 10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_29api_78dk_platform_mm_base_store_deleteStore(self):
        # 删除门店
        sql = 'manager_name="' + st_namedele + '" and state ="enabled"'
        store_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_Store', 'store_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_base_store_deleteStore(store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 额度管理相关接口
    # ------------------------------------------------------------------------
    def test_30api_78dk_platform_mm_money_saveMerchantMoney(self):
        # 新增额度管理
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                               amountsingle=30000, amountsum=5000000,
                                                                               merchantuuid=merchant_uuid,
                                                                               moneyconfiguuid='', zoomcoefficient=0)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_31api_78dk_platform_mm_money_updateMerchantMoney(self):
        # 修改额度管理
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        condition = 'merchant_uuid="{}" and state ="enabled"'.format(merchant_uuid)
        money_config_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantMoneyConfig',
                                                  'money_config_uuid', condition)  # 额度uuid
        res = PlatformAction.test_api_78dk_platform_mm_money_updateMerchantMoney(amountday=10000, amountmonth=300000,
                                                                                 amountsingle=10000, amountsum=500000,
                                                                                 merchantuuid=merchant_uuid,
                                                                                 moneyconfiguuid=money_config_uuid,
                                                                                 zoomcoefficient=1.5)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_32api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self):
        # 根据商户Uuid查询额度管理
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_33api_78dk_platform_mm_money_deleteMerchantMoney(self):
        # 删除商户额度管理
        sql = 'name="' + merchantnamedele + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        condition = 'merchant_uuid="{}" and state ="enabled"'.format(merchant_uuid)
        # # 商户绑定额度
        # 删除额度
        money_config_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantMoneyConfig',
                                                  'money_config_uuid', condition)
        res = PlatformAction.test_api_78dk_platform_mm_money_deleteMerchantMoney(money_config_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_34api_78dk_platform_mm_money_viewMerchantMoneyList(self):
        # 风险控制列表
        res = PlatformAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(1, 999, '商户名')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_35api_78dk_platform_mm_money_merchantMoneyEnlarge(self):
        # 修改预授信放大系数
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        condition = 'merchant_uuid="{}" and state ="enabled"'.format(merchant_uuid)
        money_config_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantMoneyConfig',
                                                  'money_config_uuid', condition)
        res = PlatformAction.test_api_78dk_platform_mm_money_merchantMoneyEnlarge(money_config_uuid, 1.5)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 影像资料保存接口
    # -----------------------------------------------------------------------------------------------------------------
    def test_36api_78dk_platform_mm_saveContractImages(self):
        # 影像资料保存
        # {'merchantUuid': '商户Uuid(Y)', 'url': '图片相对URL(Y)', 'key': '图片配置key(Y)'}
        sql = 'name="' + merchantname + '" and state ="enabled"'
        merchantuuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        PlatformAction.test_api_78dk_platform_mm_saveContractImages(merchantuuid, '', '')

        # def test_36api_78dk_platform_mm_saveContractImages(self):
        #     # 影像资料保存
        #     # {'merchantUuid': '商户Uuid(Y)', 'url': '图片相对URL(Y)', 'key': '图片配置key(Y)'}
        #     sql = 'name="' + merchantname + '" and state ="enabled"'
        #     merchantuuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        #     PlatformAction.test_api_78dk_platform_mm_saveContractImages(merchantuuid, '', '')
