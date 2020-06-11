#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-09-29 上午 11:15
@Author     : 闫红
@File       : test_025_web_urge_two.py
@desc       : 催收管理自动化测试用例（电话催收）
"""

import json
import os
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from hmpt.testAction import WebAction
from hmpt.testAction import loginAction
from hmpt.query import xqkj_query


global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')


class test_025_web_urge(TestBaseCase):
    def test_001_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,忘记还款
        """
        global app_user_uuid, contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        app_user_uuid = loginAction.get_user_uuid()
        xqkj_query.get_bill_overdue(contract_uuid=contract_uuid, user_uuid=app_user_uuid)
        # app_user_uuid = "bb9a44e01ce44b56a0f1aa3d7c7d478f"
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason="forget_repay", datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_002_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,还款不方便
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='', condition='', remark='',
            useruuid=app_user_uuid,
            overduereason='inconve', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,收入少
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='revenue_decre', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,额外支出
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='extra_spend', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_005_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,恶意拖欠
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='deliberate', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_006_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,赌博、吸毒等恶习
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='bad_habit', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_007_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,代扣系统原因导致有钱代扣失败
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='system_reason', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_008_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,多头借贷
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='long_loan', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_009_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,联系不到客户和联系人
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid,
            overduereason='lose_contact', datalist=[],
            replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_010_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,其他原因
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid, overduereason='other',
            datalist=[], replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_011_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,上传mp3
        """
        mp3_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource', '1.mp3')
        datalist = [{"file": mp3_path, "key": "FjHpyILVVxjHksSyGsVKmQlnI01T"}]
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=app_user_uuid, overduereason='other',
            datalist=datalist, replyrepaytime=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_012_api_78dk_platform_urge_addMessage(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收信息提交-v1.5.2,客户uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_addMessage(
            communicatee='testAPI', condition='testAPI', remark='testAPI',
            useruuid=-1, overduereason='other',
            datalist=[], replyrepaytime=''))
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,查询该催收人员催收历史记录
        """
        global userUuid
        userUuid = loginAction.global_dict.get('userUuid')
        res = json.loads(
            WebAction.test_api_78dk_platform_urge_queryHistory(useruuid=userUuid, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], 'S0006')
        # Assertion.verity(res['msg'], '成功')

    def test_014_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,催收人员为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryHistory(useruuid='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verityContain(res['msg'], '用户角色不可为空')

    def test_015_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,催收人员不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryHistory(useruuid=-1, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_016_api_78dk_platform_urge_queryuserandimageinfo_is_null(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,合同uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryUserInfo(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_017_api_78dk_platform_urge_queryuserandimageinfo_not_exist(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,合同uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryUserInfo(uid=-1))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '查询合同基本信息时出错!')

    def test_018_api_78dk_platform_urge_queryuserandimageinfo_not_exist(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :客户信息-v1.5.2,contract_uuid正常
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryUserInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_019_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_020_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2，contract_uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_021_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :联系人逾期贷款信息-v1.5.2，contract_uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryContactsOverdueLoan(uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_022_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryMailList(contractuuid=contract_uuid, uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_023_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryMailList(contractuuid=contract_uuid, uid=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_024_api_78dk_platform_urge_queryMailList(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,查询该用户的通讯录信息
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryMailList(contractuuid=contract_uuid, uid=app_user_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_025_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2-v1.5.2,查询该contract_uuid相关的逾期贷款信息
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_026_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2,该contract_uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_027_api_78dk_platform_urge_queryContactsOverdueLoan(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :逾期贷款信息-v1.5.2,该contract_uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryOverdueLoan(uid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_028_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryHistory(useruuid='', pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verityContain(res['msg'], '用户角色不可为空')

    def test_029_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID正常
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_urge_queryHistory(useruuid=app_user_uuid, pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_030_api_78dk_platform_urge_queryHistory(self):
        """
        Time       :2019-10-08
        author     : 闫红
        desc       :电话催收历史记录-v1.5.2,客户UUID不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryHistory(useruuid=-1, pagecurrent=1, pagesize=-10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_031_common_findContactInfo(self):
        """
        author     : 罗林
        desc       : 查询亲属联系人信息-美佳v1.0.0
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_findContactInfo(contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_032_urge_user_findReceivingAddress(self):
        """
        author     : 罗林
        desc       : 查询京东淘宝收货地址(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_findReceivingAddress(contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_033_common_findContactInfo_none(self):
        """
        author     : 罗林
        desc       : 查询亲属联系人信息-美佳v1.0.0
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_findContactInfo(''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], 'ContractUuid不能为空')

    def test_034_urge_user_findReceivingAddress_none(self):
        """
        author     : 罗林
        desc       : 查询京东淘宝收货地址(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_findReceivingAddress(''))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '您提交的参数异常')

    def test_035_common_findContactInfo_not_exits(self):
        """
        author     : 罗林
        desc       : 查询亲属联系人信息-美佳v1.0.0
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_findContactInfo('contract_uuid'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_036_urge_user_findReceivingAddress_not_exits(self):
        """
        author     : 罗林
        desc       : 查询京东淘宝收货地址(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_user_findReceivingAddress('contract_uuid'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    @unittest.skip('获取接口参数错误')
    def test_037_urge_queryCallList_useruuid_none(self):
        """
        author     : 罗林
        desc       : 查询通话详单(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryCallList(
            contractuuid='contractuuid', pagecurrent=1, pagesize=10, useruuid=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    @unittest.skip('获取接口参数错误')
    def test_038_urge_queryCallList_useruuid_not_exits(self):
        """
        author     : 罗林
        desc       : 查询通话详单(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryCallList(
            contractuuid=contract_uuid, pagecurrent=1, pagesize=10, useruuid='useruuid'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    @unittest.skip('获取接口参数错误')
    def test_039_urge_queryCallList_useruuid(self):
        """
        author     : 罗林
        desc       : 查询通话详单(美佳v1.0.0)
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryCallList(
            contractuuid='', pagecurrent=1, pagesize=10, useruuid=app_user_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_040_api_78dk_platform_urge_queryMailList_contractid_not_exits(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid不存在
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryMailList(contractuuid=contract_uuid, uid=-1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_041_api_78dk_platform_urge_queryMailList_contractid_none(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :通讯录信息-v1.5.2,用户uuid为空
        """
        res = json.loads(WebAction.test_api_78dk_platform_urge_queryMailList(contractuuid=contract_uuid, uid=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_042_common_queryCallDetailsList_contractuuid_none(self):
        """
        author     : 罗林
        desc       : 通话详单分页列表（美佳1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_queryCallDetailsList(
            contractuuid='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '您提交的参数异常')

    def test_043_common_queryCallDetailsList_contractuuid_not_exits(self):
        """
        author     : 罗林
        desc       : 通话详单分页列表（美佳1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_queryCallDetailsList(
            contractuuid=-1, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_044_common_queryCallDetailsList(self):
        """
        author     : 罗林
        desc       : 通话详单分页列表（美佳1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_common_queryCallDetailsList(
            contractuuid=contract_uuid, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('获取接口参数错误')
    def test_045_tm_contract_repaymentPlan(self):
        """
        author     : 罗林
        desc       : 还款计划（v1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_contract_repaymentPlan(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统发生内部异常，请稍候再试')

    @unittest.skip('获取接口参数错误')
    def test_046_tm_contract_repaymentPlan_uid_none(self):
        """
        author     : 罗林
        desc       : 还款计划（v1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_contract_repaymentPlan(uid='contract_uuid'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统发生内部异常，请稍候再试')

    @unittest.skip('获取接口参数错误')
    def test_047_tm_contract_repaymentPlan_uid_not_exits(self):
        """
        author     : 罗林
        desc       : 还款计划（v1.0.2）
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_contract_repaymentPlan(uid=-1))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统发生内部异常，请稍候再试')

    # def test_048_urge_queryOwnUserCallList(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid=contract_uuid, pagecurrent=1, pagesize=10, useruuid=loginAction.get_user_uuid()))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verity(res['msg'], '成功')

    # def test_049_urge_queryOwnUserCallList_contractuuid_none(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid='', pagecurrent=1, pagesize=10, useruuid=loginAction.get_user_uuid()))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verity(res['msg'], '成功')

    # def test_050_urge_queryOwnUserCallList_contractuuid_error(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid='contractuuid', pagecurrent=1, pagesize=10, useruuid=loginAction.get_user_uuid()))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verity(res['msg'], '成功')

    # def test_051_urge_queryOwnUserCallList_useruuid_error(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid=contract_uuid, pagecurrent=1, pagesize=10, useruuid='useruuid'))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verity(res['msg'], '成功')

    # def test_052_urge_queryOwnUserCallList_useruuid_none(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid=contract_uuid, pagecurrent=1, pagesize=10, useruuid=''))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verity(res['msg'], '成功')

    # def test_053_urge_queryOwnUserCallList_none(self):
    #     """
    #     author     : 罗林
    #     desc       : 查询通讯记录详单-app授权（mj_v1.0.3）
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_urge_queryOwnUserCallList(
    #         contractuuid='', pagecurrent=1, pagesize=10, useruuid=''))
    #     Assertion.verity(res['code'], 'S0001')
    #     Assertion.verity(res['msg'], '缺少查询uuid')

    @unittest.skip('404')
    def test_054_api_v2(self):
        """
        desc       : 验证短信码
        """
        res = json.loads(WebAction.test_api_v2())
