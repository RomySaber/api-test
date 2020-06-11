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
from common.myCommon import Assertion as a
from common.myCommon.TestBaseCase import TestBaseCase
from finance.mysqlQuery import FinanceSql as fs
from finance.mysqlQuery import ManageSql as ms
from finance.testAction import FinanceAction as f
from common.myCommon import TimeFormat as tf
from finance.testSource import Api_Const as c


orgCode = ms.get_finance_db_id()


class testFinance(TestBaseCase):
    # 车辆编号
    car_id = ''
    # 风险点id
    risk_id = ''

    # 设备报警（需优化）
    def test_001_warn(self):
        # 处理报警信息页面初始化数据
        finance_id = fs.get_car_id(c.car_owner)
        warnid = fs.get_warn_id(warn_type='sh', financeid=finance_id)
        r = json.loads(f.test_warn_getHandleWarnMessage(warnid))
        a.verity(r['data']['warnid'], warnid, '断言warnid')
        # 获取设备报警记录
        f.test_warn_getWarns('', 1, 10, 0)
        riskid = fs.get_risk_id(c.riskName)
        # 根据ID获取风险点详情
        r1 = json.loads(f.test_warn_getRiskDetail(riskid))
        a.verity(r1['data']['id'], riskid, '断言riskid')
        # 根据报警记录ID获取报警记录详情
        f.test_warn_getWarnDetailById()
        f.test_warn_doHandleWarn(1, '', '', 1, warnid)

    # 距离异常报警 （需优化）
    def test_012_warnDist(self):
        # 处理报警信息页面初始化数据
        finance_id = fs.get_car_id(c.car_owner)
        warnid = fs.get_warn_id(warn_type='jl', financeid=finance_id)
        f.test_warnDist_getHandleWarnMessage(warnid)
        # 查看设备距离报警信息
        f.test_warnDist_getDeviceWarnIntervalDetail(warnid)
        # 获取设备距离报警记录
        f.test_warnDist_getWarnIntervals('', 1, 10, 0)
        # 执行报警信息处理
        f.test_warnDist_doHandleWarn(99, 'test 其它', 'test 备注', 3, warnid)

    # 未回家 / 公司报警
    def test_013_warnhb(self):
        # 未回家/公司阀值设置
        f.test_warnhb_saveThreshold(c.TRAVEL_OUT)
        # 未回家/公司阀值获取
        r = json.loads(f.test_warnhb_getThreshold())
        a.verity(r['data'], c.TRAVEL_OUT)
        # 查询停车记录
        finance_id = fs.get_car_id(c.car_owner)
        warnid = fs.get_warn_id(warn_type='wh', financeid=finance_id)
        f.test_warnhb_getStations(warnid)
        # 查询用户住址信息
        r1 = json.loads(f.test_warnhb_getFinanceInfo(finance_id))
        a.verity(r1['data']['companyAddress'], fs.get_car_info(c.car_owner, 'company_address'))
        a.verity(r1['data']['companyCoord'], fs.get_car_info(c.car_owner, 'company_coord'))
        a.verity(r1['data']['ownerAddress'], fs.get_car_info(c.car_owner, 'owner_address'))
        a.verity(r1['data']['ownerCoord'], fs.get_car_info(c.car_owner, 'owner_coord'))
        # 查询未回家/公司报警
        f.test_warnhb_getWarns('', 1, 10, 0)
        f.test_warnhb_getWarns('', 1, 10, 1)

    # Gps安装管理
    def test_014_gps(self):
        gpsid, gpscode = fs.get_gps()[0]
        finance_id = fs.get_car_id(c.car_owner)
        # 获取机构信息
        r = json.loads(f.test_install_getLowerOrg())
        a.verity(r['data'][0]['name'], c.companyName)
        a.verity(r['data'][0]['orgCode'], orgCode)
        # 获取GPS设备
        f.test_install_getDevice(gpscode, orgCode)
        # 获取GPS类型
        f.test_install_getGpsType()
        # 获取GPS型号
        f.test_install_getGpsMoudel('有线')
        f.test_install_getGpsMoudel('无线')
        # 根据所在机构获取GPS设备信息
        r1 = json.loads(f.test_install_getDeviceByOrgCode(gpsid, orgCode))
        a.verityContain(r1['data'], gpscode)
        a.verityContain(r1['data'], str(gpsid))
        # 安装车辆搜索联想
        r2 = json.loads(f.test_install_installCarSearchAssociate(c.car_owner, orgCode))
        a.verity(r2['data'][0]['fid'], finance_id)
        a.verity(r2['data'][0]['carNo'], c.carNo)
        a.verity(r2['data'][0]['carNoAndOwner'], c.carNo + ' ' + c.car_owner)
        # 设备安装  保存GPS安装记录
        r3 = json.loads(f.test_install_saveGpsInstallRecord(finance_id, gpsid, '', '1', '1', tf.getnow_day()))
        gps_finance_id = fs.get_gps_finance_id(gpsid, finance_id)
        a.verity(r3['data'], gps_finance_id)
        # 获取GPS安装记录详情
        r4 = json.loads(f.test_install_getGpsInstallDetail(gps_finance_id))
        a.verity(r4['data']['id'], gps_finance_id)
        a.verity(r4['data']['orgCode'], orgCode)
        a.verity(r4['data']['financeId'], finance_id)
        a.verity(r4['data']['gpsId'], gpsid)
        a.verity(r4['data']['gpsCode'], gpscode)
        a.verityIn(r4['data']['installDate'], str(tf.getnow_day()))
        # 根据所在机构获取GPS设备信息
        f.test_install_getDeviceByOrgCode('', orgCode)
        # 更新GPS安装记录
        f.test_install_updateGpsInstallRecord(finance_id, gpsid, gps_finance_id, '2', '2', tf.getnow_day())
        # Gps安装记录列表
        f.test_install_findGpsInstallRecord('', 1, 10)
        # 拆机，将gps安装记录拆除
        f.test_install_dismantle(gps_finance_id)
        f.test_install_saveGpsInstallRecord(finance_id, gpsid, '', '1', '1', tf.getnow_day())
        gps_finance_id = fs.get_gps_finance_id(gpsid, finance_id)
        # 删除安装记录，安装记录出错了，将错误数据删除
        f.test_install_deleteRecord(gps_finance_id)

    # 实时监控
    def test_015_monitor(self):
        # 新增分组
        f.test_monitor_addGroup(c.groupname, orgCode)
        groupid = fs.get_gps_group(c.groupname, orgCode)
        # 修改分组
        f.test_monitor_updateGroup(groupid, c.groupname)
        # 获取当前用户能操作的分组
        # 离线
        f.test_monitor_getGroups('', 0, orgCode)
        # 在线
        f.test_monitor_getGroups('', 1, orgCode)
        # 无线
        f.test_monitor_getGroups('', 2, orgCode)
        # 获取当前登录用户的组织机构树形信息
        f.test_monitor_getCurrentOrgs()
        # 获取组织机构统计(刷新机构统计总数)
        f.test_monitor_getOrgsStatistic('', '', orgCode, 1, 10)
        gpsid = fs.get_gps(1)
        # 移动GPS到某个分组
        f.test_monitor_moveGpsToGroup(gpsid, groupid)
        gpscode = fs.get_gpscode(gpsid)
        # 查询实时消息(刷新地图上的GPS信号)
        f.test_monitor_getGpsLocationByGps(gpscode)
        # 查询某个机构的GPS统计数据(带关键字)
        f.test_monitor_getOrgCountByCode('', '', orgCode, 1, 10)
        # 获取gps信息列表(刷新机构内部的gps列表)
        f.test_monitor_getGpsByOrg(groupid, '', 0, orgCode, 1, 10)
        # 获取gps详细(用于地图展开)
        r = json.loads(f.test_monitor_gpsRealTime(gpscode))
        a.verity(r['data']['code'], gpscode)
        # 查询报警列表
        f.test_monitor_getWarns(gpsid, 1, 10)
        # 移动GPS到某个分组
        f.test_monitor_moveGpsToGroup(gpsid, 1)
        # 删除分组
        f.test_monitor_deleteGroup(groupid)

    # 车辆档案
    def test_016_historyCarRecord(self):
        financeid = fs.get_car_id(c.car_owner)
        # 车辆档案,只读,支持finance warn monitor三个模块的权限
        f.test_historyCarRecord_customerMessage(financeid)
        # 获取车辆的车贷数据
        r = json.loads(f.test_historyCarRecord_getCarFinance(financeid))
        a.verity(r['data']['owner'], c.car_owner)
        # 获取车辆设备页面初始化数据
        f.test_historyCarRecord_getCarInit(financeid)
        # 获取该车辆的实时定位数据
        f.test_historyCarRecord_getCarLocations(financeid)
        # 获取车辆的报警记录
        f.test_historyCarRecord_getCarWarn(financeid, 1, 10)
        # 获取车辆设备的报警统计信息
        f.test_historyCarRecord_getCarWarnCount(financeid)
        # 车辆档案--获取gps设备列表
        f.test_historyCarRecord_getGpsByFid(financeid)
        # 车辆档案--停车统计--常停地址
        f.test_historyCarRecord_listLocation(
            '', orgCode, '', 1, 10, financeid, c.deviceCode, c.station_starttime, c.station_endtime, 1)
        # 车辆档案--停车统计--时间分布
        f.test_historyCarRecord_quantumLocation(
            1, c.deviceCode, c.station_starttime, c.station_endtime)
        # 车辆档案--停车统计--停车明细
        f.test_historyCarRecord_stationDetail(
            '', '', '', 1, 10, 1, c.deviceCode, c.station_starttime, c.station_endtime, 1)

    # 历史轨迹
    def test_017_historyTrack(self):
        # 根据gpscode查询用户的车贷数据
        r = json.loads(f.test_historyTrack_getFinanceByGpsCode(c.deviceCode))
        gpsid = fs.get_device_id(c.deviceCode)
        financeid = fs.get_carid_by_gpsid(gpsid)
        carNo = fs.get_car_info_by_financeid(financeid, 'car_no')
        owner = fs.get_car_info_by_financeid(financeid)
        ownerMoble = fs.get_car_info_by_financeid(financeid, 'owner_moble')
        a.verity(r['data']['id'], financeid)
        a.verity(r['data']['orgCode'], orgCode)
        a.verity(r['data']['carNo'], carNo)
        a.verity(r['data']['owner'], owner)
        a.verity(r['data']['ownerMoble'], ownerMoble)
        # 根据financeId查询用户的车贷数据
        r1 = json.loads(f.test_historyTrack_getFinanceById(financeid))
        a.verity(r1['data']['id'], financeid)
        a.verity(r1['data']['orgCode'], orgCode)
        a.verity(r1['data']['carNo'], carNo)
        a.verity(r1['data']['owner'], owner)
        a.verity(r1['data']['ownerMoble'], ownerMoble)
        # 根据financeId查询绑定的GPS信息
        f.test_historyTrack_getGpsByFinanceId(financeid)
        # 获取历史轨迹定位信息(单条记录，返回所有字段)
        f.test_historyTrack_getHistoryLocation('5b188ff706699000015cda1e')
        # 获取历史轨迹(多条记录，分页查询)
        f.test_historyTrack_getHistoryLocationByPage(
            '', '', '', 1, 10, 1, c.deviceCode, c.station_starttime, c.station_endtime, 0)
        # 获取历史轨迹定位信息(全部，只返回定位相关)
        f.test_historyTrack_getHistoryTrack(
            c.deviceCode, 0, 1, c.station_starttime, c.station_endtime)
        riskid = fs.get_risk_id(c.riskName)
        # 根据id查询风险点详情
        f.test_historyTrack_getRiskDtoById(riskid)
        # 通过车贷id查询相关的所有风险点
        f.test_historyTrack_getRisksByOrgCode(c.deviceCode)
        # 根据gpsId查询相关的停车数据，查询所有
        f.test_historyTrack_getStationByGpsId(financeid, gpsid, c.station_starttime, c.station_endtime, 0)
        # 根据报警记录ID获取报警记录详情
        warnid = fs.get_warn_id(financeid=financeid)
        f.test_historyTrack_getWarnDetailById(warnid)
        # 根据报警记录ID获取报警记录详情
        f.test_historyTrack_getWarnsByGpsId(gpsid, c.station_starttime, c.station_endtime)

    # 用户管理
    def test18(self):
        pass

    def test19(self):
        pass
