#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-23 下午 4:42
@Author     : 罗林
@File       : testEasyloan_web_001_risk.py
@desc       : 风控审核 模块测试用例  设计数据库表 loan_finance ， loan_order ， process_examine ， process_exchange
"""

import json

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_webAction as ew


class testEasyloan_web_001_risk(TestBaseCase):
    def test_001_api_78dk_web_risk_addSecondProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :信审-保存处理结果
        """
        loan_order_uuid, order_main_state, order_sub_state, state = eq.get_info(
            'loan_order', 'loan_order_uuid,order_main_state,order_sub_state,state')
        eq.update_order(loan_order_uuid, 'order_main_state="SHJDPS02"')
        rs = ew.test_api_78dk_web_risk_addSecondProcess(examineresult=1000, examineamount='项目风险等级',
                                                        loanorderuuid=loan_order_uuid, examineinfo='SHJDXS01',
                                                        remark='')
        ass.verity(json.loads(rs)['code'], "10000")
        eq.update_order(loan_order_uuid, 'order_main_state="{}"'.format(order_main_state),
                        'order_sub_state="{}"'.format(order_sub_state), 'state="{}"'.format(state))
        eq.delete_info('loan_finance', 'loan_order_uuid="{}"'.format(loan_order_uuid))
        eq.delete_info('process_examine', 'loan_order_uuid="{}"'.format(loan_order_uuid))

    def test_002_api_78dk_web_risk_querySecondProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :信审-分页查询搜索查询v1.0.4
        """
        rs = ew.test_api_78dk_web_risk_querySecondProcess(username='', mobile='', pagesize=10, currentpage=1,
                                                          storename='')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "totalCount")

    def test_003_api_78dk_web_risk_updateSecondProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :信审-返回审核金额
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid', )[0]
        rs = ew.test_api_78dk_web_risk_updateSecondProcess(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "advanceFee")

    def test_004_api_78dk_web_risk_queryTrial(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :我的已审-分页查询v1.0.4
        """
        rs = ew.test_api_78dk_web_risk_queryTrial(pagesize=10, mobile='', storename='', username='', currentpage=1,
                                                  orderstate='')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "currentPage")
        ass.verityContain(json.loads(rs)['data'], "dataList")

    def test_005_api_78dk_web_risk_addFinalProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :终审-保存处理结果
        """
        loan_order_uuid, order_main_state, order_sub_state, state = eq.get_info(
            'loan_order', 'loan_order_uuid,order_main_state,order_sub_state,state')
        eq.update_order(loan_order_uuid, 'order_main_state="SHJDXS03"')
        rs = ew.test_api_78dk_web_risk_addFinalProcess(examineresult='SHJDZS01', loanorderuuid=loan_order_uuid,
                                                       remark='')
        ass.verity(json.loads(rs)['code'], "10000")
        eq.delete_info('loan_finance', 'loan_order_uuid="{}"'.format(loan_order_uuid))
        eq.delete_info('process_examine', 'loan_order_uuid="{}"'.format(loan_order_uuid))

    def test_006_api_78dk_web_risk_queryFinalProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :终审-分页查询搜索查询v1.0.4
        """
        rs = ew.test_api_78dk_web_risk_queryFinalProcess(pagesize=10, mobile='', storename='', username='',
                                                         currentpage=1)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "orderByKeys")
        ass.verityContain(json.loads(rs)['data'], "orderByDesc")

    def test_007_api_78dk_web_risk_addFirstProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :评审-保存处理结果
        """
        loan_order_uuid, order_main_state, order_sub_state, state = eq.get_info(
            'loan_order', 'loan_order_uuid,order_main_state,order_sub_state,state')
        eq.update_order(loan_order_uuid, 'order_main_state="LZJDKF02"')
        rs = ew.test_api_78dk_web_risk_addFirstProcess(examineresult='SHJDPS01', examineamount=1000, examineinfo=1001,
                                                       loanorderuuid=loan_order_uuid, remark='')
        ass.verity(json.loads(rs)['code'], "10000")
        eq.delete_info('loan_finance', 'loan_order_uuid="{}"'.format(loan_order_uuid))
        eq.delete_info('process_examine', 'loan_order_uuid="{}"'.format(loan_order_uuid))

    def test_008_api_78dk_web_risk_queryFirstProcess(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :评审-分页查询搜索查询
        """
        rs = ew.test_api_78dk_web_risk_queryFirstProcess(storename='', mobile='', username='', currentpage=1,
                                                         pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "orderByKeys")
        ass.verityContain(json.loads(rs)['data'], "orderByDesc")

    def test_009_api_78dk_web_risk_addRemark(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :保存备注-v1.0.3
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        remarkloanorder = [{"loanOrderUuid": loan_order_uuid, "remark": 'api-test保存备注', "type": '0'}]
        rs = ew.test_api_78dk_web_risk_addRemark(remarkloanorder)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_010_api_78dk_web_risk_delRemark(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :删除备注-v1.0.3
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_delRemark(type='0', uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_011_api_78dk_web_risk_addWeft(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :保存经纬度-v1.0.3
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_addWeft(uuid=loan_order_uuid, type='0', longitude='104.0710005358',
                                               latitude='30.5403921022')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_012_api_78dk_web_sum_getReportBoolean(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :判断报告是否有数据(v1.0.4)
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_sum_getReportBoolean(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dt")
        ass.verityContain(json.loads(rs)['data'], "carr")
        ass.verityContain(json.loads(rs)['data'], "taobao")
        ass.verityContain(json.loads(rs)['data'], "rf")
        ass.verityContain(json.loads(rs)['data'], "jingdong")
        ass.verityContain(json.loads(rs)['data'], "apliy")

    def test_013_api_78dk_web_risk_getFdd(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :合同-查看
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getFdd(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "signUrl")

    def test_014_api_78dk_web_sum_getReport(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :查询报告数据（v1.0.4）
        """
        rs = ew.test_api_78dk_web_sum_getReport(ictype='0', authortoken='', userid='')
        ass.verity(json.loads(rs)['code'], "20000")

    def test_015_api_78dk_web_risk_getKey(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :获取key
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getKey(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "carCode")
        ass.verityContain(json.loads(rs)['data'], "key")

    def test_016_api_78dk_web_risk_getMailList(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :获取通讯录-v1.0.3
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getMailList(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "singlePhone")
        ass.verityContain(json.loads(rs)['data'], "type")

    def test_017_api_78dk_web_risk_queryLoanClientLists(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :获提交人下拉列表
        """
        rs = ew.test_api_78dk_web_risk_queryLoanClientLists()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "name")
        # ass.verityContain(json.loads(rs)['data'], "code")
        # ass.verityContain(json.loads(rs)['data'], "desc")

    def test_018_api_78dk_web_risk_getRiskStrategyResult(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :风控机审列表-v1.0.4
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getRiskStrategyResult(loanorderuuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "list")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "result")

    def test_019_api_78dk_web_risk_getRiskScoreResult(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :风控评分列表-v1.0.4
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getRiskScoreResult(loanorderuuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "list")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "result")
        # ass.verityContain(json.loads(rs)['data'], "listData")
        # ass.verityContain(json.loads(rs)['data'], "scoreResult")
        # ass.verityContain(json.loads(rs)['data'], "typeName")

    def test_020_api_78dk_web_risk_getDetail(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :风控详情页面查看-v1.0.4
        """
        loan_order_uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_risk_getDetail(uuid=loan_order_uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "ClientContact")
        ass.verityContain(json.loads(rs)['data'], "Vehicle")
        ass.verityContain(json.loads(rs)['data'], "vehicleInspect")
        ass.verityContain(json.loads(rs)['data'], "clientBase")
        ass.verityContain(json.loads(rs)['data'], "clientWork")
        ass.verityContain(json.loads(rs)['data'], "clientPersonal")
        ass.verityContain(json.loads(rs)['data'], "loanInfoFile")
        ass.verityContain(json.loads(rs)['data'], "loanOrder")
        ass.verityContain(json.loads(rs)['data'], "remark")
        ass.verityContain(json.loads(rs)['data'], "vehicleFile")
