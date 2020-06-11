#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-19 上午 10:45
@Author     : 罗林
@File       : testTelecomCrawler.py
@desc       : 电信爬虫 接口自动化
"""


import json
import unittest
from ai.test.decorator_mongo import update_mongo, close_pile
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ai.testAction import TelecomcrawlerAction
from ai.testSource import ai_config


querys = {"project_name": "telecom"}
phone = ai_config.TelecomCrawler_phone
password = ai_config.TelecomCrawler_password
reqid = ai_config.reqid
token = ai_config.token
# 是否不打桩
pile = True


class testTelecomCrawler(TestBaseCase):
    @close_pile(querys)
    def test_001_api_telecom_login_submit(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_login_submit(
            password=password, reqid=reqid, token=token, name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_002_api_telecom_get_status(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_get_status(
            reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    @unittest.skip('每次都会发验证码')
    def test_003_api_telecom_refresh_sms_code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], None)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_SUCCESS')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    @unittest.skip('每次都会发验证码')
    def test_004_api_telecom_refresh_sms_code_two(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu='')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], None)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    @unittest.skip('每次都会发验证码')
    def test_005_api_telecom_code_submit(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, code='668995',
            sfzname='徐斌', idcard='513701199406091618', password=password, tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verityContain(json.loads(rs1)['retMsg'], '登陆已失效请重新登录')
        Assertion.verityNone(json.loads(rs1)['data'])
        # Assertion.verity(json.loads(rs1)['retCode'], 1)
        # Assertion.verityContain(json.loads(rs1)['retMsg'], '成功')
        # Assertion.verity(json.loads(rs1)['data']['extra']['remark'], None)
        # Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'SMS_VERIFY_NEW')
        # Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        # Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_006_api_telecom_get_result(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_get_result(
            reqid=reqid, token=token, name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '数据为空请检查当前手机号是否授权成功！')
        Assertion.verityNone(json.loads(rs1)['data'])

    @unittest.skip('每次都会发验证码')
    def test_007_api_telecom_login_submit_passwd_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_login_submit(
            password='941425', reqid=reqid, token=token, name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verityContain(json.loads(rs1)['data']['extra']['remark'], '账号或密码错误哦')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_008_api_telecom_login_submit_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_login_submit(
            password=password, reqid=reqid, token='', name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_009_api_telecom_login_submit_name_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_login_submit(
            password=password, reqid=reqid, token=token, name='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'name不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_010_api_telecom_login_submit_passwd_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_login_submit(
            password='', reqid=reqid, token=token, name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'password不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_011_api_telecom_refresh_sms_code_name_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name='1816666113', tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '登录失效或者请使用第一次登陆返回的reqId重试~')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_012_api_telecom_refresh_sms_code_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token='', name=phone, tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_013_api_telecom_refresh_sms_code_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid='18750fa83bcc11e98811a81e844f9fc2', token='cdddef32b7ec4be9926d30f545e76c371', name=phone, tu='')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_014_api_telecom_refresh_sms_code_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid='', token='cdddef32b7ec4be9926d30f545e76c371', name=phone, tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_015_api_telecom_refresh_sms_code_name_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid='12343', token='cdddef32b7ec4be9926d30f545e76c371', name='', tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'name不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_016_api_telecom_code_submit_all_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid='', token='', name='', code='', sfzname='', idcard='', password='', tu='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_017_api_telecom_code_submit_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid='18750fa83bcc11e98811a81e844f9fc2', token='cdddef32b7ec4be9926d30f545e76c371',
            name=phone, code='441133', sfzname='李超1', idcard='513701199406091618', password=password, tu='')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_018_api_telecom_code_submit_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid='18752', token='cdddef32b7ec4be9926d30f545e76c371',
            name=phone, code='441133', sfzname='李超1', idcard='513701199406091618', password=password, tu='')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_019_api_telecom_get_result_all_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_get_result(reqid='', token='', name='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_020_api_telecom_get_result_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_get_result(
            reqid='18750fa83bcc11e98811a81e844f9fc2', token='cdddef32b7ec4be9926d30f5451e76c37', name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    def test_021_api_telecom_get_status_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = TelecomcrawlerAction.test_api_telecom_get_status(
            reqid='18750fa83bcc11e98811a81e844f9fc2', token='cdddef32b7ec4be9926d30f5451e76c37')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')
        Assertion.verityNone(json.loads(rs1)['data'])

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='验证码发送成功')
    def test_022_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_SUCCESS')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '验证码发送成功')
        Assertion.verity(rs['data']['extra']['tips'], '请输入你收到的电信验证码')
        Assertion.verity(rs['data']['extra']['title'], '短信验证码')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='系统繁忙，请稍后再试')
    def test_023_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '系统繁忙，请稍后再试')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='发送次数已达上限，请明日再试!')
    def test_024_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '发送次数已达上限，请明日再试!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='电信号码获取短信验证码出错。状态未知')
    def test_025_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '电信号码获取短信验证码出错。状态未知')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='获取二次验证短信验证码成功')
    def test_026_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_SUCCESS')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='刷新验证码失败')
    def test_027_refresh_sms_code(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取二次短信验证码接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_refresh_sms_code(
            reqid=reqid, token=token, name=phone, tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '刷新验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='您填写的信息有误，请确认后重试！')
    def test_028_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '您填写的信息有误，请确认后重试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='恭喜您登录成功~')
    def test_029_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_SUCCESS')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra'], {})

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='短信验证码不正确或已过期，请重新获取！')
    def test_030_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='账户名与密码不匹配，请重试！')
    def test_031_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '账户名与密码不匹配，请重试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='不支持弱密码或初始密码登录，请至运营商官网重置后再试！')
    def test_032_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '不支持弱密码或初始密码登录，请至运营商官网重置后再试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='密码格式不正确，请确认后重试！')
    def test_033_login_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 账号密码登录提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_login_submit(
            reqid=reqid, token=token, name=phone, password=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(rs['data']['stage'], 'PREPARE')
        Assertion.verity(rs['data']['extra']['remark'], '密码格式不正确，请确认后重试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='验证失败!')
    def test_034_code_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, password='', code='', idcard='', sfzname='', tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'SMS_VERIFY_NEW')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '验证失败!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='成功!')
    def test_035_code_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, password='', code='', idcard='', sfzname='', tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'WAITING')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '成功!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码已失效，请重新获取')
    def test_036_code_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, password='', code='', idcard='', sfzname='', tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'SMS_VERIFY_NEW')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '短信验证码已失效，请重新获取')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码错误')
    def test_037_code_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, password='', code='', idcard='', sfzname='', tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'SMS_VERIFY_NEW')
        Assertion.verity(rs['data']['stage'], 'WAITING')
        Assertion.verity(rs['data']['extra']['remark'], '短信验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证成功')
    def test_038_code_submit(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 二次验证码提交接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_code_submit(
            reqid=reqid, token=token, name=phone, password='', code='', idcard='', sfzname='', tu=''))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'reqId')
        Assertion.verityContain(rs['data'], 'timestamp')
        Assertion.verity(rs['data']['phaseStatus'], 'WAITING')
        Assertion.verity(rs['data']['stage'], 'LOGINED')
        Assertion.verity(rs['data']['extra']['remark'], '短信验证成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_result', remark='获取数据成功')
    def test_039_get_result(self):
        """
        Time       : 2019-11-14
        author     : 罗林
        desc       : 获取运营商采集数据接口
        """
        rs = json.loads(TelecomcrawlerAction.test_api_telecom_get_result(reqid=reqid, token=token, name=phone))
        Assertion.verity(rs['retCode'], 1)
        Assertion.verity(rs['retMsg'], '成功')
        Assertion.verityContain(rs['data'], 'address')
        Assertion.verityContain(rs['data'], 'available_balance')
        Assertion.verityContain(rs['data'], 'state')
        Assertion.verityContain(rs['data'], 'province')
        Assertion.verityContain(rs['data'], 'package_name')
        Assertion.verityContain(rs['data'], 'open_time')
        Assertion.verityContain(rs['data'], 'name')
        Assertion.verityContain(rs['data'], 'mobile')
        Assertion.verityContain(rs['data'], 'level')
        Assertion.verityContain(rs['data'], 'idcard')
        Assertion.verityContain(rs['data'], 'email')
        Assertion.verityContain(rs['data'], 'city')
        Assertion.verityContain(rs['data'], 'carrier')
        Assertion.verityContain(rs['data'], 'bills')
        Assertion.verityContain(rs['data'], 'calls')
        Assertion.verityContain(rs['data'], 'smses')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_basicinfo')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_friend_circle')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_active_degree')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_cell_behavior')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_consumption_detail')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_contact_region')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_call_contact_detail')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_call_duration_detail')
        Assertion.verityContain(rs['data']['orderResult'], 'etl_behavior_check')
