#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-11-05
@Author     : QA
@File       : test_center_xqc.py
@desc       : 接口中心-小启查公众号
"""
import json

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqwx.testAction import XqwxAction


class test_center_xqc(TestBaseCase):
    def test_report_ai_phoneType(self):
        rs = XqwxAction.test_report_ai_phoneType(phone='')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_user_login(self):
        rs = XqwxAction.test_user_login('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_user_changePhone(self):
        rs = XqwxAction.test_user_changePhone('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_validateCode(self):
        rs = XqwxAction.test_common_validateCode('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_user_info(self):
        rs = XqwxAction.test_user_info()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_getVerifyCode(self):
        rs = XqwxAction.test_common_getVerifyCode('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_getVerifyPic(self):
        rs = XqwxAction.test_common_getVerifyPic()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_verify_t(self):
        rs = XqwxAction.test_verify_t()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_report_list(self):
        rs = XqwxAction.test_common_report_list('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_report_total(self):
        rs = XqwxAction.test_common_report_total()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_users(self):
        rs = XqwxAction.test_report_users('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_history(self):
        rs = XqwxAction.test_report_history('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_push(self):
        rs = XqwxAction.test_report_push('', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_addUser(self):
        rs = XqwxAction.test_report_addUser('', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_detail(self):
        rs = XqwxAction.test_report_detail('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_pay_getParam(self):
        rs = XqwxAction.test_report_pay_getParam('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_pay_getGoods(self):
        rs = XqwxAction.test_report_pay_getGoods()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneRefreshSms(self):
        rs = XqwxAction.test_report_ai_phoneRefreshSms('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneConfig(self):
        rs = XqwxAction.test_report_ai_phoneConfig('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneRefreshPic(self):
        rs = XqwxAction.test_report_ai_phoneRefreshPic('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneLogin(self):
        rs = XqwxAction.test_report_ai_phoneLogin()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneGetStatus(self):
        rs = XqwxAction.test_report_ai_phoneGetStatus('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phoneGetResult(self):
        rs = XqwxAction.test_report_ai_phoneGetResult('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_getReportScore(self):
        rs = XqwxAction.test_report_ai_getReportScore('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_callback_report(self):
        rs = XqwxAction.test_report_callback_report('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_report_price(self):
        rs = XqwxAction.test_common_report_price()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_common_getShareConf(self):
        rs = XqwxAction.test_common_getShareConf('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_news_list(self):
        rs = XqwxAction.test_news_list('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_list(self):
        rs = XqwxAction.test_report_list('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_news_info(self):
        rs = XqwxAction.test_news_info('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_applyTd(self):
        rs = XqwxAction.test_report_applyTd('', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_jlogin(self):
        rs = XqwxAction.test_report_business_jlogin('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_jgetqrcode(self):
        rs = XqwxAction.test_report_business_jgetqrcode()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_jverifyqrcode(self):
        rs = XqwxAction.test_report_business_jverifyqrcode('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_jverifycode(self):
        rs = XqwxAction.test_report_business_jverifycode('', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_jgetcode(self):
        rs = XqwxAction.test_report_business_jgetcode()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_tlogin(self):
        rs = XqwxAction.test_report_business_tlogin('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_tgetqrcode(self):
        rs = XqwxAction.test_report_business_tgetqrcode()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_tverifyqrcode(self):
        rs = XqwxAction.test_report_business_tverifyqrcode('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_tverifycode(self):
        rs = XqwxAction.test_report_business_tverifycode('', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_tgetcode(self):
        rs = XqwxAction.test_report_business_tgetcode('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_history(self):
        rs = XqwxAction.test_h5_report_history('', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_login(self):
        rs = XqwxAction.test_h5_report_login('', '', '', '', '', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_phoneConfig(self):
        rs = XqwxAction.test_h5_report_phoneConfig('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_phoneType(self):
        rs = XqwxAction.test_h5_report_phoneType('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_phoneRefreshPic(self):
        rs = XqwxAction.test_h5_report_phoneRefreshPic('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_phoneRefreshSms(self):
        rs = XqwxAction.test_h5_report_phoneRefreshSms('', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_getReportScore(self):
        rs = XqwxAction.test_h5_report_getReportScore('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_detail(self):
        rs = XqwxAction.test_h5_report_detail('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_getStatus(self):
        rs = XqwxAction.test_h5_report_getStatus('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_callback(self):
        rs = XqwxAction.test_h5_report_callback('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_reportPrice(self):
        rs = XqwxAction.test_h5_report_reportPrice()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_list(self):
        rs = XqwxAction.test_h5_report_list('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_payh5_payStatus(self):
        rs = XqwxAction.test_payh5_payStatus('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_payh5_alipay_getParam(self):
        rs = XqwxAction.test_payh5_alipay_getParam('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_payh5_wechat_getParam(self):
        rs = XqwxAction.test_payh5_wechat_getParam('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_apply(self):
        rs = XqwxAction.test_channel_apply()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_agentBasic(self):
        rs = XqwxAction.test_channel_agent_agentBasic()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_apply(self):
        rs = XqwxAction.test_channel_agent_apply('', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_rewardList(self):
        rs = XqwxAction.test_channel_agent_rewardList('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_cashList(self):
        rs = XqwxAction.test_channel_agent_cashList('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_cashApply(self):
        rs = XqwxAction.test_channel_agent_cashApply()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_orderList(self):
        rs = XqwxAction.test_channel_agent_orderList('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_inventList(self):
        rs = XqwxAction.test_channel_agent_inventList('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_channel_agent_getStatus(self):
        rs = XqwxAction.test_channel_agent_getStatus()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_getWaitPaymentReport(self):
        rs = XqwxAction.test_report_getWaitPaymentReport()
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_insertReportComment(self):
        rs = XqwxAction.test_report_insertReportComment('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_insertReportComment(self):
        rs = XqwxAction.test_h5_report_insertReportComment('', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phonesecondverify(self):
        rs = XqwxAction.test_report_ai_phonesecondverify('', '', '', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phonepicsecond(self):
        rs = XqwxAction.test_report_ai_phonepicsecond('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phonesmssecond(self):
        rs = XqwxAction.test_report_ai_phonesmssecond('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_phonestatus(self):
        rs = XqwxAction.test_report_ai_phonestatus('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_secondPic(self):
        rs = XqwxAction.test_report_ai_secondPic('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_secondSms(self):
        rs = XqwxAction.test_report_ai_secondSms('', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_secondSendCode(self):
        rs = XqwxAction.test_report_ai_secondSendCode('', '', '', '', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_updateIsNotice(self):
        rs = XqwxAction.test_report_updateIsNotice('')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_ai_compiledReportSubmit(self):
        rs = XqwxAction.test_report_ai_compiledReportSubmit('', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_report_business_businessReportSubmit(self):
        rs = XqwxAction.test_report_business_businessReportSubmit('', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_yysReportSubmitH5(self):
        rs = XqwxAction.test_h5_report_yysReportSubmitH5('', '', '', '', '', '')
        Assertion.verity(json.loads(rs)['code'], '10004')

    def test_h5_report_getUid(self):
        rs = XqwxAction.test_h5_report_getUid('', '')
        Assertion.verity(json.loads(rs)['code'], '10004')
