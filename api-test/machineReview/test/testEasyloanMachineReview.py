#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-05 上午 11:09
@Author     : 罗林
@File       : testEasyloanMachineReview.py
@desc       : 好贷机审自动化接口测试， 机审规则 1.0
"""

import ddt

from common.myCommon.Logger import getlog
from common.myCommon.TestBaseCase import TestBaseCase
from machineReview.test import get_machineReview
from machineReview.testSource import easyloan_data
from machineReview.testSource import easyloan_get_param

LOGGER = getlog(__name__)
EASYLOAN_PARAM_DATA = easyloan_data.easyloan_data_demo


@ddt.ddt  # ddt装饰器
class TestEasyloanMachineReview(TestBaseCase):
    @ddt.data(*get_machineReview.read_excel('easyloan.xlsx'))
    def test_easyloan_machine_review(self, data):
        get_machineReview.get_test_info(EASYLOAN_PARAM_DATA, data, easyloan_get_param.get_param_json)
