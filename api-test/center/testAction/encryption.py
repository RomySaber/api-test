#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-16 下午 3:06
@Author     : 罗林
@File       : encryption.py
@desc       : 
"""
import hashlib


def get_encryption_param(param_dict, appkey):
    """
    加密参数
    :param param_dict: 参数字典
    :return:返回加密后的参数
    """
    if 'SignMsg' in param_dict:
        del param_dict['SignMsg']
    # 对list排序
    seq = sorted((k+'='+str(v)) for k, v in param_dict.items())
    # 转换字符串并添加md5值
    salt_str = '&'.join(seq) + appkey
    # 获取字符串MD5
    md5str = hashlib.md5(salt_str.encode("utf-8")).hexdigest()
    param_dict['SignMsg'] = md5str
    return param_dict
