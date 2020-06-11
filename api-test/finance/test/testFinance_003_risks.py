#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018-07-16 下午 4:32
@Author     : 罗林
@File       : testFinance.py
@desc       : 
"""

import json
import time

import datetime

from common.myCommon import Assertion as a
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import FinanceSql as fs
from finance.mysqlQuery import ManageSql as ms
from finance.testAction import FinanceAction as f
from common.myCommon import TimeFormat as tf
from finance.testSource import Api_Const as c


orgCode = ms.get_finance_db_id()
yesterday = datetime.date.today() - datetime.timedelta(days=1)
yesterday_start_time = time.mktime(time.strptime(str(yesterday), '%Y-%m-%d'))
nowdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
yesterdate= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(yesterday_start_time))


class testFinance(TestBaseCase):
    # 车辆编号
    car_id = ''
    # 风险点id
    risk_id = ''

    # 风险点
    def test_001_risk_getOrgs(self):
        # 获取组织机构
        r1 = json.loads(f.test_risk_getOrgs())
        a.verity(r1['data'][0]['name'], c.companyName, '断言org-name')
        a.verity(r1['data'][0]['orgCode'], orgCode, '断言org-name')

    def test_002_risk_getRules(self):
        # 获取报警规则
        r2 = json.loads(f.test_risk_getRules())
        a.verity(r2['data'][0]['name'], "出围栏报警", '断言name')
        a.verity(r2['data'][0]['value'], "OUT", '断言value')
        a.verity(r2['data'][1]['name'], "入围栏报警", '断言name')
        a.verity(r2['data'][1]['value'], "IN", '断言value')
        a.verity(r2['data'][2]['name'], "停留报警", '断言name')
        a.verity(r2['data'][2]['value'], "STAY", '断言value')

    def test_003_risk_getRiskType(self):
        # 获取风险点类型
        r3 = json.loads(f.test_risk_getRiskType())
        a.verity(r3['data'][0]['name'], "二押点", '断言name')
        a.verity(r3['data'][0]['value'], "PLEDEGREPEAT", '断言value')
        a.verity(r3['data'][1]['name'], "维修厂", '断言name')
        a.verity(r3['data'][1]['value'], "REPAIRSHOP", '断言value')
        a.verity(r3['data'][2]['name'], "其它", '断言name')
        a.verity(r3['data'][2]['value'], "OTHER", '断言value')

    def test_004_risk_save(self):
        # 新增风险点
        r4 = json.loads(f.test_risk_save(
            str({'address': '', 'coords': '104.077945,30.66153,100', 'gisType': 'CIRCLE', 'id': '',
                 'name': c.riskName, 'radius': '100', 'orgCode': orgCode, 'riskType': 'PLEDEGREPEAT',
                 'rules': [{'id': '', 'riskId': '', 'ruleType': 'OUT'},
                           {'id': '', 'riskId': '', 'ruleType': 'STAY', 'thresholdMax': c.risk_thresholdMax},
                           {'id': '', 'riskId': '', 'ruleType': 'IN'}], 'otherRemark': ''})))
        self.risk_id = fs.get_risk_id(c.riskName)
        a.verity(r4['data']['name'], c.riskName, '断言name')
        a.verity(r4['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r4['data']['riskType'], "PLEDEGREPEAT", '断言riskType')
        a.verity(r4['data']['gisType'], "CIRCLE", '断言gisType')
        a.verity(r4['data']['id'], self.risk_id, '断言id')
        a.verity(r4['data']['rules'][0]['id'], fs.get_rule_id('OUT', self.risk_id), '断言rules-id')
        a.verity(r4['data']['rules'][0]['ruleType'], "OUT", '断言ruleType')
        a.verity(r4['data']['rules'][1]['id'], fs.get_rule_id('STAY', self.risk_id), '断言rules-id')
        a.verity(r4['data']['rules'][1]['ruleType'], "STAY", '断言ruleType')
        a.verity(r4['data']['rules'][1]['thresholdMax'], c.risk_thresholdMax, '断言thresholdMax')
        a.verity(r4['data']['rules'][2]['id'], fs.get_rule_id('IN', self.risk_id), '断言rules-id')
        a.verity(r4['data']['rules'][2]['ruleType'], "IN", '断言ruleType')

    def test_005_risk_getRisks(self):
        # 获取风险点信息列表 rap接口文档错误且未更新
        r5 = json.loads(f.test_risk_getRisks(orgcode=orgCode, keywords='', page=1, begin='', size=10))
        a.verity(r5['code'],'F2000','断言code')
        a.verity(r5['data']['pageNum'], 1, '断言pageNum')
        a.verity(r5['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r5['data']['record'], c.riskName)

    def test_006_risk_getDetail(self):
        self.risk_id = fs.get_risk_id(c.riskName)
        # 获取风险点详细信息
        r6 = json.loads(f.test_risk_getDetail(self.risk_id))
        a.verity(r6['data']['name'], c.riskName, '断言name')
        a.verity(r6['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r6['data']['riskType'], "PLEDEGREPEAT", '断言riskType')
        a.verity(r6['data']['gisType'], "CIRCLE", '断言gisType')
        a.verity(r6['data']['id'], self.risk_id, '断言id')
        a.verity(r6['data']['rules'][0]['id'], fs.get_rule_id('OUT', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][0]['ruleType'], "OUT", '断言ruleType')
        a.verity(r6['data']['rules'][0]['ruleName'], "出围栏报警", '断言ruleName')
        a.verity(r6['data']['rules'][1]['id'], fs.get_rule_id('STAY', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][1]['ruleType'], "STAY", '断言ruleType')
        a.verity(r6['data']['rules'][1]['thresholdMax'], c.risk_thresholdMax, '断言thresholdMax')
        a.verity(r6['data']['rules'][1]['ruleName'], "停留报警", '断言ruleName')
        a.verity(r6['data']['rules'][2]['id'], fs.get_rule_id('IN', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][2]['ruleType'], "IN", '断言ruleType')
        a.verity(r6['data']['rules'][2]['ruleName'], "入围栏报警", '断言ruleName')

    def test_007_risk_delete(self):
        self.risk_id = fs.get_risk_id(c.riskName)
        # 删除一个风险点
        f.test_risk_delete(self.risk_id, orgCode)

    def test_008_teardown(self):
        # 删除所有测试风险点
        fs.del_risks()
