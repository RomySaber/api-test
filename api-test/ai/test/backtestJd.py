#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-19 下午 3:37
@Author     : 罗林
@File       : testJd.py
@desc       :  京东爬虫 接口自动化 （田璐玲）
"""


import json
import unittest
from ai.test.decorator_mongo import update_mongo, close_pile
from ai.testAction import JdAction
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ai.testSource import ai_config

reqid = ai_config.reqid
token = ai_config.token
name = ai_config.Jd_name
password = ai_config.Jd_password
querys = {"project_name": "jingdong"}
# 是否不打桩
pile = True


class testJd(TestBaseCase):
    @unittest.skipIf(pile, '忽略不打桩')
    @close_pile(querys)
    @update_mongo(querys=querys, api_name='getqrcode', remark='系统繁忙')
    def test_002_api_jingdong_get_502qrcode(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二维码,返回502
        """
        rs1 = JdAction.test_api_jingdong_getqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getqrcode', remark='获取二维码成功')
    def test_003_api_jingdong_get_200qrcode(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二维码,返回200
        """
        rs1 = JdAction.test_api_jingdong_getqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '获取二维码成功')
        Assertion.verity(json.loads(rs1)['s'], 1)

    def test_004_api_jingdong_getqrcode_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二维码
        """
        rs1 = JdAction.test_api_jingdong_getqrcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_005_api_jingdong_getqrcode_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二维码
        """
        rs1 = JdAction.test_api_jingdong_getqrcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_006_api_jingdong_getqrcode_all_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       :获取二维码
        """
        rs1 = JdAction.test_api_jingdong_getqrcode(reqid='', token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='系统错误')
    def test_007_api_jingdong_verify_500qrcode(self):
        """
        Time       :2019-09-16
        author     : 罗林
        desc       :验证二维码是否已扫描，并获取信息,返回500
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='暂未授权')
    def test_008_api_jingdong_verify_300qrcode(self):
        """
        Time       :2019-09-16
        author     : 罗林
        desc       :验证二维码是否已扫描，并获取信息,返回300
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '暂未授权')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='二维码已失效')
    def test_009_api_jingdong_verify_301qrcode(self):
        """
        Time       :2019-09-16
        author     : 罗林
        desc       :验证二维码是否已扫描，并获取信息,返回301
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '二维码已失效')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='已扫描成功')
    def test_010_api_jingdong_verify_303qrcode(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，并获取信息,返回303
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 303)
        Assertion.verity(json.loads(rs1)['m'], '已扫描成功，登录中...')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='已扫描登录')
    def test_011_api_jingdong_verify_201qrcode(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，并获取信息,返回201
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 201)
        Assertion.verity(json.loads(rs1)['m'], '已扫描登录')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='授权成功')
    def test_012_api_jingdong_verify_200qrcode(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，并获取信息,返回200
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifyqrcode', remark='需要短信验证')
    def test_013_api_jingdong_verify_302qrcode(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，并获取信息,返回302
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '需要短信验证')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_014_api_jingdong_verify_qrcode_token_error(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，token错误
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_015_api_jingdong_verify_qrcode_reqid_error(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，reqid错误
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid+'1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_016_api_jingdong_verify_qrcode_reqid_is_null(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，reqid为空
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_017_api_jingdong_verify_qrcode_token_is_null(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，token为空
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_018_api_jingdong_verify_qrcode_all_is_null(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :验证二维码是否已扫描，reqid/token均为空
        """
        rs1 = JdAction.test_api_jingdong_verifyqrcode(reqid='', token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='系统错误')
    def test_019_api_jingdong_qrget_500code(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,返回500
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='验证码获取过于频繁')
    def test_020_api_jingdong_qrget_301code(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,返回301
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '获取验证码操作太频繁，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='短信验证码发送失败')
    def test_021_api_jingdong_qrget_300code(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,返回300
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码发送失败')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrgetcode', remark='短信验证码已发送')
    def test_022_api_jingdong_qrget_200code(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,返回200
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码已发送')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_023_api_jingdong_qrgetcode_reqid_error(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,reqid错误
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid+'1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_024_api_jingdong_qrgetcode_token_error(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,token错误
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token=token+'1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_025_api_jingdong_qrgetcode_token_is_null(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,token为空
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_026_api_jingdong_qrgetcode_reqid_is_null(self):
        """
        Time       :2019-09-16
        author     : 闫红
        desc       :获取短信验证码,reqid为空
        """
        rs1 = JdAction.test_api_jingdong_qrgetcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='授权成功')
    def test_027_api_jingdong_qrverifycode_code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token, code='1')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 1)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='系统错误')
    def test_028_api_jingdong_qrverifycode_500code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码,返回500
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token, code='1')
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='短信验证码错误')
    def test_029_api_jingdong_qrverifycode_300code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码,返回300
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token, code='1')
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '手机验证码错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='qrverifycode', remark='验证码失效')
    def test_030_api_jingdong_qrverifycode_301code(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码,返回301
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token, code='1')
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '本次验证已失效，请重新获取二维码重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_031_api_jingdong_qrverifycode_code_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码,code为空
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'code不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_032_api_jingdong_qrverifycode_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid + 'q1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_033_api_jingdong_qrverifycode_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_034_api_jingdong_qrverifycode_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_035_api_jingdong_qrverifycode_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_qrverifycode(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='需要短信验证')
    def test_036_api_jingdong_login_300return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回300
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '您的账号需要短信验证，请获取短信验证码')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='需要短信验证')
    def test_037_api_jingdong_login_300return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回300
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '您的账号需要短信验证，请获取短信验证码')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='系统繁忙')
    def test_038_api_jingdong_login_502return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回502
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 502)
        Assertion.verity(json.loads(rs1)['m'], '系统繁忙，请稍后再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='系统内部滑块处理错误')
    def test_039_api_jingdong_login_401return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回401
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 401)
        Assertion.verity(json.loads(rs1)['m'], '系统内部滑块处理错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账户密码错误')
    def test_040_api_jingdong_login_402return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回402
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 402)
        Assertion.verity(json.loads(rs1)['m'], '账户与密码不匹配，请重新输入')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='账号需要语音验证')
    def test_041_api_jingdong_login_301return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回301
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '您的账号需要语音验证码验证，请在京东平台上认证后再进行本平台的授权')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='需要短信验证')
    def test_042_api_jingdong_login_300return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回300
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '您的账号需要短信验证，请获取短信验证码')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='授权成功')
    def test_043_api_jingdong_login_200return(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息，返回200
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '登录成功')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_044_api_jingdong_login_name_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name='', password=password)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'name不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_045_api_jingdong_login_passwd_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token, name=name, password='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'password不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_046_api_jingdong_login_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token=token + '1', name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_047_api_jingdong_login_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息
        """
        rs1 = JdAction.test_api_jingdong_login(reqid=reqid, token='', name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='login', remark='授权成功')
    def test_048_api_jingdong_login_reqid_is_null(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 使用用户名密码登录并获取信息,非必填reqId为空
        """
        rs1 = JdAction.test_api_jingdong_login(reqid='', token=token, name=name, password=password)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '登录成功')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='系统错误')
    def test_050_api_jingdong_500getcode(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 获取短信验证码，返回500
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='短信验证码发送成功')
    def test_051_api_jingdong_200getcode(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 获取短信验证码，返回200
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码发送成功')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='短信验证码发送失败')
    def test_052_api_jingdong_300getcode(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 获取短信验证码，返回300
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 300)
        Assertion.verity(json.loads(rs1)['m'], '短信验证码发送失败')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='短信验证码获取过于频繁')
    def test_053_api_jingdong_301getcode(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 获取短信验证码，返回301
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '短期内不可再次获取，请稍后重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='getcode', remark='获取次数达上限')
    def test_054_api_jingdong_302getcode(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 获取短信验证码，返回302
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token)
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '获取次数已达上限，请明天再试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_055_api_jingdong_getcode_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 获取短信验证码，reqid错误
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid + '1', token=token)
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_056_api_jingdong_getcode_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 获取短信验证码，reqid为空
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid='', token=token)
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_057_api_jingdong_getcode_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 获取短信验证码，token错误
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token=token + '1')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_058_api_jingdong_getcode_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 获取短信验证码，token为空
        """
        rs1 = JdAction.test_api_jingdong_getcode(reqid=reqid, token='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='风险用户与验证类型不匹配')
    def test_059_api_jingdong_verifycode_302code(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 校验短信验证码，返回302
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['code'], 302)
        Assertion.verity(json.loads(rs1)['m'], '风险用户与验证类型不匹配')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='系统错误')
    def test_060_api_jingdong_verifycode_500code(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 校验短信验证码，返回500
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['code'], 500)
        Assertion.verity(json.loads(rs1)['m'], '系统错误，请重试')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='授权成功')
    def test_061_api_jingdong_verifycode_200code(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 校验短信验证码，返回200
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['code'], 200)
        Assertion.verity(json.loads(rs1)['m'], '授权成功')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='授权失败')
    def test_062_api_jingdong_verifycode_401code(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 校验短信验证码，返回401
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['code'], 401)
        Assertion.verity(json.loads(rs1)['m'], '授权失败')
        Assertion.verity(json.loads(rs1)['s'], 0)

    @unittest.skipIf(pile, '忽略不打桩')
    @update_mongo(querys=querys, api_name='verifycode', remark='验证码错误')
    def test_063_api_jingdong_verifycode_301code(self):
        """
        Time       :2019-09-17
        author     : 闫红
        desc       : 校验短信验证码，返回301
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='123')
        Assertion.verity(json.loads(rs1)['code'], 301)
        Assertion.verity(json.loads(rs1)['m'], '验证码输入有误，请重新输入')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_064_api_jingdong_verifycode_code_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token, code='')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'code不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_065_api_jingdong_verifycode_reqid_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid + '1', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 400)
        Assertion.verity(json.loads(rs1)['m'], '不存在该会话id')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_066_api_jingdong_verifycode_reqid_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid='', token=token, code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'reqId不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_067_api_jingdong_verifycode_token_error(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token=token + '1', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 501)
        Assertion.verity(json.loads(rs1)['m'], 'token错误')
        Assertion.verity(json.loads(rs1)['s'], 0)

    def test_068_api_jingdong_verifycode_token_none(self):
        """
        Time       :2019-06-19
        author     : 罗林
        desc       : 校验短信验证码
        """
        rs1 = JdAction.test_api_jingdong_verifycode(reqid=reqid, token='', code='123456')
        Assertion.verity(json.loads(rs1)['code'], 403)
        Assertion.verity(json.loads(rs1)['m'], 'token不能为空')
        Assertion.verity(json.loads(rs1)['s'], 0)
