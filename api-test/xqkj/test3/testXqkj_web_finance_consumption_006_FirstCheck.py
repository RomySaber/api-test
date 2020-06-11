#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction

fake = Factory().create('zh_CN')


class testXqkj_web_finance_consumption_006_FirstCheck(TestBaseCase):
    def test_01_api_78dk_platform_tm_first_viewFirstCheckContract(self):
        global contract_uuid
        contract_uuid = xqkj_query.get_contract_uuid()
        # 初审信息查询
        merchant_uuid, product_name, contract_number, early_repayment_support = \
            xqkj_query.get_info('Tbl_Contract',
                                'merchant_uuid,product_name,contract_number,early_repayment_support',
                                'contract_uuid="{}"'.format(contract_uuid))
        # 查询商户名称
        merchant_name = xqkj_query.get_info('Tbl_MerchantProfile', 'name', 'merchant_uuid="{}"'.format(merchant_uuid))[
            0]
        res = PlatformAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(contract_uuid)
        # 法大大地址
        contract_uuidurl = xqkj_query.get_info('Tbl_ContractInfo', 'view_url',
                                               'contract_uuid="{}"'.format(contract_uuid))[0]
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['fddUrl'], contract_uuidurl)
        Assertion.verity(json.loads(res)['data']['earlyRepaymentSupport'], early_repayment_support)
        Assertion.verity(json.loads(res)['data']['merchantName'], merchant_name)
        Assertion.verity(json.loads(res)['data']['contractNumber'], contract_number)
        Assertion.verity(json.loads(res)['data']['productName'], product_name)

    def test_02_api_78dk_platform_tm_first_viewFirstCheckContracts(self):
        # 初审列表查询
        res = json.loads(PlatformAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name=''))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'dataList')

    def test_03_api_78dk_platform_tm_first_viewTongdunInfo(self):
        # 同盾信息查询
        res = PlatformAction.test_api_78dk_platform_tm_first_viewTongdunInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    # def test_04_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(self):
    #     # 查询合同已经填写的电核问题列表
    #     # {'uid': '合同uuid'}
    #     res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(contract_uuid)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     global contractUuid
    #     contractUuid = res['data'][0]['contractUuid']
    #     global groupName
    #     groupName = res['data'][0]['groupName']
    #     global question
    #     question = res['data'][0]['question']
    #     global riskType
    #     riskType = res['data'][0]['riskType']
    #     global state
    #     state = res['data'][0]['state']
    #     global telephoneCheckFeedbackUuid
    #     telephoneCheckFeedbackUuid = res['data'][0]['telephoneCheckFeedbackUuid']
    #     global groupSort
    #     groupSort = res['data'][0]['groupSort']
    #     global questionSort
    #     questionSort = res['data'][0]['questionSort']
    #
    # def test_05_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(self):
    #     # 批量添加电核资料(3)
    #     res = PlatformAction.test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(
    #         answer='答案', contractuuid=contractUuid, groupname=groupName, question=question, risktype=riskType,
    #         state=state, telephonecheckfeedbackuuid=telephoneCheckFeedbackUuid, groupsort=groupSort,
    #         questionsort=questionSort)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')

    def test_06_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(self):
        # 电核信息查询
        res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['data'], 'baiduLogUuid')

    def test_07_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(self):
        # 电核列表查询
        res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(
            pagesize=10, state='all', name='', pagecurrent=1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_08_api_78dk_platform_tm_final_viewFDDInfo(self):
        # 法大大信息查询
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFDDInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_09_api_78dk_platform_tm_final_viewFinalCheckContract(self):
        # 终审信息查询
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_10_api_78dk_platform_tm_final_viewFinalCheckContracts(self):
        # 终审列表查询
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFinalCheckContracts(
            pagecurrent=1, state='all', pagesize=1, name='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_11_api_78dk_platform_tm_first_viewImageDataConfig(self):
        # 查询影像列表
        res = PlatformAction.test_api_78dk_platform_tm_first_viewImageDataConfig(
            subdivisiontype='subdivision_type_home_installment')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_12_api_78dk_platform_tm_first_selectCanAuditCheck(self):
        # 是否有权限审核
        res = PlatformAction.test_api_78dk_platform_tm_first_selectCanAuditCheck(
            uid=contract_uuid, checktype='audit_check_first')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_13_api_78dk_platform_tm_first_addAuditComment_one(self):
        # 添加一条评论
        res = PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment=fake.text(max_nb_chars=10))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_14_api_78dk_platform_tm_first_addAuditComment_two(self):
        # 添加一条评论
        res = PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment=fake.text(max_nb_chars=50))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        global auditCommentUuid
        auditCommentUuid = json.loads(res)['data']['auditCommentUuid']

    def test_15_api_78dk_platform_tm_first_editAuditComment(self):
        # 编辑一条评论
        res = PlatformAction.test_api_78dk_platform_tm_first_editAuditComment(
            auditcommentuuid=auditCommentUuid, auditcommentattachments=[], contractuuid=contract_uuid,
            replyauditcommentuuid='', comment=fake.text(max_nb_chars=100))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        global delAuditCommentUuid
        delAuditCommentUuid = json.loads(res)['data']['auditCommentUuid']

    def test_16_api_78dk_platform_tm_first_delAuditComment(self):
        # 删除一条评论
        res = PlatformAction.test_api_78dk_platform_tm_first_delAuditComment(delAuditCommentUuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_17_api_78dk_platform_tm_first_findAuditCommentList(self):
        # 查询评论列表
        res = PlatformAction.test_api_78dk_platform_tm_first_findAuditCommentList(
            pagesize=10, pagecurrent=1, contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_18_api_78dk_platform_tm_first_updateContractInfoSignState(self):
        # 修改法大大合同签署状态 修改为重签
        res = PlatformAction.test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_19_api_78dk_platform_tm_after_viewAuditMonitors(self):
        # 贷后列表
        res = PlatformAction.test_api_78dk_platform_tm_after_viewAuditMonitors(
            enddate='', pagecurrent=1, pagesize=10, qifascore='', searchwhere='', startdate='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    # def test_20_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(self):
    #     # 删除电核资料(3)
    #     res = PlatformAction.test_api_78dk_platform_tm_telephone_deleteTelephoneCheckInfo(uid=contractUuid)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #
    # def test_021_api_78dk_platform_tm_first_viewContractImages(self):
    #     # 删除电核资料(3)
    #     res = PlatformAction.test_api_78dk_platform_tm_first_viewContractImages(contractuuid=contract_uuid)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #
    # def test_022_api_78dk_platform_tm_first_viewMxInfo(self):
    #     # 删除电核资料(3)
    #     res = PlatformAction.test_api_78dk_platform_tm_first_viewMxInfo(contractuuid=contract_uuid, type='1')
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')

