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

    # 角色管理
    def test_001_role_addRole(self):
        # 新增角色数据
        r = json.loads(f.test_role_addRole('', '', c.role_name, c.role_remark,orgCode))
        role_id = fs.get_role_id(c.role_name)[0][0]
        a.verity(r['data']['id'], role_id, '断言id')
        a.verity(r['data']['name'], c.role_name, '断言name')
        a.verity(r['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r['data']['remark'], c.role_remark, '断言remark')

    def test_002_role_saveRoleMoudels(self):
        # 保存角色权限
        role_id = fs.get_role_id(c.role_name)
        f.test_role_saveRoleMoudels(role_id, '[{"id":1,"directHave":true}]')

    def test_003_role_getDetail(self):
        # 获取角色
        role_id = fs.get_role_id(c.role_name)[0][0]
        r1 = json.loads(f.test_role_getDetail(role_id))
        a.verity(r1['data']['id'], role_id, '断言id')
        a.verity(r1['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r1['data']['name'], c.role_name, '断言name')
        a.verity(r1['data']['remark'], c.role_remark, '断言remark')

    def test_004_role_getRoleMoudels(self):
        # 获取角色模块
        role_id = fs.get_role_id(c.role_name)
        r2 = json.loads(f.test_role_getRoleMoudels(role_id))
        a.verity(r2['data'][0]['supperParentId'], 1, '断言supperParentId')
        a.verity(r2['data'][0]['supperParentName'], "实时监控", '断言id')

    def test_005_role_getRoles(self):
        # 获取角色列表
        r3 = json.loads(f.test_role_getRoles(1, 10))
        a.verity(r3['data']['pageNum'], 1, '断言pageNum')
        a.verity(r3['data']['pageSize'], 10, '断言pageSize')
        a.verityContain(r3['data']['record'],
                        "'name': '{0}', 'remark': '{1}', 'count': 0"
                        .format(c.role_name, c.role_remark))

    def test_006_role_getRoleMoudelTree(self):
        # 获取角色模块树
        role_id = fs.get_role_id(c.role_name)
        f.test_role_getRoleMoudelTree(role_id)

    def test_007_role_updateRole(self):
        # 修改角色数据
        role_id = fs.get_role_id(c.role_name)[0][0]
        r5 = json.loads(f.test_role_updateRole(0, role_id, c.role_name, c.role_remark, orgCode))
        a.verity(r5['data']['id'], role_id, '断言id')
        a.verity(r5['data']['orgCode'], orgCode, '断言orgCode')
        a.verity(r5['data']['name'], c.role_name, '断言name')
        a.verity(r5['data']['remark'], c.role_remark, '断言remark')
        a.verity(r5['data']['count'], 0, '断言count')

    def test_008_role_deleteRole(self):
        # 删除角色数据
        role_id = fs.get_role_id(c.role_name)[0][0]
        f.test_role_deleteRole(role_id)
