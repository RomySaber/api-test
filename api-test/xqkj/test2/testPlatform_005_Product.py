#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.mydb import MysqlClent
from xqkj.test1 import case_stream
from xqkj.testAction import PlatformAction
from xqkj.testAction import loginAction
from xqkj.testAction import specialAction

fake = Factory().create('zh_CN')
name = fake.name_male()

# 渠道
channelname_stream = fake.company() + '渠道下级stream' + loginAction.sign
email_stream = fake.email()
name_stream = fake.name_male() + loginAction.sign
namecount_stream = fake.name_male() + loginAction.sign
# 商户
# 与产品绑定的商户
merchantname_stream = fake.company() + '流程stream' + loginAction.sign
account_name_stream = fake.name_male() + loginAction.sign
st_name_stream = fake.name_male() + loginAction.sign
# 产品使用资金包
pFundSidename = fake.name_male() + '资方名stream' + loginAction.sign
pFundPackagename = fake.name_male() + '资金包名stream' + loginAction.sign
# 解绑商户
merchantname_stream_del = fake.company() + 'dele' + loginAction.sign
# 产品名称
productname = fake.name_male() + loginAction.sign
# 解除产品绑定
productnamedele = fake.name_male() + loginAction.sign
# 修改商户贴息产品
merchantnametest = fake.company() + loginAction.sign
productnametest = fake.name_male() + loginAction.sign
# 不相关产品
productnamenot = fake.name_male() + loginAction.sign


