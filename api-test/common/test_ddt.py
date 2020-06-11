# coding = utf-8

import random
from common.myCommon.TestBaseCase import TestBaseCase
import ddt


def get_ddt_date():
    for i in range(10):
        yield [random.randint(1, 10), random.random(), random.uniform(10, 30), random.randrange(1, 10, 2)]


@ddt.ddt  # 装饰器
class TestDdt(TestBaseCase):
    @ddt.data(3, 4, 12, 'a', 'b', 'c')
    # 可以是数值，也可以是字符串
    def test_01_str(self, dates):
        print(dates)
        
    @ddt.data(*(('tv11', 'tv21'), ('tv12', 'tv22')))
    # 传入元组中的每个值，使用 * 表示
    # 用例名称会将测试数据做为用例名称展示
    # 将元组中的每个元组当成一个参数传入
    def test_02_tuple(self, datas):
        print(datas[0], datas[1])

    @ddt.data(*[['lv11', 'lv21'], ['lv12', 'lv22']])
    # 告诉我们的测试用例传入的是两个以上的值 使用@ddt.unpack
    @ddt.unpack
    # 定义两个参数value用于接收我们传入的参数
    # 将自动将元组和列表解压缩为多个参数，并将字典解压缩为多个关键字参数
    def test_03_list(self, value1, value2):
        print(value1, value2)

    @ddt.data(*[{'one': 1, 'two': 2}, {'one': 'a', 'two': 'b'}])
    # 用例名称 不会将测试数据做为用例名称展示 ，名称展示为dict()
    @ddt.unpack
    def test_04_dict(self, one, two):
        print(one, two)

    @ddt.data(('tv11', 'tv21'), ('tv12', 'tv22'))
    # 传入多个元组，
    @ddt.unpack
    def test_05_tuple(self, value1, value2):
        print(value1, value2)

    @ddt.data(['lv11', 'lv21'], ['lv12', 'lv22'])
    @ddt.unpack
    def test_06_list(self, value1, value2):
        print(value1, value2)

    @ddt.data({'one': 1, 'two': 2}, {'one': 'a', 'two': 'b'})
    @ddt.unpack
    def test_07_dict(self, one, two):
        print(one, two)

    @ddt.data(('tv11', 'tv21'), ('tv12', 'tv22'))
    # 传入多个元组，每个元组当成1个参数传入
    def test_08_tuple(self, dates):
        print(dates[0], dates[1])

    @ddt.data(['lv11', 'lv21'], ['lv12', 'lv22'])
    def test_09_list(self, dates):
        print(dates[0], dates[1])

    @ddt.data({'one': 1, 'two': 2}, {'one': 'a', 'two': 'b'})
    def test_10_dict(self, dates):
        print(dates['one'], dates['two'])
        print(*dates.keys())
        print(*dates.values())

    @ddt.data(*get_ddt_date())
    # 从自定义的方法中获取测试数据，原理同上面的方法
    def test_11_fun(self, datas):
        print(datas[0], datas[1], datas[2], datas[3])

    @ddt.file_data('./myFile/test_data_dict_dict.json')
    # 将json文件的 value读取出来，每次传入一个value，测试用例名称显示为key
    def test_12_json_file(self, datas):
        print('this is json file')
        print(datas)

    @ddt.file_data('./myFile/test_data_dict_dict.yml')
    # 将yaml文件的 value读取出来，每次传入一个value，测试用例名称显示为key
    def test_13_yml_file(self, datas):
        print('this is yml')
        print(datas)

    @ddt.data(u'ascii', u'non-ascii-\N{SNOWMAN}')
    def test_14_unicode(self, value):
        print(value)
        self.assertIn(value, (u'ascii', u'non-ascii-\N{SNOWMAN}'))
