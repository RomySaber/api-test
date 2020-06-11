#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-23 下午 2:33
@Author     : 罗林
@File       : test_021_web_ombd.py
@desc       : 运营管理接口自动化测试用例
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion, TimeFormat
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from hmpt.testAction import WebAction
from hmpt.testAction import loginAction
from hmpt.testAction import specialAction

fake = Factory().create('zh_CN')
bd_name = loginAction.sign + fake.name()
email = loginAction.sign + fake.email()
mobile = MockData.phone(11)
bd_name1 = loginAction.sign + fake.name()
email1 = loginAction.sign + fake.email()
mobile1 = MockData.phone(11)


class test_021_web_ombd(TestBaseCase):
    @unittest.skip('去掉了channeluuid')
    def test_001_api_78dk_platform_om_bd_addBdInfo_channeluuid_none(self):
        """
        BD新增 渠道uuid 为空
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile=mobile,
            name=bd_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('去掉了channeluuid')
    def test_002_api_78dk_platform_om_bd_addBdInfo_channeluuid_error(self):
        """
        BD新增 渠道uuid不合法
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile=mobile,
            name=bd_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_003_api_78dk_platform_om_bd_addBdInfo_email_none(self):
        """
        BD新增 邮箱 为空
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email='', mobile=mobile,
            name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_004_api_78dk_platform_om_bd_addBdInfo_mobile_none(self):
        """
        BD新增 手机号 为空
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile='',
            name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_005_api_78dk_platform_om_bd_addBdInfo_name_none(self):
        """
        BD新增 BD名称 为空
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile=mobile,
            name='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'BD名称 不能为空!')

    def test_006_api_78dk_platform_om_bd_addBdInfo_256email(self):
        """
        BD新增 256 email
        :return:
        """
        global channelid
        channelid = loginAction.global_dict.get('channelid')
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=MockData.words_cn(256),
            mobile=mobile, name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_007_api_78dk_platform_om_bd_addBdInfo_256mobile(self):
        """
        BD新增 256 mobile
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email,
            mobile=MockData.strNumber(256), name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_008_api_78dk_platform_om_bd_addBdInfo_256name(self):
        """
        BD新增  256 name
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile=mobile,
            name=MockData.strNumber(256))
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verityContain(json.loads(res)['msg'], 'BD新增数据出错!')

    def test_009_api_78dk_platform_om_bd_addBdInfo_email_error(self):
        """
        BD新增  email error
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=MockData.words_cn(10),
            mobile=mobile, name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '邮箱的格式不合法,')

    def test_010_api_78dk_platform_om_bd_addBdInfo_10mobile(self):
        """
        BD新增  10 mobile
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email,
            mobile=MockData.phone(10), name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_011_api_78dk_platform_om_bd_addBdInfo_12mobile(self):
        """
        BD新增  12 mobile
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email,
            mobile=MockData.phone(12), name=bd_name)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_012_api_78dk_platform_om_bd_addBdInfo(self):
        """
        BD新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email, mobile=mobile,
            name=bd_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global bdinfouuid
        bdinfouuid = json.loads(res)['data']['bdInfoUuid']

    def test_013_api_78dk_platform_om_bd_findBdInfoList(self):
        """
        BD列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='', enddate='', pagecurrent=1,
                pagesize=10, searchwhere='', startdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_014_api_78dk_platform_om_bd_updateBdInfoState_bdstate_none(self):
        """
        BD状态修改 bdState 为空
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid=bdinfouuid, bdstate=""))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'bdState 不能为空!')

    def test_015_api_78dk_platform_om_bd_updateBdInfoState_bdinfouuid_none(self):
        """
        BD状态修改 BdInfoUuid 为空
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid='', bdstate="bd_state_dimission"))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'BdInfoUuid 不能为空!')

    def test_016_api_78dk_platform_om_bd_updateBdInfoState_bdinfouuid_error(self):
        """
        BD状态修改 BdInfoUuid 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid='-1',
            bdstate="bd_state_dimission"))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'BdInfoUuid 不存在!')

    def test_017_api_78dk_platform_om_bd_updateBdInfoState_bdstate_error(self):
        """
        BD状态修改 bdstate 不存在!
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid=bdinfouuid, bdstate="1"))
        Assertion.verity(res['code'], '20000')

    def test_018_api_78dk_platform_om_bd_updateBdInfoState_bd_state_dimission(self):
        """
        BD状态修改  bd_state_dimission
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid=bdinfouuid,
            bdstate="bd_state_dimission"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_019_api_78dk_platform_om_bd_updateBdInfoState_bd_state_enabled(self):
        """
        BD状态修改  bd_state_enabled
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_updateBdInfoState(bdinfouuid=bdinfouuid,
            bdstate="bd_state_enabled"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_020_api_78dk_platform_om_bd_findBdMerchantList(self):
        """
        查询BD对应商户
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_findBdMerchantList(bdinfouuid=bdinfouuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_021_api_78dk_platform_om_bd_findBdMerchantList_none(self):
        """
        查询BD对应商户
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_findBdMerchantList(bdinfouuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'BdInfoUuid 不能为空!')

    def test_022_api_78dk_platform_om_bd_queryBdInfoLog_none(self):
        """
        BD操作日志查询--v1.5.0 , uuid为空
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_queryBdInfoLog(bdinfouuid=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], 'BD记录uuid不能为空')

    def test_023_api_78dk_platform_om_bd_queryBdInfoLog(self):
        """
        BD操作日志查询--v1.5.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_bd_queryBdInfoLog(bdinfouuid=bdinfouuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_024_api_78dk_platform_om_bd_findBdInfoList_bd_state_unknown(self):
        """
        BD列表  bd_state_unknown
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='bd_state_unknown', enddate='',
                pagecurrent=1, pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_025_api_78dk_platform_om_bd_findBdInfoList_bd_state_dimission(self):
        """
        BD列表  bd_state_unknown
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='bd_state_dimission', enddate='',
                pagecurrent=1, pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_026_api_78dk_platform_om_bd_findBdInfoList_bd_state_enabled(self):
        """
        BD列表  bd_state_enabled
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='bd_state_enabled', enddate='',
                pagecurrent=1, pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_027_api_78dk_platform_om_bd_findBdInfoList_searchwhere(self):
        """
        BD列表  bd_state_enabled
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='bd_state_unknown', enddate='',
                pagecurrent=1, pagesize=10, searchwhere=loginAction.sign, startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_028_api_78dk_platform_om_bd_findBdInfoList_date(self):
        """
        BD列表  bd_state_enabled
        :return:
        """

        res = json.loads(WebAction.test_api_78dk_platform_om_bd_findBdInfoList(bdstate='bd_state_unknown',
            enddate=TimeFormat.get_day_around(30), pagecurrent=1, pagesize=10, searchwhere='',
            startdate=TimeFormat.get_day_around(-30)))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_029_api_78dk_platform_om_bd_bdTj(self):
        """
        BD统计
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='', enddate='', pagecurrent=1, pagesize=10,
                searchwhere='', startdate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_030_api_78dk_platform_om_bd_bdTj_bd_state_unknown(self):
        """
        BD统计  bd_state_unknown
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='bd_state_unknown', enddate='', pagecurrent=1,
                pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_031_api_78dk_platform_om_bd_bdTj_bd_state_dimission(self):
        """
        BD统计  bd_state_unknown
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='bd_state_dimission', enddate='', pagecurrent=1,
                pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_032_api_78dk_platform_om_bd_bdTj_bd_state_enabled(self):
        """
        BD统计  bd_state_enabled
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='bd_state_enabled', enddate='', pagecurrent=1,
                pagesize=10, searchwhere='', startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_033_api_78dk_platform_om_bd_bdTj_searchwhere(self):
        """
        BD统计  bd_state_enabled
        :return:
        """

        res = json.loads(
            WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='bd_state_unknown', enddate='', pagecurrent=1,
                pagesize=10, searchwhere=loginAction.sign, startdate=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_034_api_78dk_platform_om_bd_bdTj_date(self):
        """
        BD统计  bd_state_enabled
        :return:
        """

        res = json.loads(WebAction.test_api_78dk_platform_om_bd_bdTj(bdstate='bd_state_unknown',
            enddate=TimeFormat.get_day_around(30), pagecurrent=1, pagesize=10, searchwhere='',
            startdate=TimeFormat.get_day_around(-30)))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_035_api_78dk_platform_om_bd_addBdInfo(self):
        """
        BD新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(email=email1, mobile=mobile1,
            name=bd_name1)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global bdinfouuid1
        bdinfouuid1 = json.loads(res)['data']['bdInfoUuid']

    def test_036_api_78dk_platform_om_bd_replaceBdInfoMerchant(self):
        """
        BD替换
        :return:
        """
        merchant_uuid = loginAction.global_dict.get('merchantUuid')
        merchantuuids = [merchant_uuid]
        WebAction.test_api_78dk_platform_om_bd_replaceBdInfoMerchant(merchantuuids=merchantuuids,
            newddinfouuid=bdinfouuid1, oldddinfouuid=bdinfouuid)

    @unittest.skip('废弃接口')
    def test_037_api_78dk_platform_om_contract_downContracts(self):
        """
        导出申请列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_downContracts(enddate='', orderstate='', name='',
                begindate=''))
        Assertion.verity(res['code'], '10000')

    @unittest.skip('已废弃接口')
    def test_038_api_78dk_platform_om_lm_loanOperation(self):
        """
        放款操作
        :return:
        """
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = json.loads(WebAction.test_api_78dk_platform_om_lm_loanOperation(remarks='', urls='', bankseqid='',
            contractuuid=contract_uuid, loanamount=1000))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('已废弃接口')
    def test_039_api_78dk_platform_om_lm_findLoanModeList(self):
        """
        查询线下放款列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_lm_findLoanModeList(searchwhere='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_040_api_78dk_platform_om_repayment_addRepayManualApply_userbilluuid_not_exits(self):
        """
        手动代扣 - 提交申请
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt=1000, shouldrepayamt=1000,
                userbilluuid='123213'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'].strip(), '根据userBillUuid 找不到对应的账单信息')

    def test_041_api_78dk_platform_om_repayment_addRepayManualApply_userbilluuid_none(self):
        """
        手动代扣 - 提交申请
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt=1000, shouldrepayamt=1000,
                userbilluuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'userBillUuid 不能为空!')

    def test_042_api_78dk_platform_om_repayment_addRepayManualApply_actualamt_none(self):
        """
        手动代扣 - 提交申请
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt='', shouldrepayamt=1000,
                userbilluuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '还款金额不能小于等于0！')

    def test_043_api_78dk_platform_om_repayment_addRepayManualApply_shouldrepayamt_none(self):
        """
        手动代扣 - 提交申请
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_addRepayManualApply(actualamt=1000, shouldrepayamt='',
                userbilluuid='123'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'shouldRepayAmt 不能为空!')

    def test_044_api_78dk_platform_om_repayment_findOneRepayBill_none(self):
        """
        查询还款账单 （手动还款 和 手动代扣 弹窗页面顶部公用)
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findOneRepayBill(
            userbilluuid='', actualrepaydate=''))
        Assertion.verity(res['code'], '20000')

    def test_045_api_78dk_platform_om_repayment_findOneRepayBill(self):
        """
        查询还款账单 （手动还款 和 手动代扣 弹窗页面顶部公用)
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findOneRepayBill(
            userbilluuid='123', actualrepaydate=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_046_api_78dk_platform_om_repayment_findManuelHistoryList(self):
        """
        获取 手动代扣历史记录
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_findManuelHistoryList(userbilluuid='', pagesize=10,
                pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_047_api_78dk_platform_om_repayment_findManuelHistoryList_not_exits(self):
        """
        获取 手动代扣历史记录
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_findManuelHistoryList(userbilluuid='123', pagesize=10,
                pagecurrent=1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_048_api_78dk_platform_om_repayment_auditRepayManualApply_all_none(self):
        """
        手动还款 - 审核
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_auditRepayManualApply(userbilluuid='', auditstate=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'auditState 不能为空')

    def test_049_api_78dk_platform_om_repayment_auditRepayManualApply_userbilluuid_not_exits(self):
        """
        手动还款 - 审核
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_auditRepayManualApply(userbilluuid='123', auditstate=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'auditState 不能为空')

    def test_050_api_78dk_platform_om_repayment_auditRepayManualApply_audit_state_fail(self):
        """
        手动还款 - 审核
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_auditRepayManualApply(userbilluuid='123',
            auditstate='audit_state_fail'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '没有需要审核的申请或者申请已经审核')

    def test_051_api_78dk_platform_om_repayment_auditRepayManualApply_userbilluuid_none(self):
        """
        手动还款 - 审核
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_auditRepayManualApply(userbilluuid='',
            auditstate='audit_state_fail'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'userBillUuid 不能为空')

    def test_052_api_78dk_platform_om_repayment_auditRepayManualApply_audit_state_pass(self):
        """
        手动还款 - 审核
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_auditRepayManualApply(userbilluuid='123',
            auditstate='audit_state_pass'))
        Assertion.verity(res['code'], '20000')
        Assertion.verityContain(res['msg'], '没有需要审核的申请或者申请已经审核')

    def test_053_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid_not_exits(self):
        """
        查询合同已经填写的电核问题列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid='123'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '不存在合同UUID为:123的合同信息！')

    @unittest.skip('去掉法大大')
    def test_054_api_78dk_platform_tm_fdd_findFDD_not_exits(self):
        """
        法大大查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_fdd_findFDD(contractuuid='123'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '没有查询到法大大电子合同!')

    def test_055_api_78dk_platform_om_contract_viewContract_not_exits(self):
        """
        合同详情查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewContract(uid='123'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '查询合同基本信息时出错!')

    def test_057_api_78dk_platform_om_contract_viewFDDInfo_not_exits(self):
        """
        法大大信息查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewFDDInfo(uid='123'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '查询合同基本信息时出错!')

    def test_058_api_78dk_platform_om_contract_downContracts_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出机审待审核的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_qifa_machine_audit_pending')

    def test_059_api_78dk_platform_om_contract_downContracts_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出机审拒绝的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_qifa_merchant_audit_fail')

    def test_060_api_78dk_platform_om_contract_downContracts_first_check_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出初审待审核的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_first_check_pending')

    def test_061_api_78dk_platform_om_contract_downContracts_first_check_pass(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出初审通过的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_first_check_pass')

    def test_062_api_78dk_platform_om_contract_downContracts_first_check_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出初审拒绝的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_first_check_fail')

    def test_063_api_78dk_platform_om_contract_downContracts_first_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出初审撤销的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_first_check_cancel')

    def test_064_api_78dk_platform_om_contract_downContracts_telephone_check_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出二审待审核的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_telephone_check_pending')

    def test_065_api_78dk_platform_om_contract_downContracts_telephone_check_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出二审拒绝的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_telephone_check_pending_fail')

    def test_066_api_78dk_platform_om_contract_downContracts_telephone_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出二审拒绝的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_telephone_check_cancel')

    def test_067_api_78dk_platform_om_contract_downContracts_final_check_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出终审待审核的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_final_check_pending')

    def test_068_api_78dk_platform_om_contract_downContracts_final_check_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出终审拒绝的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_final_check_fail')

    def test_069_api_78dk_platform_om_contract_downContracts_final_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出终审取消的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_final_check_cancel')

    def test_070_api_78dk_platform_om_contract_downContracts_operational_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出运营待审核的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_operational_check_pending')

    def test_071_api_78dk_platform_om_contract_downContracts_operational_check_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出运营审核失败的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_operational_check_fail')

    def test_072_api_78dk_platform_om_contract_downContracts_operational_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出运营审核撤销的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_operational_check_cancel')

    def test_073_api_78dk_platform_om_contract_downContracts_takegoods_check_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出待确认收货的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_takegoods_check_pending')

    def test_074_api_78dk_platform_om_contract_downContracts_takegoods_check_cancel(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出确认收货撤销的列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_takegoods_check_cancel')

    def test_075_api_78dk_platform_om_contract_downContracts_loan_state_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出待放款列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_loan_state_pending')

    def test_076_api_78dk_platform_om_contract_downContracts_loan_state_doing(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出放款中列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_loan_state_doing')

    def test_077_api_78dk_platform_om_contract_downContracts_loan_state_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出放款失败列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_loan_state_fail')

    def test_078_api_78dk_platform_om_contract_downContracts_repayment_state_doing(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出还款中列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_repayment_state_doing')

    def test_079_api_78dk_platform_om_contract_downContracts_repayment_state_settle(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :导出申请列表-v1.4.0,导出已结清列表
        """
        specialAction.test_api_78dk_platform_om_contract_downContracts(begindate='', enddate='', name='',
                                                                       orderstate='order_repayment_state_settle')
