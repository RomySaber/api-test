#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-12 下午 6:33
@Author     : 罗林
@File       : test_012_app_process_OrcInfo.py
@desc       : 进件模块自动化测试用例(身份证认证)
"""

import json
import unittest

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from hmpt.query import xqkj_query
from hmpt.testAction import AppAction
from hmpt.testAction import loginAction

fake = Factory().create('zh_CN')


class test_012_app_process_OrcInfo(TestBaseCase):
    def test_001_api_78dk_app_process_saveOrcInfo(self):
        """
        保存人脸识别结果
        :return:
        """
        global firstkey, secondkey, thirdkey, note, user_uuid
        firstkey = secondkey = thirdkey = 'base64_1560837249133.jpeg'
        note = ''
        user_uuid = loginAction.get_user_uuid()
        # firstkey, secondkey, thirdkey, note, user_uuid = xqkj_query.get_info(
        #     'Tbl_UserOcrInfo', 'first_key,second_key,third_key,note,user_uuid')
        loginAction.global_dict.set(user_uuid=user_uuid)
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey=firstkey, secondkey=secondkey, thirdkey=thirdkey, note=note, contractuuid='', result=1))
        Assertion.verity(res['code'], '10000')

    def test_002_api_78dk_app_process_saveOrcInfo_firstkey_none(self):
        """
        保存人脸识别结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey='', secondkey=secondkey, thirdkey=thirdkey, note=note, contractuuid='', result=0))
        Assertion.verity(res['code'], '10000')

    def test_003_api_78dk_app_process_saveOrcInfo_secondkey_none(self):
        """
        保存人脸识别结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey=firstkey, secondkey='', thirdkey=thirdkey, note=note, contractuuid='', result=0))
        Assertion.verity(res['code'], '10000')

    def test_004_api_78dk_app_process_saveOrcInfo_thirdkey_none(self):
        """
        保存人脸识别结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey=firstkey, secondkey=secondkey, thirdkey='', note=note, contractuuid='', result=0))
        Assertion.verity(res['code'], '10000')

    def test_005_api_78dk_app_process_saveOrcInfo_note_none(self):
        """
        保存人脸识别结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey=firstkey, secondkey=secondkey, thirdkey=thirdkey, note='', contractuuid='', result=1))
        Assertion.verity(res['code'], '10000')

    def test_006_api_78dk_app_process_saveOrcInfo_two(self):
        """
        保存人脸识别结果
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveOrcInfo(
            firstkey=firstkey, secondkey=secondkey, thirdkey=thirdkey, note=note, contractuuid='', result=1))
        Assertion.verity(res['code'], '10000')

    def test_007_api_78dk_app_process_saveHoldKey(self):
        """
        保存手持身份证照片
        :return:
        """
        global hold_key, card_scan_idcard_no, card_scan_name, front_key, front_note, opposite_key, opposite_note
        front_key = '0e07631d7a2c2beaa44e29c2a8301e5.png'
        opposite_key = 'b500be2dc3148cbd0cceb9bbe89d9a4.png'
        hold_key = 'des_1560837224439.jpeg'
        card_scan_idcard_no = loginAction.idcard
        card_scan_name = loginAction.user_name
        front_note = opposite_note = ''
        res = json.loads(AppAction.test_api_78dk_app_process_saveHoldKey(holdkey=hold_key))
        Assertion.verity(res['code'], '10000')

    def test_008_api_78dk_app_process_saveHoldKey_none(self):
        """
        保存手持身份证照片
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveHoldKey(holdkey=''))
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_app_process_saveIdCardInfo_cardno_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno='', cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')

    def test_010_api_78dk_app_process_saveIdCardInfo_cardno_error(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno='abc', cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_app_process_saveIdCardInfo_14cardno(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=fake.random_number(14), cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')

    def test_012_api_78dk_app_process_saveIdCardInfo_16cardno(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno='1234567890123456', cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote='', oppositenote=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '身份证号不正确！')

    def test_013_api_78dk_app_process_saveIdCardInfo_17cardno(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=fake.random_number(17), cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')

    def test_014_api_78dk_app_process_saveIdCardInfo_19cardno(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=fake.random_number(20), cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')

    def test_015_api_78dk_app_process_saveIdCardInfo_cardscanname_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname='', oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '身份证姓名为空！')

    def test_016_api_78dk_app_process_saveIdCardInfo_oppositekey_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname=card_scan_name, oppositekey='',
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '10000')

    def test_017_api_78dk_app_process_saveIdCardInfo_frontkey_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey='', frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '10000')

    def test_018_api_78dk_app_process_saveIdCardInfo_frontnote_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote='', oppositenote=opposite_note))
        Assertion.verity(res['code'], '10000')

    def test_019_api_78dk_app_process_saveIdCardInfo_oppositenote_none(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=''))
        Assertion.verity(res['code'], '10000')

    def test_020_api_78dk_app_process_saveIdCardInfo(self):
        """
        保存身份证信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveIdCardInfo(
            cardscanidcardno=card_scan_idcard_no, cardscanname=card_scan_name, oppositekey=opposite_key,
            frontkey=front_key, frontnote=front_note, oppositenote=opposite_note))
        Assertion.verity(res['code'], '10000')

    @unittest.expectedFailure
    def test_021_api_78dk_app_process_getNewestIdCardInfo(self):
        """
        查询身份证信息（最近的）
        :return:
        """
        global contract_uuid
        contract_uuid = xqkj_query.get_contract_uuid_for_user(loginAction.get_user_uuid())
        loginAction.global_dict.set(contract_uuid=contract_uuid)
        res = json.loads(AppAction.test_api_78dk_app_process_getNewestIdCardInfo(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['data']['cardScanIdcardNo'], card_scan_idcard_no)
        Assertion.verity(res['data']['cardScanName'], card_scan_name)
        Assertion.verity(res['data']['frontKey'], front_key)
        Assertion.verity(res['data']['frontNote'], front_note)
        Assertion.verityContain(res['data'], 'frontUrl')
        Assertion.verity(res['data']['holdKey'], hold_key)
        Assertion.verityContain(res['data'], 'holdUrl')
        Assertion.verity(res['data']['oppositeKey'], opposite_key)
        Assertion.verity(res['data']['oppositeNote'], opposite_note)
        Assertion.verityContain(res['data'], 'oppositeUrl')

    def test_022_api_78dk_app_process_getNewestIdCardHandle(self):
        """
        查询身份证信息(手持)---美佳v1.0.4修改
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getNewestIdCardHandle(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')

    @unittest.expectedFailure
    def test_023_api_78dk_app_process_findOrcInfo(self):
        """
        查询人脸识别结果---美佳v1.0.5
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_findOrcInfo(contractuuid=contract_uuid))
        Assertion.verity(res['code'], '10000')
