#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from xqkj.testAction import PlatformAction
from xqkj.testAction import loginAction

fake = Factory().create('zh_CN')

# 查询没有被审核的订单 取值最新的一条
sql = 'UPDATE Tbl_Contract SET contract_state=\'not_active\' WHERE user_id=27;'
MysqlClent.executed_all(loginAction.DB, sql)
sql = "SELECT Tbl_Contract.contract_uuid FROM Tbl_Contract LEFT OUTER JOIN Tbl_FirstCheckLog  ON " \
      "Tbl_Contract.id = Tbl_FirstCheckLog.contract_id WHERE Tbl_FirstCheckLog.id IS NULL AND " \
      "Tbl_Contract.qifa_machine_audit='qifa_merchant_audit_pass' AND " \
      "Tbl_Contract.first_check='first_check_pending' ORDER BY Tbl_Contract.id DESC;"

contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
print(contract_uuid_d)
print('查询用户的可用订单 contract_uuid', contract_uuid_d[0][0])
contract_uuid = contract_uuid_d[0][0]


class testPlatform_006_FirstCheck(TestBaseCase):
    def test_01api_78dk_platform_tm_first_viewFirstCheckContract(self):
        # 初审信息查询
        # {'uid': '合同uuid'}
        # contract_uuid = '1e9fe3d0be2344e2acfda1a025a607e2'
        sql = 'contract_uuid="' + contract_uuid + '" and state ="enabled"'
        channelid = MysqlClent.select(loginAction.DB, 'Tbl_Contract', condition=sql)
        # print(type(channelid[0]),channelid[0])
        # 查询商户名称
        sql = 'id="' + str(channelid[0][4]) + '" and state ="enabled"'
        merchantname = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'name', sql)
        # 查询资金包
        sql = 'id="' + str(channelid[0][6]) + '" and state ="enabled"'
        fundname = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'name', sql)
        print(merchantname, fundname, channelid[0][22])
        # fundSideName 资方名称
        sql = 'select Tbl_FundSide.name from Tbl_FundSide ,Tbl_FundPackage,Tbl_FundSidePackageRelation WHERE ' \
              'Tbl_FundPackage.id={} and Tbl_FundPackage.id=Tbl_FundSidePackageRelation.fund_package_id and ' \
              'Tbl_FundSide.id=Tbl_FundSidePackageRelation.fund_side_id ;'.format(channelid[0][6])
        fundsidename = MysqlClent.executed_one(loginAction.DB, sql)

        res = PlatformAction.test_api_78dk_platform_tm_first_viewFirstCheckContract(contract_uuid)
        # # 法大大地址：
        contract_uuidurl = 'select Tbl_ContractInfo.view_url from Tbl_ContractInfo,Tbl_Contract where ' \
                           'Tbl_Contract.contract_uuid=\'{}\' and Tbl_Contract.id=Tbl_ContractInfo.contract_id' \
            .format(contract_uuid)
        contract_uuid1 = MysqlClent.executed_one(loginAction.DB, contract_uuidurl)
        # # 分数
        score = 'select score from Tbl_QifaMachineLog where contract_uuid=\'{}\';'.format(contract_uuid)
        score1 = MysqlClent.executed_all(loginAction.DB, score)
        # 查询门店信息
        storenamesql = 'select Tbl_Store.business_address from Tbl_Store,Tbl_Contract where ' \
                       'Tbl_Contract.storm_id={} and Tbl_Contract.storm_id=Tbl_Store.id and ' \
                       'Tbl_Contract.contract_uuid=\'{}\';'.format(channelid[0][5], contract_uuid)
        storename = MysqlClent.executed_all(loginAction.DB, storenamesql)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['fddUrl'], contract_uuid1)
        Assertion.verity(json.loads(res)['data']['earlyRepaymentSupport'], channelid[0][21])
        Assertion.verity(json.loads(res)['data']['merchantName'], merchantname)
        # Assertion.verity(json.loads(res)['data']['aliscore'], '550000.00000000')
        Assertion.verity(json.loads(res)['data']['contractNumber'], channelid[0][8])
        Assertion.verity(json.loads(res)['data']['fundPackageName'], fundname)
        # Assertion.verity(json.loads(res)['data']['score'], str(score1[0][0]))
        Assertion.verity(json.loads(res)['data']['fundSideName'], fundsidename)
        # Assertion.verity(json.loads(res)['data']['repaymentMethod'], 'DBDX')
        # Assertion.verity(json.loads(res)['data']['storeName'], storename[0][0])
        # 查询商户贴息费率  discount_rate
        discountRatesql = 'select discount_rate FROM Tbl_Contract WHERE contract_uuid="{}" ' \
                          'and state ="enabled" '.format(contract_uuid)
        discountRate = MysqlClent.executed_all(loginAction.DB, discountRatesql)
        print('bbbbbbbbbbbbbbbbb', discountRate)
        # Assertion.verity(json.loads(res)['data']['discountRate'], discountRate[0][0])
        # 查询产品名称
        productNamesql = ' select Tbl_ProductDetail.name from Tbl_ProductDetail,Tbl_Contract where ' \
                         'Tbl_Contract.product_id=Tbl_ProductDetail.id and Tbl_Contract.contract_uuid=\'{}\'; ' \
            .format(contract_uuid)
        productName = MysqlClent.executed_all(loginAction.DB, productNamesql)
        Assertion.verity(json.loads(res)['data']['productName'], productName[0][0])
        Assertion.verity(json.loads(res)['data']['aliOpinion'], '网商审核通过')
        # 查询期数信息
        loanPeriodssql = 'SELECT loan_periods FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        loanPeriods = MysqlClent.executed_all(loginAction.DB, loanPeriodssql)
        Assertion.verity(json.loads(res)['data']['loanPeriods'], loanPeriods[0][0])
        # 查询个人基本资料
        personsql = 'SELECT tpb.* FROM Tbl_Contract tc, Tbl_ContractPersonBasicRelation tcpr, Tbl_PersonBasicInfo tpb ' \
                    'where tc.contract_uuid=\'{}\' and tc.id=tcpr.contract_id and tcpr.person_basic_info_id=tpb.id;' \
            .format(contract_uuid)
        person = MysqlClent.executed_all(loginAction.DB, personsql)
        # Assertion.verity(json.loads(res)['data']['person'], '个人基本资料')
        Assertion.verity(json.loads(res)['data']['person']['homeType'], person[0][6])
        Assertion.verity(json.loads(res)['data']['person']['idCardNumber'], person[0][3])
        Assertion.verity(json.loads(res)['data']['person']['immediateFamilyName'], person[0][7])
        Assertion.verity(json.loads(res)['data']['person']['immediateFamilyPhone'], person[0][9])
        Assertion.verity(json.loads(res)['data']['person']['immediateFamilyRelation'], person[0][8])
        Assertion.verity(json.loads(res)['data']['person']['name'], person[0][2])
        Assertion.verity(json.loads(res)['data']['person']['phone'], person[0][4])
        Assertion.verity(json.loads(res)['data']['person']['typeOfJob'], person[0][5])
        # 查询 overdue_handling_fee_rate  逾期手续费率 - 手续费'
        overdue_handling_fee_ratesql = 'SELECT overdue_handling_fee_rate FROM Tbl_Contract where contract_uuid=\'{}\';' \
            .format(contract_uuid)
        overdueHandlingFeeRate = MysqlClent.executed_all(loginAction.DB, overdue_handling_fee_ratesql)
        # Assertion.verity(json.loads(res)['data']['overdueHandlingFeeRate'], overdueHandlingFeeRate[0][0])
        # 提前还款手续费
        earlyRepaymentHandlingFeesql = 'SELECT early_repayment_handling_fee FROM Tbl_Contract where contract_uuid=\'{}\';' \
            .format(contract_uuid)
        earlyRepaymentHandlingFee = MysqlClent.executed_all(loginAction.DB, earlyRepaymentHandlingFeesql)
        # Assertion.verity(json.loads(res)['data']['earlyRepaymentHandlingFee'], earlyRepaymentHandlingFee[0][0])
        # submit_state
        submitStatesql = 'SELECT submit_state FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        submitState = MysqlClent.executed_all(loginAction.DB, submitStatesql)
        # Assertion.verity(json.loads(res)['data']['submitState'], submitState[0][0])
        # 用户签订日期查询
        signingDatesql = 'SELECT signing_date FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        signingDate = MysqlClent.executed_all(loginAction.DB, signingDatesql)
        # Assertion.verity(json.loads(res)['data']['signingDate'], signingDate[0][0])
        # 查询分期手续费率   精度问题
        periodRatesql = 'SELECT period_rate FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        periodRate = MysqlClent.executed_all(loginAction.DB, periodRatesql)
        # Assertion.verity(json.loads(res)['data']['periodRate'], periodRate[0][0])
        #  查询宽限期
        gracePeriodsql = 'SELECT grace_period FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        gracePeriod = MysqlClent.executed_all(loginAction.DB, gracePeriodsql)
        # Assertion.verity(json.loads(res)['data']['gracePeriod'], gracePeriod[0][0])
        # 查询贷款金额 loan_amount   精度问题  '20000' != Decimal('20000.00000000')
        loan_amountsql = 'SELECT loan_amount FROM Tbl_Contract where contract_uuid=\'{}\';'.format(contract_uuid)
        loanAmount = MysqlClent.executed_all(loginAction.DB, loan_amountsql)
        # Assertion.verity(json.loads(res)['data']['loanAmount'], loanAmount[0][0])
        # 查询   逾期手续费率 - 本金
        overduePrincipalRatesql = 'SELECT overdue_principal_rate FROM Tbl_Contract where contract_uuid=\'{}\';'.format(
            contract_uuid)
        overduePrincipalRate = MysqlClent.executed_all(loginAction.DB, overduePrincipalRatesql)
        # Assertion.verity(json.loads(res)['data']['overduePrincipalRate'], overduePrincipalRate[0][0])
        # 提前还款周期
        earlyRepaymentFreeCyclesql = 'SELECT early_repayment_free_cycle FROM Tbl_Contract where contract_uuid=\'{}\';'.format(
            contract_uuid)
        earlyRepaymentFreeCycle = MysqlClent.executed_all(loginAction.DB, earlyRepaymentFreeCyclesql)
        # 支付宝审核日志
        alipayAuditLogssql = 'SELECT talog.opinion,talog.alipay_audit FROM Tbl_Contract tc ,Tbl_AlipayAuditLog talog  ' \
                             'where tc.contract_uuid=\'{}\' and talog.contract_id=tc.id;'.format(contract_uuid)
        alipayAuditLogs = MysqlClent.executed_all(loginAction.DB, alipayAuditLogssql)
        Assertion.verity(json.loads(res)['data']['alipayAuditLogs']['opinion'], alipayAuditLogs[0][0])
        # 影响资料信息
        contractImagessql = 'SELECT tcim.* FROM Tbl_Contract tc ,Tbl_ContractImage tcim where tc.contract_uuid=\'{}\'' \
                            ' and tc.id=tcim.contract_id ORDER BY tcim.id ASC;'.format(contract_uuid)
        contractImages = MysqlClent.executed_all(loginAction.DB, contractImagessql)
        # 身份证照片(正面)
        Assertion.verity(json.loads(res)['data']['contractImages'][0]['key'], contractImages[0][4])
        Assertion.verity(json.loads(res)['data']['contractImages'][0]['keyName'], contractImages[0][6])
        # 身份证照片(反面)
        Assertion.verity(json.loads(res)['data']['contractImages'][1]['key'], contractImages[1][4])
        Assertion.verity(json.loads(res)['data']['contractImages'][1]['keyName'], contractImages[1][6])

    def test_02api_78dk_platform_tm_first_viewFirstCheckContracts(self):
        # 初审列表查询
        # {'name': '编号等一系列东西', 'state': '状态', 'pageSize': '页面大小', 'pageCurrent': '当前页'}
        res = PlatformAction.test_api_78dk_platform_tm_first_viewFirstCheckContracts(
            pagesize=10, state='all', pagecurrent=1, name='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_03api_78dk_platform_tm_first_viewTongdunInfo(self):
        # 同盾信息查询
        # {'uid': '同盾uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_first_viewTongdunInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_04api_78dk_platform_tm_telephone_viewTelephoneCheckContract(self):
        # 电核信息查询
        # {'uid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_05api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(self):
        # 电核列表查询
        # {'name': '编号等一系列东西', 'state': '状态', 'pageSize': '页面大小', 'pageCurrent': '当前页'}
        res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(
            pagesize=10, state='all', name='', pagecurrent=1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_06api_78dk_platform_tm_final_viewFDDInfo(self):
        # 法大大信息查询
        # {'uid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFDDInfo(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_07api_78dk_platform_tm_final_viewFinalCheckContract(self):
        # 终审信息查询
        # {'uid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFinalCheckContract(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_08api_78dk_platform_tm_final_viewFinalCheckContracts(self):
        # 终审列表查询
        # {'name': '编号等一系列东西', 'state': '状态', 'pageSize': '页面大小', 'pageCurrent': '当前页'}
        res = PlatformAction.test_api_78dk_platform_tm_final_viewFinalCheckContracts(
            pagecurrent=1, state='all', pagesize=1, name='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_09api_78dk_platform_tm_first_viewImageDataConfig(self):
        #     #查询影像列表
        res = PlatformAction.test_api_78dk_platform_tm_first_viewImageDataConfig(
            subdivisiontype='subdivision_type_home_installment')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_10api_78dk_platform_tm_first_selectCanAuditCheck(self):
        # 是否有权限审核  {"checkType":"audit_check_first","uid":"9b34a53921b64d608f507c21f0ba1218"}
        # {'checkType': '数据类型', 'uid': '合同uuid'} {"code":"10000","data":"can_audit_check_state_forbid","msg":"成功"}
        res = PlatformAction.test_api_78dk_platform_tm_first_selectCanAuditCheck(uid=contract_uuid,
                                                                                 checktype='audit_check_first')
        print('是否有权限审核', json.loads(res))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # can_audit_check_state_allow 允许
        # Assertion.verity(json.loads(res)['data'], 'can_audit_check_state_forbid')

    def test_11api_78dk_platform_tm_first_getSupplementImages(self):
        # 查询用户能补录的图片资料
        # {'uid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_first_getSupplementImages(contract_uuid)
        print('查询用户能补录的图片资料', json.loads(res))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['data']['images'], '图片影像资料实体')
        # Assertion.verity(json.loads(res)['data']['keyName'], '分类配置key名称')
        # Assertion.verity(json.loads(res)['data']['key'], '图片配置key')

    def test_12api_78dk_platform_tm_first_addAuditComment(self):
        # 添加一条评论
        res = PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='', comment='544543534543')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_13api_78dk_platform_tm_first_editAuditComment(self):
        # 编辑一条评论
        # 新增评论两条
        comnent = '<p>啛啛喳喳错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错错' \
                  '错错错错错错错错错错错错错错错错错错咕咕咕咕过过过过过过过过过过过过4444444444过过' \
                  '过过过过过过过过过过过过过过过过过过过过过过过过过错错错错错错</p>'
        PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment='<p>435435435</p>')
        res = PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='', comment=comnent)
        comnent = '<p>编辑后的错错错错错错错错错错错错错错错错咕咕咕咕过过过过过过过过过过过过4444444444过过' \
                  '过过过过过过过过过过过过过过过过过过过过过过过过过错</p>'
        commetid = json.loads(res)['data']['auditCommentUuid']
        print(commetid)
        res = PlatformAction.test_api_78dk_platform_tm_first_editAuditComment(
            auditcommentuuid='', auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid=commetid,
            comment=comnent)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_14api_78dk_platform_tm_first_delAuditComment(self):
        # 删除一条评论
        res1 = PlatformAction.test_api_78dk_platform_tm_first_addAuditComment(
            auditcommentattachments=[], contractuuid=contract_uuid, replyauditcommentuuid='',
            comment='删除评论435435435')
        res2 = PlatformAction.test_api_78dk_platform_tm_first_delAuditComment(
            json.loads(res1)['data']['auditCommentUuid'])
        Assertion.verity(json.loads(res2)['msg'], '成功')
        Assertion.verity(json.loads(res2)['code'], '10000')

    def test_15api_78dk_platform_tm_first_findAuditCommentList(self):
        # 查询评论列表
        # {'pageCurrent': '当前页', 'pageSize': '页面大小', 'contractUuid': '合同 UUID'}
        res = PlatformAction.test_api_78dk_platform_tm_first_findAuditCommentList(pagesize=10, pagecurrent=1,
                                                                                  contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_16api_78dk_platform_tm_first_saveSupplementImage(self):
        # 初审时-----提交或编辑补录资料 -----只有审核员自己审核的订单才能进行编辑审核
        sql = ''
        contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
        backGroundSupplementImages = [{
            "imageName": "装修合同照片自动上传初审",
            "key": "YHZXHTZP",
            "url": "2db6/99882db693a9aabc1f7a54ce7a5e1b4a805a.png"
        }]
        res = PlatformAction.test_api_78dk_platform_tm_first_saveSupplementImage(
            supplementimagetype='supplement_image_type_submit', auditchecktype='audit_check_first',
            backgroundsupplementimages=backGroundSupplementImages, contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['newImageName'], '新图片名称')
        Assertion.verity(json.loads(res)['data']['newImageUuid'], '新补录的图片UUID')
        Assertion.verity(json.loads(res)['data']['originalImageUuid'], '需要补录的图片UUID')

    def test_17api_78dk_platform_tm_first_viewBaiDuInfo(self):
        # 查询百度接口  baiduLogUuid
        # {'uid': '百度uuid'}
        res1 = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        res = PlatformAction.test_api_78dk_platform_tm_first_viewBaiDuInfo(json.loads(res1)['data']['baiduLogUuid'])
        print(json.loads(res)['data'])
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_18api_78dk_platform_tm_first_viewTencentInfo(self):
        # 查询腾讯接口
        # {'uid': '腾讯uuid'}  tencentLogUuid
        res1 = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(contract_uuid)
        res = PlatformAction.test_api_78dk_platform_tm_first_viewTencentInfo(json.loads(res1)['data']['baiduLogUuid'])
        print(json.loads(res)['data'])
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_19api_78dk_platform_tm_first_firstCheck(self):
        # 初审   {"isAdopt":true,"key":[],"message":"66666666666","uuid":"c23f3fae9d0c435c96368532565a49a4"}
        # {'isAdopt': '是否通过', 'message': '审核人提交信息', 'uuid': '合同uuid'} 审核通过
        res = PlatformAction.test_api_78dk_platform_tm_first_firstCheck(
            uuid=contract_uuid, message='接口自动通过', checkstate='pass')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_20api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(self):
        # 查询合同已经填写的电核问题列表
        # {'uid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_21api_78dk_platform_tm_telephone_addTelephoneCheckInfos(self):
        # 批量添加电核资料
        res = json.loads(
            PlatformAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(contract_uuid))
        contractUuid = res['data'][0]['contractUuid']
        groupName = res['data'][0]['groupName']
        question = res['data'][0]['question']
        riskType = res['data'][0]['riskType']
        state = res['data'][0]['state']
        telephoneCheckFeedbackUuid = res['data'][0]['telephoneCheckFeedbackUuid']
        groupSort = res['data'][0]['groupSort']
        questionSort = res['data'][0]['questionSort']
        res = PlatformAction.test_api_78dk_platform_tm_telephone_addTelephoneCheckInfos(
            answer='答案', contractuuid=contractUuid, groupname=groupName, question=question, risktype=riskType,
            state=state, telephonecheckfeedbackuuid=telephoneCheckFeedbackUuid, groupsort=groupSort,
            questionsort=questionSort)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_22api_78dk_platform_tm_first_saveSupplementImage(self):
        # 电核时-----提交或编辑补录资料 -----只有审核员自己审核的订单才能进行编辑审核
        sql = 'SELECT tc.* FROM Tbl_Contract tc  LEFT JOIN Tbl_TelephoneCheckLog ttl ' \
              'ON tc.contract_uuid=ttl.contract_uuid  WHERE ttl.contract_uuid IS NULL ' \
              'AND tc.telephone_check=\'telephone_check_pending\' ' \
              'AND tc.first_check=\'first_check_pass\' ORDER BY tc.id ASC;'
        contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
        # {'backGroundSupplementImages': '补录资料实体', 'supplementImageType': '后台编辑或提交类型', 'contractUuid': '合同UUID'}
        backGroundSupplementImages = [{
            "imageName": "装修合同照片自动上传电核",
            "key": "YHZXHTZP",
            "url": "2db6/99882db693a9aabc1f7a54ce7a5e1b4a805a.png"
        }]
        res = PlatformAction.test_api_78dk_platform_tm_first_saveSupplementImage(
            backgroundsupplementimages=backGroundSupplementImages, contractuuid=contract_uuid,
            supplementimagetype='supplement_image_type_submit', auditchecktype='audit_check_telephone')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_23api_78dk_platform_tm_telephone_telephoneCheck(self):
        # 电核
        # {'isAdopt': '是否通过', 'message': '审核人提交信息', 'uuid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_telephone_telephoneCheck(uuid=contract_uuid, message='接口自动通过',
                                                                                checkstate='pass')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_25api_78dk_platform_tm_first_saveSupplementImage(self):
        # 终审时-----提交或编辑补录资料 -----只有审核员自己审核的订单才能进行编辑审核
        sql = 'SELECT tc.* FROM Tbl_Contract tc  LEFT JOIN Tbl_TelephoneCheckLog ttl ' \
              'ON tc.contract_uuid=ttl.contract_uuid  WHERE ttl.contract_uuid IS NULL ' \
              'AND tc.telephone_check=\'telephone_check_pending\' ' \
              'AND tc.first_check=\'first_check_pass\' ORDER BY tc.id ASC;'
        contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
        backGroundSupplementImages = [{
            "imageName": "装修合同照片自动上传终审",
            "key": "YHZXHTZP",
            "url": "2db6/99882db693a9aabc1f7a54ce7a5e1b4a805a.png"
        }]
        res = PlatformAction.test_api_78dk_platform_tm_first_saveSupplementImage(
            supplementimagetype='supplement_image_type_submit', auditchecktype='audit_check_final',
            backgroundsupplementimages=backGroundSupplementImages, contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_26api_78dk_platform_tm_final_finalCheck(self):
        # 终审
        # {'isAdopt': '是否通过', 'message': '审核人提交信息', 'uuid': '合同uuid'}
        res = PlatformAction.test_api_78dk_platform_tm_final_finalCheck(checkstate='fail', uuid=contract_uuid,
                                                                        message='接口自动通过')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_27api_78dk_platform_tm_first_updateContractInfoSignState(self):
        # 修改合同状态为重签
        # {'uid': '合同uuid'}
        sql = 'UPDATE Tbl_Contract SET contract_state=\'not_active\' WHERE user_id=27;'
        MysqlClent.executed_all(loginAction.DB, sql)
        sql = 'SELECT Tbl_Contract.contract_uuid FROM Tbl_Contract LEFT OUTER JOIN Tbl_FirstCheckLog  ON ' \
              'Tbl_Contract.id = Tbl_FirstCheckLog.contract_id ' \
              'WHERE Tbl_FirstCheckLog.id IS NULL AND Tbl_Contract.qifa_machine_audit=\'qifa_merchant_audit_pass\' ' \
              'AND Tbl_Contract.first_check=\'first_check_pending\' ORDER BY Tbl_Contract.id DESC;'
        contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
        print('查询用户的可用订单 contract_uuid', contract_uuid_d[0][0])
        contract_uuid = contract_uuid_d[0][0]
        res = PlatformAction.test_api_78dk_platform_tm_first_selectCanAuditCheck(checktype='audit_check_first',
                                                                                 uid=contract_uuid)
        print('是否有权限审核', json.loads(res))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        res = PlatformAction.test_api_78dk_platform_tm_first_updateContractInfoSignState(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        # 修改法大大合同签署状态 修改为重签
        res = PlatformAction.test_api_78dk_platform_tm_first_findContractInfoSignStateWeb(contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_28api_78dk_platform_tm_after_viewAuditMonitors(self):
        # 贷后列表  enddate, pagecurrent, pagesize, qifascore, searchwhere, startdate,
        res = PlatformAction.test_api_78dk_platform_tm_after_viewAuditMonitors(
            enddate='', pagecurrent=1, pagesize=10, qifascore='', searchwhere='', startdate='')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['dataList'], '列表')
        Assertion.verity(json.loads(res)['data']['currentPage'], '当前页码')
        Assertion.verity(json.loads(res)['data']['pageSize'], '单页记录数')
        Assertion.verity(json.loads(res)['data']['totalPage'], '总页数')
        Assertion.verity(json.loads(res)['data']['totalCount'], '总记录数')
        Assertion.verity(json.loads(res)['data']['otherData'], '其它数据')

        # 查询电核待审核的订单
        def test_29api_78dk_platform_tm_first_saveSupplementImage(self):
            # 电核时-----提交或编辑补录资料 -----只有审核员自己审核的订单才能进行编辑审核
            sql = 'SELECT tc.* FROM Tbl_Contract tc  LEFT JOIN Tbl_TelephoneCheckLog ttl ' \
                  'ON tc.contract_uuid=ttl.contract_uuid  WHERE ttl.contract_uuid IS NULL ' \
                  'AND tc.telephone_check=\'telephone_check_pending\' ' \
                  'AND tc.first_check=\'first_check_pass\' ORDER BY tc.id ASC;'
            contract_uuid_d = MysqlClent.executed_all(loginAction.DB, sql)
            backGroundSupplementImages = [{
                "imageName": "装修合同照片自动上传电核",
                "key": "YHZXHTZP",
                "url": "2db6/99882db693a9aabc1f7a54ce7a5e1b4a805a.png"
            }]
            res = PlatformAction.test_api_78dk_platform_tm_first_saveSupplementImage(
                backgroundsupplementimages=backGroundSupplementImages, contractuuid=contract_uuid,
                supplementimagetype='supplement_image_type_submit', auditchecktype='audit_check_first')
            Assertion.verity(json.loads(res)['msg'], '成功')
            Assertion.verity(json.loads(res)['code'], '10000')
            Assertion.verity(json.loads(res)['data']['newImageName'], '新图片名称')
            Assertion.verity(json.loads(res)['data']['newImageUuid'], '新补录的图片UUID')
            Assertion.verity(json.loads(res)['data']['originalImageUuid'], '需要补录的图片UUID')
