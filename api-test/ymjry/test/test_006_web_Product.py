#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-14 下午 3:34
@Author     : 罗林
@File       : test_006_web_Product.py
@desc       :  产品管理模块流程自动化测试用例
"""

import json
import unittest
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.testAction import WebAction
from ymjry.testAction import loginAction
from ymjry.testAction import specialAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
name = loginAction.sign + fake.name_male()
# 产品名称
product_name = fake.word() + '产品' + loginAction.sign


class test_006_web_Product(TestBaseCase):
    def test_001_api_78dk_platform_product_pmm_viewProductTemplateList_parts(self):
        """
        根据模板类型获取具体模板信息 - 进件配置
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_incoming_parts"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global in_uuid
        in_uuid = loginAction.global_dict.get('productTemplateUuid')

    def test_002_api_78dk_platform_product_pmm_viewProductTemplateList_audit(self):
        """
        根据模板类型获取具体模板信息 - 基本机审策略
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_machine_audit"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global ma_uuid
        ma_uuid = res['data'][0]['productTemplateUuid']

    def test_003_api_78dk_platform_product_pmm_viewProductTemplateList_contract(self):
        """
        根据模板类型获取具体模板信息 - 基本专用合同
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_electronic_contract"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global ele_uuid
        ele_uuid = res['data'][0]['productTemplateUuid']

    def test_004_api_78dk_platform_product_base_saveProduct(self):
        """
        添加产品模板 productname
        :return:
        """
        global fund_package_uuid, product_detail_uuid
        fund_package_uuid = global_dict.get('fundPackageUuid')
        productConfigs = [
            {"period": 6, "rate": 0.1, "state": "enabled", "interestPeriod": 0, "interestPrincipalPeriod": 0},
            {"period": 12, "rate": 0.1, "state": "enabled", "interestPeriod": 0, "interestPrincipalPeriod": 0}]
        res = WebAction.test_api_78dk_platform_product_base_saveProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth='', maxquota='300000',
            minquota='3000', name=product_name, overduegraceperiod=1, overduehandlingfeerate=0.02,
            overdueprincipalrate=0.01, productconfigs=productConfigs, productstate='product_state_enabled',
            remark='备注', repaymentdatetype='end_of_the_month', repaymentmethod='DBDX', secondhalfofthemonth='',
            state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid=ele_uuid, incomingpartstemplateuuid=in_uuid,
            machineaudittemplateuuid=ma_uuid, loanmode='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global_dict.set(productDetailUuid=json.loads(res)['data']['productDetailUuid'])
        product_detail_uuid = json.loads(res)['data']['productDetailUuid']

    def test_005_api_78dk_platform_product_base_saveProductEarlySettle(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        global productEarlySettleUuid
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays="",
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="",
            earlysettlesupport="early_repayment_support_no",
            earlysettlevoidmode="",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        productEarlySettleUuid = json.loads(res)['data']['productEarlySettleUuid']

    def test_006_api_78dk_platform_product_base_viewProductDetails_all(self):
        """
        查询产品模板
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_viewProductDetails(name='', pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])

    def test_007_api_78dk_platform_product_base_viewProductDetails_not_exits(self):
        """
        查询产品模板
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_viewProductDetails(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['totalCount'], 0)
        Assertion.verity(json.loads(res)['data']['totalPage'], 0)
        Assertion.verityNone(json.loads(res)['data']['dataList'])

    def test_008_api_78dk_platform_product_base_viewProductDetails(self):
        """
        查询产品模板
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_base_viewProductDetails(
            name=product_name, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data']['dataList'][0]['productDetailUuid'])

    def test_009_api_78dk_platform_product_base_viewProductDetail_error(self):
        """
        查询产品模板
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_viewProductDetail('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_010_api_78dk_platform_product_base_viewProductDetail(self):
        """
        查询产品模板
        :return:
        """

        res = json.loads(WebAction.test_api_78dk_platform_product_base_viewProductDetail(product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['productDetailUuid'], product_detail_uuid)
        Assertion.verity(res['data']['fundPackageUuid'], fund_package_uuid)
        Assertion.verityContain(res['data']['productConfigs'], 'period')
        for i in range(len(res['data']['productConfigs'])):
            if "6" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid
                productDetailConfigUuid = res['data']['productConfigs'][i]['productDetailConfigUuid']
                global_dict.set(productDetailConfigUuid=res['data']['productConfigs'][i]['productDetailConfigUuid'])
            if "12" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid_one
                productDetailConfigUuid_one = res['data']['productConfigs'][i]['productDetailConfigUuid']

    def test_011_api_78dk_platform_product_base_updateProduct(self):
        """
        编辑产品模板
        :return:
        """
        productConfigs = [
            {"interestPeriod": 0, "interestPrincipalPeriod": 0, "period": "6", "productDetailUuid": product_detail_uuid,
             "state": "enabled", "rate": "0.10000", "productDetailConfigUuid": productDetailConfigUuid},
            {"interestPeriod": 0, "interestPrincipalPeriod": 0, "period": "12",
             "productDetailUuid": product_detail_uuid, "state": "enabled", "rate": "0.10000",
             "productDetailConfigUuid": productDetailConfigUuid_one}]
        res = WebAction.test_api_78dk_platform_product_base_updateProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth=11, maxquota='300000',
            minquota='3000', name=product_name, overduegraceperiod=0, overduehandlingfeerate='0.02',
            overdueprincipalrate='0.01', productconfigs=productConfigs, productdetailuuid=product_detail_uuid,
            productstate='product_state_enabled', remark='备注', repaymentdatetype='actual_cycle',
            repaymentmethod='DBDX', secondhalfofthemonth=15, state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid=ele_uuid, incomingpartstemplateuuid=in_uuid,
            machineaudittemplateuuid=ma_uuid, loanmode='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_012_api_78dk_platform_product_base_viewProductDetail(self):
        """
        查询产品模板
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_base_viewProductDetail(product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['productDetailUuid'], product_detail_uuid)
        Assertion.verity(res['data']['fundPackageUuid'], fund_package_uuid)
        Assertion.verityContain(res['data']['productConfigs'], 'period')
        for i in range(len(res['data']['productConfigs'])):
            if "6" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid
                productDetailConfigUuid = res['data']['productConfigs'][i]['productDetailConfigUuid']
                global_dict.set(productDetailConfigUuid=res['data']['productConfigs'][i]['productDetailConfigUuid'])
            if "12" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid_one
                productDetailConfigUuid_one = res['data']['productConfigs'][i]['productDetailConfigUuid']

    def test_013_api_78dk_platform_product_base_updateProductState_disabled(self):
        """
        修改产品状态为禁用
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_updateProductState(
            uuid=product_detail_uuid, productstate='product_state_disabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_014_api_78dk_platform_product_base_updateProductState_enabled(self):
        """
        修改产品状态为启用
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_updateProductState(
            uuid=product_detail_uuid, productstate='product_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_015_api_78dk_platform_product_pmm_saveMerchantTX_error(self):
        """
        保存商户贴息   (商户贴息大于利率)
        :return:
        """
        global merchant_uuid
        merchant_uuid = global_dict.get('merchantUuid')
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!')

    def test_016_api_78dk_platform_product_pmm_saveMerchantTX_not_product_config(self):
        """
        保存商户贴息   (商户贴息等于利率)   没有绑定产品
        :return:
        """
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.1, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.1, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '商户没有关联产品或产品没有关联产品配置!')

    def test_017_api_78dk_platform_product_pmm_viewProductDetails_all(self):
        """
        查看产品信息列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'], 'electronicContractTemplateUuid')

    def test_018_api_78dk_platform_product_pmm_viewProductDetails_not_exits(self):
        """
        查看产品信息列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)
        Assertion.verityNone(res['data']['dataList'])

    def test_019_api_78dk_platform_product_pmm_viewProductDetails(self):
        """
        查看产品信息列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name=product_name, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verity(res['data']['totalCount'], 1)
        Assertion.verity(res['data']['totalPage'], 1)
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'][0]['productDetailUuid'], product_detail_uuid)

    def test_020_api_78dk_platform_product_pmm_findMerchantTX(self):
        """
        查询商户贴息
        :return:
        """
        global merchant_uuid
        merchant_uuid = global_dict.get('merchantUuid')
        res = WebAction.test_api_78dk_platform_product_pmm_findMerchantTX(
            merchantuuid=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityContain(json.loads(res)['data'], 'merchantUuid')
        Assertion.verityContain(json.loads(res)['data'], 'productDetailConfigUuid')
        Assertion.verityContain(json.loads(res)['data'], 'discountRate')
        Assertion.verityContain(json.loads(res)['data'], 'period')
        Assertion.verityContain(json.loads(res)['data'], 'rate')

    def test_021_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_not_exits(self):
        """
        根据产品id查询不相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)

    def test_022_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_not_uuid(self):
        """
        根据产品id查询不相关的商户列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'ProductDetailUuid不能为空!')

    def test_023_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_all(self):
        """
        根据产品id查询不相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name='', pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'], 'merchantUuid')

    def test_024_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(self):
        """
        根据产品id查询不相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'currentPage')
        Assertion.verityContain(res['data'], 'pageSize')
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        # Assertion.verityContain(res['data']['dataList'], merchant_uuid)

    def test_025_api_78dk_platform_product_pmm_viewInMerchantsByPuid_not_exits(self):
        """
        根据产品id查询相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)

    def test_026_api_78dk_platform_product_pmm_viewInMerchantsByPuid_not_uuid(self):
        """
        根据产品id查询相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name='', pagecurrent=1, pagesize=10, uuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'ProductDetailUuid不能为空!')

    def test_027_api_78dk_platform_product_pmm_viewInMerchantsByPuid(self):
        """
        根据产品id查询相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_028_api_78dk_platform_product_pmm_bindProductMerchant(self):
        """
        绑定产品和商户关系
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_product_pmm_viewInMerchantsByPuid_bind_after(self):
        """
        根据产品id查询相关的商户列表
        :return:
        """
        res = json.loads(WebAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        # Assertion.verityContain(res['data']['dataList'], merchant_uuid)

    def test_030_api_78dk_platform_product_pmm_unBindProductMerchant(self):
        """
        解绑产品和商户关系
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_pmm_unBindProductMerchant(
            productuuid=product_detail_uuid, merchantuuids=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_031_api_78dk_platform_product_pmm_bindProductMerchant(self):
        """
        绑定产品和商户关系
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_032_api_78dk_platform_product_pmm_findMerchantTX(self):
        """
        查询商户贴息
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_pmm_findMerchantTX(
            merchantuuid=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_033_api_78dk_platform_product_pmm_saveMerchantTX_er(self):
        """
        保存商户贴息   (商户贴息大于利率)   绑定产品
        :return:
        """
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!')

    def test_034_api_78dk_platform_product_pmm_saveMerchantTX(self):
        """
        保存商户贴息   (商户贴息小于利率)   绑定产品
        :return:
        """
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.05, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.05, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_035_api_78dk_platform_product_pmm_saveMerchantTX(self):
        """
        保存商户贴息
        :return:
        """
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.1, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.1, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_036_api_78dk_platform_product_base_viewFundPackages(self):
        """
        资金包列表查询
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_viewFundPackages(
            pagecurrent=1, pagesize=10, state="enable", name='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])

    def test_037_api_78dk_platform_product_base_viewFundPackages_name_not_exits(self):
        """
        资金包列表查询
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_viewFundPackages(
            pagecurrent=1, pagesize=10, state="enable", name=fake.ean8())
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verityNone(json.loads(res)['data']['dataList'])
        # Assertion.verityNotNone(json.loads(res)['data']['dataList'])

    def test_038_api_78dk_platform_product_base_saveProductEarlySettle_all_none(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays='',
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest='',
            earlysettlesupport='',
            earlysettlevoidmode='',
            productdetailuuid='',
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品uuid不能为空!')

    def test_039_api_78dk_platform_product_base_saveProductEarlySettle_support_unknown(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays="",
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="",
            earlysettlesupport="early_repayment_support_unknown",
            earlysettlevoidmode="",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_040_api_78dk_platform_product_base_saveProductEarlySettle_earlysettledays_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=-1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('接口未做参数类型校验')
    def test_041_api_78dk_platform_product_base_saveProductEarlySettle_earlysettledays_not_num(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays='abc',
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('接口未做参数类型校验')
    def test_042_api_78dk_platform_product_base_saveProductEarlySettle_earlysettledays_max(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=99999999999,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_043_api_78dk_platform_product_base_saveProductEarlySettle_earlysettledays_zero(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=0,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_044_api_78dk_platform_product_base_saveProductEarlySettle_interest_unknown(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_unknown",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_045_api_78dk_platform_product_base_saveProductEarlySettle_interest_only_month(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_only_month",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_046_api_78dk_platform_product_base_saveProductEarlySettle_interest_normal(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_normal",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_047_api_78dk_platform_product_base_saveProductEarlySettle_interest_free(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_048_api_78dk_platform_product_base_saveProductEarlySettle_mode_unknown(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_unknown",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_049_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_free_none(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_050_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_none(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='',
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('接口未做参数类型校验')
    def test_051_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_not_num(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays='abc',
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('接口未做参数类型校验')
    def test_052_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_max(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=9999999999,
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_053_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_min(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=0.0000000001,
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_054_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=-1,
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_055_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefredays_zero(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=0,
            earlysettlefrerate='1',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_056_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_none(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate='',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    @unittest.skip('接口未做参数类型校验')
    def test_057_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_not_num(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate='abc',
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_058_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_max(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=9999999999,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_059_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=-1,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_060_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_zero(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=0,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_061_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate_min(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=0.0000000001,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_062_api_78dk_platform_product_base_saveProductEarlySettle_mode_period_earlysettlefrerate(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=1,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_063_api_78dk_platform_product_base_saveProductEarlySettle_productdetailuuid_none(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays='10',
            earlysettlefredays='10',
            earlysettlefrerate='10',
            earlysettleinterest='early_settle_interest__unknown',
            earlysettlesupport='early_settle_support_unknown',
            earlysettlevoidmode='early_settle_void_mode_unknown',
            productdetailuuid='',
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品uuid不能为空!')

    def test_064_api_78dk_platform_product_base_saveProductEarlySettle_productdetailuuid_not_exits(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays='10',
            earlysettlefredays='10',
            earlysettlefrerate='10',
            earlysettleinterest='early_settle_interest__unknown',
            earlysettlesupport='early_settle_support_unknown',
            earlysettlevoidmode='early_settle_void_mode_unknown',
            productdetailuuid='123',
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品Uuid不存在!')

    def test_065_api_78dk_platform_product_base_saveProductEarlySettle_productearlysettleuuid_not_exits(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays='10',
            earlysettlefredays='10',
            earlysettlefrerate='10',
            earlysettleinterest='early_settle_interest__unknown',
            earlysettlesupport='early_settle_support_unknown',
            earlysettlevoidmode='early_settle_void_mode_unknown',
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='123')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品提前结清业务Uuid不存在!')

    def test_066_api_78dk_platform_product_base_saveProductEarlySettle_earlysettleinterest_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=1,
            earlysettleinterest="123",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '保存产品提前结清业务信息出错!')

    def test_067_api_78dk_platform_product_base_saveProductEarlySettle_earlysettlevoidmode_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=1,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="123",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '保存产品提前结清业务信息出错!')

    def test_068_api_78dk_platform_product_base_saveProductEarlySettle_earlysettlesupport_error(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=1,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="123",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '保存产品提前结清业务信息出错!')

    def test_069_api_78dk_platform_product_base_saveProductEarlySettle(self):
        """
        产品提前结清信息保存（新增、修改）
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_saveProductEarlySettle(
            earlysettledays=1,
            earlysettlefredays=1,
            earlysettlefrerate=1,
            earlysettleinterest="early_settle_interest_free",
            earlysettlesupport="early_repayment_support_yes",
            earlysettlevoidmode="early_settle_void_mode_period_free",
            productdetailuuid=product_detail_uuid,
            productearlysettleuuid=productEarlySettleUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_070_api_78dk_platform_product_base_viewProductEarlySettle_none(self):
        """
        查询产品提前结清模块信息, uuid为空
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_queryProductEarlySettleByProductDetailUuid(
            productdetailuuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '产品uuid不能为空!')

    def test_071_api_78dk_platform_product_base_viewProductEarlySettle(self):
        """
        查询产品提前结清模块信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_product_base_queryProductEarlySettleByProductDetailUuid(
            productdetailuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

