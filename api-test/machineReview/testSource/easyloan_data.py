# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 17:57:55 2019

@author: Administrator
"""

# 好贷机审
easyloan_data_demo = {
    "data": {
        "yys": "{\"friend_circle\": {\"summary\": [{\"value\": \"否\",\"key\": \"is_city_match_friend_city_center_3m\"}, {\"value\": \"否\",\"key\": \"is_city_match_friend_city_center_6m\"},{\"value\": \"6\",\"key\": \"inter_peer_num_3m\"}, {\"value\": \"6\",\"key\": \"inter_peer_num_6m\"}],\"peer_num_top_list\": [{\"top_item\": [{\"peer_number\": \"15775800488\"}, {\"peer_number\": \"18948195035\"}, {\"peer_number\": \"18218412431\"}],\"key\": \"peer_num_top3_3m\"}, {\"top_item\": [{\"peer_number\": \"15775800488\"}, {\"peer_number\": \"18948195035\"}, {\"peer_number\": \"18218412431\"}],\"key\": \"peer_num_top3_6m\"}]},\"call_risk_analysis\": [{\"analysis_point\": {\"call_cnt_1m\": 0,\"call_cnt_3m\": 0,\"call_cnt_6m\": 0,\"call_time_3m\": 0,\"call_time_6m\": 0,\"call_time_1m\": 0},\"analysis_desc\": \"贷款\"}, {\"analysis_point\": {\"call_cnt_1m\": 0,\"call_cnt_3m\": 0,\"call_cnt_6m\": 0,\"call_time_3m\": 0,\"call_time_6m\": 0,\"avg_call_cnt_3m\": 0.0,\"call_time_1m\": 0},\"analysis_desc\": \"催收公司\"}],\"consumption_detail\": [{\"item\": {\"item_6m\": \"36001\",\"item_3m\": \"17410\",\"avg_item_3m\": \"5803\",\"item_1m\": \"5800\",\"avg_item_6m\": \"6000\"},\"app_point\": \"total_fee\",\"app_point_zh\": \"消费总金额（分）\"}],\"basic_check_items\": [{\"result\": \"否\",\"check_item\": \"is_name_and_idcard_in_court_black\"}, {\"result\": \"否\",\"comment\": \"\",\"check_item\": \"is_name_and_idcard_in_finance_black\"}, {\"result\": \"否\",\"comment\": \"\",\"check_item\": \"is_name_and_mobile_in_finance_black\"}],\"active_degree\": [{\"item\": {\"item_6m\": \"181\",\"item_3m\": \"82\",\"avg_item_3m\": \"27.33\",\"item_1m\": \"28\",\"avg_item_6m\": \"30.17\"},\"app_point\": \"peer_num_cnt\",\"app_point_zh\": \"通话号码数目\"}, {\"item\": {\"item_6m\": \"20\",\"item_3m\": \"15\",\"avg_item_3m\": \"5.00\",\"item_1m\": \"6\",\"avg_item_6m\": \"3.33\"},\"app_point\": \"no_call_day\",\"app_point_zh\": \"无通话天数\"}, {\"item\": {\"item_6m\": \"17\",\"item_3m\": \"12\",\"avg_item_3m\": \"4.00\",\"item_1m\": \"5\",\"avg_item_6m\": \"2.83\"},\"app_point\": \"power_off_day\",\"app_point_zh\": \"关机天数\"}, {\"item\": {\"item_6m\": \"0\",\"item_3m\": \"0\",\"item_1m\": \"0\"},\"app_point\": \"continue_power_off_cnt\",\"app_point_zh\": \"连续3天以上关机次数\"}],\"user_info_check\": [{\"check_search_info\": {\"register_org_cnt\": 0,\"searched_org_cnt\": 0},\"check_black_info\": {\"contacts_class1_cnt\": 121,\"contacts_class1_blacklist_cnt\": 0,\"contacts_class2_blacklist_cnt\": 5,\"contacts_router_ratio\": 0.02,\"phone_gray_score\": 67}}],\"cell_phone\": [{\"value\": \"93\",\"key\": \"in_time\"}, {\"value\": \"实名认证\",\"key\": \"reliability\"}, {\"value\": \"668\",\"key\": \"available_balance\"}],\"call_contact_detail\": [{\"call_cnt_6m\": 304,\"peer_num\": \"15775800488\",\"call_cnt_1m\": 55,\"call_cnt_3m\": 140,\"call_cnt_1w\": 9}],\"behavior_check\": [{\"result\": \"很少夜间活动（低于20%)\",\"score\": 1,\"evidence\": \"晚间活跃频率占全天的1.43%\",\"check_point_cn\": \"夜间活动情况\",\"check_point\": \"contact_night\"}]}",
        "tongdun": "{\"report\": {\"final_score\": 7,\"risk_items\": [{\"item_detail\": {\"frequency_detail_list\": [{\"detail\": \"3个月身份证关联家庭地址数：0\"}, {\"detail\": \"3月内_身份证_手机号码_关联个数_全局：2\"}, {\"detail\": \"3个月身份证关联邮箱数：2\"}],\"type\": \"frequency_detail\"},\"item_name\": \"3个月内身份证关联多个申请信息\",\"group\": \"客户行为检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"7天内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"1个月内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"3个月内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"}]}}",
        "jingdong": "{\"basic_info\": {\"user_and_account_basic_info\": {\"xiao_bai_credit\": \"71.9\",\"jd_name\": \"*之浪\"}},\"wealth_info\": {\"totalssets\": {\"available_limit\": \"0.0\",\"credit_wait_pay\": \"0.0\",\"wallet_money_available\": \"0.0\",\"credit_limit\": \"0.0\",\"total_money\": \"0.0\",\"delinquency_balance\": \"0.0\"}},\"address_analysis\": {\"commonly_used_address\": {\"deliver_address\": [{\"first_deliver_time\": \"2017-02-18 11:09:16\"}, {\"first_deliver_time\": \"2018-10-22 09:08:06\"}, {\"first_deliver_time\": \"2018-03-02 11:10:44\"}]}},\"consumption_analysis\": {\"receiving_consumption\": {\"self_consum_times\": {\"sum\": \"4\"}}}}",
        "taobao": "{\"basic_info\": {\"user_and_account_basic_info\": {\"alipay_account\": \"826****01@qq.com\",\"tao_score\": \"958\",\"taobao_name\": \"杨之浪\",\"taobao_phone_number\": \"182****3311\",\"taobao_email\": \"826****01@qq.com\",\"account_auth\": \"已认证\"}},\"wealth_info\": {\"totalssets\": {\"yue_e_bao_amt\": \"34890.05\",\"balance\": \"3253.57\",\"huai_bei_can_use_limit\": \"10816.45\",\"huai_bei_limit\": \"19000.00\",\"taobao_jiebei_amount\": \"0.00\",\"taobao_zmscore\": \"771\",\"taobao_jiebie_available_amount\": \"0.00\"}},\"address_analysis\": {\"commonly_used_address\": {\"first_deliver_time\": {\"top3\": \"2019-03-15 19:49:05\",\"top1\": \"2018-08-22 09:09:01\",\"top2\": \"2018-07-20 12:49:05\"}}},\"consumption_analysis\": {\"receiving_consumption\": {\"self_consum_times\": {\"sum\": \"17\"}}}}",
        "alipay": "{\"basic_info\": {\"user_and_account_basic_info\": {\"total_expenses_amt_6m\": \"0.00\",\"card_number\": \"51018***********11\",\"user_name\": \"杨之浪\",\"is_realname\": \"是\",\"total_income_amt_6m\": \"0.00\",\"register_month\": \"110\"}},\"major_expenditure\": {\"repayment\": {\"other_rpy_amt\": {\"sum\": \"0.00\"},\"other_rpy_cnt\": {\"sum\": \"0\"}}},\"wealth_info\": {\"total_assets\": {\"taobao_finance\": \"0.00\",\"balance\": \"11045.34\",\"fund\": \"0.00\",\"huabai_limit\": \"19000.00\",\"cun_jin_bao\": \"0.00\",\"yu_e_bao\": \"22821.47\",\"zhao_cai_bao\": \"20008.73\"}}}",
        "basicinfo": {
            "V01_3001": 3,
            "V01_3002": 0.0,
            "V01_3003": "",
            "V01_3004": "",
            "V01_3005": "",
            "V01_1009": "13399929132",
            "V01_1008": "15680750658",
            "V01_1007": "HYZK0002",
            "V01_1006": "",
            "V01_1005": "辽宁省大连市金州区城南路15号",
            "V01_1004": "210222196604109118",
            "V01_2005": "DWGM0003",
            "V01_1003": "",
            "V01_2004": "3-5年",
            "V01_1002": "1",
            "V01_2003": "HYXZ0003",
            "V01_1013": "",
            "V01_1001": 2019,
            "V01_1012": "SR000004",
            "V01_2002": "DWXZ0002",
            "V01_2001": "XL000004",
            "V01_1011": "",
            "V01_1014": "20190508",
            "V01_1010": "[]"
        }
    },
    "scene_id": "8",
    "version": {
        "tongdun": "td_v1",
        "yys": "mx_v1",
        "taobao": "mx_v4",
        "alipay": "mx_v4",
        "jingdong": "mx_v3"
    }
}

# 小启信用，请求参数
xqxy_data_demo = {
    "data": {
        "tongdun": "{\"report\": {\"final_score\": 7,\"risk_items\": [{\"item_detail\": {\"frequency_detail_list\": [{\"detail\": \"3个月身份证关联家庭地址数：0\"}, {\"detail\": \"3月内_身份证_手机号码_关联个数_全局：2\"}, {\"detail\": \"3个月身份证关联邮箱数：2\"}],\"type\": \"frequency_detail\"},\"item_name\": \"3个月内身份证关联多个申请信息\",\"group\": \"客户行为检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"7天内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"1个月内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"}, {\"item_detail\": {\"platform_detail\": [\"一般消费分期平台:1\", \"小额贷款公司:1\", \"P2P网贷:1\", \"大数据金融:1\", \"互联网金融门户:1\", \"第三方服务商:1\"],\"platform_count\": 6,\"type\": \"platform_detail\"},\"item_name\": \"3个月内申请人在多个平台申请借款\",\"group\": \"多平台借贷申请检测\"},{\"item_id\":989196,\"item_name\":\"身份证命中法院失信名单\",\"group\":\"风险信息扫描\"},{\"item_id\":989200,\"item_name\":\"身份证命中法院执行名单\",\"group\":\"风险信息扫描\"}]}}",
        "alipay": "{\"basic_info\": {\"user_and_account_basic_info\": {\"total_expenses_amt_6m\": \"0.00\",\"card_number\": \"51018***********11\",\"user_name\": \"杨之浪\",\"is_realname\": \"是\",\"total_income_amt_6m\": \"0.00\",\"register_month\": \"110\"}},\"major_expenditure\": {\"repayment\": {\"other_rpy_amt\": {\"sum\": \"0.00\"},\"other_rpy_cnt\": {\"sum\": \"0\"}}},\"wealth_info\": {\"total_assets\": {\"taobao_finance\": \"0.00\",\"balance\": \"11045.34\",\"fund\": \"0.00\",\"huabai_limit\": \"19000.00\",\"cun_jin_bao\": \"0.00\",\"yu_e_bao\": \"22821.47\",\"zhao_cai_bao\": \"20008.73\"}}}",
        "yys": "{\"open_time\": \"2018-07-02\", \"available_balance\": \"282.27\", \"state\": \"是\", \"bills\": [{\"bill_month\": \"2019-05\", \"bill_start_date\": \"2019-05-01\", \"bill_end_date\": \"2019-05-31\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"\", \"voice_fee\": \"1.20\", \"sms_fee\": \"\", \"web_fee\": \"18.10\", \"extra_fee\": \"\", \"total_fee\": \"24.30\"}, {\"bill_month\": \"2019-04\", \"bill_start_date\": \"2019-04-01\", \"bill_end_date\": \"2019-04-30\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"\", \"voice_fee\": \"3.90\", \"sms_fee\": \"\", \"web_fee\": \"25.80\", \"extra_fee\": \"\", \"total_fee\": \"34.70\"}, {\"bill_month\": \"2019-03\", \"bill_start_date\": \"2019-03-01\", \"bill_end_date\": \"2019-03-31\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"0.10\", \"voice_fee\": \"\", \"sms_fee\": \"\", \"web_fee\": \"31.00\", \"extra_fee\": \"\", \"total_fee\": \"36.10\"}, {\"bill_month\": \"2019-02\", \"bill_start_date\": \"2019-02-01\", \"bill_end_date\": \"2019-02-28\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"0.30\", \"voice_fee\": \"1.50\", \"sms_fee\": \"0.30\", \"web_fee\": \"27.40\", \"extra_fee\": \"\", \"total_fee\": \"34.20\"}, {\"bill_month\": \"2019-01\", \"bill_start_date\": \"2019-01-01\", \"bill_end_date\": \"2019-01-31\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"0.20\", \"voice_fee\": \"\", \"sms_fee\": \"\", \"web_fee\": \"30.00\", \"extra_fee\": \"\", \"total_fee\": \"35.20\"}, {\"bill_month\": \"2018-12\", \"bill_start_date\": \"2018-12-01\", \"bill_end_date\": \"2018-12-31\", \"base_fee\": \"5.00\", \"extra_service_fee\": \"0.20\", \"voice_fee\": \"0.60\", \"sms_fee\": \"0.20\", \"web_fee\": \"31.00\", \"extra_fee\": \"\", \"total_fee\": \"36.80\"}]}",
        "jingdong": "{\"first_deal_time\": \"2011-09-13 22:01:00\",\"credit\": \"100.9 \", \"btType\": \"0\", \"BtPrivilege\": {\"creditLimit\":\"2000\",\"availableLimit\":\"2000\",\"delinquencyBalance\":\"0\"}, \"creditData\": {\"jtDelinquencyBalance\": \"0.00\"}, \"authenticateData\": {\"authenticateName\": \"*忠楷\"}, \"financeData\": {\"walletMoney\": 0.0, \"totalMoney\": 0.0}, \"orderResultExtend\": {\"201906\": {\"all_fee\": 90.4, \"all_cnt\": 1, \"all_prd_cnt\": 4, \"personal_fee\": 90.4, \"personal_cnt\": 1, \"personal_prd_cnt\": 4, \"virtual_fee\": 0.0, \"virtual_cnt\": 0, \"virtual_prd_cnt\": 0, \"virtual_proportion\": 0.0}, \"201905\": {\"all_fee\": 648.44, \"all_cnt\": 9, \"all_prd_cnt\": 23, \"personal_fee\": 648.44, \"personal_cnt\": 9, \"personal_prd_cnt\": 23, \"virtual_fee\": 129.87, \"virtual_cnt\": 2, \"virtual_prd_cnt\": 2, \"virtual_proportion\": 20.028067361668}, \"201904\": {\"all_fee\": 571.26, \"all_cnt\": 9, \"all_prd_cnt\": 15, \"personal_fee\": 571.26, \"personal_cnt\": 9, \"personal_prd_cnt\": 15, \"virtual_fee\": 99.9, \"virtual_cnt\": 1, \"virtual_prd_cnt\": 1, \"virtual_proportion\": 17.487658859363513}, \"201903\": {\"all_fee\": 626.85, \"all_cnt\": 4, \"all_prd_cnt\": 6, \"personal_fee\": 626.85, \"personal_cnt\": 4, \"personal_prd_cnt\": 6, \"virtual_fee\": 0.0, \"virtual_cnt\": 0, \"virtual_prd_cnt\": 0, \"virtual_proportion\": 0.0}, \"201902\": {\"all_fee\": 220.89, \"all_cnt\": 4, \"all_prd_cnt\": 4, \"personal_fee\": 59.94, \"personal_cnt\": 2, \"personal_prd_cnt\": 2, \"virtual_fee\": 109.89, \"virtual_cnt\": 3, \"virtual_prd_cnt\": 3, \"virtual_proportion\": 49.74874371859297}, \"201901\": {\"all_fee\": 577.9499999999999, \"all_cnt\": 7, \"all_prd_cnt\": 7, \"personal_fee\": 278.25, \"personal_cnt\": 5, \"personal_prd_cnt\": 5, \"virtual_fee\": 349.65000000000003, \"virtual_cnt\": 3, \"virtual_prd_cnt\": 3, \"virtual_proportion\": 60.49831300285493}, \"201812\": {\"all_fee\": 2179.2200000000003, \"all_cnt\": 13, \"all_prd_cnt\": 23, \"personal_fee\": 2179.2200000000003, \"personal_cnt\": 13, \"personal_prd_cnt\": 23, \"virtual_fee\": 79.92, \"virtual_cnt\": 1, \"virtual_prd_cnt\": 1, \"virtual_proportion\": 3.6673672231348826}, \"201811\": {\"all_fee\": 397.6, \"all_cnt\": 6, \"all_prd_cnt\": 41, \"personal_fee\": 397.6, \"personal_cnt\": 6, \"personal_prd_cnt\": 41, \"virtual_fee\": 0.0, \"virtual_cnt\": 0, \"virtual_prd_cnt\": 0, \"virtual_proportion\": 0.0}}}",
        "taobao": "{\"user_info\": {\"email\": \"tia****ing2012@163.com\", \"phone\": \"176****0604\", \"taoScore\": \"660\", \"taobao_account\": {\"taobao_real_name\": \"田路玲\"}}, \"alipay_bindings\": {\"alipayAccount\": \"176*****604\"}, \"alipayInfo\": {\"account_amount\": \"\", \"yuebao_amount\": \"\", \"huabei_available\": \"\", \"huabei_credit\": 1000}, \"first_deal_time\": \"2012-09-08 18:38:54\", \"orderResult\": {\"basic_info\": {\"account_auth\": \"已认证\"}, \"consumption_analysis\": {\"2018-12\": {\"all_fee\": 538.8, \"all_prd_cnt\": 4, \"all_cnt\": 4, \"personal_fee\": 239.8, \"personal_prd_cnt\": 3.0, \"personal_cnt\": 3.0, \"virtual_fee\": 0.0, \"virtual_prd_cnt\": 0.0, \"virtual_cnt\": 0.0, \"virtual_proportion\": 0.0}, \"2019-01\": {\"all_fee\": 191.3, \"all_prd_cnt\": 5, \"all_cnt\": 3, \"personal_fee\": 0.0, \"personal_prd_cnt\": 0.0, \"personal_cnt\": 0.0, \"virtual_fee\": 0.0, \"virtual_prd_cnt\": 0.0, \"virtual_cnt\": 0.0, \"virtual_proportion\": 0.0}, \"2019-02\": {\"all_fee\": 79.8, \"all_prd_cnt\": 12, \"all_cnt\": 4, \"personal_fee\": 0.0, \"personal_prd_cnt\": 0.0, \"personal_cnt\": 0.0, \"virtual_fee\": 0.0, \"virtual_prd_cnt\": 0.0, \"virtual_cnt\": 0.0, \"virtual_proportion\": 0.0}, \"2019-03\": {\"all_fee\": 556.0, \"all_prd_cnt\": 7, \"all_cnt\": 7, \"personal_fee\": 0.0, \"personal_prd_cnt\": 0.0, \"personal_cnt\": 0.0, \"virtual_fee\": 16.0, \"virtual_prd_cnt\": 4.0, \"virtual_cnt\": 4.0, \"virtual_proportion\": 2.8776978417}, \"2019-04\": {\"all_fee\": 376.02, \"all_prd_cnt\": 13, \"all_cnt\": 11, \"personal_fee\": 9.82, \"personal_prd_cnt\": 1.0, \"personal_cnt\": 1.0, \"virtual_fee\": 93.82, \"virtual_prd_cnt\": 7.0, \"virtual_cnt\": 7.0, \"virtual_proportion\": 24.9508004893}, \"2019-05\": {\"all_fee\": 431.18, \"all_prd_cnt\": 6, \"all_cnt\": 6, \"personal_fee\": 197.99, \"personal_prd_cnt\": 1.0, \"personal_cnt\": 1.0, \"virtual_fee\": 201.99, \"virtual_prd_cnt\": 2.0, \"virtual_cnt\": 2.0, \"virtual_proportion\": 46.845864836}}}}",
        "basicinfo": {
            "V01_3001": 3,
            "V01_3002": 0.00,
            "V01_3003": "",
            "V01_3004": "",
            "V01_3005": "",
            "V01_1009": "13399929132",
            "V01_1008": "15680750658",
            "V01_1007": "HYZK0002",
            "V01_1006": "",
            "V01_1005": "辽宁省大连市金州区城南路15号",
            "V01_1004": "210222196604109118",
            "V01_2005": "DWGM0003",
            "V01_1003": "",
            "V01_2004": "3-5年",
            "V01_1002": "1",
            "V01_2003": "HYXZ0003",
            "V01_1013": "",
            "V01_1001": 2019,
            "V01_1012": "SR000004",
            "V01_2002": "DWXZ0002",
            "V01_2001": "XL000004",
            "V01_1011": "",
            "V01_1010": "[]",
            "V01_1014": ""
        }
    },
    "scene_id": "14",
    "version": {
        "yys": "qf_v1",
        "taobao": "qf_v1",
        "jingdong": "qf_v1",
        "rfw": "qf_v1",
        "tongdun": "td_v1",
        "alipay": "mx_v4"
    }
}
