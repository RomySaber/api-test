#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2020-03-04 下午 5:40
@Author     : 闫红
@File       : test_008_web_omsa.py
@desc       : 运营管理接口自动化测试用例
"""

import json
from faker import Faker
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from ymjry.testAction import WebAction
from ymjry.testAction import loginAction


global_dict = loginAction.global_dict

fake = Faker("zh_CN")
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = '13412345678'


class test_008_web_omsa(TestBaseCase):
    def test_001_api_78dk_platform_sa_addSa_mobile_null(self):
        """
        SA新增
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_addSa(email='', mobile='', name=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不合法')

    def test_002_api_78dk_platform_sa_addSa(self):
        """
        SA新增
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile='131', name=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不合法')

    def test_003_api_78dk_platform_sa_addSa(self):
        """
        SA新增
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_addSa(email='', mobile=mobile, name=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不合法')

    def test_004_api_78dk_platform_sa_addSa(self):
        """
        SA新增
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=mobile, name=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '不能为空')

    def test_005_api_78dk_platform_sa_addSa(self):
        """
        SA新增
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=mobile, name=name))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')
        global saUuid
        saUuid = res['data']['saUuid']
        global_dict.set(saUuid=saUuid)

    def test_006_api_78dk_platform_sa_querySaList(self):
        """
        SA列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaList(pagecurrent=1, pagesize=10, sastate='sa_state_unknown',
                                                            searchwhere=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_007_api_78dk_platform_sa_querySaList(self):
        """
        SA列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaList(pagecurrent=1, pagesize=10, sastate='sa_state_enabled',
                                                            searchwhere=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_008_api_78dk_platform_sa_querySaList(self):
        """
        SA列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaList(pagecurrent=1, pagesize=10, sastate='sa_state_dimission',
                                                            searchwhere=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_009_api_78dk_platform_sa_querySaList(self):
        """
        SA列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaList(pagecurrent=1, pagesize=10, sastate='',
                                                            searchwhere=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_010_api_78dk_platform_sa_querySaList(self):
        """
        SA统计
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaStatistics(enddate='', pagecurrent=1, pagesize=15,
                                                                  sastate='sa_state_unknown', searchwhere='',
                                                                  startdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_011_api_78dk_platform_sa_querySaList(self):
        """
        SA统计
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaStatistics(enddate='', pagecurrent=1, pagesize=15,
                                                                  sastate='sa_state_enabled', searchwhere='',
                                                                  startdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_012_api_78dk_platform_sa_querySaList(self):
        """
        SA统计
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaStatistics(enddate='', pagecurrent=1, pagesize=15,
                                                                  sastate='sa_state_dimission', searchwhere='',
                                                                  startdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_013_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_unknown', sauuid=''))
        Assertion.verity(res['code'], '20000')


    def test_014_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_unknown', sauuid='123'))
        Assertion.verity(res['code'], '20000')


    def test_015_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_enabled', sauuid=''))
        Assertion.verity(res['code'], '20000')

    def test_016_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_dimission', sauuid=''))
        Assertion.verity(res['code'], '20000')

    def test_017_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_dimission', sauuid=saUuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_018_api_78dk_platform_sa_updateSaState(self):
        """
        SA修改在职离职状态
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_enabled', sauuid=saUuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_019_api_78dk_platform_sa_querySaLog(self):
        """
        SA操作日志
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaLog(sauuid=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verityContain(res['msg'], '不能为空')

    def test_020_api_78dk_platform_sa_querySaLog(self):
        """
        SA操作日志
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaLog(sauuid='123'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_021_api_78dk_platform_sa_querySaLog(self):
        """
        SA操作日志
        :return:
        """
        sa_uuid=MockData.uuid_random(256)
        res = json.loads(
            WebAction.test_api_78dk_platform_sa_querySaLog(sauuid=sa_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')