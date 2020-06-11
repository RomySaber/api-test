#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-06-11 下午 3:33
@Author     : 罗林
@File       : test_018_web_FirstCheck.py
@desc       : 信审管理自动化测试用例
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData as MD
from ymjry.query import xqkj_query
from ymjry.testAction import WebAction
from ymjry.testAction import loginAction

# from ymjry.testAction import specialAction

fake = Factory().create('zh_CN')
labelcontent = loginAction.sign + MD.words_cn(2)
customerinformation = loginAction.sign + MD.words_cn(2)
impactdata = loginAction.sign + MD.words_cn(2)
windcontroldatasource = loginAction.sign + MD.words_en_lower(2)


class test_018_web_FirstCheck(TestBaseCase):
    def test_001_active_contract(self):
        """
        激活订单，修改订单状态未机审通过
        :return:
        """
        global contract_uuid, app_user_uuid
        app_user_uuid = loginAction.get_user_uuid()
        contract_uuid = xqkj_query.get_contract_uuid_for_user(app_user_uuid)
        # contract_uuid = '3222d8b7acac4a45a91f0b1b01bd6fec'

        # contract_uuid = xqkj_query.get_contract_uuid_for_machine()
        loginAction.global_dict.set(contract_uuid=contract_uuid)
        loginAction.global_dict.set(app_user_uuid=app_user_uuid)
        # 修改订单状态为机审通过
        xqkj_query.update_contract_machine_pass(contract_uuid, app_user_uuid)

    @unittest.skip('每次都会发送短信')
    def test_002_api_78dk_platform_tm_first_firstCheck_fail(self):
        """
        初审 不通过
        """
        xqkj_query.update_contract_machine_first_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_first_firstCheck(
            uuid=contract_uuid, message='初审 不通过', checkstate='fail')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_003_api_78dk_platform_tm_first_viewFirstCheckContract_fail(self):
        """
        初审信息查询 初审 不通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_004_api_78dk_platform_tm_first_viewFirstCheckContracts_fail(self):
        """
        初审列表查询 初审 不通过
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username=''))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'dataList')

    @unittest.skip('每次都会发送短信')
    def test_005_api_78dk_platform_tm_first_firstCheck_cancel(self):
        """
        初审  取消
        """
        xqkj_query.update_contract_machine_first_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_first_firstCheck(
            uuid=contract_uuid, message='初审  取消', checkstate='cancel')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_006_api_78dk_platform_tm_first_viewFirstCheckContract_cancel(self):
        """
        初审信息查询 初审  取消
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_007_api_78dk_platform_tm_first_viewFirstCheckContracts_cancel(self):
        """
        初审列表查询  初审  取消
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username=''))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'dataList')

    def test_008_api_78dk_platform_tm_first_firstCheck_cancel_pass(self):
        """
        初审  通过
        """
        xqkj_query.update_contract_machine_first_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_first_firstCheck(
            uuid=contract_uuid, message='初审  通过', checkstate='pass')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_009_api_78dk_platform_tm_first_viewFirstCheckContract_pass(self):
        """
        初审信息查询  初审  通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_010_api_78dk_platform_tm_first_viewFirstCheckContracts_pass(self):
        """
        初审列表查询  初审  通过
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username=''))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'dataList')

    def test_011_api_78dk_platform_tm_first_viewTongdunInfo(self):
        """
        同盾信息查询
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewTongdunInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_012_api_78dk_platform_tm_first_viewMxInfo(self):
        """
        查询魔蝎报告
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewMxInfo(contractuuid=contract_uuid, type='1')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '通过合同UUID查询不到魔蝎数据!')

    def test_013_api_78dk_platform_tm_first_viewContractImages(self):
        """
        审核详情-影像资料(新)
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractImages(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_014_api_78dk_platform_tm_first_viewImageDataConfig_home(self):
        """
        查询影像列表 家装分期
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewImageDataConfig(
            subdivisiontype='subdivision_type_home_installment')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_014_api_78dk_platform_tm_first_viewImageDataConfig_earnest(self):
        """
        查询影像列表 定金分期
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewImageDataConfig(
            subdivisiontype='subdivision_type_earnest_installment')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_015_api_78dk_platform_tm_first_selectCanAuditCheck(self):
        """
        是否有权限审核
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_selectCanAuditCheck(
            uid=contract_uuid, checktype='audit_check_first')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_016_api_78dk_platform_tm_first_addAuditComment_one(self):
        """
        添加一条评论
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment=fake.text(max_nb_chars=10))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_017_api_78dk_platform_tm_first_addAuditComment_two(self):
        """
        添加一条评论
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment=fake.text(max_nb_chars=50))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        global auditCommentUuid
        auditCommentUuid = json.loads(res)['data']['auditCommentUuid']

    def test_018_api_78dk_platform_tm_first_editAuditComment(self):
        """
        编辑一条评论
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_editAuditComment(
            auditcommentuuid=auditCommentUuid, auditcommentattachments=[], contractuuid=contract_uuid,
            replyauditcommentuuid='', comment=fake.text(max_nb_chars=100))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        global delAuditCommentUuid
        delAuditCommentUuid = json.loads(res)['data']['auditCommentUuid']

    def test_019_api_78dk_platform_tm_first_delAuditComment(self):
        """
        删除一条评论
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_delAuditComment(delAuditCommentUuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_020_api_78dk_platform_tm_first_findAuditCommentList(self):
        """
        查询评论列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_first_findAuditCommentList(
            pagesize=10, pagecurrent=1, contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    # def test_021_api_78dk_platform_tm_first_updateContractInfoSignState(self):
    #     """
    #     修改法大大合同签署状态 修改为重签
    #     :return:
    #     """
    #     res = WebAction.test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(contract_uuid)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')

    def test_022_api_78dk_platform_tm_after_viewAuditMonitors(self):
        # 贷后列表
        res = WebAction.test_api_78dk_platform_tm_after_viewAuditMonitors(
            enddate='', pagecurrent=1, pagesize=10, qifascore='', searchwhere='', startdate='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('每次都会发送短信')
    def test_023_api_78dk_platform_tm_telephone_telephoneCheck_fail(self):
        """
        电核  不通过
        :return:
        """
        xqkj_query.update_contract_machine_telephone_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_telephone_telephoneCheck(
            uuid=contract_uuid, message='电核不通过', checkstate='fail')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_024_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_fail(self):
        """
        电核信息查询  电核  不通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['data'], 'baiduLogUuid')

    def test_025_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts_fail(self):
        """
        电核列表查询  电核  不通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(
            pagesize=10, state='all', name='', pagecurrent=1, begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('每次都会发送短信')
    def test_026_api_78dk_platform_tm_telephone_telephoneCheck_cancel(self):
        """
        电核 取消
        :return:
        """
        xqkj_query.update_contract_machine_telephone_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_telephone_telephoneCheck(
            uuid=contract_uuid, message='电核取消', checkstate='cancel')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_027_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_cancel(self):
        """
        电核信息查询 电核 取消
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['data'], 'baiduLogUuid')

    def test_028_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts_cancel(self):
        """
        电核列表查询 电核 取消
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(
            pagesize=10, state='all', name='', pagecurrent=1, begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_029_api_78dk_platform_tm_telephone_telephoneCheck_fail_pass(self):
        """
        电核 通过
        :return:
        """
        xqkj_query.update_contract_machine_telephone_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_telephone_telephoneCheck(
            uuid=contract_uuid, message='电核通过', checkstate='pass')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_030_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(self):
        """
        电核信息查询  电核 通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['data'], 'baiduLogUuid')

    def test_031_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(self):
        """
        电核列表查询  电核 通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(
            pagesize=10, state='all', name='', pagecurrent=1, begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_032_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(self):
        """
        查询合同已经填写的电核问题列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_033_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(self):
        """
        批量添加电核资料(3)
        :return:
        """
        WebAction.test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(
            answer='答案', contractuuid=contract_uuid, groupname='', question='', risktype='',
            state='', telephonecheckfeedbackuuid='', groupsort='',
            questionsort='')
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

    def test_034_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(self):
        """
        删除电核资料(3)
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_035_api_78dk_platform_tm_final_viewFDDInfo(self):
        """
        法大大信息查询
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFDDInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_036_api_78dk_platform_tm_final_finalCheck_cancel(self):
        """
        终审 终审取消
        :return:
        """
        xqkj_query.update_contract_machine_final_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(
            checkstate='终审取消', uuid=contract_uuid, message='cancel', preamount='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试, 美佳')
    def test_037_api_78dk_platform_tm_final_viewFinalCheckContract_cancel(self):
        """
        终审信息查询  终审取消
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_038_api_78dk_platform_tm_final_viewFinalCheckContracts_cancel(self):
        """
        终审列表查询  终审取消
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContracts(
            pagecurrent=1, state='all', pagesize=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('需要再次调试, meijia')
    def test_039_api_78dk_platform_tm_final_finalCheck_fail(self):
        """
        终审  终审失败
        :return:
        """
        xqkj_query.update_contract_machine_final_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(
            checkstate='终审失败', uuid=contract_uuid, message='fail', preamount='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_040_api_78dk_platform_tm_final_viewFinalCheckContract_fail(self):
        """
        终审信息查询  终审失败
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_041_api_78dk_platform_tm_final_viewFinalCheckContracts_fail(self):
        """
        终审列表查询  终审失败
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContracts(
            pagecurrent=1, state='all', pagesize=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试, meijia')
    def test_042_api_78dk_platform_tm_final_finalCheck_pass(self):
        """
        终审 终审通过
        :return:
        """
        xqkj_query.update_contract_machine_final_check(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(
            checkstate='"pass"', uuid=contract_uuid, message='终审通过', preamount='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_043_api_78dk_platform_tm_final_viewFinalCheckContract_pass(self):
        """
        终审信息查询  终审通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_044_api_78dk_platform_tm_final_viewFinalCheckContracts_pass(self):
        """
        终审列表查询  终审通过
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContracts(
            pagecurrent=1, state='all', pagesize=1, name='', begindate='', contractnumber='', enddate='', lable='',
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_045_api_78dk_platform_tm_after_viewReportContract(self):
        """
        查询报告内容
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_after_viewReportContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_046_api_78dk_platform_tm_after_viewContractTongDuns(self):
        """
        查询贷后所用同盾报告列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_after_viewContractTongDuns(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_047_api_78dk_platform_tm_after_viewAuditMonitors(self):
        """
        贷后列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_tm_after_viewAuditMonitors(
            searchwhere='', startdate='', qifascore='', pagecurrent=1, pagesize=10, enddate='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_048_api_78dk_bm_viewUserBill(self):
        """
        个人账单
        :return:
        """
        res = WebAction.test_api_78dk_bm_viewUserBill(contractuuid=contract_uuid, pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_049_api_78dk_bm_viewBillList_all(self):
        """
        账单列表
        :return:
        """
        res = WebAction.test_api_78dk_bm_viewBillList(state='', pagecurrent=1, pagesize=10, merchantname='',
                                                      contractnumber='', usermobile='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_050_api_78dk_bm_viewBillList_active(self):
        """
        账单列表
        :return:
        """
        res = WebAction.test_api_78dk_bm_viewBillList(
            state='123', pagecurrent=1, pagesize=10, merchantname='', contractnumber='', usermobile='',
            username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_051_api_78dk_platform_lm_viewContract(self):
        """
        合同信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_052_api_78dk_platform_lm_downPayMoneys(self):
        # 导出打款信息
        res = WebAction.test_api_78dk_platform_lm_downPayMoneys(
            enddate='', begindate='', contractnumber='', loanstate='', merchantname='', phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_053_api_78dk_platform_lm_downLoans(self):
        # 导出放款列表
        res = WebAction.test_api_78dk_platform_lm_downLoans(
            enddate='', begindate='', contractnumber='', loanstate='', merchantname='', phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_054_api_78dk_platform_lm_offLineLoan(self):
        # 放款
        res = WebAction.test_api_78dk_platform_lm_offLineLoan(
            bankseqid='', contractuuid=contract_uuid, loanamount='', remarks='', url='', urlname='')
        Assertion.verity(json.loads(res)['msg'], 'url不能为空!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_055_api_78dk_platform_lm_viewLoans(self):
        """
        放款列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewLoans(
            begindate='', contractnumber='', enddate='', loanstate='', merchantname='', pagecurrent=1, pagesize=10,
            phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_056_api_78dk_platform_lm_viewLoanDetil(self):
        """
        查看放款详情
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewLoanDetil(contract_uuid)
        # Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_057_api_78dk_platform_lm_viewUserBill_all(self):
        """
        账单信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewUserBill(
            begindate='', enddate='', name='', orderstate='', pagecurrent=1, pagesize=10, state='all',
            uuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_058_api_78dk_platform_lm_viewUserBill_pass(self):
        """
        账单信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewUserBill(
            begindate='', enddate='', name='', orderstate='', pagecurrent=1, pagesize=10, state='pass',
            uuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_059_api_78dk_platform_lm_viewUserBill_fail(self):
        """
        账单信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewUserBill(
            begindate='', enddate='', name='', orderstate='', pagecurrent=1, pagesize=10, state='fail',
            uuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('需要再次调试')
    def test_060_api_78dk_platform_tm_first_viewFirstCheckContract(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审信息查询(新)
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(uid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_061_api_78dk_platform_tm_first_viewFirstCheckContract_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审信息查询(新),查询不存在的合同初审信息
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(uid='-1')
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_062_api_78dk_platform_tm_first_viewFirstCheckContract_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审信息查询(新),合同id超长
        """
        contract_uuid1 = MD.words_en_lower(24)
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(uid=contract_uuid1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_063_api_78dk_platform_tm_first_viewFirstCheckContract_id_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审信息查询(新),合同id为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(uid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不能为空!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_064_api_78dk_platform_tm_first_viewFirstCheckContract_id_is_None(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审信息查询(新),合同id为None
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(uid=None)
        Assertion.verityContain(json.loads(res)['msg'], '系统发生内部异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_065_api_78dk_platform_tm_first_viewFirstCheckContracts_pass(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审列表查询v1.3.0,查询成功
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='pass', pagecurrent=1,
            name='', begindate='', contractnumber='', enddate='', lable='', phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_066_api_78dk_platform_tm_first_viewFirstCheckContracts_fail(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审列表查询v1.3.0,查询失败的列表
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='fail', pagecurrent=1, name='', begindate='', contractnumber='', enddate='',
            lable='', phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_067_api_78dk_platform_tm_first_viewFirstCheckContracts_contractnumber_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 初审列表查询v1.3.0,合同编号不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name='', begindate='', contractnumber=-1,
            enddate='', lable='', phone='', username='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('无结算')
    def test_068_api_78dk_platform_tm_first_businessbillinginformation(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 商户结算信息查询接口 - V1.3 新增
        """
        res = WebAction.test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('无结算')
    def test_069_api_78dk_platform_tm_first_businessbillinginformation_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 商户结算信息查询接口 - V1.3 新增,contractuuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('无结算')
    def test_070_api_78dk_platform_tm_first_businessbillinginformation_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 商户结算信息查询接口 - V1.3 新增,contractuuid超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid=MD.number(256))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('无结算')
    def test_071_api_78dk_platform_tm_first_businessbillinginformation_contractuuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 商户结算信息查询接口 - V1.3 新增,contractuuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_businessbillinginformation(contractuuid='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_073_tm_final_viewFinalCheckContract_null(self):
        """
        desc       : 终审信息查询（v1.0.2修改）
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(uid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_074_tm_final_viewFinalCheckContract_error(self):
        """
        desc       : 终审信息查询（v1.0.2修改）
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(uid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_075_tm_final_viewFinalCheckContract_error(self):
        """
        desc       : 终审信息查询（v1.0.2修改）
        """
        res = WebAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(uid=contract_uuid)
        Assertion.verityContain(json.loads(res)['data']['authenticationState'], 'authentication_state_pass')
        Assertion.verity(json.loads(res)['code'], '10000')
