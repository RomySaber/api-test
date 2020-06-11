#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       : 2019-08-16
@Author     : QA
@File       : test_006_sht_audit.py
@desc       : 签约商户审核及后续操作测试用例
"""
import json
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import sht_query
from xqkj.testAction import ShtAction
from xqkj.testAction import loginAction
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction


fake = Factory().create('zh_CN')
mobile = '131' + fake.ean8()
idcard = fake.ssn(min_age=18, max_age=100)
name = fake.name()


class test_006_sht_audit(TestBaseCase):
    def test_001_api_78dk_sht_merchant_signing_merchantname_audit_state_pending(self):
        """
        商户名称是否已经在申请中、待审核、资料未完善、被拒绝、已经有存在的商户（审核通过的商户）
        立即签约，手机号正常，商户名称是否已经在申请中(微信申请、后台申请)，名字正常
        :return:
        """
        global merchantname
        merchantname = loginAction.global_dict.get("sht_merchantName")
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name + '1', merchantname=merchantname,
                                                                      signphone=mobile))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['code'], 'M10000')

    def test_002_api_78dk_sht_mm_base_legal_modifylegalperson_auditing(self):
        """
        保存商户法人信息-- 审批中的商户，修改法人信息-电话
        :return:
        """
        global sht_merchantUuid
        sht_merchantUuid = loginAction.global_dict.get("sht_merchantUuid")
        sht_query.update_wx_merchart_null(sht_merchantUuid)
        sht_query.update_audit_state("pending_review", sht_merchantUuid)
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name=name, uuid=sht_merchantUuid,
                shfrsfzf='', mobile='15212512632', cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_003_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_auditing(self):
        """
        保存商户帐户信息---个人账户-#审批中的商户，修改账户信息-支行名称
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称修改', accountname='开户人姓名', ))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_004_api_78dk_sht_mm_modifymerchantinfo_auditing(self):
        """
        保存商户基础信息---审核拒绝的商户，修改公司信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
        uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123', socialunifiedcreditcode='123',
        shswdjz='', shyyzz='', installmentcooperationorgs=[], city='110100', province='110000',
        papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_005_api_78dk_platform_mm_examine_merchanrExamine_fail(self):
        """
        商户审核fail
        :return:
        """
        sht_query.update_audit_state("pending_review", sht_merchantUuid)
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='fail', message='不通过',
        uid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_006_api_78dk_sht_merchant_signing_audit_state_false(self):
        """
        立即签约，手机号正常，商户名称被拒绝，(微信申请、后台申请)，名字正常
        :return:
        """
        sht_query.update_audit_state("fail", sht_merchantUuid)
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name + '1', merchantname=merchantname,
                                                                      signphone=mobile))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '你已经申请过商户了')

    def test_007_api_78dk_sht_mm_base_legal_modifylegalperson_audit_fail(self):
        """
        保存商户法人信息--# 审核拒绝的商户，修改法人信息-电话
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name=name, uuid=sht_merchantUuid,
                shfrsfzf='', mobile='15212512632', cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_008_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_audit_fail(self):
        """
        保存商户帐户信息---个人账户-#审批中的商户，修改账户信息-支行名称
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称修改', accountname='开户人姓名', ))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_sht_mm_modifymerchantinfo_audit_fail(self):
        """
        保存商户基础信息---审核拒绝的商户，修改公司信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
        uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123', socialunifiedcreditcode='123',
        shswdjz='', shyyzz='', installmentcooperationorgs=[], city='110100', province='110000',
        papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_010_api_78dk_platform_mm_examine_merchanrExamine_pass(self):
        """
        商户审核fail
        :return:
        """
        sht_query.update_audit_state("pending_review", sht_merchantUuid)
        res = json.loads(PlatformAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='pass', message='通过',
        uid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_011_api_78dk_sht_merchant_signing_audit_state_pass(self):
        """
        立即签约，手机号正常，商户名称已经存在（审核通过的），(微信申请、后台申请)，名字正常
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_signing(signname=name + '1', merchantname=merchantname,
                                                                      signphone=mobile))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '你已经申请过商户了')

    def test_012_api_78dk_sht_mm_base_legal_modifylegalperson_audit_pass(self):
        """
        保存商户法人信息--# 审核通过的商户，修改法人信息-电话
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_legal_modifyLegalPerson(shfrsfzfsc='', name=name, uuid=sht_merchantUuid,
                shfrsfzf='', mobile='15212512632', cardnumber=idcard, shfrsfzz=''))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_sht_mm_modifymerchantinfo_audit_pass(self):
        """
        保存商户基础信息---审核拒绝的商户，修改公司信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_modifyMerchantInfo(tradefirst='1', shzzjgdm='', name=name,
        uuid=sht_merchantUuid, organizationcode='123', taxregistrationnumber='123', socialunifiedcreditcode='123',
        shswdjz='', shyyzz='', installmentcooperationorgs=[], city='110100', province='110000',
        papermergen=False, tradesecond='7'))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_014_api_78dk_sht_mm_base_ShtActioniness_modifyaccountinfo_audit_pass(self):
        """
        保存商户帐户信息---个人账户-#审批中的商户，修改账户信息-支行名称
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_mm_base_business_modifyAccountInfo(accountnumber='6228481268248914675',
                shyhkfm='', accountopeningbank='开户行名称', shyhkzm='', uuid=sht_merchantUuid, shzm='',
                accounttype='public_accounts', branchname='支行名称修改', accountname='开户人姓名', ))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_015_api_78dk_sht_merchant_signing_sec(self):
        """
        立即签约， 重复签约
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_merchant_signing(signname=name, merchantname=merchantname, signphone=mobile))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '你已经申请过商户了')

    def test_016_api_78dk_sht_mm_submitmerchant_uuid_none(self):
        """
        提交审核
        根据商户名字查询出商户的uuid
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_submitMerchant(uuid=''))
        Assertion.verity(res['msg'], '无效的商户')
        Assertion.verity(res['code'], '20000')

    def test_017_api_78dk_sht_mm_submitmerchant(self):
        """
        提交审核
        根据商户名字查询出商户的uuid
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_submitMerchant(uuid=sht_merchantUuid))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_018_api_78dk_sht_mm_submitmerchant_sec(self):
        """
        提交审核, 再次提交
        根据商户名字查询出商户的uuid
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_submitMerchant(uuid=sht_merchantUuid))
        Assertion.verity(res['msg'], '商户状态不可修改')
        Assertion.verity(res['code'], '20000')

    def test_019_api_78dk_sht_mm_findMerchantSummary_none(self):
        """
        商户信息详情列表
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantSummary(uuid=''))
        Assertion.verity(res['code'], '40000')

    def test_020_api_78dk_sht_mm_findMerchantSummary(self):
        """
        商户信息详情列表
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantSummary(uuid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_021_api_78dk_sht_mm_base_legal_findlegalperson_none(self):
        """
        查看商户法人信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_findLegalPerson(uuid=''))
        Assertion.verity(res['code'], '10000')

    def test_022_api_78dk_sht_mm_base_legal_findlegalperson(self):
        """
        查看商户法人信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_base_legal_findLegalPerson(uuid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_023_api_78dk_sht_common_queryprovincecitys(self):
        """
        查询省市
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_common_queryProvinceCitys())
        Assertion.verity(res['code'], '10000')

    def test_024_api_78dk_sht_common_querytrade(self):
        """
        查询行业字典
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_common_queryTrade())
        Assertion.verity(res['code'], '10000')

    def test_025_api_78dk_sht_mm_savemerchantimg(self):
        """
        保存一张图片
        :return:
        """

        res = json.loads(ShtAction.test_api_78dk_sht_mm_saveMerchantImg(uuid='', key=''))
        Assertion.verity(res['code'], '20000')

    def test_026_api_78dk_sht_common_queryaccounttype(self):
        """
        查询帐户类型字典
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_common_queryAccountType())
        Assertion.verity(res['code'], '10000')

    def test_027_api_78dk_sht_mm_deletemerchantimg(self):
        """
        删除一张图片
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_deleteMerchantImg(uuid='', imageuuid=''))
        Assertion.verity(res['code'], '10000')

    def test_028_api_78dk_sht_mm_querymerchantimg(self):
        """
        查看商户补充图片
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_queryMerchantImg(uuid=''))
        Assertion.verity(res['code'], '10000')

    def test_029_api_78dk_sht_product_queryproducts(self):
        """
        查看商品列表
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_product_queryProducts(pagesize=10, uuid='', pagenum=1))
        Assertion.verity(res['code'], '10000')

    def test_030_api_78dk_sht_bm_findbilldetail(self):
        """
        查看订单详情
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_findBillDetail(orderuuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统数据对应异常')

    def test_031_api_78dk_sht_store_savestoreimg(self):
        """
        保存单张图片
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_saveStoreImg(key='', storeuuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '未知的图片分类')

    def test_032_api_78dk_sht_store_deletestoreimg(self):
        """
        删除单张图片
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_deleteStoreImg(imageuuid='', storeuuid=''))
        Assertion.verity(res['code'], '10000')

    def test_033_api_78dk_sht_store_findlegalperson(self):
        """
        同法人
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_findLegalPerson(merchantuuid=''))
        Assertion.verity(res['code'], '10000')

    def test_034_api_78dk_sht_common_queryprovincecityregions(self):
        """
        查询省市区
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_common_queryProvinceCityRegions())
        Assertion.verity(res['code'], '10000')

    def test_035_api_78dk_sht_mm_findmerchantinfo_none(self):
        """
        查看商户基础信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantInfo(uuid=''))
        Assertion.verity(res['code'], '20000')

    def test_037_api_78dk_sht_mm_base_ShtActioniness_findaccountinfo_none(self):
        """
        查看商户帐户信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantInfo(uuid=''))
        Assertion.verity(res['code'], '20000')

    def test_038_api_78dk_sht_mm_base_ShtActioniness_findaccountinfo(self):
        """
        查看商户帐户信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_mm_findMerchantInfo(uuid=sht_merchantUuid))
        Assertion.verity(res['code'], '10000')

    def test_039_api_78dk_sht_merchant_findstate(self):
        """
        查询用户对应商户状态
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_findState())
        Assertion.verity(res['code'], '10000')
