#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-17 上午 10:30
@Author     : 闫红
@File       : test_021_pms_message.py
@desc       : 同步日志相关接口
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import PlatformSystem_query as pq
from xqkj.testAction import PmsAction
from xqkj.testAction import specialAction
from xqkj.testAction import loginAction
from common.myFile import MockData as MD
import time


fake = Factory().create('zh_CN')
email = fake.email()


class test_021_pms_message(TestBaseCase):
    def test_001_backstage_message_list_all(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,查询所有列表
        """
        rs = PmsAction.test_backstage_message_list(name='', currentpage=1, pagesize=10, synchronizestate=None)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['objs'])

    def test_002_backstage_message_list_synchronizestate_is_null(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,synchronize_state为空
        """
        rs = PmsAction.test_backstage_message_list(name='', currentpage=1, pagesize=10, synchronizestate='')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['objs'])

    def test_003_backstage_message_list_synchronizestate_is_fail(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,synchronize_state为失败
        """
        rs = PmsAction.test_backstage_message_list(name='', currentpage=1, pagesize=10, synchronizestate='fail')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_004_backstage_message_list_synchronizestate_is_success(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,synchronize_state为成功
        """
        rs = PmsAction.test_backstage_message_list(name='', currentpage=1, pagesize=10, synchronizestate='success')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['objs'])

    def test_005_backstage_message_list_synchronizestate_is_waiting(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,synchronize_state为等待
        """
        rs = PmsAction.test_backstage_message_list(name='', currentpage=1, pagesize=10, synchronizestate='waiting')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_006_backstage_message_list_synchronizestate_is_waiting(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,指定查询，name非空，synchronize_state为等待
        """
        rs = PmsAction.test_backstage_message_list(name='-1', currentpage=1, pagesize=10, synchronizestate='waiting')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_007_backstage_message_list_synchronizestate_is_success(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,指定查询，name非空，synchronize_state为成功
        """
        rs = PmsAction.test_backstage_message_list(name='消费分期', currentpage=1, pagesize=10, synchronizestate='success')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_008_backstage_message_list_synchronizestate_is_fail(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,name非空，synchronize_state为失败
        """
        rs = PmsAction.test_backstage_message_list(name='-1', currentpage=1, pagesize=10, synchronizestate='fail')
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")

    def test_009_backstage_message_list_all(self):
        """
        Time       :2019-07-17
        author     : 闫红
        desc       : 同步日志列表查询,name非空，查询所有列表
        """
        rs = PmsAction.test_backstage_message_list(name='消费分期', currentpage=1, pagesize=10, synchronizestate=None)
        Assertion.verity(json.loads(rs)['code'], 10000)
        Assertion.verity(json.loads(rs)['msg'], "SUCCESS")
        Assertion.verityNotNone(json.loads(rs)['data']['objs'])
