#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-11 上午 11:32
@Author     : 罗林
@File       : test_016_app_process_SpecialInfo.py
@desc       :   进件模块自动化测试用例(特别信息、确认分期、法大大签约)
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from hmpt.query import xqkj_query
from hmpt.testAction import AppAction
from hmpt.testAction import loginAction
from hmpt.testAction import specialAction

fake = Factory().create('zh_CN')


class test_016_app_process_SpecialInfo(TestBaseCase):
    def test_001_api_78dk_app_process_saveContractImages(self):
        """
        保存影像资料
        :return:
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        contract_uuid1 = xqkj_query.get_contract_uuid_for_user(loginAction.global_dict.get('user_uuid'))
        image_keys = xqkj_query.get_tbl_infos('Tbl_ContractImage', '`key`', 'contract_uuid="{}"'.format(contract_uuid1))
        contractimagelist = [{"key": image_key} for image_key in image_keys]
        res = json.loads(AppAction.test_api_78dk_app_process_saveContractImages(
            contractimagelist=contractimagelist))
        Assertion.verity(res['code'], '10000')

    def test_002_api_78dk_app_process_saveContractImages_none(self):
        """
        保存影像资料
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveContractImages(
            contractimagelist=''))
        Assertion.verity(res['code'], '20000')

    def test_003_api_78dk_app_process_getContractImages(self):
        """
        查询影像资料（当前订单）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getContractImages(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data'], 'imageUrl')
        # Assertion.verityContain(res['data'], 'key')

    def test_004_api_78dk_app_process_getSpecialInfo(self):
        """
        查询特别信息认证进度
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getSpecialInfo())
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'jdAuthStatus')
        Assertion.verityContain(res['data'], 'tbAuthStatus')
        Assertion.verityContain(res['data'], 'yysAuthStatus')

    def test_005_api_78dk_app_process_mxCallback(self):
        """
        （回调接口）接口中心-魔蝎
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_mxCallback(''))
        Assertion.verity(res['code'], '20000')

    def test_006_api_78dk_app_process_submitApply(self):
        """
        提交申请
        :return:
        """
        global productDetailConfigUuid
        productDetailConfigUuid = loginAction.global_dict.get('productDetailConfigUuid')
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=10, productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '10000')

    def test_007_api_78dk_app_process_submitApply_amount_none(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount='', productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '10000')

    def test_008_api_78dk_app_process_submitApply_amount_error(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount='abc', productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_app_process_submitApply_amount_max(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=999999999999, productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_010_api_78dk_app_process_submitApply_amount_min(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=0.0000000001, productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_app_process_submitApply_amount_minus(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=-10000, productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_012_api_78dk_app_process_submitApply_amount_zero(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=0, productdetailconfiguuid=productDetailConfigUuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_app_process_submitApply_uuid_none(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=10000, productdetailconfiguuid='', repaymentdate=''))
        Assertion.verity(res['code'], '10000')

    def test_014_api_78dk_app_process_submitApply_uuid_error(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=10000, productdetailconfiguuid='abc', repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_015_api_78dk_app_process_submitApply_uuid_not_exits(self):
        """
        提交申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_submitApply(
            loanamount=10000, productdetailconfiguuid=fake.ean8(), repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_016_api_78dk_app_process_repayPlanCalculator_true(self):
        """
        还款计划试算
        :return:
        """
        global productDetailUuid, store_uuid
        productDetailUuid = loginAction.global_dict.get('productDetailUuid')
        store_uuid = loginAction.global_dict.get('store_uuid')
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='true', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'handlingFee')
        Assertion.verityContain(res['data'], 'lastPayDate')
        Assertion.verityContain(res['data'], 'number')
        Assertion.verityContain(res['data'], 'principal')
        Assertion.verityContain(res['data'], 'totalHandlingFee')
        Assertion.verityContain(res['data'], 'totalMoney')
        Assertion.verityContain(res['data'], 'totalPrincipal')

    def test_017_api_78dk_app_process_repayPlanCalculator_false(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='false', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'handlingFee')
        Assertion.verityContain(res['data'], 'lastPayDate')
        Assertion.verityContain(res['data'], 'number')
        Assertion.verityContain(res['data'], 'principal')
        Assertion.verityContain(res['data'], 'totalHandlingFee')
        Assertion.verityContain(res['data'], 'totalMoney')
        Assertion.verityContain(res['data'], 'totalPrincipal')

    def test_018_api_78dk_app_process_repayPlanCalculator_isdiscount_none(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '10000')

    def test_019_api_78dk_app_process_repayPlanCalculator_isdiscount_error(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='abc', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_020_api_78dk_app_process_repayPlanCalculator_loanamount_none(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount='', productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_021_api_78dk_app_process_repayPlanCalculator_loanamount_error(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount='abc', productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_022_api_78dk_app_process_repayPlanCalculator_loanamount_zero(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=0, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_023_api_78dk_app_process_repayPlanCalculator_loanamount_minus(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=-10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_024_api_78dk_app_process_repayPlanCalculator_loanamount_max(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=999999999999, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额太大！')

    @unittest.skip("只对0-100000000做限制，不考虑0.0000001")
    def test_025_api_78dk_app_process_repayPlanCalculator_loanamount_min(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=0.00000000001, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '分期金额必须大于1！')

    def test_026_api_78dk_app_process_repayPlanCalculator_configuuid_none(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid='',
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_027_api_78dk_app_process_repayPlanCalculator_configuuid_error(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid='abc',
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_028_api_78dk_app_process_repayPlanCalculator_configuuid_not_exits(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=fake.ean8(),
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_029_api_78dk_app_process_repayPlanCalculator_detailuuid_none(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid='', storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_030_api_78dk_app_process_repayPlanCalculator_detailuuid_error(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid='abc', storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_031_api_78dk_app_process_repayPlanCalculator_detailuuid_not_exits(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=fake.ean8(), storeuuid=store_uuid, repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_032_api_78dk_app_process_repayPlanCalculator_storeuuid_none(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid='', repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_033_api_78dk_app_process_repayPlanCalculator_storeuuid_error(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid='abc', repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    def test_034_api_78dk_app_process_repayPlanCalculator_storeuuid_not_exits(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount=True, loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=fake.ean8(), repaymentdate=''))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('去掉法大大')
    def test_035_api_78dk_app_process_getSignResult(self):
        """
        查询法大大签约结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getSignResult())
        Assertion.verity(res['code'], '10000')

    @unittest.skip('去掉法大大')
    def test_036_api_78dk_app_process_getSignUrl(self):
        """
        获取法大大签约地址
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getSignUrl())
        Assertion.verity(res['code'], 'S0003')
        # Assertion.verityContain(res['data'], 'signUrl')

    def test_037_test_api_78dk_app_process_saveContractSupplementImages(self):
        """
        保存补充资料（新）
        :return:
        """
        global contract_uuid
        contract_uuid = xqkj_query.get_contract_uuid_for_user(loginAction.get_user_uuid())
        loginAction.global_dict.set(contract_uuid=contract_uuid)
        res = json.loads(AppAction.test_api_78dk_app_process_saveContractSupplementImages(
            datalist=[], contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_038_test_api_78dk_app_process_getContractSupplementImages(self):
        """
        查询补充资料（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getContractSupplementImages(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_039_test_api_78dk_app_process_verifySchool(self):
        """
        学信网认证(新)
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_verifySchool(
            account='', password='', school='', vcode='', taskid=''))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('废弃')
    def test_040_api_78dk_app_process_repayPlanCalculator_true(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='true', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate='2019-11-25'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'handlingFee')
        Assertion.verityContain(res['data'], 'lastPayDate')
        Assertion.verityContain(res['data'], 'number')
        Assertion.verityContain(res['data'], 'principal')
        Assertion.verityContain(res['data'], 'totalHandlingFee')
        Assertion.verityContain(res['data'], 'totalMoney')
        Assertion.verityContain(res['data'], 'totalPrincipal')

    @unittest.skip('废弃')
    def test_041_api_78dk_app_process_repayPlanCalculator_false(self):
        """
        还款计划试算
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_repayPlanCalculator(
            isdiscount='false', loanamount=10000, productdetailconfiguuid=productDetailConfigUuid,
            productdetailuuid=productDetailUuid, storeuuid=store_uuid, repaymentdate='2019-11-25'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'handlingFee')
        Assertion.verityContain(res['data'], 'lastPayDate')
        Assertion.verityContain(res['data'], 'number')
        Assertion.verityContain(res['data'], 'principal')
        Assertion.verityContain(res['data'], 'totalHandlingFee')
        Assertion.verityContain(res['data'], 'totalMoney')
        Assertion.verityContain(res['data'], 'totalPrincipal')

    def test_042_api_78dk_app_process_centerCallback(self):
        """
        （回调接口）爬虫接口中心回调_正常
        :return:
        """
        AppAction.test_api_78dk_app_process_centerCallback(data='', message='', result='', task_id='',
                                                           timestamp='', type='', user_id='')

    def test_043_api_78dk_app_process_authOrization_true(self):
        """
        （回调接口）爬虫接口中心授权_正常
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_authOrization(usermobile='13018204373'))
        Assertion.verityContain(res['data'], 'loginId')
        Assertion.verityContain(res['data'], 'phoneType')
        Assertion.verityContain(res['data'], 'validateType')
        Assertion.verity(res['data']['phoneType'], 'unicom')
        Assertion.verity(res['code'], '10000')

    def test_044_api_78dk_app_process_authOrization_none(self):
        """
        （回调接口）爬虫接口中心授权_空
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_authOrization(usermobile=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '请确认请求参数！')

    def test_045_api_78dk_app_process_authOrization_error(self):
        """
        （回调接口）爬虫接口中心授权:错误usermobile
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_authOrization(usermobile="183"))
        Assertion.verityContain(res['data'], 'loginId')
        Assertion.verityContain(res['data'], 'phoneType')
        Assertion.verityContain(res['data'], 'validateType')
        Assertion.verity(res['code'], '10000')

    def test_046_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求data为空
        :return:
        """
        AppAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='success',
                                                               task_id='123', timestamp='1586760300', type='1',
                                                               user_id='13')

    def test_047_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求data为错误格式
        :return:
        """
        AppAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='success',
                                                               task_id='123', timestamp='1586760300',
                                                               type='1', user_id='13')

    def test_048_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求user_id不存在业务系统或没有业务
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='success', task_id='123',
                                                               timestamp='1586760300', type='1', user_id='8888'))
        Assertion.verity(res['code'], '20000')

    def test_049_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求user_id为空
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='success', task_id='123',
                                                               timestamp='1586760300', type='1', user_id=''))
        Assertion.verity(res['code'], '20000')

    def test_050_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求result为失败
        :return:
        """
        specialAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='fail', task_id='123',
                                                                   timestamp='1586760300', type='1', user_id='13')

    def test_051_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求result为等待
        :return:
        """
        specialAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='waiting',
                                                                   task_id='123', timestamp='1586760300', type='1',
                                                                   user_id='13')

    def test_052_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求type为taobao淘宝
        :return:
        """
        specialAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='waiting',
                                                               task_id='123', timestamp='1586760300', type='2',
                                                               user_id='13')

    def test_053_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求type为carrier运营商
        :return:
        """
        specialAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='waiting',
                                                               task_id='123', timestamp='1586760300', type='3',
                                                               user_id='13')

    def test_054_api_78dk_app_process_centerCallback_(self):
        """
        （回调接口）爬虫接口中心回调_请求type为xxw学信网
        :return:
        """
        res = specialAction.test_api_78dk_app_process_centerCallback(data='', message='阿萨德', result='waiting',
                                                                     task_id='123', timestamp='1586760300', type='4',
                                                                     user_id='13')
