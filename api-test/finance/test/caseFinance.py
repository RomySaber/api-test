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

    # 设备管理
    def test_001_device(self):
        # 获取设备类型信息
        r1 = json.loads(f.test_device_getDeviceType())
        a.verity(r1['data'][0]['dictCode'], '1', '断言dictCode')
        a.verity(r1['data'][0]['dictName'], '有线', '断言dictName')
        a.verity(r1['data'][0]['id'], 20, '断言id')
        a.verity(r1['data'][1]['dictCode'], '0', '断言dictCode')
        a.verity(r1['data'][1]['dictName'], '无线', '断言dictName')
        a.verity(r1['data'][1]['id'], 21, '断言id')
        # 获取设备型号信息
        r2 = json.loads(f.test_device_getDeviceMoudel(''))
        a.verity(r2['data'][0]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][0]['dictName'], 'TK115', '断言dictName')
        a.verity(r2['data'][0]['id'], 22, '断言id')
        a.verity(r2['data'][1]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][1]['dictName'], 'SZ-K3', '断言dictName')
        a.verity(r2['data'][1]['id'], 23, '断言id')
        a.verity(r2['data'][2]['dictLevel'], 1, '断言dictLevel')
        a.verity(r2['data'][2]['dictName'], 'GV25', '断言dictName')
        a.verity(r2['data'][2]['id'], 54, '断言id')
        a.verity(r2['data'][3]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][3]['dictName'], 'GT740', '断言dictName')
        a.verity(r2['data'][3]['id'], 55, '断言id')
        # 获取机构信息
        r3 = json.loads(f.test_device_getLowerOrg())
        a.verity(r3['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r3['data'][0]['name'], c.companyName, '断言组织机构名称')
        # 保存设备记录
        f.test_device_save('', orgCode, c.devicetypecode,
                           c.devicemoudelCode, c.deviceCode, '001', tf.getnow_day())
        device_id = fs.get_device_id(c.deviceCode)
        # 更新设备记录
        f.test_device_update(device_id, orgCode, c.devicetypecode,
                             c.devicemoudelCode, c.deviceCode, '001', tf.getnow_day())
        # 设备列表
        r4 = json.loads(f.test_device_list('', 1, 10))
        a.verity(r4['data']['pageNum'], 1, '断言pageNum')
        a.verity(r4['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r4['data']['record'], c.deviceCode, '断言修改后的deviceCode')
        # 获取设备详情
        r5 = json.loads(f.test_device_detail(device_id))
        a.verity(r5['data']['deviceCode'], c.deviceCode, '断言deviceCode')
        a.verity(r5['data']['id'], device_id, '断言device_id')
        a.verity(r5['data']['moudelCode'], c.devicemoudelCode, '断言moudelCode')
        a.verity(r5['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r5['data']['typeCode'], c.devicetypecode, '断言typeCode')
        # 删除设备记录
        f.test_device_delete(device_id)

    # 车贷数据管理
    def test_002_finance(self):
        # 查找组织机构
        r1 = json.loads(f.test_finance_getOrgs())
        a.verity(r1['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r1['data'][0]['name'], c.companyName, '断言组织机构名称')
        # 查找还款方式
        r2 = json.loads(f.test_finance_getRepayManner())
        a.verity(r2['data'][0]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][0]['name'], "等本等息", '断言还款方式')
        a.verity(r2['data'][0]['value'], "DBDX", '断言还款方式')
        a.verity(r2['data'][1]['dictLevel'], 0, '断言dictLevel')
        a.verity(r2['data'][1]['name'], "先息后本", '断言还款方式')
        a.verity(r2['data'][1]['value'], "XXHB", '断言还款方式')
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
        # 查看车牌号是否重复
        r = json.loads(f.test_finance_alreadyHasCar(c.carNo, self.car_id))
        a.verity(r['data']['alreadyHas'], 0)
        # 查找贷款性质
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
        a.verity(r5['data']['id'], self.car_id, '断言车牌id')
        # 获取车贷数据列表
        r6 = json.loads(f.test_finance_getFinances())
        a.verity(r6['data']['pageNum'], 1, '断言pageNum')
        a.verity(r6['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r6['data']['record'], c.car_owner, '断言包含新增的车辆')
        # 获取车贷数据详情
        r7 = json.loads(f.test_finance_getDetail(self.car_id))
        a.verity(r7['data']['borrowType'], 'XZ', '断言贷款性质')
        a.verity(r7['data']['carNo'], c.carNo, '断言车牌号')
        a.verity(r7['data']['owner'], c.car_owner, '断言owner')
        a.verity(r7['data']['rePayManner'], 'DBDX', '断言还款方式')
        a.verity(r7['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r7['data']['id'], self.car_id, '断言车牌id')
        nowdate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        # 逾期 / 还款, 逾期设置
        r7 = json.loads(f.test_finance_overDue(nowdate, self.car_id, 0, 1))
        a.verityTrue(r7['data'], '断言成功设置成了逾期')
        # 逾期/还款 ,还款完成
        r8 = json.loads(f.test_finance_payOver(self.car_id, nowdate))
        a.verityTrue(r8['data'], '断言成功设置还款完成')
        # 删除的车贷数据
        r9 = json.loads(f.test_finance_deleteById(orgCode, self.car_id))
        a.verity(r9['data'], 1, '断言成功设置成了逾期')

    # 组织机构
    def test_003_org(self):
        # 获取组织机构
        r1 = json.loads(f.test_org_getOrgs())
        a.verity(r1['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r1['data'][0]['name'], c.companyName, '断言companyName')
        # 获取当前用户能操作的组织机构
        r2 = json.loads(f.test_org_getCurrentOrgs())
        a.verity(r2['data'][0]['orgCode'], orgCode, '断言orgCode')
        a.verity(r2['data'][0]['orgName'], c.companyName, '断言companyName')
        a.verity(r2['data'][0]['orgId'], 1, '断言orgId')
        # 新增机构
        r3 = json.loads(f.test_org_addOrg('', 'test-api-description', '', '',
                                          'test-api-Orgs', '', '', '', 1, ''))
        a.verity(r3['data']['description'], 'test-api-description', '断言description')
        a.verity(r3['data']['name'], 'test-api-Orgs', '断言org-name')
        a.verity(r3['data']['parentId'], 1, '断言org-name')
        addorgcode = r3['data']['orgCode']
        addorgid = r3['data']['id']
        # 修改机构
        r4 = json.loads(f.test_org_addOrg('', 'test-api-description', '', addorgid,
                                          'test-api-Orgs', '', '', '', 1, ''))
        a.verity(r4['data']['description'], 'test-api-description', '断言description')
        a.verity(r4['data']['name'], 'test-api-Orgs', '断言org-name')
        a.verity(r4['data']['parentId'], 1, '断言org-name')
        a.verity(r4['data']['orgCode'], addorgcode, '断言org-name')
        a.verity(r4['data']['id'], addorgid, '断言org-name')
        # 删除机构
        f.test_org_delete(addorgid)

    # 风险点
    def test_004_risk(self):
        # 获取组织机构
        r1 = json.loads(f.test_risk_getOrgs())
        a.verity(r1['data'][0]['name'], c.companyName, '断言org-name')
        a.verity(r1['data'][0]['orgCode'], orgCode, '断言org-name')
        # 获取报警规则
        r2 = json.loads(f.test_risk_getRules())
        a.verity(r2['data'][0]['name'], "出区域报警", '断言name')
        a.verity(r2['data'][0]['value'], "OUT", '断言value')
        a.verity(r2['data'][1]['name'], "入区域报警", '断言name')
        a.verity(r2['data'][1]['value'], "IN", '断言value')
        a.verity(r2['data'][2]['name'], "停留报警", '断言name')
        a.verity(r2['data'][2]['value'], "STAY", '断言value')
        # 获取风险点类型
        r3 = json.loads(f.test_risk_getRiskType())
        a.verity(r3['data'][0]['name'], "二押点", '断言name')
        a.verity(r3['data'][0]['value'], "PLEDEGREPEAT", '断言value')
        a.verity(r3['data'][1]['name'], "维修厂", '断言name')
        a.verity(r3['data'][1]['value'], "REPAIRSHOP", '断言value')
        a.verity(r3['data'][2]['name'], "其它", '断言name')
        a.verity(r3['data'][2]['value'], "OTHER", '断言value')
        # 新增风险点
        r4 = json.loads(f.test_risk_save(
            str({'address': '', 'coords': '104.07331,30.659167,100', 'gisType': 'CIRCLE', 'id': '',
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
        # 获取风险点信息列表
        r5 = json.loads(f.test_risk_getRisks('', '', orgCode, 1, 10))
        a.verity(r5['data']['pageNum'], 1, '断言pageNum')
        a.verity(r5['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r5['data']['record'], c.riskName)
        # 获取风险点详细信息
        r6 = json.loads(f.test_risk_getDetail(self.risk_id))
        a.verity(r6['data']['name'], c.riskName, '断言name')
        a.verity(r6['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r6['data']['riskType'], "PLEDEGREPEAT", '断言riskType')
        a.verity(r6['data']['gisType'], "CIRCLE", '断言gisType')
        a.verity(r6['data']['id'], self.risk_id, '断言id')
        a.verity(r6['data']['rules'][0]['id'], fs.get_rule_id('OUT', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][0]['ruleType'], "OUT", '断言ruleType')
        a.verity(r6['data']['rules'][0]['ruleName'], "出区域报警", '断言ruleName')
        a.verity(r6['data']['rules'][1]['id'], fs.get_rule_id('STAY', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][1]['ruleType'], "STAY", '断言ruleType')
        a.verity(r6['data']['rules'][1]['thresholdMax'], c.risk_thresholdMax, '断言thresholdMax')
        a.verity(r6['data']['rules'][1]['ruleName'], "停留报警", '断言ruleName')
        a.verity(r6['data']['rules'][2]['id'], fs.get_rule_id('IN', self.risk_id), '断言rules-id')
        a.verity(r6['data']['rules'][2]['ruleType'], "IN", '断言ruleType')
        a.verity(r6['data']['rules'][2]['ruleName'], "入区域报警", '断言ruleName')
        # 删除一个风险点
        f.test_risk_delete(self.risk_id, orgCode)

    # 离线报警阈值设置 
    def test_005_warnOfflineThreshold(self):
        # 获取当前企业的阈值
        r1 = json.loads(f.test_warnOfflineThreshold_getWarnOfflineThreshold())
        a.verity(r1['data']['wireId'], 1, '断言wireId')
        a.verity(r1['data']['wiredThresholdHour'], fs.get_threshold(1)[0], '断言wiredThresholdHour')
        a.verity(r1['data']['wiredThresholdMinute'], fs.get_threshold(1)[1], '断言wireId')
        a.verity(r1['data']['wirelessId'], 2, '断言wireId')
        a.verity(r1['data']['wirelessThresholdHour'], fs.get_threshold(2)[0], '断言wirelessThresholdHour')
        a.verity(r1['data']['wirelessThresholdMinute'], fs.get_threshold(2)[1], '断言wirelessThresholdMinute')
        f.test_warnOfflineThreshold_saveNewThreshold(
            1, c.wiredThresholdHour, c.wiredThresholdMinute, 2, c.wirelessThresholdHour, c.wirelessThresholdMinute)
        r = json.loads(f.test_warnOfflineThreshold_getWarnOfflineThreshold())
        a.verity(r['data']['wireId'], 1, '断言wireId')
        a.verity(r['data']['wiredThresholdHour'], c.wiredThresholdHour, '断言wiredThresholdHour')
        a.verity(r['data']['wiredThresholdMinute'], c.wiredThresholdMinute, '断言wireId')
        a.verity(r['data']['wirelessId'], 2, '断言wireId')
        a.verity(r['data']['wirelessThresholdHour'], c.wirelessThresholdHour, '断言wirelessThresholdHour')
        a.verity(r['data']['wirelessThresholdMinute'], c.wirelessThresholdMinute, '断言wirelessThresholdMinute')

    # 角色管理
    def test_006_role(self):
        # 新增角色数据
        r = json.loads(f.test_role_addRole('', '', c.role_name, orgCode, c.role_remark))
        role_id = fs.get_role_id(c.role_name)
        a.verity(r['data']['id'], role_id, '断言id')
        a.verity(r['data']['name'], c.role_name, '断言name')
        a.verity(r['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r['data']['remark'], c.role_remark, '断言remark')
        # 保存角色权限
        f.test_role_saveRoleMoudels(role_id, '[{"id":1,"directHave":true}]')
        # 获取角色
        r1 = json.loads(f.test_role_getDetail(role_id))
        a.verity(r1['data']['id'], role_id, '断言id')
        a.verity(r1['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r1['data']['name'], c.role_name, '断言name')
        a.verity(r1['data']['remark'], c.role_remark, '断言remark')
        # 获取角色模块
        r2 = json.loads(f.test_role_getRoleMoudels(role_id))
        a.verity(r2['data'][0]['supperParentId'], 1, '断言supperParentId')
        a.verity(r2['data'][0]['supperParentName'], "实时监控", '断言id')
        # 获取角色列表
        r3 = json.loads(f.test_role_getRoles(1, 10))
        a.verity(r3['data']['pageNum'], 1, '断言pageNum')
        a.verity(r3['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r3['data']['record'],
                        "'name': '{0}', 'remark': '{1}', 'count': 0"
                        .format(c.role_name, c.role_remark))
        # 获取角色模块树
        f.test_role_getRoleMoudelTree(role_id)
        # 修改角色数据
        r5 = json.loads(f.test_role_updateRole(0, role_id, c.role_name, orgCode, c.role_remark))
        a.verity(r5['data']['id'], role_id, '断言id')
        a.verity(r5['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r5['data']['name'], c.role_name, '断言name')
        a.verity(r5['data']['remark'], c.role_remark, '断言remark')
        a.verity(r5['data']['count'], 0, '断言count')
        # 删除角色数据
        f.test_role_deleteRole(13)

    # 停车异常报警
    def test_007_warnStop(self):
        # 停车异常报警设置停车异常报警阀值
        f.test_warnStop_saveThreshold(3, c.station_thresholdHour, c.station_thresholdMinute)
        # 停车异常报警获取停车异常报警阀值
        r = json.loads(f.test_warnStop_getThreshold())
        a.verity(r['data']['id'], 3, '断言id')
        a.verity(r['data']['thresholdHour'], c.station_thresholdHour, '断言thresholdHour')
        a.verity(r['data']['thresholdMinute'], c.station_thresholdMinute, '断言thresholdMinute')
        # 停车异常报警获取设备报警记录
        f.test_warnStop_getWarns('', 1, 10, 0)
        f.test_warnStop_getWarns('', 1, 10, 1)

    # 围栏报警
    def test_008_warnGeo(self):
        # 围栏报警模块获取设备报警记录
        f.test_warnGeo_getWarns('', 1, 10, 0)
        f.test_warnGeo_getWarns('', 1, 10, 1)

    # 逾期报警
    def test_009_warnOver(self):
        # 逾期/还款 ,查询逾期报警
        f.test_warnOver_getWarns('', 1, 10, 0)
        f.test_warnOver_getWarns('', 1, 10, 1)

    # 离线报警
    def test_010_warnOffline(self):
        # 离线报警获取离线报警记录
        f.test_warnOffline_getWarns('', 1, 10, 0)
        f.test_warnOffline_getWarns('', 1, 10, 1)
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
        # 离线报警执行报警信息处理
        f.test_warnOffline_doHandleWarn(0, '', '', 1, warnid)
        financeid = fs.get_finance_id_bywarnid(warnid)
        # 离线报警获取车辆和GPS列表
        f.test_warnOffline_getFinanceById(financeid)
        gpsid = fs.get_warn_id('lx', 'gps_id', 0, financeid)
        # 通过gpsId和离线时长查询离线点
        f.test_warnOffline_getOfflinePoint(gpsid, "")

    # 设备报警（需优化）
    def test_011_warn(self):
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
