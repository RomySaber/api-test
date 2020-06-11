#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-24 下午 4:56
@Author     : 罗林
@File       : testEasyloan_app_001_other.py
@desc       :  app端首页和工具接口测试用例
"""

import json
from common.myCommon import Assertion as ass, TimeFormat as tf
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_appAction as ea_app

car_code = '川A2YF96'
vincode = 'LVSHJCAL4FE273449'


class testEasyloan_app_001_other(TestBaseCase):
    def test_001_api_78dk_clientapp_homePage_banner_queryBannerList(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 查询首页banner图列表
        """
        rs = ea_app.test_api_78dk_clientapp_homePage_banner_queryBannerList()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_002_api_78dk_clientapp_homePage_homeOrder_queryOrderState(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 订单状态
        """
        rs = ea_app.test_api_78dk_clientapp_homePage_homeOrder_queryOrderState()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "authState")
        ass.verityContain(json.loads(rs)['data'], "orderState")

    # def test_003_api_78dk_clientapp_tools_loanCalc_initPage(self):
    #     """
    #       Time       :2019-04-25
    #       author     : 罗林
    #       desc       : 页面初始化 （作废）
    #     """
    #     rs = ea_app.test_api_78dk_clientapp_tools_loanCalc_initPage()
    #     ass.verity(json.loads(rs)['code'], "10000")
    #     # ass.verityContain(json.loads(rs)['data'], "periodList")
    #     # ass.verityContain(json.loads(rs)['data'], "periodList")
    #     # ass.verityContain(json.loads(rs)['data'], "replayTypeList")

    def test_004_api_78dk_clientapp_tools_loanCalc_calc(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 贷款计算
        """
        product_id = eq.get_info('product_detail', 'product_detail_uuid')[0]
        rs = ea_app.test_api_78dk_clientapp_tools_loanCalc_calc(loanamount=10000, loanterm=3,
                                                                productdetailuuid=product_id)
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "billList")
        # ass.verityContain(json.loads(rs)['data'], "rateOfMonth")
        # ass.verityContain(json.loads(rs)['data'], "totalAmount")

    def test_005_api_78dk_clientapp_tools_carEva_carTypeEva(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车型估价
        """
        rs = ea_app.test_api_78dk_clientapp_tools_carEva_carTypeEva(
            carcode=car_code, citycode=510100, miles=10000, oncardate=tf.string_toTimestamp_13('2015-04-25 00:00:00'),
            brandid=1, modelname='奥迪A3')
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "brandPic")
        # ass.verityContain(json.loads(rs)['data'], "maxLoan")
        # ass.verityContain(json.loads(rs)['data'], "modelName")

    def test_006_api_78dk_clientapp_tools_carEva_vinEva(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : VIN估价
        """
        rs = ea_app.test_api_78dk_clientapp_tools_carEva_vinEva(
            citycode=510100, miles=10000, oncardate=tf.string_toTimestamp_13('2015-04-25 00:00:00'), vincode=vincode)
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "brandPic")
        # ass.verityContain(json.loads(rs)['data'], "maxLoan")
        # ass.verityContain(json.loads(rs)['data'], "modelName")
