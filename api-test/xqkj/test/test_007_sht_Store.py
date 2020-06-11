#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time       :2019-08-16 上午 10:10
@Author     : 张静珍
@File       : test_007_sht_Store.py
@desc       :商户通门店管理接口自动化用例
"""

import json
import unittest
import os
from faker import Factory

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from common.myFile import MockData
from xqkj.query import sht_query
from xqkj.testAction import ShtAction
from xqkj.testAction import loginAction
from xqkj.testAction import specialAction

fake = Factory().create('zh_CN')
# 商户名称,标记数据方便定位删除
merchantname = fake.company() + loginAction.sign
store_name = fake.company_prefix() + loginAction.sign
# 申请人联系信息
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = MockData.phone(11)
cardnumber = fake.ssn()


class test_007_sht_Store(TestBaseCase):
    def test_001_api_78dk_sht__store_modifystorebasic_storeaddress_none(self):
        """
        新增门店基本信息：门店地址为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='', leasetimebegin='2019-08-08',
                storename='门店地址空', leasetimeend='2020-08-08', employeesnum=100, storeregion='', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='', storeregioncode='', area='', storeaddress='',
                storeprovince='', idcardnumber=cardnumber, email=email, storecity=''))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '数据完整性错误')

    def test_002_api_78dk_sht__store_modifystorebasic_256storename(self):
        """
        新增门店基本信息：门店名称超长
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=MockData.words_cn(256), leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区',
                managername=name, managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='123', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '门店名字长度超过限制')

    def test_003_api_78dk_sht__store_modifystorebasic_storename_none(self):
        """
        新增门店基本信息：门店名称为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename='', leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='123', storeprovince='河北省', idcardnumber=cardnumber, email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '请填写门店名')
        Assertion.verity(res['code'], 'S0006')

    def test_004_api_78dk_sht__store_modifystorebasic_leasetimebegin_none(self):
        """
        新增门店基本信息：租赁起止日期为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='',
                storename='门店名称' + MockData.words_cn(1), leasetimeend='', employeesnum=100, storeregion='新华区',
                managername=name, managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='123', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '请输入租赁时间')

    def test_005_api_78dk_sht_store_modifystorebasic(self):
        """
        新增门店基本信息：租赁起始日期大于截止日期
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2219-08-08',
                storename='门店名字' + MockData.words_cn(2), leasetimeend='2020-08-08', employeesnum=100,
                storeregion='新华区', managername=name, managerphone=mobile, storeuuid='', storecitycode='130100',
                storeregioncode='130105', area='1999', storeaddress='123', storeprovince='河北省',
                idcardnumber=cardnumber, email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '起始时间不能大于结束时间')
        Assertion.verity(res['code'], 'S0006')

    def test_006_api_78dk_sht__store_modifystorebasic(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区',
                managername=name, managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='123', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['code'], '10000')
        global store_uuid
        store_uuid = res['data']['storeUuid']
        loginAction.global_dict.set(store_uuid=store_uuid)

    def test_007_api_78dk_sht_store_modifystorebasic_leasetimebegin_none(self):
        """
        新增门店基本信息：
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='',
                storename='门店名字' + MockData.words_cn(2), leasetimeend='2020-08-08', employeesnum=100,
                storeregion='新华区', managername=name, managerphone=mobile, storeuuid='', storecitycode='130100',
                storeregioncode='130105', area='1999', storeaddress='123', storeprovince='河北省',
                idcardnumber=cardnumber, email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '请输入租赁时间')
        Assertion.verity(res['code'], 'S0006')

    def test_008_api_78dk_sht__store_modifystorebasic_leasetimeend_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_009_api_78dk_sht__store_modifystorebasic_employeesnum_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum="", storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_010_api_78dk_sht__store_modifystorebasic_storeregion_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_011_api_78dk_sht__store_modifystorebasic_managername_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername='',
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '请填写负责人姓名')
        Assertion.verity(res['code'], 'S0006')

    def test_012_api_78dk_sht__store_modifystorebasic_managerphone_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone='', storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '申请人电话格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_013_api_78dk_sht__store_modifystorebasic_10managerphone(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=MockData.phone(10), storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber,
                email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '申请人电话格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_014_api_78dk_sht__store_modifystorebasic_12managerphone(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=MockData.phone(12), storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber,
                email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '申请人电话格式不合法')
        Assertion.verity(res['code'], 'S0006')

    def test_015_api_78dk_sht__store_modifystorebasic_storecitycode_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_016_api_78dk_sht__store_modifystorebasic_storeregioncode_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_017_api_78dk_sht__store_modifystorebasic_area_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_018_api_78dk_sht__store_modifystorebasic_storeprovince_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_019_api_78dk_sht__store_modifystorebasic_idcardnumber_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber='', email=email,
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '身份证格式错误')
        Assertion.verity(res['code'], 'S0006')

    def test_020_api_78dk_sht__store_modifystorebasic_17idcardnumber(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=MockData.strNumber(17),
                email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '身份证格式错误')
        Assertion.verity(res['code'], 'S0006')

    def test_021_api_78dk_sht__store_modifystorebasic_19idcardnumber(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=MockData.strNumber(19),
                email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '身份证格式错误')
        Assertion.verity(res['code'], 'S0006')

    def test_022_api_78dk_sht__store_modifystorebasic_email_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email='',
                storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_023_api_78dk_sht__store_modifystorebasic_email_error(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber,
                email=MockData.strNumber(10), storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_024_api_78dk_sht__store_modifystorebasic_storecity_none(self):
        """
        新增门店基本信息：信息正确
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105', area='1999',
                storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity=''))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_025_api_78dk_sht_store_modifystorebasic_storeprovincecode_none(self):
        """
        新增门店基本信息：
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='', leasetimebegin='2019-08-08',
                storename='门店名字' + MockData.words_cn(2), leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区',
                managername=name, managerphone=mobile, storeuuid='', storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='123', storeprovince='河北省', idcardnumber=cardnumber, email=email,
                storecity='石家庄市'))
        Assertion.verity(res['code'], '20000')
        Assertion.verity(res['msg'], '数据完整性错误')

    @unittest.expectedFailure
    def test_026_api_78dk_sht_store_modifystoreshtactioniness_store_uuid_none(self):
        """
        新增门店业务信息：有贴息，无工作占比
        :return:
        """
        global products
        products = [{"productName": "有贴息，无工作占比", "productAmount": "3", "productCycle": "3"}]
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=10, workpercent='',
            storebusinessproducts=products, businessuuid='', storeuuid=''))
        # Assertion.verity(res['code'], '10000')
        Assertion.verity(res['code'], 'S0005')
        Assertion.verityContain(res['msg'], '该门店已经提交业务信息，无法再次提交！')

    def test_027_api_78dk_sht_store_modifystoreshtactioniness_storebusinessproducts_none(self):
        """
        新增门店业务信息：有贴息，无工作占比
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=10, workpercent='',
            storebusinessproducts='', businessuuid='', storeuuid=store_uuid))
        Assertion.verity(res['code'], '20000')

    def test_028_api_78dk_sht_store_modifystoreshtactioniness_discountpercent_none(self):
        """
        新增门店业务信息：有贴息，无工作占比
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent='', workpercent='',
            storebusinessproducts=products, businessuuid='', storeuuid=store_uuid))
        Assertion.verity(res['code'], '10000')
        global businessUuid
        businessUuid = res["data"]["businessUuid"]

    def test_029_api_78dk_sht_store_modifystoreshtactioniness_workpercent_error(self):
        """
        新增门店业务信息：有贴息，无工作占比
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=10,
            workpercent=MockData.wordAndNum(256), storebusinessproducts='', businessuuid='', storeuuid=store_uuid))
        Assertion.verity(res['code'], '20000')

    def test_030_api_78dk_sht_store_modifystoreshtactioniness(self):
        """
        新增门店业务信息：有贴息，无工作占比
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=10, workpercent='',
            storebusinessproducts=products, businessuuid='', storeuuid=store_uuid))
        Assertion.verity(res['code'], 'S0005')
        Assertion.verity(res['msg'], '该门店已经提交业务信息，无法再次提交！')

    def test_031_api_78dk_sht_store_submitstore_none(self):
        """
        提交门店信息：门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_submitStore(storeuuid=''))
        Assertion.verity(res['msg'], '参数有误')
        Assertion.verity(res['code'], 'S0006')

    def test_032_api_78dk_sht_store_submitstore_error(self):
        """
        提交门店信息：门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_submitStore(storeuuid=MockData.wordAndNum(15)))
        Assertion.verity(res['msg'], '未知的门店')
        Assertion.verity(res['code'], 'S0006')

    def test_033_api_78dk_sht_store_submitstore_none(self):
        """
        提交门店信息：门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_submitStore(storeuuid=''))
        Assertion.verity(res['msg'], '参数有误')
        Assertion.verity(res['code'], 'S0006')

    def test_034_api_78dk_sht_store_submitstore(self):
        """
        提交门店信息：门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_submitStore(storeuuid=store_uuid))
        # 修改数据库，将门店审核通过
        sht_query.update_pass_store_state(audit_state='pass', store_uuid=store_uuid)
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_035_api_78dk_sht_store_submitstore(self):
        """
        保存单张图片
        :return:
        """
        image_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'testSource', '1.png')
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDFZRSFZZM', storeuuid=store_uuid,
                                                           image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDFZRSFZFM', storeuuid=store_uuid, 
                                                           image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDFZRSFZSC', storeuuid=store_uuid,
                                                           image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDWBHJZ', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDNBHJZ', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDQTLOGO', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDZLHT', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDPXXY', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDZLHT', storeuuid=store_uuid, image_path=image_path)
        specialAction.test_api_78dk_sht_store_saveStoreImg(key='MDQTZL', storeuuid=store_uuid, image_path=image_path)

    def test_036_api_78dk_sht_store_dividestore(self):
        """
        门店分配：信息完整
        :return:
        """

        res = json.loads(ShtAction.test_api_78dk_sht_store_divideStore(useruuids=[], storeuuid=store_uuid))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_037_api_78dk_sht_store_dividestore_useruuids_none(self):
        """
        门店分配：用户uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_divideStore(useruuids='', storeuuid=store_uuid))
        Assertion.verity(res['msg'], '成功')
        Assertion.verity(res['code'], '10000')

    def test_038_api_78dk_sht_store_dividestore_storeuuid_none(self):
        """
        门店分配:门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_divideStore(useruuids=[], storeuuid=''))
        Assertion.verity(res['msg'], '门店信息为空')
        Assertion.verity(res['code'], 'S0006')

    def test_039_api_78dk_sht__store_modifystoresasic_storeuuid_error(self):
        """
        修改门店基本信息:修改门店名称
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid=MockData.wordAndNum(20), storecitycode='130100',
                storeregioncode='130105', area='1999', storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省',
                idcardnumber=cardnumber, email=email, storecity='石家庄市'))
        Assertion.verity(res['msg'], '门店名重复！')
        Assertion.verity(res['code'], 'S0006')

    def test_040_api_78dk_sht__store_modifystoresasic(self):
        """
        修改门店基本信息:修改租赁起止日期
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht__store_modifyStoreBasic(storeprovincecode='130000', leasetimebegin='2019-08-08',
                storename=store_name, leasetimeend='2020-08-08', employeesnum=100, storeregion='新华区', managername=name,
                managerphone=mobile, storeuuid=store_uuid, storecitycode='130100', storeregioncode='130105',
                area='1999', storeaddress='hxhhxhchchhchchcjcjj', storeprovince='河北省', idcardnumber=cardnumber,
                email=email, storecity='石家庄市'))
        Assertion.verity(res['code'], 'S0003')
        Assertion.verity(res['msg'], '门店暂时不能修改')

    @unittest.skip('跳过，businessuuid不验证')
    def test_041_api_78dk_sht_store_modifystoreshtactioniness_businessuuid_error(self):
        """
        修改门店业务信息:修改贴息值
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=15, workpercent='',
            storebusinessproducts=products, businessuuid=MockData.wordAndNum(20), storeuuid=store_uuid))
        Assertion.verity(res['code'], '40000')

    def test_042_api_78dk_sht_store_modifystoreshtactioniness(self):
        """
        修改门店业务信息:修改客户工作占比
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_modifyStorebusiness(discountpercent=15, workpercent='',
            storebusinessproducts=products, businessuuid=businessUuid, storeuuid=store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_043_api_78dk_sht_mm_base_store_querystores(self):
        """
        查看门店
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_queryStores(store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_044_api_78dk_sht_mm_base_store_querystores_none(self):
        """
        查看门店:uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_queryStores(uuid=''))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_045_api_78dk_sht_mm_base_store_querystores_error(self):
        """
        查看门店:
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_queryStores(uuid=MockData.wordAndNum(20)))
        Assertion.verity(res['code'], '10000')

    def test_046_api_78dk_sht_bm_querybills(self):
        """
        查看门店下的订单
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_queryBills(pagesize=10, storeuuid=store_uuid, pagenum=1))
        Assertion.verity(res['code'], '10000')

    def test_047_api_78dk_sht_bm_querybills_uuid_none(self):
        """
        查看门店下的订单:门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_bm_queryBills(pagesize=10, storeuuid='', pagenum=1))
        Assertion.verity(res['code'], '10000')

    def test_048_api_78dk_sht_qrcode_showqrs(self):
        """
        查询二维码
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_qrCode_showQRs(store_uuid))
        Assertion.verity(res['code'], 'S0006')

    def test_049_api_78dk_sht_qrCode_showqrs_none(self):
        """
        查询二维码:merchantuuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_qrCode_showQRs(storeuuid=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '您提交的参数异常')

    def test_050_api_78dk_sht_qrCode_downloadqr_none(self):
        """
        下载二维码
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_qrCode_downloadQR(storeuuid=''))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_051_api_78dk_sht_qrCode_downloadqr(self):
        """
        下载二维码
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_qrCode_downloadQR(storeuuid=store_uuid))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_052_api_78dk_sht_store_querymerchantaccount(self):
        """
        查询该商户被绑定的账号
        :return:
        """
        global merchant_uuid
        merchant_uuid = loginAction.global_dict.get('merchantUuid')
        res = json.loads(
            ShtAction.test_api_78dk_sht_store_queryMerchantAccount(merchantuuid=merchant_uuid, storeuuid=store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_053_api_78dk_sht_store_querymerchantaccount_storeuuid_none(self):
        """
        查询该商户被绑定的账号,门店uuid为空
        :return:
        """
        res = json.loads(
            ShtAction.test_api_78dk_sht_store_queryMerchantAccount(merchantuuid=merchant_uuid, storeuuid=''))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_054_api_78dk_sht_store_querymerchantaccount_merchantuuid_none(self):
        """
        查询该商户被绑定的账号,商户uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_queryMerchantAccount(merchantuuid='', storeuuid=store_uuid))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_055_api_78dk_sht_store_findstorebusiness(self):
        """
        查询门店业务信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_findStorebusiness(storeuuid=store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_056_api_78dk_sht_store_findstorebusiness_none(self):
        """
        查询门店业务信息,门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_findStorebusiness(storeuuid=''))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_057_api_78dk_sht_store_findstorebasic(self):
        """
        查询门店基本信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_findStoreBasic(store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_058_api_78dk_sht_store_findstorebasic_none(self):
        """
        查询门店基本信息，门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_findStoreBasic(storeuuid=''))
        Assertion.verity(res['msg'], '您提交的参数异常')
        Assertion.verity(res['code'], 'S0006')

    def test_059_api_78dk_sht_store_querystorepics(self):
        """
        查询门店证照信息
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_queryStorePics(store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_060_api_78dk_sht_store_querystorepics_none(self):
        """
        查询门店证照信息，门店uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_queryStorePics(storeuuid=''))
        Assertion.verity(res['msg'], '参数有误')
        Assertion.verity(res['code'], 'S0006')

    def test_061_api_78dk_sht_store_querystorelist(self):
        """
        查询门店列表
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_queryStoreList(store_uuid))
        Assertion.verity(res['code'], '10000')

    def test_062_api_78dk_sht_store_querystorelist_none(self):
        """
        查询门店列表，uuid为空
        :return:
        """
        res = json.loads(ShtAction.test_api_78dk_sht_store_queryStoreList(uuid=''))
        Assertion.verity(res['code'], 'S0006')
        Assertion.verity(res['msg'], '您提交的参数异常')
