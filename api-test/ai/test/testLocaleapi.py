#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-26 下午 2:16
@Author     : songchao
@File       : testLocaleapi.py
@desc       :  归属地 接口自动化
"""
import json

from faker import Faker

from ai.testAction import LocaleapiAction
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase

fake = Faker("zh_CN")


class testLocaleapi(TestBaseCase):
    def test_001_api_Locale_getlocal(self):
        """
            Time       :2019-06-26
            author     : 宋超
            desc       :
        """
        rs = LocaleapiAction.test_operator("15189897858")
        Assertion.verity(json.loads(rs)['15189897858']['area_code'], '0514')
        Assertion.verity(json.loads(rs)['15189897858']['city'], '扬州')
        Assertion.verity(json.loads(rs)['15189897858']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['15189897858']['province'], '江苏')

    def test_002_api_Locale_getlocal(self):
        """
            Time       :2019-06-26
            author     : 宋超
            desc       :
        """
        rs = LocaleapiAction.test_operator("13347825211")
        Assertion.verity(json.loads(rs)['13347825211']['area_code'], '025')
        Assertion.verity(json.loads(rs)['13347825211']['city'], '南京')
        Assertion.verity(json.loads(rs)['13347825211']['phone_type'], '电信')
        Assertion.verity(json.loads(rs)['13347825211']['province'], '江苏')

    def test_003_api_Locale_getlocal(self):
        """
            Time       :2019-06-26
            author     : 宋超
            desc       :
        """
        rs = LocaleapiAction.test_operator(["15189897858", "13314785888"])
        Assertion.verity(json.loads(rs)['15189897858']['area_code'], '0514')
        Assertion.verity(json.loads(rs)['15189897858']['city'], '扬州')
        Assertion.verity(json.loads(rs)['15189897858']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['15189897858']['province'], '江苏')
        Assertion.verity(json.loads(rs)['13314785888']['area_code'], '0478')
        Assertion.verity(json.loads(rs)['13314785888']['city'], '巴彦淖尔')
        Assertion.verity(json.loads(rs)['13314785888']['phone_type'], '电信')
        Assertion.verity(json.loads(rs)['13314785888']['province'], '内蒙古')

    def test_004_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("8615189897858")
        Assertion.verity(json.loads(rs)['8615189897858']['area_code'], '0514')
        Assertion.verity(json.loads(rs)['8615189897858']['city'], '扬州')
        Assertion.verity(json.loads(rs)['8615189897858']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['8615189897858']['province'], '江苏')

    def test_005_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("6615189878958")
        Assertion.verity(json.loads(rs)['6615189878958']['message'], 'recognize_failed')

    # @unittest.skip('返回结果断言有问题，需要再次调试')
    def test_006_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :输入非电话号码非数字的参数
        """
        rs = LocaleapiAction.test_operator("sdgfgdghdfdgh")
        Assertion.verity(json.loads(rs)['sdgfgdghdfdgh']['message'], 'recognize_failed')

    def test_007_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("151898+58")
        Assertion.verity(json.loads(rs)['151898+58']['message'], 'recognize_failed')

    def test_008_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("151898dfg58")
        Assertion.verity(json.loads(rs)['151898dfg58']['message'], 'recognize_failed')

    def test_009_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("12345678901")
        Assertion.verity(json.loads(rs)['12345678901']['message'], 'recognize_failed')

    def test_010_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("1334782521")
        Assertion.verity(json.loads(rs)['1334782521']['message'], 'recognize_failed')

    def test_011_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("sdfgdfhfghhf")
        Assertion.verity(json.loads(rs)['sdfgdfhfghhf']['message'], 'recognize_failed')

    def test_012_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator(["12345678901", "012456789", "cvbcfjhfgjkgk"])
        Assertion.verity(json.loads(rs)['12345678901']['message'], 'recognize_failed')
        Assertion.verity(json.loads(rs)['012456789']['message'], 'recognize_failed')
        Assertion.verity(json.loads(rs)['cvbcfjhfgjkgk']['message'], 'recognize_failed')

    def test_013_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator(["15982835741", "0389304898", "-", "", "0288495844"])
        Assertion.verity(json.loads(rs)[''], 'number is empty')
        Assertion.verity(json.loads(rs)['-'], 'number is empty')
        Assertion.verity(json.loads(rs)['0389304898']['message'], 'recognize_failed')
        Assertion.verity(json.loads(rs)['0288495844']['area_code'], '028')
        Assertion.verity(json.loads(rs)['0288495844']['city'], '成都/眉山/资阳')
        Assertion.verity(json.loads(rs)['0288495844']['phone_type'], '联通')
        Assertion.verity(json.loads(rs)['0288495844']['province'], '四川')
        Assertion.verity(json.loads(rs)['15982835741']['area_code'], '028')
        Assertion.verity(json.loads(rs)['15982835741']['city'], '成都')
        Assertion.verity(json.loads(rs)['15982835741']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['15982835741']['province'], '四川')

    def test_014_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("")
        Assertion.verity(json.loads(rs)[''], 'number is empty')

    def test_015_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("[]")
        Assertion.verity(json.loads(rs)['[]']['message'], 'recognize_failed')

    def test_016_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("028 586958")
        Assertion.verity(json.loads(rs)['028 586958']['area_code'], '028')
        Assertion.verity(json.loads(rs)['028 586958']['city'], '成都/眉山/资阳')
        Assertion.verity(json.loads(rs)['028 586958']['phone_type'], '联通')
        Assertion.verity(json.loads(rs)['028 586958']['province'], '四川')

    def test_017_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("028-47896585")
        Assertion.verity(json.loads(rs)['028-47896585']['area_code'], '028')
        Assertion.verity(json.loads(rs)['028-47896585']['city'], '成都/眉山/资阳')
        Assertion.verity(json.loads(rs)['028-47896585']['phone_type'], '联通')
        Assertion.verity(json.loads(rs)['028-47896585']['province'], '四川')

    def test_018_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("+15147896585")
        Assertion.verity(json.loads(rs)['+15147896585']['area_code'], '0478')
        Assertion.verity(json.loads(rs)['+15147896585']['city'], '巴彦淖尔')
        Assertion.verity(json.loads(rs)['+15147896585']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['+15147896585']['province'], '内蒙古')

    def test_019_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("*15147896585")
        Assertion.verity(json.loads(rs)['*15147896585']['message'], 'recognize_failed')

    def test_020_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("+02*896585")
        Assertion.verity(json.loads(rs)['+02*896585']['message'], 'recognize_failed')

    def test_021_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("+8615147896585")
        Assertion.verity(json.loads(rs)['+8615147896585']['area_code'], '0478')
        Assertion.verity(json.loads(rs)['+8615147896585']['city'], '巴彦淖尔')
        Assertion.verity(json.loads(rs)['+8615147896585']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['+8615147896585']['province'], '内蒙古')

    def test_022_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("008615189897858")
        Assertion.verity(json.loads(rs)['008615189897858']['area_code'], '0514')
        Assertion.verity(json.loads(rs)['008615189897858']['city'], '扬州')
        Assertion.verity(json.loads(rs)['008615189897858']['phone_type'], '移动')
        Assertion.verity(json.loads(rs)['008615189897858']['province'], '江苏')

    def test_023_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        rs = LocaleapiAction.test_operator("[]")
        Assertion.verity(json.loads(rs)['[]']['message'], 'recognize_failed')

    def test_024_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        phone_number = dict()
        for i in range(0, 100):
            phone_number[i] = fake.phone_number()
        phone_number_list = list(phone_number.values())
        rs = LocaleapiAction.test_operator(phone_number_list)
        for phone in phone_number_list:
            Assertion.verityContain(json.loads(rs), phone)

    def test_025_api_Locale_getlocal(self):
        """
        Time       :2019-06-26
        author     : 宋超
        desc       :
        """
        phone = str(fake.phonenumber_prefix()) + str(fake.ean8())
        rs = LocaleapiAction.test_operator(phone)
        Assertion.verityContain(json.loads(rs), phone)
