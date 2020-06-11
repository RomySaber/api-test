#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-28 下午 4:27
@Author     : 罗林
@File       : testEasyloan_web_005_common.py
@desc       :  通用 接口测试用例
"""

import json
import unittest

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.testAction import Easyloan_webAction as ew


class testEasyloan_web_001_risk(TestBaseCase):
    @unittest.skip('暂停用')
    def test_001_api_78dk_web_common_selectRegionLists(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :区下拉(暂停用)
        """
        rs = ew.test_api_78dk_web_common_selectRegionLists(cityid=110100)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('暂停用')
    def test_002_api_78dk_web_common_selectCityLists(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :市下拉(暂停用)
        """
        rs = ew.test_api_78dk_web_common_selectCityLists(provinceid=110000)
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('暂停用')
    def test_003_api_78dk_web_common_selectProvinceLists(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :省下拉(暂停用)
        """
        rs = ew.test_api_78dk_web_common_selectProvinceLists()
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('暂停用')
    def test_api_78dk_web_common_delDicItem(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :字典条目-删除(暂停用)
        """
        rs = ew.test_api_78dk_web_common_delDicItem('')
        ass.verity(json.loads(rs)['code'], "10000")

    @unittest.skip('暂停用')
    def test_api_78dk_web_common_addDicItem(self):
        """
        Time       :2019-04-23
        author     : 罗林
        desc       :字典条目-删除(暂停用)
        """
        rs = ew.test_api_78dk_web_common_addDicItem(dictname='', seq='', dictcode='', dicttypecode='')
        ass.verity(json.loads(rs)['code'], "10000")
