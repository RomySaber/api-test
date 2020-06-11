#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from common.myCommon import Assertion
from xqkj.testAction import XqqbAction

#   贷款试算      # LoanCalParam(storeUuid=, isDiscount=, loanAmount=369, productDetailUuid=
# 申请金额
loanAmount = '368'
# 门店uuid
storeUuid = 'c4e213f84e5240faa1dbb736dc8518e4'
# 是否贴息
isDiscount = 'true'
# 产品uuid
productDetailUuid = 'ee784d588ccc4a4c85d379f9f5fd64f8'
# 期数uuid
productDetailConfigUuid = ''

bankCardMobile = '18381674004'
# '银行卡预留手机号(Y)',
bankCardNo = '6228480482549097517'
# 银行卡号(Y)',
billEmail = 'huhong@78dk.com'
# '账单邮箱(N)

cardScanIdcardNo = '511623199112244421'
# '身份证号码(Y)'



# 基本信息
liveProvinceName = ''
# 居住地址-省名称(Y)', '
liveProvince = ''
#: '居住地址-省编码(Y)',
datumTypeHousingId = ''
# '住房类型(Y)',
liveDetail = 'xx大街345号擦擦擦胡同说三道四'
# '居住地址-详细地址(Y)',
liveRegion = ''
# 居住地址-区编码(Y)', ' \
liveCityName = ''
# '居住地址-市名称(Y)',
liveRegionName = ''
# '居住地址-区名称(Y)',
datumTypeMarryId = ''
# '婚姻状况(Y)',
liveCity = ''
# '居住地址-市编码(Y)',
contactList = ''
# '联系人信息列表',
datumTypeEducationId = ''
# '学历(Y)'}


# 保存工作信息
companyCityName = ''
# ': '单位地址-市名称(Y)', '
companyProvinceName = ''
# ': '单位地址-省名称(Y)', '
datumTypeWorktimeId = ''
# ': '工作时间(Y)', '
companyProvince = ''
# ': '单位地址-省编码(Y)', '
workPhone = ''
# ': '工作电话(Y)', '
companyName = ''
# ': '单位名称(Y)', '
datumTypeIncomeId = ''
# ': '薪资(Y)', '
companyRegion = ''
# ': '单位地址-县编码(Y)', '
companyDetail = ''
# ': '单位地址-详细地址(Y)', '
position = ''
# ': '职位(Y)', '
companyRegionName = ''
# ': '单位地址-县名称(Y)', '
companyCity = ''
# ': '单位地址-市编码(Y)'}


# 获取版本信息
channelNo = 'app-store'
currentVersNumb = 1.0
platform = 1


