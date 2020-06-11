#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-25 下午 5:19
@Author     : 罗林
@File       : testEasyloan_app_003_loan.py
@desc       :  进件模块测试用例
"""

import json

from common.myCommon import Assertion as ass, TimeFormat as tf
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_appAction as ea_app


class testEasyloan_app_003_loan(TestBaseCase):
    def test_001_api_78dk_clientapp_auth_messAuth_queryAuthPro(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 认证进度
        """
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_queryAuthPro()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "certify")
        ass.verityContain(json.loads(rs)['data'], "subList")
        ass.verityContain(json.loads(rs)['data'], "type")

    def test_002_api_78dk_clientapp_auth_messAuth_addCarInfo(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 车辆认证
        """
        vehicleauthuuid, brandname, city, modelid, modelname, registertime, seriesid, seriesname = eq.get_info(
            'vehicle_auth', 'vehicle_auth_uuid,brand_name,city,model_id,model_name,register_time,series_id,series_name')
        registertime = tf.string_toTimestamp_13(tf.datetime_toString(registertime, tf.FORMART1))
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_addCarInfo(
            brandid='', seriesid=seriesid, city=city, registertime=registertime, modelid=modelid,
            vehicleauthuuid=vehicleauthuuid, seriesname=seriesname, brandname=brandname, modelname=modelname)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_003_api_78dk_clientapp_auth_messAuth_addIdCardIfo(self):
        """
          Time       :2019-04-25
          author     : 罗林
          desc       : 保存身份认证信息
        """
        idcard, idcarda, idcardb, name, cardaddress, nation, day, issuingbody, month, sex, validitybegin, validityend, \
        year = eq.get_info('client_base', 'idcard,idcard_a,idcard_b,name,address,nation,day,'
                                          'issuing_body,month,sex,validity_begin,validity_end,year')
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_addIdCardIfo(
            idcard=idcard, idcarda=idcarda, idcardb=idcardb, name=name, cardaddress=cardaddress, nation=nation, day=day,
            issuingbody=issuingbody, month=month, sex=sex, validitybegin=validitybegin, validityend=validityend,
            year=year)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_004_api_78dk_clientapp_auth_messAuth_queryIdCardIfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 查询身份认证信息
        """
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_queryIdCardIfo()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "cardAddress")
        ass.verityContain(json.loads(rs)['data'], "idcard")
        ass.verityContain(json.loads(rs)['data'], "idcardA")
        ass.verityContain(json.loads(rs)['data'], "idcardB")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "nation")
        ass.verityContain(json.loads(rs)['data'], "validityIdCard")

    def test_005_api_78dk_clientapp_auth_messAuth_queryFaceResult(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 人脸识别结果
        """
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_queryFaceResult(meglivedata='', biztoken='', signversion='')
        ass.verity(json.loads(rs)['code'], "20000")
        # ass.verityContain(json.loads(rs)['data'], "result")

    def test_006_api_78dk_clientapp_auth_messAuth_queryCarInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 车辆认证查询
        """
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_queryCarInfo()
        ass.verity(json.loads(rs)['code'], "10000")

    def test_007_api_78dk_clientapp_auth_messAuth_addBankCard(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 银行卡认证
        """
        bank, cardno, mobile = eq.get_info('client_cards', 'bank,card_no,mobile')
        rs = ea_app.test_api_78dk_clientapp_auth_messAuth_addBankCard(bank=bank, cardno=cardno, mobile=mobile)
        ass.verity(json.loads(rs)['code'], "S0028")
        ass.verity(json.loads(rs)['msg'], "该身份证已经完成认证，不能重复认证！")

    def test_008_api_78dk_clientapp_loan_perfectInfo_updateSelfInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 完善个人信息
        """
        address, marriage, spouseidcard, spousename, mail, housenature, region, city, province = eq.get_info(
            'client_base', 'address,marriage,spouse_idcard,spouse_name,mail,house_nature,'
                           'region,city,province', 'year is not NULL')
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_updateSelfInfo(
            address=address, marriage=marriage, spouseidcard=spouseidcard, spousename=spousename, mail=mail,
            housenature=housenature, region=region, city=city, province=province, education='')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_009_api_78dk_clientapp_loan_perfectInfo_querySelfInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 个人信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_querySelfInfo()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "address")
        # ass.verityContain(json.loads(rs)['data'], "birthDate")
        # ass.verityContain(json.loads(rs)['data'], "city")
        # ass.verityContain(json.loads(rs)['data'], "cityName")
        # ass.verityContain(json.loads(rs)['data'], "education")
        # ass.verityContain(json.loads(rs)['data'], "idcard")
        # ass.verityContain(json.loads(rs)['data'], "marriage")
        # ass.verityContain(json.loads(rs)['data'], "mobile")
        # ass.verityContain(json.loads(rs)['data'], "name")

    def test_010_api_78dk_clientapp_loan_perfectInfo_queryLoanInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 借款信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_queryLoanInfo()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "applyAmount")
        # ass.verityContain(json.loads(rs)['data'], "loanTerm")
        # ass.verityContain(json.loads(rs)['data'], "loanUse")
        # ass.verityContain(json.loads(rs)['data'], "productDetailName")
        # ass.verityContain(json.loads(rs)['data'], "productDetailUuid")

    def test_011_api_78dk_clientapp_loan_perfectInfo_updateLoanInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 借款信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_updateLoanInfo(
            applyamount=10000, loanterm=12, loanuse='', productdetailuuid='', city=510010, cityname='')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_012_api_78dk_clientapp_loan_perfectInfo_addUpWorkInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 职业信息保存或修改
        """
        address, clientworkuuid, incomemonth, industry, name, paydate, position, property, workage, incomeother, \
        region1, city, province, scale = eq.get_info(
            'client_work', 'address,client_work_uuid,income_month,industry,name,pay_date,position,property,'
                           'work_age,income_month,region,city,province,scale')
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_addUpWorkInfo(
            address=address, clientworkuuid=clientworkuuid, incomemonth=incomemonth, industry=industry, name=name,
            paydate=paydate, position=position, property=property, workage=workage, incomeother=incomeother,
            region=region1, city=city, province=province, scale=scale)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_013_api_78dk_clientapp_loan_perfectInfo_queryWorkInfo(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 职业信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_queryWorkInfo()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "incomeMonth")
        # ass.verityContain(json.loads(rs)['data'], "industry")
        # ass.verityContain(json.loads(rs)['data'], "payDate")
        # ass.verityContain(json.loads(rs)['data'], "scale")

    def test_014_api_78dk_clientapp_loan_perfectInfo_addContracts(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 职业信息查询
        """
        mobile, name, ralation = eq.get_info('client_contact', 'mobile,name,ralation')
        paramlist = [{"mobile": mobile, "name": name, "ralation": ralation}]
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_addContracts(paramlist=paramlist)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_015_api_78dk_clientapp_loan_perfectInfo_queryContractList(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 联系人信息查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_queryContractList()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "dataList")
        # ass.verityContain(json.loads(rs)['data'], "mobile")
        # ass.verityContain(json.loads(rs)['data'], "name")
        # ass.verityContain(json.loads(rs)['data'], "ralation")

    def test_016_api_78dk_clientapp_loan_perfectInfo_addLoanFile(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 借款资料保存
        """
        paramlist = [{"typeCode": 'QYZL0001', "urls": 'upload_pic_QQ图片20190220100246.jpg'}]
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_addLoanFile(paramlist=paramlist)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_017_api_78dk_clientapp_loan_perfectInfo_queryLoanFile(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 借款资料查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_queryLoanFile()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        # ass.verityContain(json.loads(rs)['data'], "typeCode")
        # ass.verityContain(json.loads(rs)['data'], "urls")

    def test_018_api_78dk_clientapp_loan_perfectInfo_infoSure(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 完善信息确认
        """
        rs = ea_app.test_api_78dk_clientapp_loan_perfectInfo_infoSure()
        ass.verity(json.loads(rs)['code'], "10000")

    def test_019_api_78dk_clientapp_loan_loanApply_queryCanLoan(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 是否可以借款
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_queryCanLoan()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "result")

    def test_020_api_78dk_clientapp_loan_loanApply_queryApplyState(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 审核状态查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_queryApplyState()
        ass.verity(json.loads(rs)['code'], "S0023")
        ass.verity(json.loads(rs)['msg'], "订单不存在")

    def test_021_api_78dk_clientapp_loan_loanApply_queryApplyState(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 审核状态查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_queryApplyState()
        ass.verity(json.loads(rs)['code'], "10000")
        # ass.verityContain(json.loads(rs)['data'], "authList")
        # ass.verityContain(json.loads(rs)['data'], "close")
        # ass.verityContain(json.loads(rs)['data'], "loanReportVO")
        # ass.verityContain(json.loads(rs)['data'], "step2SubStateList")
        # ass.verityContain(json.loads(rs)['data'], "replayDateOfMonth")

    def test_022_api_78dk_clientapp_loan_loanApply_submitApply(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 提交申请
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_submitApply(applyamount='', loanterm='', loanuse='',
                                                                       city='', productdetailuuid='')
        ass.verity(json.loads(rs)['code'], "S0006")

    def test_023_api_78dk_clientapp_loan_loanApply_querySignConResult(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 签约结果查询
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_querySignConResult()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "state")

    def test_024_api_78dk_clientapp_loan_loanApply_queryLoanPro(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 产品列表
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_queryLoanPro()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "productDetailUuid")
        ass.verityContain(json.loads(rs)['data'], "name")

    def test_025_api_78dk_clientapp_loan_loanApply_queryPeriod(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 期数列表
        """
        productdetailuuid = eq.get_info('product_detail', 'product_detail_uuid')[0]
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_queryPeriod(productdetailuuid=productdetailuuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "period")
        ass.verityContain(json.loads(rs)['data'], "rate")

    def test_026_api_78dk_clientapp_loan_loanApply_querySignUrl(self):
        """
          Time       :2019-04-26
          author     : 罗林
          desc       : 获取签约地址
        """
        rs = ea_app.test_api_78dk_clientapp_loan_loanApply_querySignUrl()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "signUrl")
