#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-16 下午 3:38
@Author     : 罗林
@File       : test_xqkj_center.py
@desc       : 
"""

from faker import Faker

from center.testAction import XqkjcenterAction as xq
from common.myCommon.TestBaseCase import TestBaseCase

f = Faker(locale='zh_CN')
acctname = f.name() + 'test-api'
liceneceno = f.ssn(min_age=18, max_age=90)
phone = f.phone_number()

urladdress = xq.baseUrl.split('//')[-1]


class test_xqkj_center(TestBaseCase):
    def test_001_tdsq(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :申请同盾报告
        """
        xq.test_api_v2_89(apiname='WEB_TDREPLY_BATCH', urladdress=urladdress, acctname=acctname,
                          liceneceno=liceneceno, phone=phone)

    def test_002_tdcx(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :查询用户同盾报告
        """
        xq.test_api_v2_90(apiname='WEB_TDREPLY_BATCH', urladdress=urladdress, reportid='')

    def test_003_qy(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :签约申请接口
        """
        xq.test_api_v2_91(apiname='WEB_KQ_AUTH', urladdress=urladdress, userid='', bankcard='',
                          acctname=acctname, liceneceno=liceneceno, phone=phone)

    def test_004_qydx(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :签约短信验证接口
        """
        xq.test_api_v2_92(apiname='WEB_KQ_VERIFY', urladdress=urladdress, transactionid='',
                          validcode='')

    def test_005_dk(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :单笔代扣接口
        """
        xq.test_api_v2_93(apiname='WEB_KQ_DDPUR', urladdress=urladdress, paytransactionid='', userid='',
                          bankcard='', acctname=acctname, liceneceno=liceneceno, phone=phone, amount=100000,
                          paymentmark='')

    def test_006_zfxy(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :协议支付接口
        """
        xq.test_api_v2_94(apiname='WEB_KQ_QPAY', urladdress=urladdress, paytransactionid='', userid='',
                          bankcard='', phone=phone, amount=100000, paymentmark='')

    def test_007_dkcx(self):
        """
        Time       :2019-04-17
        author     : 罗林
        desc       :单笔代扣、协议支付结果查询
        """
        xq.test_api_v2_95(apiname='WEB_KQ_PAYQUERY', urladdress=urladdress, paytransactionid='',
                          txntype='', flag=1)

    def test_008_qn(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :获取七牛上传token
            """
        xq.test_api_v2_96(apiname='WEB_QINIU_TOKEN', urladdress=urladdress, bucket='weixin')

    def test_009_qnxz(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :获取图片下载私链
            """
        xq.test_api_v2_97(apiname='WEB_QINIU_GETPICTURE', urladdress=urladdress, baseurl='', qiniupickey='')

    def test_010_fdd(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :手动签署合同，返回法大大签署合同url
            """
        content = [{"ContractId": "XXXXXXXXX_A", "fill_2": "001", "fill_3": "北京海淀区11号",
                    "fill_4": "13438676620", "fill_5": "张三", "fill_6": "312312@1qq.com", },
                   {"ContractId": "XXXXXXXXX_B", "fill_2": "00111", "fill_3": "成都科华北路",
                    "fill_4": "13438676770", "fill_5": "李武"}]
        xq.test_api_v2_98(apiname='WEB_FDD_SIGN', urladdress=urladdress, acctname=acctname, liceneceno=liceneceno,
                          phone=phone, content=content)

    def test_011_fddcx(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :查询用户是否已经签署某份合同
            """
        xq.test_api_v2_99(apiname='WEB_FDD_SIGN_SEARCH', urladdress=urladdress, acctname=acctname,
                          liceneceno=liceneceno,
                          phone=phone, contractid='')

    def test_012_fddcx_zd(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :调签署接口（自动）。接入平台将合同签署状态更改为签署完成。
            """
        xq.test_api_v2_100(apiname='WEB_FDD_COMPANY_SIGN', urladdress=urladdress, contractid='', clientrole=1)

    def test_013_fddwc(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :接入平台将合同签署状态更改为签署完成
            """
        xq.test_api_v2_101(apiname='WEB_FDD_SAVE', urladdress=urladdress, contractid='')

    def test_014_dx(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :发送短信
            """
        xq.test_api_v2_102(apiname='WEB_JTLSENDMSG_BATCH', urladdress=urladdress, phone=phone, type=1901,
                           datas=100)

    def test_015_fk(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :根据传入的个人信息，获取在册的被执行信息
            """
        xq.test_api_v2_103(apiname='FK_CREDIT_DISHONEST', urladdress=urladdress, cardnum=liceneceno, name=acctname)

    def test_016_fkbg(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :根据传入task_id，获取对应风控报告
            """
        xq.test_api_v2_104(apiname='FK_REPORT', urladdress=urladdress, taskid='jingdong_ughkjnlkjhkj&aslkdyu7fh',
                           type='jingdong', mobile=phone)

    def test_017_faceId_ocridcard(self):
        """
            Time       :2019-04-17
            author     : 罗林
            desc       :根据传入身份证图片，获取图片内容。
            """
        xq.test_IP_api_faceId_ocridcard_105(
            project='fuqin', returnportrait=1,
            image='http://img3.imgtn.bdimg.com/it/u=1752243568,253651337&fm=26&gp=0.jpg')

    # def test_018_faceId_app_getBizToken(self):
    #     """
    #         Time       :2019-04-17
    #         author     : 罗林
    #         desc       :根据传入的认证参数，返回app所需的认证token。
    #         """
    #     xq.test_106(project='fuqin', bizno='', livenesstimeout=15, verbose=1,
    #                 securitylevel=1, forcecompare=0, multiorienteddetection=0,
    #                 comparisontype=0, livenesstype='raw_image')
    #
    # def test_019_faceId_app_verify(self):
    #     """
    #         Time       :2019-04-17
    #         author     : 罗林
    #         desc       :根据传入的认证参数，返回app所需的认证token。
    #         """
    #     xq.test_107(project='fuqin', token='', meglivedata='meglive')
