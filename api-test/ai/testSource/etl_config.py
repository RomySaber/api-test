redis_info = {"host": "192.168.15.247", "port": 6391, "db": 0, "passwd": "aitest@78dk.com"}
mj_redis_info = {"host": "192.168.15.161", "port": 6399, "db": 8, "passwd": "meijia@78dk.com"}
mongo_info = {"host": "192.168.15.236", "port": 27022, "mydb": "webdb", "collist": "webdb", "username": "webdb",
              "password": "webdb@78dk.com"}

operatorETL = {"mobile": "18628010604", "name": "李小红", "carrier": "CHINA_UNICOM", "city": "成都",
               "level": "二星用户", "idcard": "513821201310246208", "open_time": "2018-08-02", "package_name": "米粉卡（5元卡）",
               "available_balance": "168.03", "state": "是", "email": "未绑定", "address": "四川省成都市双流区天府软件园", "bills": [
        {"bill_month": "2019-08", "bill_start_date": "2019-08-01", "bill_end_date": "2019-08-31", "base_fee": "5.00",
         "extra_service_fee": "", "voice_fee": "1.50", "sms_fee": "", "web_fee": "28.10", "extra_fee": "",
         "total_fee": "34.60"}], "calls": [{"bill_month": "2019-09", "total_size": 9, "items": [
        {"time": "2019-09-13 23:59:59", "location": "河北沧州", "fee": "0.00", "details_id": "28231",
         "peer_number": "13603188648", "location_type": "国内通话", "duration": 136, "dial_type": "DAILED"}]}], "smses": [
        {"bill_month": "2019-09", "total_size": 1, "items": [
            {"time": "2019-09-14-23:59:59", "location": "", "fee": "0.10", "details_id": "",
             "peer_number": "13603188648", "send_type": "SEND", "msg_type": "SMS", "service_name": ""}]}]}

