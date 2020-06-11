#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-09 下午 2:27
@Author     : 罗林
@File       : test_001_web_Channel.py
@desc       : 渠道管理流程自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from mjjry.query import xqkj_query
from mjjry.testAction import WebAction
from mjjry.testAction import loginAction

fake = Faker("zh_CN")

channelname = fake.company() + '渠道' + loginAction.sign
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = '15388188697'
cardnumber = fake.ssn()
# 子渠道
channelname_stream = channelname + '下级' + loginAction.sign


class test_001_web_Channel(TestBaseCase):
    def test_01_api_78dk_platform_cm_base_saveChannel(self):
        """
        添加渠道成功
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname, province="510000", region="510107", shortname=channelname + '简称',
            parentchanneluuid=''))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'freezeStateName')
        Assertion.verityContain(res['data'], 'openCloseStateName')
        global channelid
        channelid = res['data']['channelUuid']
        loginAction.global_dict.set(channelid=res['data']['channelUuid'])

    def test_02_api_78dk_platform_cm_base_legal_saveLegalPerson(self):
        """
        添加法人代表
        :return:
        """
        res1 = WebAction.test_api_78dk_platform_cm_base_legal_saveLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=channelid, legalpersonuuid='',
            mobile=mobile, name=name, city='110100', province='110000', region='110101')
        Assertion.verity(json.loads(res1)['code'], '10000')
        Assertion.verity(json.loads(res1)['msg'], '成功')

    def test_03_api_78dk_platform_cm_base_legal_viewLegalPerson(self):
        """
        查询法人代表根据渠道uuid
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'channelOrMerchantUuid')
        Assertion.verityContain(res['data'], 'legalPersonUuid')
        global legal_person_uuid
        legal_person_uuid = res['data']['legalPersonUuid']
        global channelOrMerchantUuid
        channelOrMerchantUuid = res['data']['channelOrMerchantUuid']

    def test_04_api_78dk_platform_cm_base_legal_updateLegalPerson(self):
        """
        编辑法人代表
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_legal_updateLegalPerson(
            cardnumber=cardnumber, channelormerchantuuid=channelid, legalpersonuuid=legal_person_uuid,
            mobile=mobile, name=name, city=0, province=0, region=0)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_05_api_78dk_platform_cm_base_viewChannel_all(self):
        """
        查询渠道失败

        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_viewChannel('')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_06_api_78dk_platform_cm_base_viewChannel_not_exist(self):
        """
        查询不存在渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_viewChannel(str(fake.latitude()))
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_07_api_78dk_platform_cm_base_viewChannel_all(self):
        """
        查询所有渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_viewChannel(channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['name'], channelname)

    def test_08_api_78dk_platform_cm_base_viewChannels(self):
        """
        查询对应名称的 渠道列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_viewChannels(pagecurrent=1, name=channelname, pagesize=8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_09_api_78dk_platform_cm_base_viewChannels_all(self):
        """
        渠道列表全部
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_viewChannels(pagecurrent=1, name='', pagesize=10)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityNot(json.loads(res)['data']['totalCount'], 0, '数量至少大于等于1')

    def test_10_api_78dk_platform_cm_base_saveChannel_no_examine(self):
        """
        未审核添加子渠道  (应该失败)
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '父级渠道没有审核通过,不能添加下级渠道!')
        Assertion.verity(res['code'], '20000')

    def test_11_api_78dk_platform_cm_base_updateChannel(self):
        """
        编辑渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_updateChannel(
            channeluuid=channelid, city="510100", name=channelname, note='备注', province="510000", region="510107",
            shortname=channelname + '简称', operatoruuid='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_12_api_78dk_platform_cm_state_updateFreezeState_freeze(self):
        """
        冻结渠道
        :return:
        """

        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(updatestate='freeze', uid=channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_13_api_78dk_platform_cm_state_updateFreezeState_normal(self):
        """
        解冻渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(updatestate='normal', uid=channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_14_api_78dk_platform_cm_examine_viewExamineChannels(self):
        """
        渠道审核列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_examine_viewExamineChannels('123', 1, 8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_15_api_78dk_platform_cm_examine_viewExamineChannels_all(self):
        """
        渠道审核列表全部
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_examine_viewExamineChannels(name='', pagecurrent=1, pagesize=8)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_16_api_78dk_platform_cm_examine_examine_false(self):
        """
        渠道审核不通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_examine_examine(
            isadopt='false', message='不过', uid=channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_17_api_78dk_platform_cm_base_saveChannel_examine_false(self):
        """
        渠道审核不通过后添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '父级渠道没有审核通过,不能添加下级渠道!')
        Assertion.verity(res['code'], '20000')

    def test_18_api_78dk_platform_cm_examine_examine_true(self):
        """
        渠道审核通过
        :return:
        """
        xqkj_query.update_info('Tbl_ChannelProfile', 'audit_state="pending_review"',
                               'channel_uuid="{}"'.format(channelid))
        res = WebAction.test_api_78dk_platform_cm_examine_examine(isadopt='true', message='通过', uid=channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_19_api_78dk_platform_cm_state_updateFreezeState_freeze(self):
        """
        冻结渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(uid=channelid, updatestate='freeze')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_20_api_78dk_platform_cm_base_saveChannel_freeze(self):
        """
        冻结渠道后添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '父级渠道不是正常状态,不能添加下级渠道!')
        Assertion.verity(res['code'], '20000')

    def test_21_api_78dk_platform_cm_state_updateFreezeState_normal(self):
        """
        解冻渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(uid=channelid, updatestate='normal')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_22_api_78dk_platform_cm_state_updateOpenCloseState_close(self):
        """
        渠道开关状态为close
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateOpenCloseState(uid=channelid, updatestate='close')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_23_api_78dk_platform_cm_base_saveChannel_state_close(self):
        """
        渠道开关状态为close后添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '父级渠道不是开启状态,不能添加下级渠道!')
        Assertion.verity(res['code'], '20000')

    def test_24_api_78dk_platform_cm_state_updateOpenCloseState_open(self):
        """
        渠道开关状态为open
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateOpenCloseState(uid=channelid, updatestate='open')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_25_api_78dk_platform_cm_base_saveChannel_city_none(self):
        """
        城市为空添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '渠道所属城市不能为空,')
        Assertion.verity(res['code'], '20000')

    def test_26_api_78dk_platform_cm_base_saveChannel_shortname_none(self):
        """
        ShortName为空添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname='',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '渠道简称不能为空!')
        Assertion.verity(res['code'], '20000')

    def test_27_api_78dk_platform_cm_base_saveChannel_name_none(self):
        """
        Name为空添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name='', province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '渠道名称不能为空!')
        Assertion.verity(res['code'], '20000')

    def test_28_api_78dk_platform_cm_base_saveChannel_province_none(self):
        """
        省份为空添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '渠道所属省份不能为空,')
        Assertion.verity(res['code'], '20000')

    def test_29_api_78dk_platform_cm_base_saveChannel_region_none(self):
        """
        所属大区为空添加子渠道失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '所属大区不能为空,')
        Assertion.verity(res['code'], '20000')

    def test_30_api_78dk_platform_cm_base_saveChannel(self):
        """
        添加子渠道成功
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_saveChannel(
            city="510100", name=channelname_stream, province="510000", region="510107",
            shortname=channelname_stream + '简称',
            parentchanneluuid=channelid))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'freezeStateName')
        Assertion.verityContain(res['data'], 'openCloseStateName')
        global channelid_stream
        channelid_stream = res['data']['channelUuid']
        # global_dict.set(channelid_stream=res['data']['channelUuid'])

    def test_31_api_78dk_platform_cm_base_updateChannel(self):
        """
        编辑子渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_updateChannel(
            channeluuid=channelid_stream, city="510100", name=channelname_stream, note='备注', province="510000",
            region="510107", shortname=channelname_stream + '简称', operatoruuid='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_32_api_78dk_platform_cm_state_updateFreezeState_freeze(self):
        """
        冻结子渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(uid=channelid_stream, updatestate='freeze')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_33_api_78dk_platform_cm_state_updateFreezeState_normal(self):
        """
        解冻子渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_updateFreezeState(uid=channelid_stream, updatestate='normal')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_34_api_78dk_platform_cm_examine_examine_false(self):
        """
        已审核通过的接口再次调用接口使渠道审核不过（应该失败）
        :return:
        """
        xqkj_query.update_info('Tbl_ChannelProfile', 'audit_state="pending_review"',
                               'channel_uuid="{}"'.format(channelid))
        res = WebAction.test_api_78dk_platform_cm_examine_examine(isadopt='false', message='不过', uid=channelid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_35_api_78dk_platform_cm_base_legal_viewLegalPerson_fial(self):
        """
        查询法人代表根据渠道uuid
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '您提交的参数异常')

    def test_36_api_78dk_platform_cm_base_business_saveBusinessInfor(self):
        """
        新增机构, 需要先有渠道
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_business_saveBusinessInfor(
            businessaddress='天府软件园', businessaddressgpsloction='天府软件园GPS地址', businessaddresszipcode='000000',
            businesshoursendtime='18:30', businesshoursstarttime='08:30', businessinformationuuid='',
            businessregistrationnumber='443534534543', channelormerchantuuid=channelid, documentaddress='天府软件园',
            email=email, organizationcode='567657675765', socialunifiedcreditcode='34534543534',
            storerentalendtime='2019-01-12', storerentalstarttime='2018-01-12', taxregistrationnumber='34543543543',
            documentprovince=510000, documentcity=510100, documentregion=510104, documentprovincename='',
            documentcityname='', documentregionname='', businessprovince=510000, businesscity=510100,
            businessregion=510104, businessprovincename='', businesscityname='', businessregionname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_37_api_78dk_platform_cm_base_business_viewBusinessInforByChannel(self):
        """
        根据渠道id查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_business_viewBusinessInforByChannel(channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'businessInformationUuid')
        global businnessid
        businnessid = res['data']['businessInformationUuid']

    def test_38_api_78dk_platform_cm_base_business_updateBusinessInfor(self):
        """
        编辑业务机构
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_business_updateBusinessInfor(
            businessaddress='天府软件园', businessaddressgpsloction='天府软件园GPS地址', businessaddresszipcode='000000',
            businesshoursendtime='18:30', businesshoursstarttime='08:30', businessinformationuuid=businnessid,
            businessregistrationnumber='443534534543', channelormerchantuuid=channelid, documentaddress='天府软件园',
            email=email, organizationcode='567657675765', socialunifiedcreditcode='34534543534',
            storerentalendtime='2019-01-12', storerentalstarttime='2018-01-12', taxregistrationnumber='34543543543',
            documentprovince=510000, documentcity=510100, documentregion=510104, documentprovincename='',
            documentcityname='', documentregionname='', businessprovince=510000, businesscity=510100,
            businessregion=510104, businessprovincename='', businesscityname='', businessregionname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_39_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(self):
        """
        根据渠道Uid查询渠道结算
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(channelid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], channelOrMerchantUuid)

    def test_40_api_78dk_platform_mm_viewImageRoleList(self):
        """
        影像资料权限
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageRoleList(subdivisiontype='', uid=channelid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_41_api_78dk_platform_cm_base_clear_saveClearingAccount(self):
        """
        新增结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_clear_saveClearingAccount(
            accountname=channelname, accountnumber='6011826564542944', accountopeningbank='农业银行',
            accounttype='public_accounts', branchname='支行名称', chamberlainidcard='431081199812097872',
            channelormerchantuuid=channelid, city='510100', clearingaccountuuid='',
            linenumber='6756765756', phone='15179366892', province='510000', region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_42_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(self):
        """
        根据渠道id查询结算信息
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_cm_base_clear_viewClearingAccountByChannel(channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'clearingAccountUuid')
        Assertion.verity(res['data']['channelOrMerchantUuid'], channelOrMerchantUuid)
        global clearing_account_uuid
        clearing_account_uuid = res['data']['clearingAccountUuid']

    def test_43_api_78dk_platform_cm_base_clear_updateClearingAccount(self):
        """
        编辑结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_base_clear_updateClearingAccount(
            accountname=channelname, accountnumber='6011826564542944', accountopeningbank='农业银行',
            accounttype='public_accounts', branchname='支行名称', chamberlainidcard='431081199812097872',
            channelormerchantuuid=channelid, city='510100', clearingaccountuuid=clearing_account_uuid,
            linenumber='6756765756', phone='15179366892', province='510000', region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_44_api_78dk_platform_cm_state_viewStateChannels(self):
        """
        渠道状态列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_viewStateChannels(
            pagecurrent=1, freezestate='', auditstate='', openclosestate='', pagesize=10, name='')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_45_api_78dk_platform_cm_state_viewStateChannels_name(self):
        """
        渠道状态列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_cm_state_viewStateChannels(
            pagecurrent=1, freezestate='', auditstate='', openclosestate='', pagesize=10, name=channelname)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_46_api_78dk_platform_common_viewProvinceLists(self):
        """
        省级下拉
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_viewProvinceLists(paramsingle='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityContain(json.loads(res)['data'], 'code')

    def test_47_api_78dk_platform_common_viewCityLists(self):
        """
        省级下拉
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_viewCityLists(paramsingle='110000')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityContain(json.loads(res)['data'], 'code')

    def test_48_api_78dk_platform_common_viewRegionLists(self):
        """
        区/县级下拉
        :return:
        """
        res = WebAction.test_api_78dk_platform_common_viewRegionLists(paramsingle='110100')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityContain(json.loads(res)['data'], 'code')
