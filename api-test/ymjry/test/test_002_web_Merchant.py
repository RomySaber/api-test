#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-13 下午 4:41
@Author     : 罗林
@File       : test_002_web_Merchant.py
@desc       : 商户管理流程自动化测试用例
"""

import json
from faker import Factory
import unittest
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from ymjry.query import xqkj_query
from ymjry.testAction import WebAction
from ymjry.testAction import specialAction
from ymjry.testAction import loginAction


fake = Factory().create('zh_CN')
# 商户名称
merchantname = loginAction.sign + fake.company()
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = MockData.phone(11)
cardnumber = fake.ssn()
store_name = loginAction.sign + fake.company_prefix()
bd_name = loginAction.sign + fake.name()
bd_name2 = loginAction.sign + fake.name()
email2 = loginAction.sign + fake.email()
mobile2 = MockData.phone(11)
openerName = loginAction.sign + fake.name()


class test_002_web_Merchant(TestBaseCase):
    def test_001_api_78dk_platform_mm_base_saveMerchant(self):
        """
        新增商户基本信息
        :return:
        """
        global channelid
        channelid = loginAction.global_dict.get('channelid')
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name=merchantname, parentmerchantuuid='', shortname=merchantname[:5] + '商户简称',
            channeluuid=channelid, industryfirst=1, city="110100", industrysecond=6, province="110000"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'merchantUuid')
        global merchant_uuid
        merchant_uuid = res['data']['merchantUuid']
        loginAction.global_dict.set(merchantUuid=res['data']['merchantUuid'])

    def test_002_api_78dk_platform_mm_base_viewMerchant(self):
        """
        查询基本信息
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_viewMerchant(channelid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_003_api_78dk_platform_mm_base_viewMerchantList(self):
        """
        查询商户列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_viewMerchantList(pagecurrent=1, pagesize=10,
                                                                        name=merchantname, openclosestate='open',
                                                                        auditstate='imperfect',
                                                                        contractstatus='overdue',
                                                                        freezestate='normal', overquotastatus='yes')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_004_api_78dk_platform_mm_base_viewMerchantList_all(self):
        """
        查询商户列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_viewMerchantList(pagecurrent=1, pagesize=10, name='',
                                                                        openclosestate='open', auditstate='imperfect',
                                                                        contractstatus='overdue',
                                                                        freezestate='normal', overquotastatus='yes')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')

    def test_005_api_78dk_platform_mm_base_updateMerchant(self):
        """
        修改基本信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_updateMerchant(merchantuuid=merchant_uuid, note='',
                                                                      parentmerchantuuid='', name=merchantname,
                                                                      channeluuid=channelid,
                                                                      shortname=merchantname + '商户简称',
                                                                      industryfirst=0, city=0, industrysecond=0,
                                                                      province=0)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_006_api_78dk_platform_mm_state_viewStateMerchantList_all(self):
        """
        查询商户状态列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_viewStateMerchantList(name='', pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'auditState')

    def test_007_api_78dk_platform_mm_state_viewStateMerchantList(self):
        """
        查询商户状态列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_viewStateMerchantList(pagecurrent=1, pagesize=10,
                                                                              name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_008_api_78dk_platform_mm_state_viewStateMerchantList_not_exist(self):
        """
        查询商户状态列表
        :return:
        """
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = WebAction.test_api_78dk_platform_mm_state_viewStateMerchantList(pagecurrent=1, pagesize=10,
                                                                              name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityList(json.loads(res)['data']['dataList'], [])

    def test_009_api_78dk_platform_mm_examine_viewExamineMerchantList_all(self):
        """
        查询商户审核列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(pagesize=10, pagecurrent=1,
                                                                                  name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityContain(json.loads(res)['data'], 'dataList')
        Assertion.verityContain(json.loads(res)['data']['dataList'], 'auditState')

    def test_010_api_78dk_platform_mm_examine_viewExamineMerchantList(self):
        """
        查询商户审核列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(pagesize=10, pagecurrent=1,
                                                                                  name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantName'], merchantname)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['freezeState'], 'normal')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['openCloseState'], 'open')
        Assertion.verity(json.loads(res)['data']['dataList'][0]['channelUuid'], channelid)
        Assertion.verity(json.loads(res)['data']['dataList'][0]['merchantUuid'], merchant_uuid)

    def test_011_api_78dk_platform_mm_examine_viewExamineMerchantList_not_exist(self):
        """
        查询商户审核列表
        :return:
        """
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = WebAction.test_api_78dk_platform_mm_examine_viewExamineMerchantList(pagesize=10, pagecurrent=1,
                                                                                  name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityList(json.loads(res)['data']['dataList'], [])

    def test_012_api_78dk_platform_mm_money_saveMerchantMoney_amountday_none(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday='', amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_013_api_78dk_platform_mm_money_saveMerchantMoney_amountday_error(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=-1, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '单笔限额不能超过每日限额;')

    def test_014_api_78dk_platform_mm_money_saveMerchantMoney_amountmonth_none(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth='',
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_015_api_78dk_platform_mm_money_saveMerchantMoney_amountmonth_error(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=-1,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '每日限额不能超过每月限额;')

    def test_016_api_78dk_platform_mm_money_saveMerchantMoney_amountsingle_none(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle='', amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_017_api_78dk_platform_mm_money_saveMerchantMoney_amountsum_none(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum='',
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_018_api_78dk_platform_mm_money_saveMerchantMoney_amountsum_error(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=-1,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '每月限额不能超过总限额;')

    def test_019_api_78dk_platform_mm_money_saveMerchantMoney_merchantuuid_none(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid='', moneyconfiguuid='',
                                                                          zoomcoefficient=0.5,
                                                                          depositnotice='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'MerchantUuid不能为空!')

    def test_020_api_78dk_platform_mm_money_saveMerchantMoney_merchantuuid_error(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=-1, moneyconfiguuid='',
                                                                          zoomcoefficient=0.5,
                                                                          depositnotice='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户uuid不正确!')

    def test_022_api_78dk_platform_mm_money_saveMerchantMoney(self):
        """
        新增额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_saveMerchantMoney(amountday=150000, amountmonth=3000000,
                                                                          amountsingle=30000, amountsum=5000000,
                                                                          merchantuuid=merchant_uuid,
                                                                          moneyconfiguuid='', zoomcoefficient=0.5,
                                                                          depositnotice='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_023_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self):
        """
        根据商户Uuid查询额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['merchantUuid'], merchant_uuid)
        Assertion.verity(json.loads(res)['data']['zoomCoefficient'], 0.5)
        Assertion.verityContain(json.loads(res)['data'], 'moneyConfigUuid')
        global money_config_uuid
        money_config_uuid = json.loads(res)['data']['moneyConfigUuid']

    def test_024_api_78dk_platform_mm_money_updateMerchantMoney(self):
        """
        修改额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_updateMerchantMoney(amountday=10000, amountmonth=300000,
                                                                            amountsingle=10000, amountsum=500000,
                                                                            merchantuuid=merchant_uuid,
                                                                            moneyconfiguuid=money_config_uuid,
                                                                            zoomcoefficient=1.5, depositnotice='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_025_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self):
        """
        根据商户Uuid查询额度管理
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['merchantUuid'], merchant_uuid)
        Assertion.verity(json.loads(res)['data']['zoomCoefficient'], 1.5)
        Assertion.verity(json.loads(res)['data']['moneyConfigUuid'], money_config_uuid)

    def test_026_api_78dk_platform_mm_money_viewMerchantMoneyList_all(self):
        """
        风险控制列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(pagecurrent=1, pagesize=10, name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')

    def test_027_api_78dk_platform_mm_money_viewMerchantMoneyList_not_exits(self):
        """
        风险控制列表
        :return:
        """
        not_exist_name = '<meta http-equiv="Content-Type"content="text/html;charset=UTF-8"/>'
        res = WebAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(pagecurrent=1, pagesize=10,
                                                                              name=not_exist_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityNone(json.loads(res)['data']['dataList'])
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')

    def test_028_api_78dk_platform_mm_money_viewMerchantMoneyList(self):
        """
        风险控制列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_viewMerchantMoneyList(pagecurrent=1, pagesize=10,
                                                                              name=merchantname)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_mm_money_merchantMoneyEnlarge(self):
        """
        修改预授信放大系数
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_money_merchantMoneyEnlarge(uid=money_config_uuid,
                                                                             zoomcoefficient=2)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_030_api_78dk_platform_mm_base_saveMerchant_not_name(self):
        """
        新增商户基本信息失败，没有商户名称
        :return:
        """
        res = json.loads(
            WebAction.test_api_78dk_platform_mm_base_saveMerchant(note='备注', name='', parentmerchantuuid='',
                                                                  shortname=merchantname + '商户简称',
                                                                  channeluuid=channelid, industryfirst=0, city=0,
                                                                  industrysecond=0,
                                                                  province=0))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '商户名称不能为空!')

    def test_031_api_78dk_platform_mm_base_saveMerchant_not_shortname(self):
        """
        新增商户基本信息失败，没有商户简称
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_saveMerchant(note='备注', name=merchantname,
                                                                               parentmerchantuuid='', shortname='',
                                                                               channeluuid=channelid, industryfirst=0,
                                                                               city=0, industrysecond=0,
                                                                               province=0))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '商户简称不能为空!')

    def test_032_api_78dk_platform_mm_base_saveMerchant_not_channeluuid(self):
        """
        新增商户基本信息失败，没有所属渠道
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_saveMerchant(note='备注', name=merchantname,
                                                                               parentmerchantuuid='',
                                                                               shortname=merchantname + '商户简称',
                                                                               channeluuid='', industryfirst=0, city=0,
                                                                               industrysecond=0, province=0))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '渠道Uuid不能为空!')

    def test_033_api_78dk_platform_mm_base_legal_saveLegalPerson_not_name(self):
        """
        添加法人信息,缺少法人姓名
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber=cardnumber,
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile=mobile, name='',
                                                                             effectivetimebegin='',
                                                                             effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'Name不能为空!')

    def test_034_api_78dk_platform_mm_base_legal_saveLegalPerson_not_mobile(self):
        """
        添加法人信息，缺少法人电话
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber=cardnumber,
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile='', name=name,
                                                                             effectivetimebegin='',
                                                                             effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_035_api_78dk_platform_mm_base_legal_saveLegalPerson_not_cardnumber(self):
        """
        添加法人信息，缺少法人身份证
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber='',
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile=mobile,
                                                                             name=name, effectivetimebegin='',
                                                                             effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '身份证格式错误,')

    def test_036_api_78dk_platform_mm_base_legal_saveLegalPerson_error_mobile(self):
        """
        添加法人信息，法人电话不是1开头或非11位数字
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber=cardnumber,
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile='234567890123',
                                                                             name=name,
                                                                             effectivetimebegin='', effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '手机格式不合法,')

    def test_037_api_78dk_platform_mm_base_legal_saveLegalPerson(self):
        """
        添加法人信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber=cardnumber,
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile=mobile,
                                                                             name=name,
                                                                             effectivetimebegin="2019-08-01",
                                                                             effectivetimeend="2019-09-30")
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_038_api_78dk_platform_mm_base_legal_saveLegalPerson_error_cardnumber(self):
        """
        添加法人信息，法人身份证格式错误
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(cardnumber='格式错误2',
                                                                             channelormerchantuuid=merchant_uuid,
                                                                             legalpersonuuid='', mobile=mobile,
                                                                             name=name, effectivetimebegin='',
                                                                             effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '身份证格式错误,')

    def test_039_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant_not_uuid(self):
        """
        根据商户Uuid查询法人信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_040_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(self):
        """
        根据商户Uuid查询法人信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'legalPersonUuid')
        global merchantLegalPersonUuid
        merchantLegalPersonUuid = json.loads(res)['data']['legalPersonUuid']

    def test_041_api_78dk_platform_mm_base_legal_updateLegalPerson(self):
        """
        修改商户法人信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_updateLegalPerson(channelormerchantuuid=merchant_uuid,
                                                                               mobile=mobile, name=name,
                                                                               cardnumber=cardnumber,
                                                                               effectivetimebegin='',
                                                                               effectivetimeend='',
                                                                               legalpersonuuid=merchantLegalPersonUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_042_api_78dk_platform_mm_base_clear_saveClearingAccount(self):
        """
        为商户添加结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_clear_saveClearingAccount(accountname=name,
                                                                                 accountnumber='6011826564542944',
                                                                                 accountopeningbank='农业银行',
                                                                                 accounttype='public_accounts',
                                                                                 branchname='支行名称',
                                                                                 chamberlainidcard='431081199812097872',
                                                                                 channelormerchantuuid=merchant_uuid,
                                                                                 city="110100", clearingaccountuuid='',
                                                                                 linenumber='6756765756',
                                                                                 province="110000", region="110101")
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_043_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant_none(self):
        """
        查询商户结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_044_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(self):
        """
        查询商户结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'clearingAccountUuid')
        global clearing_account_uuid
        clearing_account_uuid = json.loads(res)['data']['clearingAccountUuid']

    def test_045_api_78dk_platform_mm_base_clear_updateClearingAccount(self):
        """
        修改商户结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_clear_updateClearingAccount(
            accountnumber='6011826564542944', accountopeningbank='农业银行', accounttype='public_accounts',
            branchname='支行名称', chamberlainidcard='431081199812097872', channelormerchantuuid=merchant_uuid,
            city='510100', clearingaccountuuid=clearing_account_uuid, linenumber='6756765756', province='510000',
            region='510101', accountname=name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_046_api_78dk_platform_mm_base_business_saveBusinessInfor(self):
        """
        新增机构信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor(
            channelormerchantuuid=merchant_uuid, organizationcode="123", socialunifiedcreditcode="123",
            taxregistrationnumber='123', installmentcooperationorgs=[{"installmentCooperationOrg": "123"},
                                                                     {"installmentCooperationOrg": ""},
                                                                     {"installmentCooperationOrg": ""}],
            contracttimebegin="2019-08-01", contracttimeend="2019-09-30", merge='yes',
            specialindustrytimebegin="2019-08-01", specialindustrytimeend="2019-09-30",
            specialindustrylicenseorname='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_047_api_i78dk_platform_mm_base_business_viewBusinessInfor(self):
        """
        根据商户Uuid查询机构信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['channelOrMerchantUuid'], merchant_uuid)
        Assertion.verityContain(json.loads(res)['data'], 'businessInformationUuid')
        global businessInformationUuid
        businessInformationUuid = json.loads(res)['data']['businessInformationUuid']

    def test_048_api_78dk_platform_mm_base_business_updateBusinessInfor(self):
        """
        修改机构信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_business_updateBusinessInfor(
            businessaddress='天府软件园',
            businessaddressgpsloction='',
            businessaddresszipcode='000000',
            businesshoursendtime='18:30',
            businesshoursstarttime='08:30',
            businessinformationuuid=businessInformationUuid,
            businessregistrationnumber='',
            channelormerchantuuid=merchant_uuid,
            documentaddress='天府软件园',
            email=email,
            organizationcode="567657675765",
            socialunifiedcreditcode="34534543534",
            storerentalendtime='2019-01-12',
            storerentalstarttime='2018-01-12',
            taxregistrationnumber='34543543543',
            documentprovince="510000",
            documentcity="510100",
            documentregion="510104",
            documentregionname='',
            businessprovince="510000",
            businesscity="510100",
            businessregion="510104",
            businessprovincename='',
            businesscityname='',
            businessregionname='',
            documentprovincename='',
            documentcityname='',
            installmentcooperationorgs=[],
            contracttimebegin='',
            contracttimeend='', merge='yes',
            specialindustrytimebegin='',
            specialindustrytimeend='',
            specialindustrylicenseorname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_049_api_78dk_platform_mm_base_store_saveStore(self):
        """
        为门店新增
        songchao
        :return:
        """
        begin, end = '2019-01-01', '2019-12-01'
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStore(
            businessaddress='经营地址',
            businessaddressgpsloction='', managername=name,
            managerphone=mobile, merchantuuid=merchant_uuid,
            storeuuid="", storename=store_name,
            province=510000, city=510100, region=510104,
            provincename='',
            cityname='', regionname='',
            idcardnumber=cardnumber, numberbegindate=begin,
            numberenddate=end,
            leasetimeend=end, area='100', email=email,
            employeesnum='10', leasetimebegin=begin)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global store_uuid
        store_uuid = json.loads(res)['data']['storeUuid']
        loginAction.global_dict.set(store_uuid=store_uuid)

    @unittest.skip('1.0.3删除')
    def test_051_api_78dk_platform_mm_base_store_saveImagesAndChange_add(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :门店影像图片信息保存-1.5.2,新增
        """
        # store_uuid = loginAction.global_dict.get('store_uuid')
        key = "FrRO9vzMUGeHYGR9uVjhmwwoRRvs"
        sysImageKey = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT", "MDPXXY"]
        images = [
            {"fileName": '1', 'handleType': 'add', "sysImageKey": imagekey, 'oldImageUuid': '', "storeUuid": store_uuid,
             "key": key} for imagekey in sysImageKey]
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('v1.0.3删除')
    def test_052_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_viewImageRoleList(self):
        """
        Time       :2019-10-09
        author     : 闫红
        desc       :门店影像资料查询-v1.5.2_正常
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewImageRoleList(uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global dict_list
        dict_list = dict()
        for k in json.loads(res)['data']:
            dict_list[k['sysImageKey']] = k['storeImageUuid']

    @unittest.skip('1.0.3删除')
    def test_052_api_78dk_platform_mm_base_store_saveImagesAndChange_edit(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :门店影像图片信息保存-1.5.2,编辑
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        # sysImageKey = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT", "MDPXXY"]
        images = [{"fileName": '1', 'handleType': 'edit', "sysImageKey": imagekey, 'oldImageUuid': oldstoreImageUuid,
                   "storeUuid": store_uuid, "key": key} for imagekey, oldstoreImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('1.0.3删除')
    def test_053_api_78dk_platform_mm_base_store_saveImagesAndChange_normal(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :门店影像图片信息保存-1.5.2,未操作
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        # sysImageKey = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT", "MDPXXY"]
        images = [{"fileName": '1', 'handleType': 'normal', "sysImageKey": imagekey, 'oldImageUuid': oldstoreImageUuid,
                   "storeUuid": store_uuid, "key": key} for imagekey, oldstoreImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('1.0.3删除')
    def test_054_api_78dk_platform_mm_base_store_saveImagesAndChange_del(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :门店影像图片信息保存-1.5.2,删除
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        # sysImageKey = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT", "MDPXXY"]
        images = [{"fileName": '1', 'handleType': 'normal', "sysImageKey": imagekey, 'oldImageUuid': oldstoreImageUuid,
                   "storeUuid": store_uuid, "key": key} for imagekey, oldstoreImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    @unittest.skip('1.0.3删除')
    def test_055_api_78dk_platform_mm_base_store_saveImagesAndChange_add(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :门店影像图片信息保存-1.5.2,新增
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        # sysImageKey = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT", "MDPXXY"]
        images = [
            {"fileName": '1', 'handleType': 'add', "sysImageKey": imagekey, 'oldImageUuid': '', "storeUuid": store_uuid,
             "key": key} for imagekey, oldstoreImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_056_api_78dk_platform_mm_base_store_updateStore(self):
        """
        修改门店
        songchao
        :return:
        """
        # global store_uuid
        # sql = 'manager_name="' + store_name + '" and state ="enabled"'
        # store_uuid = xqkj_query.get_info('Tbl_Store', 'store_uuid', sql)[0]
        # loginAction.global_dict.set(store_uuid=store_uuid)
        res = WebAction.test_api_78dk_platform_mm_base_store_updateStore(businessaddress='经营地址',
                                                                         businessaddressgpsloction='GPS地址',
                                                                         managername=name, managerphone='18911390729',
                                                                         merchantuuid=merchant_uuid,
                                                                         storeuuid=store_uuid, province=510000,
                                                                         city=510100, region=510104,
                                                                         provincename='阿萨德', cityname='带我去',
                                                                         regionname='看监控', storename=store_name,
                                                                         idcardnumber='511325199309280326',
                                                                         numberbegindate='2019-01-01',
                                                                         numberenddate='2019-12-01',
                                                                         employeesnum='111', area='12',
                                                                         email='song@78dk.com',
                                                                         leasetimebegin='2019-01-01',
                                                                         leasetimeend='2019-12-01')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_057_api_78dk_platform_mm_base_store_viewStoreList(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(pagecurrent=1, name=store_name,
                                                                           pagesize=10, uid=store_uuid,
                                                                           auditstate='pass', freezestate='normal',
                                                                           managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)

    def test_058_api_78dk_platform_mm_base_store_freeze(self):
        """
        查询门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStore(uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['storeUuid'], merchant_uuid)

    def test_059_api_78dk_platform_mm_base_store_viewStore(self):
        """
        冻结门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid=store_uuid, type='freeze')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['storeUuid'], merchant_uuid)

    def test_060_api_78dk_platform_mm_base_store_viewStore_uuid_none(self):
        """
        冻结门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid='', type='freeze')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户门店uuid不能为空')

    def test_061_api_78dk_platform_mm_base_store_viewStore_uuid_error(self):
        """
        冻结门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid=MockData.words_en(20), type='freeze')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '修改商户门店不存在!')

    def test_062_api_78dk_platform_mm_base_store_viewStore_type_error(self):
        """
        冻结门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid=store_uuid, type='hsjdh')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '提交商户门店冻结状态参数格式错误！')

    def test_063_api_78dk_platform_mm_base_store_viewStore_type_none(self):
        """
        冻结门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid=store_uuid, type='')
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['data']['storeUuid'], merchant_uuid)

    def test_064_api_78dk_platform_mm_base_store_viewStore(self):
        """
        解冻门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_freeze(uid=store_uuid, type='normal')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['storeUuid'], merchant_uuid)

    def test_065_api_78dk_platform_mm_saveContractImages(self):
        """
        商户图片资料保存-ym1.0.3
        :return:
        """
        image_url = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        keys = ["SHYYZZ", "SHFRSFZZ", "SHFRSFZF", "YLXKZ", "SHHZHT", "SHHJTP", "ZFHT"]
        images = [{"fileName": '1', "handleType":"add","sysImageKey": key, "merchantUuid": merchant_uuid, "key": image_url} for key in keys]
        res = json.loads(WebAction.test_api_78dk_platform_mm_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_066_api_78dk_platform_mm_base_store_uploadQrcode(self):
        """
        下载门店二维
        :return:
        """
        WebAction.test_api_78dk_platform_mm_base_store_uploadQrcode(merchant_uuid)

    def test_067_api_78dk_platform_mm_base_store_saveStore(self):
        """
        已有门店的商户再新增门店
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                       businessaddressgpsloction='',
                                                                       managername=store_name, managerphone=mobile,
                                                                       merchantuuid=merchant_uuid,
                                                                       storeuuid="", storename='', province=510000,
                                                                       city=510100, region=510104, provincename='',
                                                                       cityname='',
                                                                       regionname='', idcardnumber='',
                                                                       numberbegindate='2019-01-01',
                                                                       numberenddate='2019-01-01',
                                                                       leasetimeend='2019-01-01', area='100',
                                                                       email=email, employeesnum='10',
                                                                       leasetimebegin='2019-01-01')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '请输入门店名称')

    def test_068_api_78dk_platform_mm_base_findOptLog(self):
        """
        查询操作记录
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_findOptLog(merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_069_api_78dk_platform_om_bd_addBdInfo(self):
        """
        BD新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(channeluuid=channelid, email=email, mobile=mobile,
                                                               name=bd_name)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global bdinfouuid
        bdinfouuid = json.loads(res)['data']['bdInfoUuid']
        loginAction.global_dict.set(bdinfouuid=json.loads(res)['data']['bdInfoUuid'])
        loginAction.global_dict.set(bd_name=bd_name)

    def test_070_api_78dk_platform_mm_bd_saveBDMerchant_name_none(self):
        """
        新增商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid=bdinfouuid,
                                                                    merchantuuid=merchant_uuid, name='', remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '姓名不能为空!')

    def test_071_api_78dk_platform_mm_bd_saveBDMerchant_merchantuuid_none(self):
        """
        新增商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid=bdinfouuid, merchantuuid='',
                                                                    name=bd_name, remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户Uuid不能为空!')

    def test_072_api_78dk_platform_mm_bd_saveBDMerchant_bdInfoUuid_none(self):
        """
        新增商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid='', merchantuuid=merchant_uuid,
                                                                    name=bd_name, remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'BdInfoUuid不能为空!')

    def test_073_api_78dk_platform_mm_bd_saveBDMerchant(self):
        """
        新增商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid=bdinfouuid,
                                                                    merchantuuid=merchant_uuid, name=bd_name,
                                                                    remark='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_074_api_78dk_platform_mm_bd_findBDMerchant_none(self):
        """
        查询商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_findBDMerchant(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'MerchantUuid不能为空!')

    def test_075_api_78dk_platform_mm_bd_findBDMerchant(self):
        """
        查询商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_findBDMerchant(uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_076_api_78dk_platform_om_bd_addBdInfo(self):
        """
        BD新增
        :return:
        """
        res = WebAction.test_api_78dk_platform_om_bd_addBdInfo(channeluuid=channelid, email=email2, mobile=mobile2,
                                                               name=bd_name2)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global bdinfouuid2
        bdinfouuid2 = json.loads(res)['data']['bdInfoUuid']

    def test_077_api_78dk_platform_mm_bd_updateBDMerchant_name_none(self):
        """
        修改商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid=bdinfouuid,
                                                                      merchantuuid=merchant_uuid, name='', remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '姓名不能为空!')

    def test_078_api_78dk_platform_mm_bd_updateBDMerchant_merchantuuid_none(self):
        """
        修改商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid=bdinfouuid2, merchantuuid='',
                                                                      name=bd_name2, remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户Uuid不能为空!')

    def test_079_api_78dk_platform_mm_bd_updateBDMerchant_bdinfouuid_none(self):
        """
        修改商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid='', merchantuuid=merchant_uuid,
                                                                      name=bd_name2, remark='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'BdInfoUuid不能为空!')

    def test_080_api_78dk_platform_mm_bd_updateBDMerchant(self):
        """
        修改商户BD信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_bd_updateBDMerchant(bdinfouuid=bdinfouuid2,
                                                                      merchantuuid=merchant_uuid, name=bd_name2,
                                                                      remark='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_081_api_78dk_platform_mm_examine_merchanrExamine_fail(self):
        """
        商户审核fail
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='fail', message='不通过',
                                                                          uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_082_api_78dk_platform_mm_base_store_saveStore_examine_fail(self):
        """
        商户审核fail为商户新增门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                       businessaddressgpsloction='',
                                                                       managername=store_name, managerphone=mobile,
                                                                       merchantuuid=merchant_uuid,
                                                                       storeuuid="", storename='', province=510000,
                                                                       city=510100, region=510104, provincename='',
                                                                       cityname='',
                                                                       regionname='', idcardnumber='',
                                                                       numberbegindate='', numberenddate='',
                                                                       leasetimeend='', area='', email='',
                                                                       employeesnum='', leasetimebegin='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_083_api_78dk_platform_mm_examine_merchanrExamine_pass(self):
        """
        商户审核pass
        :return:
        """
        xqkj_query.update_info('Tbl_MerchantProfile', 'audit_state="pending_review"',
                               'merchant_uuid="{}"'.format(merchant_uuid))
        res = WebAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='pass', message='通过',
                                                                          uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_084_api_78dk_platform_mm_state_updateOpenCloseState_close(self):
        """
        修改商户开关为close
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_updateOpenCloseState(uid=merchant_uuid,
                                                                             updatestate='close')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_085_api_78dk_platform_mm_base_store_saveStore_State_close(self):
        """
        商户开关为close 为商户新增门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                       businessaddressgpsloction='',
                                                                       managername=store_name, managerphone=mobile,
                                                                       merchantuuid=merchant_uuid,
                                                                       storeuuid="", storename='', province=510000,
                                                                       city=510100, region=510104, provincename='',
                                                                       cityname='',
                                                                       regionname='', idcardnumber='',
                                                                       numberbegindate='', numberenddate='',
                                                                       leasetimeend='', area='', email='',
                                                                       employeesnum='', leasetimebegin='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_086_api_78dk_platform_mm_state_updateOpenCloseState_open(self):
        """
        修改商户开关为open
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_updateOpenCloseState(uid=merchant_uuid, updatestate='open')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_087_api_78dk_platform_mm_state_updateFreezeState_freeze(self):
        """
        修改商户冻结状态为freeze
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_updateFreezeState(uid=merchant_uuid, updatestate='freeze')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_088_api_78dk_platform_mm_base_store_saveStore_State_freeze(self):
        """
        商户冻结状态为freeze 为商户新增门店
        songchao
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStore(businessaddress='经营地址',
                                                                       businessaddressgpsloction='',
                                                                       managername=store_name, managerphone=mobile,
                                                                       merchantuuid=merchant_uuid,
                                                                       storeuuid="", storename='', province=510000,
                                                                       city=510100, region=510104, provincename='',
                                                                       cityname='',
                                                                       regionname='', idcardnumber='',
                                                                       numberbegindate='', numberenddate='',
                                                                       leasetimeend='', area='', email='',
                                                                       employeesnum='', leasetimebegin='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_089_api_78dk_platform_mm_state_updateFreezeState_normal(self):
        """
        修改商户冻结状态为normal
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_state_updateFreezeState(uid=merchant_uuid, updatestate='normal')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_090_api_78dk_platform_mm_examine_merchanrExamine_pass(self):
        """
        商户审核pass
        :return:
        """
        xqkj_query.update_info('Tbl_MerchantProfile', 'audit_state="pending_review"',
                               'merchant_uuid="{}"'.format(merchant_uuid))
        res = WebAction.test_api_78dk_platform_mm_examine_merchanrExamine(type='pass', message='通过',
                                                                          uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_091_api_78dk_platform_mm_examine_createTemporaryCode(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 生成临时编码-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_examine_createTemporaryCode(uid=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
