#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/6/6 0006 下午 2:30
@Author     : 罗林
@File       : TestManageToOne.py
@desc       : 
"""
from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import ManageAction


class TestManageToOne(TestBaseCase):

    def test_add_company(self):
        res = ManageAction.test_company_save('', "danda", '', 'ddd', '15112365969', '', '100')
