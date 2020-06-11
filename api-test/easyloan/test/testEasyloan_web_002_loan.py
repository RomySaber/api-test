#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-23 下午 5:01
@Author     : 罗林
@File       : testEasyloan_web_002_loan.py
@desc       : 业务管理接口测试用例
"""

import json

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_webAction as ew


class testEasyloan_web_002_loan(TestBaseCase):
    def test_001_api_78dk_web_loan_info_addLoanBusinessPerson(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :保存订单业务员
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_info_addLoanBusinessPerson(loanuuid=loanuuid, businessperson=businessperson)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'order_main_state="{}"'.format(state))

    def test_002_api_78dk_web_loan_common_refuseLoanOrder(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :取消订单
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_common_refuseLoanOrder(loanuuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'order_main_state="{}"'.format(state))

    def test_003_api_78dk_web_loan_common_acceptLoanOrder(self):
        """
          Time       :2019-04-23
          author     : 罗林
          desc       :受理订单
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_common_acceptLoanOrder(loanuuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'order_main_state="{}"'.format(state))

    def test_004_api_78dk_web_loan_common_commitLoanOrder(self):
        """
          Time       :2019-04-23
          author     : 罗林
          desc       :提交订单
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_common_commitLoanOrder(loanuuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'order_main_state="{}"'.format(state))

    def test_005_api_78dk_web_loan_common_returnLoanOrder(self):
        """
          Time       :2019-04-23
          author     : 罗林
          desc       :退回订单
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_common_returnLoanOrder(loanuuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'order_main_state="{}"'.format(state))

    def test_006_api_78dk_web_loan_common_queryProcessStatusLists(self):
        """
          Time       :2019-04-23
          author     : 罗林
          desc       :获取业务状态列表
        """
        rs = ew.test_api_78dk_web_loan_common_queryProcessStatusLists()
        ass.verity(json.loads(rs)['code'], "10000")

    def test_007_api_78dk_web_loan_common_queryMerchantLists(self):
        """
          Time       :2019-04-23
          author     : 罗林
          desc       :获取商户下拉列表
        """
        rs = ew.test_api_78dk_web_loan_common_queryMerchantLists()
        ass.verity(json.loads(rs)['code'], "10000")

    def test_008_api_78dk_web_loan_common_queryStoreLists(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :根据商户获取门店下拉列表
        """
        rs = ew.test_api_78dk_web_loan_common_queryStoreLists(merchantuuid='FQBJ001')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_009_api_78dk_web_loan_base_queryLoanRequestLists(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :借款申请列表查询Page
        """
        rs = ew.test_api_78dk_web_loan_base_queryLoanRequestLists(pagesize=10, mobile='', username='', currentpage=1)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_010_api_78dk_web_loan_base_assignOtherStore(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :分配到其它门店
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        old_storeuuid = eq.get_info('loan_order', 'store_uuid', 'loan_order_uuid="{}"'.format(loanuuid))
        rs = ew.test_api_78dk_web_loan_base_assignOtherStore(storeuuid='68c5720686e942a5a990a04b5c4c0736',
                                                             loanuuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'store_uuid="{}"'.format(old_storeuuid))

    def test_011_api_78dk_web_loan_base_queryLoanOrderListsKF(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :借款订单列表查询Page
        """
        rs = ew.test_api_78dk_web_loan_base_queryLoanOrderListsKF(currentpage=1, username='', mobile='', pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_012_api_78dk_web_loan_info_updateSalesman(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :更新业务员
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_loan_info_updateSalesman(entryusername='', uuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loanuuid, 'user_name="{}"'.format(businessperson))

    def test_013_api_78dk_web_loan_base_queryLoanOrderListsPGS(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :借款订单列表查询Page
        """
        rs = ew.test_api_78dk_web_loan_base_queryLoanOrderListsPGS(pagesize=10, username='', mobile='', currentpage=1)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_014_api_78dk_web_risk_getPgsDetail(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :评估师、客服详情页面查看-v1.0.4
        """
        loanuuid, businessperson, state = eq.get_info('loan_order', 'loan_order_uuid,user_name,order_main_state')
        rs = ew.test_api_78dk_web_risk_getPgsDetail(uuid=loanuuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_015_api_78dk_web_loan_base_queryLoanOrderListsMDJL(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :借款订单列表查询Page
        """
        rs = ew.test_api_78dk_web_loan_base_queryLoanOrderListsMDJL(currentpage=1, commituseruuid='', mobile='',
                                                                    username='', pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_016_api_78dk_web_loan_common_getToken(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :获取token
        """
        rs = ew.test_api_78dk_web_loan_common_getToken()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], 'token')

    def test_017_api_78dk_web_loan_base_queryClientInfoLists(self):
        """
          Time       :2019-04-24
          author     : 罗林
          desc       :我的已办-分页查询
        """
        rs = ew.test_api_78dk_web_loan_base_queryClientInfoLists(currentpage=1, orderstate='', mobile='', pagesize=10,
                                                                 username='')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_018_api_78dk_web_loan_info_queryLoanCheckResultLists(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 历史意见列表查询Page
        """
        rs = ew.test_api_78dk_web_loan_info_queryLoanCheckResultLists(loanorderuuid='', currentpage=1, pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_019_api_78dk_web_loan_info_addLoanFileLists(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 签约资料保存   需要修改入参
        """
        rs = ew.test_api_78dk_web_loan_info_addLoanFileLists(loaninfofile=[])
        ass.verity(json.loads(rs)['code'], "20000")

    def test_020_api_78dk_web_loan_info_delLoanFile(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 签约资料删除   需要修改入参
        """
        rs = ew.test_api_78dk_web_loan_info_delLoanFile(loaninfofileuuidlist=[])
        ass.verity(json.loads(rs)['code'], "10000")

    def test_021_api_78dk_web_loan_info_vehicleInfoUpdate(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆信息保存、修改-v1.0.4   需要修改入参
        """
        rs = ew.test_api_78dk_web_loan_info_vehicleInfoUpdate(vehicleinspect=[], vehicleinfo=[])
        ass.verity(json.loads(rs)['code'], "20000")

    def test_022_api_78dk_web_loan_info_addVehicleProcedLists(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆手续保存   需要修改入参
        """
        rs = ew.test_api_78dk_web_loan_info_addVehicleProcedLists(vehiclefile=[])
        ass.verity(json.loads(rs)['code'], "10000")

    def test_023_api_78dk_web_loan_info_delVehicleProced(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆手续删除   需要修改入参
        """
        rs = ew.test_api_78dk_web_loan_info_delVehicleProced(vehiclelist=[])
        ass.verity(json.loads(rs)['code'], "10000")
