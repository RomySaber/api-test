#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-11 上午 11:26
@Author     : 罗林
@File       : test_015_app_process_WorkInfo.py
@desc       :  进件模块自动化测试用例(工作信息)
"""

import json
import unittest
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from ymjry.testAction import AppAction
from ymjry.testAction import loginAction

fake = Factory().create('zh_CN')
company_city = '510100'
company_city_name = '成都市'
company_detail = '天府软件园B区'
company_name = fake.company() + loginAction.sign
company_province = '510000'
company_province_name = '四川省'
company_region = '510108'
company_region_name = '成华区'
datum_type_income_id = '25'
datum_type_worktime_id = '93'
position = fake.job() + loginAction.sign
work_phone = fake.phone_number()


class test_015_app_process_WorkInfo(TestBaseCase):
    def test_001_api_78dk_app_process_saveWorkInfo(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '10000')

    @unittest.skip('未检查地址信息')
    def test_002_api_78dk_app_process_saveWorkInfo_companycity_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity='', companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74',
            scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    def test_003_api_78dk_app_process_saveWorkInfo_companycity_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity='abc', companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_004_api_78dk_app_process_saveWorkInfo_companycity_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=fake.ean8(), companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74',
            scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_005_api_78dk_app_process_saveWorkInfo_companyname_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname='', companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74',
            scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    def test_006_api_78dk_app_process_saveWorkInfo_256_companyname(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=''.join(fake.words(nb=128)), companyprovince=company_province,
            companyprovincename=company_province_name, companyregion=company_region,
            companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_007_api_78dk_app_process_saveWorkInfo_companyprovince_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince='', companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    def test_008_api_78dk_app_process_saveWorkInfo_companyprovince_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince='abc', companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_009_api_78dk_app_process_saveWorkInfo_companyprovince_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=fake.ean8(), companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_010_api_78dk_app_process_saveWorkInfo_companyregion_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion='', companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    def test_011_api_78dk_app_process_saveWorkInfo_companyregion_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion='abc', companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_012_api_78dk_app_process_saveWorkInfo_companyregion_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=fake.ean8(), companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查地址信息')
    def test_013_api_78dk_app_process_saveWorkInfo_datumtypeincomeid_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid='',
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '未选择薪资！')

    def test_014_api_78dk_app_process_saveWorkInfo_datumtypeincomeid_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid='abc',
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('接口修改，不在需要验证datumtypeincomeid')
    def test_015_api_78dk_app_process_saveWorkInfo_datumtypeincomeid_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=fake.ean8(),
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('接口修改，不在需要验证datumtypeworktimeid')
    def test_016_api_78dk_app_process_saveWorkInfo_datumtypeworktimeid_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '未选择工作时间！')

    @unittest.skip('接口修改，不在需要验证datumtypeworktimeid')
    def test_017_api_78dk_app_process_saveWorkInfo_datumtypeworktimeid_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='', scaleid='',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('接口修改，不在需要验证datumtypeworktimeid')
    def test_018_api_78dk_app_process_saveWorkInfo_datumtypeworktimeid_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查职位信息')
    def test_019_api_78dk_app_process_saveWorkInfo_position_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position='', workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '职位为空！')

    def test_020_api_78dk_app_process_saveWorkInfo_256position(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=''.join(fake.words(nb=128)), workphone=work_phone, propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查职位信息')
    def test_021_api_78dk_app_process_saveWorkInfo_workphone_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position='', workphone='', propertiesid='74', scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '职位为空！')

    def test_022_api_78dk_app_process_saveWorkInfo_workphone_error(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, scaleid='81',
            datumtypeincomeid=datum_type_income_id, propertiesid='74', position=position, workphone='abc',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '10000')

    def test_023_api_78dk_app_process_saveWorkInfo_10workphone(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, scaleid='81',
            datumtypeincomeid=datum_type_income_id, propertiesid='74', position=position, workphone='1310000000',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '10000')

    @unittest.skip('未检查单位性质')
    def test_024_api_78dk_app_process_saveWorkInfo_propertiesid_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '未选择单位性质！')

    def test_025_api_78dk_app_process_saveWorkInfo_propertiesid_not_num(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='weuh', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查单位性质')
    def test_026_api_78dk_app_process_saveWorkInfo_propertiesid_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='0', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '单位性质不存在')

    @unittest.skip('未检查单位规模')
    def test_027_api_78dk_app_process_scaleid_propertiesid_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='74', scaleid='',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '未选择单位规模！')

    def test_028_api_78dk_app_process_saveWorkInfo_scaleid_not_num(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='74', scaleid='sdf',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('未检查单位规模')
    def test_029_api_78dk_app_process_saveWorkInfo_scaleid_not_exits(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='74', scaleid='0',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '单位不存在')

    @unittest.skip('工作年限字段v1。4没有，废弃')
    def test_030_api_78dk_app_process_scaleid_workyear_none(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            position=position, workphone='131000000000', propertiesid='74', scaleid='81',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '现单位工作年限不能为0！')

    @unittest.skip('工作年限字段v1。4没有，废弃')
    def test_031_api_78dk_app_process_saveWorkInfo_workyear_not_num(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name,
            datumtypeincomeid=datum_type_income_id, position=position, workphone='131000000000',
            propertiesid='74', scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')

    @unittest.skip('工作年限字段v1。4没有，废弃')
    def test_032_api_78dk_app_process_saveWorkInfo_workyear_zero(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name,
            datumtypeincomeid=datum_type_income_id, position=position, workphone='131000000000',
            propertiesid='74', scaleid='81', datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '现单位工作年限不能为0！')

    def test_033_api_78dk_app_process_saveWorkInfo_12workphone(self):
        """
        保存工作信息
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_saveWorkInfo(
            companycity=company_city, companycityname=company_city_name, companydetail=company_detail,
            companyname=company_name, companyprovince=company_province, companyprovincename=company_province_name,
            companyregion=company_region, companyregionname=company_region_name, datumtypeincomeid=datum_type_income_id,
            propertiesid='74', scaleid='81', position=position, workphone='131000000000',
            datumtypeworktimeid=datum_type_worktime_id))
        Assertion.verity(res['code'], '10000')

    def test_034_api_78dk_app_process_getNewestWorkInfo(self):
        """
        查询工作信息（最近的）
        :return:
        """
        res = json.loads(AppAction.test_api_78dk_app_process_getNewestWorkInfo())
        Assertion.verity(res['code'], '10000')
        Assertion.verityContain(res['data'], 'companyCity')
        Assertion.verityContain(res['data'], 'companyCityName')
        Assertion.verityContain(res['data'], 'companyDetail')
        Assertion.verityContain(res['data'], 'companyName')
        Assertion.verityContain(res['data'], 'companyProvince')
        Assertion.verityContain(res['data'], 'companyProvinceName')
        Assertion.verityContain(res['data'], 'companyRegion')
        Assertion.verityContain(res['data'], 'companyRegionName')
        Assertion.verityContain(res['data'], 'datumTypeIncomeId')
        Assertion.verityContain(res['data'], 'datumTypeIncomeName')
        Assertion.verityContain(res['data'], 'datumTypeWorktimeId')
        Assertion.verityContain(res['data'], 'datumTypeWorktimeName')
        Assertion.verityContain(res['data'], 'position')
        Assertion.verityContain(res['data'], 'workPhone')

    def test_035_api_78dk_app_process_saveUserMailListInfo(self):
        """
        保存用户通讯录信息（新）
        :return:
        """
        content = [{"name": "税充华", "phones": []}, {"name": "张扬", "phones": ["18243003707"]},
                   {"name": "谈聪", "phones": ["18281605123", "15061122579"]}]
        res = json.loads(AppAction.test_api_78dk_app_process_saveUserMailListInfo(content))
        Assertion.verity(res['code'], '10000')

    def test_036_process_saveCallList(self):
        """
        保存通话详单（美佳v1.0.0-作废）
        :return:
        """
        content = [{"name": "税充华", "phones": []}, {"name": "张扬", "phones": ["18243003707"]},
                   {"name": "谈聪", "phones": ["18281605123", "15061122579"]}]
        res = json.loads(AppAction.test_api_78dk_app_process_saveCallList(content))
        Assertion.verity(res['code'], '20000')
