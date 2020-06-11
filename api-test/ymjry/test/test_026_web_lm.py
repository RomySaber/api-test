#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       : 2020/02/11
@Author     : 罗林
@File       : test_026_web_lm.py
@desc       : 放款管理自动化测试用例
"""

import json

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.testAction import WebAction
from ymjry.testAction import loginAction



class test_026_web_lm(TestBaseCase):
    def test_001_base_saveRepayDiscountPackage(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = WebAction.test_api_78dk_platform_lm_uploadContractImgs(
            contractuuid=contract_uuid, datas='')
        Assertion.verity(json.loads(res)['code'], 'S0006')
        Assertion.verity(json.loads(res)['msg'], '属性转换错误')

    def test_002_base_saveRepayDiscountPackage_contractuuid_error(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_uploadContractImgs(
            contractuuid=-1, datas='')
        Assertion.verity(json.loads(res)['code'], 'S0006')
        Assertion.verity(json.loads(res)['msg'], '属性转换错误')

    def test_003_base_saveRepayDiscountPackage_contractuuid_null(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_uploadContractImgs(
            contractuuid='', datas='')
        Assertion.verity(json.loads(res)['code'], 'S0006')
        Assertion.verity(json.loads(res)['msg'], '属性转换错误')

    def test_004_base_saveRepayDiscountPackage_datas_null(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_uploadContractImgs(
            contractuuid=contract_uuid, datas='')
        Assertion.verity(json.loads(res)['code'], 'S0006')
        Assertion.verity(json.loads(res)['msg'], '属性转换错误')

    def test_005_base_saveRepayDiscountPackage_datas_error(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_uploadContractImgs(
            contractuuid=contract_uuid, datas=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '系统发生内部异常，请稍候再试')

    def test_006_lm_viewContractImgs(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewContractImgs(
            contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_007_lm_viewContractImgs_null(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewContractImgs(contractuuid='')
        Assertion.verity(json.loads(res)['code'], 'S0006')
        Assertion.verity(json.loads(res)['msg'], '参数缺失')

    def test_008_lm_viewContractImgs_error(self):
        """
        合同图片上传(ym1.0.1)
        :return:
        """
        res = WebAction.test_api_78dk_platform_lm_viewContractImgs(contractuuid=-1)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_009_contract_contractCancel(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=contract_uuid,
                                                                                     loanamount=10))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '订单处于不可退单状态')

    def test_010_contract_contractCancel_contractuuid_error(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=-1,
                                                                                     loanamount=10))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '退单异常')

    def test_012_contract_contractCancel_contractuuid_null(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid='',
                                                                                     loanamount=10))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '退单异常')

    def test_013_contract_contractCancel_loanamount_error(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=contract_uuid,
                                                                                     loanamount=-1))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '订单处于不可退单状态')

    def test_014_contract_contractCancel_loanamount_null(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=contract_uuid,
                                                                                     loanamount=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统发生内部异常，请稍候再试')

    def test_015_contract_contractCancel_loanamount_str(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=contract_uuid,
                                                                                     loanamount='abc'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '系统发生内部异常，请稍候再试')

    def test_016_contract_contractCancel_loanamount_zero(self):
        """
        退单-悦美v1.0.0
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractCancel(contractuuid=contract_uuid,
                                                                                     loanamount=0))
        Assertion.verity(res['code'], 'S0001')
        Assertion.verity(res['msg'], '订单金额不能为0！')

    def test_017_contract_contractAnnul(self):
        """
        撤单v1.0.2
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractAnnul(contractuuid=contract_uuid))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '撤单失败，该订单正在审核中')

    def test_018_contract_contractAnnul_null(self):
        """
        撤单v1.0.2
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractAnnul(contractuuid=''))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '撤单失败，不存在该订单')

    def test_019_contract_contractAnnul_error(self):
        """
        撤单v1.0.2
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_om_contract_contractAnnul(contractuuid=-1))
        Assertion.verity(res['code'], 'S0003')
