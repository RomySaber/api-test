#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-10-30
@Author     : QA
@File       : testCenter_xqc.py
@desc       : 接口中心-小启科技小启查公众号接口测试用例
"""
import json

from common.myCommon.TestBaseCase import TestBaseCase
from center.testAction import Center_xqcAction as xqc


class testCenter_xqc(TestBaseCase):
    def test_001_user_login(self):
        xqc.test_user_login_1575(verifycode='', phone='')

    def test_002_user_changePhone(self):
        xqc.test_user_changePhone_1576(code='', newphone='')

    def test_003_common_validateCode(self):
        xqc.test_common_validateCode_1577(type='', phone='', code='')

    def test_004_user_info(self):
        xqc.test_user_info_1578(code='', ocode='')

    def test_005_common_getVerifyCode(self):
        xqc.test_common_getVerifyCode_1579(type='', phone='', code='')

    def test_006_h5_report_reportPrice(self):
        xqc.test_h5_report_reportPrice_1580()

    def test_007_common_report_list(self):
        xqc.test_common_report_list_1581(page='', size='', status='')

    def test_008_report_users(self):
        xqc.test_report_users_1582(page='', size='')

    def test_009_report_history(self):
        xqc.test_report_history_1583(page='', size='', types='')

    def test_010_report_push(self):
        xqc.test_report_push_1584(param='', remark='', type='', tid='')

    def test_011_report_detail(self):
        xqc.test_report_detail_1585(id='')

    def test_012_report_addUser(self):
        xqc.test_report_addUser_1586(phone='', remark='', idcard='', name='')

    def test_013_report_ai_phoneRefreshSms(self):
        xqc.test_report_ai_phoneRefreshSms_1587(reqid='', phone_type='', phone='')

    def test_014_report_ai_phoneConfig(self):
        xqc.test_report_ai_phoneConfig_1588(phone_type='', phone='')

    def test_015_report_ai_phoneType(self):
        xqc.test_report_ai_phoneType_1589(phone='')

    def test_016_report_ai_phoneGetResult(self):
        xqc.test_report_ai_phoneGetResult_1590(phone_type='', reqid='')

    def test_017_report_ai_phoneLogin(self):
        xqc.test_report_ai_phoneLogin_1591(piccode='', name='', reqid='', password='', phone_type='', randompassword='')

    def test_018_report_callback_report(self):
        xqc.test_report_callback_report_1592(signature='', taskid='', status='')

    def test_019_news_list(self):
        xqc.test_news_list_1593(currentpage='', pagesize='', type='')

    def test_020_common_getShareConf(self):
        xqc.test_common_getShareConf_1594(url='')

    def test_021_news_info(self):
        xqc.test_news_info_1595(articleinfouuid='')

    def test_022_report_business_tlogin(self):
        xqc.test_report_business_tlogin_1600(name='', password='')

    def test_023_report_business_tverifyqrcode(self):
        xqc.test_report_business_tverifyqrcode_1601(reqid='')

    def test_024_report_business_tverifycode(self):
        xqc.test_report_business_tverifycode_1602(reqid='', code='', type='')

    def test_025_report_business_tgetcode(self):
        xqc.test_report_business_tgetcode_1616(reqid='', type='')

    def test_026_report_list(self):
        xqc.test_report_list_1642(page='', size='', types='')

    def test_027_common_getVerifyCode(self):
        xqc.test_common_getVerifyCode_1643(code='', phone='', type='')

    def test_028_report_applyTd(self):
        xqc.test_report_applyTd_1644(idcard='', name='', verifycode='', phone='', type='')

    def test_029_report_applyTd(self):
        xqc.test_report_business_tverifycode_1687(code='', reqid='', type='', password='', name='')

    def test_030_report_ai_phoneType(self):
        xqc.test_h5_report_phoneType_1688(noauth='', phone='')

    def test_031_report_ai_phoneConfig(self):
        xqc.test_h5_report_phoneConfig_1689(noauth='', phone='', phone_type='')

    def test_032_report_list(self):
        xqc.test_h5_report_list_1690(noauth='', name='', page='', pagesize='')

    def test_033_report_list(self):
        xqc.test_h5_report_list_1693(max_xqc_id='')

    def test_034_payh5_payStatus(self):
        xqc.test_payh5_payStatus_1694(no='')

    def test_035_payh5_alipay_getParam(self):
        xqc.test_payh5_alipay_getParam_1695(id='', phone='')

    def test_036_payh5_wechat_getParam(self):
        xqc.test_payh5_wechat_getParam_1696(scene_info='', id='', phone='')

    def test_037_h5_report_history(self):
        xqc.test_h5_report_history_1698(idcard='', name='', phone='', type='', noauth='')

    def test_038_h5_report_login(self):
        xqc.test_h5_report_login_1699(
            idcard='', name='', phone='', type='', noauth='', password='',
            phone_type='', piccode='', randompassword='', reqid='')

    def test_039_h5_report_phoneRefreshPic(self):
        xqc.test_h5_report_phoneRefreshPic_1700(noauth='', phone_type='', reqid='')

    def test_040_h5_report_phoneRefreshSms(self):
        xqc.test_h5_report_phoneRefreshSms_1701(noauth='', phone='', phone_type='', reqid='')

    def test_041_h5_report_callback(self):
        xqc.test_h5_report_callback_1702(taskid='', status='')

    def test_042_h5_report_getStatus(self):
        xqc.test_h5_report_getStatus_1703(id='', noauth='')

