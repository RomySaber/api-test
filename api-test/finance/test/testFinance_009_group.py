#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-14 上午 10:55
@Author     : 闫红
@File       : testFinance_009_group.py
@desc       : 
"""

import json
import time

import datetime
from common.myCommon import Assertion as a
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import FinanceSql as fs
from finance.mysqlQuery import ManageSql as ms
from finance.testAction import loginAction
from finance.testAction import FinanceAction as f

orgCode = ms.get_finance_db_id()
groupname = loginAction.sign + 'group'


class testFinance_009_group(TestBaseCase):

    def test_001_realtime_addGroup(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 新增分组
        """
        rs = f.test_realtime_addGroup(groupname=groupname, orgcode=orgCode)
        a.verity(json.loads(rs)['code'], "F2000")

    def test_002_monitor_updateGroup(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 修改分组
        """
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_monitor_updateGroup(groupid=groupid, groupname=groupname)
        a.verity(json.loads(rs)['code'],'F2000')

    def test_003_realtime_getCarByGroup(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查询分组下的车辆
        """
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_realtime_getCarByGroup(groupid=groupid, type=0, orgcode=orgCode, pagenum=1, pagesize=10, keyword='')
        a.verity(json.loads(rs)['code'],'F2000')

    def test_004_realtime_findGroups(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查询分组列表
        """
        rs = f.test_realtime_findGroups(orgcode=orgCode)
        a.verity(json.loads(rs)['code'],'F2000')

    def test_005_realtime_carRelationChange(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 车辆转移
        """
        carid = fs.get_carid_by_id_desc()
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_realtime_carRelationChange(financelist=carid, groupid=groupid)
        a.verity(json.loads(rs)['code'],'F2000')

    def test_006_realtime_deleteGroup(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 删除分组
        """
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_realtime_deleteGroup(groupid=groupid)
        a.verity(json.loads(rs)['code'],'F2000')

    def test_007_teardown(self):
        fs.del_group()

    def test_008_realtime_associate(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 全局联想搜索
        """
        rs = f.test_realtime_associate(keyword='668614460410119')
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['data'][0]['gpsCode'],'668614460410119','断言GPScode')

    def test_009_realtime_getWarnsByDevice(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查看设备报警
        """
        gpsid = fs.get_gpsid('668614460410119')
        rs = f.test_realtime_getWarnsByDevice(gpsid=gpsid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')

    def test_010_monitor_getCurrentOrgs(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 获取当前登录用户的组织机构树形信息
        """
        rs = f.test_monitor_getCurrentOrgs()
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')

    def test_011_device_detail(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 获取设备详情
        """
        gpsid = fs.get_gpsid('668614460410119')
        rs = f.test_device_detail(id=gpsid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')
        a.verity(json.loads(rs)['data']['deviceCode'],'668614460410119')
        a.verity(json.loads(rs)['data']['orgCode'],orgCode)

    def test_012_realtime_getDeviceList(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查询分组,按设备显示
        """
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_realtime_getDeviceList(devicecondition='', deviceorder='CAR', linestatus=99,
                                           orgcode=orgCode, type=0, groupid=groupid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')

    def test_013_realtime_getWarnsByCar(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查看车辆报警
        """
        financeid = fs.get_warn_latest()
        rs = f.test_realtime_getWarnsByCar(financeid=financeid, pagesize=1, pagenum=10)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')
        a.verity(json.loads(rs)['data']['record'][0]['financeId'],financeid,'断言financeid')

    def test_014_realtime_getCarList(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查询分组,按车辆查询
        """
        groupid = fs.get_gps_group(groupname=groupname,orgcod=orgCode)
        rs = f.test_realtime_getCarList(devicecondition='', deviceorder='CAR'
                                        , linestatus=99, orgcode=orgCode, type=0, groupid=groupid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')

    def test_015_realtime_getDeviceByCar(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 查询同车设备
        """
        financeid = fs.get_warn_latest()
        rs = f.test_realtime_getDeviceByCar(financeid=financeid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')
        a.verity(json.loads(rs)['data'][0]['financeId'],financeid,'断言financeid')

    def test_016_realtime_mainDevice(self):
        """
          Time       :2019-06-14
          author     : 闫红
          desc       : 设置主设备
        """
        financeid = fs.get_warn_latest()
        gpsid = fs.get_gpsid_by_fid(financeid)
        rs = f.test_realtime_mainDevice(financeid=financeid, gpsid=gpsid)
        a.verity(json.loads(rs)['code'],'F2000')
        a.verityContain(json.loads(rs)['message'],'成功')

