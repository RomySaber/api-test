#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019/02/21 0003 下午 1:48
@Author     : 罗林
@File       : FileUtils.py
@desc       :
"""
import json
import os
import platform
import re
import socket
import uuid


def is_ch(word):
    # 判断字符串是否包含中文字符
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


def is_start_num(str_url):
    # 包含数组中的特定字符
    words = ['127', '192', 'dev']
    flag = False
    for word in words:
        if str_url.startswith(word):
            flag = True
            break
    return flag


def is_special_char(str1):
    # 包含特殊字符
    patrn = '[`~!@#$%^&*()\+=<>?"{}|,\'\\[\]·~！@#￥%……&*（）\+={}|《》？：“”【】、;；‘’，。、]'
    if re.findall(patrn, str1):
        return True
    else:
        return False


def is_special_str(str1):
    # 包含数组中的特定字符
    words = ['MyToken', '.jpg', 'token']
    flag = False
    for word in words:
        if word in str1:
            flag = True
            break
    return flag


def is_valid(str1):
    """
    判断URL是否有效
    :param str1: 需要判断的字符串
    :return:
    """
    if any([is_ch(str1), is_special_char(str1), is_special_str(str1)]):
        return False
    else:
        return True


def getFileList(path, fileList):
    """遍历文件夹"""
    if os.path.isfile(path):
        fileList.append(path)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            newDir = os.path.join(path, s)
            getFileList(newDir, fileList)
    return fileList


def mkdir(path):
    # 创建文件夹
    if os.path.exists(path):
        # 判断路径是否存在
        if os.path.isfile(path):
            # 判断路径是否是文件
            os.makedirs(path)
    else:
        os.makedirs(path)


def write(filepath, sb):
    # 写入文件,不会换行，需要自己写入换行 ,文件不存在时自动生成文件
    if "Windows" in platform.system():
        filepath = filepath.replace("/", "\\")
    fp = open(filepath, "w", encoding="utf8")
    for s in sb:
        fp.write(s)
    fp.close()


def writefile(path, file_str=None, mode='a'):
    # 写入文件
    modes = {'a', 'w', 'r', 'r+', 'w+', 'a+', 'rb', 'wb', 'ab'}
    """
    r 只能读 
    r+ 可读可写，不会创建不存在的文件，从顶部开始写，会覆盖之前此位置的内容
    w+ 可读可写，如果文件存在，则覆盖整个文件，不存在则创建
    w 只能写，覆盖整个文件，不存在则创建 
    a 只能写，从文件底部添加内容 不存在则创建 
    a+ 可读可写 从文件顶部读取内容 从文件底部添加内容 不存在则创建
    rb  “b”表示处理二进制文件
    wb   “b”表示处理二进制文件
    ab    “b”表示处理二进制文件
    """
    if mode in modes:
        with open(path, mode, encoding='utf-8') as fw:
            fw.writelines(file_str)
    else:
        message = 'The input not in {},please input again '.format(modes)
        raise message


def readfile(path, file_str=None, mode='r'):
    # 读取文件
    modes = {'a', 'w', 'r', 'r+', 'w+', 'a+', 'rb', 'wb', 'ab'}
    if mode in modes:
        with open(path, mode, encoding='utf-8') as fw:
            return fw.readlines(file_str)
    else:
        message = 'The input not in {},please input again '.format(modes)
        raise message


def readline(filepath):
    # 一次只读取一行，占内存小，速度慢
    if "Windows" in platform.system():
        filepath = filepath.replace("/", "\\")
    f = open(filepath, "r", encoding="utf8")
    result = list()
    for line in f.readlines():  # 依次读取每行
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith("#"):  # 判断是否是空行或注释行
            continue  # 是的话，跳过不处理
        result.append(line)  # 保存
    result.sort()  # 排序结果
    f.close()  # 关闭文件
    return result


def create_file(filepath):
    # 创建空白文件
    if not os.path.exists(filepath):
        f = open(filepath, 'w', encoding='utf-8')
        f.close()


def read_json_file(json_file_path):
    # 读取json文件
    with open(json_file_path, 'r', encoding='utf-8') as f:
        json_str = f.read()
    if json_str == '':
        json_map = json.loads(json.dumps({}))
    else:
        json_map = json.loads(json_str)
    return json_map


def write_json_file(json_file_path, json_map):
    # 将json数据写入到文件中
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(json_map, f)


def is_windows(filepath):
    # 判断系统是否是Windows系统，如果是Windows系统就把文件地址中的"/"转换成"\"
    if "Windows" in platform.system():
        filepath = filepath.replace("/", "\\")
    return filepath


def get_mac_address():
    # 获取本机Mac地址
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e + 2] for e in range(0, 11, 2)]).upper()


def get_hostname():
    # 获取主机名
    return socket.gethostname()


def get_ip():
    # 获取IP地址
    return socket.gethostbyname(get_hostname())


def str_to_bool(str_bool):
    """
    传入值，返回bool类型
    :param str_bool: 传入的字符串值
    :return: 传入'true', '1' 返回 True， 传入 'false', '0' 返回False， 如果传入其他值，返回原值
    """
    if str(str_bool).strip(' ').lower() in ('true', '1', '1.0'):
        flag = True
    elif str(str_bool).strip(' ').lower() in ('false', '0', '0.0'):
        flag = False
    else:
        flag = str_bool
    return flag


def str_to_num(str_num, num_len=8):
    """
    字符串转换为数字类型
    :param str_num:数字字符串
    :param num_len:数字长度
    :return:  整数且小于4位直接转换成int类型整数，大于4位返回字符串，
    尝试转换成浮点数，转换成功返回float浮点数，转换失败返回字符串
    """
    str_num = re.sub('\s+', '', str_num)
    if str_num == '':
        return ''
    elif str_num.isdigit() and len(str_num) <= num_len:
        return int(str_num)
    elif str_num.split('-')[-1].isdigit() and len(str_num.split('-')[-1]) <= num_len:
        return int(str_num)
    elif str_num.lower() in ('nan', 'inf', '-inf'):
        return str_num
    elif any(filter(lambda x: len(x) > num_len, str_num.split('.'))):
        return str_num
    elif '.' in str_num:
        try:
            return float(str_num)
        except ValueError:
            return str_num
    else:
        return str_num


if __name__ == '__main__':
    print(get_mac_address())
    print(get_hostname())
    print(get_ip())
