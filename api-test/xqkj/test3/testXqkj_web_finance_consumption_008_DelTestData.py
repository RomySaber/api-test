#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-16 下午 4:29
@Author     : 罗林
@File       : testXqkj_web_finance_consumption_008_DelTestData.py
@desc       : 删除测试数据
"""

import os

from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import loginAction


class testXqkj_web_finance_consumption_008_DelTestData(TestBaseCase):
    def test_001_del_json_file(self):
        os.remove(os.path.join(os.path.dirname(loginAction.__file__), 'xqkj_data.json'))

    def test_002_del_user(self):
        # 删除平台用户信息
        user_uuids = xqkj_query.get_tbl_infos('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                              'POSITION("{}" IN name)'.format(loginAction.sign))
        print(user_uuids)
        xqkj_query.delete_info('Tbl_PlatformUserProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        for user_uuid in user_uuids:
            xqkj_query.delete_info('Tbl_PlatformUserPrivilegeRelation', 'platform_user_uuid="{}"'.format(user_uuid))

    def test_003_del_product(self):
        #  删除平台商品信息
        product_detail_uuids = xqkj_query.get_tbl_infos('Tbl_ProductDetail', 'product_detail_uuid',
                                                        'POSITION("{}" IN name)'.format(loginAction.sign))
        print(product_detail_uuids)
        xqkj_query.delete_info('Tbl_ProductDetail', 'POSITION("{}" IN name)'.format(loginAction.sign))
        for product_detail_uuid in product_detail_uuids:
            product_detail_config_uuids = xqkj_query.get_tbl_infos('Tbl_ProductDetailConfig',
                                                                   'product_detail_config_uuid',
                                                                   'product_detail_uuid="{}"'.format(
                                                                       product_detail_uuid))
            print(product_detail_config_uuids)
            xqkj_query.delete_info('Tbl_ProductDetailConfig', 'product_detail_uuid="{}"'.format(product_detail_uuid))
            for product_detail_config_uuid in product_detail_config_uuids:
                xqkj_query.delete_info('Tbl_ProductDetailConfigMerchantRelation',
                                       'product_detail_config_uuid="{}"'.format(product_detail_config_uuid))
            xqkj_query.delete_info('Tbl_ProductFundPackageRelation',
                                   'product_detail_uuid="{}"'.format(product_detail_uuid))
            xqkj_query.delete_info('Tbl_ProductMerchantRelation',
                                   'product_detail_uuid="{}"'.format(product_detail_uuid))

    def test_004_del_fundside(self):
        # 删除平台资金信息
        fund_package_uuids = xqkj_query.get_tbl_infos('Tbl_FundPackage', 'fund_package_uuid',
                                                      'POSITION("{}" IN name)'.format(loginAction.sign))
        fund_side_uuids = xqkj_query.get_tbl_infos('Tbl_FundSide', 'fund_side_uuid',
                                                   'POSITION("{}" IN name)'.format(loginAction.sign))
        print(fund_package_uuids)
        print(fund_side_uuids)
        xqkj_query.delete_info('Tbl_FundPackage', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_FundSide', 'POSITION("{}" IN name)'.format(loginAction.sign))
        for fund_package_uuid in fund_package_uuids:
            xqkj_query.delete_info('Tbl_FundSidePackageRelation', 'fund_package_uuid="{}"'.format(fund_package_uuid))
        for fund_side_uuid in fund_side_uuids:
            xqkj_query.delete_info('Tbl_FundSidePackageRelation', 'fund_side_uuid="{}"'.format(fund_side_uuid))

    def test_005_del_merchant(self):
        # 删除商户信息
        merchant_uuids = xqkj_query.get_tbl_infos('Tbl_MerchantProfile', 'merchant_uuid',
                                                  'POSITION("{}" IN name)'.format(loginAction.sign))
        store_uuids = xqkj_query.get_tbl_infos('Tbl_Store', 'store_uuid',
                                               'POSITION("{}" IN manager_name)'.format(loginAction.sign))
        print(merchant_uuids)
        print(store_uuids)
        xqkj_query.delete_info('Tbl_MerchantProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_Store', 'POSITION("{}" IN manager_name)'.format(loginAction.sign))
        for merchant_uuid in merchant_uuids:
            xqkj_query.delete_info('Tbl_MerchantProfile', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantStoreRelation', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantMoneyConfig', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantLegalPersonRelation', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantImage', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantClearingAccountRelation', 'merchant_uuid="{}"'.format(merchant_uuid))
            xqkj_query.delete_info('Tbl_MerchantBusinessInformationRelation',
                                   'merchant_uuid="{}"'.format(merchant_uuid))
        for store_uuid in store_uuids:
            xqkj_query.delete_info('Tbl_MerchantStoreRelation', 'store_uuid="{}"'.format(store_uuid))

    def test_006_del_channel(self):
        channel_uuids = xqkj_query.get_tbl_infos('Tbl_ChannelProfile', 'channel_uuid',
                                                 'POSITION("{}" IN name)'.format(loginAction.sign))
        print(channel_uuids)
        xqkj_query.delete_info('Tbl_ChannelProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        for channel_uuid in channel_uuids:
            xqkj_query.delete_info('Tbl_ChannelMerchantRelation', 'channel_uuid="{}"'.format(channel_uuid))
            xqkj_query.delete_info('Tbl_ChannelLegalPersonRelation', 'channel_uuid="{}"'.format(channel_uuid))
            xqkj_query.delete_info('Tbl_ChannelClearingAccountRelation', 'channel_uuid="{}"'.format(channel_uuid))
            xqkj_query.delete_info('Tbl_ChannelBusinessInformationRelation', 'channel_uuid="{}"'.format(channel_uuid))

    def test_007_del_legalPerson(self):
        # 删除平台法人代表信息
        legal_person_uuids = xqkj_query.get_tbl_infos('Tbl_LegalPerson', 'legal_person_uuid',
                                                      'POSITION("{}" IN name)'.format(loginAction.sign))
        print(legal_person_uuids)
        xqkj_query.delete_info('Tbl_LegalPerson', 'POSITION("{}" IN name)'.format(loginAction.sign))
        for legal_person_uuid in legal_person_uuids:
            xqkj_query.delete_info('Tbl_MerchantLegalPersonRelation',
                                   'legal_person_uuid="{}"'.format(legal_person_uuid))
            xqkj_query.delete_info('Tbl_ChannelLegalPersonRelation', 'legal_person_uuid="{}"'.format(legal_person_uuid))

    def test_008_del_clearingAccount(self):
        # 删除平台机构结算信息
        clearing_account_uuids = xqkj_query.get_tbl_infos('Tbl_ClearingAccount', 'clearing_account_uuid',
                                                          'POSITION("{}" IN account_name)'.format(loginAction.sign))
        print(clearing_account_uuids)
        xqkj_query.delete_info('Tbl_ClearingAccount', 'POSITION("{}" IN account_name)'.format(loginAction.sign))
        for clearing_account_uuid in clearing_account_uuids:
            xqkj_query.delete_info('Tbl_MerchantClearingAccountRelation',
                                   'clearing_account_uuid="{}"'.format(clearing_account_uuid))
            xqkj_query.delete_info('Tbl_ChannelClearingAccountRelation',
                                   'clearing_account_uuid="{}"'.format(clearing_account_uuid))

    def test_009_del_businessInformation(self):
        # 删除平台机构结算信息
        business_information_uuids = xqkj_query.get_tbl_infos('Tbl_BusinessInformation', 'business_information_uuid',
                                                              'POSITION("{}" IN email)'.format(loginAction.sign))
        print(business_information_uuids)
        xqkj_query.delete_info('Tbl_BusinessInformation', 'POSITION("{}" IN email)'.format(loginAction.sign))
        for business_information_uuid in business_information_uuids:
            xqkj_query.delete_info('Tbl_ChannelBusinessInformationRelation',
                                   'business_information_uuid="{}"'.format(business_information_uuid))
            xqkj_query.delete_info('Tbl_MerchantBusinessInformationRelation',
                                   'business_information_uuid="{}"'.format(business_information_uuid))

    def test_009_del_template(self):
        # 删除进件配置信息
        product_template_uuids = xqkj_query.get_tbl_infos('Tbl_ProductParamTemplate', 'product_template_uuid',
                                                          'POSITION("{}" IN template_name)'.format(loginAction.sign))
        print(product_template_uuids)
        xqkj_query.delete_info('Tbl_ProductParamTemplate', 'POSITION("{}" IN template_name)'.format(loginAction.sign))
        for product_template_uuid in product_template_uuids:
            xqkj_query.delete_info('Tbl_ProductParamTemplateConfig',
                                   'product_template_uuid="{}"'.format(product_template_uuid))
