#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-10 下午 4:37
@Author     : 罗林
@File       : test_011_app_process_Product.py
@desc       : 进件模块自动化测试用例(选择商品、分期详情)
"""
import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData as MD
from ymjry.testAction import AppAction
from ymjry.testAction import loginAction

fake = Factory().create('zh_CN')
gpsaddress = '四川省成都市高新区软件园B区6栋3楼'
gpscity = '成都市'
gpsdetail = '软件园B区6栋3楼'
gpsinfolat = '30.5450700000'
gpsinfolon = '104.0714500000'
gpsprovince = '四川省'
gpsregion = '蒲江县'


class test_011_app_process_Product(TestBaseCase):
    def test_001_api_78dk_app_process_getStoreAndProduct(self):
        """
        根据门店uuid查询门店商品
        :return:
        """
        global storeuuid
        storeuuid = loginAction.global_dict.get('store_uuid')
        res = json.loads(AppAction.test_api_78dk_app_process_getStoreAndProduct(isdiscount=True, storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data']['productList'], 'maxQuota')
        # Assertion.verityContain(res['data']['productList'], 'minQuota')
        # Assertion.verityContain(res['data']['productList'], 'name')
        # Assertion.verityContain(res['data']['productList'], 'productDetailUuid')
        Assertion.verityContain(res['data']['store'], 'businessAddress')
        Assertion.verityContain(res['data']['store'], 'storeName')
        Assertion.verityContain(res['data']['store'], 'storeUuid')

    def test_002_api_78dk_app_process_getStoreAndProduct_false(self):
        """
        根据门店uuid查询门店商品
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getStoreAndProduct(isdiscount=False, storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data']['productList'], 'maxQuota')
        # Assertion.verityContain(res['data']['productList'], 'minQuota')
        # Assertion.verityContain(res['data']['productList'], 'name')
        # Assertion.verityContain(res['data']['productList'], 'productDetailUuid')
        Assertion.verityContain(res['data']['store'], 'businessAddress')
        Assertion.verityContain(res['data']['store'], 'storeName')
        Assertion.verityContain(res['data']['store'], 'storeUuid')

    def test_003_api_78dk_app_process_getStoreAndProduct_isdiscount_none(self):
        """
        根据门店uuid查询门店商品
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getStoreAndProduct(isdiscount='', storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')

    def test_004_api_78dk_app_process_getStoreAndProduct_storeuuid_none(self):
        """
        根据门店uuid查询门店商品
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getStoreAndProduct(isdiscount='', storeuuid=''))
        Assertion.verity(res['code'], '20000')

    def test_005_api_78dk_app_process_getStoreAndProduct_storeuuid_not_exits(self):
        """
        根据门店uuid查询门店商品
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getStoreAndProduct(isdiscount='', storeuuid=fake.ean8()))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '没有此门店信息!')

    def test_006_api_78dk_app_process_getProductDetail(self):
        """
        根据产品uuid查询分期详情
        :return:
        """
        global productdetailuuid
        productdetailuuid = loginAction.global_dict.get('productDetailUuid')
        res = json.loads(AppAction.test_api_78dk_app_process_getProductDetail(productdetailuuid=productdetailuuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList'], 'id')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList'], 'itemCode')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList']['sonList'], 'id')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList']['sonList'], 'itemCode')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList']['sonList'], 'typeName')
        # Assertion.verityContain(res['data']['incomingPartsTemplateList'], 'typeName')
        # Assertion.verityContain(res['data'], 'maxQuota')
        # Assertion.verityContain(res['data'], 'minQuota')
        # Assertion.verityContain(res['data'], 'name')
        # Assertion.verityContain(res['data'], 'productDetailUuid')
        # Assertion.verityContain(res['data']['productDetailConfigs'], 'period')
        # Assertion.verityContain(res['data']['productDetailConfigs'], 'productDetailConfigUuid')
        # Assertion.verityContain(res['data']['productDetailConfigs'], 'rate')

    def test_007_api_78dk_app_process_getProductDetail_none(self):
        """
        根据产品uuid查询分期详情
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getProductDetail(productdetailuuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '产品uuid为空！')

    def test_008_api_78dk_app_process_getProductDetail_not_exits(self):
        """
        根据产品uuid查询分期详情
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getProductDetail(productdetailuuid=fake.ean8()))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无此产品！')

    def test_018_api_78dk_app_process_saveUserPlaceOrderGps(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_019_api_78dk_app_process_saveUserPlaceOrderGps_gpsaddress_is_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsaddress为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress='', gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '完整地址为空！')

    def test_020_api_78dk_app_process_saveUserPlaceOrderGps_gpscity_is_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpscity为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity='',
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_021_api_78dk_app_process_saveUserPlaceOrderGps_gpsdetail_is_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsdetail为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail='', gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince, gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_022_api_78dk_app_process_saveUserPlaceOrderGps_fat_lon_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsinfolat,gpsinfolat为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat='', gpsinfolon='', gpsprovince=gpsprovince, gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '维度为空！')

    def test_023_api_78dk_app_process_saveUserPlaceOrderGps_fat_lon_zero(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsinfolat,gpsinfolat错误
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=0, gpsinfolon=0, gpsprovince=gpsprovince, gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_024_api_78dk_app_process_saveUserPlaceOrderGps_fat_lon_error(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsinfolat,gpsinfolon格式不正确
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat='113.962145', gpsinfolon='22.982667', gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_025_api_78dk_app_process_saveUserPlaceOrderGps_gpsprovince_is_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsprovince为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat='113.962145', gpsinfolon='22.982667', gpsprovince='', gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_026_api_78dk_app_process_saveUserPlaceOrderGps_gpsregion_is_null(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsregion为空
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat='113.962145', gpsinfolon='22.982667', gpsprovince=gpsprovince, gpsregion='')
        Assertion.verity(json.loads(res)['code'], '10000')
        global placeordergpsuuid
        placeordergpsuuid = json.loads(res)['data']
        # Assertion.verity(json.loads(res)['msg'], 'success')

    def test_027_api_78dk_app_process_saveUserPlaceOrderGps_gpsaddress_is_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsaddress超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=MD.words_en(256), gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '完整地址太长！')

    def test_028_api_78dk_app_process_saveUserPlaceOrderGps_gpscity_is_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpscity超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=MD.words_en(256),
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统繁忙，请稍候再试')

    def test_029_api_78dk_app_process_saveUserPlaceOrderGps_gpsdetail_is_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsdetail超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=MD.words_en(256), gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统繁忙，请稍候再试')

    def test_030_api_78dk_app_process_saveUserPlaceOrderGps_lat_lon_is_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsinfolat,gpsinfolon超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=MD.words_en(256), gpsinfolon=MD.words_en(256), gpsprovince=gpsprovince,
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统繁忙，请稍候再试')

    def test_031_api_78dk_app_process_saveUserPlaceOrderGps_gpsprovince_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsprovince超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=MD.words_en(256),
            gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统繁忙，请稍候再试')

    def test_032_api_78dk_app_process_saveUserPlaceOrderGps_gpsregion_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,gpsregion超长
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince=gpsprovince,
            gpsregion=MD.words_en(256))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统繁忙，请稍候再试')

    def test_033_api_78dk_app_process_saveUserPlaceOrderGps_gpsregion_overlong(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 保存位置信息V1.4.0,s省市区不对应
        """
        res = AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
            gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsinfolon=gpsinfolon, gpsprovince='北京', gpsregion=gpsregion)
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['msg'], '失败')

    def test_034_api_78dk_app_process_createContract_productdetailconfiguuid_none(self):
        """
        创建订单
        :return:
        """
        # user_uuid = loginAction.get_user_uuid()
        global productDetailConfigUuid,saUuid
        productDetailConfigUuid = loginAction.global_dict.get('productDetailConfigUuid')
        saUuid = loginAction.global_dict.get('saUuid')
        # placeordergpsuuid = xqkj_query.get_info("Tbl_UserPlaceOrderGps", "place_order_gps_uuid",
        #                                         "user_uuid='{}'".format(user_uuid))[-1]
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid='',
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '产品期数为空！')

    def test_035_api_78dk_app_process_createContract_false(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount='false',
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verity(res['msg'], '成功')

    def test_036_api_78dk_app_process_createContract_amount_none(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount='', isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额必须大于0！')

    def test_037_api_78dk_app_process_createContract_amount_max(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=99999999999999, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额太大！')

    def test_038_api_78dk_app_process_createContract_amount_not_int(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount='abc', isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统繁忙，请稍候再试')

    def test_039_api_78dk_app_process_createContract_productdetailuuid_none(self):
        """
        创建订单
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True, productdetailuuid='',
                storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
                placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '产品为空！')

    def test_040_api_78dk_app_process_createContract_productdetailuuid_not_exits(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True,
            productdetailuuid=fake.ean8(), storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '产品没有关联的资金包！')

    def test_041_api_78dk_app_process_createContract_storeuuid_none(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid='', productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '门店为空！')

    def test_042_api_78dk_app_process_createContract_storeuuid_not_exits(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=fake.ean8(), productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '门店没有关联的商户！')

    def test_043_api_78dk_app_process_createContract_productdetailconfiguuid_not_exits(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=fake.ean8(),
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '没有分期信息！')

    def test_044_api_78dk_app_process_createContract(self):
        """
        创建订单
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_createContract(loanamount=10000, isdiscount='true',
            productdetailuuid=productdetailuuid, storeuuid=storeuuid, productdetailconfiguuid=productDetailConfigUuid,
            placeordergpsuuid=placeordergpsuuid, projectname='', selectrepaydiscount='select_repay_discount_yes', sauuid=saUuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verity(res['msg'], '成功')

    def test_045_api_78dk_app_process_loanCalculatorV2_amount_none(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount='', isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')

    def test_046_api_78dk_app_process_loanCalculatorV2_amount_error(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount='abc', isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')

    def test_047_api_78dk_app_process_loanCalculatorV2_amount_not_exits(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=fake.ean8(), isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')

    def test_048_api_78dk_app_process_loanCalculatorV2_amount_max(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=999999999999, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('只验证1-100000000')
    def test_049_api_78dk_app_process_loanCalculatorV2_amount_min(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=0.0000000001, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额必须大于1！')

    def test_050_api_78dk_app_process_loanCalculatorV2_amount_zero(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=0, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额必须大于0！')

    def test_051_api_78dk_app_process_loanCalculatorV2_amount_minus(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=-10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额必须大于0！')

    def test_052_api_78dk_app_process_loanCalculatorV2_detailuuid_none(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid='', storeuuid=storeuuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '产品期数为空！')

    def test_053_api_78dk_app_process_loanCalculatorV2_detailuuid_error(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid='abc', storeuuid=storeuuid))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无此产品！')

    def test_054_api_78dk_app_process_loanCalculatorV2_detailuuid_not_exits(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid=fake.ean8(), storeuuid=storeuuid))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '查无此产品！')

    def test_055_api_78dk_app_process_loanCalculatorV2_storeuuid_none(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '商户为空！')

    def test_040_api_78dk_app_process_loanCalculatorV2_storeuuid_error(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid='abc'))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '属性复制错误')

    def test_056_api_78dk_app_process_loanCalculatorV2_storeuuid_not_exits(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=fake.ean8()))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '属性复制错误')

    def test_057_api_78dk_app_process_loanCalculatorV2_true(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=True,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')

    def test_058_api_78dk_app_process_loanCalculatorV2_false(self):
        """
        贷款试算（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_loanCalculatorV2(loanamount=10000, isdiscount=False,
            productdetailuuid=productdetailuuid, storeuuid=storeuuid))
        Assertion.verity(res['code'], '10000')

    def test_059_api_78dk_app_process_saveUserPlaceOrderGps(self):
        """
        保存用户下单位置信息（新）
        :return:
        """

    res = json.loads(AppAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsaddress=gpsaddress, gpscity=gpscity,
        gpsregion=gpsregion, gpsdetail=gpsdetail, gpsinfolat=gpsinfolat, gpsprovince=gpsprovince,
        gpsinfolon=gpsinfolon))
    Assertion.verity(res['code'], '10000')

    def test_060_api_78dk_app_process_getCodeUrl(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 获取商户二维码前缀V1.4.0
        """
        res = AppAction.test_api_78dk_app_process_getCodeUrl()
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_061_api_78dk_app_process_querySaList(self):
        """
        Time       :2019-08-14
        author     : 闫红
        desc       : 获取所有SA在职人员v1.0.3新增
        """
        res = AppAction.test_api_78dk_app_process_querySaList()
        Assertion.verity(json.loads(res)['code'], '10000')
