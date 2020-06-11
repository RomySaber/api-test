#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-06-11
@Author     : 罗林
@File       : test_023_app_Mine.py
@desc       : 系统管理自动化测试用例 (需放在审核之后)
"""


import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from hmpt.testAction import AppAction
from hmpt.testAction import loginAction
from common.myFile import MockData as MD
fake = Factory().create('zh_CN')


class test_023_app_Mine(TestBaseCase):
    def test_001_api_78dk_app_perCenter_viewByStagesLists(self):
        """
        分期列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_viewByStagesLists(pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data']['dataList'], 'billState')
        # Assertion.verityContain(res['data']['dataList'], 'created')
        # Assertion.verityContain(res['data']['dataList'], 'loanAmount')
        # Assertion.verityContain(res['data']['dataList'], 'loanOrderUuid')
        # Assertion.verityContain(res['data']['dataList'], 'productName')
        # Assertion.verityContain(res['data']['dataList'], 'storeName')
        # Assertion.verityContain(res['data'], 'pageCurrent')
        # Assertion.verityContain(res['data'], 'pageSize')
        # Assertion.verityContain(res['data'], 'pageTotal')

    def test_002_api_78dk_app_perCenter_renounceApplication_none(self):
        """
        放弃申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_renounceApplication(loanorderuuid=''))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无订单!')

    def test_003_api_78dk_app_perCenter_renounceApplication_error(self):
        """
        放弃申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_renounceApplication(loanorderuuid='abc'))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无订单!')

    def test_004_api_78dk_app_perCenter_renounceApplication_not_exits(self):
        """
        放弃申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_renounceApplication(loanorderuuid=fake.ean8()))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无订单!')

    def test_009_api_78dk_app_login_retrievePw(self):
        """
        忘记密码
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_login_retrievePw(
            vercode='123456', mobile=loginAction.app_phone))
        Assertion.verity(res['code'], 'S0012')
        Assertion.verity(res['msg'], '短信验证码错误!')

    def test_010_api_78dk_app_login_newPw_new_old(self):
        """
        忘记密码(设置新密码)
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(
            password=loginAction.app_passwd, mobile=loginAction.app_phone))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '新密码和旧密码一致!')

    def test_011_api_78dk_app_login_newPw_one(self):
        """
        忘记密码(设置新密码)
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(
            password='123456', mobile=loginAction.app_phone))
        Assertion.verity(res['code'], 'S0006')

    def test_012_api_78dk_app_login_newPw(self):
        """
        忘记密码(设置新密码)
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(
            password=loginAction.app_passwd, mobile=loginAction.app_phone))
        Assertion.verity(res['code'], 'S0006')

    def test_013_api_78dk_app_login_smsLogin(self):
        """
        登录（短信）
        :return: 
        """
        res = json.loads(AppAction.test_api_78dk_app_login_smsLogin(
            vercode='123456', mobile=loginAction.app_phone, jgpushid=loginAction.get_jgPushId()))
        Assertion.verity(res['code'], 'S0012')
        Assertion.verity(res['msg'], '短信验证码错误!')

    def test_014_test_api_78dk_app_bill_getMyBill(self):
        """
        全部账单-分页查询(新)
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_bill_getBillPage(pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')

    def test_015_api_78dk_app_perCenter_loanDatail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 申请详情V1.4.0
        """
        global loanorderuuid
        loanorderuuid = loginAction.global_dict.get('contract_uuid')
        res = AppAction.test_api_78dk_app_perCenter_loanDatail(loanorderuuid=loanorderuuid)
        Assertion.verity(json.loads(res)['code'], 'S0003')
        # Assertion.verity(json.loads(res)['msg'], 'Successful')

    def test_016_api_78dk_app_perCenter_loanDatail_not_exist(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 申请详情V1.4.0,订单不存在
        """
        res = AppAction.test_api_78dk_app_perCenter_loanDatail(loanorderuuid=-1)
        Assertion.verity(json.loads(res)['code'], 'S0003')
        Assertion.verityContain(json.loads(res)['msg'], '查无数据')

    def test_017_api_78dk_app_perCenter_loanDatail_is_null(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 申请详情V1.4.0,订单uuid为空
        """
        res = AppAction.test_api_78dk_app_perCenter_loanDatail(loanorderuuid='')
        Assertion.verity(json.loads(res)['code'], 'S0003')
        Assertion.verityContain(json.loads(res)['msg'], '查无数据')

    def test_018_api_78dk_app_perCenter_loanDatail_overlong(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 申请详情V1.4.0,订单uuid为空
        """
        res = AppAction.test_api_78dk_app_perCenter_loanDatail(loanorderuuid=MD.words_en_lower(256))
        Assertion.verity(json.loads(res)['code'], 'S0003')
        Assertion.verityContain(json.loads(res)['msg'], '查无数据')

    def test_020_api_78dk_app_common_takeGoods_contractuuid_is_not_exist(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 确认收货V1.4.0,运营审核前,合同uuid不存在
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verityContain(json.loads(res)['msg'], '无此订单')

    def test_021_api_78dk_app_common_takeGoods_contractuuid_is_null(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 确认收货V1.4.0,运营审核前,合同uuid为空
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verityContain(json.loads(res)['msg'], '订单uuid不能为空')

    def test_022_api_78dk_app_common_takeGoods_overlong(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 确认收货V1.4.0,运营审核前,合同uuid超长
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=MD.words_en_lower(256))
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '无此订单！')

    @unittest.expectedFailure
    def test_023_api_78dk_app_perCenter_getTakeGoodsContent(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 获取确认收货协议参数V1.40
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=loanorderuuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '成功')

    def test_024_api_78dk_app_perCenter_getTakeGoodsContent_contractuuid_is_null(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 获取确认收货协议参数V1.40.合同uuid为空
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '订单uuid不能为空！')

    def test_025_api_78dk_app_perCenter_getTakeGoodsContent_contractuuid_is_not_exist(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 获取确认收货协议参数V1.40.合同uuid不存在
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '无此订单！')

    def test_026_api_78dk_app_perCenter_getTakeGoodsContent_contractuuid_overlong(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 获取确认收货协议参数V1.40.合同uuid不存在
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=MD.words_en(256))
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '无此订单！')

    def test_027_api_78dk_app_bill_immediateRepayment_none(self):
        """
        desc       : 立刻还款V1.5.0， 账单Uuid为空
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_immediateRepayment(userbilluuid='', userbankcarduuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '没有账单')

    def test_028_api_78dk_app_bill_immediateRepayment_not_exits(self):
        """
        desc       : 立刻还款V1.5.0， 账单Uuid不存在
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_immediateRepayment(userbilluuid=MD.wordAndNum(20), userbankcarduuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '没有账单')

    def test_029_api_78dk_app_bill_immediateRepayment_userbankcarduuid_none(self):
        """
        desc       : 立刻还款V1.5.0， userbankcarduuidUuid为空
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_immediateRepayment(userbilluuid=loanorderuuid, userbankcarduuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '没有账单')

    def test_030_api_78dk_app_bill_immediateRepayment_userbankcarduuid_not_exits(self):
        """
        desc       : 立刻还款V1.5.0， userbankcarduuid Uuid不存在
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_immediateRepayment(userbilluuid=loanorderuuid,
                                                                  userbankcarduuid=MD.wordAndNum(20))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '没有账单')

    def test_031_api_78dk_app_bill_immediateRepayment(self):
        """
        desc       : 立刻还款V1.5.0
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_immediateRepayment(userbilluuid=loanorderuuid, userbankcarduuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '没有账单')

    def test_032_api_78dk_app_bill_PaymentStatus_non(self):
        """
        desc       : 还款状态 v1.5.0， 账单Uuid为空
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_paymentStatus(contractuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_033_api_78dk_app_bill_PaymentStatus_not_exits(self):
        """
        desc       : 还款状态 v1.5.0， 账单Uuid不存在
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_paymentStatus(contractuuid=MD.wordAndNum(20))
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_034_api_78dk_app_bill_PaymentStatus(self):
        """
        desc       : 还款状态 v1.5.0， 账单Uuid为空
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_paymentStatus(contractuuid=loanorderuuid)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_035_app_bill_getMyBill_billdate_none(self):
        """
        desc       : 我的账单v1.0.0
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_getMyBill(billdate='')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_036_app_bill_getMyBill(self):
        """
        desc       : 我的账单v1.0.0
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_getMyBill(billdate='')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_037_app_bill_getMyBill_contractuuid_none(self):
        """
        desc       : 我的账单v1.0.0
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_getMyBill(billdate='')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_038_app_bill_getMyBill_contractuuid_not_exites(self):
        """
        desc       : 我的账单v1.0.0
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_bill_getMyBill(billdate='1574956800')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_039_api_78dk_app_perCenter_findRejectModel(self):
        """
        desc       : 根据订单查询被驳回的模块--美佳v1.0.4新增
        author     : 罗林
        """
        res = AppAction.test_api_78dk_app_perCenter_findRejectModel(contractuuid=loanorderuuid)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_099_api_78dk_app_login_loginOut(self):
        """
        退出登录
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_login_loginOut())
        Assertion.verity(res['code'], '10000')
