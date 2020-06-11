#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-26 下午 6:04
@Author     : 罗林
@File       : testDishonestExecutor.py
@desc       : 失信被执行人爬虫接口自动化测试 (已经停止维护)
"""

import json
import unittest

from faker import Faker

from ai.testAction import DishonestexecutorAction
from ai.testSource import ai_config
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

fake = Faker("zh_CN")
token = ai_config.token
name = ai_config.DishonestExecutor_name
cardnum = ai_config.DishonestExecutor_cardnu
name_two = ai_config.DishonestExecutor_name_two
cardnum_two = ai_config.DishonestExecutor_cardnu_two
person = fake.profile()
name_thr = person['name']
cardnum_thr = person['ssn']


class testDishonestExecutor(TestBaseCase):
    def test_001_api_execute_searchnocap(self):
        """
        desc       : 获取失信人数据
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum, name=name, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')

    def test_002_api_execute_searchnocap_two(self):
        """
        desc       : 获取失信人数据再次调用
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum_two, name=name_two, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')
            Assertion.verity(json.loads(rs1)['data']['data'][0]['age'], '44')
            Assertion.verity(json.loads(rs1)['data']['data'][0]['areaName'], '河北')
            Assertion.verity(json.loads(rs1)['data']['data'][0]['courtName'], '唐山市中级人民法院')
            Assertion.verity(json.loads(rs1)['data']['data'][0]['age'], '44')

    def test_003_api_execute_searchnocap_name_none(self):
        """
        desc       : 获取失信人数据name为空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum, name='', token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')

    def test_004_api_execute_searchnocap_17cardnum(self):
        """
        desc       : 获取失信人数据 17位数cardnum
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=fake.random_number(17), name='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 10200)
        Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')

    def test_005_api_execute_searchnocap_19cardnum(self):
        """
        desc       : 获取失信人数据 19位数cardnum
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=fake.random_number(19), name='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 10200)
        Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')

    def test_006_api_execute_searchnocap_cardnum_none(self):
        """
        desc       : 获取失信人数据 cardnum空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum='', name=name, token=token)
        Assertion.verity(json.loads(rs1)['code'], 10400)
        Assertion.verity(json.loads(rs1)['msg'], 'cardnum不能为空')

    def test_007_api_execute_searchnocap_token_error(self):
        """
        desc       : 获取失信人数据  token错误
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum, name=name, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 10501)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    def test_008_api_execute_searchnocap_token_none(self):
        """
        desc       : 获取失信人数据  token空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum, name=name, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 10501)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    def test_009_api_execute_searchnocap_thr(self):
        """
        desc       : 获取失信人数据再次调用
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_execute_searchnocap(cardnum=cardnum_thr, name=name_thr, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取失信人数据成功')

    @unittest.skip("接口已废弃")
    def test_010_api_court_searchnocap(self):
        """
        desc       : 获取被执行人数据
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum, name=name, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_011_api_court_searchnocap_two(self):
        """
        desc       : 获取被执行人数据 再次调取
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum_two, name=name_two, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_012_api_court_searchnocap_thr(self):
        """
        desc       : 获取被执行人数据 再次调取
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum_thr, name=name_thr, token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_013_api_court_searchnocap_name_none(self):
        """
        desc       : 获取被执行人数据 name为空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum, name='', token=token)
        if json.loads(rs1)['code'] == 10300:
            Assertion.verity(json.loads(rs1)['msg'], '验证码错误或验证码已过期，请重试！')
        elif json.loads(rs1)['code'] == 10200:
            Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_014_api_court_searchnocap_17cardnum(self):
        """
        desc       : 获取被执行人数据 17位数cardnum
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=fake.random_number(17), name='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 10200)
        Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_015_api_court_searchnocap_19cardnum(self):
        """
        desc       : 获取被执行人数据 19位数cardnum
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=fake.random_number(19), name='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 10200)
        Assertion.verity(json.loads(rs1)['msg'], '获取被执行人数据成功')

    @unittest.skip("接口已废弃")
    def test_016_api_court_searchnocap_cardnum_none(self):
        """
        desc       : 获取被执行人数据 cardnum空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum='', name=name, token=token)
        Assertion.verity(json.loads(rs1)['code'], 10400)
        Assertion.verity(json.loads(rs1)['msg'], 'cardnum不能为空')

    @unittest.skip("接口已废弃")
    def test_017_api_court_searchnocap_token_error(self):
        """
        desc       : 获取被执行人数据  token错误
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum, name=name, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 10501)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')

    @unittest.skip("接口已废弃")
    def test_018_api_court_searchnocap_token_none(self):
        """
        desc       : 获取被执行人数据  token空
        author     : 罗林
        """
        rs1 = DishonestexecutorAction.test_api_court_searchnocap(cardnum=cardnum, name=name, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 10501)
        Assertion.verity(json.loads(rs1)['msg'], 'token错误')
