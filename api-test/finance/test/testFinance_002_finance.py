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

    # 车贷数据管理
    def test_001_finance_getOrgs(self):
        # 查找组织机构
        r1 = json.loads(f.test_finance_getOrgs())
        a.verity(r1['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r1['data'][0]['name'], c.companyName, '断言组织机构名称')

    def test_002_finance_getRepayManner(self):
        # 查找还款方式
        r2 = json.loads(f.test_finance_getRepayManner())
        a.verity(r2['data'][0]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][0]['name'], "等本等息", '断言还款方式')
        a.verity(r2['data'][0]['value'], "DBDX", '断言还款方式')
        a.verity(r2['data'][1]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][1]['name'], "先息后本", '断言还款方式')
        a.verity(r2['data'][1]['value'], "XXHB", '断言还款方式')

    def test_003_finance_getRepayStatus(self):
        # 查找还款状态
        r3 = json.loads(f.test_finance_getRepayStatus(2))
        a.verity(r3['data'][0]['dictLevel'], 0, '断言dictLevel')
        a.verity(r3['data'][0]['name'], "还款中", '断言还款状态')
        a.verity(r3['data'][0]['value'], "HKZ", '断言还款状态')
        a.verity(r3['data'][1]['dictLevel'], 0, '断言dictLevel')
        a.verity(r3['data'][1]['name'], "已还清", '断言还款状态')
        a.verity(r3['data'][1]['value'], "YJQ", '断言还款状态')
        a.verity(r3['data'][2]['dictLevel'], 0, '断言dictLevel')
        a.verity(r3['data'][2]['name'], "未还款", '断言还款状态')
        a.verity(r3['data'][2]['value'], "WHK", '断言还款状态')

    def test_004_finance_getBorrowType(self):
        # 查找贷款性质
        r4 = json.loads(f.test_finance_getBorrowType())
        a.verity(r4['data'][0]['dictLevel'], 0, '断言dictLevel')
        a.verity(r4['data'][0]['name'], "新增", '断言贷款性质')
        a.verity(r4['data'][0]['value'], "XZ", '断言贷款性质')
        a.verity(r4['data'][1]['dictLevel'], 0, '断言dictLevel')
        a.verity(r4['data'][1]['name'], "结清再贷", '断言贷款性质')
        a.verity(r4['data'][1]['value'], "JQZD", '断言贷款性质')
        a.verity(r4['data'][2]['dictLevel'], 0, '断言dictLevel')
        a.verity(r4['data'][2]['name'], "展期", '断言贷款性质')
        a.verity(r4['data'][2]['value'], "ZQ", '断言贷款性质')

    def test_005_finance_alreadyHasCar(self):
        # 查看车牌号是否重复
        r = json.loads(f.test_finance_alreadyHasCar(c.carNo, self.car_id))
        a.verity(r['data']['alreadyHas'], 0,'断言重复车牌')

    def test_006_finance_save(self):
        # 新增车贷数据
        r5 = json.loads(f.
                        test_finance_save(0, '', '', '', '', '', '', True, '', '', '', c.car_owner, 'DBDX', 1,
                                          '', 1, '四川省成都市武侯区桂溪街道天府大道北段', '104.068402,30.572893',
                                          '四川省成都市武侯区桂溪街道益州大道中段674号成都高新孵化园',
                                          '104.06432,30.572869', 'XZ', '', 1, '', '', '',
                                          c.carNo, orgCode, '13600000016'))
        self.car_id = fs.get_car_id(c.car_owner)
        a.verity(r5['data']['borrowType'], 'XZ', '断言贷款性质')
        a.verity(r5['data']['carNo'], c.carNo, '断言车牌号')
        a.verity(r5['data']['owner'], c.car_owner, '断言owner')
        a.verity(r5['data']['rePayManner'], 'DBDX', '断言还款方式')
        a.verity(r5['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r5['data']['id'], self.car_id[0][0], '断言车牌id')

    def test_007_finance_getFinances(self):
        # 获取车贷数据列表 rap未更新
        r6 = json.loads(f.test_finance_getFinances())
        a.verity(r6['data']['pageNum'], 1, '断言pageNum')
        a.verity(r6['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r6['data']['record'], c.car_owner, '断言包含新增的车辆')

    def test_008_finance_getDetail(self):
        # 获取车贷数据详情
        self.car_id = fs.get_car_id(c.car_owner)
        r7 = json.loads(f.test_finance_getDetail(self.car_id))
        a.verity(r7['data']['borrowType'], 'XZ', '断言贷款性质')
        a.verity(r7['data']['carNo'], c.carNo, '断言车牌号')
        a.verity(r7['data']['owner'], c.car_owner, '断言owner')
        a.verity(r7['data']['rePayManner'], 'DBDX', '断言还款方式')
        a.verity(r7['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r7['data']['id'], self.car_id[0][0], '断言车牌id')
        # nowdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
