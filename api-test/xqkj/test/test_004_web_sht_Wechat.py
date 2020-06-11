#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-08-12 上午 11:00
@Author     : 闫红
@File       : test_004_web_sht_Wechat.py
@desc       : 商户管理签约商户自动化测试用例， 商户通签约商户自动化测试用例
"""

import json

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from xqkj.testAction import ShtAction
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction
from xqkj.query import sht_query


class test_004_web_sht_Wechat(TestBaseCase):
    def test_001_api_78dk_platform_mm_base_viewWeChart_none(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信查看-v1.4,商户id为空
        """
        res = PlatformAction.test_api_78dk_platform_mm_base_viewWeChart(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_002_api_78dk_platform_mm_base_viewWeChart(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信查看-v1.4
        """
        global merchantUuid
        merchantUuid = loginAction.global_dict.get('merchantUuid')
        res = PlatformAction.test_api_78dk_platform_mm_base_viewWeChart(uid=merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_003_api_78dk_platform_mm_base_viewWeChart_merchant_not_exist(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信查看-v1.4，商户id不存在
        """
        res = PlatformAction.test_api_78dk_platform_mm_base_viewWeChart(uid=-1)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['msg'], '成功')

    def test_004_api_78dk_platform_mm_base_viewWeChart_merchant_overlong(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信查看-v1.4，商户id超长
        """
        res = PlatformAction.test_api_78dk_platform_mm_base_viewWeChart(uid=MockData.number(256))
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['msg'], '成功')

    def test_005_api_78dk_sht_merchant_binding_auditing_merchant(self):
        """
        商户绑定,  绑定一个审核中的商户
        :return:
        """
        global bindingnumber, merchantName
        bindingnumber = sht_query.get_merchant_number(merchantUuid)
        merchantName = sht_query.get_merchant_name(merchantUuid)
        sht_query.update_wx_merchart_null()
        # xqkj_query.delete_info("Tbl_WX_User", 'wx_user_uuid="{}"'.format(wx_info['wxUserUuid']))
        sht_query.update_audit_state("pending_review", merchantUuid)
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=merchantName,
                                                                      bindingnumber=bindingnumber))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_006_api_78dk_sht_merchant_binding_fail_merchant(self):
        """
        商户绑定,  绑定一个审核拒绝的商户
        :return:
        """
        sht_query.update_audit_state("fail", merchantUuid)
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=merchantName,
                                                                      bindingnumber=bindingnumber))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_008_api_78dk_sht_merchant_binding_error_merchant(self):
        """
        商户绑定,  绑定一个不存在的商户
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=MockData.wordAndNum(20),
                                                                      bindingnumber=bindingnumber))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_sht_merchant_binding_null_merchantname_none(self):
        """
        商户绑定,  没有输入商户名称，进行绑定
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname='', bindingnumber=bindingnumber))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_010_api_78dk_sht_merchant_binding_error_bindingnumber(self):
        """
        商户绑定,  绑定一个商户名称正确，编码错误的商户
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=merchantName,
                                                                      bindingnumber='4534543543鬼地方个发的广泛地'))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_sht_merchant_binding_null_bindingnumber_none(self):
        """
        商户绑定,  没有输入编号进行绑定
        :return:
        """
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=merchantName, bindingnumber=''))
        Assertion.verity(res['msg'], '公司名称或编码不正确')
        Assertion.verity(res['code'], '20000')

    def test_012_api_78dk_sht_merchant_binding(self):
        """
        商户绑定,  要在后端查找一个审核通过的正常商户，绑定没有上限的商户
        :return:
        """
        sht_query.update_open_close_state("open", merchantUuid)
        sht_query.update_audit_state("pass", merchantUuid)
        sht_query.update_wx_merchart_null()
        res = json.loads(ShtAction.test_api_78dk_sht_merchant_binding(merchantname=merchantName,
                                                                      bindingnumber=bindingnumber))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_013_api_78dk_platform_mm_base_unbind_wechart_is_master(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,主账号解绑
        """
        wx_list = [{'master': loginAction.wx_isMaster, 'weChart': loginAction.wx_name, 'wxUid': loginAction.wxUserUuid}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid=merchantUuid, list=wx_list)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_014_api_78dk_platform_mm_base_unbind_wechart_is_master(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,主账号解绑,微信id不存在
        """
        wx_list = [{'master': 'is_master_yes', 'weChart': '', 'wxUid': -1}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid=merchantUuid, list=wx_list)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_015_api_78dk_platform_mm_base_unbind_wechart_not_master(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,非主账号解绑,微信id不存在
        """
        wx_list = [{'master': 1, 'weChart': '', 'wxUid': -1}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid=merchantUuid, list=wx_list)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_016_api_78dk_platform_mm_base_unbind_wechart_not_master(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,非主账号解绑
        """
        wx_list = [{'master': loginAction.wx_isMaster, 'weChart': '', 'wxUid': loginAction.wxUserUuid}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid=merchantUuid, list=wx_list)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_017_api_78dk_platform_mm_base_unbind_uid_none(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,非主账号解绑
        """
        wx_list = [{'master': loginAction.wx_isMaster, 'weChart': '', 'wxUid': loginAction.wxUserUuid}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid='', list=wx_list)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_018_api_78dk_platform_mm_base_unbind_uid_error(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 微信解绑-v1.4,非主账号解绑
        """
        wx_list = [{'master': loginAction.wx_isMaster, 'weChart': '', 'wxUid': loginAction.wxUserUuid}]
        res = PlatformAction.test_api_78dk_platform_mm_base_unbind_wechart(uid=MockData.wordAndNum(20), list=wx_list)
        Assertion.verity(json.loads(res)['code'], '10000')
