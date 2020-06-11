#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-16 下午 4:29
@Author     : 罗林
@File       : test_016_DelTestData.py
@desc       : 删除测试数据
"""

import os

from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.query import xqkj_query
from ymjry.testAction import loginAction


class test_016_DelTestData(TestBaseCase):
    def test_001_del_json_file(self):
        """
        删除 数据文件
        :return:
        """
        os.remove(os.path.join(os.path.dirname(loginAction.__file__), loginAction.json_file + '.json'))

    def test_002_del_user(self):
        """
        删除平台用户信息
        :return:
        """
        user_uuids = xqkj_query.get_tbl_infos('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                              'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_PlatformUserProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_PlatformUserPrivilegeRelation', 'platform_user_uuid', user_uuids)

    def test_003_del_product(self):
        """
        删除平台商品信息
        :return:
        """
        product_detail_uuids = xqkj_query.get_tbl_infos('Tbl_ProductDetail', 'product_detail_uuid',
                                                        'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_ProductDetail', 'POSITION("{}" IN name)'.format(loginAction.sign))
        product_detail_config_uuids = xqkj_query.select_infos('Tbl_ProductDetailConfig',
            'product_detail_config_uuid', 'product_detail_uuid', product_detail_uuids)
        xqkj_query.delete_infos('Tbl_ProductDetailConfig', 'product_detail_uuid', product_detail_uuids)
        xqkj_query.delete_infos('Tbl_ProductDetailConfigMerchantRelation', 'product_detail_config_uuid',
                                product_detail_config_uuids)
        xqkj_query.delete_infos('Tbl_ProductFundPackageRelation', 'product_detail_uuid', product_detail_uuids)
        xqkj_query.delete_infos('Tbl_ProductMerchantRelation', 'product_detail_uuid', product_detail_uuids)
        xqkj_query.delete_infos('Tbl_ProductEarlySettle', 'product_detail_uuid', product_detail_uuids)
        RepayDiscountPackage = xqkj_query.select_infos('Tbl_ProductDetail', 'discount_package_uuid',
                                                       'product_detail_uuid', product_detail_uuids)
        xqkj_query.delete_infos('Tbl_RepayDiscountPackage', 'discount_package_uuid', RepayDiscountPackage)

    def test_004_del_fundside(self):
        """
        删除平台资金信息
        :return:
        """
        fund_package_uuids = xqkj_query.get_tbl_infos('Tbl_FundPackage', 'fund_package_uuid',
                                                      'POSITION("{}" IN name)'.format(loginAction.sign))
        fund_side_uuids = xqkj_query.get_tbl_infos('Tbl_FundSide', 'fund_side_uuid',
                                                   'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_FundPackage', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_FundSide', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_FundSidePackageRelation', 'fund_package_uuid', fund_package_uuids)
        xqkj_query.delete_infos('Tbl_FundSidePackageRelation', 'fund_side_uuid', fund_side_uuids)

    def test_005_del_merchant(self):
        """
        删除商户信息
        :return:
        """
        merchant_uuids = xqkj_query.get_tbl_infos('Tbl_MerchantProfile', 'merchant_uuid',
                                                  'POSITION("{}" IN name)'.format(loginAction.sign))
        store_uuids = xqkj_query.get_tbl_infos('Tbl_Store', 'store_uuid',
                                               'POSITION("{}" IN manager_name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_MerchantProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_Store', 'POSITION("{}" IN manager_name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_MerchantProfile', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantStoreRelation', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantMoneyConfig', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantLegalPersonRelation', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantImage', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantClearingAccountRelation', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantBusinessInformationRelation', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_BDMerchantRelation', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_WX_MerchantInformationDesc', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_LoanCount', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantProfileBond', 'merchant_uuid', merchant_uuids)
        xqkj_query.delete_infos('Tbl_MerchantStoreRelation', 'store_uuid', store_uuids)
        xqkj_query.delete_infos('Tbl_WX_UserStoreRelation', 'store_uuid', store_uuids)
        xqkj_query.delete_infos('Tbl_StoreBusiness', 'store_uuid', store_uuids)
        store_business_uuids = xqkj_query.select_infos('Tbl_StoreBusiness', 'store_business_uuid',
                                                       'store_uuid', store_uuids)
        xqkj_query.delete_infos('Tbl_StoreBusinessProduct', 'store_business_uuid', store_business_uuids)
        xqkj_query.delete_infos('Tbl_StoreImage', 'store_uuid', store_uuids)
        # 删除 微信 商户信息
        # sht_query.update_wx_merchart_null()
        # xqkj_query.delete_info('Tbl_WX_MerchantInformationDesc',
        #                        'created_uuid="{0}" OR updated_uuid="{0}" '.format(loginAction.wxUserUuid))
        # xqkj_query.delete_info('Tbl_WX_UserStoreRelation', 'wx_user_uuid="{}"'.format(loginAction.wxUserUuid))

    def test_006_del_channel(self):
        """
        删除渠道信息
        :return:
        """
        channel_uuids = xqkj_query.get_tbl_infos('Tbl_ChannelProfile', 'channel_uuid',
                                                 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_ChannelProfile', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_ChannelMerchantRelation', 'channel_uuid', channel_uuids)
        xqkj_query.delete_infos('Tbl_ChannelLegalPersonRelation', 'channel_uuid', channel_uuids)
        xqkj_query.delete_infos('Tbl_ChannelClearingAccountRelation', 'channel_uuid', channel_uuids)
        xqkj_query.delete_infos('Tbl_ChannelBusinessInformationRelation', 'channel_uuid', channel_uuids)
        xqkj_query.delete_infos('Tbl_BDInfo', 'channel_uuid', channel_uuids)

    def test_007_del_legalPerson(self):
        """
        删除平台法人代表信息
        :return:
        """
        legal_person_uuids = xqkj_query.get_tbl_infos('Tbl_LegalPerson', 'legal_person_uuid',
                                                      'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_LegalPerson', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_MerchantLegalPersonRelation', 'legal_person_uuid', legal_person_uuids)
        xqkj_query.delete_infos('Tbl_ChannelLegalPersonRelation', 'legal_person_uuid', legal_person_uuids)

    def test_008_del_clearingAccount(self):
        """
        删除平台机构结算信息
        :return:
        """
        clearing_account_uuids = xqkj_query.get_tbl_infos('Tbl_ClearingAccount', 'clearing_account_uuid',
                                                          'POSITION("{}" IN account_name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_ClearingAccount', 'POSITION("{}" IN account_name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_MerchantClearingAccountRelation', 'clearing_account_uuid', clearing_account_uuids)
        xqkj_query.delete_infos('Tbl_ChannelClearingAccountRelation', 'clearing_account_uuid', clearing_account_uuids)

    def test_009_del_businessInformation(self):
        """
        删除平台机构结算信息
        :return:
        """
        business_information_uuids = xqkj_query.get_tbl_infos('Tbl_BusinessInformation', 'business_information_uuid',
                                                              'POSITION("{}" IN email)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_BusinessInformation', 'POSITION("{}" IN email)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_ChannelBusinessInformationRelation', 'business_information_uuid',
                                business_information_uuids)
        xqkj_query.delete_infos('Tbl_MerchantBusinessInformationRelation', 'business_information_uuid',
                                business_information_uuids)

    def test_009_del_template(self):
        """
        删除进件配置信息
        :return:
        """
        product_template_uuids = xqkj_query.get_tbl_infos('Tbl_ProductParamTemplate', 'product_template_uuid',
                                                          'POSITION("{}" IN template_name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_ProductParamTemplate', 'POSITION("{}" IN template_name)'.format(loginAction.sign))

        xqkj_query.delete_infos('Tbl_ProductParamTemplateConfig', 'product_template_uuid', product_template_uuids)

    def test_010_del_contract(self):
        """
        删除订单信息
        :return:
        """
        user_uuid = loginAction.get_user_uuid()
        contract_uuids = xqkj_query.get_tbl_infos('Tbl_Contract', 'contract_uuid', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_Contract', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_infos('Tbl_ContractCustomerLabel', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_ContractImage', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_ContractInfo', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_ContractOperationLog', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_FinalCheckLog', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_FirstCheckLog', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_TelephoneCheckLog', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_QifaMachineLog', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_AuditComment', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_AuditCommentAttachment', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_AuditMonitor', 'contract_uuid', contract_uuids)

    def test_011_del_uerinfo(self):
        """
        删除客户信息
        :return:
        """
        user_uuid = loginAction.get_user_uuid()
        xqkj_query.delete_info('Tbl_UserBankCardInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserContactInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserIdCardInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserMailListInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserOcrInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserPersonalInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserPlaceOrderGps', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_UserWorkInfo', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_info('Tbl_TransLog', 'user_id="{}"'.format(user_uuid))
        # 客户主表，客户注册表，暂不删除
        # xqkj_query.delete_info('Tbl_UserProfile', 'user_uuid="{}"'.format(user_uuid))
        # xqkj_query.delete_info('Tbl_UserRegisterInfo', 'user_uuid="{}"'.format(user_uuid))

    def test_012_del_lable(self):
        """
        删除标签
        :return:
        """
        xqkj_query.delete_info('Tbl_ContractCustomerLabel', 'position("{}" in label_content)'.format(loginAction.sign))

    def test_013_del_remark(self):
        """
        删除电核备注、影响资料、风控数据源
        :return:
        """
        xqkj_query.delete_info('Tbl_ElectronuclearRemark', 'CONCAT(impact_data, wind_control_data_source, '
                                                           'customer_information) REGEXP "{}"'.format(loginAction.sign))

    def test_014_del_bd(self):
        """
        删除BD数据
        :return:
        """
        bd_info_uuids = xqkj_query.get_tbl_infos('Tbl_BDInfo', 'bd_info_uuid',
                                                 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_BDInfo', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_BDMerchantRelation', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_BDInfoLog', 'bd_info_uuid', bd_info_uuids)
        xqkj_query.delete_infos('Tbl_BDMerchantRelation', 'bd_info_uuid', bd_info_uuids)

    def test_015_del_Urge(self):
        """
        删除催收数据
        :return:
        """
        user_uuids = xqkj_query.get_tbl_infos('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                              'POSITION("{}" IN name)'.format(loginAction.sign))
        user_uuid = xqkj_query.get_info('Tbl_PlatformUserProfile', 'platform_user_profile_uuid',
                                        'email="{}"'.format(loginAction.super_email))
        app_user_uuid = loginAction.get_user_uuid()
        urge_uuids = xqkj_query.select_infos('Tbl_Urge', 'urge_uuid', 'user_uuid', user_uuids)
        urge_uuids2 = xqkj_query.select_infos('Tbl_Urge', 'urge_uuid', 'user_uuid', user_uuid)
        xqkj_query.delete_infos('Tbl_PlatformUserProfileCollection', 'platform_user_profile_uuid', user_uuids)
        xqkj_query.delete_infos('Tbl_PlatformUserProfileCollection', 'platform_user_profile_uuid', user_uuid)
        xqkj_query.delete_infos('Tbl_Urge', 'user_uuid', app_user_uuid)
        xqkj_query.delete_infos('Tbl_Urge', 'user_uuid', user_uuids)
        xqkj_query.delete_infos('Tbl_UrgeUserRelation', 'user_profile_uuid', app_user_uuid)
        xqkj_query.delete_infos('Tbl_UrgeUserRelation', 'platform_user_profile_uuid', user_uuids)
        xqkj_query.delete_infos('Tbl_UrgeUserRelation', 'platform_user_profile_uuid', user_uuid)
        xqkj_query.delete_infos('Tbl_UrgeFile', 'urge_uuid', urge_uuids)
        xqkj_query.delete_infos('Tbl_UrgeFile', 'urge_uuid', urge_uuids2)

    def test_016_del_bill(self):
        """
        客户账单逾期流水表、客户账单流水表
        :return:
        """
        user_uuid = loginAction.get_user_uuid()
        contract_uuids = xqkj_query.get_tbl_infos('Tbl_Contract', 'contract_uuid', 'user_uuid="{}"'.format(user_uuid))
        user_bill_uuids = list()
        if contract_uuids:
            user_bill_uuids = xqkj_query.select_infos(
                'Tbl_Contract', 'user_bill_uuid', 'contract_uuid', contract_uuids)
        xqkj_query.delete_info('Tbl_UserBill', 'user_uuid="{}"'.format(user_uuid))
        xqkj_query.delete_infos('Tbl_UserBill', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_UserBillOverdueStream', 'contract_uuid', contract_uuids)
        xqkj_query.delete_infos('Tbl_UserBillOverdueStream', 'user_bill_uuid', user_bill_uuids)

    def test_017_del_sa(self):
        """
        删除sa信息
        :return:
        """
        sas = xqkj_query.get_tbl_infos('Tbl_SA', 'sa_uuid', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_info('Tbl_SA', 'POSITION("{}" IN name)'.format(loginAction.sign))
        xqkj_query.delete_infos('Tbl_SA_Contract', 'sa_uuid', sas)
        xqkj_query.delete_infos('Tbl_SA_Log', 'sa_uuid', sas)