#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-09 下午 2:59
@Author     : 罗林
@File       : testJtlMachineReview.py
@desc       : 金螳螂机审
"""
import json

from common.myCommon import Assertion as ass
from common.myCommon.TestBaseCase import TestBaseCase
from machineReview.testAction import JtlmachinereviewAction as jtl


class testJtlMachineReview(TestBaseCase):

    def test_001_risk_system(self):
        risk_system_datas = "{\"contract_no\":\"2019040811045722840960\",\"immediate_family_name\":\"嗯\",\"td_json\":\"{\\\"data\\\":{\\\"final_score\\\":69,\\\"risk_items\\\":[{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"namelist_hit_details\\\":[{\\\"hit_type_displayname\\\":\\\"借款人身份证\\\",\\\"fraud_type\\\":\\\"异常提现、异常借款\\\",\\\"description\\\":\\\"验证匹配字段是否在欺诈灰名单中\\\",\\\"type\\\":\\\"grey_list\\\"}],\\\"fraud_type\\\":\\\"异常提现、异常借款\\\"},\\\"item_id\\\":989216,\\\"item_name\\\":\\\"身份证命中低风险关注名单\\\",\\\"group\\\":\\\"风险信息扫描\\\"},{\\\"risk_level\\\":\\\"medium\\\",\\\"item_detail\\\":{\\\"namelist_hit_details\\\":[{\\\"hit_type_displayname\\\":\\\"借款人手机\\\",\\\"fraud_type\\\":\\\"异常登录\\\",\\\"description\\\":\\\"验证匹配字段是否在欺诈灰名单中\\\",\\\"type\\\":\\\"grey_list\\\"}],\\\"fraud_type\\\":\\\"异常登录\\\"},\\\"item_id\\\":989236,\\\"item_name\\\":\\\"手机号命中中风险关注名单\\\",\\\"group\\\":\\\"风险信息扫描\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"namelist_hit_details\\\":[{\\\"hit_type_displayname\\\":\\\"借款人手机\\\",\\\"fraud_type\\\":\\\"异常提现、作弊行为\\\",\\\"description\\\":\\\"验证匹配字段是否在欺诈灰名单中\\\",\\\"type\\\":\\\"grey_list\\\"}],\\\"fraud_type\\\":\\\"异常提现、作弊行为\\\"},\\\"item_id\\\":989240,\\\"item_name\\\":\\\"手机号命中低风险关注名单\\\",\\\"group\\\":\\\"风险信息扫描\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"frequency_detail_list\\\":[{\\\"data\\\":[\\\"34252319861121041x\\\",\\\"谢自超\\\"],\\\"detail\\\":\\\"3月内_手机号码_身份证_关联个数_全局：2\\\"}],\\\"type\\\":\\\"frequency_detail\\\"},\\\"item_id\\\":989292,\\\"item_name\\\":\\\"3个月内申请信息关联多个身份证\\\",\\\"group\\\":\\\"客户行为检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"frequency_detail_list\\\":[{\\\"detail\\\":\\\"7天内_手机号码_出现次数_本应用：8\\\"}],\\\"type\\\":\\\"frequency_detail\\\"},\\\"item_id\\\":989306,\\\"item_name\\\":\\\"7天内设备或身份证或手机号申请次数过多\\\",\\\"group\\\":\\\"客户行为检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963813,\\\"item_name\\\":\\\"7天内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963823,\\\"item_name\\\":\\\"1个月内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963833,\\\"item_name\\\":\\\"3个月内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"}],\\\"address_detect\\\":{\\\"mobile_address\\\":\\\"上海市\\\",\\\"id_card_address\\\":\\\"安徽省宣城地区广德县\\\"},\\\"final_decision\\\":\\\"Review\\\",\\\"report_time\\\":1533284589000,\\\"success\\\":true,\\\"report_id\\\":\\\"ER2018080316230934D08559\\\",\\\"apply_time\\\":1533284589000,\\\"application_id\\\":\\\"180803162309447F5CC883D44631CC34\\\"}}\",\"idcard\":\"511623199112244421\",\"name\":\"胡红\",\"mobile\":\"18381674004\",\"alipay_user_id\":\"2088902303336935\",\"immediate_family_mobile\":\"15815815815\",\"apply_time\":\"2019-04-08 11:34:50\",\"merchant_address\":[{\"city_address\":\"县\",\"city_id\":\"120200\",\"province_address\":\"天津市\",\"province_id\":120000},{\"city_address\":\"市辖区\",\"city_id\":\"110100\",\"province_address\":\"北京市\",\"province_id\":110000},{\"city_address\":\"县\",\"city_id\":\"110200\",\"province_address\":\"北京市\",\"province_id\":110000}],\"decoration_address\":{\"decoration_district\":\"阿鲁科尔沁旗\",\"decoration_province_id\":150000,\"decoration_city_id\":150400,\"decoration_province\":\"内蒙古自治区\",\"decoration_city\":\"赤峰市\",\"decoration_input_address\":\"恶魔之眼\",\"decoration_district_id\":150421}}".encode('utf-8')
        rs = json.loads(jtl.test_risk_system(risk_system_datas))
        ass.verity(rs["contract_no"], '2019040811045722840960')
        ass.verity(rs["final_score"], 69)
        ass.verity(rs["result"], 2)
        ass.verity(rs["advice"], '客户装修地址与商户经营地址不匹配，建议拒绝')

    def test_002_risk_system_earnest(self):
        risk_system_earnest_datas = "{\"contract_no\": \"20181205111233465126976\", \"immediate_family_name\": \"369\", \"tencent_json\": \"\", \"rule_type\": 2, \"td_json\": \"{\\\"data\\\":{\\\"final_score\\\":80,\\\"risk_items\\\":[{\\\"risk_level\\\":\\\"medium\\\",\\\"score\\\":20,\\\"item_detail\\\":{\\\"namelist_hit_details\\\":[{\\\"hit_type_displayname\\\":\\\"借款人身份证\\\",\\\"fraud_type\\\":\\\"申请行为异常\\\",\\\"description\\\":\\\"验证匹配字段是否在欺诈灰名单中\\\",\\\"type\\\":\\\"grey_list\\\"}],\\\"fraud_type\\\":\\\"申请行为异常\\\"},\\\"item_id\\\":989212,\\\"item_name\\\":\\\"身份证命中中风险关注名单\\\",\\\"group\\\":\\\"风险信息扫描\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"namelist_hit_details\\\":[{\\\"hit_type_displayname\\\":\\\"借款人身份证\\\",\\\"fraud_type\\\":\\\"异常借款\\\",\\\"description\\\":\\\"验证匹配字段是否在欺诈灰名单中\\\",\\\"type\\\":\\\"grey_list\\\"}],\\\"fraud_type\\\":\\\"异常借款\\\"},\\\"item_id\\\":989216,\\\"item_name\\\":\\\"身份证命中低风险关注名单\\\",\\\"group\\\":\\\"风险信息扫描\\\"},{\\\"risk_level\\\":\\\"medium\\\",\\\"score\\\":30,\\\"item_id\\\":989218,\\\"item_name\\\":\\\"手机号格式校验错误\\\",\\\"group\\\":\\\"个人基本信息核查\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":9,\\\"item_detail\\\":{\\\"frequency_detail_list\\\":[{\\\"detail\\\":\\\"3个月身份证关联家庭地址数：0\\\"},{\\\"data\\\":[\\\"17360026896\\\",\\\"183※※※※8237\\\",\\\"183※※※※4004\\\"],\\\"detail\\\":\\\"3月内_身份证_手机号码_关联个数_全局：3\\\"}],\\\"type\\\":\\\"frequency_detail\\\"},\\\"item_id\\\":989290,\\\"item_name\\\":\\\"3个月内身份证关联多个申请信息\\\",\\\"group\\\":\\\"客户行为检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":6,\\\"item_detail\\\":{\\\"frequency_detail_list\\\":[{\\\"data\\\":[\\\"511623199112244421\\\",\\\"620503199001250910\\\"],\\\"detail\\\":\\\"3月内_手机号码_身份证_关联个数_全局：2\\\"}],\\\"type\\\":\\\"frequency_detail\\\"},\\\"item_id\\\":989292,\\\"item_name\\\":\\\"3个月内申请信息关联多个身份证\\\",\\\"group\\\":\\\"客户行为检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":10,\\\"item_detail\\\":{\\\"frequency_detail_list\\\":[{\\\"detail\\\":\\\"1月内_手机号码_出现次数_本应用：70\\\"},{\\\"detail\\\":\\\"7天内_手机号码_出现次数_本应用：1\\\"}],\\\"type\\\":\\\"frequency_detail\\\"},\\\"item_id\\\":989308,\\\"item_name\\\":\\\"1个月内设备或身份证或手机号申请次数过多\\\",\\\"group\\\":\\\"客户行为检测\\\"},{\\\"risk_level\\\":\\\"high\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":2,\\\"detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\"],\\\"platform_count\\\":2,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":989320,\\\"item_name\\\":\\\"7天内申请人在多个平台申请借款\\\",\\\"group\\\":\\\"多平台借贷申请检测\\\"},{\\\"risk_level\\\":\\\"medium\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":3,\\\"detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\",\\\"综合类电商平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\",\\\"综合类电商平台:1\\\"],\\\"platform_count\\\":3,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":989322,\\\"item_name\\\":\\\"1个月内申请人在多个平台申请借款\\\",\\\"group\\\":\\\"多平台借贷申请检测\\\"},{\\\"risk_level\\\":\\\"medium\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":4,\\\"detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\",\\\"网上银行:1\\\",\\\"综合类电商平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\",\\\"信用卡中心:1\\\",\\\"网上银行:1\\\",\\\"综合类电商平台:1\\\"],\\\"platform_count\\\":4,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":989324,\\\"item_name\\\":\\\"3个月内申请人在多个平台申请借款\\\",\\\"group\\\":\\\"多平台借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":1,\\\"item_detail\\\":{\\\"platform_detail\\\":[\\\"信用卡中心:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15962003,\\\"item_name\\\":\\\"7天内申请人在银行类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail\\\":[\\\"信用卡中心:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15962013,\\\"item_name\\\":\\\"1个月内申请人在银行类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":1,\\\"item_detail\\\":{\\\"platform_detail\\\":[\\\"信用卡中心:1\\\",\\\"网上银行:1\\\"],\\\"platform_count\\\":2,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15962023,\\\"item_name\\\":\\\"3个月内申请人在银行类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":3,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963813,\\\"item_name\\\":\\\"7天内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963823,\\\"item_name\\\":\\\"1个月内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"},{\\\"risk_level\\\":\\\"low\\\",\\\"score\\\":0,\\\"item_detail\\\":{\\\"platform_detail_dimension\\\":[{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人手机详情\\\"},{\\\"count\\\":1,\\\"detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"dimension\\\":\\\"借款人身份证详情\\\"}],\\\"platform_detail\\\":[\\\"一般消费分期平台:1\\\"],\\\"platform_count\\\":1,\\\"type\\\":\\\"platform_detail\\\"},\\\"item_id\\\":15963833,\\\"item_name\\\":\\\"3个月内申请人在一般消费分期平台和房地产金融类平台申请借款\\\",\\\"group\\\":\\\"指定平台多头借贷申请检测\\\"}],\\\"address_detect\\\":{\\\"id_card_address\\\":\\\"四川省广安市邻水县\\\"},\\\"final_decision\\\":\\\"Reject\\\",\\\"report_time\\\":1545039983000,\\\"success\\\":true,\\\"report_id\\\":\\\"ER20181217171123F257422D\\\",\\\"apply_time\\\":1545039983000,\\\"application_id\\\":\\\"181217174623421EB2213D536CC82127\\\"}}\", \"baidu_json\": \"\", \"idcard\": \"511623199112244421\", \"name\": \"可达鸭\", \"mobile\": \"17360026896\", \"immediate_family_mobile\": \"15836958257\", \"apply_time\": \"2019-02-15 16:38:50\", \"credit_number\": \"550000\"}".encode('utf-8')
        rs = json.loads(jtl.test_risk_system_earnest(risk_system_earnest_datas))
        ass.verity(rs["contract_no"], '20181205111233465126976')
        ass.verity(rs["final_score"], 80)
        ass.verity(rs["result"], 2)
        ass.verity(rs["advice"], '高风险，建议拒绝')

