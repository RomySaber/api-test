#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-02-21 下午 5:44
@Author     : 罗林
@File       : Properties.py
@desc       :  读取properties配置文件

"""

import re
import os
import tempfile


class Properties(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r', encoding='utf-8')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception as e:
            raise e
        else:
            fopen.close()

    # 判断是否包含该key,返回bool
    def has_key(self, key):
        return key in self.properties

    # 根据key读取value
    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    # 修改/添加key=value
    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '=.*', key + '=' + value, True)


def parse(file_name):
    return Properties(file_name)


def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    # 修改配置文件中的值
    tmp_file = tempfile.TemporaryFile()  # 创建临时文件
    if os.path.exists(file_name):
        r_open = open(file_name, 'r', encoding='utf-8')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open:   # 读取原文件
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            tmp_file.write(line.encode('utf-8'))  # 写入临时文件
        if not found and append_on_not_exists:
            tmp_file.write(('\n' + to_str).encode('utf-8'))
        r_open.close()
        tmp_file.seek(0)
        content = tmp_file.read()  # 读取临时文件中的所有内容
        if os.path.exists(file_name):
            os.remove(file_name)
        w_open = open(file_name, 'w', encoding='utf-8') # 将临时文件中的内容写入原文件
        w_open.write(content.decode('utf-8'))
        w_open.close()
        tmp_file.close()  # 关闭临时文件，同时也会自动删掉临时文件
    else:
        print("file %s not found" % file_name)


if __name__ == "__main__":
    file_path = 'filename.properties'
    props = parse(file_path)  # 读取文件
    print(props.get('a.b.d'))
    props.put('a.b.d', 'v1')  # 修改/添加key=value
    print(props.get('a.b.d'))  # 根据key读取value
    print("props.has_key('a.b.d')=" + str(props.has_key('a.b.d')))  # 判断是否包含该key
