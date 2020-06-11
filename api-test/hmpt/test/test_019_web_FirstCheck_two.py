#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@Time       :2019-06-11 下午 3:33
@Author     : 罗林
@File       : test_019_web_FirstCheck_two.py
@desc       : 信审管理自动化测试用例
"""

import json
import unittest
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData as MD
from hmpt.query import xqkj_query
from hmpt.testAction import WebAction
from hmpt.testAction import loginAction
from hmpt.testAction import specialAction

fake = Factory().create('zh_CN')
labelcontent = loginAction.sign + MD.words_cn(2)
customerinformation = loginAction.sign + MD.words_cn(2)
impactdata = loginAction.sign + MD.words_cn(2)
windcontroldatasource = loginAction.sign + MD.words_en_lower(2)


class test_019_web_FirstCheck_two(TestBaseCase):
    @unittest.skip('美佳无')
    def test_001_api_78dk_platform_tm_first_xuexinreport(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 学信网报告 V1.3 新增
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = WebAction.test_api_78dk_platform_tm_first_xuexinreport(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('美佳无')
    def test_002_api_78dk_platform_tm_first_xuexinreport_contract_uuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 学信网报告 V1.3 新增,contract_uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_xuexinreport(contractuuid='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('美佳无')
    def test_003_api_78dk_platform_tm_first_xuexinreport_contract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 学信网报告 V1.3 新增,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_xuexinreport(contractuuid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_004_api_78dk_platform_tm_first_showSupplementImage(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 展示补录的图片资料 V1.3 新增 contract_uuid
        """
        global contract_uuid
        contract_uuid = loginAction.global_dict.get('contract_uuid')
        res = specialAction.test_api_78dk_platform_tm_first_showSupplementImage(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_005_api_78dk_platform_tm_first_showSupplementImage_contract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 展示补录的图片资料 V1.3 新增,contract_uuid不存在
        """
        res = specialAction.test_api_78dk_platform_tm_first_showSupplementImage(contractuuid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_006_api_78dk_platform_tm_first_showSupplementImage_contract_uuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 展示补录的图片资料 V1.3 新增,contract_uuid为空
        """
        res = specialAction.test_api_78dk_platform_tm_first_showSupplementImage(contractuuid='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_007_api_78dk_platform_tm_first_showSupplementImage_contract_uuid_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 展示补录的图片资料 V1.3 新增,contract_uuid超长
        """
        res = specialAction.test_api_78dk_platform_tm_first_showSupplementImage(contractuuid=MD.words_en_lower(256))
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_008_api_78dk_platform_tm_first_alipayreport(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 支付宝报告 V1.3 新增
        """
        res = WebAction.test_api_78dk_platform_tm_first_alipayreport(contractuuid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_009_api_78dk_platform_tm_first_alipayreport_contract_uuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 支付宝报告 V1.3 新增,contract_uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_alipayreport(contractuuid='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_010_api_78dk_platform_tm_first_alipayreport_contract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 支付宝报告 V1.3 新增,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_alipayreport(contractuuid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_011_api_78dk_platform_tm_first_alipayreport_contract_uuid_overlogn(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 支付宝报告 V1.3 新增,contract_uuid超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_alipayreport(contractuuid=MD.number(256))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    # @unittest.expectedFailure
    def test_012_api_78dk_platform_tm_bd_viewBdInfo(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 查询BD信息v1.3.0
        """
        res = WebAction.test_api_78dk_platform_tm_bd_viewBdInfo(uid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_013_api_78dk_platform_tm_bd_viewBdInfo_contract_uuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 查询BD信息v1.3.0,contract_uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_bd_viewBdInfo(uid='')
        # Assertion.verity(json.loads(res)['msg'], 'ContractUuid不能为空!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_014_api_78dk_platform_tm_bd_viewBdInfo_contract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 查询BD信息v1.3.0,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_bd_viewBdInfo(uid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['contractUuid'], '{}'.format(-1))

    def test_015_api_78dk_platform_tm_bd_viewBdInfo_contract_uuid_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 查询BD信息v1.3.0,contract_uuid超长
        """
        contract_uuid1 = MD.number(256)
        res = WebAction.test_api_78dk_platform_tm_bd_viewBdInfo(uid=contract_uuid1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['data']['contractUuid'], '{}'.format(contract_uuid1))

    @unittest.skip('获取接口参数错误')
    def test_016_api_78dk_platform_tm_first_addContractCustomerLabel_labelcontent_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 新增客户标签,labelcontent正常填写
        """
        res = WebAction.test_api_78dk_platform_tm_first_addContractCustomerLabel(
            labelcontent=labelcontent, contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_017_api_78dk_platform_tm_first_addContractCustomerLabel_labelcontent_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 新增客户标签,labelcontent为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_addContractCustomerLabel(
            labelcontent='', contractuuid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '标签内容不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('获取接口参数错误')
    def test_018_api_78dk_platform_tm_first_addContractCustomerLabel_contract_uuid_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 新增客户标签,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_addContractCustomerLabel(
            labelcontent='', contractuuid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '标签内容不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('获取接口参数错误')
    def test_019_api_78dk_platform_tm_first_viewLabels(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 标签查询v1.3.0，查询新增的标签
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewLabels()
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['data'], '{}'.format(labelcontent), '断言包含新增标签')

    @unittest.skip('获取接口参数错误')
    def test_020_api_78dk_platform_tm_first_deleteContractCustomerLabel(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 删除客户标签v1.3.0
        """
        global label_uuid
        label_uuid = xqkj_query.get_label_uuid(contract_uuid)
        res = WebAction.test_api_78dk_platform_tm_first_deleteContractCustomerLabel(uid=label_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_021_api_78dk_platform_tm_first_viewLabels_is_del(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 标签查询v1.3.0，标签被删除后查询
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewLabels()
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityNotContain(json.loads(res)['data'], '{}'.format(labelcontent), message='断言不包含被删除标签')

    def test_022_api_78dk_platform_tm_first_saveCustomerInformationis_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 客户信息 保存接口 V1.3 新增,客户信息为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveCustomerInformation(
            contractuuid=contract_uuid, customerinformation='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_023_api_78dk_platform_tm_first_saveCustomerInformation_contract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 客户信息 保存接口 V1.3 新增,customerinformation为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveCustomerInformation(
            contractuuid=-1, customerinformation=customerinformation)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_024_api_78dk_platform_tm_first_saveCustomerInformation_contract_uuid_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 客户信息 保存接口 V1.3 新增,contract_uuid超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveCustomerInformation(
            contractuuid=MD.number(256), customerinformation=customerinformation)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_025_api_78dk_platform_tm_first_saveCustomerInformation_customerinformation_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 客户信息 保存接口 V1.3 新增,contract_uuid超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveCustomerInformation(
            contractuuid=contract_uuid, customerinformation=MD.words_cn(256))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_026_api_78dk_platform_tm_first_saveImpactData_impactdata_is_null(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 影像资料 保存接口 V1.3 新增,impactdata为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveImpactData(contractuuid=contract_uuid, impactdata='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_027_api_78dk_platform_tm_first_saveImpactData_contractuuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 影像资料 保存接口 V1.3 新增,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveImpactData(
            contractuuid=-1, impactdata=impactdata)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_028_api_78dk_platform_tm_first_saveImpactData_contractuuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 影像资料 保存接口 V1.3 新增
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveImpactData(
            contractuuid=contract_uuid, impactdata=impactdata)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_029_api_78dk_platform_tm_first_queryElectronuclearRemark(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 查询接口 V1.3 新增
        """
        res = specialAction.test_api_78dk_platform_tm_first_queryElectronuclearRemark(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_030_api_78dk_platform_tm_first_queryElectronuclearRemark_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 查询接口 V1.3 新增,contract_uuid不存在
        """
        res = specialAction.test_api_78dk_platform_tm_first_queryElectronuclearRemark(contractuuid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_031_api_78dk_platform_tm_first_queryElectronuclearRemark_overlong(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 查询接口 V1.3 新增,contract_uuid不存在
        """
        res = specialAction.test_api_78dk_platform_tm_first_queryElectronuclearRemark(contractuuid=MD.uuid_random(256))
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_032_api_78dk_platform_tm_first_saveWindControlDataSourcecontract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 风控数据源 保存接口,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveWindControlDataSource(
            contractuuid=-1, windcontroldatasource='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_033_api_78dk_platform_tm_first_saveWindControlDataSourcecontract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 风控数据源 保存接口，windcontroldatasource为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveWindControlDataSource(
            contractuuid=contract_uuid, windcontroldatasource='')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_034_api_78dk_platform_tm_first_saveWindControlDataSourcecontract_uuid_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 电核备注 - 风控数据源 保存接口，正常保存
        """
        res = WebAction.test_api_78dk_platform_tm_first_saveWindControlDataSource(
            contractuuid=contract_uuid, windcontroldatasource=windcontroldatasource)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_035_api_78dk_platform_tm_first_setSupplementState2Yes(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 翻转合同补录状态为Yes
        """
        res = WebAction.test_api_78dk_platform_tm_first_setSupplementState2Yes(contractuuid=contract_uuid)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_036_api_78dk_platform_tm_first_setSupplementState2Yes_not_exist(self):
        """
        Time       :2019-07-22
        author     : 闫红
        desc       : 翻转合同补录状态为Yes,合同为不存在的合同
        """
        res = WebAction.test_api_78dk_platform_tm_first_setSupplementState2Yes(contractuuid=-1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_037_api_78dk_platform_tm_first_viewContractOperationLogs(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询合同操作日志
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogs(
            uuid=contract_uuid, pagesize=10, pagecurrent=1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_038_api_78dk_platform_tm_first_viewContractOperationLogs_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询合同操作日志,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogs(
            uuid=-1, pagesize=10, pagecurrent=1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_039_api_78dk_platform_tm_first_viewContractOperationLogs_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询合同操作日志,contract_uuid超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogs(
            uuid=MD.words_en_lower(256), pagesize=10, pagecurrent=1)
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_040_api_78dk_platform_tm_first_viewContractOperationLogs_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询合同操作日志,contract_uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogs(
            uuid='', pagesize=10, pagecurrent=1)
        Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('获取接口参数错误')
    def test_041_api_78dk_platform_tm_first_viewContractLabels(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 通过合同UUID查询对应的客户标签
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractLabels(uid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_042_api_78dk_platform_tm_first_viewContractLabels_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 通过合同UUID查询对应的客户标签，UUID不存在
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractLabels(uid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '合同uuid不合法')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('获取接口参数错误')
    def test_043_api_78dk_platform_tm_first_viewContractLabels_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 通过合同UUID查询对应的客户标签，UUID超长
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractLabels(uid=MD.words_en_lower(256))
        Assertion.verityContain(json.loads(res)['msg'], '合同uuid不合法')
        Assertion.verity(json.loads(res)['code'], '20000')

    @unittest.skip('获取接口参数错误')
    def test_044_api_78dk_platform_tm_first_viewContractLabels_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 通过合同UUID查询对应的客户标签，UUID为空,查询所有
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractLabels(uid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.skip('获取接口参数错误')
    def test_045_api_78dk_platform_tm_first_viewContractLabels_is_None(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 通过合同UUID查询对应的客户标签，UUID为None
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractLabels(uid=None)
        Assertion.verityContain(json.loads(res)['msg'], '系统发生内部异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_046_api_78dk_platform_tm_first_viewContractOperationLogInfo_OperationLoguuid_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询操作日志详情,contractoperationloguuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogInfo(
            contractuuid=contract_uuid, contractoperationloguuid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractOperationLogUuid不能为空!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_047_api_78dk_platform_tm_first_viewContractOperationLogInfo_contractuuid_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询操作日志详情,合同uuid、contractoperationloguuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogInfo(
            contractuuid='', contractoperationloguuid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_048_api_78dk_platform_tm_first_viewContractOperationLogInfo_contractuuid_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询操作日志详情,contractuuid、contractoperationloguuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogInfo(
            contractuuid=-1, contractoperationloguuid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractOperationLogUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_049_api_78dk_platform_tm_first_viewContractOperationLogInfo_contractuuid_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 查询操作日志详情,contractuuid超长，contractoperationloguuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_first_viewContractOperationLogInfo(
            contractuuid=MD.words_en_lower(256), contractoperationloguuid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractOperationLogUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_050_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 电核信息查询
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid=contract_uuid)
        # Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_051_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 电核信息查询,合同不存在
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_052_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 电核信息查询,合同uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid='')
        Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不能为空')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_053_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 电核信息查询,合同uuid超长
        """
        uuid1 = MD.words_en_lower(256)
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid=uuid1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_054_api_78dk_platform_tm_telephone_viewTelephoneCheckContract_is_None(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 电核信息查询,合同uuid为None
        """
        res = WebAction.test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(uid=None)
        Assertion.verityContain(json.loads(res)['msg'], '系统发生内部异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_055_api_78dk_platform_tm_final_finalCheck_pass(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,不存在的合同终审通过
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(uuid=-1, checkstate='pass',
                                                                   preamount='', finalchecksuggest=10000)
        # Assertion.verityContain(json.loads(res)['msg'], '终审金额不能为空!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_056_api_78dk_platform_tm_final_finalCheck_fail(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,不存在的合同终审打回
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(uuid=-1, checkstate='fail',
                                                                   preamount='', finalchecksuggest=10000)
        # Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不存在')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_057_api_78dk_platform_tm_final_finalCheck_canl(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,不存在的合同终审取消
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(uuid=-1, checkstate='cancel',
                                                                   preamount='', finalchecksuggest=10000)
        # Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不存在')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_058_api_78dk_platform_tm_final_finalCheck_return_first(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,不存在的合同终审返回初审
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(uuid=-1,
                                                                   checkstate='return_first', preamount='',
                                                                   finalchecksuggest=10000)
        # Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不存在')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_059_api_78dk_platform_tm_final_finalCheck_return_second(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,不存在的合同终审退回二审
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(uuid=-1,
                                                                   checkstate='return_second', preamount='',
                                                                   finalchecksuggest=10000)
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.expectedFailure
    def test_060_api_78dk_platform_tm_machine_resultMachine(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 终审,通过
        """
        res = WebAction.test_api_78dk_platform_tm_final_finalCheck(
            uuid=contract_uuid, checkstate='pass', preamount='', finalchecksuggest=10000)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_061_api_78dk_platform_tm_machine_resultMachine_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 机审详情,合同uuid为空
        """
        res = WebAction.test_api_78dk_platform_tm_machine_resultMachine(uuid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_062_api_78dk_platform_tm_machine_resultMachine_is_None(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 机审详情,合同uuid为None
        """
        res = WebAction.test_api_78dk_platform_tm_machine_resultMachine(uuid=None)
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_063_api_78dk_platform_tm_machine_resultMachine_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 机审详情,合同uuid为超长
        """
        res = WebAction.test_api_78dk_platform_tm_machine_resultMachine(uuid=MD.words_en_lower(256))
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_064_api_78dk_platform_tm_machine_resultMachine_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 机审详情,合同uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_machine_resultMachine(uuid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_065_api_78dk_platform_tm_operate_operationalCheck_all(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核列表查询,查询所有
        """
        res = WebAction.test_api_78dk_platform_tm_operate_operationalCheck(
            name='', pagecurrent=1, pagesize=10, state='all', phone='', begindate='', enddate='', uuid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_066_api_78dk_platform_tm_operate_operationalCheck_contactuuid_is_null(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核列表查询,contactuuid为空查询所有
        """
        res = WebAction.test_api_78dk_platform_tm_operate_operationalCheck(
            name='', pagecurrent=1, pagesize=10, state='all', phone='', begindate='', enddate='', uuid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_067_api_78dk_platform_tm_operate_operationalCheck_pass(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核列表查询,contactuuid为空查询pass
        """
        res = WebAction.test_api_78dk_platform_tm_operate_operationalCheck(
            name='', pagecurrent=1, pagesize=10, state='pass', phone='', begindate='', enddate='', uuid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_068_api_78dk_platform_tm_operate_operationalCheck_fail(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核列表查询,contactuuid为空查询fail
        """
        res = WebAction.test_api_78dk_platform_tm_operate_operationalCheck(
            name='', pagecurrent=1, pagesize=10, state='fail', phone='', begindate='', enddate='', uuid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_069_api_78dk_platform_tm_operate_operationalCheck_pending(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核列表查询,contactuuid为空查询fail
        """
        res = WebAction.test_api_78dk_platform_tm_operate_operationalCheck(
            name='', pagecurrent=1, pagesize=10, state='pending', phone='', begindate='', enddate='', uuid='')
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.expectedFailure
    def test_070_api_78dk_platform_tm_operate_operationalsave_fail(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核,审核拒绝
        """
        message = loginAction.sign + '拒绝'
        res = WebAction.test_api_78dk_platform_tm_operate_operationalsave(
            checkstate='fail', message=message, uuid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    @unittest.expectedFailure
    def test_071_api_78dk_platform_tm_operate_operationalsave_pass(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核,审核拒绝
        """
        message = loginAction.sign + '通过'
        res = WebAction.test_api_78dk_platform_tm_operate_operationalsave(
            checkstate='fail', message=message, uuid=contract_uuid)
        Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_072_api_78dk_platform_tm_operate_operationalsave_contact_uuid_not_exist_fail(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核,ContractUuid不存在、审核拒绝
        """
        message = loginAction.sign + '拒绝'
        res = WebAction.test_api_78dk_platform_tm_operate_operationalsave(
            checkstate='fail', message=message, uuid=-1)
        # Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不存在')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_073_api_78dk_platform_tm_operate_operationalsave_contact_uuid_not_exist_pass(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核,ContractUuid不存在、审核拒绝
        """
        message = loginAction.sign + '通过'
        res = WebAction.test_api_78dk_platform_tm_operate_operationalsave(
            checkstate='fail', message=message, uuid=-1)
        # Assertion.verityContain(json.loads(res)['msg'], 'ContractUuid不存在')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_074_api_78dk_platform_tm_operate_operationAllsave_fail(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核-批量,审核拒绝
        """
        message = loginAction.sign + '拒绝'
        res = WebAction.test_api_78dk_platform_tm_operate_operationAllsave(
            checkstate='fail', message=message, begindate='', phone='', enddate='',
            name='', state='pending', uuid=-1, pagecurrent=1)
        Assertion.verityContain(json.loads(res)['msg'], '存在非待审核订单')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_075_api_78dk_platform_tm_operate_operationAllsave_pass(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审核-批量,审核通过
        """
        message = loginAction.sign + '通过'
        res = WebAction.test_api_78dk_platform_tm_operate_operationAllsave(
            checkstate='fail', message=message, begindate='', phone='', enddate='',
            name='', state='pending', uuid=-1, pagecurrent=1)
        Assertion.verityContain(json.loads(res)['msg'], '存在非待审核订单')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_076_api_78dk_platform_tm_operate_viewOperateCheckContract(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审批信息查询
        """
        res = WebAction.test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid=contract_uuid)
        # Assertion.verityContain(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_077_api_78dk_platform_tm_operate_viewOperateCheckContract_not_exist(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审批信息查询,contract_uuid不存在
        """
        res = WebAction.test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid=-1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_078_api_78dk_platform_tm_operate_viewOperateCheckContract_overlong(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审批信息查询,contract_uuid超长
        """
        uid1 = MD.words_en_lower(256)
        res = WebAction.test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid=uid1)
        Assertion.verityContain(json.loads(res)['msg'], '查询合同基本信息时出错!')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_079_api_78dk_platform_tm_operate_viewOperateCheckContract_is_None(self):
        """
        Time       :2019-07-23
        author     : 闫红
        desc       : 运营审批信息查询,contract_uuid为None
        """
        uid1 = None
        res = WebAction.test_api_78dk_platform_tm_operate_viewOperateCheckContract(uid=uid1)
        Assertion.verityContain(json.loads(res)['msg'], '系统发生内部异常')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_080_api_78dk_platform_tm_operate_downOperationalCheck_all(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :运营列表导出-v1.4.0,导出全部
        """
        WebAction.test_api_78dk_platform_tm_operate_downOperationalCheck(begindate='', enddate='',
                                                                         name='', phone='', state='all',
                                                                         uuid=contract_uuid)

    def test_081_api_78dk_platform_tm_operate_downOperationalCheck_pass(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :运营列表导出-v1.4.0,导出通过的列表
        """
        WebAction.test_api_78dk_platform_tm_operate_downOperationalCheck(begindate='', enddate='',
                                                                         name='', phone='', state='pass',
                                                                         uuid=contract_uuid)

    def test_082_api_78dk_platform_tm_operate_downOperationalCheck_pass_fail(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :运营列表导出-v1.4.0,导出未通过审核的列表
        """
        WebAction.test_api_78dk_platform_tm_operate_downOperationalCheck(begindate='', enddate='',
                                                                         name='', phone='', state='fail',
                                                                         uuid=contract_uuid)

    def test_083_api_78dk_platform_tm_operate_downOperationalCheck_pass_pending(self):
        """
        Time       :2019-08-13
        author     : 闫红
        desc       :运营列表导出-v1.4.0,导出待审核的列表
        """
        WebAction.test_api_78dk_platform_tm_operate_downOperationalCheck(begindate='', enddate='',
                                                                         name='', phone='', state='pending',
                                                                         uuid=contract_uuid)
