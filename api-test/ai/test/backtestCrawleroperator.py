#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-19 上午 11:47
@Author     : 罗林
@File       : testCrawleroperator.py
@desc       : 运营商爬虫接口测试  (姜伟)
"""

import json
import unittest

from ai.testAction import CrawleroperatorAction
from ai.testSource import ai_config
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

phone = ai_config.Crawleroperator_phone
password = ai_config.Crawleroperator_passwd
reqid = ai_config.reqid
token = ai_config.token


class testCrawleroperator(TestBaseCase):
    def test_001_api_mobile_refresh_smscode(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')

    def test_002_api_mobile_refresh_smscode_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_smscode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_003_api_mobile_refresh_smscode_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_004_api_mobile_refresh_smscode_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_smscode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_005_api_mobile_phone_config(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['reqId'], reqid)
        # Assertion.verityNone(json.loads(rs1)['extra'])

    @unittest.expectedFailure
    def test_006_api_mobile_get_status(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'IMG_VERIFY_NEW')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verity(json.loads(rs1)['data']['extra']['tips'], '请输入查询详单所需的图片验证码')
        Assertion.verity(json.loads(rs1)['data']['extra']['title'], '图片验证码')
        Assertion.verityNotNone(json.loads(rs1)['data']['extra']['title']['remark'])

    @unittest.expectedFailure
    def test_007_api_mobile_get_status_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_status(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '不存在该reqId')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_008_api_mobile_get_status_reqid_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_status(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_009_api_mobile_get_status_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_status(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_010_api_mobile_get_status_token_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_status(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_011_api_mobile_phone_config_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_phone_config(reqid=reqid, token=token + '1', phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_012_api_mobile_phone_config_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_phone_config(reqid=reqid, token='', phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_013_api_mobile_phone_config_phone_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'phone不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_014_api_mobile_refresh_sms_code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        if json.loads(rs1)['data']['phaseStatus'] == 'REFRESH_SMS_SUCCESS':
            Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证码发送成功')
            Assertion.verity(json.loads(rs1)['data']['extra']['tips'], '请输入你收到的移动验证码')
            Assertion.verity(json.loads(rs1)['data']['extra']['title'], '短信验证码')
        elif json.loads(rs1)['data']['phaseStatus'] == 'REFRESH_SMS_FAILED':
            Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '对不起，短信随机码获取达到上限！')

    def test_015_api_mobile_refresh_sms_code_two(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_016_api_mobile_refresh_sms_code_thr(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '对不起，短信随机码获取达到上限！')

    def test_017_api_mobile_refresh_sms_code_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_018_api_mobile_refresh_sms_code_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_019_api_mobile_refresh_sms_code_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_020_api_mobile_refresh_sms_code_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_sms_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_021_api_mobile_login_submit(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, name=phone, password=password, code='', randompassword='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_022_api_mobile_login_submit_reqid_not_exits(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid + '1', token=token, name=phone, password='123456', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_023_api_mobile_login_submit_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid='', token=token, name=phone, password='123456', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_024_api_mobile_login_submit_reqid_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token + '1', name=phone, password='123456', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_025_api_mobile_login_submit_reqid_token_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token='', name=phone, password='123456', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_026_api_mobile_login_submit_reqid_randompassword_timeout(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, name=phone, password='123456', code='', randompassword='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取')

    def test_027_api_mobile_login_submit_reqid_randompassword_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token + '1', name=phone, password='123456', code='', randompassword='123')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_028_api_mobile_login_submit_reqid_randompassword_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, name=phone, password='123456', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取')

    def test_029_api_mobile_login_submit_reqid_password_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token + '1', name=phone, password='', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'password不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_030_api_mobile_login_submit_reqid_name_None(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_login_submit(
            reqid=reqid, token=token + '1', name='', password='123', code='', randompassword='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'name不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    @unittest.skip('接口需要放在登录之后，无法登陆成功')
    def test_031_api_mobile_get_result(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口 (放在登录之后)
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_result(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 1)

    @unittest.skip('接口需要放在登录之后，无法登陆成功')
    def test_032_api_mobile_get_result_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口 (放在登录之后)
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_result(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '不存在该reqId')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_033_api_mobile_get_result_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口 (放在登录之后)
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_result(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_034_api_mobile_get_result_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口 (放在登录之后)
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_result(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_035_api_mobile_get_result_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口 (放在登录之后)
        """
        rs1 = CrawleroperatorAction.test_api_mobile_get_result(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    def test_036_api_mobile_refresh_smscode_two(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verityContain(json.loads(rs1)['data']['extra'], 'session信息为空，请先登录!')

    def test_037_api_mobile_refresh_verify_code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        CrawleroperatorAction.test_api_mobile_refresh_verify_code(reqid=reqid, token=token)

    def test_038_api_mobile_refresh_verify_code_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_039_api_mobile_refresh_verify_code_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_040_api_mobile_refresh_verify_code_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_code(reqid=reqid, token='123')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_041_api_mobile_refresh_verify_pic(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次图片验证
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'IMG_VERIFY_NEW')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verityContain(json.loads(rs1)['data']['extra'], '图片验证码')
        Assertion.verityContain(json.loads(rs1)['data']['extra'], '请输入查询详单所需的图片验证码')
        Assertion.verityNotNone(json.loads(rs1)['data']['extra'])

    def test_042_api_mobile_refresh_verify_pic_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次图片验证
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_pic(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_043_api_mobile_refresh_verify_pic_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次图片验证
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_044_api_mobile_refresh_verify_pic_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次图片验证
        """
        rs1 = CrawleroperatorAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_045_api_mobile_code_submit_code_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_code_submit(reqid=reqid, code='123', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'IMG_VERIFY_NEW')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        # Assertion.verityNone(json.loads(rs1)['data']['extra'])

    def test_046_api_mobile_code_submit_code_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_code_submit(reqid=reqid, code='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'code不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_047_api_mobile_code_submit_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_code_submit(reqid='', code='123', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_048_api_mobile_code_submit_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_code_submit(reqid=reqid, code='123', token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_049_api_mobile_code_submit_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = CrawleroperatorAction.test_api_mobile_code_submit(reqid=reqid, code='123', token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])
