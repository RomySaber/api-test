#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from reborn.test import case_stream
from reborn.testAction import PlatformAction as JtlbasicAction, loginAction

fake = Factory().create('zh_CN')
name = fake.name_male()

channelname = fake.company() + '渠道'
channelname3 = channelname + '下级'
channelname1 = fake.company() + '渠道拒绝'
channelname2 = fake.company() + '删除机构测试'
email = fake.email()

# 法人名称
# 新增
# name=fake.name_male()
# 测试删除法定代表人
name2 = fake.name_male()

# 结算账户名称人
namecount = fake.name_male()
# 测试删除账户信息
namecount2 = fake.name_male()
# 删除结算账户测试
email2 = fake.email()

# 流程测试渠道
channelname_stream = channelname + '下级'
email_stream = fake.email()
name_stream = fake.name_male()
namecount_stream = fake.name_male()


class testJtlbasic_003_Channel(TestBaseCase):
    channelid = case_stream.saveChannel(channelname)

    # 渠道相关
    def test_01api_78dk_platform_cm_base_saveChannel(self):
        # 添加渠道  city, name, province, region, shortname, parentchanneluuid,
        res = JtlbasicAction.test_api_78dk_platform_cm_base_saveChannel(city="510100", name=channelname,
                                                                        province="510000", region="510107",
                                                                        shortname=channelname + '简称',
                                                                        parentchanneluuid='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_02api_78dk_platform_cm_base_updateChannel(self):
        # 编辑渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_base_updateChannel(channeluuid=self.channelid, city="510100",
                                                                          name=channelname, note='备注',
                                                                          province="510000", region="510107",
                                                                          shortname=channelname + '简称', operatoruuid='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_03api_78dk_platform_cm_base_viewChannel_all(self):
        # 查询渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_base_viewChannel(self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['name'], channelname)
        # Assertion.verity(len(json.loads(res)['data']),18)

    def test_04api_78dk_platform_cm_base_viewChannel_not_exist(self):
        # 查询不存在渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_base_viewChannel('111111111111111111111111111')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_05api_78dk_platform_cm_state_updateFreezeState_freeze(self):
        # 冻结渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_state_updateFreezeState(self.channelid, 'freeze')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_06api_78dk_platform_cm_state_updateFreezeState_normal(self):
        # 解冻渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_state_updateFreezeState(self.channelid, 'normal')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_07api_78dk_platform_cm_state_updateOpenCloseState_close(self):
        # 渠道开关状态为close
        res = JtlbasicAction.test_api_78dk_platform_cm_state_updateOpenCloseState(uid=self.channelid,
                                                                                  updatestate='close')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_08api_78dk_platform_cm_state_updateOpenCloseState_open(self):
        # 渠道开关状态为open
        res = JtlbasicAction.test_api_78dk_platform_cm_state_updateOpenCloseState(uid=self.channelid,
                                                                                  updatestate='open')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_09api_78dk_platform_cm_examine_examine_true(self):
        # 渠道审核通过
        res = JtlbasicAction.test_api_78dk_platform_cm_examine_examine(isadopt='true', message='通过', uid=self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_10api_78dk_platform_cm_examine_examine_false(self):
        # 渠道审核不过
        res = JtlbasicAction.test_api_78dk_platform_cm_base_saveChannel(city="510100", name=channelname1,
                                                                        province="510000", region="510107",
                                                                        shortname=channelname1 + '拒绝简称',
                                                                        parentchanneluuid=self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        res = JtlbasicAction.test_api_78dk_platform_cm_examine_examine(isadopt='false', message='不过',
                                                                       uid=self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_11api_78dk_platform_cm_examine_viewExamineChannels(self):
        # 渠道审核列表
        res = JtlbasicAction.test_api_78dk_platform_cm_examine_viewExamineChannels('123', 1, 8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_12api_78dk_platform_cm_examine_viewExamineChannels_all(self):
        # 渠道审核列表全部
        res = JtlbasicAction.test_api_78dk_platform_cm_examine_viewExamineChannels(name='', pagecurrent=1, pagesize=8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # self.assertNotEqual(json.loads(res)['data']['totalCount'],0,'数量至少大于等于1')

    def test_13api_78dk_platform_cm_base_viewChannels(self):
        # 渠道列表
        res = JtlbasicAction.test_api_78dk_platform_cm_base_viewChannels(pagecurrent=1, name=channelname, pagesize=8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # self.assertNotEqual(json.loads(res)['data']['totalCount'],0,'数量至少大于等于1')

    def test_14api_78dk_platform_cm_base_viewChannels_all(self):
        # 渠道列表全部
        res = JtlbasicAction.test_api_78dk_platform_cm_base_viewChannels(pagecurrent=1, name='', pagesize=10)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        self.assertNotEqual(json.loads(res)['data']['totalCount'], 0, '数量至少大于等于1')

    def test_15api_78dk_platform_cm_state_viewStateChannels(self):
        # 渠道状态列表
        res = JtlbasicAction.test_api_78dk_platform_cm_state_viewStateChannels(name=channelname, pagecurrent=1,
                                                                               pagesize=10,
                                                                               openclosestate='open',
                                                                               freezestate='normal',
                                                                               auditstate=0)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # self.assertNotEqual(json.loads(res)['data']['totalCount'],0,'数量至少大于等于1')

    def test_16api_78dk_platform_cm_state_viewStateChannels_all(self):
        # 渠道状态列表全部
        res = JtlbasicAction.test_api_78dk_platform_cm_state_viewStateChannels(name='', pagecurrent=1, pagesize=10,
                                                                               openclosestate='open',
                                                                               freezestate='normal',
                                                                               auditstate=0)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # self.assertNotEqual(json.loads(res)['data']['totalCount'],0,'数量至少大于等于1')

    # 操作员相关接口 需要先有渠道
    # -----------------------------------------------------------------------------------------------------
    # def test_18api_78dk_platform_cm_base_operator_saveOperator(self):
    #     # 添加操作员
    #     res = JtlbasicAction.test_api_78dk_platform_cm_base_operator_saveOperator(mail='yanhong@78dk.com',
    #                                                                               mobile='15100909879',
    #                                                                               name='dandan', password='123456',
    #                                                                               salt='喂自己袋盐',
    #                                                                               title='喂了自己一袋儿盐的操作员',
    #                                                                               channelormerchantuuid=self.channelid)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #
    # def test_20api_78dk_platform_cm_base_operator_viewOperator_not_exist(self):
    #     # 查询不存在的操作员
    #     res = JtlbasicAction.test_api_78dk_platform_cm_base_operator_viewOperator('11')
    #     Assertion.verity(json.loads(res)['code'], '10000')

    # def test_21api_78dk_platform_cm_base_operator_updateOperator(self):
    #     # 编辑操作员
    #     operatorid1 = MysqlClent.select_one(loginAction.DB, 'Tbl_Operator', 'operator_uuid', 'name="dandan"')
    #     channelid1 = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid',
    #                                        'name="渠道名" and state ="enabled"')
    #     res = JtlbasicAction.test_api_78dk_platform_cm_base_operator_updateOperator(channelormerchantuuid=channelid1,
    #                                                                                 mail='dd@78dk.com',
    #                                                                                 mobile='13100000000', name='',
    #                                                                                 operatoruuid=operatorid1,
    #                                                                                 password='1', salt='继续喂盐',
    #                                                                                 title='继续喂了自己一袋儿盐的操作员')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #
    # def test_22api_78dk_platform_cm_base_operator_deleteOperator(self):
    #     # 删除操作员
    #     operatorid = MysqlClent.select_one(loginAction.DB, 'Tbl_Operator', 'operator_uuid',
    #                                        'name="dandan" and state = "enabled"')
    #     res = JtlbasicAction.test_api_78dk_platform_cm_base_operator_deleteOperator(operatorid)
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     operator = 'operator_uuid = ' + '"{}"'.format(operatorid)
    #     operatorid1 = MysqlClent.select_one(loginAction.DB, 'Tbl_Operator', 'operator_uuid', '{}'.format(operator))
    #     res1 = JtlbasicAction.test_api_78dk_platform_cm_base_operator_viewOperator(
    #         operatorid1)  # 调用查询查询接口，判断state是否真的修改为disabled
    #     Assertion.verity(json.loads(res1)['data']['state'], 'disabled')

    # 省市区下拉
    # -------------------------------------------------------------------------------------------------------------
    def test_23api_78dk_platform_common_viewProvinceLists(self):
        # 省级下拉
        res = JtlbasicAction.test_api_78dk_platform_common_viewProvinceLists('')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data'][0]['code'], '110000', '北京市code')
        Assertion.verity(json.loads(res)['data'][1]['code'], '120000', '天津市code')
        Assertion.verity(json.loads(res)['data'][2]['code'], '130000', '河北省')

    def test_24api_78dk_platform_common_viewCityLists(self):
        # 市级下拉
        res = JtlbasicAction.test_api_78dk_platform_common_viewCityLists(51000)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_25api_78dk_platform_common_viewRegionLists(self):
        # 区/县级下拉
        res = JtlbasicAction.test_api_78dk_platform_common_viewRegionLists(51010)
        Assertion.verity(json.loads(res)['code'], '10000')

    # 法人相关接口 需要先有渠道
    # ------------------------------------------------------------------------------------------------------------
    def test_26api_78dk_platform_cm_base_legal_saveLegalPerson(self):
        # 添加法人代表
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        res1 = JtlbasicAction.test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber='510903199909098900',
                                                                                   channelormerchantuuid=channelid,
                                                                                   legalpersonuuid='',
                                                                                   mobile='18909890989', name=name)
        Assertion.verity(json.loads(res1)['code'], '10000')

    def test_27api_78dk_platform_cm_base_legal_viewLegalPerson(self):
        # 查询法人代表根据渠道uuid
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(channelid)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(channelid)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_28api_78dk_platform_cm_base_legal_updateLegalPerson(self):
        # 编辑法人代表
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(channelid)
        sql = 'name="' + name + '" and state ="enabled"'
        legalPersonUuid = MysqlClent.select_one(loginAction.DB, 'Tbl_LegalPerson', 'legal_person_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_legal_updateLegalPerson(cardnumber='510903199909098900',
                                                                                    channelormerchantuuid=channelid,
                                                                                    legalpersonuuid=legalPersonUuid,
                                                                                    mobile='18909890989', name=name)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_29api_78dk_platform_cm_base_legal_deleteLegalPerson(self):
        # 删除法人代表 name2  channelname2
        # 添加渠道
        res = JtlbasicAction.test_api_78dk_platform_cm_base_saveChannel(city="510100", name=channelname2,
                                                                        province="510000", region="510107",
                                                                        shortname=channelname2 + '拒绝简称',
                                                                        parentchanneluuid=self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # 添加法人代表
        sql = 'name="' + channelname2 + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        JtlbasicAction.test_api_78dk_platform_cm_base_legal_saveLegalPerson(cardnumber='510903199909098900',
                                                                            channelormerchantuuid=channelid,
                                                                            legalpersonuuid='',
                                                                            mobile='18909890989', name=name2)
        # 删除法人代表
        sql = 'name="' + name2 + '" and state ="enabled"'
        legalpersonid = MysqlClent.select_one(loginAction.DB, 'Tbl_LegalPerson', 'legal_person_uuid', sql)
        res4 = JtlbasicAction.test_api_78dk_platform_cm_base_legal_deleteLegalPerson(legalpersonid)
        Assertion.verity(json.loads(res4)['code'], '10000')

    # 结算相关接口 需要先有渠道
    # -------------------------------------------------------------------------------------
    def test_30api_78dk_platform_cm_base_clear_saveClearingAccount(self):
        # 新增结算信息
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_clear_saveClearingAccount(accountname=namecount,
                                                                                      accountnumber='6011826564542944',
                                                                                      accountopeningbank='农业银行',
                                                                                      accounttype='public_accounts',
                                                                                      branchname='支行名称',
                                                                                      chamberlainidcard='431081199812097872',
                                                                                      channelormerchantuuid=channelid,
                                                                                      city='510100',
                                                                                      clearingaccountuuid='',
                                                                                      linenumber='6756765756',
                                                                                      phone='15179366892',
                                                                                      province='510000',
                                                                                      region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_31api_78dk_platform_cm_base_clear_updateClearingAccount(self):
        # 编辑结算信息
        sql = 'account_name="' + namecount + '" and state ="enabled"'
        clearing_account_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ClearingAccount', 'clearing_account_uuid',
                                                      sql)
        print(clearing_account_uuid)
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(channelid)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_clear_updateClearingAccount(accountname=namecount,
                                                                                        accountnumber='6011826564542944',
                                                                                        accountopeningbank='农业银行',
                                                                                        accounttype='public_accounts',
                                                                                        branchname='支行名称',
                                                                                        chamberlainidcard='431081199812097872',
                                                                                        channelormerchantuuid=channelid,
                                                                                        city='510100',
                                                                                        clearingaccountuuid=clearing_account_uuid,
                                                                                        linenumber='6756765756',
                                                                                        phone='15179366892',
                                                                                        province='510000',
                                                                                        region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_34api_78dk_platform_cm_base_clear_deleteClearingAccount_not_exist(self):
        # 删除结算信息---不存在
        res = JtlbasicAction.test_api_78dk_platform_cm_base_clear_deleteClearingAccount('123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '请求参数不正确!')

    def test_35api_78dk_platform_cm_base_clear_deleteClearingAccount(self):
        # 删除结算信息
        # 新建结算信息
        sql = 'name="' + channelname2 + '" and state ="enabled"'
        channelid1 = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        JtlbasicAction.test_api_78dk_platform_cm_base_clear_saveClearingAccount(accountname=namecount2,
                                                                                accountnumber='6011826564542944',
                                                                                accountopeningbank='农业银行',
                                                                                accounttype='public_accounts',
                                                                                branchname='支行名称',
                                                                                chamberlainidcard='431081199812097872',
                                                                                channelormerchantuuid=channelid1,
                                                                                city='510100', clearingaccountuuid='',
                                                                                linenumber='6756765756',
                                                                                phone='15179366892',
                                                                                province='510000', region='510101')
        sql = 'account_name="' + namecount2 + '" and state ="enabled"'
        clearing_account_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ClearingAccount', 'clearing_account_uuid',
                                                      sql)
        #  删除结算信息
        res = JtlbasicAction.test_api_78dk_platform_cm_base_clear_deleteClearingAccount(clearing_account_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')

    # 机构相关接口 需要先有渠道
    # ---------------------------------------------------------------------------------------------------------------
    def test_36api_78dk_platform_cm_base_business_saveBusinessInfor(self):
        # 新增机构
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(channelid)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress='天府软件园',
                                                                                       businessaddressgpsloction='天府软件园GPS地址',
                                                                                       businessaddresszipcode='000000',
                                                                                       businesshoursendtime='18:30',
                                                                                       businesshoursstarttime='08:30',
                                                                                       businessinformationuuid='',
                                                                                       businessregistrationnumber='443534534543',
                                                                                       channelormerchantuuid=channelid,
                                                                                       documentaddress='天府软件园',
                                                                                       email=email,
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
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_37api_78dk_platform_cm_base_business_updateBusinessInfor(self):
        # 编辑业务机构
        sql = 'email="' + email + '" and state ="enabled"'
        businnessid = MysqlClent.select_one(loginAction.DB, 'Tbl_BusinessInformation',
                                            'business_information_uuid', sql)
        sql = 'name="' + channelname + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(businnessid, 11, channelid)
        res = JtlbasicAction.test_api_78dk_platform_cm_base_business_updateBusinessInfor(businessaddress='天府软件园',
                                                                                       businessaddressgpsloction='天府软件园GPS地址',
                                                                                       businessaddresszipcode='000000',
                                                                                       businesshoursendtime='18:30',
                                                                                       businesshoursstarttime='08:30',
                                                                                       businessinformationuuid=businnessid,
                                                                                       businessregistrationnumber='443534534543',
                                                                                       channelormerchantuuid=channelid,
                                                                                       documentaddress='天府软件园',
                                                                                       email=email,
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
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_39api_78dk_platform_cm_base_business_deleteBusinessInfor_not_exist(self):
        # 删除不存在的机构
        res = JtlbasicAction.test_api_78dk_platform_cm_base_business_deleteBusinessInfor('123')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_40api_78dk_platform_cm_base_business_deleteBusinessInfor(self):
        res = JtlbasicAction.test_api_78dk_platform_cm_base_saveChannel(city="510100", name=channelname2,
                                                                        province="510000", region="510107",
                                                                        shortname=channelname2 + '拒绝简称',
                                                                        parentchanneluuid=self.channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

        # 查询渠道id
        sql = 'name="' + channelname2 + '" and state ="enabled"'
        channelid = MysqlClent.select_one(loginAction.DB, 'Tbl_ChannelProfile', 'channel_uuid', sql)
        print(channelid)
        # 新增机构信息
        JtlbasicAction.test_api_78dk_platform_cm_base_business_saveBusinessInfor(businessaddress='天府软件园',
                                                                                       businessaddressgpsloction='天府软件园GPS地址',
                                                                                       businessaddresszipcode='000000',
                                                                                       businesshoursendtime='18:30',
                                                                                       businesshoursstarttime='08:30',
                                                                                       businessinformationuuid='',
                                                                                       businessregistrationnumber='443534534543',
                                                                                       channelormerchantuuid=channelid,
                                                                                       documentaddress='天府软件园',
                                                                                       email=email,
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

        sql = 'email="' + email + '" and state ="enabled"'
        businnessid = MysqlClent.select_one(loginAction.DB, 'Tbl_BusinessInformation', 'business_information_uuid', sql)
        # 删除结算
        res = JtlbasicAction.test_api_78dk_platform_cm_base_business_deleteBusinessInfor(businnessid)
        Assertion.verity(json.loads(res)['code'], '10000')
