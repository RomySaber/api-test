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

    # 停车异常报警
    def test_001_warnStop_saveThreshold(self):
        # 停车异常报警设置停车异常报警阀值
        f.test_warnStop_saveThreshold(3, c.station_thresholdHour, c.station_thresholdMinute)

    def test_002_warnStop_getThreshold(self):
        # 停车异常报警获取停车异常报警阀值
        r = json.loads(f.test_warnStop_getThreshold())
        a.verity(r['data']['id'], 3, '断言id')
        a.verity(r['data']['thresholdHour'], c.station_thresholdHour, '断言thresholdHour')
        a.verity(r['data']['thresholdMinute'], c.station_thresholdMinute, '断言thresholdMinute')

    def test_003_warnStop_getWarns(self):
        # 停车异常报警获取设备报警记录
        f.test_warnStop_getWarns('', 1, 10, 0)
        f.test_warnStop_getWarns('', 1, 10, 1)
