#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-11-28
@Author     : 六月
@File       : testCenter_meijia.py
@desc       : 接口中心-美佳金额接口测试用例
"""

from common.myCommon.TestBaseCase import TestBaseCase
from center.testAction import Center_meijiaAction as meijia


class testCenter_mj(TestBaseCase):
    def test_001_api_v2_2792(self):
        # 京东_获取二维码
        meijia.test_api_v2_2792(apiname='AI_JD_GET_QR', urladdress='meijia.78dk.com', useridentity='15111111111')

    def test_002_api_v2_2793(self):
        # 京东_获取二维码被扫描状态
        meijia.test_api_v2_2793(apiname='AI_JD_QR_STATUS', urladdress='meijia.78dk.com',
                                useridentity='15111111111', reqid='123456')

    def test_003_api_v2_2794(self):
        # 京东_获取短信验证码_ac:账号密码登陆
        meijia.test_api_v2_2794(apiname='AI_JD_GET_SMSCODE', urladdress='meijia.78dk.com', useridentity='15111111111',
                                reqid='123456', type='ac')

    def test_004_api_v2_2794(self):
        # 京东_获取短信验证码_qr:二维码登陆
        meijia.test_api_v2_2794(apiname='AI_JD_GET_SMSCODE', urladdress='meijia.78dk.com', useridentity='15111111111',
                                reqid='123456', type='qr')

    def test_005_api_v2_2795(self):
        # 京东_验证短信码_ac:账号密码登陆
        meijia.test_api_v2_2795(apiname='AI_JD_VERIFY_SMSCODE', urladdress='meijia.78dk.com',
                                useridentity='15111111111',
                                code='789456', name='zhangsan', password='456456', reqid='1234', type='ac')

    def test_006_api_v2_2795(self):
        # 京东_验证短信码_qr:二维码登陆
        meijia.test_api_v2_2795(apiname='AI_JD_VERIFY_SMSCODE', urladdress='meijia.78dk.com',
                                useridentity='15111111111',
                                code='789456', name='zhangsan', password='456456', reqid='1234', type='qr')

    def test_007_api_v2_2796(self):
        # 京东_账号密码登陆
        meijia.test_api_v2_2796(apiname='AI_JD_AC_LOG', urladdress='meijia.78dk.com', useridentity='15111111111',
                                name='lisi', password='456456')

    def test_008_api_v2_2792(self):
        # 淘宝_获取二维码
        # meijia.test_api_v2_2792(apiname='AI_TB_GET_QR', urladdress='meijia.78dk.com', useridentity='15111111111')
        meijia.test_api_v2_2792(apiname='', urladdress='', useridentity='')

    def test_009_api_v2_2793(self):
        # 淘宝_获取二维码被扫描状态
        meijia.test_api_v2_2793(apiname='AI_TB_QR_STATUS', urladdress='meijia.78dk.com',
                                useridentity='15111111111', reqid='123456')

    def test_010_api_v2_2794(self):
        # 淘宝_获取短信验证码_ac:账号密码登陆
        meijia.test_api_v2_2794(apiname='AI_TB_GET_SMSCODE', urladdress='meijia.78dk.com', useridentity='15111111111',
                                reqid='123456', type='ac')

    def test_011_api_v2_2795(self):
        # 淘宝_获取短信验证码_qr:二维码登陆
        meijia.test_api_v2_2795(apiname='AI_TB_GET_SMSCODE', urladdress='meijia.78dk.com', useridentity='15111111111',
                                reqid='123456', type='qr', code='789456', name='zhangsan', password='456456')

    def test_012_api_v2_2795(self):
        # 淘宝_验证短信码_ac:账号密码登陆
        meijia.test_api_v2_2795(apiname='AI_TB_VERIFY_SMSCODE', urladdress='meijia.78dk.com',
                                useridentity='15111111111',
                                code='789456', name='zhangsan', password='456456', reqid='1234', type='ac')

    def test_013_api_v2_2795(self):
        # 淘宝_验证短信码_qr:二维码登陆
        meijia.test_api_v2_2795(apiname='AI_TB_VERIFY_SMSCODE', urladdress='meijia.78dk.com',
                                useridentity='15111111111',
                                code='789456', name='zhangsan', password='456456', reqid='1234', type='qr')

    def test_014_api_v2_2796(self):
        # 淘宝_账号密码登陆
        meijia.test_api_v2_2796(apiname='', urladdress='', useridentity='15111111111',
                                name='lisi', password='456456')

    def test_015_api_v2_2798(self):
        # 获取手机号码类型
        meijia.test_api_v2_2798(apiname='ert', urladdress='6456', useridentity='ry', phone='5e54')

    def test_016_api_v2_2799(self):
        # 初始化配置
        meijia.test_api_v2_2799(apiname='5656', urladdress='rte', useridentity='ert', phone='6', phone_type='66')

    def test_017_api_v2_2800(self):
        # 获取二次短信验证码接口
        meijia.test_api_v2_2800(apiname='3', urladdress='5t', useridentity='r1', phone='3', phone_type='35', reqid='36')

    def test_018_api_v2_2801(self):
        # 获取图片验证码
        meijia.test_api_v2_2801(apiname='456', urladdress='75', useridentity='7', phone_type='rt', reqid='6')

    def test_019_api_v2_2802(self):
        # 登录
        meijia.test_api_v2_2802(apiname='4', urladdress='4', useridentity='4', password='4', phone='',
                                phone_type='4', piccode='4', randompassword='4', reqid='5')

    def test_020_api_v2_2803(self):
        # 二次验证码提交验证
        meijia.test_api_v2_2803(apiname='', urladdress='', useridentity='', code='', idcard='', name='',
                                password='', phone='', phone_type='', piccode='', reqid='')

    def test_021_api_v2_2804(self):
        # 获取二次图片验证码接口
        meijia.test_api_v2_2804(apiname='a', urladdress='s', useridentity='c', phone_type='r', reqid='f')

    def test_022_api_v1_aiCallback_2805(self):
        # AI回调接口中心通知接口
        meijia.test_api_v1_aiCallback_2805(status='5', taskid='6')

    def test_023_api_v2_2806(self):
        # 获取图片验证码
        meijia.test_api_v2_2806(apiname='67', urladdress='6', useridentity='df', reqid='f')

    def test_024_api_v2_2807(self):
        # 账号密码学校名称登录
        meijia.test_api_v2_2807(apiname='45', urladdress='fd', useridentity='g', code='5',
                                name='5', password='rt', reqid='fgdf', school='6556')

    def test_025_api_v2_2797(self):
        # 验证短信码
        meijia.test_api_v2_2797()

    def test_026_api_weixin_login_2808(self):
        # 登陆接口
        meijia.test_api_weixin_login_2808('', '')

    def test_027_api_weixin_findPassword_2809(self):
        # 找回密码
        meijia.test_api_weixin_findPassword_2809('', '', '')

    def test_028_api_weixin_sendMsg_2810(self):
        # 获取验证码
        meijia.test_api_weixin_sendMsg_2810('')

    def test_029_api_weixin_getSaUser_2811(self):
        # 获取SA人员
        meijia.test_api_weixin_getSaUser_2811('', '')

    def test_030_api_weixin_loanList_2812(self):
        # 放款信息列表
        meijia.test_api_weixin_loanList_2812('', '', '', '', '', '')

    def test_031_api_weixin_userBill_2813(self):
        # 全部账单
        meijia.test_api_weixin_userBill_2813('', '', '')

    def test_032_api_weixin_userList_2814(self):
        # 账单信息列表
        meijia.test_api_weixin_userList_2814('', '', '', '', '', '', '')

    def test_033_api_weixin_repaymentDetail_2815(self):
        # 还款信息详情
        meijia.test_api_weixin_repaymentDetail_2815('', '', '')

    def test_034_api_weixin_repaymentList_2816(self):
        # 还款信息列表
        meijia.test_api_weixin_repaymentList_2816('', '', '', '', '', '', '')

    def test_035_api_weixin_merchantList_2817(self):
        # 商户信息列表
        meijia.test_api_weixin_merchantList_2817('', '', '', '', '', '', '')

    def test_036_api_weixin_storeDetail_2818(self):
        # 门店信息详情
        meijia.test_api_weixin_storeDetail_2818('', '', '')

    def test_037_api_weixin_storeList_2819(self):
        # 门店列表
        meijia.test_api_weixin_storeList_2819('', '', '', '', '', '', '')

    def test_038_api_weixin_userBill_2820(self):
        # 全部账单
        meijia.test_api_weixin_userBill_2820('', '', '')

    def test_039_api_weixin_login_3173(self):
        # 登陆接口
        meijia.test_api_weixin_login_3173('', '')

    def test_040_api_weixin_loanList_3174(self):
        # 放款信息列表
        meijia.test_api_weixin_loanList_3174('', '', '', '', '', '', '', '', '')

    def test_041_api_weixin_loanDetail_3175(self):
        # 放款信息详情
        meijia.test_api_weixin_loanDetail_3175('', '', '')

    def test_042_api_weixin_userList_3176(self):
        # 账单信息列表
        meijia.test_api_weixin_userList_3176('', '', '', '', '', '', '', '', '', '')

    def test_043_api_weixin_userDetail_3177(self):
        # 还款信息详情
        meijia.test_api_weixin_repaymentDetail_3177('', '', '')

    def test_044_api_weixin_repaymentList_3178(self):
        # 还款信息列表
        meijia.test_api_weixin_repaymentList_3178('', '', '', '', '', '', '', '', '', '')

    def test_045_api_weixin_repaymentDetail_3179(self):
        # 还款信息详情
        meijia.test_api_weixin_repaymentDetail_3179('', '', '')

    def test_046_api_weixin_merchantList_3180(self):
        # 商户信息列表
        meijia.test_api_weixin_merchantList_3180('', '', '', '', '', '', '')

    def test_047_api_weixin_merchantDetail_3181(self):
        # 商户信息详情
        meijia.test_api_weixin_merchantDetail_3181('', '', '')

    def test_048_api_weixin_storeDetail_3182(self):
        # 门店信息详情
        meijia.test_api_weixin_storeDetail_3182('', '', '')

    def test_049_api_weixin_storeList_3183(self):
        # 门店列表
        meijia.test_api_weixin_storeList_3183('', '', '', '', '', '', '')

    def test_050_api_v2_3190(self):
        # 小启报告
        meijia.test_api_v2__3190('', '', '', '', '')

    def test_051_api_weixin_findPassword_3297(self):
        # 找回密码
        meijia.test_api_weixin_findPassword_3297('', '', '')

    def test_052_api_weixin_loanList_3298(self):
        # 放款信息列表
        meijia.test_api_weixin_loanList_3298('', '', '', '', '', '', '', '', '')

    def test_053_api_weixin_loanDetail_3299(self):
        # 放款信息详情
        meijia.test_api_weixin_loanDetail_3299('', '', '')

    def test_054_api_weixin_userList_3300(self):
        # 账单信息列表
        meijia.test_api_weixin_userList_3300('', '', '', '', '', '', '', '', '', '')

    def test_055_api_weixin_repaymentList_3301(self):
        # 还款信息列表
        meijia.test_api_weixin_repaymentList_3301('', '', '', '', '', '', '', '', '', '')

    def test_056_api_weixin_getProvince_3302(self):
        # 获取系统所有省份
        meijia.test_api_weixin_getProvince_3302('', '')

    def test_057_api_weixin_merchantList_3303(self):
        # 商户信息列表
        meijia.test_api_weixin_merchantList_3303('', '', '', '', '', '', '')

    def test_058_api_weixin_storeDetail_3304(self):
        # 门店信息详情
        meijia.test_api_weixin_storeDetail_3304('', '', '')

    def test_059_api_weixin_storeList_3305(self):
        # 门店列表
        meijia.test_api_weixin_storeList_3305('', '', '', '', '', '', '')