#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-08-20
@Author     : QA
@File       : test_005_sht_singing.py
@desc       : 商户签约测试用例
"""
import json
import unittest
from faker import Factory
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from xqkj.query import sht_query
from xqkj.testAction import ShtAction
from xqkj.testAction import loginAction
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import specialAction
import os
fake = Factory().create('zh_CN')
mobile = '131' + fake.ean8()
idcard = fake.ssn(min_age=18, max_age=100)
name = fake.name()
# 商户名称
merchantname = fake.company_prefix() + loginAction.sign


class test_005_sht_singing(TestBaseCase):
    def test_001_api_78dk_sht_merchant_signing(self):
        """
        立即签约，输入为空
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname='', merchantname='', signphone=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityFalse(res['isPage'])

    def test_002_api_78dk_sht_merchant_signing_256signname(self):
        """
        立即签约，商户正常，公司名称正常的，名字超长的
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(
            ShtAction.test_api_78dk_sht_merchant_signing(signname=MockData.words_cn(256), merchantname=merchantname,
                                                         signphone=mobile))
        Assertion.verity(res['code'], '20000')
        Assertion.verityFalse(res['isPage'])

    def test_003_api_78dk_sht_merchant_signing_256merchantname(self):
        """
        立即签约，商户正常，公司名称超长，名字正常
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(
            ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=MockData.words_cn(256),
                                                         signphone=mobile))
        Assertion.verity(res['code'], '20000')
        Assertion.verityFalse(res['isPage'])

    def test_004_api_78dk_sht_merchant_signing_10mobile(self):
        """
        立即签约，10 手机号错误，公司名称正常，名字正常
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=merchantname,
                                                                      signphone='1345434567'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '申请人电话格式不合法')

    def test_005_api_78dk_sht_merchant_signing_mobile_not_num(self):
        """
        立即签约，手机号错误,非数字，公司名称正常，名字正常
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=merchantname,
                                                                      signphone='..ddddweew手机号错误测试'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '申请人电话格式不合法')

    def test_006_api_78dk_sht_merchant_signing_12mobile(self):
        """
        立即签约，12 手机号错误，公司名称正常，名字正常
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=merchantname,
                                                                      signphone='1838167400433'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '申请人电话格式不合法')

    def test_007_api_78dk_sht_merchant_signing_3merchantname(self):
        """
        立即签约，商户正常，公司名称3字符，名字正常
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(
            ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=merchantname, signphone=mobile))
        Assertion.verity(res['code'], '10000')
        global sht_merchantUuid
        sht_merchantUuid = res['data']['merchantUuid']
        loginAction.global_dict.set(sht_merchantUuid=res['data']['merchantUuid'])
        loginAction.global_dict.set(sht_merchantName=merchantname)

    def test_008_api_78dk_sht_mm_findMerchantSummary(self):
        """
        商户信息详情列表
        :return:
        """
        sht_query.update_wx_merchart_null(sht_merchantUuid)
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantSummary(uuid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_009_api_78dk_sht_mm_saveMerchantImg(self):
        """
        上传图片
        :return:
        """
        global shfrsfzfsc, shfrsfzf, shfrsfzz, shzm, shzzjgdm, shswdjz, shyyzz
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource', '1.png')
        res = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shfrsfzfsc',
                                                                 image_path=image_path))
        shfrsfzfsc = res['data']['uuid']
        res1 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shfrsfzf',
                                                                 image_path=image_path))
        shfrsfzf = res1['data']['uuid']
        res2 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shfrsfzz',
                                                                 image_path=image_path))
        shfrsfzz = res2['data']['uuid']
        res3 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shzm',
                                                                             image_path=image_path))
        shzm = res3['data']['uuid']
        res4 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shzzjgdm',
                                                                            image_path=image_path))
        shzzjgdm = res4['data']['uuid']
        res5 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shswdjz',
                                                                             image_path=image_path))
        shswdjz = res5['data']['uuid']
        res6 = json.loads(specialAction.test_api_78dk_sht_mm_saveMerchantImg(uuid=sht_merchantUuid, key='shyyzz',
                                                                             image_path=image_path))
        shyyzz = res6['data']['uuid']

    def test_010_api_78dk_sht_mm_base_legal_modifylegalperson(self):
        """
        保存商户法人信息--正常场景
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc=shfrsfzfsc,
                name=name, uuid=sht_merchantUuid, shfrsfzf=shfrsfzf, mobile=mobile,
                cardnumber=idcard, shfrsfzz=shfrsfzz))
        Assertion.verity(res['code'], '10000')

    def test_011_api_78dk_sht_mm_base_legal_modifylegalperson_12mobile(self):
        """
        保存商户法人信息--异常场景-法人联系电话错误
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name='法人名字',
            uuid=sht_merchantUuid, shfrsfzf='', mobile='136543456789', cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '法人联系电话格式不合法')

    def test_012_api_78dk_sht_mm_base_legal_modifylegalperson_10mobile(self):
        """
        保存商户法人信息--异常场景-法人联系电话错误
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name='法人名字',
            uuid=sht_merchantUuid, shfrsfzf='', mobile='1365434567', cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '法人联系电话格式不合法')

    def test_013_api_78dk_sht_mm_base_legal_modifylegalperson_19cardnumber(self):
        """
        保存商户法人信息--异常场景-法人身份证号错误
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name='法人名字',
            uuid=sht_merchantUuid, shfrsfzf='', mobile=mobile, cardnumber=idcard + '1', shfrsfzz=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '法人身份证格式错误')

    def test_014_api_78dk_sht_mm_base_legal_modifylegalperson_17cardnumber(self):
        """
        保存商户法人信息--异常场景-法人身份证号错误
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name='法人名字',
            uuid=sht_merchantUuid, shfrsfzf='', mobile=mobile, cardnumber=MockData.strNumber(17), shfrsfzz=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '法人身份证格式错误')

    def test_015_api_78dk_sht_mm_base_legal_modifylegalperson_256name(self):
        """
        保存商户法人信息--异常场景-法人姓名超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name=MockData.words_cn(256),
                uuid=sht_merchantUuid, shfrsfzf='', mobile=mobile, cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '法人姓名长度过长')

    def test_016_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo(self):
        """
        保存商户帐户信息---个人账户
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid,
                shzm=shzm, accounttype='public_accounts',
                branchname='支行名称', accountname='开户人姓名'))
        Assertion.verity(res['code'], '10000')

    def test_017_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_accountnumber_not_num(self):
        """
        保存商户帐户信息---企业账户-异常场景--银行卡号错误
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='54645645645645654非数字的银行卡号',
                shyhkfm='', accountopeningbank='123', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '银行卡号格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_018_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_30accountnumber(self):
        """
        保存商户帐户信息---企业账户-异常场景--银行卡号错误
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber=MockData.bankAccount(30),
                shyhkfm='', accountopeningbank='123', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '银行卡号格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_019_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_accountnumber_error(self):
        """
        保存商户帐户信息---企业账户-异常场景--银行卡号错误
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='nnnfgfggdfgdfdgdf',
                shyhkfm='', accountopeningbank='123', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '银行卡号格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_020_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_accountnumber_none(self):
        """
        保存商户帐户信息---企业账户-异常场景--银行卡为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='', shyhkfm='',
            accountopeningbank='123', shyhkzm='', uuid=sht_merchantUuid, shzm='', accounttype='public_accounts',
            branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '银行卡号格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_021_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_credit_card(self):
        """
        保存商户帐户信息---企业账户-异常场景-信用卡号
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber=fake.credit_card_number(),
                shyhkfm='', accountopeningbank='开户行名称银行卡为空', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '帐户类型不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_022_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_none_str(self):
        """
        保存商户帐户信息---企业账户-异常场景--银行卡为空字符串
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='     ', shyhkfm='',
                accountopeningbank='123', shyhkzm='', uuid=sht_merchantUuid, shzm='', accounttype='public_accounts',
                branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '银行卡号格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_023_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_11accountopeningbank(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户行名称超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank=MockData.words_cn(11), shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '开户行名称过长')
        Assertion.verity(res['code'], 'S0006')

    def test_024_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_accountopeningbank_none(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户行名称输入空字符串
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='     ', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '开户行名称不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_025_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_accountname_none(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户人姓名为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称农业', accountname=''))
        Assertion.verity(res['msg'], '帐户名称不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_026_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_21branchname(self):
        """
        保存商户帐户信息---企业账户-异常场景--支行名称超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname=MockData.words_cn(21), accountname='开户人姓名'))
        Assertion.verity(res['msg'], '支行名称过长')
        Assertion.verity(res['code'], 'S0006')

    @unittest.skip('未验证支行名称')
    def test_027_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_branchname_none(self):
        """
        保存商户帐户信息---企业账户-异常场景--支行名称为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '支行名称不能为空')
        Assertion.verity(res['code'], 'S0006')

    @unittest.skip('未验证支行名称')
    def test_028_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_branchname_none_str(self):
        """
        保存商户帐户信息---企业账户-异常场景--支行名称为空字符串
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='       ', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '支行名称不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_029_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_branchname_special_str(self):
        """
        保存商户帐户信息---企业账户-异常场景--支行名称为特殊字符串
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname=MockData.wordAndNum(35), accountname='开户人姓名'))
        Assertion.verity(res['msg'], '支行名称过长')
        Assertion.verity(res['code'], 'S0006')

    def test_030_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_21shzm(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户许可证超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid,
                shzm=shzm, accounttype='public_accounts', branchname='支行名称', accountname='开户人姓名'))
        # Assertion.verity(res['msg'], '数据完整性错误')
        Assertion.verity(res['code'], '10000')

    def test_031_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_shzm_none(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户许可证为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='', accounttype='',
                branchname='支行名称', accountname='开户人姓名'))
        Assertion.verity(res['msg'], '帐户类型不能为空')
        Assertion.verity(res['code'], 'S0006')

    @unittest.skip('未断言shzm')
    def test_032_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_shzm_none_str(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户许可证空字符串
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='       ',
                accounttype='public_accounts', branchname='支行名称', accountname='开户人姓名'))
        # Assertion.verity(res['msg'], '数据完整性错误')
        Assertion.verity(res['code'], '10000')

    @unittest.skip('未断言shzm')
    def test_033_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_shzm_not_all_num(self):
        """
        保存商户帐户信息---企业账户-异常场景--开户许可证空非纯数字
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, accountname='开户人姓名',
                shzm=MockData.wordAndNum(256), accounttype='public_accounts', branchname='支行名称'))
        # Assertion.verity(res['msg'], '数据完整性错误')
        Assertion.verity(res['code'], '10000')

    @unittest.skip('组织机构代码可以为空，跳过为空的用例')
    def test_034_api_78dk_sht_mm_modifymerchantinfo_organizationcode_null(self):
        """
        保存商户基础信息---组织结构不填
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode=None, taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '组织机构代码不能为空')
        Assertion.verity(res['code'], 'S0006')
        
    @unittest.skip('组织机构代码可以为空，跳过为空的用例')
    def test_035_api_78dk_sht_mm_modifymerchantinfo_organizationcode_nullstring(self):
        """
        保存商户基础信息---组织结构空字符串
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='             ', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verityContain(res['msg'], '组织机构代码不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_036_api_78dk_sht_mm_modifymerchantinfo_10organizationcode(self):
        """
        保存商户基础信息---组织结构超长
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode=MockData.strNumber(10), taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '组织机构代码过长')
        Assertion.verity(res['code'], 'S0006')

    def test_037_api_78dk_sht_mm_modifymerchantinfo_organizationcode_notnumber(self):
        """
        保存商户基础信息---组织结构不是存数字
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode=MockData.words_en(10), taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '组织机构代码过长')
        Assertion.verity(res['code'], 'S0006')

    def test_038_api_78dk_sht_mm_modifymerchantinfo_taxregistrationnumber_null(self):
        """
        保存商户基础信息---税务登记证号码为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm=shzzjgdm, name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='',
            socialunifiedcreditcode='123', shswdjz=shswdjz, shyyzz=shyyzz, installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['code'], '10000')

    def test_039_api_78dk_sht_mm_modifymerchantinfo_taxregistrationnumber_notnumber(self):
        """
        保存商户基础信息---税务登记证号码不是纯数字
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber=MockData.words_en(256),
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '税务登记证号过长')
        Assertion.verity(res['code'], 'S0006')

    def test_040_api_78dk_sht_mm_modifymerchantinfo_name_null(self):
        """
        保存商户基础信息---商户名为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name='',
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '公司名称不能为空')

    def test_041_api_78dk_sht_mm_modifymerchantinfo_21name(self):
        """
        保存商户基础信息---商户名为超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=MockData.words_cn(21),
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '公司名称过长')
        Assertion.verity(res['code'], 'S0006')

    def test_042_api_78dk_sht_mm_modifymerchantinfo_socialunifiedcreditcode_null(self):
        """
        保存商户基础信息---统一社会信用代码为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '社会统一征信代码不能为空')

    def test_043_api_78dk_sht_mm_modifymerchantinfo_19socialunifiedcreditcode(self):
        """
        保存商户基础信息---统一社会信用代码为超长
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode=MockData.strNumber(19), shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '社会统一征信代码过长')
        Assertion.verity(res['code'], 'S0006')

    def test_044_api_78dk_sht_mm_modifymerchantinfo_socialunifiedcreditcode_notnumber(self):
        """
        保存商户基础信息---统一社会信用代码为非数字
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='  546546nnn,<<>*&()()', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '社会统一征信代码过长')
        Assertion.verity(res['code'], 'S0006')

    def test_045_api_78dk_sht_mm_modifymerchantinfo_tradefirst_null(self):
        """
        保存商户基础信息---所属行业(第一级id)为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '所属行业不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_046_api_78dk_sht_mm_modifymerchantinfo_city_null(self):
        """
        保存商户基础信息---城市代码空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='', province='110000', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '所在市不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_047_api_78dk_sht_mm_modifymerchantinfo_tradesecond_null(self):
        """
        保存商户基础信息--所属行业(第二级id)空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='110000', papermergen=False, tradesecond=''))
        Assertion.verity(res['msg'], '所属行业不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_048_api_78dk_sht_mm_modifymerchantinfo_province_null(self):
        """
        保存商户基础信息--省代码空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
            uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123',
            socialunifiedcreditcode='123', shswdjz='', shyyzz='', installmentcooperationorgs=[],
            city='110100', province='', papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '所在省不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_049_api_78dk_sht_mm_modifymerchantinfo(self):
        """
        保存商户基础信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst=5,
            shzzjgdm=shzzjgdm, name=name, uuid=sht_merchantUuid, organizationcode='123',
            taxregistrationnumber='123', socialunifiedcreditcode='123', shswdjz=shswdjz,
            shyyzz=shyyzz, installmentcooperationorgs=[{"name": "1", "uuid": ""}, {"name": "2", "uuid": ""},
            {"name": "3", "uuid": ""}], city='110100', province='110000', papermergen=False, tradesecond=20))
        Assertion.verity(res['code'], '10000')

    def test_050_api_78dk_platform_mm_bd_saveBDMerchant(self):
        """
        新增商户BD信息
        :return:
        """
        bdinfouuid = loginAction.global_dict.get('bdinfouuid')
        bd_name = loginAction.global_dict.get('bd_name')
        res = PlatformAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid=bdinfouuid,
            merchantuuid=sht_merchantUuid, name=bd_name, remark='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_051_api_78dk_sht_mm_submitmerchant(self):
        """
        提交审核
        根据商户名字查询出商户的uuid
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_submitMerchant(uuid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_052_api_78dk_platform_mm_examine_merchanrExamine_fail(self):
        """
        商户审核
        :return:
        """
        res = PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='pass', message='通过',
                                                                               uid=sht_merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_053_api_78dk_sht_mm_findMerchantSummary(self):
        """
        商户信息详情列表
        :return:
        """
        # sht_query.update_wx_merchart_null(sht_merchantUuid)
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantSummary(uuid=sht_merchantUuid))
        print(res)
        Assertion.verity(res['code'], '10000')
