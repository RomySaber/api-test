#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-28 下午 2:49
@Author     : 罗林
@File       : testEasyloan_web_004_other.py
@desc       : 财务管理,报表导出,产品管理测试用例
"""

import json

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from easyloan.query import easyloan_query as eq
from easyloan.testAction import Easyloan_webAction as ew, loginAction as la

product_name = 'product' + la.sign


class testEasyloan_web_004_other(TestBaseCase):
    def test_001_api_78dk_web_finance_financePage(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 财务管理分页
        """
        rs = ew.test_api_78dk_web_finance_financePage(begindate='', beginloanamount='', contractno='', currentpage=1,
                                                      enddate='', endloanamount='', ordermainstate='', orderno='',
                                                      pagesize=10, storename='', username='', years='')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "currentPage")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "contractNo")
        ass.verityContain(json.loads(rs)['data'], "totalCount")

    def test_002_api_78dk_web_finance_queryLoanFinance(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 财务管理详情
        """
        uuid = ''
        rs = ew.test_api_78dk_web_finance_queryLoanFinance(uuid=uuid)
        ass.verity(json.loads(rs)['code'], "S0001")
        ass.verity(json.loads(rs)['msg'], "请勿非法提交数据")

    def test_003_api_78dk_web_finance_queryLoanFinance(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 财务管理详情
        """
        uuid = eq.get_info('loan_order', 'loan_order_uuid')[0]
        rs = ew.test_api_78dk_web_finance_queryLoanFinance(uuid=uuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_004_api_78dk_web_finance_addLoanFinance(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 财务详情保存
        """
        rs = ew.test_api_78dk_web_finance_addLoanFinance(bankbranch='', loantype='', moenyuse='', uuid='')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_005_api_78dk_web_print_printLink(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 报表导出
        """
        rs = ew.test_api_78dk_web_print_printLink(bigendate='', enddate='', loanamount='', ordermainstate='',
                                                  storename='', usrename='')
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "herf")

    def test_006_api_78dk_web_print_printPage(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 报表导出
        """
        rs = ew.test_api_78dk_web_print_printPage(bigendate='', enddate='', loanamount='', ordermainstate='',
                                                  storename='', usrename='', currentpage=1, pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "loanTerm")
        ass.verityContain(json.loads(rs)['data'], "currentPage")
        ass.verityContain(json.loads(rs)['data'], "dataList")
        ass.verityContain(json.loads(rs)['data'], "totalCount")
        ass.verityContain(json.loads(rs)['data'], "totalPage")
        ass.verityContain(json.loads(rs)['data'], "replayType")

    def test_007_api_78dk_web_org_queryOrgMd(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 门店获取
        """
        rs = ew.test_api_78dk_web_org_queryOrgMd()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "code")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(type(json.loads(rs)['data']), "list")

    def test_008_api_78dk_web_product_addProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 产品-添加(v1.0.4) - 新增
        """
        productDetailConfigList = [{"period": 12, "rate": 0.01}]
        rs = ew.test_api_78dk_web_product_addProduct(
            repaymentmethod='HKFS0001', minquota=100, productdetailconfiglist=productDetailConfigList,
            repaymentdatetype='0', channelfee=10, serverfee=1, controlserverfee=10, minpenaltyfee=1,
            secondhalfofthemonth=25, penaltyrate=0.01, maxquota=10000, name=product_name, producttype='JKFS0001',
            overduepenaltyrate=0.02, firsthalfofthemonth=10, middlehalfofthemonth=15, productdetailuuid='')
        ass.verity(json.loads(rs)['code'], "10000")

    def test_009_api_78dk_web_product_addProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 产品-添加(v1.0.4) - 编辑
        """
        uuid = eq.get_info('product_detail', 'product_detail_uuid', 'name="{}"'.format(product_name))[0]
        productDetailConfigList = [{"period": 12, "rate": 0.01}]
        rs = ew.test_api_78dk_web_product_addProduct(
            repaymentmethod='HKFS0002', minquota=100, productdetailconfiglist=productDetailConfigList,
            repaymentdatetype='0', channelfee=10, serverfee=1, controlserverfee=10, minpenaltyfee=1,
            secondhalfofthemonth=25, penaltyrate=0.01, maxquota=10000, name=product_name, producttype='JKFS0002',
            overduepenaltyrate=0.02, firsthalfofthemonth=10, middlehalfofthemonth=15, productdetailuuid=uuid)
        ass.verity(json.loads(rs)['code'], "10000")

    def test_010_update_product_state(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 更新产品状态
        """
        eq.update_info('product_detail', 'product_state=0,state=0', 'name="{}"'.format(product_name))

    def test_011_api_78dk_web_product_enableOrDisableProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 产品-禁用
        """
        uuid = eq.get_info('product_detail', 'product_detail_uuid', 'name="{}"'.format(product_name))[0]
        rs = ew.test_api_78dk_web_product_enableOrDisableProduct(productdetailuuid=uuid, productstate=1)
        ass.verity(json.loads(rs)['code'], "10000")
        productstate = eq.get_info('product_detail', 'product_state', 'product_detail_uuid="{}"'.format(uuid))[0]
        ass.verity(productstate, "1", "产品状态断言")

    def test_012_api_78dk_web_product_enableOrDisableProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 产品-启用
        """
        uuid = eq.get_info('product_detail', 'product_detail_uuid', 'name="{}"'.format(product_name))[0]
        rs = ew.test_api_78dk_web_product_enableOrDisableProduct(productdetailuuid=uuid, productstate=0)
        ass.verity(json.loads(rs)['code'], "10000")
        productstate = eq.get_info('product_detail', 'product_state', 'product_detail_uuid="{}"'.format(uuid))[0]
        ass.verity(productstate, "0", "产品状态断言")

    def test_013_api_78dk_web_product_queryProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 产品-详情
        """
        uuid = eq.get_info('product_detail', 'product_detail_uuid', 'name="{}"'.format(product_name))[0]
        rs = ew.test_api_78dk_web_product_queryProduct(productdetailuuid=uuid)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "channelFee")
        ass.verityContain(json.loads(rs)['data'], "firstHalfOfTheMonth")
        ass.verityContain(json.loads(rs)['data'], "middleHalfOfTheMonth")
        ass.verityContain(json.loads(rs)['data'], "overduePenaltyRate")
        ass.verityContain(json.loads(rs)['data'], "repaymentDateType")

    def test_014_api_78dk_web_product_queryProductList(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 分页查询
        """
        rs = ew.test_api_78dk_web_product_queryProductList(producttype='', name='', currentpage=1, repaymentmethod='',
                                                           pagesize=10)
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "channelFee")
        ass.verityContain(json.loads(rs)['data'], "firstHalfOfTheMonth")
        ass.verityContain(json.loads(rs)['data'], "middleHalfOfTheMonth")
        ass.verityContain(json.loads(rs)['data'], "overduePenaltyRate")
        ass.verityContain(json.loads(rs)['data'], "repaymentDateType")

    def test_015_api_78dk_web_product_getTotalProduct(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 获取产品下拉列表
        """
        rs = ew.test_api_78dk_web_product_getTotalProduct()
        ass.verity(json.loads(rs)['code'], "10000")
        ass.verityContain(json.loads(rs)['data'], "name")
        ass.verityContain(json.loads(rs)['data'], "uuid")

    def test_016_delete_product(self):
        """
          Time       :2019-04-28
          author     : 罗林
          desc       : 获取产品下拉列表
        """
        uuid = eq.get_info('product_detail', 'product_detail_uuid', 'name="{}"'.format(product_name))[0]
        eq.delete_info('product_detail', 'name="{}"'.format(product_name))
        eq.delete_info('product_detail_config', 'product_detail_uuid="{}"'.format(uuid))
