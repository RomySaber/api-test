#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-08-08 上午 10:21
@Author     : songchao
@File       : testXuexincrawler.py
@desc       : 学信网 接口自动化
"""

import json

from ai.testAction import XuexincrawlerAction
from ai.testSource import ai_config
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

name = ai_config.Xuexincrawler_name
password = ai_config.Xuexincrawler_password
school = ai_config.Xuexincrawler_schoolname
token = ai_config.Xuexincrawler_token
reqid = ai_config.Xuexincrawler_reqid
code = ai_config.Xuexincrawler_code


class testXuexincrawler(TestBaseCase):
    def test_001_api_xuexin_yes(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_正常登录
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token, code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 1)
            Assertion.verity(json.loads(rs1)['m'], '获取数据成功')
            Assertion.verity(json.loads(rs1)['data']['personInfo']['birthday'], '1992年02月02日')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'ID')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'birthday')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'certificateNO')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'college_branch')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'degreelevel')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'department')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'educationForm')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type2')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'enroDate')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'gender')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduateResult')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduate_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'headmaster_name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'is_graduated')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'leaving_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'nation')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'schooling_length')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'university')

    def test_002_api_xuexin_name_none(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_name为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name='', token=token, code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'name不能为空')

    def test_003_api_xuexin_password_none(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_password为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password='', name=name, token=token, code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'password不能为空')

    def test_004_api_xuexin_reqid_none(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_password为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token, code='', reqid='', xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')

    def test_005_api_xuexin_token_none(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_password为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(password=password, name=name, token='', code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'token不能为空')

    def test_006_api_xuexin_xx_none(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_password为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token, code='', reqid=reqid, xx='')
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'xx不能为空')

    def test_007_api_xuexin_token_error(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_token错误
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token + '1', code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], 'token错误')
            Assertion.verity(json.loads(rs1)['code'], 50001)

    def test_008_api_xuexin_password_error(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_password错误
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password + '1', name=name, token=token, code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], '您输入的用户名或密码有误。')
            Assertion.verity(json.loads(rs1)['reqId'], reqid)

    def test_009_api_xuexin_name_error(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_name错误
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name + '1', token=token, code='', reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], '您输入的用户名或密码有误。')
            Assertion.verity(json.loads(rs1)['reqId'], reqid)

    def test_010_api_xuexin_code_error(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_code错误
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name + '1', token=token, code=code, reqid=reqid, xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['m'], '您输入的用户名或密码有误。')
            Assertion.verity(json.loads(rs1)['reqId'], reqid)

    def test_011_api_xuexin_reqid_haizi(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_reqid汉字
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token, code='', reqid=reqid + '健康是福', xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid + '健康是福')
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 1)
            Assertion.verity(json.loads(rs1)['m'], '获取数据成功')
            Assertion.verity(json.loads(rs1)['data']['personInfo']['birthday'], '1992年02月02日')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'ID')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'birthday')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'certificateNO')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'college_branch')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'degreelevel')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'department')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'educationForm')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type2')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'enroDate')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'gender')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduateResult')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduate_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'headmaster_name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'is_graduated')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'leaving_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'nation')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'schooling_length')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'university')

    def test_012_api_xuexin_reqid_tebie(self):
        """
        Time       :2019-08-08
        author     : songchao
        desc       :登录提交接口_reqid特殊字符
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_login_submit(
            password=password, name=name, token=token, code='', reqid=reqid + '@#@￥%￥……&', xx=school)
        if json.loads(rs1)['m'] == '为保障您的账号安全，请输入图片验证码后重新登录':
            Assertion.verity(json.loads(rs1)['m'], '为保障您的账号安全，请输入图片验证码后重新登录')
            Assertion.verity(json.loads(rs1)['s'], 0)
            Assertion.verity(json.loads(rs1)['reqId'], reqid + '@#@￥%￥……&')
        elif json.loads(rs1)['m'] == '请重新刷新验证码，带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '请重新刷新验证码，带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        elif json.loads(rs1)['m'] == '图片验证码输入有误':
            Assertion.verity(json.loads(rs1)['m'], '图片验证码输入有误')
            Assertion.verity(json.loads(rs1)['s'], 0)
        elif json.loads(rs1)['m'] == '验证码已经失效，请重新刷新验证码带入新验证码登陆~':
            Assertion.verity(json.loads(rs1)['m'], '验证码已经失效，请重新刷新验证码带入新验证码登陆~')
            Assertion.verity(json.loads(rs1)['s'], 0)
        else:
            Assertion.verity(json.loads(rs1)['s'], 1)
            Assertion.verity(json.loads(rs1)['m'], '获取数据成功')
            Assertion.verity(json.loads(rs1)['data']['personInfo']['birthday'], '1992年02月02日')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'ID')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'birthday')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'certificateNO')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'college_branch')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'degreelevel')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'department')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'educationForm')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'education_type2')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'enroDate')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'gender')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduateResult')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'graduate_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'headmaster_name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'is_graduated')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'leaving_date')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'name')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'nation')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'schooling_length')
            Assertion.verityContain(json.loads(rs1)['data']['personInfo'], 'university')

    def test_013_api_xuexin_refresh_verify_code_yes(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_正常刷新
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid=reqid, token=token)
        Assertion.verityContain(json.loads(rs1)['data'], 'captcha')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['m'], '获取验证码成功')

    def test_014_api_xuexin_refresh_verify_code_reqid_none(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_reqid为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['s'], 0)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')

    def test_015_api_xuexin_refresh_verify_code_token_none(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_token为空
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['s'], 0)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')

    def test_016_api_xuexin_refresh_verify_code_token_ERROR(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_token错误
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['s'], 0)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')

    def test_017_api_xuexin_refresh_verify_code_reqId_hanzi(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_reqId为汉字
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid=reqid + '及卡机审的', token=token)
        Assertion.verityContain(json.loads(rs1)['data'], 'captcha')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['m'], '获取验证码成功')

    def test_018_api_xuexin_refresh_verify_code_reqId_teshu(self):
        """
        Time       :2019-08-09
        author     : songchao
        desc       :刷新学信登录的图片验证码接口_reqId为特殊字符
        """
        rs1 = XuexincrawlerAction.test_api_xuexin_refresh_verify_code(reqid=reqid + '@#%…………&', token=token)
        Assertion.verityContain(json.loads(rs1)['data'], 'captcha')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['m'], '获取验证码成功')
