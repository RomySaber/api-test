#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-24 下午 5:11
@Author     : 罗林
@File       : testMobileCrawler.py
@desc       : 移动爬虫 接口测试用例
"""

import json
import unittest

from ai.test.decorator_mongo import update_mongo, close_pile
from ai.testAction import MobilecrawlerAction
from ai.testSource import ai_config
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

reqid = ai_config.reqid
token = ai_config.token
phone = ai_config.MobileCrawler_phone
passwd = ai_config.MobileCrawler_password
querys = {"project_name": "mobile"}
# 是否不打桩
pile = True


class testMobileCrawler(TestBaseCase):
    @close_pile(querys)
    def test_001_api_mobile_phone_config(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    def test_002_api_mobile_phone_config_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid='', token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    def test_003_api_mobile_phone_config_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid='', token=token + '1', phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_004_api_mobile_phone_config_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid='', token='', phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    def test_005_api_mobile_phone_config_phone_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid='', token=token, phone='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'phone不能为空')

    @unittest.skip('每次都会发验证码')
    def test_006_api_mobile_refresh_sms_code(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    def test_007_api_mobile_refresh_sms_code_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_008_api_mobile_refresh_sms_code_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_009_api_mobile_refresh_sms_code_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_010_api_mobile_refresh_sms_code_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('')
    def test_011_api_mobile_login_submit(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token, password=passwd, code='123456',
                                                               name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        # Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取')

    def test_012_api_mobile_login_submit_code_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token, password=passwd, code='',
                                                               name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        # Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取')

    def test_013_api_mobile_login_submit_randompassword_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token, password=passwd, code='123456',
                                                               name=phone, randompassword='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        # Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取')

    def test_014_api_mobile_login_submit_name_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token, password=passwd, code='123456',
                                                               name='', randompassword='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'name不能为空')

    def test_015_api_mobile_login_submit_password_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token, password='', code='123456',
                                                               name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'password不能为空')

    def test_016_api_mobile_login_submit_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid='', token=token, password=passwd, code='123456',
                                                               name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_017_api_mobile_login_submit_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid='1', token=token, password=passwd, code='123456',
                                                               name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_018_api_mobile_login_submit_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token=token + '1', password=passwd,
                                                               code='123456', name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_019_api_mobile_login_submit_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(reqid=reqid, token='', password=passwd,
                                                               code='123456', name=phone, randompassword='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不维护')
    def test_020_api_mobile_get_status(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    @unittest.skip('不维护')
    def test_021_api_mobile_get_status_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WAITING')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    @unittest.skip('不维护')
    def test_022_api_mobile_get_status_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], 'session信息为空，请先登录!')

    @unittest.skip('不维护')
    def test_023_api_mobile_get_status_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    @unittest.skip('不维护')
    def test_024_api_mobile_get_status_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不维护')
    def test_025_api_mobile_code_submit(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'SMS_VERIFY_NEW')
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '系统错误!')

    @unittest.skip('不维护')
    def test_026_api_mobile_code_submit_code_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'code不能为空')

    @unittest.skip('不维护')
    def test_027_api_mobile_code_submit_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid + '1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WAITING')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    @unittest.skip('不维护')
    def test_028_api_mobile_code_submit_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    @unittest.skip('不维护')
    def test_029_api_mobile_code_submit_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    @unittest.skip('不维护')
    def test_030_api_mobile_code_submit_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不维护')
    def test_031_api_mobile_refresh_verify_pic(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    @unittest.skip('不维护')
    def test_032_api_mobile_refresh_verify_pic_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WAITING')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_033_api_mobile_refresh_verify_pic_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_034_api_mobile_refresh_verify_pic_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_035_api_mobile_refresh_verify_pic_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不维护')
    def test_036_api_mobile_refresh_smscode(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    @unittest.skip('不维护')
    def test_037_api_mobile_refresh_smscode_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WAITING')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_038_api_mobile_refresh_smscode_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_039_api_mobile_refresh_smscode_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_040_api_mobile_refresh_smscode_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    def test_041_api_mobile_get_result(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不维护')
    def test_042_api_mobile_get_result_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WAITING')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不存在该reqId')

    def test_043_api_mobile_get_result_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_044_api_mobile_get_result_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_045_api_mobile_get_result_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='token错误')
    def test_046_msg_code_submit_token_error(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token='123', code='123')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='系统繁忙，验证短信验证码失败')
    def test_047_msg_code_submit_error(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 703)
        Assertion.verity(json.loads(rs1)['msg'], '系统繁忙，验证短信验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='转发移动的其它提示信息')
    def test_048_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 702)
        Assertion.verity(json.loads(rs1)['msg'], '转发移动的其它提示信息')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='验证码输入错误')
    def test_049_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 701)
        Assertion.verity(json.loads(rs1)['msg'], '验证码输入错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='登陆状态已失效')
    def test_050_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 600)
        Assertion.verity(json.loads(rs1)['msg'], '登陆状态已失效')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='验证通过')
    def test_051_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['msg'], '验证通过')

    @unittest.skip('去掉了打桩数据，不维护')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='获取验证码失败')
    def test_052_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 900)
        Assertion.verity(json.loads(rs1)['msg'], '获取验证码失败')

    @unittest.skip('去掉了打桩数据，不维护')
    @update_mongo(querys=querys, api_name='msg_code_submit', remark='未成功时，转发的移动提示信息')
    def test_053_msg_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次短信验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_msg_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 800)
        Assertion.verity(json.loads(rs1)['msg'], '验证码格式不对...')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='token错误')
    def test_054_mobile_refresh_smscode(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='登录状态已失效')
    def test_055_mobile_refresh_smscode(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 600)
        Assertion.verity(json.loads(rs1)['msg'], '登录状态已失效')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='短信验证码发送成功')
    def test_056_mobile_refresh_smscode(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['msg'], '短信验证码发送成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='获取验证码失败')
    def test_057_mobile_refresh_smscode(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 900)
        Assertion.verity(json.loads(rs1)['msg'], '获取验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='pic_code_submit', remark='token错误')
    def test_058_pic_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次图片验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_pic_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='pic_code_submit', remark='系统繁忙，图片验证出错')
    def test_059_pic_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次图片验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_pic_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 602)
        Assertion.verity(json.loads(rs1)['msg'], '系统繁忙，图片验证出错')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='pic_code_submit', remark='图片验证码错误')
    def test_060_pic_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次图片验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_pic_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 601)
        Assertion.verity(json.loads(rs1)['msg'], '图片验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='pic_code_submit', remark='登录状态已失效')
    def test_061_pic_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次图片验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_pic_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 600)
        Assertion.verity(json.loads(rs1)['msg'], '登录状态已失效')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='pic_code_submit', remark='图片验证成功')
    def test_062_pic_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 验证二次图片验证码
        """
        rs1 = MobilecrawlerAction.test_api_mobile_pic_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['msg'], '图片验证成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_pic', remark='获取验证码失败')
    def test_063_refresh_verify_pic(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 900)
        Assertion.verity(json.loads(rs1)['msg'], '获取验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_pic', remark='token错误')
    def test_064_refresh_verify_pic(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_pic', remark='登录状态已失效')
    def test_065_refresh_verify_pic(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 600)
        Assertion.verity(json.loads(rs1)['msg'], '登录状态已失效')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_pic', remark='获取图片验证码成功')
    def test_066_refresh_verify_pic(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取二次图片验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_verify_pic(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['msg'], '获取图片验证码成功')
        Assertion.verityContain(json.loads(rs1), 'pic')

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码错误')
    def test_067_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "SMS_VERIFY_NEW")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'FINISHED')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码错误')

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码已失效，请重新获取')
    def test_068_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'FINISHED')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码已失效，请重新获取')

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='code_submit', remark='请重新登录重试')
    def test_069_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'FINISHED')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '请重新登录重试')

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='get_status', remark='系统错误！')
    def test_070_get_status(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '系统错误！')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "WAITING")
        Assertion.verityNone(json.loads(rs1)['data']['stage'])
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verityNone(json.loads(rs1)['data']['extra']['remark'])
        Assertion.verityNone(json.loads(rs1)['data']['extra']['title'])
        Assertion.verityNone(json.loads(rs1)['data']['extra']['tips'])
        Assertion.verityNone(json.loads(rs1)['data']['extra']['interactiveOver'])

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='验证码错误')
    def test_071_login_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, code='123', name='123', password='123', randompassword='123')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "LOGIN_FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='尝试次数过多，请次日重试')
    def test_072_login_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, code='123', name='123', password='123', randompassword='123')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "LOGIN_FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '尝试次数过多，请次日重试')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='图片验证码错误')
    def test_073_login_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, code='123', name='123', password='123', randompassword='123')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "LOGIN_FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '图片验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='短信验证码不正确')
    def test_074_login_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, code='123', name='123', password='123', randompassword='123')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "LOGIN_FAILED")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='系统错误！')
    def test_075_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '系统错误！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='移动号码获取短信验证码失败，未知错误。')
    def test_076_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '移动号码获取短信验证码失败，未知错误。')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='移动号码获取短信验证码错误！')
    def test_077_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '移动号码获取短信验证码错误！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='短信发送次数过于频繁！')
    def test_078_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '对不起，短信发送次数过于频繁！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='短信随机码获取达到上限！')
    def test_079_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '对不起，短信随机码获取达到上限！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='短信随机码暂时不能发送，请一分钟以后再试')
    def test_080_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '对不起，短信随机码暂时不能发送，请一分钟以后再试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='phone_config', remark='获取短信验证失败')
    def test_081_phone_config(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '系统错误，请重试！')
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '移动')
        Assertion.verity(json.loads(rs1)['data']['lastUpdatedAt'], '')
        Assertion.verityTrue(json.loads(rs1)['data']['needSecondAuth'])
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['formName'], '账号授权')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['status'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginFormType'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginTips'],
                         '请输入本人实名的在网手机号码和正确的密码登录，若登录多次总是失败，请明天再试或联系客服。')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['passResetType'], 'SMS')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsTemplate'], '2010')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsReceiver'], '10086')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['resetTips'],
                         '请编辑短信\"2010\"发送至\"10086\"找回密码!')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['field'], 'username')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldName'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldDesc'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['checkRegex'], '^\\d{11}$')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldTips'], '手机号格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['field'], 'password')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldName'], '服务密码')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldDesc'], '服务密码')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='phone_config', remark='不需要短信验证')
    def test_082_phone_config(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '移动')
        Assertion.verity(json.loads(rs1)['data']['lastUpdatedAt'], '')
        Assertion.verityTrue(json.loads(rs1)['data']['needSecondAuth'])
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['formName'], '账号授权')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['status'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginFormType'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginTips'],
                         '请输入本人实名的在网手机号码和正确的密码登录，若登录多次总是失败，请明天再试或联系客服。')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['passResetType'], 'SMS')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsTemplate'], '2010')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsReceiver'], '10086')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['resetTips'],
                         '请编辑短信\"2010\"发送至\"10086\"找回密码!')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['field'], 'username')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldName'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldDesc'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['checkRegex'], '^\\d{11}$')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldTips'], '手机号格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['field'], 'password')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldName'], '服务密码')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldDesc'], '服务密码')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_result', remark='获取数据成功')
    def test_083_get_result(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_result(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['mobile'], '18280325059')
        Assertion.verity(json.loads(rs1)['data']['name'], 'xx洪')
        Assertion.verity(json.loads(rs1)['data']['carrier'], 'CHINA_MOBILE')
        Assertion.verityContain(json.loads(rs1)['data'], "mobile")
        Assertion.verityContain(json.loads(rs1)['data'], "name")
        Assertion.verityContain(json.loads(rs1)['data'], "carrier")
        Assertion.verityContain(json.loads(rs1)['data'], "province")
        Assertion.verityContain(json.loads(rs1)['data'], "city")
        Assertion.verityContain(json.loads(rs1)['data'], "level")
        Assertion.verityContain(json.loads(rs1)['data'], "idcard")
        Assertion.verityContain(json.loads(rs1)['data'], "open_time")
        Assertion.verityContain(json.loads(rs1)['data'], "package_name")
        Assertion.verityContain(json.loads(rs1)['data'], "available_balance")
        Assertion.verityContain(json.loads(rs1)['data'], "state")
        Assertion.verityContain(json.loads(rs1)['data'], "email")
        Assertion.verityContain(json.loads(rs1)['data'], "address")
        Assertion.verityContain(json.loads(rs1)['data'], "bills")

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证成功')
    def test_084_code_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "WAITING")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '')

    @unittest.skip('接口不维护')
    @update_mongo(querys=querys, api_name='get_status', remark='需要图片验证码')
    def test_085_get_status(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商任务当前状态接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "IMG_VERIFY_NEW")
        Assertion.verityNone(json.loads(rs1)['data']['stage'])
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verityNone(json.loads(rs1)['data']['extra']['remark'])
        Assertion.verityNone(json.loads(rs1)['data']['extra']['title'])
        Assertion.verityNone(json.loads(rs1)['data']['extra']['tips'])

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='登陆成功')
    def test_086_login_submit(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_login_submit(
            reqid=reqid, token=token, code='123', name='123', password='123', randompassword='123')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "LOGIN_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verityContain(json.loads(rs1)['data']['extra'], 'remark')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='验证码发送成功')
    def test_087_refresh_sms_code(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 刷新运营商登录的短信验证码接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], "REFRESH_SMS_SUCCESS")
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verityContain(json.loads(rs1)['data'], 'reqId')
        Assertion.verityContain(json.loads(rs1)['data'], 'timestamp')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证码发送成功')
        Assertion.verity(json.loads(rs1)['data']['extra']['title'], '短信验证码')
        Assertion.verity(json.loads(rs1)['data']['extra']['tips'], '请输入你收到的移动验证码')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='phone_config', remark='需要短信验证')
    def test_088_phone_config(self):
        """
        Time       : 2019-11-13
        author     : 罗林
        desc       : 获取运营商授权初始化配置接口
        """
        rs1 = MobilecrawlerAction.test_api_mobile_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '移动')
        Assertion.verity(json.loads(rs1)['data']['lastUpdatedAt'], '')
        Assertion.verityTrue(json.loads(rs1)['data']['needSecondAuth'])
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['formName'], '账号授权')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['status'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginFormType'], 'NORMAL')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginTips'],
                         '请输入本人实名的在网手机号码和正确的密码登录，若登录多次总是失败，请明天再试或联系客服。')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['passResetType'], 'SMS')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsTemplate'], '2010')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['smsReceiver'], '10086')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['resetTips'],
                         '请编辑短信\"2010\"发送至\"10086\"找回密码!')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['field'], 'username')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldName'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldDesc'], '手机号')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['checkRegex'], '^\\d{11}$')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldTips'], '手机号格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['field'], 'password')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldName'], '服务密码')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][1]['fieldDesc'], '服务密码')
