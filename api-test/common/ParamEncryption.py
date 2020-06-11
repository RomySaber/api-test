#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-04-18 下午 5:09
@Author     : 罗林
@File       : ParamEncryption.py
@desc       :  参数加密方法
"""

import hashlib


def param_encryption(param_dict, param_key, salt):
    """
    加密参数
    :param param_dict: 参数字典
    :param param_key: 获取加密的key
    :param salt: 盐值
    :return:返回加密后的参数
    """
    if param_key in param_dict:
        del param_dict[param_key]
    # 对list排序
    seq = sorted((k+'='+str(v)) for k, v in param_dict.items())
    # 转换字符串并添加md5值
    salt_str = '&'.join(seq) + salt
    # 获取字符串MD5
    md5str = hashlib.md5(salt_str.encode("utf-8")).hexdigest()
    param_dict[param_key] = md5str
    return param_dict