tb_ETL = {"user_info": {"username": "千寻七号", "email": "qia****ing999@163.com", "phone": "130****0983", "taoScore": "683",
                        "taobao_account": {"real_name": "千寻寻", "login_email": "qia****ing999@163.com", "sex": "女",
                                           "birthday": "1983年8月19日", "adress": ""}}, "user_level": {},
          "alipay_bindings": {"alipayAccount": "130*****983", "accoutType": "个人账户",
                              "certification": "千**\u00a0|\u00a03****************9\u00a0已认证"}, "tbBuyGoodsInfo": [{
        "extra": {"batchGroup": "0", "batchGroupTips": "预售商品", "batchMaxCount": 20, "bizType": 200, "currency": "CNY",
                  "currencySymbol": "￥", "finish": True, "id": 621305282475124069, "inHold": False,
                  "isShowSellerService": False, "needDisplay": True, "tradeStatus": "TRADE_FINISHED",
                  "visibility": True}, "id": "621305282475124069",
        "operations": [{"id": "share", "style": "thead", "text": "分享", "type": "operation"}],
        "orderInfo": {"b2C": True, "createDay": "2019-09-13", "createTime": "2019-04-08 01:00:00",
                      "id": "621305282475124069"},
        "payInfo": {"actualFee": "65.00", "icons": [{"linkTitle": "手机订单", "linkUrl": "", "type": 3, "url": ""}],
                    "postFees": [{"prefix": "(含运费", "suffix": ")", "value": "￥0.00", "postType": ""}]},
        "seller": {"alertStyle": 0, "guestUser": False, "id": 2113517056, "nick": "回力萨莎专卖店", "notShowSellerInfo": False,
                   "opeanSearch": False, "shopDisable": False, "shopImg": "", "shopName": "回力萨莎专卖店", "shopUrl": "",
                   "wangwangType": "nonAlipay"}, "statusInfo": {
            "operations": [{"id": "huabeiBill", "style": "t0", "text": "花呗账单", "type": "operation", "url": ""}],
            "text": "交易成功", "type": "t0", "url": ""}, "subOrders": [{"id": 621305282475124069,
                                                                     "itemInfo": {"id": 579001574459, "itemUrl": "",
                                                                                  "pic": "", "serviceIcons": [
                                                                             {"linkTitle": "七天退换", "linkUrl": "",
                                                                              "name": "七天退换", "title": "七天退换",
                                                                              "type": 3, "url": ""}],
                                                                                  "skuId": 3957965908017, "skuText": [
                                                                             {"name": "颜色分类", "value": "黑色-经典版",
                                                                              "visible": "SOLID"},
                                                                             {"name": "尺码", "value": "",
                                                                              "visible": "SOLID"}], "snapUrl": "",
                                                                                  "title": "回力帆布鞋", "xtCurrent": False},
                                                                     "operations": [
                                                                         {"action": "a3", "dataUrl": "", "style": "t0",
                                                                          "text": "申请售后"}],
                                                                     "priceInfo": {"original": "139.00",
                                                                                   "realTotal": "65.00"},
                                                                     "quantity": "1"}, {
                                                                        "itemInfo": {"itemUrl": "", "skuId": 0,
                                                                                     "title": "保险服务",
                                                                                     "xtCurrent": False},
                                                                        "priceInfo": {"realTotal": "0.00"}}],
        "orderReceiver": {"orderReceiverName": "", "orderReceiverPhone": "13000123123",
                          "orderReceiverAddress": "四川省 成都市 西溪区 中和街道长久路福分小区E区", "orderReceiverPostcode": "000000"}}],
          "alipayInfo": {"account_amount": "", "yuebao_amount": "", "huabei_available": "", "huabei_credit": "",
                         "lifes_payment": [{"PaymentType": "水费", "PaymentRegion": "成都", "PaymentCompany": "成都市水务有限责任公司",
                                            "PaymentMaster": "*寻寻", "PaymentNumber": "40071027"}], "bankcards": [
                  {"bankname": "中国农业银行", "banknumber": "尾号2134", "bankcardtype": ["card-type", "card-type-DC"]},
                  {"bankname": "招商银行", "banknumber": "尾号8895", "bankcardtype": ["card-type", "card-type-DC"]}],
                         "alipay_account": {"alipay_real_name": "*寻寻|5****************8已认证",
                                            "alipay_open_time": "2012年09月08日", "alipay_phone": "130******23",
                                            "alipay_email": "未添加邮箱账户名"}}, "first_deal_time": "2015-09-18 19:24:34",
          "inserttime": "2019-10-08 09:34:17"}

