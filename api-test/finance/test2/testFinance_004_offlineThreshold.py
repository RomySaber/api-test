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

    # 离线报警阈值设置 
    def test_001_warnOfflineThreshold_getWarnOfflineThreshold(self):
        # 获取当前企业的阈值
        r1 = json.loads(f.test_warnOfflineThreshold_getWarnOfflineThreshold())
        a.verity(r1['data']['wireId'], 1, '断言wireId')
        a.verity(r1['data']['wiredThresholdHour'], fs.get_threshold(1)[0], '断言wiredThresholdHour')
        a.verity(r1['data']['wiredThresholdMinute'], fs.get_threshold(1)[1], '断言wireId')
        a.verity(r1['data']['wirelessId'], 2, '断言wireId')
        a.verity(r1['data']['wirelessThresholdHour'], fs.get_threshold(2)[0], '断言wirelessThresholdHour')
        a.verity(r1['data']['wirelessThresholdMinute'], fs.get_threshold(2)[1], '断言wirelessThresholdMinute')
        r2 = json.loads(f.test_warnOfflineThreshold_saveNewThreshold(
            1, 2, c.wiredThresholdHour, c.wiredThresholdMinute, c.wirelessThresholdHour, c.wirelessThresholdMinute))
        a.verityTrue(r2['data'])
        r = json.loads(f.test_warnOfflineThreshold_getWarnOfflineThreshold())
        a.verity(r['data']['wireId'], 1, '断言wireId')
        a.verity(r['data']['wiredThresholdHour'], c.wiredThresholdHour, '断言wiredThresholdHour')
        a.verity(r['data']['wiredThresholdMinute'], c.wiredThresholdMinute, '断言wireId')
        a.verity(r['data']['wirelessId'], 2, '断言wireId')
        a.verity(r['data']['wirelessThresholdHour'], c.wirelessThresholdHour, '断言wirelessThresholdHour')
        a.verity(r['data']['wirelessThresholdMinute'], c.wirelessThresholdMinute, '断言wirelessThresholdMinute')
