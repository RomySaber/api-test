#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-07-22 下午 2:04
@Author     : 罗林
@File       : test_020_web_om.py
@desc       : 运营管理接口自动化测试用例
"""

import json

from common.myCommon import Assertion
from common.myCommon import TimeFormat
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from mjjry.testAction import WebAction
from mjjry.testAction import loginAction


class test_020_web_om(TestBaseCase):
    def test_001_api_78dk_platform_sys_user_saveSystemUser_all(self):
        """
        合同列表查询（申请列表） 全部
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='', enddate='', begindate='', pagesize=10, name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_002_api_78dk_platform_sys_user_saveSystemUser_user_defined(self):
        """
        合同列表查询（申请列表） 自定义时间段
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='', enddate=1563811199999, begindate=1561910400000, pagesize=10, name=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_sys_user_saveSystemUser_recent_7_days(self):
        """
        合同列表查询（申请列表） 最近7天
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='', enddate=TimeFormat.get_now_time_13(),
                begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(-7)), pagesize=10, name=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_004_api_78dk_platform_sys_user_saveSystemUser_recent_30_days(self):
        """
        合同列表查询（申请列表） 最近30天
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='', enddate=TimeFormat.get_now_time_13(),
                begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(-30)), pagesize=10, name=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_005_api_78dk_platform_sys_user_saveSystemUser_now_days(self):
        """
        合同列表查询（申请列表） 最近30天
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='', enddate=TimeFormat.get_now_time_13(),
                begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(0)), pagesize=10, name=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_006_api_78dk_platform_sys_user_saveSystemUser_order_first_check_pending(self):
        """
        合同列表查询（申请列表） 初审待审核
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='order_first_check_pending', enddate='', begindate='', pagesize=10, name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_007_api_78dk_platform_sys_user_saveSystemUser_order_first_check_fail(self):
        """
        合同列表查询（申请列表） 初审拒绝
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate='order_first_check_fail', enddate='', begindate='', pagesize=10, name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_008_api_78dk_platform_sys_user_saveSystemUser_order_first_check_cancel(self):
        """
        合同列表查询（申请列表） 初审撤销
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="order_first_check_cancel", enddate='', begindate='', pagesize=10, name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_009_api_78dk_platform_sys_user_saveSystemUser_order_telephone_check_pending(self):
        """
        合同列表查询（申请列表） 电核待审核
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="order_telephone_check_pending", enddate='', begindate='', pagesize=10,
                name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_010_api_78dk_platform_sys_user_saveSystemUser_order_telephone_check_pending_fail(self):
        """
        合同列表查询（申请列表） 电核拒绝
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="order_telephone_check_pending_fail", enddate='', begindate='', pagesize=10,
                name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_011_api_78dk_platform_sys_user_saveSystemUser_order_telephone_check_cancel(self):
        """
        合同列表查询（申请列表） 电核撤销
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="order_telephone_check_cancel", enddate='', begindate='', pagesize=10,
                name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_012_api_78dk_platform_sys_user_saveSystemUser_order_final_check_pending(self):
        """
        合同列表查询（申请列表） 终审待审核
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="order_final_check_pending", enddate='', begindate='', pagesize=10,
                name=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_013_api_78dk_platform_sys_user_saveSystemUser_name(self):
        """
        合同列表查询（申请列表） 按名称查询
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="", enddate='', begindate='', pagesize=10, name=loginAction.sign))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')

    def test_014_api_78dk_platform_sys_user_saveSystemUser_name_not_exits(self):
        """
        合同列表查询（申请列表） 名称不存在
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewContracts(
                pagecurrent=1, orderstate="", enddate='', begindate='', pagesize=10, name=MockData.words_cn(10)))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '成功')
        # Assertion.verityNone(res['data']['dataList'])

    def test_015_api_78dk_platform_om_contract_viewFDDInfo(self):
        """
        法大大信息查询
        :return:
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewFDDInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    def test_016_api_78dk_platform_om_contract_viewContract(self):
        """
        合同详情查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewContract(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    # def test_017_api_78dk_platform_tm_first_findContractInfoSignStateWeb(self):
    #     """
    #     修改法大大合同签署状态 修改为重签(废)
    #     :return:
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(uid=contract_uuid))
    #     Assertion.verity(res['code'], '10000')

    # @unittest.skip('获取接口参数错误')
    # def test_018_api_78dk_platform_tm_first_findAuditCommentList(self):
    #     """
    #     查询评论列表(3)
    #     :return:
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_tm_first_findAuditCommentList(
    #         pagesize=10, pagecurrent=1, contractuuid=contract_uuid))
    #     Assertion.verity(res['code'], '10000')
    #     Assertion.verityNotNone(res['data']['dataList'])

    def test_019_api_78dk_platform_om_contract_viewUserBill(self):
        """
        账单信息查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewUserBill(
            pagesize=10, pagecurrent=1, name=''))
        Assertion.verity(res['code'], '20000')

    def test_020_api_78dk_platform_tm_fdd_findFDD(self):
        """
        法大大查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_fdd_findFDD(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    def test_021_api_78dk_platform_om_contract_viewTongdunInfo(self):
        """
        同盾信息查询
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewTongdunInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_022_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(self):
        """
        查询合同已经填写的电核问题列表
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_contract_viewTelephoneCheckInfosByContractUuid(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    def test_023_api_78dk_platform_om_contract_viewBaiDuInfo(self):
        """
        查询百度接口
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewBaiDuInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    def test_025_api_78dk_platform_om_contract_viewTencentInfo(self):
        """
        查询腾讯接口
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_viewTencentInfo(uid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    # def test_026_api_78dk_platform_om_contract_saveErpInfo(self):
    #     """
    #     保存合同ERP信息
    #     :return:
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_om_contract_saveErpInfo(
    #         erpinfonumber='', contractuuid=contract_uuid))
    #     Assertion.verity(res['code'], '20000')

    def test_027_api_78dk_platform_om_trans_findTransLogList_all(self):
        """
        交易流水列表  全部
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', transstate='', begindate='', searchwhere='', transtype=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_028_api_78dk_platform_om_trans_findTransLogList_now(self):
        """
        交易流水列表  今天
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate=TimeFormat.get_now_time_13(), transstate='',
            begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(0)), searchwhere='', transtype=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_029_api_78dk_platform_om_trans_findTransLogList_recent_7_days(self):
        """
        交易流水列表  最近7天
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate=TimeFormat.get_now_time_13(), transstate='',
            begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(-7)), searchwhere='',
            transtype=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_030_api_78dk_platform_om_trans_findTransLogList_recent_30_days(self):
        """
        交易流水列表  最近30天
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate=TimeFormat.get_now_time_13(), transstate='',
            begindate=TimeFormat.string_toTimestamp_13(TimeFormat.get_day_start_time(-30)), searchwhere='',
            transtype=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_031_api_78dk_platform_om_trans_findTransLogList_user_defined(self):
        """
        交易流水列表  自定义时段
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate=1563811199999, begindate=1561910400000, transstate='', searchwhere='',
            transtype=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_032_api_78dk_platform_om_trans_findTransLogList_trans_type_P001(self):
        """
        交易流水列表  代发
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P001"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_033_api_78dk_platform_om_trans_findTransLogList_trans_type_P002(self):
        """
        交易流水列表  代扣
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P002"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_034_api_78dk_platform_om_trans_findTransLogList_trans_type_P003(self):
        """
        交易流水列表  线下还款
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P003"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_035_api_78dk_platform_om_trans_findTransLogList_trans_type_P004(self):
        """
        交易流水列表  手动扣款
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P004"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_036_api_78dk_platform_om_trans_findTransLogList_trans_type_P005(self):
        """
        交易流水列表  提前结清
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P005"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_037_api_78dk_platform_om_trans_findTransLogList_trans_type_P006(self):
        """
        交易流水列表  提前部分还款
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate='', searchwhere='',
            transtype="trans_type_P006"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_038_api_78dk_platform_om_trans_findTransLogList_bank_state_S(self):
        """
        交易流水列表  成功
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate="bank_state_S", searchwhere='',
            transtype=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_039_api_78dk_platform_om_trans_findTransLogList_bank_state_F(self):
        """
        交易流水列表  失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate="bank_state_F", searchwhere='',
            transtype=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_040_api_78dk_platform_om_trans_findTransLogList_bank_state_P(self):
        """
        交易流水列表  处理中
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate="bank_state_P", searchwhere='',
            transtype=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_041_api_78dk_platform_om_trans_findTransLogList(self):
        """
        交易流水列表  查询交易对象
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate="", searchwhere=loginAction.sign,
            transtype=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_042_api_78dk_platform_om_trans_findTransLogList_searchwhere_not_exits(self):
        """
        交易流水列表  查询不存在的交易对象
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_trans_findTransLogList(
            pagesize=10, pagecurrent=1, enddate='', begindate='', transstate="", searchwhere=MockData.words_cn(10),
            transtype=""))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNone(res['data']['dataList'])

    def test_045_api_78dk_platform_om_repayment_findRepaymentList_all_none(self):
        """
        还款列表 全部为空
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate='', auditoptname='', lastpaydatebegintime='', username='',
            contractnumber='', usermobile='', overduestate='', paystate='', applyoptname='', pagesize=10,
            pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_046_api_78dk_platform_om_repayment_findRepaymentList_all(self):
        """
        还款列表  查询全部
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber='', usermobile='', overduestate="overdue_state_all", paystate="pay_state_all",
            applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_047_api_78dk_platform_om_repayment_findRepaymentList_time(self):
        """
        还款列表  查询 还款时间 为2019-07-01 ~ 2019-08-31
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime="2019-08-31", auditstate="audit_state_all", auditoptname='',
            lastpaydatebegintime="2019-07-01", username='', contractnumber='', usermobile='',
            overduestate="overdue_state_all", paystate="pay_state_all",
            applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_048_api_78dk_platform_om_repayment_findRepaymentList_pay_state_nopay(self):
        """
        还款列表  查询 还款状态 为 未还
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber='', usermobile='', overduestate="overdue_state_all", paystate="pay_state_nopay",
            applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_049_api_78dk_platform_om_repayment_findRepaymentList_pay_state_part(self):
        """
        还款列表  查询 还款状态 为 部分还款
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber='', usermobile='', overduestate="overdue_state_all", paystate="pay_state_part",
            applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_050_api_78dk_platform_om_repayment_findRepaymentList_pay_state_settle(self):
        """
        还款列表  查询 还款状态 为 结清
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber='', usermobile='', overduestate="overdue_state_all", paystate="pay_state_settle",
            applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_051_api_78dk_platform_om_repayment_findRepaymentList_contractNumber_not_exits(self):
        """
        还款列表  查询 订单编号 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber=MockData.words_cn(10), usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_052_api_78dk_platform_om_repayment_findRepaymentList_contractNumber(self):
        """
        还款列表  查询 订单编号
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='', username='',
            contractnumber=contract_uuid, usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_053_api_78dk_platform_om_repayment_findRepaymentList_userName_not_exits(self):
        """
        还款列表  查询 借款人 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username=MockData.words_cn(10), contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_054_api_78dk_platform_om_repayment_findRepaymentList_userName(self):
        """
        还款列表  查询 借款人
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username=loginAction.sign, contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_054_api_78dk_platform_om_repayment_findRepaymentList_userMobile_not_exits(self):
        """
        还款列表  查询 手机号 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='183', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_055_api_78dk_platform_om_repayment_findRepaymentList_userMobile(self):
        """
        还款列表  查询 手机号
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='18328088971', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_056_api_78dk_platform_om_repayment_findRepaymentList_applyOptName_not_exits(self):
        """
        还款列表  查询 提交人 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='123', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_057_api_78dk_platform_om_repayment_findRepaymentList_applyOptName(self):
        """
        还款列表  查询 提交人
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='胡红', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_058_api_78dk_platform_om_repayment_findRepaymentList_auditOptName(self):
        """
        还款列表  查询 审核人 不存在
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='123', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_059_api_78dk_platform_om_repayment_findRepaymentList(self):
        """
        还款列表  查询 审核人
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='胡红', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_060_api_78dk_platform_om_repayment_findRepaymentList_audit_state_pending(self):
        """
        还款列表  查询 审核状态 待审核
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_pending", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_061_api_78dk_platform_om_repayment_findRepaymentList_audit_state_pass(self):
        """
        还款列表  查询 审核状态 审核通过
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_pass", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_062_api_78dk_platform_om_repayment_findRepaymentList_audit_state_fail(self):
        """
        还款列表  查询 审核状态 审核失败
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_fail", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_all",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_063_api_78dk_platform_om_repayment_findRepaymentList_overdue_state_doing(self):
        """
        还款列表  查询 逾期状态 逾期中
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_doing",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_064_api_78dk_platform_om_repayment_findRepaymentList_overdue_state_end(self):
        """
        还款列表  查询 逾期状态 结束逾期
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_end",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_065_api_78dk_platform_om_repayment_findRepaymentList_overdue_state_no(self):
        """
        还款列表  查询 逾期状态 未逾期
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentList(
            lastpaydateendtime='', auditstate="audit_state_all", auditoptname='', lastpaydatebegintime='',
            username='', contractnumber='', usermobile='', overduestate="overdue_state_no",
            paystate="pay_state_all", applyoptname='', pagesize=10, pagecurrent=1, merchantname=''))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_066_api_78dk_platform_om_repayment_findRepayment(self):
        """
        还款基本信息
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepayment(userbilluuid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_067_api_78dk_platform_om_repayment_findRepayment_not_exits(self):
        """
        还款基本信息
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepayment(userbilluuid='123'))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_068_api_78dk_platform_om_repayment_findRepaymentDetil(self):
        """
        还款详情
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_om_repayment_findRepaymentDetil(userbilluuid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_069_api_78dk_platform_om_repayment_findRepaymentDetil_not_exits(self):
        """
        还款详情
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_findRepaymentDetil(userbilluuid='123'))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    # def test_070_api_78dk_platform_om_hmaw_addRepayManualApply(self):
    #     """
    #     添加 手动还款申请
    #     :return:
    #     """
    #     res = json.loads(WebAction.test_api_78dk_platform_om_hmaw_addRepayManualApply(
    #         actualamt='', billperiod='', contractuuid='', optway='', shouldrepayamt='', userbilluuid=''))
    #     Assertion.verity(res['code'], '20000')
    #     Assertion.verity(res['msg'], '还款金额不能小于等于0！')

    def test_071_api_78dk_platform_om_repayment_addRepayUnderLineApply(self):
        """
        添加 手动还款申请
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_addRepayUnderLineApply(
            actualamt=1000, shouldrepayamt=1000, userbilluuid='', actualrepaydate='', picturelist='', remarks=''))
        Assertion.verity(res['code'], '20000')

    def test_072_api_78dk_platform_om_repayment_addRepayUnderLineApply_actualamt_none(self):
        """
        添加 手动还款申请
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_addRepayUnderLineApply(
            actualamt='', shouldrepayamt=1000, userbilluuid='', actualrepaydate='', picturelist='', remarks=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '还款金额不能小于等于0！')

    def test_073_api_78dk_platform_om_repayment_addRepayUnderLineApply_shouldrepayamt_none(self):
        """
        添加 手动还款申请
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_addRepayUnderLineApply(
            actualamt=1000, shouldrepayamt='', userbilluuid='', actualrepaydate='', picturelist='', remarks=''))
        Assertion.verity(res['code'], '20000')
        # Assertion.verity(res['msg'], '还款金额不能小于等于0！')

    def test_074_api_78dk_platform_om_repayment_downRepaymentList(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :还款列表导出-v1.4.0,导出待审核的列表
        """
        res = WebAction.test_api_78dk_platform_om_repayment_downRepaymentList(applyoptname='', auditoptname='',
              auditstate='audit_state_all', contractnumber='', lastpaydatebegintime='', lastpaydateendtime='',
              overduestate='overdue_state_all', paystate='pay_state_all', usermobile='', username='')
        # Assertion.verityContain(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

    def test_075_api_78dk_platform_ap_repayment_advancePayment(self):
        """
        提前还清-v1.5.0 ， 产生 数据库锁
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_ap_repayment_advancePayment(
            paydate='', remarks='', urls='', userbilluuid='', interestporid=''))
        Assertion.verity(res['code'], '20000')

    def test_076_api_78dk_platform_ap_repayment_findCalculate_none(self):
        """
        提前还清试算-v1.5.0,uid为空
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_ap_repayment_findCalculate(uid='', interestporid=''))
        Assertion.verity(res['code'], '20000')

    def test_077_api_78dk_platform_ap_repayment_findCalculate(self):
        """
        提前还清试算-v1.5.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_ap_repayment_findCalculate(uid=contract_uuid, interestporid=''))
        Assertion.verity(res['code'], '20000')

    def test_078_api_78dk_platform_ap_repayment_findRepaymentList_none(self):
        """
        未结清列表--v1.5.0 , uuid为空
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_ap_repayment_findRepaymentList(uid='', interestporid=''))
        Assertion.verity(res['code'], '20000')

    def test_079_api_78dk_platform_ap_repayment_findRepaymentList(self):
        """
        未结清列表--v1.5.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_ap_repayment_findRepaymentList(uid=contract_uuid, interestporid=1))
        Assertion.verity(res['code'], '10000')

    def test_080_api_78dk_platform_om_contract_chargeback(self):
        """
        退单--美佳v1.0.4新增
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_chargeback(contractuuid='', retreatmoney=''))
        Assertion.verity(res['code'], '20000')

    def test_081_api_78dk_platform_om_contract_queryRefundInfo(self):
        """
        订单还款信息（v1.0.4）
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_queryRefundInfo(contractuuid=''))
        Assertion.verity(res['code'], '20000')

    def test_082_api_78dk_platform_lm_loandownLimit(self):
        """
        订单还款信息（v1.0.4）
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_lm_loandownLimit(contractuuid=''))
        Assertion.verity(res['code'], '20000')

    def test_083_om_repayment_deferredPayment(self):
        """
        延期还款-v1.0.6
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_repayment_deferredPayment(userbilluuid=''))
        Assertion.verity(res['code'], 'S0001')
        Assertion.verity(res['msg'], 'uuid异常')