jd_ETL = {"order": [
    {"amount": "50.00", "payType": "在线支付", "dealtime": "2019-07-21 09:33:29", "orderid": "94872100254",
     "goods": [{"goodsNum": 1, "goodsName": "快充", "goodsUrl": "", "goodsPrice": 49.95}], "name": "李明一", "status": "已完成",
     "address": "浙江杭州市西溪区路西镇菲菲小区1栋", "telephone": "198****9993", "shop": "手机充值", "amount_total": "商品总金额：￥49.95",
     "returncash": "", "transpay": "", "taxpay": "", "discount": "", "coupon": "", "balance": "0.00"}],
    "card": [{"bank": "cmb", "tailNum": "尾号1689", "saving": "\n储蓄卡\n", "name": "*寻", "phone": "198****9993"}],
    "first_deal_time": "2015-01-18 12:43:17", "name": "千寻1号", "loginName": "千寻1号", "nickName": "千寻1号",
    "credit": "92.0 ", "totalScore": "1911", "userType": "个人用户", "accountScore": "194", "activityScore": "6",
    "consumptionScore": "1419", "riskScore": "3", "financeScore": "92", "btType": "1", "btStatus": "1",
    "needPayTotal": "", "permLimit": "", "billLists": "", "BtPrivilege": "",
    "creditData": {"totalDebt": 0.0, "creditLimit": "0.00", "jtTotalDebt": "0.00", "jtCreditLimit": "0.00",
                   "actStatus": 2, "tourCreditLimit": "0.00", "jieqianActStatus": 2, "creditWaitPaySeven": "0.00",
                   "creditWaitPayPercent": 0, "tourCreditWaitPaySeven": "0.00", "jtAvailableLimit": "0.00",
                   "availableLimit": "0.00", "jtCreditWaitPay": "0.00", "tourCreditWaitPayPercent": 0,
                   "tourActStatus": 2, "creditWaitPay": "0.00", "tourTotalDebt": "0.00", "tourCreditWaitPay": "0.00",
                   "jtCreditWaitPaySeven": "0.00", "jtCreditWaitPayPercent": 0, "delinquencyBalance": "0.00",
                   "jtDelinquencyBalance": "0.00", "tourDelinquencyBalance": "0.00", "jtActStatus": 2,
                   "tourAvailableLimit": "0.00"},
    "authenticateData": {"authenticateName": "*寻", "id_card": "5****************8", "authenticateTime": "2017-07-21",
                         "phone_number": "198****9993", "authenticateWay": "京东金融实名认证", "financeService": ""},
    "authenticateDataExtend": {"real_maskCard": "51************6208", "sex": "女", "province": "浙江",
                               "mobile_mask": "198*****9993"},
    "financeData": {"walletMoney": 0.0, "freezeMoney": 0.0, "walletMoneyAvailable": 0.0, "balance": 0.0,
                    "balanceFreeze": 0.0, "balanceAvailable": 0, "currIncome": 0, "totalIncome": 0, "borrow": 0,
                    "investAmount": None, "totalMoney": 0.0, "rate": 0, "currency": None, "fundIncome": 0.0,
                    "finance": 0.0, "fund": 0.0, "billoanKeep": 0, "insuranceKeep": 0.0, "bankKeep": 0, "fundsKeep": 0,
                    "incomeSumYesterday": 0, "incomeTotal": 1.26, "incomeFinanceYesterday": 0, "incomeFinanceSum": 1.26,
                    "p2pAmount": 0, "trustAmount": 0, "firmFinance": 0, "secondaryAmount": 0, "lastestIncomeFlag": "1",
                    "lecaiAmount": None, "stockAmount": 0, "jgtAmount": 0, "cmaAmount": 0, "pensionAmount": None,
                    "gdScrtKeep": 0, "ztAmount": 0, "mmlc": 0, "balancePercent": 0, "fundPercent": 0,
                    "walletMoneyAvailablePercent": 0}, "inserttime": "2019-09-20 09:33:29"}

