#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
import json
import reborn.test.case_loginadmin as loginadmin
from reborn.test.case_token import globaltoken

baseUrl = "http://192.168.15.129:9396"
# API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache","mytoken": "158ded9a0c4ac124a3cde0b45ddf611e"}

API_TEST_HEADERS = loginadmin.login()
print(API_TEST_HEADERS)
API_TEST_HEADERS2 = loginadmin.superadminlogin()
print(API_TEST_HEADERS2)


class BusinessAction(object):
    LOGGER = getlog(__name__)

    ###############################################################################
    #                                   机构管理                                  #
    # 模块描述：机构管理相关接口                                                  #
    ###############################################################################

    def test_api_78dk_platform_cm_base_business_saveBusinessInfor(self, businessaddress, businessaddressgpsloction,
                                                                  businessaddresszipcode, businesshoursendtime,
                                                                  businesshoursstarttime, businessinformationuuid,
                                                                  businessregistrationnumber, channelormerchantuuid,
                                                                  documentaddress, email, organizationcode,
                                                                  socialunifiedcreditcode, storerentalendtime,
                                                                  storerentalstarttime, taxregistrationnumber):
        """
        添加机构
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/business/saveBusinessInfor"
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_saveBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "businessAddressZipCode": businessaddresszipcode,
                             "businessHoursEndTime": businesshoursendtime,
                             "businessHoursStartTime": businesshoursstarttime,
                             "businessInformationUuid": businessinformationuuid,
                             "businessRegistrationNumber": businessregistrationnumber,
                             "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress,
                             "email": email, "organizationCode": organizationcode,
                             "socialUnifiedCreditCode": socialunifiedcreditcode,
                             "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime,
                             "taxRegistrationNumber": taxregistrationnumber})
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_saveBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_business_updateBusinessInfor(self, businessaddress, businessaddressgpsloction,
                                                                    businessaddresszipcode, businesshoursendtime,
                                                                    businesshoursstarttime, businessinformationuuid,
                                                                    businessregistrationnumber, channelormerchantuuid,
                                                                    documentaddress, email, organizationcode,
                                                                    socialunifiedcreditcode, storerentalendtime,
                                                                    storerentalstarttime, taxregistrationnumber):
        """
        编辑机构
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/business/updateBusinessInfor"
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_updateBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "businessAddressZipCode": businessaddresszipcode,
                             "businessHoursEndTime": businesshoursendtime,
                             "businessHoursStartTime": businesshoursstarttime,
                             "businessInformationUuid": businessinformationuuid,
                             "businessRegistrationNumber": businessregistrationnumber,
                             "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress,
                             "email": email, "organizationCode": organizationcode,
                             "socialUnifiedCreditCode": socialunifiedcreditcode,
                             "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime,
                             "taxRegistrationNumber": taxregistrationnumber})
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_updateBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_business_viewBusinessInfor(self, uid):
        """
        查询机构
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/business/viewBusinessInfor"
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_viewBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_viewBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_business_deleteBusinessInfor(self, uid):
        """
        删除机构
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/business/deleteBusinessInfor"
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_deleteBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_business_deleteBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   渠道信息                                  #
    # 模块描述：渠道相关接口                                                      #
    ###############################################################################

    def test_api_78dk_platform_cm_base_saveChannel(self, city, name, parentchanneluuid, province, region, shortname):
        """
        添加渠道
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/saveChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_saveChannel请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"city": city, "name": name, "parentChannelUuid": parentchanneluuid, "province": province, "region": region,
             "shortName": shortname})
        self.LOGGER.info("test_api_78dk_platform_cm_base_saveChannel请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_updateChannel(self, channeluuid, city, name, note, operatoruuid, province,
                                                     region, shortname):
        """
        编辑渠道
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/updateChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_updateChannel请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"channelUuid": channeluuid, "city": city, "name": name, "note": note, "operatorUuid": operatoruuid,
             "province": province, "region": region, "shortName": shortname})
        self.LOGGER.info("test_api_78dk_platform_cm_base_updateChannel请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_viewChannel(self, uid):
        """
        查询渠道
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_viewChannel请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_viewChannel请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_deleteChannel(self, uid):
        """
        删除渠道
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/deleteChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_deleteChannel请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_deleteChannel请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_state_updateFreezeState(self, uid, updatestate):
        """
        冻结渠道
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/state/updateFreezeState"
        self.LOGGER.info("test_api_78dk_platform_cm_state_updateFreezeState请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "updateState": updatestate})
        self.LOGGER.info("test_api_78dk_platform_cm_state_updateFreezeState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_state_updateOpenCloseState(self, uid, updatestate):
        """
        渠道开关
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/state/updateOpenCloseState"
        self.LOGGER.info("test_api_78dk_platform_cm_state_updateOpenCloseState请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "updateState": updatestate})
        self.LOGGER.info("test_api_78dk_platform_cm_state_updateOpenCloseState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_examine_examine(self, isadopt, message, uid):
        """
        渠道审核
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/examine/examine"
        self.LOGGER.info("test_api_78dk_platform_cm_examine_examine请求地址:【{}】".format(requesturl))
        params = json.dumps({"isAdopt": isadopt, "message": message, "uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_examine_examine请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_examine_viewExamineChannels(self, name, pagecurrent, pagesize):
        """
        渠道审核列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/examine/viewExamineChannels"
        self.LOGGER.info("test_api_78dk_platform_cm_examine_viewExamineChannels请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_cm_examine_viewExamineChannels请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_viewChannels(self, name, pagecurrent, pagesize):
        """
        渠道列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/viewChannels"
        self.LOGGER.info("test_api_78dk_platform_cm_base_viewChannels请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_cm_base_viewChannels请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_state_viewStateChannels(self, name, pagecurrent, pagesize, openCloseState,
                                                          freezeState, auditState):
        """
        渠道状态列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/state/viewStateChannels"
        self.LOGGER.info("test_api_78dk_platform_cm_state_viewStateChannels请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "openCloseState": openCloseState,
             "freezeState": freezeState, "auditState": auditState})
        self.LOGGER.info("test_api_78dk_platform_cm_state_viewStateChannels请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  渠道操作员                                  #
    # 模块描述：渠道操作员相关接口                                                #
    ###############################################################################

    def test_api_78dk_platform_cm_base_operator_saveOperator(self, channelormerchantuuid, mail, mobile, name, password,
                                                             salt, title):
        """
        添加操作员
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/saveOperator"
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_saveOperator请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"channelOrMerchantUuid": channelormerchantuuid, "mail": mail, "mobile": mobile, "name": name,
             "password": password, "salt": salt, "title": title})
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_saveOperator请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_operator_updateOperator(self, channelormerchantuuid, mail, mobile, name,
                                                               operatoruuid, password, salt, title):
        """
        编辑操作员
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/updateOperator"
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_updateOperator请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"channelOrMerchantUuid": channelormerchantuuid, "mail": mail, "mobile": mobile, "name": name,
             "operatorUuid": operatoruuid, "password": password, "salt": salt, "title": title})
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_updateOperator请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_operator_viewOperator(self, uid):
        """
        查询操作员
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/viewOperator"
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_viewOperator请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_viewOperator请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_operator_deleteOperator(self, uid):
        """
        删除操作员
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/operator/deleteOperator"
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_deleteOperator请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_operator_deleteOperator请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  渠道法人代表                                 #
    # 模块描述：渠道法人代表相关接口                                              #
    ###############################################################################

    def test_api_78dk_platform_cm_base_legal_saveLegalPerson(self, cardnumber, channelormerchantuuid, legalpersonuuid,
                                                             mobile, name):
        """
        添加法人代表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/saveLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_saveLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid,
                             "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name})
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_saveLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_legal_updateLegalPerson(self, cardnumber, channelormerchantuuid, legalpersonuuid,
                                                               mobile, name):
        """
        编辑法人代表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/updateLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_updateLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid,
                             "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name})
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_updateLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel(self, uid):
        """
        查询法人代表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/viewLegalPersonByChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_viewLegalPersonByChannel请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_legal_deleteLegalPerson(self, uid):
        """
        删除法人代表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/legal/deleteLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_deleteLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_legal_deleteLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  渠道结算信息                                 #
    # 模块描述：结算信息相关接口                                                  #
    ###############################################################################

    def test_api_78dk_platform_cm_base_clear_saveClearingAccount(self, accountname, accountnumber, accountopeningbank,
                                                                 accounttype, branchname, chamberlainidcardnumber,
                                                                 channelormerchantuuid, city, clearingaccountuuid,
                                                                 linenumber, phone, province, region):
        """
        添加渠道结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/saveClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_saveClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank,
             "accountType": accounttype, "branchName": branchname, "chamberlainIdcardNumber": chamberlainidcardnumber,
             "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid,
             "lineNumber": linenumber, "phone": phone, "province": province, "region": region})
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_saveClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_clear_updateClearingAccount(self, accountname, accountnumber, accountopeningbank,
                                                                   accounttype, branchname, chamberlainidcardnumber,
                                                                   channelormerchantuuid, city, clearingaccountuuid,
                                                                   linenumber, phone, province, region):
        """
        编辑渠道结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/updateClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_updateClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank,
             "accountType": accounttype, "branchName": branchname, "chamberlainIdcardNumber": chamberlainidcardnumber,
             "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid,
             "lineNumber": linenumber, "phone": phone, "province": province, "region": region})
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_updateClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_clear_viewClearingAccount(self, uid):
        """
        查询渠道结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/viewClearingAccountByChannel"
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_viewClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_viewClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_cm_base_clear_deleteClearingAccount(self, uid):
        """
        删除渠道结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/cm/base/clear/deleteClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_deleteClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_cm_base_clear_deleteClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   公共信息                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_common_viewRegionLists(self, paramsingle):
        """
        区/县级下拉
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/common/viewRegionLists"
        self.LOGGER.info("test_api_78dk_platform_common_viewRegionLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle})
        self.LOGGER.info("test_api_78dk_platform_common_viewRegionLists请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_common_viewCityLists(self, paramsingle):
        """
        市级下拉
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/common/viewCityLists"
        self.LOGGER.info("test_api_78dk_platform_common_viewCityLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle})
        self.LOGGER.info("test_api_78dk_platform_common_viewCityLists请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_common_viewProvinceLists(self, paramsingle):
        """
        省级下拉
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/common/viewProvinceLists"
        self.LOGGER.info("test_api_78dk_platform_common_viewProvinceLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle})
        self.LOGGER.info("test_api_78dk_platform_common_viewProvinceLists请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   商户管理                                  #
    # 模块描述：商户管理相关接口                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_base_saveMerchant(self, channeluuid, city, name, note, org, parentmerchantuuid,
                                                    province, region, shortname):
        """
        新增商户基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/saveMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_base_saveMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"channelUuid": channeluuid, "city": city, "name": name, "note": note, "org": org,
                             "parentMerchantUuid": parentmerchantuuid, "province": province, "region": region,
                             "shortName": shortname})
        self.LOGGER.info("test_api_78dk_platform_mm_base_saveMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_updateMerchant(self, channeluuid, city, merchantuuid, name, note, org,
                                                      parentmerchantuuid, province, region, shortname):
        """
        修改商户基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/updateMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_base_updateMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"channelUuid": channeluuid, "city": city, "merchantUuid": merchantuuid, "name": name, "note": note,
             "org": org, "parentMerchantUuid": parentmerchantuuid, "province": province, "region": region,
             "shortName": shortname})
        self.LOGGER.info("test_api_78dk_platform_mm_base_updateMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_viewMerchantList(self, name, pagecurrent, pagesize):
        """
        查询商户列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchantList"
        self.LOGGER.info("test_api_78dk_platform_mm_base_viewMerchantList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_mm_base_viewMerchantList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_examine_merchanrExamine(self, ispass, message, uid):
        """
        商户审核
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/examine/merchanrExamine"
        self.LOGGER.info("test_api_78dk_platform_mm_examine_merchanrExamine请求地址:【{}】".format(requesturl))
        params = json.dumps({"isPass": ispass, "message": message, "uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_examine_merchanrExamine请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_viewMerchant(self, uid):
        """
        查询基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/viewMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_base_viewMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_viewMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_examine_viewExamineMerchantList(self, name, pagecurrent, pagesize):
        """
        查询商户审核列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/examine/viewExamineMerchantList"
        self.LOGGER.info("test_api_78dk_platform_mm_examine_viewExamineMerchantList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_mm_examine_viewExamineMerchantList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_state_viewStateMerchantList(self, name, pagecurrent, pagesize):
        """
        查询商户状态列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/state/viewStateMerchantList"
        self.LOGGER.info("test_api_78dk_platform_mm_state_viewStateMerchantList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_mm_state_viewStateMerchantList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_state_updateOpenCloseState(self, uid, updatestate):
        """
        修改商户开关
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/state/updateOpenCloseState"
        self.LOGGER.info("test_api_78dk_platform_mm_state_updateOpenCloseState请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "updateState": updatestate})
        self.LOGGER.info("test_api_78dk_platform_mm_state_updateOpenCloseState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_state_updateFreezeState(self, uid, updatestate):
        """
        修改冻结状态
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/state/updateFreezeState"
        self.LOGGER.info("test_api_78dk_platform_mm_state_updateFreezeState请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "updateState": updatestate})
        self.LOGGER.info("test_api_78dk_platform_mm_state_updateFreezeState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_deleteMerchant(self, uid):
        """
        删除商户基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/deleteMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_base_deleteMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_deleteMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  商户机构信息                                 #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_base_business_saveBusinessInfor(self, businessaddress, businessaddressgpsloction,
                                                                  businessaddresszipcode, businesshoursendtime,
                                                                  businesshoursstarttime, businessinformationuuid,
                                                                  businessregistrationnumber,
                                                                  channelormerchantuuid, documentaddress, email,
                                                                  organizationcode, socialunifiedcreditcode,
                                                                  storerentalendtime, storerentalstarttime,
                                                                  taxregistrationnumber, businessProvince, BusinessCity,
                                                                  BusinessRegion, DocumentProvince, DocumentCity,
                                                                  DocumentRegion):
        """
        新增机构信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/business/saveBusinessInfor"
        self.LOGGER.info("test_api_78dk_platform_mm_base_business_saveBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "businessAddressZipCode": businessaddresszipcode,
                             "businessHoursEndTime": businesshoursendtime,
                             "businessHoursStartTime": businesshoursstarttime,
                             "businessInformationUuid": businessinformationuuid,
                             "businessRegistrationNumber": businessregistrationnumber,
                             "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress,
                             "email": email, "organizationCode": organizationcode,
                             "socialUnifiedCreditCode": socialunifiedcreditcode,
                             "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime,
                             "taxRegistrationNumber": taxregistrationnumber, "businessProvince": businessProvince,
                             "BusinessCity": BusinessCity, "BusinessRegion": BusinessRegion,
                             "DocumentProvince": DocumentProvince, "DocumentCity": DocumentCity,
                             "DocumentRegion": DocumentRegion})
        self.LOGGER.info("test_api_78dk_platform_mm_base_business_saveBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_i78dk_platform_mm_base_business_updateBusinessInfor(self, businessaddress, businessaddressgpsloction,
                                                                     businessaddresszipcode, businesshoursendtime,
                                                                     businesshoursstarttime, businessinformationuuid,
                                                                     businessregistrationnumber, channelormerchantuuid,
                                                                     documentaddress, email, organizationcode,
                                                                     socialunifiedcreditcode, storerentalendtime,
                                                                     storerentalstarttime,
                                                                     taxregistrationnumber, businessProvince,
                                                                     BusinessCity, BusinessRegion, DocumentProvince,
                                                                     DocumentCity, DocumentRegion):
        """
        修改机构信息
        POST http://test.jtlservice.78dk.com/api/78dk/platform/mm/base/business/updateBusinessInfor HTTP/1.1
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/business/updateBusinessInfor"
        self.LOGGER.info("test_api_i78dk_platform_mm_base_business_updateBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "businessAddressZipCode": businessaddresszipcode,
                             "businessHoursEndTime": businesshoursendtime,
                             "businessHoursStartTime": businesshoursstarttime,
                             "businessInformationUuid": businessinformationuuid,
                             "businessRegistrationNumber": businessregistrationnumber,
                             "channelOrMerchantUuid": channelormerchantuuid, "documentAddress": documentaddress,
                             "email": email, "organizationCode": organizationcode,
                             "socialUnifiedCreditCode": socialunifiedcreditcode,
                             "storeRentalEndTime": storerentalendtime, "storeRentalStartTime": storerentalstarttime,
                             "taxRegistrationNumber": taxregistrationnumber, "businessProvince": businessProvince,
                             "BusinessCity": BusinessCity, "BusinessRegion": BusinessRegion,
                             "DocumentProvince": DocumentProvince, "DocumentCity": DocumentCity,
                             "DocumentRegion": DocumentRegion})
        self.LOGGER.info("test_api_i78dk_platform_mm_base_business_updateBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant(self, uid):
        """
        根据商户Uuid查询机构信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/business/viewBusinessInforByMerchant"
        self.LOGGER.info(
            "test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_business_viewBusinessInforByMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_i78dk_platform_mm_base_business_deleteBusinessInfor(self, uid):
        """
        删除机构信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/business/deleteBusinessInfor"
        self.LOGGER.info("test_api_i78dk_platform_mm_base_business_deleteBusinessInfor请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_i78dk_platform_mm_base_business_deleteBusinessInfor请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  商户法人信息                                 #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_base_legal_saveLegalPerson(self, cardnumber, channelormerchantuuid, legalpersonuuid,
                                                             mobile, name):
        """
        新增商户法人信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/saveLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_saveLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid,
                             "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name})
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_saveLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_legal_updateLegalPerson(self, cardnumber, channelormerchantuuid, legalpersonuuid,
                                                               mobile, name):
        """
        修改商户法人信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/updateLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_updateLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"cardNumber": cardnumber, "channelOrMerchantUuid": channelormerchantuuid,
                             "legalPersonUuid": legalpersonuuid, "mobile": mobile, "name": name})
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_updateLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant(self, uid):
        """
        根据商户Uuid查询法人信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/viewLegalPersonByMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_viewLegalPersonByMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_legal_deleteLegalPerson(self, uid):
        """
        删除商户法人信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/legal/deleteLegalPerson"
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_deleteLegalPerson请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_legal_deleteLegalPerson请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  商户结算信息                                 #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_base_clear_saveClearingAccount(self, accountname, accountnumber, accountopeningbank,
                                                                 accounttype, branchname, chamberlainidcardnumber,
                                                                 channelormerchantuuid, city, clearingaccountuuid,
                                                                 linenumber, phone, province, region):
        """
        新增商户结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/saveClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_saveClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank,
             "accountType": accounttype, "branchName": branchname, "chamberlainIdcardNumber": chamberlainidcardnumber,
             "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid,
             "lineNumber": linenumber, "phone": phone, "province": province, "region": region})
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_saveClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_clear_updateClearingAccount(self, accountname, accountnumber, accountopeningbank,
                                                                   accounttype, branchname, chamberlainidcardnumber,
                                                                   channelormerchantuuid, city, clearingaccountuuid,
                                                                   linenumber, phone, province, region):
        """
        修改商户结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/updateClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_updateClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"accountName": accountname, "accountNumber": accountnumber, "accountOpeningBank": accountopeningbank,
             "accountType": accounttype, "branchName": branchname, "chamberlainIdcardNumber": chamberlainidcardnumber,
             "channelOrMerchantUuid": channelormerchantuuid, "city": city, "clearingAccountUuid": clearingaccountuuid,
             "lineNumber": linenumber, "phone": phone, "province": province, "region": region})
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_updateClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant(self, uid):
        """
        根据商户Uuid查询结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/viewClearingAccountByMerchant"
        self.LOGGER.info(
            "test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_viewClearingAccountByMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_clear_deleteClearingAccount(self, uid):
        """
        删除商户结算信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/clear/deleteClearingAccount"
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_deleteClearingAccount请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_clear_deleteClearingAccount请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  商户门店管理                                 #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_base_store_saveStore(self, businessaddress, businessaddressgpsloction, managername,
                                                       managerphone, merchantuuid,
                                                       stormuuid, Province, City, region, storeName):
        """
        新增商户门店信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/store/saveStore"
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_saveStore请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "managerName": managername,
                             "managerPhone": managerphone, "merchantUuid": merchantuuid, "stormUuid": stormuuid,
                             "Province": Province, "City": City, "region": region, "storeName": storeName})
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_saveStore请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_store_updateStore(self, businessaddress, businessaddressgpsloction, managername,
                                                         managerphone, merchantuuid, stormuuid, Province, City, region,
                                                         storeName):
        """
        修改商户门店信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/store/updateStore"
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_updateStore请求地址:【{}】".format(requesturl))
        params = json.dumps({"businessAddress": businessaddress, "businessAddressGpsLoction": businessaddressgpsloction,
                             "managerName": managername, "managerPhone": managerphone, "merchantUuid": merchantuuid,
                             "stormUuid": stormuuid, "Province": Province, "City": City, "region": region,
                             "storeName": storeName})
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_updateStore请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_store_viewStore(self, uid):
        """
        查询商户门店信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStore"
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_viewStore请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_viewStore请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_store_viewStoreList(self, name, pagecurrent, pagesize):
        """
        查询商户门店列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/store/viewStoreList"
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_viewStoreList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_viewStoreList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_base_store_deleteStore(self, uid):
        """
        删除商户门店信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/base/store/deleteStore"
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_deleteStore请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_base_store_deleteStore请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  商户额度管理                                 #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_money_saveMerchantMoney(self, amountday, amountmonth, amountsingle, amountsum,
                                                          merchantuuid, moneyconfiguuid, zoomcoefficient):
        """
        新增额度管理
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/saveMerchantMoney"
        self.LOGGER.info("test_api_78dk_platform_mm_money_saveMerchantMoney请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum,
             "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient})
        self.LOGGER.info("test_api_78dk_platform_mm_money_saveMerchantMoney请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_money_updateMerchantMoney(self, amountday, amountmonth, amountsingle, amountsum,
                                                            merchantuuid, moneyconfiguuid, zoomcoefficient):
        """
        修改额度管理
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/updateMerchantMoney"
        self.LOGGER.info("test_api_78dk_platform_mm_money_updateMerchantMoney请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"amountDay": amountday, "amountMonth": amountmonth, "amountSingle": amountsingle, "amountSum": amountsum,
             "merchantUuid": merchantuuid, "moneyConfigUuid": moneyconfiguuid, "zoomCoefficient": zoomcoefficient})
        self.LOGGER.info("test_api_78dk_platform_mm_money_updateMerchantMoney请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant(self, uid):
        """
        根据商户Uuid查询额度管理
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyByMerchant"
        self.LOGGER.info("test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_money_viewMerchantMoneyByMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_money_deleteMerchantMoney(self, uid):
        """
        删除额度管理
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/deleteMerchantMoney"
        self.LOGGER.info("test_api_78dk_platform_mm_money_deleteMerchantMoney请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_mm_money_deleteMerchantMoney请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_money_viewMerchantMoneyList(self, name, pagecurrent, pagesize):
        """
        风险控制列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/viewMerchantMoneyList"
        self.LOGGER.info("test_api_78dk_platform_mm_money_viewMerchantMoneyList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_mm_money_viewMerchantMoneyList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_mm_saveContractImages(self, merchantuuid, ):
        """
        影像资料保存
        依赖函数：test_{'msg': '', 'data': '', 'code': ''}
        依赖参数：
        :return: response.text
        """
        par = [
            {"key": "SHYYZZ", "merchantUuid": merchantuuid, "url": "327f/325969327f31529f4f4cccc762ebfac92c408d.png"},
            {"key": "SHFRSFZZ", "merchantUuid": merchantuuid, "url": "e230/380165e2302f4a7e8f267a11258ab8bac3897d.png"},
            {"key": "SHFRSFZF", "merchantUuid": merchantuuid, "url": "4c48/4583604c48acec7057dda85391b5dd60c5ab04.png"},
            {"key": "SHFRSFZFSC", "merchantUuid": merchantuuid,
             "url": "7a75/5021527a75821c5a09e18c7021875347672e4c.png"}]
        requesturl = baseUrl + "/api/78dk/platform/mm/saveContractImages"
        self.LOGGER.info("test_api_78dk_platform_mm_saveContractImages请求地址:【{}】".format(requesturl))
        params = json.dumps(par)
        self.LOGGER.info("test_api_78dk_platform_mm_saveContractImages请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                               商户预授信放大系数管理                               #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_mm_money_merchantMoneyEnlarge(self, uid, zoomcoefficient):
        """
        修改预授信放大系数
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/mm/money/merchantMoneyEnlarge"
        self.LOGGER.info("test_api_78dk_platform_mm_money_merchantMoneyEnlarge请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "zoomCoefficient": zoomcoefficient})
        self.LOGGER.info("test_api_78dk_platform_mm_money_merchantMoneyEnlarge请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   系统管理                                  #
    # 模块描述：系统相关接口                                                      #
    ###############################################################################

    def test_api_78dk_platform_sys_user_saveSystemUser(self, email, mobile, name):
        """
        新增用户
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/saveSystemUser"
        self.LOGGER.info("test_api_78dk_platform_sys_user_saveSystemUser请求地址:【{}】".format(requesturl))
        params = json.dumps({"email": email, "mobile": mobile, "name": name})
        self.LOGGER.info("test_api_78dk_platform_sys_user_saveSystemUser请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_updateSystemUser(self, email, mobile, name, platformuserprofileuuid):
        """
        修改用户
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUser"
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateSystemUser请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"email": email, "mobile": mobile, "name": name, "platformUserProfileUuid": platformuserprofileuuid})
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateSystemUser请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_viewSystemUser(self, uid):
        """
        查询用户
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUser"
        self.LOGGER.info("test_api_78dk_platform_sys_user_viewSystemUser请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": uid})
        self.LOGGER.info("test_api_78dk_platform_sys_user_viewSystemUser请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_updateUserPass(self, email, password, passwordrepeat, uid):
        """
        修改密码
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/updateUserPass"
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateUserPass请求地址:【{}】".format(requesturl))
        params = json.dumps({"email": email, "password": password, "passwordRepeat": passwordrepeat, "uid": uid})
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateUserPass请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_viewSystemUserList(self, name, pagecurrent, pagesize):
        """
        查询用户列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/viewSystemUserList"
        self.LOGGER.info("test_api_78dk_platform_sys_user_viewSystemUserList请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_sys_user_viewSystemUserList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_updateSystemUserState(self, uid, updatestate):
        """
        状态修改
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/updateSystemUserState"
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateSystemUserState请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, "updateState": updatestate})
        self.LOGGER.info("test_api_78dk_platform_sys_user_updateSystemUserState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_login(self, email, password):
        """
        用户登录
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/login"
        self.LOGGER.info("test_api_78dk_platform_sys_user_login请求地址:【{}】".format(requesturl))
        params = json.dumps({"email": email, "password": password})
        self.LOGGER.info("test_api_78dk_platform_sys_user_login请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_resetUserPass(self, uid):
        """
        重置密码
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/resetUserPass"
        self.LOGGER.info("test_api_78dk_platform_sys_user_resetUserPass请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_sys_user_resetUserPass请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_user_deleteSystemUser(self, uid):
        """
        删除用户
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/user/deleteSystemUser"
        self.LOGGER.info("test_api_78dk_platform_sys_user_deleteSystemUser请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_sys_user_deleteSystemUser请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   权限管理                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_sys_privilege_saveUserPrivilege(self, platformprivilegeuuid, platformuseruuid):
        """
        新增/修改权限
        # [{"platformPrivilegeUuid":"5db0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"},---产品管理
        # {"platformPrivilegeUuid":"15b0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"},---产品列表
        # {"platformPrivilegeUuid":"67b0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"}]---产品分配
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveUserPrivilege请求地址:【{}】".format(requesturl))
        params = json.dumps([{"platformPrivilegeUuid": platformprivilegeuuid, "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "5db0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "15b0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "685424dff6b24278a77281f2367be331",
                              "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "67b0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid}])
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveUserPrivilege请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_saveUserPrivilegesuperadmin(self, platformprivilegeuuid, platformuseruuid):
        """
        使用超级管理员token，分配权限给新用户
        # [{"platformPrivilegeUuid":"5db0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"},---产品管理
        # {"platformPrivilegeUuid":"15b0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"},---产品列表
        # {"platformPrivilegeUuid":"67b0d9fb5d524a098810855385fb042e","platformUserUuid":"879995afdbc0435e966a0a4eaa5b378c"}]---产品分配
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveUserPrivilege"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveUserPrivilege请求地址:【{}】".format(requesturl))
        params = json.dumps([{"platformPrivilegeUuid": platformprivilegeuuid, "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "5db0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "15b0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid},
                             {"platformPrivilegeUuid": "685424dff6b24278a77281f2367be331",
                              "platformUserUuid": platformuseruuid},
                             # 决策中心
                             {"platformPrivilegeUuid": "67b0d9fb5d524a098810855385fb042e",
                              "platformUserUuid": platformuseruuid}])
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveUserPrivilege请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS2, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_viewUserPrivilegeList(self, paramsingle):
        """
        查询权限
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewUserPrivilegeList"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_viewUserPrivilegeList请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle})
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_viewUserPrivilegeList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_clearUserPrivilege(self, uid):
        """
        清除用户权限
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/clearUserPrivilege"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_clearUserPrivilege请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_clearUserPrivilege请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                 1.6.1.1新增权限                                #
    # 模块描述：                                                                  #
    ###############################################################################
    def test_FileUploadController_handlerFileUpload(self):
        """
        图片上传
        依赖函数：test_{'data': '图片URL数组，数组里面的返回上传文件的URL', 'msg': '返回信息（code为1000时，无msg）', 'code': '响应代码（1000正确，4000参数错误，5000服务器错误）'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/FileUploadController/handlerFileUpload"
        self.LOGGER.info("test_FileUploadController_handlerFileUpload请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_FileUploadController_handlerFileUpload请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_images_ba45_ba45c8f60456a672e003a875e469d0ebjpg(self):
        """
        图片访问接口
        :return: response.text
        """
        requesturl = baseUrl + "/images/ba45/ba45c8f60456a672e003a875e469d0eb.jpg"
        self.LOGGER.info("test_images_ba45_ba45c8f60456a672e003a875e469d0eb.jpg请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_images_ba45_ba45c8f60456a672e003a875e469d0eb.jpg请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_deleteMenu(self, uid, ):
        """
        删除一个菜单
        依赖函数：test_{'data': '返回数据', 'msg': '返回消息文本', 'code': '返回码'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/deleteMenu"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_deleteMenu请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_deleteMenu请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_saveMenu(self, name, platformprivilegeuuid, url, ):
        """
        保存一个菜单
        依赖函数：test_{'data': "{'platformPrivilegeUuid': '菜单uuid', 'permissionTypeName': '权限类型', 'permissionType': '权限类型', 'url': '菜单url', 'name': '菜单名称'}", 'msg': '返回消息文本', 'code': '返回码'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/saveMenu"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveMenu请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "platformPrivilegeUuid": platformprivilegeuuid, "url": url, })
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_saveMenu请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_sys_privilege_viewMenus(self, paramsingle, ):
        """
        查询所有菜单
        依赖函数：test_{'data': "{'permissionTypeName': '菜单类型', 'state': '', 'name': '菜单名称', 'created': '创建时间', 'permissionType': '菜单类型', 'platformPrivilegeUuid': '菜单uuid', 'updated': '', 'url': '菜单路径'}", 'msg': '返回消息文本', 'code': '返回码'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/sys/privilege/viewMenus"
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_viewMenus请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle, })
        self.LOGGER.info("test_api_78dk_platform_sys_privilege_viewMenus请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   资方功能                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_fund_fundSide_saveFundSide(self, name, state):
        """
        添加资方
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/saveFundSide"
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_saveFundSide请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "state": state})
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_saveFundSide请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundSide_updateFundSide(self, fundsideuuid, name, state):
        """
        编辑资方
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/updateFundSide"
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_updateFundSide请求地址:【{}】".format(requesturl))
        params = json.dumps({"fundSideUuid": fundsideuuid, "name": name, "state": state})
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_updateFundSide请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundSide_viewFundSide(self, uid):
        """
        查询加资方
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSide"
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_viewFundSide请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_viewFundSide请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundSide_viewFundSides(self, name, pagecurrent, pagesize, state):
        """
        资方列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/viewFundSides"
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_viewFundSides请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state})
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_viewFundSides请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundSide_deleteFundSide(self, uid):
        """
        删除资方
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundSide/deleteFundSide"
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_deleteFundSide请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_fund_fundSide_deleteFundSide请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                  资金包管理                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_fund_fundPackage_saveFundPackage(self, amount, contracttemplate, fundsideuuid, name,
                                                                state):
        """
        添加资金包
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/saveFundPackage"
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_saveFundPackage请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"amount": amount, "contractTemplate": contracttemplate, "fundSideUuid": fundsideuuid, "name": name,
             "state": state})
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_saveFundPackage请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundPackage_updateFundPackage(self, amount, contracttemplate, fundpackageuuid,
                                                                  fundsideuuid, name, state):
        """
        编辑资金包
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/updateFundPackage"
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_updateFundPackage请求地址:【{}】".format(requesturl))
        params = json.dumps({"amount": amount, "contractTemplate": contracttemplate, "fundPackageUuid": fundpackageuuid,
                             "fundSideUuid": fundsideuuid, "name": name, "state": state})
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_updateFundPackage请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundPackage_viewFundPackage(self, uid):
        """
        查询资金包
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackage"
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_viewFundPackage请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_viewFundPackage请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundPackage_viewFundPackages(self, name, pagecurrent, pagesize):
        """
        资金包列表查询
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/viewFundPackages"
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_viewFundPackages请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_viewFundPackages请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_fund_fundPackage_deleteFundPackage(self, uid):
        """
        删除资金包
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/fund/fundPackage/deleteFundPackage"
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_deleteFundPackage请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_fund_fundPackage_deleteFundPackage请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   产品管理                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_product_base_saveProduct(self, discountrate, earlyrepaymentfreecycle,
                                                        earlyrepaymenthandlingfee, earlyrepaymentsupport,
                                                        firsthalfofthemonth, fundpackageuuid, maxquota, minquota, name,
                                                        overduegraceperiod, overduehandlingfeerate,
                                                        overdueprincipalrate, productconfigs, productstate, remark,
                                                        repaymentdatetype, repaymentmethod, secondhalfofthemonth,
                                                        state):
        """
        添加产品模板
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/saveProduct"
        self.LOGGER.info("test_api_78dk_platform_product_base_saveProduct请求地址:【{}】".format(requesturl))
        params = json.dumps({"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle,
                             "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee,
                             "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth,
                             "fundPackageUuid": fundpackageuuid, "maxQuota": maxquota, "minQuota": minquota,
                             "name": name, "overdueGracePeriod": overduegraceperiod,
                             "overdueHandlingFeeRate": overduehandlingfeerate,
                             "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs,
                             "productState": productstate, "remark": remark, "repaymentDateType": repaymentdatetype,
                             "repaymentMethod": repaymentmethod, "secondHalfOfTheMonth": secondhalfofthemonth,
                             "state": state})
        self.LOGGER.info("test_api_78dk_platform_product_base_saveProduct请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_updateProduct(self, discountrate, earlyrepaymentfreecycle,
                                                          earlyrepaymenthandlingfee, earlyrepaymentsupport,
                                                          firsthalfofthemonth, fundpackageuuid, maxquota, minquota,
                                                          name, overduegraceperiod, overduehandlingfeerate,
                                                          overdueprincipalrate, productconfigs, productdetailuuid,
                                                          productstate, remark, repaymentdatetype, repaymentmethod,
                                                          secondhalfofthemonth, state):
        """
        编辑产品模板
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/updateProduct"
        self.LOGGER.info("test_api_78dk_platform_product_base_updateProduct请求地址:【{}】".format(requesturl))
        params = json.dumps({"discountRate": discountrate, "earlyRepaymentFreeCycle": earlyrepaymentfreecycle,
                             "earlyRepaymentHandlingFee": earlyrepaymenthandlingfee,
                             "earlyRepaymentSupport": earlyrepaymentsupport, "firstHalfOfTheMonth": firsthalfofthemonth,
                             "fundPackageUuid": fundpackageuuid, "maxQuota": maxquota, "minQuota": minquota,
                             "name": name, "overdueGracePeriod": overduegraceperiod,
                             "overdueHandlingFeeRate": overduehandlingfeerate,
                             "overduePrincipalRate": overdueprincipalrate, "productConfigs": productconfigs,
                             "productDetailUuid": productdetailuuid, "productState": productstate, "remark": remark,
                             "repaymentDateType": repaymentdatetype, "repaymentMethod": repaymentmethod,
                             "secondHalfOfTheMonth": secondhalfofthemonth, "state": state})
        self.LOGGER.info("test_api_78dk_platform_product_base_updateProduct请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_viewProductDetail(self, uid):
        """
        查询产品模板
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetail"
        self.LOGGER.info("test_api_78dk_platform_product_base_viewProductDetail请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_product_base_viewProductDetail请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_deleteProduct(self, uid):
        """
        删除产品模板
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/deleteProduct"
        self.LOGGER.info("test_api_78dk_platform_product_base_deleteProduct请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid})
        self.LOGGER.info("test_api_78dk_platform_product_base_deleteProduct请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_updateProductState(self, productstate, uuid):
        """
        修改产品状态
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/updateProductState"
        self.LOGGER.info("test_api_78dk_platform_product_base_updateProductState请求地址:【{}】".format(requesturl))
        params = json.dumps({"productState": productstate, "uuid": uuid})
        self.LOGGER.info("test_api_78dk_platform_product_base_updateProductState请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_viewProductDetails(self, name, pagecurrent, pagesize):
        """
        产品列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/viewProductDetails"
        self.LOGGER.info("test_api_78dk_platform_product_base_viewProductDetails请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_product_base_viewProductDetails请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_base_viewFundPackages(self, name, pagecurrent, pagesize, state):
        """
        资金包列表查询
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/base/viewFundPackages"
        self.LOGGER.info("test_api_78dk_platform_product_base_viewFundPackages请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state})
        self.LOGGER.info("test_api_78dk_platform_product_base_viewFundPackages请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   产品分配                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_product_pmm_saveMerchantTX(self, discountrate, merchantuuid, period,
                                                          productdetailconfiguuid, rate, discountrate2, merchantuuid2,
                                                          period2, productdetailconfiguuid2, rate2):
        """
        保存商户贴息   POST http://test.jtlservice.78dk.com/api/78dk/platform/product/pmm/saveMerchantTX HTTP/1.1
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/saveMerchantTX"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_saveMerchantTX请求地址:【{}】".format(requesturl))
        params = json.dumps([{"discountRate": discountrate, "merchantUuid": merchantuuid, "period": period,
                              "productDetailConfigUuid": productdetailconfiguuid, "rate": rate},
                             {"discountRate": discountrate2, "merchantUuid": merchantuuid2, "period": period2,
                              "productDetailConfigUuid": productdetailconfiguuid2, "rate": rate2}])
        self.LOGGER.info("test_api_78dk_platform_product_pmm_saveMerchantTX请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_viewProductDetails(self, name, pagecurrent, pagesize):
        """
        查看产品信息列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewProductDetails"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewProductDetails请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewProductDetails请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_findMerchantTX(self, merchantuid, productuid):
        """
        查询商户贴息  POST http://test.jtlservice.78dk.com/api/78dk/platform/product/pmm/findMerchantTX HTTP/1.1
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/findMerchantTX"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_findMerchantTX请求地址:【{}】".format(requesturl))
        params = json.dumps({"merchantUuid": merchantuid, "productUuid": productuid})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_findMerchantTX请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid(self, name, pagecurrent, pagesize, uuid):
        """
        根据产品id查询不相关的商户列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewNotInMerchantsByPuid"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewNotInMerchantsByPuid请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_viewInMerchantsByPuid(self, name, pagecurrent, pagesize, uuid):
        """
        根据产品id查询相关的商户列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/viewInMerchantsByPuid"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewInMerchantsByPuid请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "uuid": uuid})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_viewInMerchantsByPuid请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_bindProductMerchant(self, merchantuuids, productuuid):
        """
        绑定产品和商户关系
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/bindProductMerchant"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_bindProductMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"merchantUuids": merchantuuids, "productUuid": productuuid})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_bindProductMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_product_pmm_unBindProductMerchant(self, merchantuids, productuid):
        """
        解绑产品和商户关系
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/product/pmm/unBindProductMerchant"
        self.LOGGER.info("test_api_78dk_platform_product_pmm_unBindProductMerchant请求地址:【{}】".format(requesturl))
        params = json.dumps({"merchantUuids": merchantuids, "productUuid": productuid})
        self.LOGGER.info("test_api_78dk_platform_product_pmm_unBindProductMerchant请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    ###############################################################################
    #                                   信审管理                                  #
    # 模块描述：                                                                  #
    ###############################################################################

    def test_api_78dk_platform_tm_first_firstCheck(self, isadopt, message, uuid, ):
        """
        初审
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/firstCheck"
        self.LOGGER.info("test_api_78dk_platform_tm_first_firstCheck请求地址:【{}】".format(requesturl))
        params = json.dumps({"isAdopt": isadopt, "message": message, "uuid": uuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_firstCheck请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewFirstCheckContract(self, uid, ):
        """
        初审信息查询
        依赖函数：test_{'data': "{'loanAmount': '贷款金额', 'earlyRepaymentSupport': '是否支持提前还款', 'periodRate': '分期手续费率', 'finalCheckAuditName': '终审人', 'person': '个人基本资料', 'telephoneChecks': '电审', 'loanState': '同放款状态', 'overdueHandlingFeeRate': '逾期手续费率 - 手续费', 'contractNumber': '合同编号', 'created': '创建时间', 'contractUuid': '合同 UUID', 'qifaMachineAuditName': '启发机审核状态', 'fundSideName': '资方名称', 'loanStateName': '同放款状态', 'score': '启发风控分数', 'qifaMachineLogs': '启发机审', 'alipayAuditLogs': '支付宝审核', 'earlyRepaymentHandlingFee': '提前还款手续费率', 'baiduLogUuid': '百度风控报告UUID', 'repaymentDate': '还款日', 'telephoneCheck': '电审状态', 'firstCheckDateTime': '初审时间(时间戳)', 'tencentLogUuid': '腾讯风控报告UUID', 'fddUrl': '法大大合同路径', 'gracePeriod': '宽限期', 'riskWarning': '启发风险提示', 'storeName': '门店地址', 'aliscore': '支付宝评测额度', 'aliOpinion': '网商审核意见', 'parentMerchantName': '关联商户', 'finalCheckName': '终审状态', 'loanLog': '放款日志', 'firstCheckAuditName': '初审人', 'firstChecks': '初审日志', 'contractState': '合同状态', 'earlyRepaymentFreeCycle': '前还款-免收周期（天）', 'telephoneCheckDateTime': '电审时间(时间戳)', 'fundPackageName': '资金包名称', 'telephoneCheckAuditName': '电核人', 'discountRate': '商户贴息费率', 'alipayAuditName': '网商审核结果', 'tongdunReportId': '同盾id', 'submitStateName': '合同提交状态', 'finalChecks': '终审日志', 'signingDate': '用户签订日期（即申请日期', 'submitState': '合同提交状态', 'contractStateName': '合同状态', 'contractImages': '影像资料', 'overduePrincipalRate': '逾期手续费率 - 本金', 'stateName': '状态', 'productName': '产品名称', 'firstCheckName': '初审状态', 'loanPeriods': '期数', 'repaymentMethod': '还款方式 - 目前只支持等本等费即可', 'finalCheckDateTime': '终审时间(时间戳)', 'telephoneCheckName': '电审状态', 'merchantName': '商户名称'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContract"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewFirstCheckContract请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewFirstCheckContract请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewFirstCheckContracts(self, name, pagecurrent, pagesize, state, ):
        """
        初审列表查询
        依赖函数：test_{'data': "{'pageSize': '单页记录数', 'totalCount': '总记录数', 'dataList': '列表', 'totalPage': '总页数', 'currentPage': '当前页码'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewFirstCheckContracts"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewFirstCheckContracts请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewFirstCheckContracts请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewTongdunInfo(self, uid, ):
        """
        同盾信息查询
        依赖函数：test_{'data': '数据', 'code': '返回编号', 'msg': '返回信息'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTongdunInfo"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewTongdunInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewTongdunInfo请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_telephone_telephoneCheck(self, isadopt, message, uuid, ):
        """
        电核
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/telephone/telephoneCheck"
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_telephoneCheck请求地址:【{}】".format(requesturl))
        params = json.dumps({"isAdopt": isadopt, "message": message, "uuid": uuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_telephoneCheck请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract(self, uid, ):
        """
        电核信息查询
        依赖函数：test_{'data': "{'decorationInputAddress': '装修地址- 手输地址', 'loanAmount': '贷款金额', 'decorationCityName': '装修地址-市', 'earlyRepaymentSupport': '是否支持提前还款', 'periodRate': '分期手续费率', 'finalCheckAuditName': '终审人', 'person': '个人基本资料', 'telephoneChecks': '电审', 'loanState': '同放款状态', 'overdueHandlingFeeRate': '逾期手续费率 - 手续费', 'contractNumber': '合同编号', 'created': '创建时间', 'contractUuid': '合同 UUID', 'qifaMachineAuditName': '启发机审核状态', 'fundSideName': '资方名称', 'tencentLogUuid': '腾讯风控报告UUID', 'loanStateName': '同放款状态', 'score': '启发风控分数', 'qifaMachineLogs': '启发机审', 'alipayAuditLogs': '支付宝审核', 'earlyRepaymentHandlingFee': '提前还款手续费率', 'updated': '修改时间', 'baiduLogUuid': '百度风控报告UUID', 'repaymentDate': '还款日', 'decorationDistrictId': '装修地址- 区（县）id', 'fddUrl': '法大大合同路径', 'gracePeriod': '宽限期', 'riskWarning': '启发风险提示', 'storeName': '门店地址', 'aliscore': '支付宝评测额度', 'aliOpinion': '网商审核意见', 'parentMerchantName': '关联商户', 'finalCheckName': '终审状态', 'firstCheckAuditName': '初审人', 'firstChecks': '初审日志', 'contractState': '合同状态', 'earlyRepaymentFreeCycle': '前还款-免收周期（天）', 'fundPackageName': '资金包名称', 'telephoneCheckAuditName': '电核人', 'discountRate': '商户贴息费率', 'alipayAuditName': '网商审核结果', 'tongdunReportId': '同盾id', 'submitStateName': '合同提交状态', 'decorationDistrictName': '装修地址- 区（县）', 'decorationCityId': '装修地址-市 id', 'finalChecks': '终审日志', 'signingDate': '用户签订日期（即申请日期', 'submitState': '合同提交状态', 'contractStateName': '合同状态', 'contractImages': '影像资料', 'decorationProvinceName': '装修地址-省', 'overduePrincipalRate': '逾期手续费率 - 本金', 'stateName': '状态', 'productName': '产品名称', 'firstCheckName': '初审状态', 'loanPeriods': '期数', 'repaymentMethod': '还款方式 - 目前只支持等本等费即可', 'telephoneCheckName': '电审状态', 'decorationProvinceId': '装修地址-省 id', 'merchantName': '商户名称'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContract"
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_viewTelephoneCheckContract请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts(self, name, pagecurrent, pagesize, state, ):
        """
        电核列表查询
        依赖函数：test_{'data': "{'pageSize': '单页记录数', 'totalCount': '总记录数', 'dataList': '列表', 'totalPage': '总页数', 'currentPage': '当前页码'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckContracts"
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state, })
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_viewTelephoneCheckContracts请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_final_viewFDDInfo(self, uid, ):
        """
        法大大信息查询
        依赖函数：test_{'data': '返回法大大url', 'code': '返回编号', 'msg': '返回信息'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFDDInfo"
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFDDInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFDDInfo请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_final_finalCheck(self, isadopt, message, uuid, ):
        """
        终审
        依赖函数：test_{'data': '返回数据', 'code': '返回信息', 'msg': '返回信息'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/final/finalCheck"
        self.LOGGER.info("test_api_78dk_platform_tm_final_finalCheck请求地址:【{}】".format(requesturl))
        params = json.dumps({"isAdopt": isadopt, "message": message, "uuid": uuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_final_finalCheck请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_final_viewFinalCheckContract(self, uid, ):
        """
        终审信息查询
        依赖函数：test_{'data': "{'decorationInputAddress': '装修地址- 手输地址', 'loanAmount': '贷款金额', 'decorationCityName': '装修地址-市', 'earlyRepaymentSupport': '是否支持提前还款', 'periodRate': '分期手续费率', 'finalCheckAuditName': '终审人', 'person': '个人基本资料', 'telephoneChecks': '电审', 'loanState': '同放款状态', 'overdueHandlingFeeRate': '逾期手续费率 - 手续费', 'contractNumber': '合同编号', 'created': '创建时间', 'contractUuid': '合同 UUID', 'qifaMachineAuditName': '启发机审核状态', 'fundSideName': '资方名称', 'tencentLogUuid': '腾讯风控报告UUID', 'loanStateName': '同放款状态', 'score': '启发风控分数', 'qifaMachineLogs': '启发机审', 'alipayAuditLogs': '支付宝审核', 'earlyRepaymentHandlingFee': '提前还款手续费率', 'updated': '修改时间', 'baiduLogUuid': '百度风控报告UUID', 'repaymentDate': '还款日', 'telephoneCheck': '电审状态', 'decorationDistrictId': '装修地址- 区（县）id', 'fddUrl': '法大大合同路径', 'gracePeriod': '宽限期', 'riskWarning': '启发风险提示', 'storeName': '门店地址', 'aliscore': '支付宝评测额度', 'aliOpinion': '网商审核意见', 'parentMerchantName': '关联商户', 'finalCheckName': '终审状态', 'firstCheck': '初审状态', 'firstCheckAuditName': '初审人', 'firstChecks': '初审日志', 'contractState': '合同状态', 'earlyRepaymentFreeCycle': '前还款-免收周期（天）', 'fundPackageName': '资金包名称', 'telephoneCheckAuditName': '电核人', 'discountRate': '商户贴息费率', 'alipayAuditName': '网商审核结果', 'submitStateName': '合同提交状态', 'decorationDistrictName': '装修地址- 区（县）', 'decorationCityId': '装修地址-市 id', 'finalChecks': '终审日志', 'signingDate': '用户签订日期（即申请日期', 'submitState': '合同提交状态', 'contractStateName': '合同状态', 'contractImages': '影像资料', 'decorationProvinceName': '装修地址-省', 'overduePrincipalRate': '逾期手续费率 - 本金', 'stateName': '状态', 'productName': '产品名称', 'firstCheckName': '初审状态', 'loanPeriods': '期数', 'repaymentMethod': '还款方式 - 目前只支持等本等费即可', 'telephoneCheckName': '电审状态', 'decorationProvinceId': '装修地址-省 id', 'merchantName': '商户名称'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContract"
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFinalCheckContract请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFinalCheckContract请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_final_viewFinalCheckContracts(self, name, pagecurrent, pagesize, state, ):
        """
        终审列表查询
        依赖函数：test_{'data': "{'pageSize': '单页记录数', 'totalCount': '总记录数', 'dataList': '列表', 'totalPage': '总页数', 'currentPage': '当前页码'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/final/viewFinalCheckContracts"
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFinalCheckContracts请求地址:【{}】".format(requesturl))
        params = json.dumps({"name": name, "pageCurrent": pagecurrent, "pageSize": pagesize, "state": state, })
        self.LOGGER.info("test_api_78dk_platform_tm_final_viewFinalCheckContracts请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewImageDataConfig(self):
        """
        查询影像列表
        依赖函数：test_{'data': "{'multiple': '是否多选', 'created': '创建时间', 'key': '图片标识', 'type': '影像资料配置类型', 'state': '数据状态', 'updated': '更新时间', 'sort': '排序参数', 'name': '图片名称'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewImageDataConfig"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewImageDataConfig请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewImageDataConfig请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_selectCanAuditCheck(self, checktype, uid, ):
        """
        是否有权限审核
        依赖函数：test_{'data': '返回数据', 'code': '返回编码', 'msg': '返回信息'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/selectCanAuditCheck"
        self.LOGGER.info("test_api_78dk_platform_tm_first_selectCanAuditCheck请求地址:【{}】".format(requesturl))
        params = json.dumps({"checkType": checktype, "uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_selectCanAuditCheck请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid(self, uid, ):
        """
        查询合同已经填写的电核问题列表
        依赖函数：test_{'data': "{'refInfo': '参考信息', 'replyTypeName': '回答是否正确', 'groupSort': '分组排序', 'questionSort': '问题排序', 'answer': '答案', 'updated': '最后一次修改时间', 'riskType': '风险类型', 'stateName': '数据状态', 'telephoneCheckFeedbackUuid': '电核uuid', 'riskTypeName': '风险类型', 'created': '创建时间', 'contractUuid': '合同UUID', 'groupName': '分组名', 'state': '数据状态', 'replyType': '回答是否正确', 'question': '问题'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/telephone/viewTelephoneCheckInfosByContractUuid"
        self.LOGGER.info(
            "test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info(
            "test_api_78dk_platform_tm_telephone_viewTelephoneCheckInfosByContractUuid请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewBaiDuInfo(self, uid, ):
        """
        查询百度接口
        依赖函数：test_{'data': "{'reportInfo': '报告信息', 'created': '创建时间', 'updated': '更新时间'}", 'code': '返回编号', 'msg': '返回信息'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewBaiDuInfo"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewBaiDuInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewBaiDuInfo请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_saveSupplementImage(self, backgroundsupplementimages, contractuuid,
                                                            supplementimagetype, auditCheckType):
        """
        提交或编辑补录资料
        依赖函数：test_{'data': "{'newImageUuid': '新补录的图片UUID', 'newImageName': '新图片名称', 'originalImageUuid': '需要补录的图片UUID'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :param backgroundsupplementimages: newImageName
        :param contractuuid: newImageUuid
        :param supplementimagetype: originalImageUuid
        :param :
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/saveSupplementImage"
        self.LOGGER.info("test_api_78dk_platform_tm_first_saveSupplementImage请求地址:【{}】".format(requesturl))
        params = json.dumps({"backGroundSupplementImages": backgroundsupplementimages, "contractUuid": contractuuid,
                             "supplementImageType": supplementimagetype, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_saveSupplementImage请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_getSupplementImages(self, uid, ):
        """
        查询用户能补录的图片资料
        依赖函数：test_{'data': "{'keyName': '分类配置key名称', 'images': '图片影像资料实体', 'key': '图片配置key'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/getSupplementImages"
        self.LOGGER.info("test_api_78dk_platform_tm_first_getSupplementImages请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_getSupplementImages请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_passContract(self, audituuid, contractuuid, description,
                                                     supplementimagerequires, auditCheckType):
        """
        打回初审的合同
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/passContract"
        self.LOGGER.info("test_api_78dk_platform_tm_first_passContract请求地址:【{}】".format(requesturl))
        params = json.dumps({"auditUuid": audituuid, "contractUuid": contractuuid, "description": description,
                             "supplementImageRequires": supplementimagerequires, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_passContract请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_delAuditComment(self, uid, ):
        """
        删除一条评论
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/delAuditComment"
        self.LOGGER.info("test_api_78dk_platform_tm_first_delAuditComment请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_delAuditComment请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_findAuditCommentList(self, contractuuid, pagecurrent, pagesize, ):
        """
        查询评论列表
        依赖函数：test_{'data': "{'otherData': '其它数据', 'currentPage': '当前页码', 'totalPage': '总页数', 'pageSize': '单页记录数', 'dataList': '列表', 'totalCount': '总记录数'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/findAuditCommentList"
        self.LOGGER.info("test_api_78dk_platform_tm_first_findAuditCommentList请求地址:【{}】".format(requesturl))
        params = json.dumps({"contractUuid": contractuuid, "pageCurrent": pagecurrent, "pageSize": pagesize, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_findAuditCommentList请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_addAuditComment(self, comment, contractuuid, ):
        """
        添加一条评论
        依赖函数：test_{'data': "{'comment': '', 'auditCommentUuid': '评论UUID', 'created': '', 'auditUser': '审核人员', 'contractUuid': '', 'state': '', 'auditUserUuid': '', 'updated': '', 'replyAuditCommentUuid': ''}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/addAuditComment"
        self.LOGGER.info("test_api_78dk_platform_tm_first_addAuditComment请求地址:【{}】".format(requesturl))
        # params = json.dumps({"auditCommentAttachments": auditcommentattachments, "comment": comment, "contractUuid": contractuuid, "replyAuditCommentUuid": replyauditcommentuuid, })
        params = json.dumps({"comment": comment, "contractUuid": contractuuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_addAuditComment请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_editAuditComment(self, auditcommentuuid, comment, contractuuid, ):
        """
        编辑一条评论
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/editAuditComment"
        self.LOGGER.info("test_api_78dk_platform_tm_first_editAuditComment请求地址:【{}】".format(requesturl))
        params = json.dumps({"auditCommentUuid": auditcommentuuid, "comment": comment, "contractUuid": contractuuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_editAuditComment请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_first_viewTencentInfo(self, uid, ):
        """
        查询腾讯接口
        依赖函数：test_{'data': "{'reportInfo': '报告信息', 'created': '创建时间', 'updated': '更新时间'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/first/viewTencentInfo"
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewTencentInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_platform_tm_first_viewTencentInfo请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_telephone_saveTelephoneCheckInfos(self, answer, contractuuid, groupname, groupsort,
                                                                    question, questionsort, replytype,
                                                                    risktype, telephonecheckfeedbackuuid, ):
        """
        批量添加电核资料
        依赖函数：test_{'data': '返回数据', 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/telephone/saveTelephoneCheckInfos"
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_saveTelephoneCheckInfos请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"answer(N)": answer, "contractUuid(Y)": contractuuid, "groupName(Y)": groupname, "groupSort(Y)": groupsort,
             "question(Y)": question,
             "questionSort(Y)": questionsort, "replyType(Y)": replytype, "riskType": risktype,
             "telephoneCheckFeedbackUuid(N)": telephonecheckfeedbackuuid, })
        self.LOGGER.info("test_api_78dk_platform_tm_telephone_saveTelephoneCheckInfos请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_platform_tm_after_viewAuditMonitors(self, enddate, pagecurrent, pagesize, qifascore, searchwhere,
                                                          startdate, ):
        """
        贷后列表
        依赖函数：test_{'data': "{'pageSize': '单页记录数', 'totalCount': '总记录数', 'currentPage': '当前页码', 'otherData': '其它数据', 'dataList': '列表', 'totalPage': '总页数'}", 'code': '返回码', 'msg': '返回消息文本'}
        依赖参数：
        :param enddate: currentPage
        :param pagecurrent: dataList
        :param pagesize: otherData
        :param qifascore: pageSize
        :param searchwhere: totalCount
        :param startdate: totalPage
        :param :
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/platform/tm/after/viewAuditMonitors"
        self.LOGGER.info("test_api_78dk_platform_tm_after_viewAuditMonitors请求地址:【{}】".format(requesturl))
        params = json.dumps(
            {"endDate": enddate, "pageCurrent": pagecurrent, "pageSize": pagesize, "qifaScore": qifascore,
             "searchWhere": searchwhere, "startDate": startdate})
        self.LOGGER.info("test_api_78dk_platform_tm_after_viewAuditMonitors请求参数：【{}】".format(params))
        response = requests.request(
            "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text
