#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-12 下午 14:20
@Author     : 闫红
@File       : testScreen_web_001_login.py
@desc       : web端登录接口测试用例
"""
import json
from common.myCommon.TestBaseCase import TestBaseCase
from dp.testAction import Dp_webAction as dpweb
from common.myCommon import Assertion as ass

class testScreen_web_001_login(TestBaseCase):
    def test_001_login(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :登录成功
        """
        rs = dpweb.test_login('apitest','123456')
        ass.verity(json.loads(rs)['code'], "20000")

    def test_002_login_fail(selfs):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :不存在的用户进行登录
        """
        rs = dpweb.test_login('dd11','111')
        ass.verity(json.loads(rs)['code'],'50000')

    def test_003_login_fail(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :错误密码进行登录
        """
        rs = dpweb.test_login('admin','123')
        ass.verity(json.loads(rs)['code'],'50000')
        ass.verityContain(json.loads(rs)['message'],'用户名 或 密码错误！')


