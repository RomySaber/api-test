#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from faker import Factory

from common.myCommon import Assertion
from common.mydb import MysqlClent
from reborn.testAction import PlatformAction as JtlbasicAction, loginAction

fake = Factory().create('zh_CN')

# 渠道
channelname_stream = fake.company() + '渠道' + '下级stream'
email_stream = fake.email()
name_stream = fake.name_male()
namecount_stream = fake.name_male()
# 商户
# 与产品绑定的商户
merchantname_stream = fake.company() + '流程stream'
# email_stream=fake.email()
# name_stream=fake.name_male()
account_name_stream = fake.name_male()
st_name_stream = fake.name_male()

# 产品使用资金包
pFundSidename = fake.name_male() + '资方名stream'
pFundPackagename = fake.name_male() + '资金包名stream'


# 新增资金包
def saveFundPackage(fundSide_name, fundPackage_name):
    # 产品使用资金包
    res = JtlbasicAction.test_api_78dk_platform_fund_fundSide_saveFundSide(fundSide_name, 'enabled')
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    sql = 'name="' + fundSide_name + '" and state ="enabled"'
    fundside_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundSide', 'fund_side_uuid', sql)  # 资方uuid
    res = JtlbasicAction.test_api_78dk_platform_fund_fundPackage_saveFundPackage(amount=300000, name=fundPackage_name,
                                                                                 state='enabled',
                                                                                 fundsideuuid=fundside_uuid)
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    return fundPackage_name


def channel(channelname, accountname, LegalPerson_name, business_email):
    channelid = saveChannel(channelname)
    # 审核通过
    # sql = 'name="' + channelname + '" and state ="enabled"'
    # channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
    JtlbasicAction.test_api_78dk_platform_cm_examine_examine('true', channelid, '通过')
    # 添加结算信息
    JtlbasicAction.test_api_78dk_platform_cm_base_clear_saveClearingAccount(accountname=accountname,
                                                                            accountnumber='6011826564542944',
                                                                            accountopeningbank='农业银行',
                                                                            accounttype='public_accounts',
                                                                            branchname='支行名称',
                                                                            chamberlainidcard='431081199812097872',
                                                                            channelormerchantuuid=channelid,
                                                                            city='510100', clearingaccountuuid='',
                                                                            linenumber='6756765756',
                                                                            phone='15179366892',
                                                                            province='510000', region='510101')
    # 添加法人
    JtlbasicAction.test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber='510903199909098900',
                                                                        channelormerchantuuid=channelid,
                                                                        legalpersonuuid='',
                                                                        mobile='18909890989', name=LegalPerson_name)
    # 添加机构信息
    JtlbasicAction.test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress='天府软件园',
                                                                             businessaddressgpsloction='天府软件园GPS地址',
                                                                             businessaddresszipcode='000000',
                                                                             businesshoursendtime='18:30',
                                                                             businesshoursstarttime='08:30',
                                                                             businessinformationuuid=channelid,
                                                                             businessregistrationnumber='443534534543',
                                                                             channelormerchantuuid=channelid,
                                                                             documentaddress='天府软件园',
                                                                             email=business_email,
                                                                             organizationcode='567657675765',
                                                                             socialunifiedcreditcode='34534543534',
                                                                             storerentalendtime='2019-01-12',
                                                                             storerentalstarttime='2018-01-12',
                                                                             taxregistrationnumber='34543543543',
                                                                             documentprovince=510000,
                                                                             documentcity=510100,
                                                                             documentregion=510104,
                                                                             documentprovincename='',
                                                                             documentcityname='',
                                                                             documentregionname='',
                                                                             businessprovince=510000,
                                                                             businesscity=510100,
                                                                             businessregion=510104,
                                                                             businessprovincename='',
                                                                             businesscityname='',
                                                                             businessregionname='')

    return channelname


