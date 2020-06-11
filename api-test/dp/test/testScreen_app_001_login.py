#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-12 下午 14:20
@Author     : 闫红
@File       : testScreen_app_001_login.py
@desc       : app端登录接口测试用例
"""
import json
from common.myCommon.TestBaseCase import TestBaseCase
from dp.testAction import Dp_appAction as dpapp
from common.myCommon import Assertion as ass

class testScreen_app_001_login(TestBaseCase):
    def test_001_login(self):
        """
          Time       :2019-06-12
          author     :闫红
          desc       :登录成功
        """
        rs = dpapp.test_login('1','apitest','123456')
        ass.verity(json.loads(rs)['code'], "20000")



