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

    # 设备管理
    def test_001_getDeviceType(self):
        # 获取设备类型信息
        r1 = json.loads(f.test_device_getDeviceType())
        a.verity(r1['data'][0]['dictCode'], '1', '断言dictCode')
        a.verity(r1['data'][0]['dictName'], '有线', '断言dictName')
        a.verity(r1['data'][0]['id'], 20, '断言id')
        a.verity(r1['data'][1]['dictCode'], '0', '断言dictCode')
        a.verity(r1['data'][1]['dictName'], '无线', '断言dictName')
        a.verity(r1['data'][1]['id'], 21, '断言id')

    def test_002_getDeviceMoudel(self):
        # 获取设备型号信息
        r2 = json.loads(f.test_device_getDeviceMoudel('1'))
        a.verity(r2['data'][0]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][0]['dictName'], 'GT02D', '断言dictName')
        a.verity(r2['data'][0]['id'], 81, '断言id')
        a.verity(r2['data'][1]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][1]['dictName'], 'GM02F', '断言dictName')
        a.verity(r2['data'][1]['id'], 85, '断言id')
        a.verity(r2['data'][2]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][2]['dictName'], 'GM02E', '断言dictName')
        a.verity(r2['data'][2]['id'], 86, '断言id')
        a.verity(r2['data'][3]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][3]['dictName'], 'GT06N', '断言dictName')
        a.verity(r2['data'][3]['id'], 88, '断言id')

    def test_003_getLowerOrg(self):
        # 获取机构信息
        r3 = json.loads(f.test_device_getLowerOrg())
        a.verity(r3['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r3['data'][0]['name'], c.companyName, '断言组织机构名称')

    def test_004_device_save(self):
        # 保存设备记录
        f.test_device_save('', orgCode, c.devicetypecode,
                           c.devicemoudelCode, c.deviceCode, '001', tf.getnow_day())

    def test_005_device_update(self):
        device_id = fs.get_device_id(c.deviceCode)
        # 更新设备记录
        f.test_device_update(device_id, orgCode, c.devicetypecode,
                             c.devicemoudelCode, c.deviceCode, '001', tf.getnow_day())

    def test_006_device_list(self):
        # 设备列表
        r4 = json.loads(f.test_device_list('', 1, 10))
        a.verity(r4['data']['pageNum'], 1, '断言pageNum')
        a.verity(r4['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r4['data']['record'], c.deviceCode, '断言修改后的deviceCode')

    def test_007_device_detail(self):
        # 获取设备详情
        device_id = fs.get_device_id(c.deviceCode)
        r5 = json.loads(f.test_device_detail(device_id))
        a.verity(r5['data']['deviceCode'], c.deviceCode, '断言deviceCode')
        a.verity(r5['data']['id'], device_id[0][0], '断言device_id')
        a.verity(r5['data']['moudelCode'], c.devicemoudelCode, '断言moudelCode')
        a.verity(r5['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r5['data']['typeCode'], c.devicetypecode, '断言typeCode')

    def test_008_device_delete(self):
        device_id = fs.get_device_id(c.deviceCode)
        # 删除设备记录
        f.test_device_delete(device_id)