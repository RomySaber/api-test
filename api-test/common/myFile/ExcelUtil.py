#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2019/02/21 0002 下午 3:49
@Author     : 罗林
@File       : ExcelUtil.py
@desc       : 读取操作Excel数据
"""

import openpyxl
import os
import xlrd

from common.myCommon.Assertion import MyError
from common.myCommon.Logger import getlog

LOG = getlog(__name__)


def read_excel_all(path, mysheet):
    # 读取Excel文件
    if not isinstance(mysheet, (int, str)):
        raise MyError('输入了错误的Sheet类型【{}】'.format(mysheet))
    try:
        workbook = xlrd.open_workbook(path)
        if isinstance(mysheet, int):
            worksheet = workbook.sheet_by_index(mysheet)
        else:
            worksheet = workbook.sheet_by_name(mysheet)
        for ia in range(0, worksheet.nrows):
            list1 = []
            for j in range(0, worksheet.ncols):
                list1.append(worksheet.cell_value(ia, j))
            yield list1
        LOG.debug('成功读取Excel文件【{0}】的Sheet【{1}】的内容'.format(path, mysheet))
    except Exception as e:
        raise MyError('读取Excel文件【{0}】的Sheet【{1}】错误，错误原因：【{2}】'.format(path, mysheet, e))


def read_excel(path, mysheet, startrow=0, endrow=None, startcol=0, endcols=None):
    # 读取Excel文件
    if not isinstance(mysheet, (int, str)):
        raise MyError('输入了错误的Sheet类型【{}】'.format(mysheet))
    try:
        # 打开Excel文件
        workbook = xlrd.open_workbook(path)
        # 读取Excel的sheet
        if isinstance(mysheet, int):
            worksheet = workbook.sheet_by_index(mysheet)
        else:
            worksheet = workbook.sheet_by_name(mysheet)
        # 获取总行数和总列数
        allrows = worksheet.nrows
        allcols = worksheet.ncols
        endrow = allrows if endrow is None else endrow
        endcols = allcols if endcols is None else endcols
        if not all(
                (isinstance(startrow, int), isinstance(endrow, int), isinstance(startcol, int),
                 isinstance(endcols, int))):
            raise MyError('开始行,结束行,开始列,结束列必须为数字，输入错误！')
        if startrow > endrow or startcol > endcols:
            raise MyError('开始行大于结束行或者开始列大于结束列，输入错误！')
        if startrow > allrows or endrow > allrows:
            raise MyError('输入行数大于总行数，输入错误！')
        if startcol > allcols or endcols > allcols:
            raise MyError('输入列数大于总列数，输入错误！')
        for ia in range(startrow, endrow):
            list1 = []
            for j in range(startcol, endcols):
                list1.append(str(worksheet.cell_value(ia, j)).strip(' ').strip(''))
            yield list1
    except Exception as e:
        raise MyError('读取Excel文件【{0}】的Sheet【{1}】错误，错误原因：【{2}】'.format(path, mysheet, e))


def read_excel_list(path, mysheet, startrow=0, endrow=None, startcol=0, endcols=None):
    excel_list = list()
    for excel_data in read_excel(path, mysheet, startrow, endrow, startcol, endcols):
        excel_list.append(excel_data)
    return excel_list


def write07Excel(path, sheetname, stus):
    # 只能写xlsx文件
    try:
        book = openpyxl.Workbook()  # 新建一个excel
        sheet = book.active
        sheet.title = sheetname  # 添加一个sheet页
        for ia in range(0, len(stus)):  # 控制行
            for j in range(0, len(stus[ia])):
                sheet.cell(row=ia + 1, column=j + 1, value=str(stus[ia][j]))
        book.save(path)  # 保存到当前目录下
        LOG.debug('成功将数据写入Excel文件【{0}】的Sheet表【{1}】中'.format(path, sheetname))
    except Exception as e:
        raise MyError('将数据写入Excel文件【{0}】的Sheet表【{1}】中失败，失败原因：{2}'.format(path, sheetname, e))


def get_sheets(path):
    worksheet = xlrd.open_workbook(path)
    sheet_names = worksheet.sheet_names()
    return sheet_names


def read_excel_all_sheet(excel_path, excel_name):
    """
    读取Excel中的所有sheet，组装成字典并加入数组
    :return:  返回多个字典组成的数组
    """
    sheets = get_sheets(os.path.join(excel_path, excel_name))
    for _sheet in sheets:
        for excel_data in ExcelUtil(excel_path, excel_name, _sheet).next():
            excel_data['sheet'] = _sheet
            yield excel_data


# 读取Excel数据 , 组成字典
class ExcelUtil(object):
    def __init__(self, excelPath, excelName, sheetName):
        """获取Excel信息"""
        datapath = os.path.join(excelPath, excelName)
        self.data = xlrd.open_workbook(datapath)
        self.table = self.data.sheet_by_name(sheetName)
        self.row = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        self.curRowNo = 1

    def next(self):
        """读取Excel数据"""
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = str(col[x]).strip()
            r.append(s)
            self.curRowNo += 1
        return r

    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True


# 读取Excel数据 , 组成字典, 返回迭代器
class ExcelIter(object):
    def __init__(self, excelPath, excelName, sheetName):
        """获取Excel信息"""
        datapath = os.path.join(excelPath, excelName)
        self.data = xlrd.open_workbook(datapath)
        self.table = self.data.sheet_by_name(sheetName)
        self.row = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols
        self.curRowNo = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curRowNo == self.rowNum:
            raise StopIteration
        s = dict()
        col = self.table.row_values(self.curRowNo)
        for j in range(self.colNum):
            s[self.row[j]] = str(col[j]).strip()
        self.curRowNo += 1
        return s


if __name__ == '__main__':

    a = ExcelIter(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                               'test_api_excel'), 'finance.xlsx', 'manage')
    print(list(a))
    # print(next(a))
    # for b in a:
    #     print(b)
