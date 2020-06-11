#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-08-12 上午 11:00
@Author     : 闫红
@File       : test_003_web_Merchant_two.py
@desc       : 商户管理（门店）自动化测试用例 1.4版本修改及新增
"""

import json
from faker import Factory
from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from hmpt.testAction import WebAction, specialAction
from hmpt.testAction import loginAction

global_dict = loginAction.global_dict
fake = Factory().create('zh_CN')
# 商户名称
merchantname = loginAction.sign + fake.company()
name = fake.name_male() + loginAction.sign
email = loginAction.sign + fake.email()
mobile = '15388188697'
cardnumber = fake.ssn()


class test_003_web_Merchant_two(TestBaseCase):

    def test_001_api_78dk_platform_mm_base_saveMerchant(self):
        """
        新增商户基本信息
        :return:
        """
        channelid = loginAction.global_dict.get('channelid')
        res = json.loads(WebAction.test_api_78dk_platform_mm_base_saveMerchant(
            note='备注', name=merchantname,
            parentmerchantuuid='',
            shortname=merchantname + '商户简称',
            channeluuid=channelid, industryfirst=0,
            city=0,
            industrysecond=0, province=0, repaymentmax=1000, repaymentproportion=0.1))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')
        Assertion.verityContain(res['data'], 'merchantUuid')
        global merchantUuid_del
        merchantUuid_del = res['data']['merchantUuid']
        loginAction.global_dict.set(merchantUuid_del=res['data']['merchantUuid'])

    def test_002_api_78dk_platform_mm_base_legal_saveLegalPerson(self):
        """
        添加法人信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_legal_saveLegalPerson(
            cardnumber=cardnumber,
            channelormerchantuuid=merchantUuid_del,
            legalpersonuuid='', mobile=mobile,
            name=name, effectivetimebegin='',
            effectivetimeend='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_003_api_78dk_platform_mm_base_clear_saveClearingAccount(self):
        """
        为商户添加结算信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_clear_saveClearingAccount(
            accountname=name,
            accountnumber='6011826564542944',
            accountopeningbank='农业银行',
            accounttype='public_accounts',
            branchname='支行名称',
            chamberlainidcard='431081199812097872',
            channelormerchantuuid=merchantUuid_del,
            city='510100', clearingaccountuuid='',
            linenumber='6756765756',
            province='510000', region='510101')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_004_api_78dk_platform_mm_base_business_saveBusinessInfor(self):
        """
        新增机构信息
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_business_saveBusinessInfor(
            channelormerchantuuid=merchantUuid_del, organizationcode="567657675765",
            socialunifiedcreditcode="34534543534", taxregistrationnumber='34543543543', installmentcooperationorgs=[],
            contracttimebegin='', contracttimeend='', merge='yes', specialindustrytimebegin='',
            specialindustrytimeend='', specialindustrylicenseorname='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_005_api_78dk_platform_mm_saveContractImages(self):
        """
        影像资料保存
        :return:
        """
        # merchant_uuid = '9321312cda564b18854d1a6af102048e'
        image_url = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        keys = ["SHYYZZ", "SHFRSFZZ", "SHFRSFZF", "SHFRSFZFSC", "SHZM"]
        images = [{"fileName": '1', "key": key, "merchantUuid": merchantUuid_del, "url": image_url} for key in keys]
        res = json.loads(specialAction.test_api_78dk_platform_mm_saveContractImages(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_006_api_78dk_platform_mm_saveImagesAndChange(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :商户图片资料保存-1.5.2，新增
        """
        global merchantUuid
        merchantUuid = loginAction.global_dict.get('merchantUuid')
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        sysImageKey = ["SHYYZZ", "SHFRSFZZ", "SHFRSFZF", "SHFRSFZFSC", "SHZM"]
        images = [
            {"fileName": '1', 'handleType': 'add', "sysImageKey": imagekey, "merchantUuid": merchantUuid, "key": key}
            for imagekey in sysImageKey]
        res = json.loads(WebAction.test_api_78dk_platform_mm_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_007_api_78dk_platform_mm_viewImageByMerchantUuid(self):
        """
        Time       :2019-10-09
        author     : 闫红
        desc       :查询商户图片-v1.5.2，merchantuuid正常
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageByMerchantUuid(uid=merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global dict_list
        dict_list = dict()
        for k in json.loads(res)['data']:
            dict_list[k['sysImageKey']] = k['merchantImageUuid']
        print(dict_list)

    def test_008_api_78dk_platform_mm_saveImagesAndChange(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :商户图片资料保存-1.5.2,编辑
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        images = [{"fileName": '1', 'handleType': 'normal', "sysImageKey": imagekey, 'oldImageUuid': oldImageUuid,
                   "merchantUuid": merchantUuid, "key": key} for imagekey, oldImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_009_api_78dk_platform_mm_saveImagesAndChange(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :商户图片资料保存-1.5.2,未操作
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        # sysImageKey = ["SHYYZZ", "SHFRSFZZ", "SHFRSFZF", "SHFRSFZFSC", "SHZM"]
        images = [{"fileName": '1', 'handleType': 'normal', "sysImageKey": imagekey, 'oldImageUuid': oldImageUuid,
                   "merchantUuid": merchantUuid, "key": key} for imagekey, oldImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_010_api_78dk_platform_mm_saveImagesAndChange(self):
        """
        Time       :2019-09-29
        author     : 闫红
        desc       :商户图片资料保存-1.5.2,删除
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        images = [{"fileName": '1', 'handleType': 'del', "sysImageKey": imagekey, 'oldImageUuid': oldImageUuid,
                   "merchantUuid": merchantUuid, "key": key} for imagekey, oldImageUuid in dict_list.items()]
        res = json.loads(WebAction.test_api_78dk_platform_mm_saveImagesAndChange(images))
        Assertion.verity(res['code'], '10000')
        Assertion.verity(res['msg'], '成功')

    def test_011_api_78dk_platform_mm_bd_saveBDMerchant(self):
        """
        新增商户BD信息
        :return:
        """
        bdinfouuid = loginAction.global_dict.get('bdinfouuid')
        bd_name = loginAction.global_dict.get('bd_name')
        res = WebAction.test_api_78dk_platform_mm_bd_saveBDMerchant(bdinfouuid=bdinfouuid,
                                                                    merchantuuid=merchantUuid_del, name=bd_name,
                                                                    remark='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_012_api_78dk_platform_mm_base_addOrUpdateBond(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :新增或者编辑商户保证金模块-v1.5.2
        """
        res = WebAction.test_api_78dk_platform_mm_base_addOrUpdateBond(
            merchantuuid=merchantUuid_del,
            payamount='5000', paydate='2019-10-02',
            poolamount='1000', pooldate='2019-10-02',
            returnamount='1000',
            returndate='2019-10-02', deductionamount='1000',
            deductiondate='2019-10-02')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_013_api_78dk_platform_mm_base_findBond(self):
        """
        Time       :2019-09-30
        author     : 闫红
        desc       :商户保证金缴纳记录查询-v1.5.2
        """
        res = WebAction.test_api_78dk_platform_mm_base_findBond(merchantuuid=merchantUuid_del, pagecurrent=1,
                                                                pagesize=10)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_014_api_78dk_platform_mm_examine_createTemporaryCode(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 生成临时编码-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_examine_createTemporaryCode(uid=merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_015_api_78dk_platform_mm_viewImageRoleList_type_home(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 影像资料查询-v1.4,查询家装分期
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageRoleList(uid=merchantUuid,
                                                                    subdivisiontype='subdivision_type_home_installment')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_016_api_78dk_platform_mm_viewImageRoleList_type_earnest(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 影像资料查询-v1.4,查询定金分期
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageRoleList(
            uid=merchantUuid,
            subdivisiontype='subdivision_type_earnest_installment')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_017_api_78dk_platform_mm_viewImageRoleList_all(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 影像资料查询-v1.4,分期类型为空
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageRoleList(uid=merchantUuid,
                                                                    subdivisiontype='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_018_api_78dk_platform_mm_viewImageRoleList_not_exist(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 影像资料查询-v1.4,商户为空
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageRoleList(uid='',
                                                                    subdivisiontype='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], 'ChannelOrMerchantUuid不能为空!')

    def test_019_api_78dk_platform_mm_base_bd_listDbLogs(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 查询商户业BD 操作日志-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_base_bd_listDbLogs(uid=merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_020_api_78dk_platform_mm_base_bd_listDbLogs_is_null(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 查询商户业BD 操作日志-v1.4,商户为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_bd_listDbLogs(uid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_021_api_78dk_platform_mm_base_bd_listDbLogs_not_exist(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 查询商户业BD 操作日志-v1.4,商户不存在
        """
        res = WebAction.test_api_78dk_platform_mm_base_bd_listDbLogs(uid=-1)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_022_api_78dk_platform_mm_base_deleteMerchant(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 基本信息-删除-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_base_deleteMerchant(uid=merchantUuid_del)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_023_api_78dk_platform_mm_base_deleteMerchant_is_null(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 基本信息-删除-v1.4,商户为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_deleteMerchant(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verityContain(json.loads(res)['msg'], '参数异常')

    def test_024_api_78dk_platform_mm_base_deleteMerchant_not_exist(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 基本信息-删除-v1.4,不存在的商户
        """
        res = WebAction.test_api_78dk_platform_mm_base_deleteMerchant(uid=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verityContain(json.loads(res)['msg'], '商户Uuid不存在')

    def test_025_api_78dk_platform_mm_examine_createTemporaryCode(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 生成临时编码-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_examine_createTemporaryCode(uid=merchantUuid_del)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '只有审核通过的商户才能生成临时编码')

    def test_026_api_78dk_platform_mm_examine_createTemporaryCode_is_null(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 生成临时编码-v1.4,商户为空
        """
        res = WebAction.test_api_78dk_platform_mm_examine_createTemporaryCode(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '您提交的参数异常')

    def test_027_api_78dk_platform_mm_examine_createTemporaryCode_not_exist(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       : 生成临时编码-v1.4,商户不存在
        """
        res = WebAction.test_api_78dk_platform_mm_examine_createTemporaryCode(uid=-1)
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '只有审核通过的商户才能生成临时编码')

    def test_028_api_78dk_platform_mm_base_viewIndustryCategory(self):
        """
        Time       :2019-08-12
        author     : 闫红
        desc       :行业分类查询-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_base_viewIndustryCategory()
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_029_api_78dk_platform_mm_base_saveStoreBusiness(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正常新增或修改-v1.4
        """
        global store_uuid
        store_uuid = global_dict.get('store_uuid')
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent='',
                                                                               list=[], storeuuid=store_uuid,
                                                                               workpercent='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_030_api_78dk_platform_mm_base_saveStoreBusiness_discountpercentNONE(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正新增或修改-v1.4——贴息占比为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent='',
                                                                               list=[], storeuuid=store_uuid,
                                                                               workpercent='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_031_api_78dk_platform_mm_base_aveStoreBusiness_listNONE(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正新增或修改-v1.4——list比为空
        """

        res = WebAction.test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent='',
                                                                               list=[], storeuuid=store_uuid,
                                                                               workpercent='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_032_api_78dk_platform_mm_base_saveStoreBusiness_uidNONE(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正新增或修改-v1.4——uuid比为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent='',
                                                                               list=[], storeuuid='', workpercent='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_033_api_78dk_platform_mm_base_saveStoreBusiness_workpercentNONE(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正新增或修改-v1.4——workpercent比为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_saveStoreBusiness(discountpercent='',
                                                                               list=[], storeuuid=store_uuid,
                                                                               workpercent='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_034_api_78dk_platform_mm_base_addStoreBusiness_viewStoreBusiness(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-正常查询-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreBusiness(uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        # Assertion.verityContain(json.loads(res)['data'],'discountPercent')
        # Assertion.verityContain(json.loads(res)['data'], 'list')
        # Assertion.verityContain(json.loads(res)['data'], 'workPercent')
        # Assertion.verityContain(json.loads(res)['data']['list'], 'amount')
        # Assertion.verityContain(json.loads(res)['data']['list'], 'cycle')
        # Assertion.verityContain(json.loads(res)['data']['list'], 'productName')
        # Assertion.verityContain(json.loads(res)['data']['list'], 'productUid')

    def test_035_api_78dk_platform_mm_base_addStoreBusiness_viewStoreBusiness_NONE(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店业务信息-uuid为空查询-v1.4
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreBusiness(uid='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_036_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_pass(self):
        """
                Time       :2019-08-14
                author     : songchao
                desc       :门店审核-v1.4-正常通过审核
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_storeExamine(ispass='pass', message='阿达',
                                                                          uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_037_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_fail(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店审核-v1.4-正常失败审核
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_storeExamine(ispass='fail', message='阿达',
                                                                          uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_038_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_isPass_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店审核-v1.4-isPass为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_storeExamine(ispass='', message='阿达',
                                                                          uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_039_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_message_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店审核-v1.4-message为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_storeExamine(ispass='pass', message='',
                                                                          uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_040_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uid_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店审核-v1.4-uid为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_storeExamine(ispass='pass', message='1231', uid='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_041_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uploadImageRoleList(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料上传-v1.4
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        sysImageKeys = ["MDFZRSFZZM", "MDFZRSFZFM", "MDFZRSFZSC", "MDWBHJZ", "MDNBHJZ", "MDQTLOGO", "MDZLHT",
                        "MDPXXY"]
        images = [{"fileName": '1', "key": key, "storeUuid": store_uuid, "handleType": "add",
                   "oldImageUuid": '', "sysImageKey": sysImageKey} for sysImageKey in sysImageKeys]
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_042_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uploadImageRoleList_fileName_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料异常上传-v1.4_fileName为空
        """
        images = {"fileName": '', "key": "key", "merchantUuid": "", "url": "image_url"}
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_043_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uploadImageRoleList_key_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料异常上传-v1.4_key为空
        """
        images = {"fileName": '1', "key": "", "merchantUuid": "123", "url": "image_url"}
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_044_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uploadImageRoleList_uid_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料异常上传-v1.4_uid为空
        """
        images = {"fileName": '1', "key": "key", "merchantUuid": "", "url": "image_url"}
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_045_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_uploadImageRoleList_url_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料异常上传-v1.4_url为空
        """
        images = {"fileName": '1', "key": "key", "merchantUuid": "123", "url": ""}
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_046_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_viewImageRoleList(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料查询-v1.4_正常
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewImageRoleList(uid=store_uuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
        global image_dict
        image_dict = {r['storeImageUuid']: r['sysImageKey'] for r in json.loads(res)['data']}

    def test_047_api_78dk_platform_mm_base_store_saveImagesAndChange_edit(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料上传-v1.4
        """
        key = "FjHpyILVVxjHksSyGsVKmQlnI01T"
        images = [{"fileName": '1', "key": key, "storeUuid": store_uuid, "handleType": "edit",
                   "oldImageUuid": storeImageUuid, "sysImageKey": sysImageKey}
                  for storeImageUuid, sysImageKey in image_dict.items()]
        res = WebAction.test_api_78dk_platform_mm_base_store_saveImagesAndChange(images=images)
        Assertion.verity(json.loads(res)['code'], '10000')

    def test_048_api_78dk_platform_mm_base_addStoreBusiness_storeExamine_viewImageRoleList_none(self):
        """
        Time       :2019-08-14
        author     : songchao
        desc       :门店影像资料查询-v1.4_uuid为空
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewImageRoleList(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')

    def test_049_api_78dk_platform_mm_base_store_viewStoreList_name_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='normal',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_050_api_78dk_platform_mm_base_store_viewStoreList_name_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name=fake.company(),
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='normal',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_051_api_78dk_platform_mm_base_store_viewStoreList_uid_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid='', auditstate='pass',
            freezestate='normal', managername='',
            sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_052_api_78dk_platform_mm_base_store_viewStoreList_uid_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid='123', auditstate='pass',
            freezestate='normal', managername='',
            sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_053_api_78dk_platform_mm_base_store_viewStoreList_auditstate_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='123', freezestate='normal',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_054_api_78dk_platform_mm_base_store_viewStoreList_auditstate_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid, auditstate='',
            freezestate='normal', managername='',
            sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_055_api_78dk_platform_mm_base_store_viewStoreList_freezestate_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='123',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_056_api_78dk_platform_mm_base_store_viewStoreList_freezestate_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_057_api_78dk_platform_mm_base_store_viewStoreList_sign_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='normal',
            managername='', sign='123')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_058_api_78dk_platform_mm_base_store_viewStoreList_sign_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='normal',
            managername='', sign='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_059_api_78dk_platform_mm_base_store_viewStoreList_managername_not_exits(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='normal',
            managername=fake.company(),
            sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_060_api_78dk_platform_mm_base_store_viewStoreList_auditstate_pending_review(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pending_review',
            freezestate='normal', managername='',
            sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_061_api_78dk_platform_mm_base_store_viewStoreList_auditstate_imperfect(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='imperfect', freezestate='normal',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_062_api_78dk_platform_mm_base_store_viewStoreList_auditstate_fail(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='fail', freezestate='normal',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_063_api_78dk_platform_mm_base_store_viewStoreList_freezestate_freeze(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='freeze',
            managername='', sign='overdue')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_064_api_78dk_platform_mm_base_store_viewStoreList_sign_urgent(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='freeze',
            managername='', sign='urgent')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_065_api_78dk_platform_mm_base_store_viewStoreList_sign_expire(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid,
            auditstate='pass', freezestate='freeze',
            managername='', sign='expire')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_066_api_78dk_platform_mm_base_store_viewStoreList_all_none(self):
        """
        查询商户门店列表
        :return:
        """
        res = WebAction.test_api_78dk_platform_mm_base_store_viewStoreList(
            pagecurrent=1, name='',
            pagesize=10, uid=store_uuid, auditstate='',
            freezestate='', managername='', sign='')
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')

    def test_067_api_78dk_platform_mm_viewImageByMerchantUuid_not_exist(self):
        """
        Time       :2019-10-09
        author     : 闫红
        desc       :查询商户图片-v1.5.2,merchantuuid为空
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageByMerchantUuid(uid='')
        Assertion.verity(json.loads(res)['code'], '20000')
        Assertion.verity(json.loads(res)['msg'], '商户uuid不能为空')

    def test_068_api_78dk_platform_mm_viewImageByMerchantUuid_is_null(self):
        """
        Time       :2019-10-09
        author     : 闫红
        desc       :查询商户图片-v1.5.2，merchantuuid不存在
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageByMerchantUuid(uid=-1)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verityContain(json.loads(res)['msg'], '成功')

    def test_069_api_78dk_platform_mm_viewImageByMerchantUuid(self):
        """
        Time       :2019-10-09
        author     : 闫红
        desc       :查询商户图片-v1.5.2，merchantuuid正常
        """
        res = WebAction.test_api_78dk_platform_mm_viewImageByMerchantUuid(uid=merchantUuid)
        Assertion.verity(json.loads(res)['code'], '10000')
        Assertion.verity(json.loads(res)['msg'], '成功')