tianxing_etl = {"json_data": {
    "data": {
        "task_id": "td_9a2200f094e611eaba2a4b3fa5a4913b",
        "report_time": "2020-05-13 14:54:33",
        "report": {
            "B": {
                "phone": "135XXXX2818",
                "province": "XXX",
                "city": "XXX",
                "cycle": "2016-02-07--2018-02-07",
                "creditPlatformRegistrationDetails": [
                    {
                        "type": "非银行",
                        "code": "TX_0000182683",
                        "time": "2017-03-10"
                    }
                ],
                "loanApplicationDetails": [
                    {
                        "type": "非银行",
                        "code": "TX_0000182683",
                        "time": "2017-04-02",
                        "applicationAmountut": "0W～0.2W",
                        "applicationResult": "Yes"
                    }
                ],
                "loanDetails": [
                    {
                        "type": "非银行",
                        "code": "TX_0000182683",
                        "time": "2017-04-02",
                        "loanlendersAmount": "0W～0.2W"
                    }
                ],
                "loanRejectDetails": [
                    {
                        "type": "非银行",
                        "code": "TX_BAAACJ",
                        "time": "2017-06-23"
                    }
                ],
                "overduePlatformDetails": [
                    {
                        "code": "TX_0000182683",
                        "counts": "1",
                        "money": "0W～0.2W"
                    }
                ],
                "arrearsInquiry": [
                    {
                        "code": "TX_0000182683",
                        "money": "0W～0.2W"
                    }
                ],
                "status": "SUCCESS",
                "statusDesc": "查询正常"
            },
            "A": {
                "identityCard": "XXX",
                "name": "XXX",
                "pagination": {
                    "pageIndex": 1,
                    "totalPage": 6,
                    "resultSize": 105,
                    "pageSize": 20,
                    "officialAccountAmount": 0,
                    "testAccountAmount": 0,
                    "totalAccountAmount": 0
                },
                "pageData": [
                    {
                        "name": "XXX",
                        "gender": "男性",
                        "implementationStatus": "全部未履行",
                        "evidenceCode": "XXX",
                        "identificationNO": "XXX",
                        "executableUnit": "XXX",
                        "specificCircumstances": "有履行能力而拒不履行生效法律文书确定义务",
                        "obligations": "支付款项650000元",
                        "province": "XXX",
                        "postTime": 1463068800000,
                        "id": "XXX",
                        "recordTime": 1463068800000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "SXGG",
                        "time": "2016年09月13日"
                    },
                    {
                        "title": "XXXX",
                        "name": "XXX",
                        "caseStatus": "0",
                        "identificationNO": "XXXX",
                        "executionTarget": 650000,
                        "id": "XXX",
                        "recordTime": 1505232000000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "ZXGG",
                        "time": "2016年09月13日"
                    },
                    {
                        "name": "XXX",
                        "proposer": "",
                        "id": "XXX",
                        "recordTime": 1479744000000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "BGT",
                        "time": "2016年09月13日"
                    },
                    {
                        "caseType": "民事判决书",
                        "title": "XXX",
                        "litigants": [],
                        "id": "XXX",
                        "recordTime": 1468512000000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "CPWS",
                        "time": "2016年09月13日"
                    },
                    {
                        "layout": "",
                        "name": "XXX",
                        "announcementType": "裁判文书",
                        "id": "XXX",
                        "recordTime": 1483200000000,
                        "content": "XXX",
                        "court": "XXXX",
                        "dataType": "FYGG",
                        "time": "2017年01月01日"
                    },
                    {
                        "identificationNO": "4206841986****1518",
                        "sex": "",
                        "id": " XXX ",
                        "address": "",
                        "email": "",
                        "name": "XXX",
                        "phone": "",
                        "sourceName": "催收律师函",
                        "principal": 685.98,
                        "penalty": 1,
                        "mobile": "",
                        "recordTime": 1431532800000,
                        "content": "XXX",
                        "court": "",
                        "dataType": "WDHMD",
                        "time": "2015年05月14日"
                    },
                    {
                        "caseType": "",
                        "caseCause": "",
                        "status": "移送待接收",
                        "name": "XXX",
                        "id": "XXX ",
                        "recordTime": 1489075200000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "AJLC",
                        "time": "2016年09月13日"
                    },
                    {
                        "party": "XXX",
                        "title": "XXX",
                        "caseCause": "诈骗罪",
                        "courtroom": "第十一审判法庭",
                        "id": " XXX ",
                        "recordTime": 1487295000000,
                        "content": "XXX",
                        "caseNO": "XXX",
                        "court": "XXX",
                        "dataType": "KTGG",
                        "time": "2016年09月13日"
                    }
                ],
                "statistic": {
                    "ktggResultSize": 0,
                    "cpwsResultSize": 0,
                    "zxggResultSize": 0,
                    "sxggResultSize": 0,
                    "fyggResultSize": 0,
                    "wdhmdResultSize": 0,
                    "ajlcResultSize": 0,
                    "bgtResultSize": 0
                },
                "checkStatus": "EXIST"
            }
        }
    }
}}
