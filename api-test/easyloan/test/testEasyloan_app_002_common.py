#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-25 下午 2:19
@Author     : 罗林
@File       : testEasyloan_app_002_common.py
@desc       : APP端通用接口测试用例
"""

import json
import unittest

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.testAction import Easyloan_appAction as ea_app, loginAction as la


class testEasyloan_app_002_common(TestBaseCase):
    def test_001_api_78dk_clientapp_common_gps_addGpsInfo(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : GPS数据上传
        """
        rs = ea_app.test_api_78dk_clientapp_common_gps_addGpsInfo(
            address='', region=510107, city=510100, lat='30.5403921022', lng='104.0710005358', province=510000)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_002_api_78dk_clientapp_common_qiniu_queryQiNiuToken(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 七牛云上传token
        """
        rs = ea_app.test_api_78dk_clientapp_common_qiniu_queryQiNiuToken()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "token")

    def test_003_api_78dk_clientapp_common_userInfo_queryUserInfo(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 个人综合信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_common_userInfo_queryUserInfo()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "bankCard")
        # ass.verityContain(json.loads(rs)['data'], "headPic")
        # ass.verityContain(json.loads(rs)['data'], "idcard")
        # ass.verityContain(json.loads(rs)['data'], "name")

    def test_004_api_78dk_clientapp_common_userInfo_queryUserAgreement(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 借款协议
        """
        rs = ea_app.test_api_78dk_clientapp_common_userInfo_queryUserAgreement()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "deduPowersUrl")
        # ass.verityContain(json.loads(rs)['data'], "userInfoQueryUrl")

    def test_005_api_78dk_clientapp_common_userInfo_uploadAddressBook(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 上传通讯录
        """
        addressbookjson = """ [{'name':'田边','phones':['13018204370']},
        {'name':'阿部','phones':['13018204374','13018850528','0281365085','0281336856']},
        {'name':'130 1820 4370','phones':['13018204370']}]"""
        rs = ea_app.test_api_78dk_clientapp_common_userInfo_uploadAddressBook(addressbookjson)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_006_api_78dk_clientapp_common_city_queryCityList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 城市列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_city_queryCityList()
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('每次都会发验证码')
    def test_007_api_78dk_clientapp_common_sms_sendValidate(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 短信验证码
        """
        rs = ea_app.test_api_78dk_clientapp_common_sms_sendValidate(mobile=la.mobile, type=2)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('每次都会发验证码')
    def test_008_api_78dk_clientapp_common_sms_sendCodeVer(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 短信验证码（需校验）
        """
        rs = ea_app.test_api_78dk_clientapp_common_sms_sendCodeVer(mobile=la.mobile, type=2, picvercode='', verid='')
        ass.verity(json.loads(rs)['code'], "S0019")

    def test_009_api_78dk_clientapp_common_sys_versionUp(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 版本升级（普通）
        """
        rs = ea_app.test_api_78dk_clientapp_common_sys_versionUp()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "description")
        # ass.verityContain(json.loads(rs)['data'], "upUrl")
        # ass.verityContain(json.loads(rs)['data'], "versNumb")

    def test_010_api_78dk_clientapp_common_sys_iosOnline(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : ios上架标识
        """
        rs = ea_app.test_api_78dk_clientapp_common_sys_iosOnline()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "online")
        ass.verityTrue(json.loads(rs)['data']['online'])

    def test_011_api_78dk_clientapp_common_sys_androidIsOnline(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : andriod上架标识
        """
        rs = ea_app.test_api_78dk_clientapp_common_sys_androidIsOnline()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "online")
        ass.verityTrue(json.loads(rs)['data']['online'])

    def test_012api_78dk_clientapp_common_car_queryCarTypeList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆品牌列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_car_queryCarTypeList(brandname='宝马')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_013_api_78dk_clientapp_common_car_queryCarModelList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车系列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_car_queryCarModelList(brandid=1)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_014_api_78dk_clientapp_common_car_queryCarlList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_car_queryCarlList(seriesid=1)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_015_api_78dk_clientapp_common_dict_queryDictList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 下拉字典列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_dict_queryDictList(dicttypecode='LIST01')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_016_api_78dk_clientapp_common_dict_queryProductList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 获取产品及期数列表
        """
        rs = ea_app.test_api_78dk_clientapp_common_dict_queryProductList()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "productConfigList")
        ass.verityContain(json.loads(rs)['data'], "productDetailUuid")
        ass.verityContain(json.loads(rs)['data'], "period")
        ass.verityContain(json.loads(rs)['data'], "rate")

    def test_017_api_78dk_clientapp_common_picCode_getPicVerCode(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 获取图形验证码
        """
        rs = ea_app.test_api_78dk_clientapp_common_picCode_getPicVerCode()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "codeBase64")
        ass.verityContain(json.loads(rs)['data'], "verId")

