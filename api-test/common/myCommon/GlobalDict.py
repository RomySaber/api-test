#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-10 下午 4:58
@Author     : 罗林
@File       : GlobalDict.py
@desc       : 
"""
import os
from common.myCommon.Logger import getlog
from common.myFile import FileUtils

log = getlog(__name__)


class GlobalDict(object):
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    def __init__(self, json_file_path, json_file_name):
        self.file_path = os.path.join(json_file_path, json_file_name + '.json')
        log.debug("全局变量文件存储位置{}".format(self.file_path))
        FileUtils.create_file(self.file_path)
        self.map = FileUtils.read_json_file(self.file_path)

    def set(self, **keys):
        try:
            for key_, value_ in keys.items():
                self.map[key_] = str(value_)
                log.debug(key_ + ":" + str(value_))
            FileUtils.write_json_file(self.file_path, self.map)
            log.debug("写入键对值{}".format(self.map))
        except BaseException as msg:
            log.error(msg)
            raise msg

    def del_map(self, key):
        self.map = FileUtils.read_json_file(self.file_path)
        try:
            del self.map[key]
            FileUtils.write_json_file(self.file_path, self.map)
            log.debug("删除键值{0}， 删除后数据{1}".format(key, self.map))
            return self.map
        except KeyError:
            log.error("key:'" + str(key) + "'  不存在")

    def get(self, key, default=None):
        self.map = FileUtils.read_json_file(self.file_path)
        try:
            log.debug("获取键值{0}，值为{1}".format(key, self.map[key]))
            return self.map[key]
        except KeyError:
            log.warning("键值key:'{}'  不存在".format(key))
            return default

    def read(self):
        self.map = FileUtils.read_json_file(self.file_path)
        log.debug("全局环境变量值{}".format(self.map))
        return self.map
