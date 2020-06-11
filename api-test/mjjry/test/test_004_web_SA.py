#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2020-01-08
@Author     : QA
@File       : test_004_SA.py
@desc       : SA相关测试用例
"""
import json
from faker import Factory
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from mjjry.testAction import WebAction
from mjjry.testAction import loginAction
from common.myFile import MockData


global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = '13412345678'


class test_004_web_SA(TestBaseCase):
    def test_001_api_78dk_platform_sa_addSa_all_none(self):
        """
        author     : 罗林
        desc       : SA新增，全部为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email='', mobile='', name=''))
        Assertion.verity(res['code'], '20000')

    def test_002_api_78dk_platform_sa_addSa_none_mobile(self):
        """
        author     : 罗林
        desc       : SA新增，手机号为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile='', name=name))
        Assertion.verityContain(res['msg'], '手机格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_003_api_78dk_platform_sa_addSa_10mobile(self):
        """
        author     : 罗林
        desc       : SA新增，10位手机号
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=MockData.phone(10), name=name))
        Assertion.verityContain(res['msg'], '手机格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_004_api_78dk_platform_sa_addSa_12mobile(self):
        """
        author     : 罗林
        desc       : SA新增，12位手机号
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=MockData.phone(12), name=name))
        Assertion.verityContain(res['msg'], '手机格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_005_api_78dk_platform_sa_addSa_error_mobile(self):
        """
        author     : 罗林
        desc       : SA新增，手机号不是数字
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile='mobile', name=name))
        Assertion.verityContain(res['msg'], '手机格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_006_api_78dk_platform_sa_addSa_none_email(self):
        """
        author     : 罗林
        desc       : SA新增，邮箱为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email='', mobile=mobile, name=name))
        Assertion.verityContain(res['msg'], '邮箱的格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_007_api_78dk_platform_sa_addSa_error_email(self):
        """
        author     : 罗林
        desc       : SA新增，邮箱错误
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email='email', mobile=mobile, name=name))
        Assertion.verityContain(res['msg'], '邮箱的格式不合法,')
        Assertion.verity(res['code'], '20000')

    def test_008_api_78dk_platform_sa_addSa_none_name(self):
        """
        author     : 罗林
        desc       : SA新增，姓名为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=mobile, name=''))
        Assertion.verityContain(res['msg'], 'Sa名称 不能为空!')
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_platform_sa_addSa(self):
        """
        author     : 罗林
        desc       : SA新增，成功
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_addSa(email=email, mobile=mobile, name=name))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        global saUuid
        saUuid = res['data']['saUuid']
        global_dict.set(saUuid=saUuid)

    def test_010_api_78dk_platform_sa_updateSaState_none_sastate(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，状态为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='', sauuid=saUuid))
        Assertion.verityContain(res['msg'], '系统发生内部异常，请稍候再试')
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_platform_sa_updateSaState_error_sastate(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，状态错误
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='123', sauuid=saUuid))
        Assertion.verityContain(res['msg'], '系统发生内部异常，请稍候再试')
        Assertion.verity(res['code'], '20000')

    def test_012_api_78dk_platform_sa_updateSaState_none_sauuid(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，UUID为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_dimission', sauuid=''))
        Assertion.verityContain(res['msg'], '系统发生内部异常，请稍候再试')
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_platform_sa_updateSaState_error_sauuid(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，UUID错误
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_dimission', sauuid=-1))
        Assertion.verityContain(res['msg'], '系统发生内部异常，请稍候再试')
        Assertion.verity(res['code'], '20000')

    def test_014_api_78dk_platform_sa_updateSaState_dimission(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，修改为离职
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_dimission', sauuid=saUuid))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_015_api_78dk_platform_sa_updateSaState_enabled(self):
        """
        author     : 罗林
        desc       : SA修改在职离职状态，修改为在职
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_updateSaState(sastate='sa_state_enabled', sauuid=saUuid))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_016_api_78dk_platform_sa_querySaList(self):
        """
        author     : 罗林
        desc       : SA列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaList(
            pagecurrent=1, pagesize=10, sastate='', searchwhere=''))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_017_api_78dk_platform_sa_querySaList_dimission(self):
        """
        author     : 罗林
        desc       : SA列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaList(
            pagecurrent=1, pagesize=10, sastate='sa_state_dimission', searchwhere=''))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_018_api_78dk_platform_sa_querySaList_enabled(self):
        """
        author     : 罗林
        desc       : SA列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaList(
            pagecurrent=1, pagesize=10, sastate='sa_state_enabled', searchwhere=''))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_019_api_78dk_platform_sa_querySaList(self):
        """
        author     : 罗林
        desc       : SA列表
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaList(
            pagecurrent=1, pagesize=10, sastate='sa_state_enabled', searchwhere=name))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_020_api_78dk_platform_sa_querySaStatistics(self):
        """
        author     : 罗林
        desc       : SA统计
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaStatistics(
            pagecurrent=1, pagesize=10, sastate='sa_state_enabled', searchwhere=name, startdate='', enddate=''))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_021_api_78dk_platform_sa_querySaLog_uuid_none(self):
        """
        author     : 罗林
        desc       : SA操作日志，UUID为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaLog(sa_uuid=''))
        Assertion.verityContain(res['msg'], 'SA记录uuid不能为空')
        Assertion.verity(res['code'], 'S0006')

    def test_022_api_78dk_platform_sa_querySaLog_uuid_error(self):
        """
        author     : 罗林
        desc       : SA操作日志，UUID错误
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaLog(sa_uuid=-1))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_022_api_78dk_platform_sa_querySaLog(self):
        """
        author     : 罗林
        desc       : SA操作日志
        """
        res = json.loads(WebAction.test_api_78dk_platform_sa_querySaLog(sa_uuid=saUuid))
        Assertion.verityContain(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
