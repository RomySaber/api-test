#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018/5/3 0003 下午 3:23
@Author     : 罗林
@File       : CalcMD5.py
@desc       : 获取md5
"""

import hashlib
import os


def calcFileMd5(filePath):
    """
    获取文件夹的MD5
    :param filePath:
    :return: filePath checksum value
    """
    md5 = hashlib.md5()
    fp = open(filePath, "a")
    md5.update(fp.read())
    while True:
        block = fp.read(1048576)
        if not block:
            break
        md5.update(block)
    fp.close()
    return md5.hexdigest()


def calcStringMd5(str1):
    """
    获取字符串的MD5
    :param str1:
    :return: string checksum value
    """
    return hashlib.md5(str1.encode("utf-8")).hexdigest()


def getFileList(path, fileList):
    """遍历文件夹"""
    # newDir = path
    if os.path.isfile(path):
        fileList.append(path)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            newDir = os.path.join(path, s)
            getFileList(newDir, fileList)
    return fileList


def get_small_file_md5(file_path):
    # 获取较小文件的MD5
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


def get_large_file_md5(file_path):
    # 获取较大文件的MD5
    f = open(file_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5


def get_file_md5(path, file_dict):
    # 遍历获取文件夹MD5
    if os.path.isfile(path):
        md5_obj = hashlib.md5()
        with open(path, 'rb') as f:
            md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        md5 = str(hash_code).lower()
        file_dict[os.path.basename(path)] = md5
    elif os.path.isdir(path):
        for s in os.listdir(path):
            newDir = os.path.join(path, s)
            get_file_md5(newDir, file_dict)


def get_one_file_md5(file_path):
    # 获取文件的MD5
    md5_obj = hashlib.md5()
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            md5_obj.update(f.read())
    return md5_obj.hexdigest().lower()
