#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-19 下午 4:54
@Author     : 罗林
@File       : testTb.py
@desc       : 淘宝爬虫  接口自动化 （田璐玲）
"""

import json
import unittest

from ai.test.decorator_mongo import update_mongo, close_pile
from ai.testAction import TbAction
from ai.testSource import ai_config
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

reqid = ai_config.reqid
token = ai_config.token
name = ai_config.Tb_name
password = ai_config.Tb_password
querys = {"project_name": "taobao"}
# 是否不打桩
pile = True


class testTb(TestBaseCase):
    @unittest.skipIf(pile, '忽略不打桩')
    @close_pile(querys)
    @update_mongo(querys=querys, api_name='getcode', remark='短信验证码已发送')
    def test_002_api_taobao_getcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码已发送')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='系统错误')
    def test_003_api_taobao_500getcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='验证码操作太频繁')
    def test_004_api_taobao_301getcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '获取验证码操作太频繁，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='获取次数已达上限')
    def test_005_api_taobao_302getcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '获取次数已达上限，请15分钟后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='短信验证码发送失败')
    def test_006_api_taobao_300getcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码发送失败')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_007_api_taobao_getcode_reqid_error(self):
        """
        desc       :获取短信验证码， reqId 错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_008_api_taobao_getcode_reqid_none(self):
        """
        desc       :获取短信验证码 ，reqId 为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_009_api_taobao_getcode_token_error(self):
        """
        desc       :获取短信验证码 ， token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_010_api_taobao_getcode_token_none(self):
        """
        desc       :获取短信验证码, token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='系统错误')
    def test_011_api_taobao_500verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='暂未授权')
    def test_012_api_taobao_300verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '暂未授权')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='二维码已失效')
    def test_013_api_taobao_301verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '二维码已失效')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='已扫描成功')
    def test_014_api_taobao_303verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 303)
        Assertion.verity(json.loads(rs1)['m'], '已扫描成功，登录中...')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='已扫描登录')
    def test_015_api_taobao_201verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 201)
        Assertion.verity(json.loads(rs1)['m'], '已扫描登录')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='授权成功')
    def test_016_api_taobao_200verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='需要短信验证')
    def test_017_api_taobao_302verifyqrcode(self):
        """
        desc       :验证二维码是否已扫描，并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '需要短信验证')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_018_api_taobao_verifyqrcode_reqid_error(self):
        """
        desc       :验证二维码是否已扫描，并获取信息 ，reqId错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_019_api_taobao_verifyqrcode_reqid_none(self):
        """
        desc       :验证二维码是否已扫描，并获取信息 ，reqId为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_020_api_taobao_verifyqrcode_token_error(self):
        """
        desc       :验证二维码是否已扫描，并获取信息 ，token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_021_api_taobao_verifyqrcode_token_none(self):
        """
        desc       :验证二维码是否已扫描，并获取信息  ,token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifyqrcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_022_api_taobao_qrverifycode_code_none(self):
        """
        desc       :校验短信验证码， code为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'code不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_023_api_taobao_qrverifycode_code_time_out(self):
        """
        desc       :校验短信验证码 ，code超时
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['s'], 0)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')

    @unittest.skipIf(pile, '忽略不打桩')
    def test_024_api_taobao_qrverifycode_reqid_error(self):
        """
        desc       :校验短信验证码 ，reqId错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid + '1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_025_api_taobao_qrverifycode_reqid_none(self):
        """
        desc       :校验短信验证码 ，reqId为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_026_api_taobao_qrverifycode_token_error(self):
        """
        desc       :校验短信验证码 ，token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_027_api_taobao_qrverifycode_token_none(self):
        """
        desc       :校验短信验证码 ， token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='系统错误')
    def test_028_api_taobao_500qrverifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='短信验证码错误')
    def test_029_api_taobao_300qrverifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='授权成功')
    def test_030_api_taobao_200qrverifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrverifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['data']['reqId'], '123')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='系统错误')
    def test_031_api_taobao_500qrgetcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='短信验证码已发送')
    def test_032_api_taobao_200qrgetcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码已发送')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='短信验证码发送失败')
    def test_033_api_taobao_300qrgetcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码发送失败')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='发送短信验证码出错')
    def test_034_api_taobao_304qrgetcode(self):
        """
        desc       :获取短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 304)
        Assertion.verity(json.loads(rs1)['m'], '发送短信验证码出错！')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_035_api_taobao_304qrgetcode_reqid_none(self):
        """
        desc       :获取短信验证码 , reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_036_api_taobao_qrgetcode_reqid_error(self):
        """
        desc       :获取短信验证码 , reqid错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid='123', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_037_api_taobao_qrgetcode_token_error(self):
        """
        desc       :获取短信验证码 , token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_038_api_taobao_qrgetcode_token_none(self):
        """
        desc       :获取短信验证码 , token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_qrgetcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='需要短信验证')
    def test_039_api_taobao_300login(self):
        """
        desc       :使用用户名密码登录并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '需要短信认证')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='系统繁忙')
    def test_040_api_taobao_502login(self):
        """
        desc       :使用用户名密码登录并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账户已被冻结')
    def test_041_api_taobao_401login(self):
        """
        desc       :使用用户名密码登录并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 401)
        Assertion.verity(json.loads(rs1)['m'], '该账户已被冻结，暂时无法登录')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='授权成功')
    def test_042_api_taobao_200login(self):
        """
        desc       :使用用户名密码登录并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['data']['reqId'], '12345')

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账号密码错误')
    def test_043_api_taobao_400login(self):
        """
        desc       :使用用户名密码登录并获取信息
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '你输入的密码和账户名不匹配')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='需要短信验证')
    def test_044_api_taobao_300login_reqid_none(self):
        """
        desc       :使用用户名密码登录并获取信息, reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '需要短信认证')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='系统繁忙')
    def test_045_api_taobao_502login_reqid_none(self):
        """
        desc       :使用用户名密码登录并获取信息, reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账户已被冻结')
    def test_046_api_taobao_401login_reqid_none(self):
        """
        desc       :使用用户名密码登录并获取信息 , reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 401)
        Assertion.verity(json.loads(rs1)['m'], '该账户已被冻结，暂时无法登录')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='授权成功')
    def test_047_api_taobao_200login_reqid_none(self):
        """
        desc       :使用用户名密码登录并获取信息, reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账号密码错误')
    def test_048_api_taobao_400login_reqid_none(self):
        """
        desc       :使用用户名密码登录并获取信息, reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '你输入的密码和账户名不匹配')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_049_api_taobao_login_password_none(self):
        """
        desc       :使用用户名密码登录并获取信息 ,password为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name=name, password='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'password不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_050_api_taobao_login_name_none(self):
        """
        desc       :使用用户名密码登录并获取信息，name为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid=reqid, token=token, name='', password=password)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'name不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_051_api_taobao_login_token_error(self):
        """
        desc       :使用用户名密码登录并获取信息， token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token=token + '1', name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_052_api_taobao_login_token_none(self):
        """
        desc       :使用用户名密码登录并获取信息 ，token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_login(reqid='', token='', name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='验证码错误')
    def test_053_api_taobao_302verifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '手机验证码错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='系统错误')
    def test_054_api_taobao_500verifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='校验码失效')
    def test_055_api_taobao_301verifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '校验码失效，请重新获取')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='授权成功')
    def test_056_api_taobao_200verifycode(self):
        """
        desc       :校验短信验证码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verity(json.loads(rs1)['data']['reqId'], '')

    @unittest.skipIf(pile, '忽略不打桩')
    def test_057_api_taobao_verifycode_code_error(self):
        """
        desc       :校验短信验证码，code错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['s'], 0)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')

    @unittest.skipIf(pile, '忽略不打桩')
    def test_058_api_taobao_verifycode_reqid_error(self):
        """
        desc       :校验短信验证码， reqId错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid + '1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_059_api_taobao_verifycode_reqid_none(self):
        """
        desc       :校验短信验证码，reqId为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_060_api_taobao_verifycode_code_none(self):
        """
        desc       :校验短信验证码，code为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'code不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_061_api_taobao_verifycode_token_none(self):
        """
        desc       :校验短信验证码 ,token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_062_api_taobao_verifycode_token_error(self):
        """
        desc       :校验短信验证码 ,token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_verifycode(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getqrcode', remark='获取二维码成功')
    def test_063_api_taobao_200getqrcode(self):
        """
        desc       :获取二维码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '获取二维码成功')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verityNotNone(json.loads(rs1)['data']['pic'])
        Assertion.verityNotNone(json.loads(rs1)['data']['reqId'])

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getqrcode', remark='系统繁忙')
    def test_064_api_taobao_502getqrcode(self):
        """
        desc       :获取二维码
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getqrcode', remark='获取二维码成功')
    def test_065_api_taobao_200getqrcode_reqid_none(self):
        """
        desc       :获取二维码 , reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '获取二维码成功')
        Assertion.verity(json.loads(rs1)['s'], 1)
        Assertion.verityNotNone(json.loads(rs1)['data']['pic'])
        Assertion.verityNotNone(json.loads(rs1)['data']['reqId'])

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getqrcode', remark='系统繁忙')
    def test_066_api_taobao_502getqrcode_reqid_none(self):
        """
        desc       :获取二维码 , reqid为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_067_api_taobao_getqrcode_token_error(self):
        """
        desc       :获取二维码, token错误
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid='', token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    def test_068_api_taobao_getqrcode_token_none(self):
        """
        desc       :获取二维码, token为空
        author     : 罗林
        """
        rs1 = TbAction.test_api_taobao_getqrcode(reqid='', token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)