def saveMerchant(channel_name, account_name, LegalPerson_name, business_email, merchant_name, manager_name):
    #         与产品绑定的商户
    #         新增商户
    sql = 'name="' + channel_name + '" and state ="enabled"'
    channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
    JtlbasicAction.test_api_78dk_platform_mm_base_saveMerchant(note='备注', name=merchant_name, parentmerchantuuid='',
                                                               shortname=merchant_name, channeluuid=channelid)
    # 审核通过
    sql1 = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
    JtlbasicAction.test_api_78dk_platform_mm_examine_merchanrExamine(uid=merchant_uuid, ispass='pass', message='通过')
    # 新增机构
    sql1 = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql1)
    res = JtlbasicAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor(businessaddress='天府软件园',
                                                                                   businessaddressgpsloction='天府软件园GPS地址',
                                                                                   businessaddresszipcode='000000',
                                                                                   businesshoursendtime='18:30',
                                                                                   businesshoursstarttime='08:30',
                                                                                   businessinformationuuid=merchant_uuid,
                                                                                   businessregistrationnumber='443534534543',
                                                                                   channelormerchantuuid=merchant_uuid,
                                                                                   documentaddress='天府软件园',
                                                                                   email=business_email,
                                                                                   organizationcode='567657675765',
                                                                                   socialunifiedcreditcode='34534543534',
                                                                                   storerentalendtime='2019-01-12',
                                                                                   storerentalstarttime='2018-01-12',
                                                                                   taxregistrationnumber='34543543543',
                                                                                   documentprovince=510000,
                                                                                   documentcity=510100,
                                                                                   documentregion=510104,
                                                                                   documentprovincename='',
                                                                                   documentcityname='',
                                                                                   documentregionname='',
                                                                                   businessprovince=510000,
                                                                                   businesscity=510100,
                                                                                   businessregion=510104,
                                                                                   businessprovincename='',
                                                                                   businesscityname='',
                                                                                   businessregionname='')

    # 添加法人
    sql = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
    res = JtlbasicAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber='123456',
                                                                              channelormerchantuuid=merchant_uuid,
                                                                              legalpersonuuid='',
                                                                              mobile='18911390729',
                                                                              name=LegalPerson_name)
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    print(res)

    # 为商户添加结算信息
    sql = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
    res = JtlbasicAction.test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname=account_name,
                                                                                  accountnumber='6011826564542944',
                                                                                  accountopeningbank='农业银行',
                                                                                  accounttype='public_accounts',
                                                                                  branchname='支行名称',
                                                                                  chamberlainidcard='431081199812097872',
                                                                                  channelormerchantuuid=merchant_uuid,
                                                                                  city='510100', clearingaccountuuid='',
                                                                                  linenumber='6756765756',
                                                                                  phone='15179366892',
                                                                                  province='510000', region='510101')
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    # 为商户新增门店
    sql = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
    res = JtlbasicAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                        businessaddressgpsloction='GPS地址',
                                                                        managername=manager_name,
                                                                        managerphone='18911390729',
                                                                        merchantuuid=merchant_uuid,
                                                                        stormuuid="storeName5555555555", storename='',
                                                                        province=510000, city=510100, region=510104,
                                                                        provincename='', cityname='', regionname='')
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    # 新增额度管理
    sql = 'name="' + merchant_name + '" and state ="enabled"'
    merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
    res = JtlbasicAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                           amountsingle=30000, amountsum=5000000,
                                                                           merchantuuid=merchant_uuid,
                                                                           moneyconfiguuid='', zoomcoefficient=0)
    Assertion.verity(json.loads(res)['code'], '10000')
    Assertion.verity(json.loads(res)['msg'], '成功')
    return merchant_name


def saveChannel(channelname):
    # 添加渠道  city, name, province, region, shortname, parentchanneluuid,
    res = JtlbasicAction.test_api_78dk_platform_cm_base_saveChannel(city="510100", province="510000", name=channelname,
                                                                    shortname=channelname + '简称',
                                                                    parentchanneluuid='', region="510107")
    Assertion.verity(json.loads(res)['msg'], '成功')
    Assertion.verity(json.loads(res)['code'], '10000')
    channelid = json.loads(res)['data']['channelUuid']
    return channelid


# 用户创建订单
if __name__ == '__main__':
    print(saveChannel(channelname_stream))