class testPlatform_005_Product(TestBaseCase):
    def test_001_saveFundPackage(self):
        case_stream.saveFundPackage(pFundSidename, pFundPackagename)

    def test_002_saveMerchant(self):
        case_stream.saveChannel(channelname_stream)
        case_stream.saveMerchant(channelname_stream, account_name_stream, name_stream, email_stream,
                                 merchantname_stream, st_name_stream)

    def test_003_saveMerchant_del(self):
        case_stream.saveMerchant(channelname_stream, account_name_stream, name_stream, email_stream,
                                 merchantname_stream_del, st_name_stream)

    def test_004_saveMerchant_test(self):
        case_stream.saveMerchant(channelname_stream, account_name_stream, name_stream, email_stream,
                                 merchantnametest, st_name_stream)

    def test_01api_78dk_platform_product_base_saveProduct(self):
        # 添加产品模板 productname
        sql = 'name="' + pFundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        productConfigs = [{'period': 6, 'rate': 0.1, 'state': 'enabled'},
                          {'period': 12, 'rate': 0.1, 'state': 'enabled'}]
        res = PlatformAction.test_api_78dk_platform_product_base_saveProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth='', maxquota='300000',
            minquota='3000', name=productname, overduegraceperiod=1, overduehandlingfeerate=0.02,
            overdueprincipalrate=0.01, productconfigs=productConfigs, productstate='product_state_enabled',
            remark='备注', repaymentdatetype='end_of_the_month', repaymentmethod='DBDX', secondhalfofthemonth='',
            state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid="a910b003c68340df9ae7ce92178629ab",
            incomingpartstemplateuuid="53256e8b73ee4a57b746757a5cccd339",
            machineaudittemplateuuid="8e6772a91adc4267bff0879c146a9294",
            loanmode='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_02api_78dk_platform_product_base_updateProduct(self):
        # 编辑产品模板
        sql = 'name="' + pFundPackagename + '" and state ="enabled"'
        # 资金包UUid
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        # 查询条件
        condition = "product_detail_uuid = '" + product_detail_uuid + "' and state = 'enabled'"
        # 分期UUid
        productDetailConfigUuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetailConfig',
                                                        'product_detail_config_uuid', condition)
        productConfigs = [{"period": "6", "productDetailUuid": product_detail_uuid, "state": "enabled",
                           "rate": "0.10000", "productDetailConfigUuid": productDetailConfigUuid},
                          {"period": "12", "productDetailUuid": product_detail_uuid, "state": "enabled",
                           "rate": "0.10000", "productDetailConfigUuid": productDetailConfigUuid}]
        res = PlatformAction.test_api_78dk_platform_product_base_updateProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth=0, maxquota='300000',
            minquota='3000', name=productname, overduegraceperiod=0, overduehandlingfeerate='0.02',
            overdueprincipalrate='0.01', productconfigs=productConfigs, productdetailuuid=product_detail_uuid,
            productstate='product_state_enabled', remark='备注', repaymentdatetype='actual_cycle',
            repaymentmethod='DBDX', secondhalfofthemonth=0, state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid="a910b003c68340df9ae7ce92178629ab",
            incomingpartstemplateuuid="53256e8b73ee4a57b746757a5cccd339",
            machineaudittemplateuuid="8e6772a91adc4267bff0879c146a9294", loanmode='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_03api_78dk_platform_product_base_viewProductDetail(self):
        # 查询产品模板
        sql = 'name="' + productname + '" and state ="enabled"'
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_base_viewProductDetail(product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['name'], productname)

    # def test_03_01api_78dk_platform_product_pmm_viewProductTemplateList(self):
    #     # 根据模板类型获取具体模板信息
    #     res = PlatformAction.test_api_78dk_platform_product_pmm_viewProductTemplateList(paramsingle='')
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')
    #     Assertion.verity(json.loads(res)['data']['name'], productname)

    def test_04api_78dk_platform_product_base_updateProductState_disabled(self):
        # 修改产品状态为禁用
        sql = 'name="' + productname + '" and state ="enabled"'
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_base_updateProductState(
            uuid=product_detail_uuid, productstate='product_state_disabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_05api_78dk_platform_product_base_updateProductState_enabled(self):
        # 修改产品状态为启用
        sql = 'name="' + productname + '" and state ="enabled"'
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_base_updateProductState(product_detail_uuid,
                                                                                    'product_state_enabled')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_06api_78dk_platform_product_base_viewProductDetails(self):
        # 产品列表
        res = PlatformAction.test_api_78dk_platform_product_base_viewProductDetails('测试产品', 1, 10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # 商户贴息
    def test_07api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息大于利率)
        # 添加产品
        sql = 'name="' + pFundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        productConfigs = [{'period': 6, 'rate': 0.1, 'state': 'enabled'},
                          {'period': 12, 'rate': 0.1, 'state': 'enabled'}]
        PlatformAction.test_api_78dk_platform_product_base_saveProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth=0, maxquota='300000',
            minquota='3000', name=productname, overduegraceperiod=0, overduehandlingfeerate='0.02',
            overdueprincipalrate='0.01', productconfigs=productConfigs, productstate='product_state_enabled',
            remark='备注', repaymentdatetype='actual_cycle', repaymentmethod='DBDX', secondhalfofthemonth=0,
            state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid="a910b003c68340df9ae7ce92178629ab",
            incomingpartstemplateuuid="53256e8b73ee4a57b746757a5cccd339",
            machineaudittemplateuuid="8e6772a91adc4267bff0879c146a9294",
            loanmode='')
        sql = 'name="' + productnametest + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'name="' + merchantnametest + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!!')

    def test_08api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息大于利率)
        sql = 'name="' + productnametest + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'name="' + merchantnametest + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '产品配置不存在!')

    def test_09api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息等于利率)   没有绑定产品
        sql = 'name="' + productnametest + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'name="' + merchantnametest + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        # Assertion.verity(json.loads(res)['msg'], '产品配置不存在!')

    def test_10api_78dk_platform_product_pmm_viewProductDetails(self):
        # 查看产品信息列表
        res = PlatformAction.test_api_78dk_platform_product_pmm_viewProductDetails('', 1, 999)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_11api_78dk_platform_product_pmm_findMerchantTX(self):
        # 查询商户贴息
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_pmm_findMerchantTX(merchant_uuid, product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data']['merchantUuid'],merchant_uuid)

    def test_12api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(self):
        # 根据产品id查询不相关的商户列表
        sql = 'name="' + productname + '" and state ="enabled"'
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid',
                                                    sql)  # 产品UUid
        res = PlatformAction.test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(
            name=productname, pagecurrent=1, pagesize=999, uuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_13api_78dk_platform_product_pmm_viewInMerchantsByPuid(self):
        # 根据产品id查询相关的商户列表
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(
            name=productname, pagecurrent=1, pagesize=999, uuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_14api_78dk_platform_product_pmm_bindProductMerchant(self):
        # 绑定产品和商户关系
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        # 查询条件
        condition = 'product_detail_uuid = {} and state = "enabled"'.format(product_detail_uuid)
        merchanttx = []
        res = PlatformAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchanttx=merchanttx, merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_15api_78dk_platform_product_pmm_unBindProductMerchant(self):
        # 解绑产品和商户关系
        # 添加产品
        sql = 'name="' + pFundPackagename + '" and state ="enabled"'
        fund_package_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_FundPackage', 'fund_package_uuid', sql)
        productConfigs = [{'period': 6, 'rate': 0.1, 'state': 'enabled'},
                          {'period': 12, 'rate': 0.1, 'state': 'enabled'}]
        PlatformAction.test_api_78dk_platform_product_base_saveProduct(
            discountrate='0.9', earlyrepaymentfreecycle=12, earlyrepaymenthandlingfee='0.02',
            earlyrepaymentsupport='early_repayment_support_yes', firsthalfofthemonth=0, maxquota='300000',
            minquota='3000', name=productnamedele, overduegraceperiod=0, overduehandlingfeerate='0.02',
            overdueprincipalrate='0.01', productconfigs=productConfigs, productstate='product_state_enabled',
            remark='备注', repaymentdatetype='actual_cycle', repaymentmethod='DBDX', secondhalfofthemonth=0,
            state='enabled', fundpackageuuid=fund_package_uuid,
            electroniccontracttemplateuuid="a910b003c68340df9ae7ce92178629ab",
            incomingpartstemplateuuid="53256e8b73ee4a57b746757a5cccd339",
            machineaudittemplateuuid="8e6772a91adc4267bff0879c146a9294",
            loanmode='')
        # 绑定商户
        sql = 'name="' + merchantname_stream_del + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        sql = 'name="' + productnamedele + '" and state ="enabled"'
        # 产品UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        merchanttx = []
        PlatformAction.test_api_78dk_platform_product_pmm_bindProductMerchant(
            merchanttx=merchanttx, merchantuuids=merchant_uuid, productuuid=product_detail_uuid)
        res = PlatformAction.test_api_78dk_platform_product_pmm_unBindProductMerchant(
            productuuid=product_detail_uuid, merchantuuids=merchant_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_16api_78dk_platform_product_pmm_findMerchantTX(self):
        # 查询商户贴息
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'product_detail_uuid="' + product_uuid + '" and state ="enabled"'
        # 产品配置UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetailConfig',
                                                    'product_detail_config_uuid', sql)
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_pmm_findMerchantTX(
            merchantuuid=merchant_uuid, productuuid=product_detail_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verity(json.loads(res)['data'][0]['merchantUuid'],merchant_uuid)

    def test_17api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息等于利率)   绑定产品
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'product_detail_uuid="' + product_uuid + '" and state ="enabled"'
        # 产品配置UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetailConfig',
                                                    'product_detail_config_uuid', sql)
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_18api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息大于利率)   绑定产品
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'product_detail_uuid="' + product_uuid + '" and state ="enabled"'
        # 产品配置UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetailConfig',
                                                    'product_detail_config_uuid', sql)
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户贴息不能大于产品利率!')

    def test_19api_78dk_platform_product_pmm_saveMerchantTX(self):
        # 保存商户贴息   (商户贴息小于利率)   绑定产品
        sql = 'name="' + productname + '" and state ="enabled"'
        # 产品UUid
        product_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        sql = 'product_detail_uuid="' + product_uuid + '" and state ="enabled"'
        # 产品配置UUid
        product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetailConfig',
                                                    'product_detail_config_uuid', sql)
        sql = 'name="' + merchantname_stream + '" and state ="enabled"'
        # 商户uuid
        merchant_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_MerchantProfile', 'merchant_uuid', sql)
        params = [{"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '6'},
                  {"rate": 0.1, "merchantUuid": merchant_uuid, "productDetailConfigUuid": product_detail_uuid,
                   "discountRate": 0.2, "period": '12'}]
        res = specialAction.test_api_78dk_platform_product_pmm_saveMerchantTX(params)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    # def test_20api_78dk_platform_product_base_deleteProduct(self):
    #     # 删除产品模版
    #     sql = 'name="' + productname + '" and state ="enabled"'
    #     product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
    #     res = PlatformAction.test_api_78dk_platform_product_base_deleteProduct(product_detail_uuid)
    #     Assertion.verity(json.loads(res)['code'], '10000')
    #     Assertion.verity(json.loads(res)['msg'], '成功')

    def test_21api_78dk_platform_product_base_viewFundPackages(self):
        # 删除产品模版
        # sql = 'name="' + productname + '" and state ="enabled"'
        # product_detail_uuid = MysqlClent.select_one(loginAction.DB, 'Tbl_ProductDetail', 'product_detail_uuid', sql)
        res = PlatformAction.test_api_78dk_platform_product_base_viewFundPackages(
            pagecurrent=1, pagesize=10, state='', name=pFundPackagename)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
