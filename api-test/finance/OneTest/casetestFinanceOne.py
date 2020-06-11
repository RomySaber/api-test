#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/22 0022 上午 11:01
@Author     : 罗林
@File       : testFinanceOne.py
@desc       : 
"""

import json
import unittest
import ddt
import time
# from myCommon import TimeFormat as tf
# from myCommon.ExcelUtil import ExcelUtil
# from mysqlQuery import ManageSql
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import FinanceAction
# from myCommon import ReadExcel
# from mysqlQuery import FinanceSql as fs


@ddt.ddt
class testFinanceOne(TestBaseCase):
    # orgcode = ManageSql.get_finance_db_id()
    orgcode = '0045'

    @ddt.data(["1", "GT02D", "11wxwire01"],
              ["1", "GT06N", "11wxwire02"],
              ["0", "GM09", "11wxwireless01"],
              ["0", "GM08D", "11wxwireless02"]
              )
    @ddt.unpack
    def test_device_save(self, typeCode, codetype, code):
        # 新增设备，typeCode，0无线，1有线
        rsponse = FinanceAction.test_device_save('', self.orgcode, typeCode, codetype, code, '', '2018-11-30')
        Assertion.verity(json.loads(rsponse)['code'], 'F2000', '检查返回结果状态码')
        time.sleep(1)
    #
    # @ddt.data(["wxtest1", "成A12345", "13600000021"],
    #           ["wxtest2", "成A456789", "13600000024"]
    #           )
    # @ddt.unpack
    # def test_finance_save(self, carname, carno, phone):
    #     # 新增车辆
    #     rsponse = FinanceAction.test_finance_save(0, '', '', '', '', '', '', True, '', '', '', carname, 'DBDX',
    #                                                 1, '', 1, '四川省成都市双流区统龙路', '103.935048,30.652529',
    #                                                 '四川省成都市龙泉驿区洪安镇黄新路', '104.336254,30.70002',
    #                                                 'XZ', '', 1, '', '', '', carno, self.orgcode, phone)
    #     Assertion.verity(json.loads(rsponse)['code'], 'F2000', '检查返回结果状态码')
    #     time.sleep(1)
    #
    # @ddt.data(["风险1", "104.07331,30.659167,100"],
    #           ["风险3", "104.634052,30.145127,100"],
    #           ["风险2", "104.072515,30.65932,100"]
    #           )
    # @ddt.unpack
    # def test_risk_save(self, riskname, coords):
    #     rs = FinanceAction.test_risk_save(str({'address': '', 'coords': coords, 'gisType': 'CIRCLE', 'id': '',
    #                                              'name': riskname, 'radius': '100', 'orgCode': self.orgcode,
    #                                              'riskType': 'PLEDEGREPEAT',
    #                                              'rules': [{'id': '', 'riskId': '', 'ruleType': 'OUT'},
    #                                                        {'id': '', 'riskId': '', 'ruleType': 'STAY',
    #                                                         'thresholdMax': '1'},
    #                                                        {'id': '', 'riskId': '', 'ruleType': 'IN'}],
    #                                              'otherRemark': ''}))
    #     Assertion.verity(json.loads(rs)['code'], 'F2000', '检查返回结果状态码')
    #     time.sleep(1)

    # @ddt.data(["5", "2"], ["5", "9"], ["6", "3"], ["6", "10"], ["7", "4"],
    #           ["7", "11"], ["8", "5"], ["8", "12"], ["9", "6"], ["9", "13"],
    #           ["10", "7"], ["10", "14"], ["11", "8"], ["11", "15"], ["11", "16"])
    # @ddt.unpack
    # def test_install_saveGpsInstallRecord(self, finaceid, gpsid):
    #     # 设备安装
    #     rs = FinanceAction.test_install_saveGpsInstallRecord(finaceid, gpsid, '', '1', '1', '2018-05-22')
    #     Assertion.verity(json.loads(rs)['code'], 'F2000', '检查返回结果状态码')
    #     time.sleep(1)

    # @ddt.data(
    #           ["fuletian@78dk.com", "付乐天", "13600000104"],
    #           ["liuyang@78dk.com", "刘杨", "18702828609"],
    #           ["tongchao@78dk.com", "童超", "13200000101"],
    #           ["huanghuijian@78dk.com", "黄辉建", "13200000102"],
    #           ["mazhengwu@78dk.com", "马正武", "13200000103"]
    #           )
    # @ddt.unpack
    # def test_userManage_saveUser(self, email, name, phone):
    #     rs = FinanceAction.test_userManage_saveUser(email, name, self.orgcode, phone, 2, '')
    #     Assertion.verity(json.loads(rs)['code'], 'F2000', '检查返回结果状态码')

    # excel = ExcelUtil("data.xlsx", "device")
    #
    # @ddt.data(*excel.next())
    # def test_device_save(self, data):
    #     typeCode, codetype, code = data['typeCode'], data['codetype'], data['code']
    #     # 新增设备，typeCode，0无线，1有线
    #     rsponse = FinanceAction.test_device_save('', '0039', typeCode, codetype, code, '', '2018-09-05')
    #     Assertion.verity(json.loads(rsponse)['code'], 'F2000', '检查返回结果状态码')
    #     # time.sleep(1)
    #     gpsid = FinanceSql.get_device_id(code)
    #     rs = FinanceAction.test_install_saveGpsInstallRecord(13, gpsid, '', '1', '1', '2018-09-06')

    # excel1 = ReadExcel.read_excel("data.xlsx", "finance", 1002, 1502)
    #
    # @ddt.data(*excel1)
    # def test_device_save_onebyone(self, data):
    #     groupid = 1
    #     carname, carno, phone, codetype, code, codetypeless, codeless = data
    #     #
    #     # carname = 'a' + carname
    #     # carno = carno.replace('A', 'B', 1)
    #     # phone = phone.replace('0', '1', 1)
    #     # code = 'a' + code
    #     # codeless = 'a' + codeless
    #     FinanceAction.test_finance_save(0, '', '', '', '', '', '', True, '', '', '', carname, 'DBDX',
    #                                       'X1', '', 1, '四川省成都市双流区统龙路', '103.935048,30.652529',
    #                                       '四川省成都市龙泉驿区洪安镇黄新路', '104.336254,30.70002',
    #                                       'XZ', '', '宝马', '', '', '', carno, self.orgcode, phone)
    #     FinanceAction.test_device_save('', self.orgcode, 1, codetype, code, '', tf.getnow_day())
    #     financeid = fs.get_car_id(carname)
    #     gpsid = fs.get_device_id(code)
    #     FinanceAction.test_install_saveGpsInstallRecord(financeid, gpsid, '', '1', '1', tf.getnow_day())
    #     FinanceAction.test_monitor_moveGpsToGroup(gpsid, groupid)
    #     # time.sleep(1)
    #     FinanceAction.test_device_save('', self.orgcode, 0, codetypeless, codeless, '', tf.getnow_day())
    #     lessgpsid = fs.get_device_id(codeless)
    #     FinanceAction.test_install_saveGpsInstallRecord(financeid, lessgpsid, '', '1', '1', tf.getnow_day())
    #     # time.sleep(1)
    #     FinanceAction.test_monitor_moveGpsToGroup(lessgpsid, groupid)



if __name__ == "__main__":
    unittest.main()
