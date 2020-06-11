#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-11 下午 3:06
@Author     : 罗林
@File       : test_017_app_Common.py
@desc       : 通用模块自动化测试用例
"""

import json
import unittest
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.testAction import AppAction, loginAction

fake = Factory().create('zh_CN')
contract_uuid = loginAction.global_dict.get('contract_uuid')
authorization = AppAction.API_TEST_HEADERS['authorization']
mobile = '18911390720'


class test_017_app_Common(TestBaseCase):
    def test_001_api_78dk_app_common_queryQiNiuToken(self):
        """
        获取七牛上传token
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_queryQiNiuToken())
        Assertion.verity(res['code'], '10000')

    def test_002_api_78dk_app_common_getCites(self):
        """
        获取城市列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getCites(parent=110000))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'name')

    def test_003_api_78dk_app_common_getCites_none(self):
        """
        获取城市列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getCites(parent=''))
        Assertion.verity(res['code'], '20000')

    def test_004_api_78dk_app_common_getCites_error(self):
        """
        获取城市列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getCites(parent='abc'))
        Assertion.verity(res['code'], '20000')

    def test_005_api_78dk_app_common_getCites_not_exits(self):
        """
        获取城市列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getCites(parent=fake.ean8()))
        Assertion.verity(res['code'], '10000')

    def test_006_api_78dk_app_common_getDictionaries_none(self):
        """
        获取字典列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype=''))
        Assertion.verity(res['code'], '10000')

    def test_007_api_78dk_app_common_getDictionaries_error(self):
        """
        获取字典列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='abc'))
        Assertion.verity(res['code'], '10000')

    def test_008_api_78dk_app_common_getDictionaries_not_exits(self):
        """
        获取字典列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype=fake.ean8()))
        Assertion.verity(res['code'], '10000')

    def test_009_api_78dk_app_common_getDictionaries_datum_type_worktime(self):
        """
        获取字典列表  工作时间
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_worktime'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_010_api_78dk_app_common_getDictionaries_datum_type_income(self):
        """
        获取字典列表  薪资
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_income'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_011_api_78dk_app_common_getDictionaries_datum_type_housing(self):
        """
        获取字典列表  房类型
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_housing'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_012_api_78dk_app_common_getDictionaries_datum_type_contact_relatives(self):
        """
        获取字典列表  亲属联系人
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_contact_relatives'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_013_api_78dk_app_common_getDictionaries_datum_type_contact_urgent(self):
        """
        获取字典列表  紧急联系人
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_contact_urgent'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_014_api_78dk_app_common_getDictionaries(self):
        """
        获取字典列表  婚姻状况：datum_type_marry
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_marry'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_015_api_78dk_app_common_getDictionaries_datum_type_education(self):
        """
        获取字典列表  学历：datum_type_education
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_education'))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'typeName')

    def test_016_api_78dk_app_common_getAllCites(self):
        """
        获取所有城市列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getAllCites())
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'id')
        Assertion.verityContain(res['data'], 'name')
        Assertion.verityContain(res['data'], 'parent')

    def test_017_api_78dk_app_common_getVersionInfo(self):
        """
        获取所有城市列表
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_getVersionInfo(channelno='', currentversnumb='', platform=''))
        Assertion.verity(res['code'], '20000')

    def test_018_api_78dk_app_common_idCardInit(self):
        """
        初始化(获取身份认证)
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_idCardInit())
        Assertion.verity(res['code'], '10000')

    def test_019_api_78dk_app_common_sms_sendValidate(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=1))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_020_api_78dk_app_common_sms_sendValidate_one(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=1))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_021_api_78dk_app_common_sms_sendValidate_two(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=2))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_022_api_78dk_app_common_sms_sendValidate_thr(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=3))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_023_api_78dk_app_common_sms_sendValidate_four(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=4))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_024_api_78dk_app_common_sms_sendValidate_fiv(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=5))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_025_api_78dk_app_common_sms_sendValidate_six(self):
        """
        发送短信
        类型[1. 注册; 2. 短信登陆; 3. 修改密码; 4.找回密码; 5: 更改手机号（旧手机号）；6：更改手机号（新手机号）]
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_sms_sendValidate(mobile='', type=6))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入手机号！')

    def test_026_api_78dk_app_perCenter_loanAgreement(self):
        """
        查看贷款协议
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_perCenter_loanAgreement(loanorderuuid=''))
        Assertion.verity(res['code'], '10000')

    def test_027_api_78dk_app_common_getAppReview_ios(self):
        """
        获取app审核环境（新）
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_getAppReview(platform='iOS'))
        Assertion.verity(res['code'], '10000')

    def test_028_api_78dk_app_common_getAppReview_Android(self):
        """
        获取app审核环境（新）
        :return:
        """
        res = json.loads(
            AppAction.test_api_78dk_app_common_getAppReview(platform='Android'))
        Assertion.verity(res['code'], '10000')

    def test_030_test_api_78dk_app_bill_getBillDetail(self):
        """
        账单明细(新)
        :return:
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = json.loads(AppAction.test_api_78dk_app_bill_getBillDetail(userbilluuid=contract_uuid))
        Assertion.verity(res['code'], '20000')

    def test_032_test_api_78dk_app_perCenter_loanData(self):
        """
        贷款资料
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_loanData(loanorderuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_033_test_api_78dk_app_perCenter_repaymentFormLists(self):
        """
        还款计划列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_repaymentFormLists(
            paraminfo=contract_uuid, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')

    def test_034_test_api_78dk_app_perCenter_loanAgreement(self):
        """
        查看贷款协议
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_loanAgreement(loanorderuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_035_test_api_78dk_app_perCenter_viewByStagesLists(self):
        """
        分期列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_viewByStagesLists(pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')

    @unittest.expectedFailure
    def test_036_api_78dk_app_perCenter_renounceApplication(self):
        """
        放弃申请
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_renounceApplication(loanorderuuid=contract_uuid))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '订单正在审核！')

    def test_037_api_78dk_app_perCenter_loanAgreement(self):
        """
        查看贷款协议
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_loanAgreement(loanorderuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_038_api_78dk_app_perCenter_loanDatail(self):
        """
        申请详情
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_loanDatail(loanorderuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    def test_039_api_78dk_app_perCenter_repaymentFormLists(self):
        """
        还款计划列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_perCenter_repaymentFormLists(
            paraminfo=contract_uuid, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')

    def test_040_test_api_78dk_app_common_getDictionaries(self):
        """
        获取字典列表
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype=''))
        Assertion.verity(res['code'], '10000')

    def test_041_test_api_78dk_app_common_getDictionaries_datum_type_properties(self):
        """
        获取字典列表 单位性质
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_properties'))
        Assertion.verity(res['code'], '10000')

    def test_042_test_api_78dk_app_common_getDictionaries_datum_type_scale(self):
        """
        获取字典列表 单位规模
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_scale'))
        Assertion.verity(res['code'], '10000')

    def test_043_test_api_78dk_app_common_getDictionaries_datum_type_worktime(self):
        """
        获取字典列表  工作时间
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_worktime'))
        Assertion.verity(res['code'], '10000')

    def test_044_test_api_78dk_app_common_getDictionaries_datum_type_income(self):
        """
        获取字典列表 薪资
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_income'))
        Assertion.verity(res['code'], '10000')

    def test_045_test_api_78dk_app_common_getDictionaries_datum_type_housing(self):
        """
        获取字典列表  住房类型
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_housing'))
        Assertion.verity(res['code'], '10000')

    def test_046_test_api_78dk_app_common_getDictionaries_datum_type_contact_relatives(self):
        """
        获取字典列表 亲属联系人
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_contact_relatives'))
        Assertion.verity(res['code'], '10000')

    def test_047_test_api_78dk_app_common_getDictionaries_datum_type_contact_urgent(self):
        """
        获取字典列表 紧急联系人
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_contact_urgent'))
        Assertion.verity(res['code'], '10000')

    def test_048_test_api_78dk_app_common_getDictionaries_datum_type_marry(self):
        """
        获取字典列表 婚姻状况
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_marry'))
        Assertion.verity(res['code'], '10000')

    def test_049_test_api_78dk_app_common_getDictionaries_datum_type_education(self):
        """
        获取字典列表  学历
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDictionaries(datumtype='datum_type_education'))
        Assertion.verity(res['code'], '10000')

    @unittest.skip('上一个流程还处理完成，不能处理当前流程')
    def test_050_api_78dk_app_common_takeGoods(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       : 确认收货V1.4.0，运营审核前收货失败
        """
        res = AppAction.test_api_78dk_app_perCenter_takeGoods(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['code'], 'S0003')
        Assertion.verityContain(json.loads(res)['msg'], '无权限操作')

    @unittest.skip('废弃')
    def test_051_common_userInfo(self):
        """
        author     : 罗林
        desc       : 用户信息-v1.0.0
        """
        res = json.loads(AppAction.test_api_78dk_app_common_userInfo())
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    @unittest.skip('废弃')
    def test_052__Header(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 用户token
        """
        res = json.loads(AppAction.test_Header(authorization=authorization))
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['msg'], '成功')

    def test_053_api_78dk_app_common_queryQiNiuTokenVideo(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 获取七牛视频上传token
        """
        res = json.loads(AppAction.test_api_78dk_app_common_queryQiNiuTokenVideo())
        Assertion.verity(res['code'], '10000')

    def test_054_api_78dk_app_common_getDomainNamet(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 获取项目域名
        """
        res = json.loads(AppAction.test_api_78dk_app_common_getDomainName())
        Assertion.verity(res['code'], '10000')

    def test_055_api_78dk_app_login_retrievePw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码,手机号格式不正确
        """
        res = json.loads(AppAction.test_api_78dk_app_login_retrievePw(mobile='', vercode=''))
        Assertion.verity(res['code'], '70000')
        Assertion.verityContain(res['msg'], '格式错误')

    def test_056_api_78dk_app_login_retrievePw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码,短信验证码为空
        """
        res = json.loads(AppAction.test_api_78dk_app_login_retrievePw(mobile=mobile, vercode=''))
        Assertion.verity(res['code'], 'S0012')
        Assertion.verityContain(res['msg'], '请输入短信验证码')

    def test_057_api_78dk_app_login_retrievePw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码,短信验证码错误
        """
        res = json.loads(AppAction.test_api_78dk_app_login_retrievePw(mobile=mobile, vercode='1234'))
        Assertion.verity(res['code'], 'S0012')
        Assertion.verityContain(res['msg'], '短信验证码错误!')

    def test_058_api_78dk_app_login_newPw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码(设置新密码),密码格式不正确
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(mobile=mobile, password=''))
        Assertion.verity(res['code'], '70000')
        Assertion.verityContain(res['msg'], '密码为6位数字')

    def test_059_api_78dk_app_login_newPw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码(设置新密码)，用户不存在
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(mobile=mobile, password='123456'))
        Assertion.verity(res['code'], '90000')
        Assertion.verityContain(res['msg'], '用户不存在')

    @unittest.expectedFailure
    def test_060_api_78dk_app_login_newPw(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 忘记密码(设置新密码)，密码为123456
        """
        res = json.loads(AppAction.test_api_78dk_app_login_newPw(mobile='', password='123456'))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '新密码和旧密码一致!')

    def test_061_api_78dk_app_login_register(self):
        """
        Time       :2019-11-28
        author     : 闫红
        desc       : 注册，手机号为空
        """
        res = json.loads(AppAction.test_api_78dk_app_login_register(mobile='', password='123456',vercode='',
              appversion='',ipaddress='',mobilename='',mobilenetwork='',registersource='',mobilesystem='',
              mobileuuid='',mobileversion='',))
        Assertion.verity(res['code'], '70000')
        Assertion.verity(res['msg'], '手机格式错误！')




