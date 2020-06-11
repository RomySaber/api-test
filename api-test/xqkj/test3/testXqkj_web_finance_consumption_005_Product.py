#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-14 下午 3:34
@Author     : 罗林
@File       : testXqkj_web_finance_consumption_005_Product.py
@desc       : 
"""

import json
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction
from xqkj.testAction import specialAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
name = loginAction.sign + fake.name_male()
# 产品名称
product_name = fake.word() + '产品' + loginAction.sign


class testXqkj_web_finance_consumption_005_Product(TestBaseCase):
    def test_01_api_78dk_platform_product_pmm_viewProductTemplateList_parts(self):
        # 根据模板类型获取具体模板信息 - 进件配置
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_incoming_parts"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global in_uuid
        in_uuid = res['data'][0]['productTemplateUuid']

    def test_02_api_78dk_platform_product_pmm_viewProductTemplateList_audit(self):
        # 根据模板类型获取具体模板信息 - 基本机审策略
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_machine_audit"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global ma_uuid
        ma_uuid = res['data'][0]['productTemplateUuid']

    def test_03_api_78dk_platform_product_pmm_viewProductTemplateList_contract(self):
        # 根据模板类型获取具体模板信息 - 基本专用合同
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(
            paramsingle="template_type_electronic_contract"))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data'][0]['productTemplateUuid'])
        global ele_uuid
        ele_uuid = res['data'][0]['productTemplateUuid']

    def test_04_api_78dk_platform_product_base_saveProduct(self):
        # 添加产品模板 productname
        global fund_package_uuid
        fund_package_uuid = global_dict.get('fundPackageUuid')
        productConfigs = [
            {"period": 6, "rate": 0.1, "state": "enabled", "interestPeriod": 0, "interestPrincipalPeriod": 0},
            {"period": 12, "rate": 0.1, "state": "enabled", "interestPeriod": 0, "interestPrincipalPeriod": 0}]
        res = PlatformAction.test_api_78dk_platform_product_base_saveProduct(
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

    def test_05_api_78dk_platform_product_base_viewProductDetails_all(self):
        # 查询产品模板
        res = PlatformAction.test_api_78dk_platform_product_base_viewProductDetails(name='', pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verityContain(json.loads(res)['data'], 'totalCount')
        Assertion.verityContain(json.loads(res)['data'], 'totalPage')
        Assertion.verityNotNone(json.loads(res)['data']['dataList'])

    def test_06_api_78dk_platform_product_base_viewProductDetails_not_exits(self):
        # 查询产品模板
        res = PlatformAction.test_api_78dk_platform_product_base_viewProductDetails(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verity(json.loads(res)['data']['currentPage'], 1)
        Assertion.verity(json.loads(res)['data']['pageSize'], 10)
        Assertion.verity(json.loads(res)['data']['totalCount'], 0)
        Assertion.verity(json.loads(res)['data']['totalPage'], 0)
        Assertion.verityNone(json.loads(res)['data']['dataList'])

    def test_07_api_78dk_platform_product_base_viewProductDetails(self):
        # 查询产品模板
        res = json.loads(PlatformAction.test_api_78dk_platform_product_base_viewProductDetails(
            name=product_name, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityNotNone(res['data']['dataList'][0]['productDetailUuid'])
        global_dict.set(productDetailUuid=res['data']['dataList'][0]['productDetailUuid'])

    def test_08_api_78dk_platform_product_base_viewProductDetail_error(self):
        # 查询产品模板
        res = PlatformAction.test_api_78dk_platform_product_base_viewProductDetail('')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_09_api_78dk_platform_product_base_viewProductDetail(self):
        # 查询产品模板
        global product_detail_uuid
        product_detail_uuid = global_dict.get('productDetailUuid')
        res = json.loads(PlatformAction.test_api_78dk_platform_product_base_viewProductDetail(product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['productDetailUuid'], product_detail_uuid)
        Assertion.verity(res['data']['fundPackageUuid'], fund_package_uuid)
        Assertion.verityContain(res['data']['productConfigs'], 'period')
        for i in range(len(res['data']['productConfigs'])):
            if "6" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid
                productDetailConfigUuid = res['data']['productConfigs'][i]['productDetailConfigUuid']
                global_dict.set(productDetailConfigUuid = res['data']['productConfigs'][i]['productDetailConfigUuid'])
            if "12" == res['data']['productConfigs'][i]['period']:
                global productDetailConfigUuid_one
                productDetailConfigUuid_one = res['data']['productConfigs'][i]['productDetailConfigUuid']

    def test_10_api_78dk_platform_product_base_updateProduct(self):
        # 编辑产品模板
        productConfigs = [
            {"interestPeriod": 0, "interestPrincipalPeriod": 0, "period": "6", "productDetailUuid": product_detail_uuid,
             "state": "enabled", "rate": "0.10000", "productDetailConfigUuid": productDetailConfigUuid},
            {"interestPeriod": 0, "interestPrincipalPeriod": 0, "period": "12",
             "productDetailUuid": product_detail_uuid, "state": "enabled", "rate": "0.10000",
             "productDetailConfigUuid": productDetailConfigUuid_one}]
        res = PlatformAction.test_api_78dk_platform_product_base_updateProduct(
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

    def test_11_api_78dk_platform_product_base_updateProductState_disabled(self):
        # 修改产品状态为禁用
        res = PlatformAction.test_api_78dk_platform_product_base_updateProductState(
            uuid=product_detail_uuid, productstate='product_state_disabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_12_api_78dk_platform_product_base_updateProductState_enabled(self):
        # 修改产品状态为启用
        res = PlatformAction.test_api_78dk_platform_product_base_updateProductState(
            uuid=product_detail_uuid, productstate='product_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # def test_13_api_78dk_platform_product_pmm_saveMerchantTX_error(self):
    #     # 保存商户贴息   (商户贴息大于利率)
    #     global merchant_uuid
    #     merchant_uuid = global_dict.get('merchantUuid')
    #     params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
    #                "discountRate": 0.2, "period": '6'},
    #               {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
    #                "discountRate": 0.2, "period": '12'}]
    #     res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
    #     Assertion.verity(json.loads(res)['code'], '20000')
    #     Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!')
    #
    # def test_14_api_78dk_platform_product_pmm_saveMerchantTX_not_product_config(self):
    #     # 保存商户贴息   (商户贴息等于利率)   没有绑定产品
    #     params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
    #                "discountRate": 0.1, "period": '6'},
    #               {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
    #                "discountRate": 0.1, "period": '12'}]
    #     res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
    #     Assertion.verity(json.loads(res)['code'], '20000')
    #     # Assertion.verity(json.loads(res)['msg'], '商户没有关联产品或产品没有关联产品配置!')

    def test_15_api_78dk_platform_product_pmm_viewProductDetails_all(self):
        # 查看产品信息列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name='', pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'], 'electronicContractTemplateUuid')

    def test_16_api_78dk_platform_product_pmm_viewProductDetails_not_exits(self):
        # 查看产品信息列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)
        Assertion.verityNone(res['data']['dataList'])

    def test_17_api_78dk_platform_product_pmm_viewProductDetails(self):
        # 查看产品信息列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewProductDetails(
            name=product_name, pagecurrent=1, pagesize=10))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verity(res['data']['totalCount'], 1)
        Assertion.verity(res['data']['totalPage'], 1)
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'][0]['productDetailUuid'], product_detail_uuid)

    def test_18_api_78dk_platform_product_pmm_findMerchantTX(self):
        # 查询商户贴息
        global merchant_uuid
        merchant_uuid = global_dict.get('merchantUuid')
        res = PlatformAction.test_api_78dk_platform_product_pmm_findMerchantTX(
            merchantuuid=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        Assertion.verityContain(json.loads(res)['data'], 'merchantUuid')
        Assertion.verityContain(json.loads(res)['data'], 'productDetailConfigUuid')
        Assertion.verityContain(json.loads(res)['data'], 'discountRate')
        Assertion.verityContain(json.loads(res)['data'], 'period')
        Assertion.verityContain(json.loads(res)['data'], 'rate')

    def test_19_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_not_exits(self):
        # 根据产品id查询不相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)

    def test_20_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_not_uuid(self):
        # 根据产品id查询不相关的商户列表
        res = PlatformAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'ProductDetailUuid不能为空!')

    def test_21_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid_all(self):
        # 根据产品id查询不相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name='', pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['currentPage'], 1)
        Assertion.verity(res['data']['pageSize'], 10)
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        Assertion.verityNotNone(res['data']['dataList'])
        Assertion.verityContain(res['data']['dataList'], 'merchantUuid')

    def test_22_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(self):
        # 根据产品id查询不相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'currentPage')
        Assertion.verityContain(res['data'], 'pageSize')
        Assertion.verityContain(res['data'], 'totalCount')
        Assertion.verityContain(res['data'], 'totalPage')
        # Assertion.verityContain(res['data']['dataList'], merchant_uuid)

    def test_23_api_78dk_platform_product_pmm_viewInMerchantsByPuid_not_exits(self):
        # 根据产品id查询相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['data']['totalCount'], 0)
        Assertion.verity(res['data']['totalPage'], 0)

    def test_24_api_78dk_platform_product_pmm_viewInMerchantsByPuid_not_uuid(self):
        # 根据产品id查询相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name='', pagecurrent=1, pagesize=10, uuid=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], 'ProductDetailUuid不能为空!')

    def test_25_api_78dk_platform_product_pmm_viewInMerchantsByPuid(self):
        # 根据产品id查询相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_26_api_78dk_platform_product_pmm_bindProductMerchant(self):
        # 绑定产品和商户关系
        product_detail_uuid = global_dict.get('productDetailUuid')
        merchant_uuid = global_dict.get('merchantUuid')
        res = PlatformAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_27_api_78dk_platform_product_pmm_viewInMerchantsByPuid_bind_after(self):
        # 根据产品id查询相关的商户列表
        res = json.loads(PlatformAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=product_name, pagecurrent=1, pagesize=10, uuid=product_detail_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        # Assertion.verityContain(res['data']['dataList'], merchant_uuid)

    def test_28_api_78dk_platform_product_pmm_unBindProductMerchant(self):
        # 解绑产品和商户关系
        # 添加产品
        # merchanttx = []
        res = PlatformAction.test_api_78dk_platform_product_pmm_unBindProductMerchant(
            productuuid=product_detail_uuid, merchantuuids=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_29_api_78dk_platform_product_pmm_bindProductMerchant(self):
        # 绑定产品和商户关系
        # merchanttx = []
        res = PlatformAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_30_api_78dk_platform_product_pmm_findMerchantTX(self):
        # 查询商户贴息
        res = PlatformAction.test_api_78dk_platform_product_pmm_findMerchantTX(
            merchantuuid=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_31_api_78dk_platform_product_pmm_saveMerchantTX_er(self):
        # 保存商户贴息   (商户贴息大于利率)   绑定产品
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!')

    # def test_32_api_78dk_platform_product_pmm_saveMerchantTX(self):
    #     # 保存商户贴息   (商户贴息小于利率)   绑定产品
    #     params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
    #                "discountRate": 0.05, "period": '6'},
    #               {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
    #                "discountRate": 0.05, "period": '12'}]
    #     res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #
    # def test_33_api_78dk_platform_product_pmm_saveMerchantTX(self):
    #     # 保存商户贴息
    #     params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid,
    #                "discountRate": 0.1, "period": '6'},
    #               {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": productDetailConfigUuid_one,
    #                "discountRate": 0.1, "period": '12'}]
    #     res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')
