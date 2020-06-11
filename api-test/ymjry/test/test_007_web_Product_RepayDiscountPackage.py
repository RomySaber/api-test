#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020/02/11
@Author     : 罗林
@File       : test_007_web_Product_RepayDiscountPackage.py
@desc       :  产品管理模块-还款优惠包-自动化测试用例
"""

import json
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.testAction import WebAction
from ymjry.testAction import loginAction



num = 10
ne = -1
se = 'abc'
ze = 0
total = 'money_type_total_money'
remain = 'money_type_remain_principal'
show_y = 'show_state_yes'
show_n = 'show_state_no'


class test_007_web_Product_RepayDiscountPackage(TestBaseCase):
    def test_001_base_saveRepayDiscountPackage(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        global product_detail_uuid
        product_detail_uuid = loginAction.global_dict.get('productDetailUuid')
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_002_base_saveRepayDiscountPackage_delayrepaydays_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=ze, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_003_base_saveRepayDiscountPackage_delayrepaydays_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=ne, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '延期还款天数 不能为空!')

    def test_004_base_saveRepayDiscountPackage_delayrepaydays_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=se, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_005_base_saveRepayDiscountPackage_gtbreachcontractrate_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=ze, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_006_base_saveRepayDiscountPackage_gtbreachcontractrate_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=ne, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '大于xx天-违约费率 不能为空!')

    def test_007_base_saveRepayDiscountPackage_gtbreachcontractrate_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=se, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_008_base_saveRepayDiscountPackage_gtdays_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=ze, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_009_base_saveRepayDiscountPackage_gtdays_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=ne, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '大于xx天-提前结清天数 不能为空!')

    def test_010_base_saveRepayDiscountPackage_gtdays_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=se, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_011_base_saveRepayDiscountPackage(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=remain,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_012_base_saveRepayDiscountPackage(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=remain,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=remain,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_013_base_saveRepayDiscountPackage(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=remain,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=remain,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_n)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_014_base_saveRepayDiscountPackage_ltebreachcontractrate_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=ze, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_015_base_saveRepayDiscountPackage_ltebreachcontractrate_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=ne, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '小于等于xx天-违约费率 不能为空!')

    def test_016_base_saveRepayDiscountPackage_ltebreachcontractrate_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=se, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_017_base_saveRepayDiscountPackage_ltedays_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=ze, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_018_base_saveRepayDiscountPackage_ltedays_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=ne, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '小于等于xx天-提前结清天数 不能为空!')

    def test_019_base_saveRepayDiscountPackage_ltedays_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=se, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_020_base_saveRepayDiscountPackage_ltehandlingfeemonths_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=ze, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_021_base_saveRepayDiscountPackage_ltehandlingfeemonths_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=ne, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '小于等于xx天-收取利息月数 不能为空!')

    def test_022_base_saveRepayDiscountPackage_ltehandlingfeemonths_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=se, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_023_base_saveRepayDiscountPackage_productdetailuuid_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=ze, ltemoneytype=total,
            productdetailuuid=-1, repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '还款优惠包落库出错，产品uuid 在数据库找不到对应的产品记录!')

    def test_024_base_saveRepayDiscountPackage_productdetailuuid_null(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=ne, ltemoneytype=total,
            productdetailuuid='', repaydiscountprice=num,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品uuid不能为空!')

    def test_025_base_saveRepayDiscountPackage_repaydiscountprice_zero(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=ze,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_026_base_saveRepayDiscountPackage_repaydiscountprice_error(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=ne,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '还款优惠包价格 不能为空!')

    def test_027_base_saveRepayDiscountPackage_repaydiscountprice_str(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays=num, gtbreachcontractrate=num, gtdays=num, gtmoneytype=total,
            ltebreachcontractrate=num, ltedays=num, ltehandlingfeemonths=num, ltemoneytype=total,
            productdetailuuid=product_detail_uuid, repaydiscountprice=se,
            showstate=show_y)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_028_base_saveRepayDiscountPackage(self):
        """
        还款优惠包保存（新增，修改）-v1.0.2 新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveRepayDiscountPackage(
            delayrepaydays='', gtbreachcontractrate='', gtdays='', gtmoneytype='', ltebreachcontractrate='',
            ltedays='', ltehandlingfeemonths='', ltemoneytype='', productdetailuuid='', repaydiscountprice='',
            showstate='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verityContain(json.loads(res)['msg'], '不能为空')

    def test_029_base_getRepayDiscountPackage_error(self):
        """
        还款优惠包查询-v1.0.2版本新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_getRepayDiscountPackage(
            productdetailuuid=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '')

    def test_030_base_getRepayDiscountPackage_error(self):
        """
        还款优惠包查询-v1.0.2版本新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_getRepayDiscountPackage(
            productdetailuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品uuid不能为空!')

    def test_031_base_getRepayDiscountPackage_error(self):
        """
        还款优惠包查询-v1.0.2版本新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_getRepayDiscountPackage(
            productdetailuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
