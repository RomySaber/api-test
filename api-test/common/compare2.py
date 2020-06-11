#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
1.difflib的HtmlDiff类创建html表格用来展示文件差异，通过make_file方法
2.make_file方法使用
make_file(fromlines, tolines [, fromdesc][, todesc][, context][, numlines])
用来生成一个包含表格的html文件，其内容是用来展示差异。
fromlines和tolines,用于比较的内容，格式为字符串组成的列表
fromdesc和todesc，可选参数，对应的fromlines,tolines的差异化文件的标题，默认为空字符串
context 和 numlines，可选参数，context 为True时，只显示差异的上下文，为false，显示全文，numlines默认为5，
当context为True时，控制展示上下文的行数，当context为false时,控制不同差异的高亮之间移动时“next”的开始位置
3.使用argparse传入两个需要对比的文件
"""
import difflib
import argparse
import sys
import os
import platform

class cmpFile:

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def fileExists(self):
        if os.path.exists(self.file1) and \
                os.path.exists(self.file2):
            return True
        else:
            return False

    # 对比文件不同之处, 并返回结果
    def compare(self):
        if cmpFile(self.file1, self.file2).fileExists() == False:
            return []

        fp1 = open(self.file1,encoding='utf-8')
        fp2 = open(self.file2,encoding='utf-8')
        flist1 = [i for i in fp1]
        flist2 = [x for x in fp2]
        fp1.close()
        fp2.close()
        flines1 = len(flist1)
        flines2 = len(flist2)

        if flines1 < flines2:
            flist1[flines1:flines2+1] = ' ' * (flines2 - flines1)
        if flines2 < flines1:
            flist2[flines2:flines1+1] = ' ' * (flines1 - flines2)

        counter = 1
        cmpreses = []
        for x in zip(flist1, flist2):
            if x[0] == x[1]:
                counter +=1
                continue
            if x[0] != x[1]:
                cmpres = '%s和%s第%s行不同, 内容为:\n %s\n -->\n %s\n' % \
                         (self.file1, self.file2, counter, x[0].strip(), x[1].strip())
                cmpreses.append(cmpres)
                counter +=1
        return cmpreses


# 创建打开文件函数，并按换行符分割内容
def readfile(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as fileHandle:
            text = fileHandle.read().splitlines()
        return text
    except IOError as e:
        print("Read file Error:", e)
        sys.exit()


# 比较两个文件并输出到html文件中
def diff_file(filename1, filename2):
    cmpfile = cmpFile(filename1,filename2 )
    difflines = cmpfile.compare()
    for k in difflines:
        print(k, end='\n')
    text1_lines = readfile(filename1)
    text2_lines = readfile(filename2)
    d = difflib.HtmlDiff()
    # context=True时只显示差异的上下文，默认显示5行，由numlines参数控制，context=False显示全文，差异部分颜色高亮，默认为显示全文
    result = d.make_file(text1_lines, text2_lines, filename1, filename2, context=True)
    # 内容保存到result.html文件中
    resylt = os.path.join(os.path.dirname(__file__), 'api_diff/result.html')
    print(resylt)
    with open(resylt, 'a') as resultfile:
        resultfile.write(result)
    filename11=''
    filename22=''
    # print(result)


if __name__ == '__main__':
    # 定义必须传入两个参数，使用格式-f1 filename1 -f2 filename
    # parser = argparse.ArgumentParser(description="传入两个文件参数")
    # parser.add_argument('-f1', action='store', dest='filename1', required=True)
    # parser.add_argument('-f2', action='store', dest='filename2', required=True)
    # given_args = parser.parse_args()
    # filename1 = given_args.filename1
    # filename2 = given_args.filename2
    # filename1='E:\grpc\interface\core\\testsort1.6.2base.txt'
    # filename2='E:\grpc\interface\\2.1.0APP_1\\testsort2.1.0APPtestsort.txt'
    # filename1 = 'E:\grpc\interface\\app2.0.0\\testsort2.0.0APPtestbase.txt'
    file_path = os.path.dirname(__file__)
    filename1 = os.path.join(file_path, 'reborn/testAction/Reborn_serviceAction.py')
    filename2 = os.path.join(file_path, 'reborn/testAction/BusinessAction.py')
    if "Windows" in platform.system():
        filename1 = filename1.replace("/", "\\")
        filename2 = filename2.replace("/", "\\")
    diff_file(filename1, filename2)
