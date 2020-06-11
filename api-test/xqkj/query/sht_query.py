#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2019-08-16
@Author     : 罗林
@File       : sht_query.py
@desc       : 商户通数据查询
"""

from common.mydb import MysqlClent
from xqkj.testAction import loginAction

DB = loginAction.DB


def get_merchant_uuid(open_id):
    """
    通过 微信的 open_id查询商户UUID
    :param open_id:  微信的 open_id
    :return:
    """
    return MysqlClent.select_one(DB, "Tbl_WX_User", "merchant_uuid", "open_id='{}'".format(open_id))


def get_merchant_uuid_merchant_name(merchant_name):
    """
    通过 商户名称 查询商户的UUID
        N m.merchant_uuid=log.opt_uuid
        WHERE m.merchant_uuid=#{uuid} AND m.state='enabled'
    :param merchant_name:  商户名称
    :return:
    """
    return MysqlClent.select_one(DB, "Tbl_MerchantProfile", "merchant_uuid",
                                 "name='{}' AND state='enabled'".format(merchant_name))


def get_merchant_name(merchant_uuid):
    """
    根据商户UUID 查询商户名称
    :param merchant_uuid:
    :return:
    """
    return MysqlClent.select_one(DB, "Tbl_MerchantProfile", "name", "merchant_uuid='{}'".format(merchant_uuid))


def update_open_uuid(open_id_old, open_id_new):
    """
    修改 微信 open_id
    :param open_id_old: 修改前 open_id
    :param open_id_new: 修改后 open_id
    :return:
    """
    MysqlClent.update(DB, "Tbl_WX_User", "open_id='{}'".format(open_id_new), "open_id='{}'".format(open_id_old))


def update_state(merchant_uuid):
    """
    更新商户 数据状态 为 enabled
    :param merchant_uuid: 商户的UUID
    :return:
    """
    MysqlClent.update(DB, "Tbl_MerchantProfile", "state='enabled'", "merchant_uuid='{}'".format(merchant_uuid))


def update_audit_state(audit_state, merchant_uuid):
    """
    更新商户审核状态
    :param audit_state: 审核状态
    :param merchant_uuid: 商户的UUID
    :return:
    """
    MysqlClent.update(DB, "Tbl_MerchantProfile", "audit_state='{}'".format(audit_state),
                      "merchant_uuid='{}'".format(merchant_uuid))


def update_open_close_state(open_close_state, merchant_uuid):
    """
    更新商户开启状态
    :param open_close_state: 开启状态
    :param merchant_uuid: 商户的UUID
    :return:
    """
    MysqlClent.update(DB, "Tbl_MerchantProfile", "open_close_state='{}'".format(open_close_state),
                      "merchant_uuid='{}'".format(merchant_uuid))


def insert_OptLog(merchant_uuid):
    """
    插入审核 日志
    :param merchant_uuid: 商户的UUID
    :return:
    """
    values = {"opt_log_uuid": "3ca5f41cf27f40229adea5e152d3bb67", "opt_uuid": merchant_uuid,
              "audit_user_uuid": "109e99a3720a4a1a8b977ce0766bd2c3", "audit_user_name": "luolin",
              "opt_log_type": "Merchant", "opt_state_type": "Audit", "opt_result": "pass",
              "created": "2019-08-16 06:36:07", "updated": "2019-08-16 06:36:07", "state": "enabled"}
    MysqlClent.insert(DB, "Tbl_OptLog", values)


def update_pass_store_state(audit_state, store_uuid):
    """
    插入审核 日志
    :param audit_state: 更新状态
    :param store_uuid: 门店的UUID
    :return:
    """
    MysqlClent.update(DB, "Tbl_Store", "audit_state ='{}'".format(audit_state), "store_uuid ='{}'".format(store_uuid))


def get_store_uuid(storename):
    """
    通过 微信的 open_id查询商户UUID
    :param storename:  微信的 storename
    :return:
    """
    return MysqlClent.select_one(DB, "Tbl_Store", "store_uuid", "store_name='{}'".format(storename))


def get_merchant_number(merchant_uuid):
    """
    通过商户 UUID 查询商户 编号
    :param merchant_uuid: 商户 UUID
    :return:
    """
    return MysqlClent.select_one(DB, "Tbl_MerchantProfile", "temporary_code",
                                 "merchant_uuid='{}'".format(merchant_uuid))


def update_wx_merchart_null(merchant_uuid=None):
    """
    更新 商户的UUID为空
    :return:
    """
    if merchant_uuid is None:
        uuid = ''
    else:
        uuid = merchant_uuid
    MysqlClent.update(DB, "Tbl_WX_User", "merchant_uuid='{}'".format(uuid),
                      "wx_user_uuid='{}'".format(loginAction.wxUserUuid))
