#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 5:44
@Author     : 罗林
@File       : readyaml.py
@desc       : 读取yaml文件
"""

import yaml


def read_yaml_str(path):
    # 字符串格式读取
    f = open(path, 'r', encoding='utf-8')
    cfg = f.read()
    f.close()
    return cfg


def read_yaml_dict(path):
    # 用load方法转字典
    return yaml.load(read_yaml_str(path))
