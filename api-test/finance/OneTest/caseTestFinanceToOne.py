#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/18 0018 下午 4:12
@Author     : 罗林
@File       : TestFinanceToOne.py
@desc       :
"""

import json
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import FinanceAction

class TestFinanceToOne(TestBaseCase):

    def test_device_delete(self):
        # 删除设备记录
        FinanceAction.test_device_delete(18)

    def test_device_detail(self):
        # 获取设备详情
        FinanceAction.test_device_detail(2)

    def test_device_getDeviceMoudel(self):
        # 获取设备型号信息
        FinanceAction.test_device_getDeviceMoudel('SZ-K3')

    def test_device_getDeviceType(self):
        # 获取设备类型信息
        FinanceAction.test_device_getDeviceType()

    def test_device_getLowerOrg(self):
        #  获取机构信息
        FinanceAction.test_device_getLowerOrg()

    def test_device_list(self):
        # 设备列表
        r4 = json.loads(FinanceAction.test_device_list('', 1, 5))
        print(type(r4['data']))
        print(r4['data']['pageNum'])

    def test_device_save(self):
        # 新增设备
        rsponse = FinanceAction.test_device_save('', '0039', '1', 'SZ-K3', '00wxwire08', '001', '2018-05-22')
        print(rsponse)
        Assertion.verity(json.loads(rsponse)['code'], 'F2000', '检查返回结果状态码')

    def test_device_update(self):
        # 更新设备记录
        FinanceAction.test_device_update('1140', '0029', '1', 'SZ-K3', 'Q55556', '', '2018-07-11')

    def test_finance_alreadyHasCar(self):
        # 查看车牌号是否重复
        FinanceAction.test_finance_alreadyHasCar('AA', '')

    def test_finance_deleteById(self):
        # 删除的车贷数据
        FinanceAction.test_finance_deleteById('0032', 11)

    def test_finance_getBorrowType(self):
        # 查找贷款性质
        FinanceAction.test_finance_getBorrowType()

    def test_finance_getDetail(self):
        # 获取车贷数据详情
        FinanceAction.test_finance_getDetail(self, 1)

    def test_finance_getFinances(self):
        # 获取车贷数据列表
        FinanceAction.test_finance_getFinances(self, '0032', '', '', 1, 10)

    def test_finance_getOrgs(self):
        # 查找组织机构
        FinanceAction.test_finance_getOrgs()

    def test_finance_getRepayManner(self):
        # 查找还款方式
        FinanceAction.test_finance_getRepayManner()

    def test_finance_getRepayStatus(self):
        # 查找还款状态
        FinanceAction.test_finance_getRepayStatus(2)

    def test_finance_save(self):
        # 新增车辆
        rsponse = FinanceAction.test_finance_save(0,'','','','','','',True,'','','','1wx03','DBDX',1,'',1,'四川省成都市武侯区桂溪街道天府大道北段','104.068402,30.572893','四川省成都市武侯区桂溪街道益州大道中段674号成都高新孵化园','104.06432,30.572869','XZ','',1,'','','','B6','00290005','13600000016')

    # def test_gis_receivegps(self):
    #     # GPS接收，用于数据对接
    #     FinanceAction.test_gis_receivegps({"serviceKey":"KKS","gps":"[{'hbTime':'2018-07-12 13:56:26','lng':'114.020536','icon':'automobile','gpsTime':'2018-07-12 13:56:26','deviceName':'scw-GT740-51410','accStatus':'0','posType':'GPS','speed':'5','electQuantity':'70','expireFlag':'1','imei':'0209_8','activationFlag':'1','lat':'31.842657','status':'1'}]"})
    #
    # def test_gis_receivewarn(self):
    #     # receiveWarn
    #     FinanceAction.test_gis_receivewarn()
    #  接口已关闭

    def test_historyCarRecord_customerMessage(self):
        # 车辆档案,只读,支持finance warn monitor三个模块的权限
        FinanceAction.test_historyCarRecord_customerMessage(13)

    def test_historyCarRecord_getCarFinance(self):
        # 获取车辆的车贷数据
        FinanceAction.test_historyCarRecord_getCarFinance(13)

    def test_historyCarRecord_getCarInit(self):
        # 获取车辆设备页面初始化数据
        FinanceAction.test_historyCarRecord_getCarInit(13)

    def test_historyCarRecord_getCarLocations(self):
        # 获取该车辆的实时定位数据
        FinanceAction.test_historyCarRecord_getCarLocations(13)

    def test_historyCarRecord_getCarWarn(self):
        # 获取车辆的报警记录
        FinanceAction.test_historyCarRecord_getCarWarn(13, 1, 15)

    def test_historyCarRecord_getCarWarnCount(self):
        # 获取车辆设备的报警统计信息
        FinanceAction.test_historyCarRecord_getCarWarnCount(13)

    def test_historyCarRecord_getGpsByFid(self):
        # 车辆档案--获取gps设备列表
        FinanceAction.test_historyCarRecord_getGpsByFid(13)

    def test_historyCarRecord_listLocation(self):
        # 车辆档案--停车统计--常停地址
        FinanceAction.test_historyCarRecord_listLocation(
            '', '0039', '', 1, 10, 13, '12wxwire00013', '2018-10-07 00:00:00' , '2018-10-10 23:59:59', 1)

    def test_historyCarRecord_quantumLocation(self):
        # 车辆档案--停车统计--时间分布
        FinanceAction.test_historyCarRecord_quantumLocation(
            1, '12wxwire00013', '2018-10-07 00:00:00' , '2018-10-10 23:59:59')

    def test_historyCarRecord_stationDetail(self):
        # 车辆档案--停车统计--停车明细
        FinanceAction.test_historyCarRecord_stationDetail(
            '', '', '', 1, 10, 1, '00wxwire01', '2018-07-05 00:00:00', '2018-07-12 23:59:59', 1)

    def test_historyTrack_getFinanceByGpsCode(self):
        # 根据financeId查询用户的车贷数据
        FinanceAction.test_historyTrack_getFinanceByGpsCode('12wxwire00013')

    def test_historyTrack_getFinanceById(self):
        # 根据financeId查询用户的车贷数据
        FinanceAction.test_historyTrack_getFinanceById(5)

    def test_historyTrack_getGpsByFinanceId(self):
        # 根据financeId查询绑定的GPS信息
        FinanceAction.test_historyTrack_getGpsByFinanceId(5)

    def test_historyTrack_getHistoryLocation(self):
        # 获取历史轨迹定位信息(单条记录，返回所有字段)
        FinanceAction.test_historyTrack_getHistoryLocation('5b188ff706699000015cda1e')

    def test_historyTrack_getHistoryLocationByPage(self):
        # 获取历史轨迹(多条记录，分页查询)
        FinanceAction.test_historyTrack_getHistoryLocationByPage(
            '', '', '', 1, 10, 1, '12wxwire00013', '2018-10-07 00:00:00', '2018-10-10 23:59:59', 0)

    def test_historyTrack_getHistoryTrack(self):
        # 获取历史轨迹定位信息(全部，只返回定位相关)
        FinanceAction.test_historyTrack_getHistoryTrack(
            '12wxwire00013', 0, 1, '2018-10-07 00:00:00', '2018-10-10 23:59:59')

    def test_historyTrack_getRiskDtoById(self):
        # 根据id查询风险点详情
        FinanceAction.test_historyTrack_getRiskDtoById(1)

    def test_historyTrack_getRisksByOrgCode(self):
        # 通过车贷id查询相关的所有风险点
        FinanceAction.test_historyTrack_getRisksByOrgCode('12wxwire00013')

    def test_historyTrack_getStationByGpsId(self):
        # 根据gpsId查询相关的停车数据，查询所有
        FinanceAction.test_historyTrack_getStationByGpsId(2, 2, '2018-06-01 00:00:00', '2018-06-30 23:59:59', 0)

    def test_historyTrack_getWarnDetailById(self):
        # 根据报警记录ID获取报警记录详情
        FinanceAction.test_historyTrack_getWarnDetailById(5)

    def test_historyTrack_getWarnsByGpsId(self):
        # 根据报警记录ID获取报警记录详情
        FinanceAction.test_historyTrack_getWarnsByGpsId(1, '2018-10-01 00:00:00', '2018-10-30 23:59:59')

    def test_install_findGpsInstallRecord(self):
        # Gps安装记录列表
        FinanceAction.test_install_findGpsInstallRecord('', 1, 10)

    def test_install_saveGpsInstallRecord(self):
        # 设备安装  保存GPS安装记录
        FinanceAction.test_install_saveGpsInstallRecord('7', '7', '', '1', '1', '2018-05-22')

    def test_install_deleteRecord(self):
        # 删除安装记录，安装记录出错了，将错误数据删除
        FinanceAction.test_install_deleteRecord(7)

    def test_install_installCarSearchAssociate(self):
        # 安装车辆搜索联想
        FinanceAction.test_install_installCarSearchAssociate('car_api_test', '0039')

    def test_install_dismantle(self):
        # 拆机，将gps安装记录拆除
        FinanceAction.test_install_dismantle(25)

    def test_install_updateGpsInstallRecord(self):
        # 更新GPS安装记录
        FinanceAction.test_install_updateGpsInstallRecord('13', '2031', '25', '1', '1', '2018-05-22')

    def test_install_getDeviceByOrgCode(self):
        # 根据所在机构获取GPS设备信息
        FinanceAction.test_install_getDeviceByOrgCode('', '0039')

    def test_install_getGpsMoudel(self):
        # 获取GPS型号
        FinanceAction.test_install_getGpsMoudel('有线')

    def test_install_getGpsInstallDetail(self):
        # 获取GPS安装记录详情
        FinanceAction.test_install_getGpsInstallDetail(1)

    def test_install_getGpsType(self):
        # 获取GPS类型
        FinanceAction.test_install_getGpsType()

    def test_install_getDevice(self):
        # 获取GPS设备
        FinanceAction.test_install_getDevice('1', '0039')

    def test_install_getLowerOrg(self):
        # 获取机构信息
        FinanceAction.test_install_getLowerOrg()

    def test_instruct_getInstructs(self):
        # 获取指令列表
        FinanceAction.test_instruct_getInstructs('0032', '2018-07-11', '1', 1, 10)

    def test_instruct_updateWire(self):
        # 更新有线指令
        FinanceAction.test_instruct_updateWire('1', '123')

    def test_instruct_updateWireLess(self):
        # 更新无线指令
        FinanceAction.test_instruct_updateWireLess('1', '123', '2018-07-11')

    def test_monitor_updateGroup(self):
        # 修改分组
        FinanceAction.test_monitor_updateGroup(2, '125')

    def test_monitor_deleteGroup(self):
        # 删除分组
        FinanceAction.test_monitor_deleteGroup(4)

    def test_monitor_addGroup(self):
        # 新增分组
        FinanceAction.test_monitor_addGroup('124', '0039')

    def test_monitor_getGpsLocationByGps(self):
        # 查询实时消息(刷新地图上的GPS信号)
        FinanceAction.test_monitor_getGpsLocationByGps('00wxwire01,00wxwire02,00wxwire03,00wxwire04,00wxwire05')

    def test_monitor_getOrgCountByCode(self):
        # 查询某个机构的GPS统计数据(带关键字)
        FinanceAction.test_monitor_getOrgCountByCode('', '', '0032', 1, 10)

    def test_monitor_moveGpsToGroup(self):
        # 移动GPS到某个分组
        FinanceAction.test_monitor_moveGpsToGroup(2, 4)

    def test_monitor_getGpsByOrg(self):
        # 获取gps信息列表(刷新机构内部的gps列表)
        FinanceAction.test_monitor_getGpsByOrg(2, '', 0, '0032', 1, 10)

    def test_monitor_gpsRealTime(self):
        # 获取gps详细(用于地图展开)
        FinanceAction.test_monitor_gpsRealTime('00wxwire02')

    def test_monitor_getGroups(self):
        # 获取当前用户能操作的分组
        FinanceAction.test_monitor_getGroups('', 1, '0032')

    def test_monitor_getCurrentOrgs(self):
        # 获取当前登录用户的组织机构树形信息
        FinanceAction.test_monitor_getCurrentOrgs()

    def test_monitor_getOrgsStatistic(self):
        # 获取组织机构统计(刷新机构统计总数)
        FinanceAction.test_monitor_getOrgsStatistic('', '', '0039', 1, 10)

    def test_monitor_getWarns(self):
        # 查询报警列表
        FinanceAction.test_monitor_getWarns('', 1, 10)
        
    def test_warnOfflineThreshold_saveNewThreshold(self):
        # 离线报警阈值设置
        FinanceAction.test_warnOfflineThreshold_saveNewThreshold(1, 0, 11, 2, 0, 12)

    def test_warnOfflineThreshold_getWarnOfflineThreshold(self):
        # 获取当前企业的阈值
        FinanceAction.test_warnOfflineThreshold_getWarnOfflineThreshold()

    def test_org_updateOrg(self):
        # 修改机构
        FinanceAction.test_org_updateOrg('', 'test-description', '', 2, 'test', '', '', '', 1, '')

    def test_org_delete(self):
        # 删除机构
        FinanceAction.test_org_delete(7)

    def test_org_addOrg(self):
        # 新增机构
        FinanceAction.test_org_addOrg('', 'test-description', '', '', 'test1', '', '', '', 7, '')

    def test_org_getCurrentOrgs(self):
        # 获取当前用户能操作的组织机构
        FinanceAction.test_org_getCurrentOrgs()

    def test_org_getOrgs(self):
        # 获取组织机构
        FinanceAction.test_org_getOrgs()

    def test_risk_save(self):
        # 风险点
        FinanceAction.test_risk_save(str({'address':'','coords':'104.07331,30.659167,100','gisType':'CIRCLE','id':'','name':'风险点1','radius':'100','orgCode':'0032','riskType':'PLEDEGREPEAT','rules':[{'id':'','riskId':'','ruleType':'OUT'},{'id':'','riskId':'','ruleType':'STAY','thresholdMax':'1'},{'id':'','riskId':'','ruleType':'IN'}],'otherRemark':''}))

    def test_risk_delete(self):
        # 删除一个风险点
        FinanceAction.test_risk_delete('13', '0032')

    def test_risk_getRules(self):
        # 获取报警规则
        FinanceAction.test_risk_getRules()

    def test_risk_getOrgs(self):
        # 获取组织机构
        FinanceAction.test_risk_getOrgs()

    def test_risk_getRisks(self):
        # 获取风险点信息列表
        FinanceAction.test_risk_getRisks('', '', '0032', 1, 10)

    def test_risk_getRiskType(self):
        # 获取风险点类型
        FinanceAction.test_risk_getRiskType()

    def test_risk_getDetail(self):
        # 获取风险点详细信息
        FinanceAction.test_risk_getDetail(14)

    def test_role_saveRoleMoudels(self):
        # 保存角色权限
        FinanceAction.test_role_saveRoleMoudels(7, '[{"id":1,"directHave":true},{"id":7,"directHave":true},{"id":8,"directHave":true},{"id":16,"directHave":true},{"id":17,"directHave":true},{"id":18,"directHave":true},{"id":22,"directHave":true},{"id":23,"directHave":true},{"id":9,"directHave":true},{"id":10,"directHave":true},{"id":14,"directHave":true},{"id":15,"directHave":true},{"id":11,"directHave":true},{"id":12,"directHave":true},{"id":13,"directHave":true},{"id":20,"directHave":true},{"id":21,"directHave":true}]')

    def test_role_updateRole(self):
        # 修改角色数据
        FinanceAction.test_role_updateRole(0, 13, 'testrole', '0032', 'testdesc')

    def test_role_deleteRole(self):
        # 删除角色数据
        FinanceAction.test_role_deleteRole(14)

    def test_role_addRole(self):
        # 新增角色数据
        FinanceAction.test_role_addRole('', '', 'testrole', '0032', 'testdesc')

    def test_role_getDetail(self):
        # 获取角色
        FinanceAction.test_role_getDetail(10)

    def test_role_getRoles(self):
        # 获取角色列表
        FinanceAction.test_role_getRoles(1, 10)

    def test_role_getRoleMoudels(self):
        # 获取角色模块
        FinanceAction.test_role_getRoleMoudels(10)

    def test_role_getRoleMoudelTree(self):
        # 获取角色模块树
        FinanceAction.test_role_getRoleMoudelTree(13)

    def test_user_saveWarnManner(self):
        # 保存报警设置
        FinanceAction.test_user_saveWarnManner('')

    def test_user_getMoudels(self):
        # 模块权限
        FinanceAction.test_user_getMoudels()

    def test_user_updatePassword(self):
        # 模块权限
        FinanceAction.test_user_updatePassword('123456', '123456')

    def test_user_getMannerType(self):
        # 获取报警设置
        FinanceAction.test_user_getMannerType()

    def test_user_getWarnManner(self):
        # 获取用户的报警设置，如果返回的数据中没有id，则表示数据库中无此数据，此数据为默认
        FinanceAction.test_user_getWarnManner()

    def test_user_getMessages(self):
        # 获取用户的提示消息
        FinanceAction.test_user_getMessages('', '', '0032', 1, 10, 0)

    def test_user_getMessageCount(self):
        # 获取用户的提示消息数量
        FinanceAction.test_user_getMessageCount()

    def test_user_getUser(self):
        # 获取登陆用户信息
        FinanceAction.test_user_getUser()

    def test_user_logout(self):
        # 退出登陆
        FinanceAction.test_user_logout()

    def test_userManage_saveUser(self):
        FinanceAction.test_userManage_saveUser('luolin@78dk.com', 'wxtest', '0029', '13600000011', 2, '')

    def test_userManage_getCreateUserInitData(self):
        # 新增用户基础数据获取
        FinanceAction.test_userManage_getCreateUserInitData()

    def test_userManage_getUsers(self):
        # 系统用户列表
        FinanceAction.test_userManage_getUsers('', 1, 10)

    def test_userManage_modifyUser(self):
        # 编辑用户保存
        FinanceAction.test_userManage_modifyUser('', 'testuser', '0032', '13600000001', 2, 2)

    def test_userManage_getUserDetailByid(self):
        # 编辑页面数据获取
        FinanceAction.test_userManage_getUserDetailByid(2)

    def test_userManage_getPersonalmsg(self):
        # 获取个人资料
        FinanceAction.test_userManage_getPersonalmsg(2)

    def test_userManage_lockUser(self):
        # 锁定一个用户
        FinanceAction.test_userManage_lockUser(2)

    def test_userManage_unlockUser(self):
        # 解锁一个用户
        FinanceAction.test_userManage_unlockUser(2)

    def test_warn_getHandleWarnMessage(self):
        # 设备报警处理报警信息页面初始化数据
        FinanceAction.test_warn_getHandleWarnMessage('758')

    def test_warn_doHandleWarn(self):
        # 设备报警执行报警信息处理
        FinanceAction.test_warn_doHandleWarn(0, '', '', 1, '758')

    def test_warn_getRiskDetail(self):
        # 设备报警根据ID获取风险点详情
        FinanceAction.test_warn_getRiskDetail(1)

    def test_warn_getWarnDetailById(self):
        # 设备报警根据报警记录ID获取报警记录详情
        FinanceAction.test_warn_getWarnDetailById('496')

    def test_warn_getWarns(self):
        # 设备报警获取设备报警记录
        FinanceAction.test_warn_getWarns('', 1, 10, 0)

    def test_warnDist_getHandleWarnMessage(self):
        # 距离异常报警处理报警信息页面初始化数据
        FinanceAction.test_warnDist_getHandleWarnMessage(471)

    def test_warnDist_doHandleWarn(self):
        # 距离异常报警执行报警信息处理
        FinanceAction.test_warnDist_doHandleWarn(99, 'test 其它', 'test 备注', 3, 471)

    def test_warnDist_getDeviceWarnIntervalDetail(self):
        # 距离异常报警情况反馈类型,其它反馈类型补充说明,备注,风险情况类型,报警记录id
        FinanceAction.test_warnDist_getDeviceWarnIntervalDetail(471)

    def test_warnDist_getWarnIntervals(self):
        # 距离异常报警获取设备距离报警记录
        FinanceAction.test_warnDist_getWarnIntervals('', 1, 10, 0)

    def test_warnGeo_getWarns(self):
        # 围栏报警模块获取设备报警记录
        FinanceAction.test_warnGeo_getWarns('', 1, 10, 0)

    def test_warnOffline_getHandleWarnMessage(self):
        # 离线报警处理报警信息页面初始化数据
        FinanceAction.test_warnOffline_getHandleWarnMessage(174)

    def test_warnOffline_doHandleWarn(self):
        # 离线报警执行报警信息处理
        FinanceAction.test_warnOffline_doHandleWarn(0, '', '', 1, '761')

    def test_warnOffline_getWarns(self):
        # 离线报警获取离线报警记录
        FinanceAction.test_warnOffline_getWarns('', 1, 10, 0)

    def test_warnOffline_getFinanceById(self):
        # 离线报警获取车辆和GPS列表
        FinanceAction.test_warnOffline_getFinanceById(13)

    def test_warnOffline_getOfflinePoint(self):
        # 离线报警通过gpsId和离线时长查询离线点
        FinanceAction.test_warnOffline_getOfflinePoint(1, '')

    def test_warnStop_saveThreshold(self):
        # 停车异常报警设置停车异常报警阀值
        FinanceAction.test_warnStop_saveThreshold(3, 0, 3)

    def test_warnStop_getThreshold(self):
        # 停车异常报警获取停车异常报警阀值
        FinanceAction.test_warnStop_getThreshold()

    def test_warnStop_getWarns(self):
        # 停车异常报警获取设备报警记录
        FinanceAction.test_warnStop_getWarns('', 1, 10, 1)

    def test_finance_payOver(self):
        # 逾期/还款 ,还款完成
        FinanceAction.test_finance_payOver(11, '2018-07-12 23:59:59')

    def test_finance_overDue(self):
        # 逾期/还款 ,逾期设置
        FinanceAction.test_finance_overDue('2018-07-12 23:59:59', 3, 0, 1)

    def test_warnOver_getWarns(self):
        # 逾期/还款 ,查询逾期报警
        FinanceAction.test_warnOver_getWarns('', 1, 10, 0)

    def test_warnhb_getThreshold(self):
        # 未回家/公司报警 ,阀值获取
        FinanceAction.test_warnhb_getThreshold()

    def test_warnhb_saveThreshold(self):
        # 未回家/公司阀值设置
        FinanceAction.test_warnhb_saveThreshold(1)

    def test_warnhb_getStations(self):
        # 未回家/公司， 查询停车记录
        FinanceAction.test_warnhb_getStations('11')

    def test_warnhb_getWarns(self):
        # 查询未回家/公司报警
        FinanceAction.test_warnhb_getWarns('', 1, 10, 1)

    def test_warnhb_getFinanceInfo(self):
        # 查询用户住址信息
        FinanceAction.test_warnhb_getFinanceInfo(13)


