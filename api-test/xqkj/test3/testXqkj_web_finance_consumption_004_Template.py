#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-06-05 上午 11:25
@Author     : 罗林
@File       : testXqkj_web_finance_consumption_004_Template.py
@desc       :  进件配置流程自动化测试用例
"""

import json

from faker import Faker

from common.myCommon import Assertion
from common.myCommon.TestBaseCase import TestBaseCase
from xqkj.query import xqkj_query
from xqkj.testAction import Xqkj_web_finance_consumptionAction as PlatformAction
from xqkj.testAction import loginAction

global_dict = loginAction.global_dict
fake = Faker("zh_CN")

template_name = loginAction.sign + fake.name_male()
del_template_name = loginAction.sign + fake.name_male()


class testXqkj_web_finance_consumption_004_Template(TestBaseCase):
    def test_001_api_78dk_platform_tm_incoming_addOrEditTemplate_none_name(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 添加或者编辑进件模板(新)名称为空
        """
        global sysdata
        sysdata = xqkj_query.get_sysdata()
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
            remark='', sysdata=sysdata, templatename='', templatetype='template_type_incoming_parts',
            producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "TemplateName 不能为空!")

    def test_002_api_78dk_platform_tm_incoming_addOrEditTemplate_256_name(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 添加或者编辑进件模板(新)名称长度256
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
            remark='', sysdata=sysdata, templatename=''.join(fake.words(nb=128)),
            templatetype='template_type_incoming_parts', producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "添加或编辑进件模板发生错误!")

    def test_003_api_78dk_platform_tm_incoming_addOrEditTemplate_none_sysdata(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 添加或者编辑进件模板(新)
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
            remark='', sysdata='', templatename=template_name, templatetype='template_type_incoming_parts',
            producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "系统发生内部异常，请稍候再试")

    def test_004_api_78dk_platform_tm_incoming_addOrEditTemplate(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 添加或者编辑进件模板(新)
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
            remark='', sysdata=sysdata, templatename=template_name, templatetype='template_type_incoming_parts',
            producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data']['productTemplateUuid'])
        global productTemplateUuid
        productTemplateUuid = json.loads(rs)['data']['productTemplateUuid']

    def test_005_api_78dk_platform_tm_incoming_templateList_name_none(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板查询列表
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateList(name='', pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'pageCurrent')
        Assertion.verityContain(json.loads(rs)['data'], 'dataList')
        Assertion.verityContain(json.loads(rs)['data'], 'pageSize')

    def test_006_api_78dk_platform_tm_incoming_templateList_name_not_exits(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板查询列表
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateList(
            name=''.join(fake.words(nb=128)), pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'dataList')

    def test_007_api_78dk_platform_tm_incoming_templateList(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板查询列表
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateList(
            name=template_name, pagecurrent=1, pagesize=10)
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'pageCurrent')
        Assertion.verityContain(json.loads(rs)['data'], 'dataList')
        Assertion.verityContain(json.loads(rs)['data'], 'pageSize')
        Assertion.verityNotNone(json.loads(rs)['data']['dataList'])
        Assertion.verityContain(json.loads(rs)['data']['dataList'], 'created')
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['templateName'], template_name)
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['templateType'], 'template_type_incoming_parts')
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['productTemplateUuid'], productTemplateUuid)
    #
    # def test_008_api_78dk_platform_tm_incoming_addOrEditTemplate_edit_none_name(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 添加或者编辑进件模板(新)名称为空
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
    #         remark='', sysdata=sysdata, templatename='', templatetype='template_type_incoming_parts',
    #         producttemplateuuid=productTemplateUuid)
    #     Assertion.verity(json.loads(rs)['code'], "20000")
    #     Assertion.verity(json.loads(rs)['msg'], "TemplateName 不能为空!")
    #
    # def test_009_api_78dk_platform_tm_incoming_addOrEditTemplate_edit_256_name(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 添加或者编辑进件模板(新)名称长度256
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
    #         remark='', sysdata=sysdata, templatename=''.join(fake.words(nb=128)),
    #         templatetype='template_type_incoming_parts', producttemplateuuid=productTemplateUuid)
    #     Assertion.verity(json.loads(rs)['code'], "20000")
    #     Assertion.verity(json.loads(rs)['msg'], "添加或编辑进件模板发生错误!")
    #
    # def test_010_api_78dk_platform_tm_incoming_addOrEditTemplate_edit_none_sysdata(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 添加或者编辑进件模板(新)
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
    #         remark='', sysdata='', templatename=template_name, templatetype='template_type_incoming_parts',
    #         producttemplateuuid=productTemplateUuid)
    #     Assertion.verity(json.loads(rs)['code'], "20000")
    #     Assertion.verity(json.loads(rs)['msg'], "系统发生内部异常，请稍候再试")
    #
    # def test_011_api_78dk_platform_tm_incoming_addOrEditTemplate_edit(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 添加或者编辑进件模板(新)
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
    #         remark='', sysdata=sysdata, templatename=template_name, templatetype='template_type_incoming_parts',
    #         producttemplateuuid=productTemplateUuid)
    #     Assertion.verity(json.loads(rs)['code'], "10000")
    #     Assertion.verity(json.loads(rs)['msg'], "成功")
    #     Assertion.verityNotNone(json.loads(rs)['data'])

    def test_012_api_78dk_platform_tm_incoming_templateDetails_none(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板详情查询
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateDetails('')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "ProductTemplateUuid 不能为空!")

    def test_013_api_78dk_platform_tm_incoming_templateDetails_not_exits(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板详情查询
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateDetails(fake.ean8())
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "ProductTemplateUuid 不合法!")

    def test_014_api_78dk_platform_tm_incoming_templateDetails(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板详情查询
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateDetails(productTemplateUuid)
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'created')
        Assertion.verityNotNone(json.loads(rs)['data']['sysData'])
        Assertion.verityContain(json.loads(rs)['data']['sysData'], 'id')
        Assertion.verityContain(json.loads(rs)['data']['sysData'], 'parentId')
        Assertion.verityContain(json.loads(rs)['data']['sysData'], 'typeName')
        Assertion.verity(json.loads(rs)['data']['productTemplateUuid'], productTemplateUuid)
        Assertion.verity(json.loads(rs)['data']['remark'], '')
        Assertion.verity(json.loads(rs)['data']['templateName'], template_name)
        Assertion.verity(json.loads(rs)['data']['templateType'], 'template_type_incoming_parts')

    def test_015_api_78dk_platform_tm_incoming_findTemplateDictionaries(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 查询所有模板配置字典
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_findTemplateDictionaries()
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'id')
        Assertion.verityContain(json.loads(rs)['data'], 'parentId')
        Assertion.verityContain(json.loads(rs)['data'], 'typeName')

    def test_016_api_78dk_platform_tm_incoming_findProductByTemplate_none(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 查询模板关联产品
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_findProductByTemplate(
            pagecurrent=1, pagesize=10, producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "ProductTemplateUuid 不能为空!")

    def test_017_api_78dk_platform_tm_incoming_findProductByTemplate_not_exits(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 查询模板关联产品
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_findProductByTemplate(
            pagecurrent=1, pagesize=10, producttemplateuuid=fake.ean8())
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "ProductTemplateUuid 不合法!")

    def test_018_api_78dk_platform_tm_incoming_findProductByTemplate(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 查询模板关联产品
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_findProductByTemplate(
            pagecurrent=1, pagesize=10, producttemplateuuid=productTemplateUuid)
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityContain(json.loads(rs)['data'], 'dataList')

    def test_019_api_78dk_platform_tm_incoming_delTemplate_none(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 删除进件模板
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "productTemplateUuid 不能为空!")

    def test_020_api_78dk_platform_tm_incoming_delTemplate_not_exits(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 删除进件模板
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid=fake.ean8())
        Assertion.verity(json.loads(rs)['code'], "20000")
        Assertion.verity(json.loads(rs)['msg'], "productTemplateUuid 不合法!")

    def test_021_api_78dk_platform_tm_incoming_addOrEditTemplate_two(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 添加或者编辑进件模板(新)
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_addOrEditTemplate(
            remark='', sysdata=sysdata, templatename=del_template_name, templatetype='template_type_incoming_parts',
            producttemplateuuid='')
        Assertion.verity(json.loads(rs)['code'], "10000")
        Assertion.verity(json.loads(rs)['msg'], "成功")
        Assertion.verityNotNone(json.loads(rs)['data']['productTemplateUuid'])
        global del_template_id
        del_template_id = json.loads(rs)['data']['productTemplateUuid']

    def test_022_api_78dk_platform_tm_incoming_templateList_two(self):
        """
        Time       :2019-06-05
        author     : 罗林
        desc       : 模板查询列表
        """
        rs = PlatformAction.test_api_78dk_platform_tm_incoming_templateList(
            name=del_template_name, pagecurrent=1, pagesize=10)
        Assertion.verityNotNone(json.loads(rs)['data'])
        Assertion.verityContain(json.loads(rs)['data'], 'pageCurrent')
        Assertion.verityContain(json.loads(rs)['data'], 'dataList')
        Assertion.verityContain(json.loads(rs)['data'], 'pageSize')
        Assertion.verityNotNone(json.loads(rs)['data']['dataList'])
        Assertion.verityContain(json.loads(rs)['data']['dataList'], 'created')
        Assertion.verityContain(json.loads(rs)['data']['dataList'], 'productTemplateUuid')
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['templateName'], del_template_name)
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['templateType'], 'template_type_incoming_parts')
        Assertion.verity(json.loads(rs)['data']['dataList'][0]['productTemplateUuid'], del_template_id)

    # def test_023_api_78dk_platform_tm_incoming_delTemplate_none(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 删除进件模板
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid='')
    #     Assertion.verity(json.loads(rs)['code'], "20000")
    #     Assertion.verity(json.loads(rs)['msg'], "productTemplateUuid 不能为空!")
    # 
    # def test_024_api_78dk_platform_tm_incoming_delTemplate_not_exits(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 删除进件模板
    #     """
    #     del_template_id = ''
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid=fake.ean8())
    #     Assertion.verity(json.loads(rs)['code'], "20000")
    #     Assertion.verity(json.loads(rs)['msg'], "productTemplateUuid 不合法!")
    #
    # def test_025_api_78dk_platform_tm_incoming_delTemplate(self):
    #     """
    #     Time       :2019-06-05
    #     author     : 罗林
    #     desc       : 删除进件模板
    #     """
    #     rs = PlatformAction.test_api_78dk_platform_tm_incoming_delTemplate(producttemplateuuid=del_template_id)
    #     Assertion.verity(json.loads(rs)['code'], "10000")
    #     Assertion.verity(json.loads(rs)['msg'], "成功")
