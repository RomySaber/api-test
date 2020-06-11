#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-03-01 下午 5:27
@File       : testTemplate.py
@desc       :
"""

from common.myCommon.TestBaseCase import TestBaseCase
from finance.testAction import FinanceAction
import json
from common.myCommon import Assertion
from finance.mysqlQuery import FinanceSql


# 保证每条case可持续性
# 类名要求：test+模块名称(首字母大写)
class testTemplate(TestBaseCase):
    # 用例名称要求：以test_3位数字_用例名称
    def test_001_testTemplate(self):
        """
        Time       :该条case编写时间
        author     : XXX
        desc       :该条case中的描述：例如实现XXX功能
        """
        r=json.loads(FinanceAction.test_warnhb_getThreshold())
        Assertion.verity(r['code'],'F2000','断言code')
        Assertion.verity(r['message'],'请求成功','断言message')

    def test_002_XXX(self):
        pass


    def test_001_devices(self):
        """
        Time       :2019-03-20 上午 10:27
        author     : 闫红
        desc       :实现设备相关接口，新增设备、编辑设备、查看设备详情、获取设备类型、获取设备列表、删除设备
        """
        r1 = json.loads(FinanceAction.test_device_save('','0045',1,'GT02D','ddwire10000','1064847072526','2019-02-27'))
        Assertion.verity(r1['code'],'F2000','断言新增设备')
        gps_id = FinanceSql.get_device_id('ddwire10000')
        r4 = json.loads(FinanceAction.test_device_update(gps_id,'0045',1,'GT02D','ddwire10000','1064847072527','2019-02-28'))
        Assertion.verity(r4['code'],'F2000','断言修改设备')
        r5 = json.loads(FinanceAction.test_device_getLowerOrg())
        r6 = json.loads(FinanceAction.test_device_getDeviceMoudel(1))
        Assertion.verityContain(r6['data'][0]['dictCode'],'GT02D','断言有线型号包含GT02D')
        r7 = json.loads(FinanceAction.test_device_getDeviceType())
        Assertion.verity(r7['data'][0]['dictCode'],'1','断言dictCode')
        Assertion.verity(r7['data'][0]['dictName'],'有线','断言dictName')
        Assertion.verity(r7['data'][1]['dictCode'],'0','断言dictCode')
        Assertion.verity(r7['data'][1]['dictName'],'无线','断言dictName')
        r8 = json.loads(FinanceAction.test_device_detail(gps_id))
        Assertion.verity(r8['data']['deviceCode'],'ddwire10000','断言设备号')
        Assertion.verity(r8['data']['id'],gps_id[0][0],'断言id')
        r2 = json.loads(FinanceAction.test_device_delete(gps_id))
        Assertion.verityContain(r2['message'],'成功','断言删除')
        r9 = json.loads(FinanceAction.test_device_list('ddwire10000',1,10))
        Assertion.verity(r9['data']['pageNum'],1,'断言页码')
        Assertion.verity(r9['data']['pageSize'],10,'断言条码')
        Assertion.verityNone(r9['data']['record'],'断言删除后应该为空')