class Action(object):
    # def test_api_78dk_app_login_register(self):
    #     #注册  已经注册，不可以重复注册
    #     #{'registerSource': '注册来源（N）', 'mobileVersion': '注册时手机版本号（N）', 'ipAddress': '注册时IP地址（N）', 'appVersion': '注册时APP版本号（N）', 'verCode': '验证码（Y）', 'mobileName': '注册时手机名字（N）', 'mobile': '手机号（Y）', 'mobileNetwork': '注册是手机网络（N）', 'mobileUuid': '手机唯一标识UUID（Y）', 'password': '密码（Y）', 'jgPushId': '极光id编号（N）', 'mobileSystem': '手机系统（N）'}
    #     # res = XqqbAction.test_api_78dk_app_login_register(appVersion='',registerSource='',ipAddress='',mobileSystem='',mobileName='',password='',mobile='',jgPushId='',mobileUuid='',verCode='',mobileVersion='',mobileNetwork='',)
    #     res = XqqbAction.testapi_78dk_app_login_register(mobile='18381674004', password='12345678hh', verCode='394220', type='', loanOrderUuid='', userUuid='', idCard='', idName='', appVersion=1.0,
    #                                               ipAddress='192.168.10.252', jgPushId='', mobileName='vivovivo X9', mobileNetwork='mobile_network_WIFI',
    #                                               mobileSystem='mobile_system_Android', mobileUuid='864022034561034', mobileVersion='android7.1.2', registerSource='register_source_app')
    #     Assertion.verity(json.loads(res)['code'], '10000')

    # def test_api_78dk_app_login_pwLogin(self):
    #     # 登录（密码）   极光随机生成的，不能重复使用
    #     # mobile=18381674004, password=fq123456, verCode=null, type=null, loanOrderUuid=null, userUuid=null, idCard=null, idName=null,
    #     # appVersion=null, ipAddress=null, jgPushId=183816740041554947818381, mobileName=null, mobileNetwork=null, mobileSystem=null, mobileUuid=null, mobileVersion=null, registerSource=null
    #     # {'jgPushId': '极光id编号（Y）', 'password': '密码（Y）', 'mobile': '手机号（Y）'}
    #     res = XqqbAction.test_api_78dk_app_login_pwLogin(mobile=18381674004, password='fq123456', verCode='', type='',
    #                                              loanOrderUuid='', userUuid='', idCard='', idName='',
    #                                              appVersion='', ipAddress='', jgPushId=183816740041554947818381,
    #                                              mobileName='', mobileNetwork='', mobileSystem='', mobileUuid='',
    #                                              mobileVersion='', registerSource='')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     print(json.loads(res)['data']['token'])




    def test_api_78dk_app_process_getStoreAndProduct(self):
        # 根据门店uuid查询门店商品
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getStoreAndProduct(storeuuid='c4e213f84e5240faa1dbb736dc8518e4',
                                                                      isdiscount='true')

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_loanCalculator(self):
        # 贷款试算

        # {'isDiscount': '是否贴息(Y)', 'loanAmount': '申请金额(Y)', 'storeUuid': '门店Uuid(Y)', 'productDetailUuid': '产品Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_loanCalculator(loanamount=loanAmount, storeuuid=storeUuid,
                                                                  isdiscount=isDiscount,
                                                                  productdetailuuid=productDetailUuid, )

        Assertion.verity(json.loads(res)['code'], '10000')
        print(json.loads(res))
        # Assertion.verity(json.loads(res)['data']['period'], '期数')
        # Assertion.verity(json.loads(res)['data']['productDetailConfigUuid'], '期数uuid')
        # Assertion.verity(json.loads(res)['data']['principal'], '每期本金')
        # Assertion.verity(json.loads(res)['data']['lastPayDate'], '还款日')
        # Assertion.verity(json.loads(res)['data']['handlingFee'], '每期手续费')

    def test_api_78dk_app_process_choiceBankCard(self):
        # 选择还款银行卡
        # {'userBankCardUuid': '银行卡Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_choiceBankCard(userbankcarduuid='0e15f960798749228fce94e8f23b074e', )
        Assertion.verity(json.loads(res)['code'], '10000')
        print(json.loads(res))

    def test_api_78dk_app_process_getProductDetail(self):
        # 根据产品uuid查询分期详情
        # {'productDetailUuid': '产品Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getProductDetail(productDetailUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['minQuota'], '单笔额度下限')
        Assertion.verity(json.loads(res)['data']['maxQuota'], '单笔额度上限')
        Assertion.verity(json.loads(res)['data']['productDetailUuid'], '产品Uuid')
        Assertion.verity(json.loads(res)['data']['name'], '产品名称')
        Assertion.verity(json.loads(res)['data']['incomingPartsTemplateList'], '进件要素模板')
        Assertion.verity(json.loads(res)['data']['productDetailConfigs'], '分期方案')

    def test_api_78dk_app_process_saveOrcInfo(self):
        # 保存人脸识别结果
        # {'thirdKey': '第三张图片key(Y)', 'note': 'faceID返回结果(Y)', 'secondKey': '第二张图片key(Y)', 'firstKey': '第一张图片key(Y)'}
        res = XqqbAction.test_api_78dk_app_process_saveOrcInfo(firstKey='', note='', secondKey='', thirdKey='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_saveIdCardInfo(self):
        # 保存身份证信息
        # {'cardScanIdcardNo': '身份证号码(Y)', 'oppositeNote': '身份证反面照faceID返回结果(Y)', 'frontNote': '身份证正面照faceID返回结果(Y)', 'oppositeKey': '身份证反面照key(Y)', 'cardScanName': '名字(Y)', 'frontKey': '身份证正面照key(Y)'}
        res = XqqbAction.test_api_78dk_app_process_saveIdCardInfo(oppositeNote='', frontKey='', frontNote='',
                                                                  cardScanIdcardNo='', oppositeKey='',
                                                                  cardScanName='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getNewestIdCardInfo(self):
        # 查询身份证信息（最近的）
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getNewestIdCardInfo(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['frontKey'], '身份证正面照key')
        Assertion.verity(json.loads(res)['data']['holdUrl'], '手持照Url')
        Assertion.verity(json.loads(res)['data']['frontUrl'], '身份证正面照url')
        Assertion.verity(json.loads(res)['data']['oppositeUrl'], '身份证反面照url')
        Assertion.verity(json.loads(res)['data']['cardScanIdcardNo'], '身份证号码')
        Assertion.verity(json.loads(res)['data']['holdKey'], '手持照key')
        Assertion.verity(json.loads(res)['data']['oppositeKey'], '身份证反面照key')
        Assertion.verity(json.loads(res)['data']['cardScanName'], '名字')

    def test_api_78dk_app_process_getSupportBanks(self):
        # 查询支持银行（弹窗描述）
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getSupportBanks(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getBankCardInfo(self):
        # 查询绑定的银行卡列表
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getBankCardInfo(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['bankImageUrl'], '银行图片')
        Assertion.verity(json.loads(res)['data']['bankColor'], '银行背景色')
        Assertion.verity(json.loads(res)['data']['bankCardNo'], '银行卡号')
        Assertion.verity(json.loads(res)['data']['bankName'], '银行名称')
        Assertion.verity(json.loads(res)['data']['bankCardType'], '银行卡类型[0:借记卡  1:信用卡]')
        Assertion.verity(json.loads(res)['data']['userBankCardUuid'], '银行卡Uuid')

    def test_api_78dk_app_process_saveBankCardInfo(self):
        # 绑定银行卡1-输入银行卡信息
        # {'bankCardMobile': '银行卡预留手机号(Y)', 'bankCardNo': '银行卡号(Y)', 'billEmail': '账单邮箱(N)'}
        res = XqqbAction.test_api_78dk_app_process_saveBankCardInfo(bankCardNo=bankCardNo, bankCardMobile='',
                                                                    billEmail='', )

        Assertion.verity(json.loads(res)['code'], '10000')

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_savePersonInfo(self):
        # 保存基本信息
        # {'liveProvinceName': '居住地址-省名称(Y)', 'liveProvince': '居住地址-省编码(Y)', 'datumTypeHousingId': '住房类型(Y)', 'liveDetail': '居住地址-详细地址(Y)', 'liveRegion': '居住地址-区编码(Y)', 'liveCityName': '居住地址-市名称(Y)', 'liveRegionName': '居住地址-区名称(Y)', 'datumTypeMarryId': '婚姻状况(Y)', 'liveCity': '居住地址-市编码(Y)', 'contactList': '联系人信息列表', 'datumTypeEducationId': '学历(Y)'}
        res = XqqbAction.test_api_78dk_app_process_savePersonInfo(datumTypeHousingId=datumTypeHousingId,
                                                                  liveDetail=liveDetail,
                                                                  datumTypeMarryId=datumTypeMarryId,
                                                                  liveProvinceName=liveProvinceName,
                                                                  liveRegion=liveRegion, contactList=contactList,
                                                                  liveCity=liveCity,
                                                                  datumTypeEducationId=datumTypeEducationId,
                                                                  liveProvince=liveProvince,
                                                                  liveRegionName=liveRegionName,
                                                                  liveCityName=liveCityName, )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getNewestPersonInfo(self):
        # 查询基本信息（最近的）
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getNewestPersonInfo(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['datumTypeHousingId'], '住房类型id')
        Assertion.verity(json.loads(res)['data']['liveRegionName'], '居住地址-区名称')
        Assertion.verity(json.loads(res)['data']['liveProvinceName'], '居住地址-省名称')
        Assertion.verity(json.loads(res)['data']['datumTypeEducationName'], '学历-字典名称')
        Assertion.verity(json.loads(res)['data']['datumTypeEducationId'], '学历id')
        Assertion.verity(json.loads(res)['data']['liveRegion'], '居住地址-区编码')
        Assertion.verity(json.loads(res)['data']['liveProvince'], '居住地址-省编码')
        Assertion.verity(json.loads(res)['data']['datumTypeHousingName'], '住房类型-字典名称')
        Assertion.verity(json.loads(res)['data']['liveCityName'], '居住地址-市名称')
        Assertion.verity(json.loads(res)['data']['datumTypeMarryId'], '婚姻状况id')
        Assertion.verity(json.loads(res)['data']['liveCity'], '居住地址-市编码')
        Assertion.verity(json.loads(res)['data']['datumTypeMarryName'], '婚姻状况-字典名称')
        Assertion.verity(json.loads(res)['data']['liveDetail'], '居住地址-详细地址')
        Assertion.verity(json.loads(res)['data']['contactList'], '联系人信息列表')

    def test_api_78dk_app_process_saveWorkInfo(self):
        # 保存工作信息
        # {'companyCityName': '单位地址-市名称(Y)', 'companyProvinceName': '单位地址-省名称(Y)', 'datumTypeWorktimeId': '工作时间(Y)', 'companyProvince': '单位地址-省编码(Y)', 'workPhone': '工作电话(Y)', 'companyName': '单位名称(Y)', 'datumTypeIncomeId': '薪资(Y)', 'companyRegion': '单位地址-县编码(Y)', 'companyDetail': '单位地址-详细地址(Y)', 'position': '职位(Y)', 'companyRegionName': '单位地址-县名称(Y)', 'companyCity': '单位地址-市编码(Y)'}
        res = XqqbAction.test_api_78dk_app_process_saveWorkInfo(companyCityName=companyCityName, position=position,
                                                                companyCity=companyCity, companyRegion=companyRegion,
                                                                companyProvince=companyProvince, workPhone=workPhone,
                                                                companyProvinceName=companyProvinceName,
                                                                datumTypeWorktimeId=datumTypeWorktimeId,
                                                                companyName=companyName, companyDetail=companyDetail,
                                                                companyRegionName=companyRegionName,
                                                                datumTypeIncomeId=datumTypeIncomeId, )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getNewestWorkInfo(self):
        # 查询工作信息（最近的）
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getNewestWorkInfo(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['datumTypeIncomeName'], '薪资-字典名称')
        Assertion.verity(json.loads(res)['data']['companyCityName'], '单位地址-市名称')
        Assertion.verity(json.loads(res)['data']['position'], '职位')
        Assertion.verity(json.loads(res)['data']['companyCity'], '单位地址-市编码')
        Assertion.verity(json.loads(res)['data']['companyRegion'], '单位地址-县编码')
        Assertion.verity(json.loads(res)['data']['companyProvince'], '单位地址-省编码')
        Assertion.verity(json.loads(res)['data']['datumTypeWorktimeName'], '工作时间-字典名称')
        Assertion.verity(json.loads(res)['data']['workPhone'], '工作电话')
        Assertion.verity(json.loads(res)['data']['companyProvinceName'], '单位地址-省名称')
        Assertion.verity(json.loads(res)['data']['datumTypeWorktimeId'], '工作时间id')
        Assertion.verity(json.loads(res)['data']['companyName'], '单位名称')
        Assertion.verity(json.loads(res)['data']['companyDetail'], '单位地址-详细地址')
        Assertion.verity(json.loads(res)['data']['companyRegionName'], '单位地址-县名称')
        Assertion.verity(json.loads(res)['data']['datumTypeIncomeId'], '薪资id')

    def test_api_78dk_app_process_saveContractImages(self):
        # 保存影像资料
        # {'contractImageList': '影像资料列表'}
        res = XqqbAction.test_api_78dk_app_process_saveContractImages(contractImageList='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getContractImages(self):
        # 查询影像资料（当前订单）
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getContractImages(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['imageUrl'], '图片Url')
        Assertion.verity(json.loads(res)['data']['key'], '图片相对key')

    def test_api_78dk_app_process_submitApply(self):
        # 提交申请
        # {'productDetailConfigUuid': '产品分期方案Uuid(N)', 'loanAmount': '分期金额(N)'}
        res = XqqbAction.test_api_78dk_app_process_submitApply(loanAmount='', productDetailConfigUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getSignResult(self):
        # 查询法大大签约结果
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getSignResult(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getSignUrl(self):
        # 获取法大大签约地址
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getSignUrl(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['signUrl'], '签约地址')

    def test_api_78dk_app_process_createContract(self):
        # 下一步-创建订单
        # {'productDetailConfigUuid': '期数Uuid(Y)', 'loanAmount': '分期金额(Y)', 'storeUuid': '门店Uuid(Y)', 'isDiscount': '是否贴息(Y)', 'productDetailUuid': '产品Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_createContract(loanAmount='', productDetailConfigUuid='',
                                                                  isDiscount='', storeUuid='', productDetailUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_getSpecialInfo(self):
        # 查询特别信息认证进度
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_process_getSpecialInfo(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['jdAuthStatus'], '京东认证状态')
        Assertion.verity(json.loads(res)['data']['yysAuthStatus'], '运营商认证状态')
        Assertion.verity(json.loads(res)['data']['tbAuthStatus'], '淘宝认证状态')

    def test_api_78dk_app_process_saveHoldKey(self):
        # 保存手持身份证照片
        # {'holdKey': '手持照key(Y)'}
        res = XqqbAction.test_api_78dk_app_process_saveHoldKey(holdKey='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_validBankCardInfo(self):
        # 绑定银行卡2-输入手机验证码
        # {'validCode': '手机验证码(Y)'}
        res = XqqbAction.test_api_78dk_app_process_validBankCardInfo(validCode='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_mxCallback(self):
        # （回调接口）接口中心-魔蝎
        # {'body': '回调内容'}
        res = XqqbAction.test_api_78dk_app_process_mxCallback(body='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_process_repayPlanCalculator(self):
        # 还款计划试算
        # {'productDetailConfigUuid': '期数uuid(Y)', 'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)', 'productDetailUuid': '产品Uuid(Y)', 'loanAmount': '申请金额(Y)'}
        res = XqqbAction.test_api_78dk_app_process_repayPlanCalculator(loanAmount='', productDetailConfigUuid='',
                                                                       isDiscount='', storeUuid='',
                                                                       productDetailUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['number'], '第几期')
        Assertion.verity(json.loads(res)['data']['lastPayDate'], '还款时间')
        Assertion.verity(json.loads(res)['data']['principal'], '本金')
        Assertion.verity(json.loads(res)['data']['handlingFee'], '手续费')

    def test_api_78dk_app_process_saveUserPlaceOrderGps(self):
        # 保存用户下单位置信息
        # {'gpsDetail': 'gps解析信息-详细地址(Y)', 'gpsCity': 'gps解析信息-市(Y)', 'gpsProvince': 'gps解析信息-省(Y)', 'gpsRegion': 'gps解析信息-县(Y)', 'gpsInfoLon': 'gps经度(Y)', 'gpsAddress': 'gps解析完整地址(Y)', 'gpsInfoLat': 'gps维度(Y)'}
        res = XqqbAction.test_api_78dk_app_process_saveUserPlaceOrderGps(gpsDetail='', gpsRegion='', gpsInfoLon='',
                                                                         gpsProvince='', gpsInfoLat='', gpsAddress='',
                                                                         gpsCity='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_common_queryQiNiuToken(self):
        # 获取七牛上传token
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_common_queryQiNiuToken(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_common_getCites(self):
        # 获取城市列表
        # {'parent': '父级地区编码'}
        res = XqqbAction.test_api_78dk_app_common_getCites(parent='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['name'], '地区名称')
        Assertion.verity(json.loads(res)['data']['id'], '地区编码')

    def test_api_78dk_app_common_getDictionaries(self):
        # 获取字典列表
        # {'datumType': '类型'}
        res = XqqbAction.test_api_78dk_app_common_getDictionaries(datumType='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['id'], '字典id')
        Assertion.verity(json.loads(res)['data']['typeName'], '字典名称')

    def test_api_78dk_app_common_getAllCites(self):
        # 获取所有城市列表
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_common_getAllCites(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['parent'], '父级城市编码')
        Assertion.verity(json.loads(res)['data']['name'], '城市名称')
        Assertion.verity(json.loads(res)['data']['id'], '城市编码')

    def test_api_78dk_app_common_getVersionInfo(self):
        # 获取版本信息
        # {'platform': '平台(Y)', 'channelNo': '应用平台渠道号(Y)', 'currentVersNumb': 'APP当前版本号(Y)'}
        res = XqqbAction.test_api_78dk_app_common_getVersionInfo(platform=platform, currentVersNumb=currentVersNumb,
                                                                 channelNo=channelNo, )
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_common_sms_sendValidate(self):
        # 发送短信
        # {'type': '类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号]（Y）', 'mobile': '手机号码（Y）'}
        res = XqqbAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_common_idCardInit(self):
        # 初始化(获取身份认证)
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_common_idCardInit(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['idName'], '姓名')
        Assertion.verity(json.loads(res)['data']['mobile'], '手机号')
        Assertion.verity(json.loads(res)['data']['idCard'], '身份证号码(号码中间部分会打码)')

    def test_api_78dk_app_perCenter_viewByStagesLists(self):
        # 分期列表
        # {'pageSize': '每页条数(Y)', 'pageCurrent': '当前页数(Y)'}
        res = XqqbAction.test_api_78dk_app_perCenter_viewByStagesLists(pageSize='', pageCurrent='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['pageTotal'], '总页数')
        Assertion.verity(json.loads(res)['data']['pageSize'], '页面大小')
        Assertion.verity(json.loads(res)['data']['pageCurrent'], '当前页')
        Assertion.verity(json.loads(res)['data']['dataList'], '')

    def test_api_78dk_app_perCenter_renounceApplication(self):
        # 放弃申请
        # {'loanOrderUuid': '订单UUID（Y）'}
        res = XqqbAction.test_api_78dk_app_perCenter_renounceApplication(loanOrderUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_perCenter_loanData(self):
        # 贷款资料
        # {'loanOrderUuid': '订单UUID（Y）'}
        res = XqqbAction.test_api_78dk_app_perCenter_loanData(loanOrderUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['oppositeUrl'], '身份证反面')
        Assertion.verity(json.loads(res)['data']['holdUrl'], '手持身份证')
        Assertion.verity(json.loads(res)['data']['frontUrl'], '身份证正面')

    def test_api_78dk_app_perCenter_repaymentFormLists(self):
        # 还款计划列表
        # {'pageSize': '每页条数(Y)', 'paramInfo': '订单UUID（Y）', 'pageCurrent': '当前页数(Y)'}
        res = XqqbAction.test_api_78dk_app_perCenter_repaymentFormLists(paramInfo='', pageSize='', pageCurrent='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['pageTotal'], '总页数')
        Assertion.verity(json.loads(res)['data']['pageSize'], '页面大小')
        Assertion.verity(json.loads(res)['data']['pageCurrent'], '当前页')
        Assertion.verity(json.loads(res)['data']['dataList'], '')

    def test_api_78dk_app_perCenter_loanDatail(self):
        # 申请详情
        # {'loanOrderUuid': '订单UUID（Y）'}
        res = XqqbAction.test_api_78dk_app_perCenter_loanDatail(loanOrderUuid='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['loanAmount'], '申请金额')
        Assertion.verity(json.loads(res)['data']['billState'], '状态[审批中：0, 已放款：1]')
        Assertion.verity(json.loads(res)['data']['loanOrderUuid'], '订单uuid')

    def test_api_78dk_app_login_loginOut(self):
        # 登出
        # {'isDiscount': '是否贴息(Y)', 'storeUuid': '门店Uuid(Y)'}
        res = XqqbAction.test_api_78dk_app_login_loginOut(storeUuid='', isDiscount='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_login_pwLogin(self):
        # 登录（密码）
        # {'jgPushId': '极光id编号（Y）', 'password': '密码（Y）', 'mobile': '手机号（Y）'}
        res = XqqbAction.test_api_78dk_app_login_pwLogin(password='', mobile='', jgPushId='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['token'], 'token值')

    def test_api_78dk_app_login_smsLogin(self):
        # 登录（短信）
        # {'jgPushId': '极光id编号（Y）', 'verCode': '验证码（Y）', 'mobile': '手机号（Y）'}
        res = XqqbAction.test_api_78dk_app_login_smsLogin(verCode='', mobile='', jgPushId='', )

        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['token'], 'token值')

    def test_api_78dk_app_login_retrievePw(self):
        # 忘记密码
        # {'verCode': '验证码（Y）', 'mobile': '手机号码（Y）'}
        res = XqqbAction.test_api_78dk_app_login_retrievePw(verCode='', mobile='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_login_newPw(self):
        # 忘记密码(设置新密码)
        # {'password': '新密码（Y）', 'mobile': '手机号（Y）'}
        res = XqqbAction.test_api_78dk_app_login_newPw(password='', mobile='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_login_updatePw(self):
        # 修改登录密码
        # {'verCode': '验证码（Y）', 'password': '新密码（Y）'}
        res = XqqbAction.test_api_78dk_app_login_updatePw(verCode='', password='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_login_updateMobileSms(self):
        # 更改手机号(可接受短信)
        # {'verCode': '验证码（Y）', 'mobile': '新手机号码（Y）'}
        res = XqqbAction.test_api_78dk_app_login_updateMobileSms(verCode='', mobile='', )

        Assertion.verity(json.loads(res)['code'], '10000')

    def test_api_78dk_app_login_updateMobile(self):
        # 更改手机号(无法接受短信)
        # {'idCard': '身份证号码（Y）', 'mobile': '新手机号（Y）'}
        res = XqqbAction.test_api_78dk_app_login_updateMobile(mobile='', idCard='', )

        Assertion.verity(json.loads(res)['code'], '10000')


if __name__ == '__main__':
    cc = Action()
    # cc.test_api_78dk_app_process_getStoreAndProduct()
    cc.test_api_78dk_app_process_loanCalculator()
    # cc.test_api_78dk_app_process_choiceBankCard()
