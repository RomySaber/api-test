#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 5:44
@Author     : 罗林
@File       : ConfigUtils.py
@desc       :  读写config文件
"""

import configparser, os, platform


class ConfigUtils(object):

    def __init__(self, file_path=None):
        if file_path is None:
            path = os.path.dirname(os.path.dirname(__file__)) + '/config.ini'
            if "Windows" in platform.system():
                path = path.replace("/", "\\")
        else:
            path = file_path
        self.path = path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.path, encoding="utf-8-sig")


def get_config(file_path=None):
    return ConfigUtils(file_path)


def write_config(section, config_name, config_value, mode='w', file_path=None):
    config = get_config(file_path)
    if section in sections():
        # 对section中的option进行设置，需要调用write将内容写入配置文件
        config.conf.set(section, config_name, config_value)
    else:
        # 写入配置文件
        config.conf.add_section(section)  # 添加一个新的section
        # 对section中的option进行设置，需要调用write将内容写入配置文件
        config.conf.set(section, config_name, config_value)
    modes = {'a', 'w', 'r', 'r+', 'w+', 'a+'}
    """
    r:读模式
    w:写模式
    a: 追加模式
    r+：可读可写，若文件不存在，报错, 进行了覆盖写；
    w+: 可读可写，若文件不存在，创建，进行了清空写；
    a+：可读可写但光标在最后面（然后读到最后面，所以读到空字符串），若文件不存在，创建，进行了追加写；
    """
    if mode in modes:
        # 写入文件
        with open(config.path, mode, encoding="utf-8-sig") as fw:
            config.conf.write(fw)
    else:
        message = 'The input not in {},please input again '.format(modes)
        raise message


def getint(section, config_name, file_path=None):
    # 获取int类型的配置数据
    config = get_config(file_path)
    return config.conf.getint(section, config_name)


def get(section, config_name, file_path=None):
    # 获取str类型的配置数据
    config = get_config(file_path)
    return config.conf.get(section, config_name).strip()


def getboolean(section, config_name, file_path=None):
    # 获取boolean类型的配置数据
    config = get_config(file_path)
    return config.conf.getboolean(section, config_name)


def getfloat(section, config_name, file_path=None):
    # 获取float类型的配置数据
    config = get_config(file_path)
    return config.conf.getfloat(section, config_name)


def read(file_path=None):
    # 读取整个配置文件
    config = get_config(file_path)
    path = config.path
    return config.conf.read(path, encoding="utf-8-sig")


def sections(file_path=None):
    # 得到所有的section，并以列表的形式返回
    config = get_config(file_path)
    return config.conf.sections()


def options(section, file_path=None):
    # 得到该section的所有option
    config = get_config(file_path)
    return config.conf.options(section)


def items(section, file_path=None):
    # 得到该section的所有键值对
    config = get_config(file_path)
    return config.conf.items(section)
