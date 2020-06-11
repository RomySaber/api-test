#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-10 下午 6:34
@Author     : 罗林
@File       : test_014_app_process_PersonInfo.py
@desc       : 进件模块自动化测试用例(基本信息)
"""

import json

from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_app_finance_consumptionAction as AppAction
from xqkj.testAction import loginAction

fake = Factory().create('zh_CN')
contact_num = 2  # 通讯录个数
email = fake.email()


class test_014_app_process_PersonInfo(TestBaseCase):
    def test_001_api_78dk_app_process_savePersonInfo(self):
        """
        保存基本信息
        :return:
        """
        user_uuid = loginAction.global_dict.get('user_uuid')
        global datum_type_education_id, datum_type_housing_id, datum_type_marry_id, live_city, live_city_name
        global live_detail, live_province, live_province_name, live_region, live_region_name, contactlist
        datum_type_education_id, datum_type_housing_id, datum_type_marry_id, live_city, live_city_name, live_detail, \
        live_province, live_province_name, live_region, live_region_name = xqkj_query.get_info(
            'Tbl_UserPersonalInfo',
            'datum_type_education_id,datum_type_housing_id,datum_type_marry_id,live_city,live_city_name,'
            'live_detail,live_province,live_province_name,live_region,live_region_name',
            'user_uuid="{}"'.format(user_uuid))
        contactlist = [{"datumTypeContactId": i + 1, "name": fake.name(), "phone": fake.phone_number()} for i in
                       range(contact_num)]
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province, email=email, iswork=1,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name))
        Assertion.verity(res['code'], '20000')

    def test_002_api_78dk_app_process_savePersonInfo_contactlist_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=[], datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_003_api_78dk_app_process_savePersonInfo_contactlist_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist='123', datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_004_api_78dk_app_process_savePersonInfo_datumtypeeducationid_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid='',
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_005_api_78dk_app_process_savePersonInfo_datumtypeeducationid_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid='abc',
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_006_api_78dk_app_process_savePersonInfo_datumtypeeducationid_not_exits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=fake.ean8(),
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_007_api_78dk_app_process_savePersonInfo_datumtypehousingid_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid='', datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_008_api_78dk_app_process_savePersonInfo_datumtypehousingid_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid='abc', datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_009_api_78dk_app_process_savePersonInfo_datumtypehousingid_not_exits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=fake.ean8(), datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_010_api_78dk_app_process_savePersonInfo_datumtypemarryid_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid='', livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_app_process_savePersonInfo_datumtypemarryid_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid='abc', livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_012_api_78dk_app_process_savePersonInfo_datumtypemarryid_notexits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=fake.ean8(), livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_013_api_78dk_app_process_savePersonInfo_livecity_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity='',
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_014_api_78dk_app_process_savePersonInfo_livecity_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity='abc',
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_015_api_78dk_app_process_savePersonInfo_livecity_not_exits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=fake.ean8(),
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_016_api_78dk_app_process_savePersonInfo_liveprovince_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince='',
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_017_api_78dk_app_process_savePersonInfo_liveprovince_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince='ABC',
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_018_api_78dk_app_process_savePersonInfo_liveprovince_not_exits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=fake.ean8(),
            liveprovincename=live_province_name, liveregion=live_region, liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_019_api_78dk_app_process_savePersonInfo_liveregion_none(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion='', liveregionname=live_region_name, email='', iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_020_api_78dk_app_process_savePersonInfo_liveregion_error(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion='abc', liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_021_api_78dk_app_process_savePersonInfo_liveregion_not_exits(self):
        """
        保存基本信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_savePersonInfo(
            contactlist=contactlist, datumtypeeducationid=datum_type_education_id,
            datumtypehousingid=datum_type_housing_id, datumtypemarryid=datum_type_marry_id, livecity=live_city,
            livecityname=live_city_name, livedetail=live_detail, liveprovince=live_province,
            liveprovincename=live_province_name, liveregion=fake.ean8(), liveregionname=live_region_name, email='',
            iswork=''))
        Assertion.verity(res['code'], '20000')

    def test_022_api_78dk_app_process_getNewestPersonInfo(self):
        """
        查询基本信息（最近的）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getNewestPersonInfo())
        Assertion.verity(res['code'], '10000')
        # Assertion.verityContain(res['data']['contactList'], 'datumTypeContactId')
        # Assertion.verityContain(res['data']['contactList'], 'datumTypeContactName')
        # Assertion.verityContain(res['data']['contactList'], 'name')
        # Assertion.verityContain(res['data']['contactList'], 'phone')
        # Assertion.verityContain(res['data'], 'datumTypeEducationId')
        # Assertion.verityContain(res['data'], 'datumTypeEducationName')
        # Assertion.verityContain(res['data'], 'datumTypeHousingId')
        # Assertion.verityContain(res['data'], 'datumTypeHousingName')
        # Assertion.verityContain(res['data'], 'datumTypeMarryId')
        # Assertion.verityContain(res['data'], 'datumTypeMarryName')
        # Assertion.verityContain(res['data'], 'liveCity')
        # Assertion.verityContain(res['data'], 'liveCityName')
        # Assertion.verityContain(res['data'], 'liveDetail')
        # Assertion.verityContain(res['data'], 'liveProvince')
        # Assertion.verityContain(res['data'], 'liveProvinceName')
        # Assertion.verityContain(res['data'], 'liveRegion')
        # Assertion.verityContain(res['data'], 'liveRegionName')

    def test_023_test_api_78dk_app_process_sendVerifyEmail(self):
        """
        发送验证邮件（新）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_sendVerifyEmail(email=email))
        Assertion.verity(res['code'], '10000')
