#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-20 下午 3:35
@Author     : 罗林
@File       : testUnicomCrawler.py
@desc       :  联通爬虫 接口自动化
"""

import json
import unittest
from ai.test.decorator_mongo import update_mongo, close_pile
from ai.testSource import ai_config
from ai.testAction import UnicomcrawlerAction
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

reqid = ai_config.reqid
token = ai_config.UnicomCrawler_token
phone = ai_config.Crawleroperator_phone
passwd = ai_config.Crawleroperator_passwd
querys = {"project_name": "unicom"}
# 是否不打桩
pile = True


class testUnicomCrawler(TestBaseCase):
    @close_pile(querys)
    def test_001_api_unicom_phone_config(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '联通')

    def test_002_api_unicom_phone_config_phone_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token, phone=phone + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['reqId'], reqid)
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '联通')
        Assertion.verityContain(json.loads(rs1)['data']['loginForms'], '手机号格式不正确')

    def test_003_api_unicom_phone_config_phone_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token, phone='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'phone不能为空')

    def test_004_api_unicom_phone_config_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid + '1', token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '联通')
        Assertion.verityContain(json.loads(rs1)['data']['loginForms'], '手机号格式不正确')

    def test_005_api_unicom_phone_config_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid='', token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['authItem'], 'operator_pro')
        Assertion.verity(json.loads(rs1)['data']['authName'], '联通')
        Assertion.verityContain(json.loads(rs1)['data']['loginForms'], '手机号格式不正确')

    def test_006_api_unicom_phone_config_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token + '1', phone=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_007_api_unicom_phone_config_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商授权初始化配置接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token='', phone=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('每次都会发验证码')
    def test_008_api_unicom_refresh_sms_code(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '联通号码获取短信验证码出错。状态未知')

    @unittest.skip('每次都会发验证码')
    def test_009_api_unicom_refresh_sms_code_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_SUCCESS')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证码发送成功')

    @unittest.skipIf(pile, '忽略不打桩')
    def test_010_api_unicom_refresh_sms_code_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_011_api_unicom_refresh_sms_code_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    @unittest.skipIf(pile, '忽略不打桩')
    def test_012_api_unicom_refresh_sms_code_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    def test_013_api_unicom_refresh_verify_code(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    @unittest.skip('每次都会发验证码')
    def test_014_api_unicom_refresh_verify_code_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_IMAGE_SUCCESS')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')

    def test_015_api_unicom_refresh_verify_code_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_016_api_unicom_refresh_verify_code_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_017_api_unicom_refresh_verify_code_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :刷新运营商登录的图片验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不进行维护')
    def test_018_api_unicom_login_submit(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token, randompassword='123456', password=passwd, code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确')

    @unittest.skip('不进行维护')
    def test_019_api_unicom_login_submit_randompassword_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token, randompassword='', password=passwd, code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确')

    @unittest.skip('不进行维护')
    def test_020_api_unicom_login_submit_code_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token, randompassword='123456', password=passwd, code='', name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'PREPARE')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确')

    def test_021_api_unicom_login_submit_name_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token, randompassword='123456', password=passwd, code='123456', name='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'name不能为空')

    def test_022_api_unicom_login_submit_password_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token, randompassword='123456', password='', code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'password不能为空')

    def test_023_api_unicom_login_submit_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid='', token=token, randompassword='123456', password=passwd, code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_024_api_unicom_login_submit_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token=token + '1', randompassword='123456', password=passwd, code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_025_api_unicom_login_submit_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :账号密码登录提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(
            reqid=reqid, token='', randompassword='123456', password=passwd, code='123456', name=phone)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不进行维护')
    def test_026_api_unicom_refresh_smscode(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '刷新验证码失败')

    @unittest.skip('不进行维护')
    def test_027_api_unicom_refresh_smscode_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_FAILED')
        Assertion.verity(json.loads(rs1)['data']['stage'], 'LOGINED')
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '刷新验证码失败')

    def test_028_api_unicom_refresh_smscode_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_029_api_unicom_refresh_smscode_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_030_api_unicom_refresh_smscode_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取二次短信验证码接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('每次都会发验证码')
    def test_031_api_unicom_code_submit(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '失败')

    def test_032_api_unicom_code_submit_code_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'code不能为空')

    @unittest.skip('每次都会发验证码')
    def test_033_api_unicom_code_submit_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid + '1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '不存在该reqId')

    def test_034_api_unicom_code_submit_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_035_api_unicom_code_submit_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_036_api_unicom_code_submit_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :二次验证码提交接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('不进行维护')
    def test_037_api_unicom_get_status(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    def test_038_api_unicom_get_status_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '失败')

    def test_039_api_unicom_get_status_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_041_api_unicom_get_status_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_042_api_unicom_get_status_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商任务当前状态接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skip('接口需要放在登录之后，无法登陆成功')
    def test_043_api_unicom_get_result(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')

    @unittest.skip('接口需要放在登录之后，无法登陆成功')
    def test_044_api_unicom_get_result_reqid_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], '不存在该reqId')

    def test_045_api_unicom_get_result_reqid_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'reqId不能为空')

    def test_046_api_unicom_get_result_token_error(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['retCode'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token错误')

    def test_047_api_unicom_get_result_token_none(self):
        """
        Time       :2019-06-24
        author     : 罗林
        desc       :获取运营商采集数据接口
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 0)
        Assertion.verity(json.loads(rs1)['retMsg'], 'token不能为空')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='phone_config', remark='需要短信验证')
    def test_049_api_unicom_phone_config(self):
        """
        desc       :获取运营商授权初始化配置接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['needSecondAuth'], True)
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginTips'],
                         '请输入本人实名的在网手机号码和正确的密码登录，若登录多次总是失败，请明天再试或联系客服。')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldTips'], '手机号格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][2]['fieldTips'], '验证码格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['resetTips'],
                         '请编辑短信"2010"发送至"10086"找回密码!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='phone_config', remark='需要短信+图片验证')
    def test_050_api_unicom_phone_config(self):
        """
        desc       :获取运营商授权初始化配置接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_phone_config(reqid=reqid, token=token, phone=phone)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['needSecondAuth'], True)
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['loginTips'],
                         '请输入本人实名的在网手机号码和正确的密码登录，若登录多次总是失败，请明天再试或联系客服。')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][0]['fieldTips'], '手机号格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['fields'][2]['fieldTips'], '验证码格式不正确')
        Assertion.verity(json.loads(rs1)['data']['loginForms'][0]['pwdResetConfig']['resetTips'],
                         '请编辑短信"2010"发送至"10086"找回密码!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='验证码发送成功')
    def test_051_api_unicom_refresh_sms_code(self):
        """
        desc       :刷新运营商登录的短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证码发送成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='系统繁忙，请稍后再试')
    def test_052_api_unicom_refresh_sms_code(self):
        """
        desc       :刷新运营商登录的短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '系统繁忙，请稍后再试')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='发送次数已达上限，请明日再试!')
    def test_053_api_unicom_refresh_sms_code(self):
        """
        desc       :刷新运营商登录的短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '发送次数已达上限，请明日再试!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_sms_code', remark='联通号码获取短信验证码出错。状态未知')
    def test_054_api_unicom_refresh_sms_code(self):
        """
        desc       :刷新运营商登录的短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_sms_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '联通号码获取短信验证码出错。状态未知')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_code', remark='获取图片验证码成功')
    def test_055_api_unicom_refresh_verify_code(self):
        """
        desc       :刷新运营商登录的图片验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verityContain(json.loads(rs1)['data']['extra'], 'remark')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_verify_code', remark='获取图片验证码失败')
    def test_056_api_unicom_refresh_verify_code(self):
        """
        desc       :刷新运营商登录的图片验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_verify_code(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '获取图片验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='您填写的信息有误，请确认后重试！')
    def test_057_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '您填写的信息有误，请确认后重试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='图片验证码错误')
    def test_058_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '图片验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='登录成功')
    def test_059_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_SUCCESS')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='短信验证码不正确或已过期，请重新获取！')
    def test_060_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码不正确或已过期，请重新获取！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='账户名与密码不匹配，请重试！')
    def test_061_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '账户名与密码不匹配，请重试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='登录失败')
    def test_062_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_FAILED')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='登录成功')
    def test_063_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'LOGIN_SUCCESS')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='需要短信验证')
    def test_064_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'SMS_VERIFY_NEW')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='请输入查询详单所需的短信验证码')
    def test_065_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['tips'], '请输入查询详单所需的短信验证码')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='爬取成功')
    def test_066_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'SUCCESS')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_status', remark='正在爬取中')
    def test_067_api_unicom_get_status(self):
        """
        desc       :获取运营商任务当前状态接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_status(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'WATING')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='获取二次验证短信验证码成功')
    def test_068_api_unicom_refresh_smscode(self):
        """
        desc       :获取二次短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['phaseStatus'], 'REFRESH_SMS_SUCCESS')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='refresh_smscode', remark='刷新验证码失败')
    def test_069_api_unicom_refresh_smscode(self):
        """
        desc       :获取二次短信验证码接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_refresh_smscode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '刷新验证码失败')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='验证失败!')
    def test_070_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '验证失败!')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='请重新登录重试')
    def test_071_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '请重新登录重试')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码已失效，请重新获取')
    def test_072_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码已失效，请重新获取')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证码错误')
    def test_073_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证码错误')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='get_result', remark='获取数据成功')
    def test_074_api_unicom_get_result(self):
        """
        desc       :获取运营商采集数据接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_get_result(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['address'], '四川省成都市高新区中和镇心怡花园5栋')
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["base_fee"], "5.00")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["bill_end_date"], "2019-08-31")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["bill_month"], "2019-08")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["bill_start_date"], "2019-08-01")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["extra_fee"], "")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["extra_service_fee"], "")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["sms_fee"], "")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["total_fee"], "34.60")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["voice_fee"], "1.50")
        Assertion.verity(json.loads(rs1)['data']['bills'][0]["web_fee"], "28.10")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['bill_month'], "2019-09")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['total_size'], 10)
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]['details_id'], "50594")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["details_id"], "50594")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["dial_type"], "DAILED")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["duration"], 22)
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["fee"], "0.00")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["location"], "四川成都")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["location_type"], "国内通话")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["peer_number"], "13270000000")
        Assertion.verity(json.loads(rs1)['data']['calls'][0]['items'][0]["time"], "2019-09-21 17:40:41")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]['details_id'], "")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["fee"], "0.10")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["location"], "")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["msg_type"], "SMS")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["peer_number"], "13270000000")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["send_type"], "SEND")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["service_name"], "")
        Assertion.verity(json.loads(rs1)['data']['smses'][0]['items'][0]["time"], "2019-09-14-19:49:18")
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["bill_month"], "2019-07")
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["call_cnt"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["dial_cnt"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["dialed_cnt"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["call_time"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["dial_time"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["dialed_time"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["call_fees"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["sms_cnt"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["sms_fees"], 0.0)
        Assertion.verity(json.loads(rs1)['data']['orderResult']['etl_cell_behavior']["0"]["total_fee"], "93.63")
        Assertion.verity(json.loads(rs1)['data']["carrier"], "CHINA_UNICOM")
        Assertion.verity(json.loads(rs1)['data']["city"], "成都")
        Assertion.verity(json.loads(rs1)['data']["email"], "未绑定")
        Assertion.verity(json.loads(rs1)['data']["idcard"], "1327000000001011118")
        Assertion.verity(json.loads(rs1)['data']["level"], "二星用户")
        Assertion.verity(json.loads(rs1)['data']["mobile"], "13270000000")
        Assertion.verity(json.loads(rs1)['data']["name"], "哦大姐")
        Assertion.verity(json.loads(rs1)['data']["open_time"], "2018-07-02")

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='不支持弱密码或初始密码登录，请至运营商官网重置后再试！')
    def test_075_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '不支持弱密码或初始密码登录，请至运营商官网重置后再试！')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证成功-第一次验证')
    def test_076_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='code_submit', remark='短信验证成功-第二次验证')
    def test_077_api_unicom_code_submit(self):
        """
        desc       :二次验证码提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_code_submit(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '短信验证成功')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login_submit', remark='密码格式不正确，请确认后重试！')
    def test_078_api_unicom_login_submit(self):
        """
        desc       :账号密码登录提交接口
        author     : 闫红
        """
        rs1 = UnicomcrawlerAction.test_api_unicom_login_submit(reqid=reqid, token=token, code='123', name='123',
                                                               randompassword='123', password=passwd)
        Assertion.verity(json.loads(rs1)['retMsg'], '成功')
        Assertion.verity(json.loads(rs1)['retCode'], 1)
        Assertion.verity(json.loads(rs1)['data']['extra']['remark'], '密码格式不正确，请确认后重试！')
