#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from common.mydb import MysqlClent
import unittest
from common.myCommon.TestBaseCase import TestBaseCase
from common.myCommon import Assertion
from reborn.testAction import AppserverAction as JtlappAction
from reborn.testAction import loginAction
import time

API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache"}


class test_Jtlapp_002_periods(TestBaseCase):
    def test_01api_78dk_app_base_getUserInfo(self):
        # 将用户的所有订单设置成无效：
        # UPDATE Tbl_Contract set contract_state='invalid' where user_id=27;
        #获取用户信息    authCode每次扫码都在变化
        #  [{authCode=0026c51b2e9e4fc4adfb224a80cfWF93,storeUuid=e6eb671c41a148ef84b4b4cfedf0a28e,preferential=57cec4137b}]
        # [{authCode=f771573ebbaf475f957f825d038bZX93,storeUuid=e6eb671c41a148ef84b4b4cfedf0a28e,preferential=57cec4137b}]
        #{'preferential': '57cec4137b', 'storeUuid': 'e6eb671c41a148ef84b4b4cfedf0a28e', 'authCode': '用户权限编码(Y)'}
        sql = 'UPDATE Tbl_Contract set contract_state=\'invalid\' where user_id=27;'
        MysqlClent.executed_all(loginAction.DB, sql)
        res = JtlappAction.test_api_78dk_app_base_getUserInfo('57cec4137b','e6eb671c41a148ef84b4b4cfedf0a28e','0026c51b2e9e4fc4adfb224a80cfWF93')
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')


    def test_02api_78dk_app_periods_getConsumption(self):
        #获取额度测评
        # {"paramSingle":{"speed":"-1.000000","cityAdcode":"510100","bearing":"-1.000000","longitude":"104.071547","countryCode":"156","latitude":"30.545090","province":"四川省",
        # "districtAdcode":"510107","pois":[],"city":"成都市","district":"武侯区","accuracy":"65.000000","streetNumber":{"street":"天华路","number":"365号"},"country":"中国"}}
        #{'paramSingle': '用户位置信息(Y)'}
        sql = 'UPDATE Tbl_Contract set contract_state=\'invalid\' where user_id=27;'
        MysqlClent.executed_all(loginAction.DB, sql)

        paramSingle = {"country": "中国", "city": "成都市", "streetNumber": {"number": "475号", "street": "天华路"},
                        "bearing": 0, "latitude": 30.54621, "districtAdcode": "510107", "accuracy": 550, "speed": 0,
                        "province": "四川省", "cityAdcode": "510100", "countryCode": "156", "district": "武侯区",
                        "longitude": 104.072154}
        res = JtlappAction.test_api_78dk_app_periods_getConsumption(paramSingle)
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')
        # print(json.loads(res))
        # maxAmount=550000
        # merchantName=1.5.1
        # minAmount = 0
        # Assertion.verity(json.loads(res)['data']['periodList|2'], '')


    def test_03api_78dk_app_periods_getPeriodsOptions(self):
        #获取申请分期applyPeriods
        #{'money': ''}
        res = JtlappAction.test_api_78dk_app_periods_getPeriodsOptions('200000')
        # print(json.loads(res))
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

    def test_04api_78dk_app_periods_applyPeriods(self):
        #申请分期  amount, period, periodmoney, method, userlocation   period=12,periodMoney=null,method=3+9,amount=200000
        # {msg=成功,code=10000,data={periodList=[{period=6,value=3333.33}, {period=12,value=1733.16}, {period=24,value=933.16}, {period=36,value=688.71}]}}
        #{'userLocation': '用户位置信息(N)', 'periodMoney': '每期还款金额(Y)', 'method': '还款方式(Y)', 'amount': '总金额(Y)', 'period': '还款期数(Y)'}
        res = JtlappAction.test_api_78dk_app_periods_applyPeriods('200000', '12', '', '3+9')
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

        # Assertion.verity(json.loads(res)['data']['maxAmount'], '')
        # Assertion.verity(json.loads(res)['data']['merchantName'], '商户名称')
        # Assertion.verity(json.loads(res)['data']['minAmount'], '')


    def test_05api_78dk_app_periods_postUserInfo(self):
        #填写基本信息
        # {"username":"胡红","idcard":"511623199112244421","phone":"18381674004","job":"企业高管/副处级以上官员","house":"本人名下","decorationInputAddress":"抖音","immediatefamily":"嗯呢",
        # "relationship":"父母","kinsfolkphone":"15836985369","decorationProvinceId":"110000","decorationCityId":"110100","decorationDistrictId":"110101"}
        #  house, idcard, immediatefamily, job, kinsfolkphone, phone, relationship, username,
        # '本人名下','511623199112244421','企业高管/副处级以上官员','15263215235','18381674004','胡红','510000', '510104','vvsdfsdfdsfdsfdsfdsfdsfd','510100'
        #  decorationcityid, decorationdistrictid, decorationinputaddress, decorationprovinceid,
        # {'house': '房产类型', 'relationship': '亲属关系', 'phone': '手机号', 'decorationInputAddress': '装修地址-详细',
        # 'job': '职业类型', 'decorationDistrictId': '装修地址-区/县', 'kinsfolkphone': '亲属电话', 'idcard': '身份证',
        # 'decorationCityId': '装修地址-市', 'username': '姓名', 'immediatefamily': '亲属姓名', 'decorationProvinceId': '装修地址-省'}
        res = JtlappAction.test_api_78dk_app_periods_postUserInfo('本人名下','511623199112244421','retret','企业高管/副处级以上官员','15263215235','18381674004','父母','胡红',
                                                          '510000', '510104','vvsdfsdfdsfdsfdsfdsfdsfd','510100')
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

        # Assertion.verity(json.loads(res)['data']['aproveResult'], '实名认证结果')

    def test_06api_78dk_app_loan_image_saveContractImages(self):
        #影像资料保存
        # [[{contractImageUuid=null,contractId=null,contractUuid=null,key=YHSFZZPZM,url=f12f/215684f12f875fc4982ff938590810acf066cd,originalImageUuid=null},
        # {contractImageUuid=null,contractId=null,contractUuid=null,key=YHSFZZPFM,url=f12f/215684f12f875fc4982ff938590810acf066cd,originalImageUuid=null},
        # {contractImageUuid=null,contractId=null,contractUuid=null,key=YHSFZZPSC,url=32cc/22183732cc17031b1dcd9550f79de5c9ff071f,originalImageUuid=null},
        # {contractImageUuid=null,contractId=null,contractUuid=null,key=YHZXHTZP,url=3e3a/2477093e3ae16110e4592b09b1f7a2c70f609b,originalImageUuid=null},
        # {contractImageUuid=null,contractId=null,contractUuid=null,key=YHFCZM,url=3e3a/2477093e3ae16110e4592b09b1f7a2c70f609b,originalImageUuid=null}]]
        #{'url': '图片相对URL(Y)', 'key': '图片配置key(Y)'}
        res = JtlappAction.test_api_78dk_app_loan_image_saveContractImages()
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['data']['url'], '图片路径URL')
        # Assertion.verity(json.loads(res)['data']['type'], '类型 : 渠道、商户、用户')
        # Assertion.verity(json.loads(res)['data']['multiple'], '是否多选')
        # Assertion.verity(json.loads(res)['data']['name'], '图片名称')
        # Assertion.verity(json.loads(res)['data']['sort'], '排序参数')
        # Assertion.verity(json.loads(res)['data']['key'], '图片标识')


    def test_07api_78dk_app_base_getFddUrl(self):
        #获取法大大合同地址
        #{}
        res = JtlappAction.test_api_78dk_app_base_getFddUrl()
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')

        # Assertion.verity(json.loads(res)['data']['url'], '法大大合同签订地址')


    def test_08api_78dk_app_base_getFddResult(self):
        #获取法大大合同签订结果
        #{}
        # time.sleep(15)
        res = JtlappAction.test_api_78dk_app_base_getFddResult()

        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')


        # Assertion.verity(json.loads(res)['data']['auditResult'], '结果')

        # Assertion.verity(json.loads(res)['data']['phone'], '手机号')
        # Assertion.verity(json.loads(res)['data']['job'], '职业类型')
        # Assertion.verity(json.loads(res)['data']['immediatefamily'], '亲属姓名')
        # Assertion.verity(json.loads(res)['data']['relationship'], '亲属关系')
        # Assertion.verity(json.loads(res)['data']['kinsfolkphone'], '亲属电话')
        # Assertion.verity(json.loads(res)['data']['house'], '房产类型')
        # Assertion.verity(json.loads(res)['data']['username'], '姓名')
        # Assertion.verity(json.loads(res)['data']['idcard'], '身份证')
        # Assertion.verity(json.loads(res)['data']['decorationInputAddress'], '装修地址详细')

    def test_09api_78dk_app_loan_alipay_getAlipayVid(self):
        #获取支付宝验签Vid
        #{}
        res = JtlappAction.test_api_78dk_app_loan_alipay_getAlipayVid()
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')
        # print(json.loads(res))
        # Assertion.verity(json.loads(res)['data']['vid'], '')

    #     http://test.jtlappserver.78dk.com/api/78dk/app/base/getWsAuditResult
    def test_10api_78dk_app_base_getWsAuditResult(self):
        #网商进件
        #{}
        res = JtlappAction.test_api_78dk_app_base_getWsAuditResult()
        # Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['code'], '10000')
        # Assertion.verity(json.loads(res)['data']['uuid'], '合同Uuid')
        # Assertion.verity(json.loads(res)['data']['immediatefamily'], '亲属姓名')
        # Assertion.verity(json.loads(res)['data']['certification'], '是否实名')
        # Assertion.verity(json.loads(res)['data']['relationship'], '亲属关系')
        # Assertion.verity(json.loads(res)['data']['job'], '职业类型')
        # Assertion.verity(json.loads(res)['data']['sex'], '用户性别')
        # Assertion.verity(json.loads(res)['data']['phone'], '用户电话')
        # Assertion.verity(json.loads(res)['data']['decorationInputAddress'], '装修地址')
        # Assertion.verity(json.loads(res)['data']['kinsfolkphone'], '亲属电话')
        # Assertion.verity(json.loads(res)['data']['house'], '房产类型')
        # Assertion.verity(json.loads(res)['data']['username'], '用户姓名')
        # Assertion.verity(json.loads(res)['data']['idcard'], '身份证')


    #  http://test.jtlappserver.78dk.com/api/78dk/app/base/wsAuditResult
    # [{outOrderNo=2019052515055303236864,authResult=pass,errorMsg=,name=胡红,idcard=511623199112244421,phone=18381674004}]



    # def test_getLotteryLists(self):
    #     #获取热门房地区列表
    #     #{'keyword': '关键字', 'count': '请求数量', 'start': '起始值'}
    #     res = JtlappAction.test_getLotteryLists()
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['banners|3'], '')
    #     Assertion.verity(json.loads(res)['data']['grids|6'], '')
    # def test_getHomeConfig(self):
    #     #获取首页内容（banner数据）
    #     #{}
    #     res = JtlappAction.test_getHomeConfig(当前页,页面大小,)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['totalCount'], '')
    #     Assertion.verity(json.loads(res)['data']['currentPage'], '')
    #     Assertion.verity(json.loads(res)['data']['dataList'], '')
    #     Assertion.verity(json.loads(res)['data']['totalPage'], '')
    #     Assertion.verity(json.loads(res)['data']['pageSize'], '')
    # def test_api_st_sm_repayment_setting(self):
    #     #支付设置-页面初始化
    #     #{'currentPage': '当前页', 'pageSize': '页面大小'}
    #     res = JtlappAction.test_api_st_sm_repayment_setting(,,,)
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')



    # def test_api_78dk_app_periods_certification(self):
    #     #实名认证
    #     #{'idcard': '身份证', 'username': '姓名', 'phone': '手机号', 'verifycode': '验证码'}
    #     res = JtlappAction.test_api_78dk_app_periods_certification(手机号,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    # def test_api_78dk_app_periods_getVerify(self):
    #     #获取短信验证码
    #     #{'mobile': '手机号'}
    #     res = JtlappAction.test_api_78dk_app_periods_getVerify(图片相对URL(Y),图片配置key(Y),):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #
    # def test_api_78dk_app_loan_image_viewImageRoleList(self):
    #     #影像资料权限
    #     #{'uid': '合同Uuid'}
    #     res = JtlappAction.test_api_78dk_app_loan_image_viewImageRoleList(影像资料列表(Y),合同Uuid(Y),):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    # def test_api_78dk_app_loan_image_saveSupplementImage(self):
    #     #影像资料补录保存
    #     #{'dataLists': '影像资料列表(Y)', 'uid': '合同Uuid(Y)'}
    #     res = JtlappAction.test_api_78dk_app_loan_image_saveSupplementImage(合同Uuid,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['dataLists'], '补录资料列表')
    #     Assertion.verity(json.loads(res)['data']['description'], '补录资料说明')
    # def test_api_78dk_app_loan_image_viewImageSupplementList(self):
    #     #影像资料补录列表
    #     #{'uid': '合同Uuid'}
    #     res = JtlappAction.test_api_78dk_app_loan_image_viewImageSupplementList(门店/商户id(N),用户权限编码(Y),商户门店优惠(N),):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['merchantUuid'], '商户Uuid')
    #     Assertion.verity(json.loads(res)['data']['merchantName'], '商户名称')
    #     Assertion.verity(json.loads(res)['data']['jtlToken'], '唯一Token')
    #     Assertion.verity(json.loads(res)['data']['contractUuid'], '合同Uuid')
    #
    # def test_api_78dk_app_periods_getUserInfo(self):
    #     #查询基本信息
    #     #{}
    #     res = JtlappAction.test_api_78dk_app_periods_getUserInfo():
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')

    # def test_api_78dk_app_user_getUserInfo(self):
    #     #获取个人信息
    #     #{}
    #     res = JtlappAction.test_api_78dk_app_user_getUserInfo(当前页,每页大小,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['productName'], '产品名称')
    #     Assertion.verity(json.loads(res)['data']['merchantName'], '商户名称')
    #     Assertion.verity(json.loads(res)['data']['uuid'], '合同Uuid')
    #     Assertion.verity(json.loads(res)['data']['supplementStatus'], '补录状态')
    #     Assertion.verity(json.loads(res)['data']['status'], '合同状态')
    #     Assertion.verity(json.loads(res)['data']['loanAmount'], '合同金额')
    #     Assertion.verity(json.loads(res)['data']['createdate'], '创建时间')
    # def test_api_78dk_app_apply_getRecords(self):
    #     #获取申请记录
    #     #{'pageCurrent': '当前页', 'pageSize': '每页大小'}
    #     res = JtlappAction.test_api_78dk_app_apply_getRecords(当前页,合同Uuid,每页大小,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['stage'], '')
    #     Assertion.verity(json.loads(res)['data']['poundage'], '')
    #     Assertion.verity(json.loads(res)['data']['repaymentDate'], '')
    #     Assertion.verity(json.loads(res)['data']['repaymentAmount'], '')
    #     Assertion.verity(json.loads(res)['data']['status'], '')
    # def test_api_78dk_app_apply_getRepaymentPlan(self):
    #     #获取还款计划
    #     #{'pageCurrent': '当前页', 'paramInfo': '合同Uuid', 'pageSize': '每页大小'}
    #     res = JtlappAction.test_api_78dk_app_apply_getRepaymentPlan(合同Uuid,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['createdate'], '创建时间')
    #     Assertion.verity(json.loads(res)['data']['decorationCompany'], '商家名称')
    #     Assertion.verity(json.loads(res)['data']['uuid'], '合同Uuid')
    #     Assertion.verity(json.loads(res)['data']['supplementStatus'], '补录状态')
    #     Assertion.verity(json.loads(res)['data']['status'], '合同状态')
    #     Assertion.verity(json.loads(res)['data']['loanAmount'], '合同金额')
    # def test_api_78dk_app_apply_getRecordByUuid(self):
    #     #查询单条申请记录
    #     #{'paramInfo': '合同Uuid'}
    #     res = JtlappAction.test_api_78dk_app_apply_getRecordByUuid(合同Uuid,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['url'], '法大大合同查看地址')
    # def test_api_78dk_app_base_getFddCheckUrl(self):
    #     #获取法大大合同查看地址
    #     #{'uid': '合同Uuid'}
    #     res = JtlappAction.test_api_78dk_app_base_getFddCheckUrl(上级编码,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['value'], '区/县名称')
    #     Assertion.verity(json.loads(res)['data']['code'], '区/县编码')
    # def test_api_78dk_app_base_list_viewRegionLists(self):
    #     #获取区/县下拉列表
    #     #{'paramSingle': '上级编码'}
    #     res = JtlappAction.test_api_78dk_app_base_list_viewRegionLists(上级编码,):
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['value'], '市名称')
    #     Assertion.verity(json.loads(res)['data']['code'], '市编码')
    # def test_api_78dk_app_base_list_viewCityLists(self):
    #     #获取市下拉列表
    #     #{'paramSingle': '上级编码'}
    #     res = JtlappAction.test_api_78dk_app_base_list_viewCityLists():
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['data']['value'], '省名称')
    #     Assertion.verity(json.loads(res)['data']['code'], '省编码')
