#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-11 下午 5:19
@Author     : songchao
@File       : testEasyloan_app_004_login.py
@desc       :  登录相关模块测试用例
"""
import json
import time
import unittest

import redis

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_appAction as ea_app
from easyloan.testAction import specialAction as  ea_app1


class testEasyloan_app_004_login(TestBaseCase):
    def test_001__api_78dk_clientapp_common_sms_sendValidate(self):
        """
            Time       :2019-06-11
            author     : songchao
            desc       : 登录短信验证码
        """
        rs = ea_app.test_api_78dk_clientapp_common_sms_sendValidate('2', 18780101362)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_002__api_78dk_clientapp_login_fastRegister(self):
        """
              Time       :2019-06-12
              author     : songchao
              desc       : 短信登录
        """
        pool = redis.ConnectionPool(host='192.168.15.159', port=801, password='78dk.com')
        r = redis.Redis(connection_pool=pool)
        r.set("2_18780101362", "123456")
        time.sleep(0.5)
        # duanxin=r.get("2_18780101362")
        # print(duanxin)
        # print(type(duanxin))
        # new_duanxin=json.loads(duanxin)
        # new_duanxin=eval(duanxin.decode('utf-8'))
        # print(new_duanxin)
        # print(type(new_duanxin))
        rs = ea_app.test_api_78dk_clientapp_login_smsLogin('18780101362', 123456)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "token")

    @unittest.skip('退出登录')
    def test_003_api_78dk_clientapp_login_loginOut(self):
        """
             Time: 2019 - 06 - 12
             author: songchao
             desc: 退出登录
        """
        rs=ea_app.test_api_78dk_clientapp_login_loginOut()
        ass.verity(json.loads(rs)['code'], "10000")

    def test_004__api_78dk_clientapp_login_register(self):
        """
                 Time       :2019-06-12
                 author     : songchao
                 desc       : 注册
        """
        pool = redis.ConnectionPool(host='192.168.15.159', port=801, password='78dk.com')
        # r=redis.Redis(host='192.168.15.159', port=6379)
        r = redis.Redis(connection_pool=pool)
        r.set("1_15542487837", "123456")
        time.sleep(0.5)
        rs = ea_app1.test_api_78dk_clientapp_login_register(123456, "15542487837", "sc123456", 18780101362)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "token")
        eq.delete_info("client_base", "mobile=15542487837")
        # rs1 = ea_app.test_api_78dk_clientapp_login_pwLogin('sc123456', 15542487837)
        # ass.verity(json.loads(rs1)['code'], "10000")

    def test_005__api_78dk_clientapp_login_retrievedPw(self):
        """
            Time       :2019-06-12
            author     : songchao
            desc       : 找回密码
        """
        pool = redis.ConnectionPool(host='192.168.15.159', port=801, password='78dk.com')
        # r=redis.Redis(host='192.168.15.159', port=6379)
        r = redis.Redis(connection_pool=pool)
        r.set("1_15542487836", "123456")
        time.sleep(0.5)
        rs1 = ea_app.test_api_78dk_clientapp_login_register(123456, "15542487836", "sc123456", 18780101362)
        r.set("3_15542487836", "123456")
        time.sleep(0.5)
        rs = ea_app.test_api_78dk_clientapp_login_retrievedPw("sc199222", 15542487836, "123456")
        ass.verity(json.loads(rs)['code'], "10000")
        eq.delete_info("client_base", "mobile=15542487836")

    def test_006__api_78dk_clientapp_login_pwLogin(self):
        global token
        """
             Time       :2019-06-12
             author     : songchao
             desc       : 密码登录
        """
        rs = ea_app.test_api_78dk_clientapp_login_pwLogin('sc199222', 18780101362)
        ass.verity(json.loads(rs)['code'], "10000")
        token = json.loads(rs)["data"]["token"]
        ass.verityContain(json.loads(rs)['data'], "token")

    def test_007__api_78dk_clientapp_auth_messAuth_queryCarInfo(self):
        """
                     Time       :2019-06-13
                     author     : songchao
                     desc       : 车辆认证查询
        """
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_queryCarInfo()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "brandId")
        # ass.verityContain(json.loads(rs)['data'], "brandName")
        # ass.verityContain(json.loads(rs)['data'], "city")
        # ass.verityContain(json.loads(rs)['data'], "cityName")
        # ass.verityContain(json.loads(rs)['data'], "modelId")
        # ass.verityContain(json.loads(rs)['data'], "modelName")
        # ass.verityContain(json.loads(rs)['data'], "registerTime")
        # ass.verityContain(json.loads(rs)['data'], "seriesId")
        # ass.verityContain(json.loads(rs)['data'], "seriesName")
        # ass.verityContain(json.loads(rs)['data'], "vehicleAuthUuid")

    def test_008__api_78dk_clientapp_homePage_homeOrder_queryOrderState(self):
        """
                     Time       :2019-06-13
                     author     : songchao
                     desc       : 订单状态
        """
        rs = ea_app.test_api_78dk_clientapp_homePage_homeOrder_queryOrderState()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "authState")
        ass.verityContain(json.loads(rs)['data'], "orderState")
