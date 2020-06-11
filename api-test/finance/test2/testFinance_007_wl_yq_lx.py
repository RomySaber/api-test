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

    # 围栏报警
    def test_001_warnGeo(self):
        # 围栏报警模块获取设备报警记录
        f.test_warnGeo_getWarns('', 1, 10, 0)
        f.test_warnGeo_getWarns('', 1, 10, 1)

    # 逾期报警
    def test_002_warnOver(self):
        # 逾期/还款 ,查询逾期报警
        f.test_warnOver_getWarns('', 1, 10, 0)
        f.test_warnOver_getWarns('', 1, 10, 1)

    # 逾期报警详情
    def test_003_test_warn_getWarnDetailById(self):
        r = json.loads(f.test_warn_getWarnDetailById())
        a.verity(r['code'],'F2000','断言code')

    # 离线报警
    def test_004_warnOffline(self):
        # 离线报警获取离线报警记录
        f.test_warnOffline_getWarns('', 1, 10, 0)
        f.test_warnOffline_getWarns('', 1, 10, 1)

    def test_005_warnOffline_getHandleWarnMessage(self):
        warnid = fs.get_warn_id('lx')
        # 离线报警处理报警信息页面初始化数据
        r = json.loads(f.test_warnOffline_getHandleWarnMessage(warnid))
        a.verity(r['data']['warnid'], warnid, '断言warnid')
        a.verity(r['data']['warnFeedbacks'][0]['feedbackName'], "误报", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][0]['feedbackCode'], '0', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][1]['feedbackName'], "数据异常", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][1]['feedbackCode'], '10', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][2]['feedbackName'], "二次抵押", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][2]['feedbackCode'], '2', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][3]['feedbackName'], "失联", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][3]['feedbackCode'], '3', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][4]['feedbackName'], "GPS换车安装", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][4]['feedbackCode'], '8', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][5]['feedbackName'], "定位偏差", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][5]['feedbackCode'], '9', '断言feedbackCode')
        a.verity(r['data']['warnFeedbacks'][6]['feedbackName'], "其它", '断言feedbackName')
        a.verity(r['data']['warnFeedbacks'][6]['feedbackCode'], '99', '断言feedbackCode')
        a.verity(r['data']['warnRisks'][0]['warnCode'], "1", '断言warnCode')
        a.verity(r['data']['warnRisks'][0]['warnName'], "低风险", '断言warnName')
        a.verity(r['data']['warnRisks'][1]['warnCode'], "2", '断言warnCode')
        a.verity(r['data']['warnRisks'][1]['warnName'], "中风险", '断言warnName')
        a.verity(r['data']['warnRisks'][2]['warnCode'], "3", '断言warnCode')
        a.verity(r['data']['warnRisks'][2]['warnName'], "高风险", '断言warnName')
        a.verity(r['data']['warnRisks'][3]['warnCode'], "0", '断言warnCode')
        a.verity(r['data']['warnRisks'][3]['warnName'], "正常", '断言warnName')

    def test_006_warnOffline_doHandleWarn(self):
        # 离线报警执行报警信息处理
        warnid = fs.get_warn_id('lx')
        f.test_warnOffline_doHandleWarn(0, '', '', 1, warnid)

    def test_007_warnOffline_getFinanceById(self):
        warnid = fs.get_warn_id('lx')
        financeid = fs.get_finance_id_bywarnid(warnid)
        # 离线报警获取车辆和GPS列表
        f.test_warnOffline_getFinanceById(financeid)

    def test_008_warnOffline_getOfflinePoint(self):
        warnid = fs.get_warn_id('lx')
        financeid = fs.get_finance_id_bywarnid(warnid)[0][0]
        gpsid = fs.get_warn_id('lx', 'wire_id', 0, financeid)
        # 通过gpsId和离线时长查询离线点
        f.test_warnOffline_getOfflinePoint(gpsid, "")
