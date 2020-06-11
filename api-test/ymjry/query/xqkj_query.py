#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-23 下午 5:24
@Author     : 罗林
@File       : easyloan_query.py
@desc       : 
"""

import uuid

from common.mydb import MysqlClent as mydb
from ymjry.testAction import loginAction as la


def get_info(table_name, column, *condition):
    string_list = list()
    if len(condition) == 0:
        info = mydb.select(la.DB, table_name, column)
    else:
        info = mydb.select(la.DB, table_name, column, ' AND '.join(condition))
    if len(info) > 0:
        string_list = [i if i is not None else '' for i in info[0]]
    return string_list


def get_tbl_infos(table_name, column, *condition):
    if len(condition) == 0:
        info_list = mydb.select_col(la.DB, table_name, column)
    else:
        info_list = mydb.select_col(la.DB, table_name, column, ' AND '.join(condition))
    return info_list


def delete_info(table_name, condition):
    mydb.delete(la.DB, table_name, condition)


def delete_infos(table_names, condition_column, condition_value_list=None):
    if isinstance(table_names, str):
        table_names = [table_names]
    for table_name in table_names:
        if condition_value_list is None:
            continue
        if len(condition_value_list) > 1:
            condition = '{0} IN {1}'.format(condition_column, tuple(condition_value_list))
        elif len(condition_value_list) == 1:
            value = condition_value_list[0]
            if isinstance(value, str):
                condition = '{0}="{1}"'.format(condition_column, value)
            else:
                condition = '{0}={1}'.format(condition_column, value)
        else:
            continue
        mydb.delete(la.DB, table_name, condition)


def select_infos(table_name, col_name, condition_column, condition_value_list):
    if len(condition_value_list) > 1:
        condition = '{0} IN {1}'.format(condition_column, tuple(condition_value_list))
    elif len(condition_value_list) == 1:
        value = condition_value_list[0]
        if isinstance(value, str):
            condition = '{0}="{1}"'.format(condition_column, value)
        else:
            condition = '{0}={1}'.format(condition_column, value)
    else:
        condition = None
    return mydb.select_col(la.DB, table_name, col_name, condition)


def update_info(table_name, value, condition):
    mydb.update(la.DB, table_name, value, condition)


def get_contract_uuid_for_user(user_uuid=None):
    if user_uuid is None:
        user_uuid = la.get_user_uuid()
    la.LOGGER.info('user_uuid : {}'.format(user_uuid))
    return mydb.select_one(la.DB, 'Tbl_Contract', 'contract_uuid',
                           "user_uuid='{}' ORDER BY id DESC".format(user_uuid))


def get_contract_uuid_for_machine():
    condtion = ["qifa_machine_audit='qifa_merchant_audit_pass'", "submit_state='submit_submit'",
                "contract_state='active'"]
    return mydb.select_one(la.DB, 'Tbl_Contract', 'contract_uuid', ' AND '.join(condtion))


def get_sysdata():
    sysdatas = list()
    parent_ids = mydb.select(la.DB, 'Tbl_SysDataEnumConfig', 'id',
                             'datum_type = "datum_type_incoming" AND item_code != "incoming_tbxx"')
    parents = [i[0] for i in parent_ids]
    for parent_id in parents:
        sysdata = mydb.select(la.DB, 'Tbl_SysDataEnumConfig', 'id', 'parent_id = {}'.format(parent_id))
        sysdatas.extend([i[0] for i in sysdata])
    sysdatas.extend(parents)
    return [{"id": i} for i in sysdatas]


def update_contract_state(contract_uuid, state_dict):
    # 修改订单状态
    la.LOGGER.info('contract_uuid : {}'.format(contract_uuid))
    states = {"repayment_state": {"未开始": 'repayment_state_not_begin', "还款中": 'repayment_state_doing',
                                  "已完成": 'repayment_state_settle'},
              "bill_state": {"待出账": 'bill_state_pending', "已出账": 'bill_state_finish'},
              "loan_state": {"待放款": 'loan_state_pending', "放款中": 'loan_state_doing',
                             "放款成功": 'loan_state_pass', "放款失败": 'loan_state_fail'},
              "contract_state": {"未生效": 'not_active', "生效": 'active', "失效": 'invalid'},
              "final_check": {"终审中": 'final_check_pending', "终审通过": 'final_check_pass',
                              "终审失败": 'final_check_fail', "终审取消": 'final_check_cancel'},
              "telephone_check": {"电核中": 'telephone_check_pending', "电核通过": 'telephone_check_pending_pass',
                                  "电核失败": 'telephone_check_pending_fail', "电核取消": 'telephone_check_cancel'},
              "first_check": {"初审中": 'first_check_pending', "初审通过": 'first_check_pass',
                              "初审失败": 'first_check_fail', "初审取消": 'first_check_cancel'},
              "submit_state": {"提交中": 'submit_pending', "提交成功": 'submit_submit'},
              "qifa_machine_audit": {"风控规则预置中": 'qifa_machine_audit_pending',
                                     "风控规则预置通过": 'qifa_merchant_audit_pass',
                                     "风控规则预置失败": 'qifa_merchant_audit_fail'}}
    value_dict = dict()
    for k, v in state_dict.items():
        state_dict = states[k]
        if v in state_dict.keys():
            state_value = state_dict[v]
        else:
            state_value = '{}_unknown'.format(k)
        value_dict[k] = state_value
    la.LOGGER.info('修改Tbl_Contract的值{}'.format(value_dict))
    mydb.update_dict(la.DB, 'Tbl_Contract', value_dict, 'contract_uuid="{}"'.format(contract_uuid))


def update_contract_machine_first_check(contract_uuid):
    """
    删除初审信息，修改订单为机审完成状态
    :param contract_uuid:  订单UUID
    :return:
    """
    condtion = "contract_uuid='{0}'".format(contract_uuid)
    la.LOGGER.info(condtion)
    mydb.delete(la.DB, 'Tbl_FirstCheckLog', condtion)
    contract_state = {"qifa_machine_audit": "风控规则预置通过", "submit_state": "提交成功",
                      "contract_state": "生效", "first_check": "初审中"}
    update_contract_state(contract_uuid, contract_state)


def update_contract_machine_telephone_check(contract_uuid):
    """
    删除电审信息，修改订单为初审通过状态
    :param contract_uuid:  订单UUID
    :return:
    """
    condtion = "contract_uuid='{0}'".format(contract_uuid)
    la.LOGGER.info(condtion)
    mydb.delete(la.DB, 'Tbl_TelephoneCheckLog', condtion)
    contract_state = {"qifa_machine_audit": "风控规则预置通过", "submit_state": "提交成功",
                      "contract_state": "生效", "first_check": "初审通过", "telephone_check": "电核中"}
    update_contract_state(contract_uuid, contract_state)


def update_contract_machine_final_check(contract_uuid):
    """
    删除终信息，修改订单为电审完成状态
    :param contract_uuid:  订单UUID
    :return:
    """
    condtion = "contract_uuid='{0}'".format(contract_uuid)
    la.LOGGER.info(condtion)
    mydb.delete(la.DB, 'Tbl_FinalCheckLog', condtion)
    contract_state = {"qifa_machine_audit": "风控规则预置通过", "submit_state": "提交成功",
                      "contract_state": "生效", "first_check": "初审通过", "telephone_check": "电核通过",
                      "final_check": "终审中"}
    update_contract_state(contract_uuid, contract_state)


def update_contract_machine_pass(contract_uuid, user_uuid):
    """
    修改订单状态，绕过机审和签订合同
    :param contract_uuid: 订单UUID
    :param user_uuid: 用户UUID
    :return:
    """
    la.LOGGER.info('contract_uuid : {0} user_uuid : {1}'.format(contract_uuid, user_uuid))
    contract_state = {"qifa_machine_audit": "风控规则预置通过", "submit_state": "提交成功",
                      "contract_state": "生效"}
    update_contract_state(contract_uuid, contract_state)
    value_dict = {"loan_periods": 3}
    mydb.update_dict(la.DB, 'Tbl_Contract', value_dict, 'contract_uuid="{}"'.format(contract_uuid))
    get_uuid = lambda x: ''.join(str(x).split('-'))
    contract_info_col = ['contract_info_uuid', 'contract_uuid', 'fdd_number', 'contract_name', 'type', 'platform',
                         'sign_state', 'view_url', 'download_url', 'state']
    # contract_name = ["分期还款服务合同", "委托付款函", "通知函"]
    contract_name = ['服务完结确认书', '应收账款转让协议书', '债权转让通知书', '居间服务协议', '医疗美容项目服务合同']
    condtion = ['contract_uuid="{}"'.format(contract_uuid)]
    for _name in contract_name:
        _edtion = 'contract_name="{}"'.format(_name)
        condtion.append(_edtion)
        contract_info_rows = mydb.select_rows(la.DB, 'Tbl_ContractInfo', 'id', ' AND '.join(condtion))
        # if contract_info_rows == 0:
        #     contract_info = mydb.select(la.DB, 'Tbl_ContractInfo', ','.join(contract_info_col), condtion[1])[0]
        #     la.LOGGER.info('查询Tbl_ContractInfo中"{0}"的值{1}'.format(_name, contract_info))
        #     contract_info[0:2] = get_uuid(uuid.uuid1()), contract_uuid
        #     la.LOGGER.info('插入Tbl_ContractInfo中"{0}"的值{1}'.format(_name, contract_info))
        #     mydb.insert(la.DB, 'Tbl_ContractInfo', dict(zip(contract_info_col, contract_info)))
        condtion.remove(_edtion)
    translog_rows = mydb.select_rows(la.DB, 'Tbl_TransLog', 'id', "user_id='{}'".format(user_uuid))
    if not translog_rows:
        translog_dict = {'out_id': '2019112910110111420480', 'trans_log_uuid': get_uuid(uuid.uuid1()),
                         'trans_seq_id': '2019112911111294628672', 'user_id': user_uuid, 'cust_id': '',
                         'trans_type': 'trans_type_P001', 'trans_amt': 1000, 'fee_amt': 0.0,
                         'trans_state': 'trans_state_S', 'resp_code': '', 'err_code': '',
                         'chk_state': 'chk_state_S', 'bank_state': 'bank_state_S', 'oper_seq_id': '',
                         'trans_name': 'testAPI', 'trans_obj': 'testAPI',
                         'card_acct_type': 'card_acct_type_private', 'card_id': '213105529995110',
                         'card_opening_bank': '招商银行', 'card_acct_name': 'testAPI',
                         'card_line_num': '34646546', 'bank_remark': 'testAPI', 'bank_seq_id': '',
                         'acct_seq_id': '', 'ret_fee': 'ret_fee_no', 'bank_proc_desc': '', 'gate_id': '',
                         'pay_channel_id': '', 'cash_type': 'cash_type_T0', 'state': 'enabled',
                         'business_data': ''}
        la.LOGGER.info('插入Tbl_TransLog的值{}'.format(translog_dict))
        # 交易流水表 新增数据
        mydb.insert(la.DB, 'Tbl_TransLog', translog_dict)
    qifamachinelog_rows = mydb.select_rows(la.DB, 'Tbl_QifaMachineLog', 'id', condtion[0])
    if qifamachinelog_rows == 0:
        qifamachinelog_col = ['qifa_machine_log_uuid', 'contract_uuid', 'qifa_machine_audit', 'score',
                              'risk_warning', 'state']
        qifamachinelog_value = [get_uuid(uuid.uuid1()), contract_uuid, 'qifa_merchant_audit_pass', '67',
                                '中风险，建议核查', 'enabled']
        la.LOGGER.info('插入Tbl_QifaMachineLog的值{}'.format(qifamachinelog_value))
        # 系统机审表 新增数据
        mydb.insert(la.DB, 'Tbl_QifaMachineLog', dict(zip(qifamachinelog_col, qifamachinelog_value)))
    condtion.append('user_uuid="{}"'.format(user_uuid))
    user_ocr_info_rows = mydb.select_rows(la.DB, 'Tbl_UserOcrInfo', 'id', ' AND '.join(condtion))
    if user_ocr_info_rows == 0:
        user_ocr_info_col = ['user_ocr_uuid', 'contract_uuid', 'user_uuid', 'first_key', 'second_key', 'third_key',
                             'qiniu_config_id', 'authentication_state', 'state', 'note']
        user_ocr_info_value = mydb.select(la.DB, 'Tbl_UserOcrInfo', ','.join(user_ocr_info_col), 'note IS NOT NULL')[0]
        la.LOGGER.info('查询Tbl_UserOcrInfo的值{}'.format(user_ocr_info_value))
        user_ocr_info_value[0:3] = get_uuid(uuid.uuid1()), contract_uuid, user_uuid
        user_ocr_info_value[-1] = str(user_ocr_info_value[-1]).replace('\"', '\\\"')
        la.LOGGER.info('插入bl_UserOcrInfo的值{}'.format(user_ocr_info_value))
        # 客户OCR信息表 新增人脸识别数据
        mydb.insert(la.DB, 'Tbl_UserOcrInfo', dict(zip(user_ocr_info_col, user_ocr_info_value)))
    user_personal_info_rows = mydb.select_rows(la.DB, 'Tbl_UserPersonalInfo', 'id', ' AND '.join(condtion))
    if user_personal_info_rows == 0:
        user_personal_info_col = ['user_person_uuid', 'contract_uuid', 'user_uuid', 'datum_type_marry_id',
                                  'datum_type_education_id', 'datum_type_housing_id', 'live_province',
                                  'live_province_name', 'live_city', 'live_city_name', 'live_region',
                                  'live_region_name', 'live_detail', 'state']
        user_personal_info_value = mydb.select(la.DB, 'Tbl_UserPersonalInfo', ','.join(user_personal_info_col))[0]
        la.LOGGER.info('查询Tbl_UserPersonalInfo的值{}'.format(user_personal_info_value))
        user_personal_info_value[0:3] = get_uuid(uuid.uuid1()), contract_uuid, user_uuid
        la.LOGGER.info('插入Tbl_UserPersonalInfo的值{}'.format(user_personal_info_value))
        # 客户个人信息表 新增和订单关联的数据
        mydb.insert(la.DB, 'Tbl_UserPersonalInfo', dict(zip(user_personal_info_col, user_personal_info_value)))
    user_work_info_rows = mydb.select_rows(la.DB, 'Tbl_UserWorkInfo', 'id', ' AND '.join(condtion))
    if user_work_info_rows == 0:
        user_work_info_col = ['user_work_uuid', 'contract_uuid', 'user_uuid', 'company_name', 'position',
                              'work_phone', 'datum_type_income_id', 'datum_type_worktime_id', 'company_province',
                              'company_province_name', 'company_city', 'company_city_name', 'company_region',
                              'company_region_name', 'company_detail', 'state']
        user_work_info_value = mydb.select(la.DB, 'Tbl_UserWorkInfo', ','.join(user_work_info_col))[0]
        la.LOGGER.info('查询Tbl_UserWorkInfo的值{}'.format(user_work_info_value))
        user_work_info_value[0:3] = get_uuid(uuid.uuid1()), contract_uuid, user_uuid
        la.LOGGER.info('插入Tbl_UserWorkInfo的值{}'.format(user_work_info_value))
        # 客户工作信息表 新增和订单关联的数据
        mydb.insert(la.DB, 'Tbl_UserWorkInfo', dict(zip(user_work_info_col, user_work_info_value)))
    user_contact_info_rows = mydb.select_rows(la.DB, 'Tbl_UserContactInfo', 'id', ' AND '.join(condtion))
    user_contact_info_col = ['user_contact_uuid', 'contract_uuid', 'user_uuid', 'name', 'phone',
                             'datum_type_contact_id', 'state']
    user_contact_info_value = mydb.select(la.DB, 'Tbl_UserContactInfo', ','.join(user_contact_info_col))[0]
    la.LOGGER.info('查询Tbl_UserContactInfo的值{}'.format(user_contact_info_value))
    user_contact_info_value[0:3] = get_uuid(uuid.uuid1()), contract_uuid, user_uuid
    if user_contact_info_rows == 0:
        # 客户联系人信息表 新增和订单关联的数据
        la.LOGGER.info('插入Tbl_UserContactInfo的值{}'.format(user_contact_info_value))
        mydb.insert(la.DB, 'Tbl_UserContactInfo', dict(zip(user_contact_info_col, user_contact_info_value)))
    elif user_contact_info_rows > 1:
        mydb.delete(la.DB, 'Tbl_UserContactInfo',
                    "contract_uuid='{0}' AND user_uuid='{1}'".format(contract_uuid, user_uuid))
        la.LOGGER.info('插入Tbl_UserContactInfo的值{}'.format(user_contact_info_value))
        mydb.insert(la.DB, 'Tbl_UserContactInfo', dict(zip(user_contact_info_col, user_contact_info_value)))


def get_label_uuid(contact_uuid):
    contact_uuid = mydb.select(la.DB, 'Tbl_ContractCustomerLabel', 'contract_customer_label_uuid',
                               "contract_uuid='{}' ORDER BY id DESC".format(contact_uuid))
    return contact_uuid[0][0]


def get_collection_uuid(platform_user_profile_uuid):
    """
    根据系统用户uuid，查询催收人员uuid
    """
    return mydb.select(la.DB, 'Tbl_PlatformUserProfileCollection', 'collection_uuid',
                       "platform_user_profile_uuid='{}'".format(platform_user_profile_uuid))[0][0]


def del_collection(platform_user_profile_uuid):
    """
    根据系统用户uuid，删除催收人员
    """
    mydb.delete(la.DB, 'Tbl_PlatformUserProfileCollection',
                'platform_user_profile_uuid="{}"'.format(platform_user_profile_uuid))


def get_bill_overdue(contract_uuid, user_uuid):
    """
    生成账单，并生成逾期数据
    :param contract_uuid:  订单ID
    :param user_uuid:  用户ID
    :return:
    """
    get_uuid = lambda x: ''.join(str(x).split('-'))
    user_bill_uuid = get_uuid(uuid.uuid1())
    user_bill_overdue_uuid = get_uuid(uuid.uuid1())
    # 增加出账信息
    bill_dict = {'user_bill_uuid': user_bill_uuid, 'contract_uuid': contract_uuid, 'user_uuid': user_uuid,
                 'number': 1, 'principal': 0.3, 'handling_fee': 0.1, 'payed_principal': 0,
                 'payed_handling_fee': 0, 'overdue_state': 'overdue_state_doing', 'overdue_day': 30,
                 'overdue_principal': 0.1, 'overdue_handling_fee': 0.1, 'payed_overdue_principal': 0,
                 'last_pay_date': '2019-11-02 00:00:00', 'payed_overdue_handling_fee': 0,
                 'advance_payment_fee': 0, 'preferential_amount': 0, 'pay_state': 'pay_state_nopay',
                 'state': 'enabled'}
    mydb.insert(la.DB, 'Tbl_UserBill', bill_dict)
    # 增加逾期信息
    bill_overdue_dict = {'user_bill_overdue_stream_uuid': user_bill_overdue_uuid,
                         'contract_uuid': contract_uuid, 'user_bill_uuid': user_bill_uuid, 'number': 1,
                         'principal': 0.3, 'handling_fee': 0.1, 'payed_principal': 0, 'payed_handling_fee': 0,
                         'overdue_principal': 0.2, 'overdue_handling_fee': 0.02, 'payed_overdue_principal': 0,
                         'payed_overdue_handling_fee': 0, 'state': 'enabled'}
    mydb.insert(la.DB, 'Tbl_UserBillOverdueStream', bill_overdue_dict)


def insert_user_bankinfo(user_uuid):
    """
    增加银行卡绑定信息
    :param user_uuid:  用户id
    :return:
    """
    bank_info = {'user_bank_card_uuid': ''.join(str(uuid.uuid1()).split('-')), 'user_uuid': user_uuid,
                 'bank_name': '工商银行', 'bank_card_no': '62122202001081234', 'bank_card_mobile': '13612345678',
                 'bank_card_type': 'bank_card_type_unknown', 'bill_email': 'qa_api@78dk.com',
                 'authentication_state': 'authentication_state_pass', 'created':'2019-12-19 18:57:34',
                 'updated': '2019-12-19 18:57:34', 'state': 'enabled'}
    mydb.insert(la.DB, 'Tbl_UserBankCardInfo', bank_info)


if __name__ == '__main__':
    del_collection('ca4e5ffe45a24c429f72a9978e4fdcc1')
