#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-12 下午 6:33
@Author     : 罗林
@File       : test_013_app_process_BankCardInfo.py
@desc       : 进件模块自动化测试用例(银行卡认证)
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_app_finance_consumptionAction as AppAction
from xqkj.testAction import loginAction

fake = Factory().create('zh_CN')


class test_013_app_process_BankCardInfo(TestBaseCase):
    def test_001_api_78dk_app_process_getSupportBanks(self):
        """
        查询支持银行（弹窗描述）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getSupportBanks())
        Assertion.verity(res['code'], '10000')

    def test_002_api_78dk_app_process_getBankCardInfo(self):
        """
        查询绑定的银行卡列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getBankCardInfo())
        Assertion.verity(res['code'], '10000')

    def test_003_api_78dk_app_process_saveBankCardInfo(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        xqkj_query.insert_user_bankinfo(loginAction.get_user_uuid())
        global bank_card_no, bank_card_mobile, bill_email
        # user_uuid = loginAction.global_dict.get('user_uuid')
        # bank_card_no, bill_email = xqkj_query.get_info(
        #     'Tbl_UserBankCardInfo', 'bank_card_no, bill_email',
        #     'user_uuid="{}"'.format(user_uuid))
        # bank_card_mobile = fake.phone_number()
        # res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
        #     bankcardmobile=bank_card_mobile, bankcardno=bank_card_no, billemail=bill_email))
        # Assertion.verity(res['code'], '20000')

    @unittest.skip('产生收费')
    def test_004_api_78dk_app_process_saveBankCardInfo_bankcardmobile_none(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile='', bankcardno=bank_card_no, billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '银行卡预留手机号为空！')

    @unittest.skip('产生收费')
    def test_005_api_78dk_app_process_saveBankCardInfo_bankcardmobile_error(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile='abc', bankcardno=bank_card_no, billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '银行卡预留手机号格式错误！')

    @unittest.skip('产生收费')
    def test_006_api_78dk_app_process_saveBankCardInfo_10bankcardmobile(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile='13' + fake.ean8(), bankcardno=bank_card_no, billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '银行卡预留手机号格式错误！')

    @unittest.skip('产生收费')
    def test_007_api_78dk_app_process_saveBankCardInfo_13bankcardmobile(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=fake.ean13(), bankcardno=bank_card_no, billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '银行卡预留手机号格式错误！')

    @unittest.skip('产生收费')
    def test_008_api_78dk_app_process_saveBankCardInfo_bankcardno_none(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno='', billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '银行卡号为空！')

    @unittest.skip('产生收费')
    def test_009_api_78dk_app_process_saveBankCardInfo_bankcardno_error(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno='abc', billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '请输入正确的银行卡号')

    @unittest.skip('产生收费')
    def test_010_api_78dk_app_process_saveBankCardInfo_8bankcardno(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno=fake.ean8(), billemail=bill_email))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '卡号无效/卡号输入错误')

    @unittest.skip('产生收费')
    def test_011_api_78dk_app_process_saveBankCardInfo_billemail_none(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno=bank_card_no, billemail=''))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('产生收费')
    def test_012_api_78dk_app_process_saveBankCardInfo_billemail_error(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno=bank_card_no, billemail='abc'))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('产生收费')
    def test_013_api_78dk_app_process_saveBankCardInfo_billemail_no_com(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno=bank_card_no, billemail='abc@123'))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('产生收费')
    def test_014_api_78dk_app_process_saveBankCardInfo_two(self):
        """
        绑定银行卡1-输入银行卡信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveBankCardInfo(
            bankcardmobile=bank_card_mobile, bankcardno=fake.credit_card_number(), billemail=bill_email))
        Assertion.verity(res['code'], '20000')

    def test_015_api_78dk_app_process_validBankCardInfo_none(self):
        """
        绑定银行卡2-输入手机验证码
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_validBankCardInfo(validcode=''))
        Assertion.verity(res['code'], '20000')

    def test_016_api_78dk_app_process_validBankCardInfo_overdue(self):
        """
        绑定银行卡2-输入手机验证码
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_validBankCardInfo(validcode=loginAction.vercode))
        Assertion.verity(res['code'], '20000')

    def test_017_api_78dk_app_process_choiceBankCard_none(self):
        """
        选择还款银行卡
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_choiceBankCard(userbankcarduuid=''))
        Assertion.verity(res['code'], '20000')

    def test_018_api_78dk_app_process_choiceBankCard_not_exits(self):
        """
        选择还款银行卡
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_choiceBankCard(userbankcarduuid=fake.credit_card_number()))
        Assertion.verity(res['code'], '10000')
