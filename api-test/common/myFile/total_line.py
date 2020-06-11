#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019-05-13 下午 2:16
@Author     : 罗林
@File       : total_line.py
@desc       : 统计代码行数
"""

import os

# 指定想要统计的文件类型
whitelist = ['.py']


# 遍历文件, 递归遍历文件夹中的所有
def getFile(basedir):
    filelists = list()
    for parent, dirnames, filenames in os.walk(basedir):
        for filename in filenames:
            name, suf = os.path.splitext(filename)
            # 只统计指定的文件类型，略过一些log和cache文件
            if suf in whitelist:
                filelists.append(os.path.join(parent, filename))
    return filelists


def countLine(fname):
    # 统计一个文件的行数
    count = 0
    for file_line in open(fname, 'r', encoding='utf-8').readlines():
        if file_line != '' and file_line != '\n':  # 过滤掉空行和注释行
            count += 1
    return count


def total_line(basedir):
    filelists = getFile(basedir)
    totalline = 0
    for filelist in filelists:
        totalline += countLine(filelist)
    return totalline


if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    dir_path = os.path.join(dir_path, 'xqkj')
    print(dir_path)
    print(total_line(dir_path))
