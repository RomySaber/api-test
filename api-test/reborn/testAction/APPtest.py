#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import requests
from common.myCommon import Assertion
from common.myCommon.Logger import getlog
import json

API_TEST_HEADERS = {"Content-Type": "application/json", "Cache-Control": "no-cache",'MyToken':'9a36591438c19c97720119a6ccff3b25'}
# baseUrl = "http://192.168.10.215:8080"
# http://test.jtlappserver.78dk.com/api/78dk/app/periods/postUserInfo
baseUrl="http://test2.jtlappserver.78dk.com"

class Buss4Action(object):
    LOGGER = getlog(__name__)
###############################################################################
#                              某模块（点击编辑后双击修改）                             #
# 模块描述：                                                                  #
###############################################################################

    def test_getLotteryLists(self, count, start, keyword,):
        """
        获取热门房地区列表
        :return: response.text
        """
        requesturl = baseUrl + "/getLotteryLists"
        self.LOGGER.info("test_getLotteryLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"count": count, "start": start, "keyword": keyword, })
        self.LOGGER.info("test_getLotteryLists请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_getHomeConfig(self):
        """
        获取首页内容（banner数据）
        :return: response.text
        """
        requesturl = baseUrl + "/getHomeConfig"
        self.LOGGER.info("test_getHomeConfig请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_getHomeConfig请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_technews(self, curentpage, pagesize,):
        """
        开发者资讯
        :return: response.text
        """
        requesturl = baseUrl + "/technews"
        self.LOGGER.info("test_technews请求地址:【{}】".format(requesturl))
        params = json.dumps({"curentPage": curentpage, "pageSize": pagesize, })
        self.LOGGER.info("test_technews请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_news(self, currentpage, pagesize,):
        """
        科技动态
        :return: response.text
        """
        requesturl = baseUrl + "/news"
        self.LOGGER.info("test_news请求地址:【{}】".format(requesturl))
        params = json.dumps({"currentPage": currentpage, "pageSize": pagesize, })
        self.LOGGER.info("test_news请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_topic(self, currentpage, pagesize,):
        """
        请求热门话题
        :return: response.text
        """
        requesturl = baseUrl + "/topic"
        self.LOGGER.info("test_topic请求地址:【{}】".format(requesturl))
        params = json.dumps({"currentPage": currentpage, "pageSize": pagesize, })
        self.LOGGER.info("test_topic请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_st_sm_repayment_setting(self, currentpage, pagesize,):
        """
        支付设置-页面初始化
        :return: response.text
        """
        requesturl = baseUrl + "/api/st/sm/repayment/setting"
        self.LOGGER.info("test_api_st_sm_repayment_setting请求地址:【{}】".format(requesturl))
        params = json.dumps({"currentPage": currentpage, "pageSize": pagesize, })
        self.LOGGER.info("test_api_st_sm_repayment_setting请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_st_sm_setting_save(self, id, openorclose, remarks,):
        """
        保存接口
        :return: response.text
        """
        requesturl = baseUrl + "/api/st/sm/setting/save"
        self.LOGGER.info("test_api_st_sm_setting_save请求地址:【{}】".format(requesturl))
        params = json.dumps({"id": id, "openOrClose": openorclose, "remarks": remarks, })
        self.LOGGER.info("test_api_st_sm_setting_save请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_sm_test(self, id, username, password,):
        """
        测试接口
        :return: response.text
        """
        requesturl = baseUrl + "/sm/test"
        self.LOGGER.info("test_sm_test请求地址:【{}】".format(requesturl))
        params = json.dumps({"id": id, "userName": username, "password": password, })
        self.LOGGER.info("test_sm_test请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_applyPeriods(self, amount, period, periodmoney, method,):
        """
        申请分期
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/applyPeriods"
        self.LOGGER.info("test_api_78dk_app_periods_applyPeriods请求地址:【{}】".format(requesturl))
        params = json.dumps({"amount": amount, "period": period, "periodMoney": periodmoney, "method": method ,"userLocation":''})
        self.LOGGER.info("test_api_78dk_app_periods_applyPeriods请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_getConsumption(self, paramsingle,):
        """
        获取额度测评
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/getConsumption"
        self.LOGGER.info("test_api_78dk_app_periods_getConsumption请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle, })
        self.LOGGER.info("test_api_78dk_app_periods_getConsumption请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_getPeriodsOptions(self, money,):
        """
        获取申请分期
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/getPeriodsOptions"
        self.LOGGER.info("test_api_78dk_app_periods_getPeriodsOptions请求地址:【{}】".format(requesturl))
        params = json.dumps({"money": money, })
        self.LOGGER.info("test_api_78dk_app_periods_getPeriodsOptions请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_postUserInfo(self, house, idcard, immediatefamily, job, kinsfolkphone, phone, relationship, username, decorationcityid, decorationdistrictid, decorationinputaddress, decorationprovinceid,):
        """
        填写基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/postUserInfo"
        self.LOGGER.info("test_api_78dk_app_periods_postUserInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"house": house, "idcard": idcard, "immediatefamily": immediatefamily, "job": job, "kinsfolkphone": kinsfolkphone, "phone": phone, "relationship": relationship, "username": username, "decorationCityId": decorationcityid, "decorationDistrictId": decorationdistrictid, "decorationInputAddress": decorationinputaddress, "decorationProvinceId": decorationprovinceid, })
        self.LOGGER.info("test_api_78dk_app_periods_postUserInfo请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_certification(self, idcard, phone, username, verifycode,):
        """
        实名认证
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/certification"
        self.LOGGER.info("test_api_78dk_app_periods_certification请求地址:【{}】".format(requesturl))
        params = json.dumps({"idcard": idcard, "phone": phone, "username": username, "verifycode": verifycode, })
        self.LOGGER.info("test_api_78dk_app_periods_certification请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_getVerify(self, mobile,):
        """
        获取短信验证码
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getVerify"
        self.LOGGER.info("test_api_78dk_app_periods_getVerify请求地址:【{}】".format(requesturl))
        params = json.dumps({"mobile": mobile, })
        self.LOGGER.info("test_api_78dk_app_periods_getVerify请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_loan_image_saveContractImages(self):
        """
        影像资料保存
        :param key: {'code': ''
        :param url:  'data': ''
        :param :  'msg': ''}
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/loan/image/saveContractImages"
        self.LOGGER.info("test_api_78dk_app_loan_image_saveContractImages请求地址:【{}】".format(requesturl))
        params = json.dumps([{"contractImageUuid":"","contractId":"","contractUuid":"","key":"YHSFZZPZM","url":"f12f/215684f12f875fc4982ff938590810acf066cd","originalImageUuid":""},{"contractImageUuid":"","contractId":"","contractUuid":"","key":"YHSFZZPFM","url":"f12f/215684f12f875fc4982ff938590810acf066cd","originalImageUuid":""},{"contractImageUuid":"","contractId":"","contractUuid":"","key":"YHSFZZPSC","url":"32cc/22183732cc17031b1dcd9550f79de5c9ff071f","originalImageUuid":""},{"contractImageUuid":"","contractId":"","contractUuid":"","key":"YHZXHTZP","url":"3e3a/2477093e3ae16110e4592b09b1f7a2c70f609b","originalImageUuid":""},{"contractImageUuid":"","contractId":"","contractUuid":"","key":"YHFCZM","url":"3e3a/2477093e3ae16110e4592b09b1f7a2c70f609b","originalImageUuid":""}])
        self.LOGGER.info("test_api_78dk_app_loan_image_saveContractImages请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_loan_image_viewImageRoleList(self, uid,):
        """
        影像资料权限
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageRoleList"
        self.LOGGER.info("test_api_78dk_app_loan_image_viewImageRoleList请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_app_loan_image_viewImageRoleList请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_loan_image_saveSupplementImage(self, datalists, uid,):
        """
        影像资料补录保存
        :param datalists: {'code': ''
        :param uid:  'data': ''
        :param :  'msg': ''}
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/loan/image/saveSupplementImage"
        self.LOGGER.info("test_api_78dk_app_loan_image_saveSupplementImage请求地址:【{}】".format(requesturl))
        params = json.dumps({"dataLists": datalists, "uid": uid, })
        self.LOGGER.info("test_api_78dk_app_loan_image_saveSupplementImage请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_loan_image_viewImageSupplementList(self, uid,):
        """
        影像资料补录列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/loan/image/viewImageSupplementList"
        self.LOGGER.info("test_api_78dk_app_loan_image_viewImageSupplementList请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_app_loan_image_viewImageSupplementList请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_getUserInfo(self, authcode, storeuuid, preferential,):
        """
        获取用户信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getUserInfo"
        self.LOGGER.info("test_api_78dk_app_base_getUserInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({"authCode": authcode, "storeUuid": storeuuid, "preferential": preferential, })
        self.LOGGER.info("test_api_78dk_app_base_getUserInfo请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_loan_alipay_getAlipayVid(self):
        """
        获取支付宝验签Vid
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/loan/alipay/getAlipayVid"
        self.LOGGER.info("test_api_78dk_app_loan_alipay_getAlipayVid请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_loan_alipay_getAlipayVid请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_getFddUrl(self):
        """
        获取法大大合同地址
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getFddUrl"
        self.LOGGER.info("test_api_78dk_app_base_getFddUrl请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_base_getFddUrl请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_getFddResult(self):
        """
        获取法大大合同签订结果
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getFddResult"
        self.LOGGER.info("test_api_78dk_app_base_getFddResult请求地址:【{}】".format(requesturl))
        # params = json.dumps({"url":url})
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_base_getFddResult请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_periods_getUserInfo(self):
        """
        查询基本信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/periods/getUserInfo"
        self.LOGGER.info("test_api_78dk_app_periods_getUserInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_periods_getUserInfo请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_getWsAuditResult(self):
        """
        网商进件
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getWsAuditResult"
        self.LOGGER.info("test_api_78dk_app_base_getWsAuditResult请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_base_getWsAuditResult请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_user_getUserInfo(self):
        """
        获取个人信息
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/user/getUserInfo"
        self.LOGGER.info("test_api_78dk_app_user_getUserInfo请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_user_getUserInfo请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_apply_getRecords(self, pagecurrent, pagesize,):
        """
        获取申请记录
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/apply/getRecords"
        self.LOGGER.info("test_api_78dk_app_apply_getRecords请求地址:【{}】".format(requesturl))
        params = json.dumps({"pageCurrent": pagecurrent, "pageSize": pagesize, })
        self.LOGGER.info("test_api_78dk_app_apply_getRecords请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_apply_getRepaymentPlan(self, pagesize, pagecurrent, paraminfo,):
        """
        获取还款计划
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/apply/getRepaymentPlan"
        self.LOGGER.info("test_api_78dk_app_apply_getRepaymentPlan请求地址:【{}】".format(requesturl))
        params = json.dumps({"pageSize": pagesize, "pageCurrent": pagecurrent, "paramInfo": paraminfo, })
        self.LOGGER.info("test_api_78dk_app_apply_getRepaymentPlan请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_apply_getRecordByUuid(self, paraminfo,):
        """
        查询单条申请记录
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/apply/getRecordByUuid"
        self.LOGGER.info("test_api_78dk_app_apply_getRecordByUuid请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramInfo": paraminfo, })
        self.LOGGER.info("test_api_78dk_app_apply_getRecordByUuid请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_getFddCheckUrl(self, uid,):
        """
        获取法大大合同查看地址
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/getFddCheckUrl"
        self.LOGGER.info("test_api_78dk_app_base_getFddCheckUrl请求地址:【{}】".format(requesturl))
        params = json.dumps({"uid": uid, })
        self.LOGGER.info("test_api_78dk_app_base_getFddCheckUrl请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_list_viewRegionLists(self, paramsingle,):
        """
        获取区/县下拉列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/list/viewRegionLists"
        self.LOGGER.info("test_api_78dk_app_base_list_viewRegionLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle, })
        self.LOGGER.info("test_api_78dk_app_base_list_viewRegionLists请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_list_viewCityLists(self, paramsingle,):
        """
        获取市下拉列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/list/viewCityLists"
        self.LOGGER.info("test_api_78dk_app_base_list_viewCityLists请求地址:【{}】".format(requesturl))
        params = json.dumps({"paramSingle": paramsingle, })
        self.LOGGER.info("test_api_78dk_app_base_list_viewCityLists请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

    def test_api_78dk_app_base_list_viewProvinceLists(self):
        """
        获取省下拉列表
        :return: response.text
        """
        requesturl = baseUrl + "/api/78dk/app/base/list/viewProvinceLists"
        self.LOGGER.info("test_api_78dk_app_base_list_viewProvinceLists请求地址:【{}】".format(requesturl))
        params = json.dumps({})
        self.LOGGER.info("test_api_78dk_app_base_list_viewProvinceLists请求参数：【{}】".format(params))
        response = requests.request(
                "POST", requesturl, headers=API_TEST_HEADERS, data=params
        )
        self.LOGGER.info("请求结果参数：【{}】".format(response.text))
        Assertion.verity(response.status_code, 200, "状态码检查")
        return response.text

