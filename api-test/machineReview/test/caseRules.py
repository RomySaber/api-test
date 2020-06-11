#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-09 下午 1:48
@Author     : 罗林
@File       : testRules.py
@desc       : 机审规则测试
"""
import os
import ddt
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import FileUtils
from common.myFile.ExcelUtil import ExcelUtil
from machineReview.testAction import RulesAction as ra


@ddt.ddt
class TestRules(TestBaseCase):
    excel_path = FileUtils.is_windows(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource'))
    orderId = ''
    userId = ''

    @ddt.data(*ExcelUtil(excel_path, 'rules.xls', '测试数据').next())
    @ddt.unpack
    def test_rules(self, data):
        print(data)
        ra.testrules(orderId=self.orderId, userId=self.userId, ruleKey=data['ruleKey'], ruleParams=data['ruleParams'],
                     testParams=data['testParams'], ruleState=data['ruleState'], code=data['code'], msg=data['msg'])
