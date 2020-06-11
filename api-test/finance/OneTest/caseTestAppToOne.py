#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/6/5 0005 下午 2:01
@Author     : 罗林
@File       : TestAppToOne.py
@desc       : 
"""
import json

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import ClappAction


class TestAppToOne(TestBaseCase):

    def test16(self):
        r = ClappAction.test_login('', '', 'yanhong@78dk.com', '123456', '', '', '')
        # Assertion.verity(json.loads(r)['data']['phone'], '13699479886', r)

    def test01(self):
        r = ClappAction.test_notification_update(True, 0)

    def test02(self):
        r = ClappAction.test_userinfo()
        Assertion.verity(json.loads(r)['data']['user']['phone'], '13699479886', r)

    def test15(self):
        r = ClappAction.test_logout()

    def test03(self):
        r = ClappAction.test_device_caralldevice('1')

    def test04(self):
        r = ClappAction.test_device_updateposition('1')
        Assertion.verity(json.loads(r)['data']['carId'], 1, r)

    def test05(self):
        r = ClappAction.test_device_tracklist('1', '', '', '')
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test06(self):
        r = ClappAction.test_device_list('', '1', 0)
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test07(self):
        r = ClappAction.test_device_more('1', '', '1', '1', 0)
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test08(self):
        r = ClappAction.test_organization_list()
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test09(self):
        r = ClappAction.test_warning_list('', '', '', '1', '10', '')
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test10(self):
        r = ClappAction.test_warningType_list()
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test11(self):
        r = ClappAction.test_warning_handleinit(1)
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test12(self):
        r = ClappAction.test_warning_resolve(1, '', 1, '', 2)
        Assertion.verity(json.loads(r)['code'], 'F2000')

    def test13(self):
        r = ClappAction.test_warning_detail(1)
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")

    def test14(self):
        r = ClappAction.test_warning_mapinfo(1)
        Assertion.verity(json.loads(r)['code'], 'F2000', "返回参数状态码检查")
