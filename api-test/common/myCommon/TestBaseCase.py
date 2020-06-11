#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/6/5 0005 下午 2:06
@Author     : 罗林
@File       : TestBaseCase.py
@desc       : unittest 启动方式封装
"""
import unittest
from common.myCommon.Logger import getlog


class TestBaseCase(unittest.TestCase):

    LOGGER = getlog(__name__)

    @classmethod
    def setUpClass(cls):
        # 只执行一次，可以放所有测试执行前的操作
        cls.LOGGER.info('开始执行测试用例模块'.center(50, '✈'))

    @classmethod
    def tearDownClass(cls):
        # 只执行一次，可以放所有测试执行后的操作，如：执行sql-delete，重置测试状态
        cls.LOGGER.info('测试用例模块执行完毕'.center(50, '✈'))

    def setUp(self):
        # 每个测试用例都会执行
        self.LOGGER.info('开始执行测试用例'.center(40, '*'))

    def tearDown(self):
        # 每个测试用例都会执行
        self.LOGGER.info('测试用例执行完成'.center(40, '*'))
