#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2020-01-10
@Author     : 闫红
@File       : test_002_web_ur.py
@desc       :  催收管理接口自动化
"""


import json
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xyf.testAction import Creditpay_urAction, Creditpay_urAction_special
from faker import Factory
from common.myFile import MockData

fake = Factory().create('zh_CN')
carno = fake.ssn()
phone = MockData.phone()
name = fake.name()


class test_002_web_ur(TestBaseCase):
    def test_001_ui_user_findUserBill(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出所有逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_002_ui_user_findUserBill_M1(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出M1阶段逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='M1', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_ui_user_findUserBill_M2(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出M2阶段逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='M2', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_ui_user_findUserBill_M3(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出M3阶段逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='M3', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_005_test_ui_user_findUserBill_WEIWAI(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出WEIWAI阶段逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='WEIWAI', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_006_test_ui_user_findUserBill_SHUSONG(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，筛选出SHUSONG阶段逾期用户数据
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='SHUSONG', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_007_ui_user_findUserBill_err_carno(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，身份证号错误
        """
        carno = '123'
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno=carno, loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_008_ui_user_findUserBill_carno_not_exist(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，身份证不存在
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno=carno, loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_009_ui_user_findUserBill_carno_overlong(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，身份证号错误
        """
        carno = MockData.number(30)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno=carno, loantimebegin='', loantimeend='',
              phone='', realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_010_ui_user_findUserBill_name_not_exist(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，姓名不存在
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname=name, shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_011_ui_user_findUserBill_name_overlong(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，姓名超长
        """
        name = MockData.words_cn(256)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname=name, shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_012_ui_user_findUserBill_name_no_str(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，姓名传入非字符
        """
        name = 123
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone='', realname=name, shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_013_ui_user_findUserBill_phone_not_exist(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，电话不存在
        """
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone=phone, realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_014_ui_user_findUserBill_phone_overlong(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，电话超长
        """
        phone = '131'+ MockData.phone(11)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone=phone, realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_015_ui_user_findUserBill_phone_not_startwith_1(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，电话传入非1开头的11位数
        """
        phone = int('2')+MockData.number(10)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone=phone, realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_016_ui_user_findUserBill_phone(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，电话格式不正确
        """
        phone = MockData.words_cn(3)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone=phone, realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_017_ui_user_findUserBill_phone(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :逾期用户-列表，电话输入座机
        """
        phone = '010-'+MockData.words_cn(9)
        res = json.loads(Creditpay_urAction.test_ui_user_findUserBill(cardno='', loantimebegin='', loantimeend='',
              phone=phone, realname='', shouldrepaymentbegin='', shouldrepaymentend='', stage='', currentpage=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_018_ui_user_getUserInfo_null(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :用户信息，传入空
        """
        res = json.loads(Creditpay_urAction.test_ui_user_getUserInfo(userid=''))
        Assertion.verity(res['code'], '20000')

    def test_019_ui_user_getUserInfo_overlong(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :用户信息，userid超长
        """
        userid = MockData.number(256)
        res = json.loads(Creditpay_urAction.test_ui_user_getUserInfo(userid=userid))
        Assertion.verity(res['code'], '20000')

    def test_020_ui_user_getUserInfo_error(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :用户信息，userid格式不正确
        """
        userid = MockData.words_cn(3)
        res = json.loads(Creditpay_urAction.test_ui_user_getUserInfo(userid=userid))
        Assertion.verity(res['code'], '20000')

    def test_021_ui_user_getUserInfo_not_exist(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :用户信息，userid不存在
        """
        userid = -1
        res = json.loads(Creditpay_urAction.test_ui_user_getUserInfo(userid=userid))
        Assertion.verity(res['code'], '20000')

    def test_022_ui_user_getUserInfo(self):
        """
        Time       :20120-04-10
        author     : 闫红
        desc       :用户信息
        """
        res = json.loads(Creditpay_urAction_special.test_ui_user_getUserInfo(userid=94368))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')


