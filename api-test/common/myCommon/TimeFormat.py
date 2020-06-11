#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       :2018-09-14 下午 5:44
@Author     : 罗林
@File       : TimeFormat.py
@desc       : 时间格式处理
"""
import calendar
import random
import time
from datetime import date, datetime, timedelta

from dateutil.relativedelta import relativedelta

FORMART1 = '%Y-%m-%d %H:%M:%S'
FORMART2 = '%Y-%m-%d'
FORMART3 = '%Y%m%d%H%M%S'
FORMART4 = '%Y-%m'


def time_formart(date_time, formart):
    return time.strftime(formart, date_time)


def getnow():
    # 转换成新的时间格式(2016-05-09 18:59:20)
    dt = time.strftime(FORMART1, time.localtime())
    return dt


def getnow_day():
    # 转换成新的时间格式(2016-05-09)
    dt = time.strftime(FORMART2, time.localtime())
    return dt


def get_now_day():
    return date.today()


def get_now_time():
    # 获取10位时间戳
    return int(time.time())


def get_now_time_13():
    # 获取13位时间戳,  round 四舍五入
    return int(round(time.time() * 1000))


def get_time(year, month, day):
    return date(year, month, day)


def time_stamp(dt, formart1, formart2):
    # 转换成时间数组
    timeArray = time.strptime(dt, formart1)
    # 转换成新的时间格式(20160505-20:28:54)
    dt_new = time.strftime(formart2, timeArray)
    return dt_new


def time_array(dt):
    # 转换成时间数组
    return time.strptime(dt, FORMART1)


def gettimeYear(dt):
    # 4位数年
    return time.strptime(dt, FORMART1)[0]


def get_time_Month(dt):
    # 月
    return time.strptime(dt, FORMART1)[1]


def get_time_day(dt):
    # 日
    return time.strptime(dt, FORMART1)[2]


def get_time_Hour(dt):
    # 小时
    return time.strptime(dt, FORMART1)[3]


def gettimeMin(dt):
    # 分钟
    return time.strptime(dt, FORMART1)[4]


def get_time_Sec(dt):
    # 秒
    return time.strptime(dt, FORMART1)[5]


def get_day_Week(dt):
    # 一周的第几日,0到6 (0是周一)
    return time.strptime(dt, FORMART1)[6]


def get_day_Year(dt):
    # 一年的第几日 ,1到366 (儒略历)
    return time.strptime(dt, FORMART1)[7]


def getDaylightSaving(dt):
    # 	夏令时,-1, 0, 1, -1是决定是否为夏令时的旗帜
    return time.strptime(dt, FORMART1)[8]


def mktime(timeArray):
    # 时间数组转换成时间戳
    return time.mktime(timeArray)


def time_format(format1, date1):
    # 格式化日期
    return time.strftime(format1, date1)


def getMonthCalendar(year, month):
    # 打印year年month月日历
    return calendar.month(year, month)


def isleap(year):
    # 是闰年返回True，否则为false。
    return calendar.isleap(year)


def time_between_day(start_date, end_date):
    """
    获取2天之间的时间差
    :param start_date:  '%Y-%m-%d'
    :param end_date:  '%Y-%m-%d'
    :return: 天数t
    """
    start_date = datetime.strptime(start_date, FORMART2)
    end_date = datetime.strptime(end_date, FORMART2)
    return (end_date - start_date).days


def time_between_day_out_week(start_date, end_date):
    """
    计算2个时间之间的时间差，减掉中间的周末时间
    :param start_date: '%Y-%m-%d'
    :param end_date:  '%Y-%m-%d'
    :return:  天数
    """
    days_between = time_between_day(start_date, end_date)
    weekends, leftover = divmod(days_between, 7)
    if leftover:
        start_day = (end_date - timedelta(leftover)).isoweekday()
        end_day = start_day + leftover
        if all([start_day <= 6, end_day > 6]):
            weekends += 0.5
        if all([start_day <= 7, end_day > 7]):
            weekends += 0.5
    margin = int(abs(days_between - weekends * 2)) + 1
    return margin


def datetime_toString(dt, formart):
    """
    把datetime转成字符串
    :param dt: datetime时间
    :param formart: 格式化方式
    :return: 字符串
    """
    return dt.strftime(formart)


def string_toDatetime(str_time, formart):
    """
    把字符串转成datetime
    :param str_time: 字符串时间格式
    :param formart: 格式化方式
    :return: datetime 时间
    """
    return datetime.strptime(str_time, formart)


def string_toTimestamp(str_time, formart):
    """
    把字符串转成时间戳形式
    :param formart:
    :param str_time: 字符串时间戳
    :return: 10位时间戳
    """
    return int(time.mktime(string_toDatetime(str_time, formart).timetuple()))


def string_toTimestamp_10(str_time):
    """
    把字符串转成时间戳形式
    :param str_time: 字符串时间戳
    :return: 10位时间戳
    """
    return int(time.mktime(string_toDatetime(str_time, FORMART1).timetuple()))


def string_toTimestamp_13(str_time):
    """
    把字符串转成时间戳形式
    :param str_time: 字符串时间戳
    :return: 13位时间戳
    """
    return int(round(time.mktime(string_toDatetime(str_time, FORMART1).timetuple()) * 1000))


def timestamp_toString(stamp, formart):
    """
     把时间戳转成字符串形式
    :param stamp: 时间戳
    :param formart: 格式化方式
    :return: 字符串
    """
    return time.strftime(formart, time.localtime(stamp))


def datetime_toTimestamp(dateTim):
    """
    把datetime类型转外时间戳形式
    :param dateTim: datetime类型时间
    :return: 时间戳
    """
    return time.mktime(dateTim.timetuple())


def timestamp_to_datetime(timestamp):
    """
    timestamp转换为datetime
    :param timestamp: 时间戳
    :return:
    """
    return datetime.fromtimestamp(timestamp)


def get_day_around(days, date_time=None):
    """
    获取 date_time前或后几天的日期
    :param days: 大于0代表后几天，小于0代表前几天
    :param date_time: 计算时间的日期，如2019-04-02，不填代表当天
    :return: 返回str类型的时间日期
    """
    if date_time is not None:
        t = time.strptime(date_time, FORMART2)
        y, m, d = t[0:3]
        date_ago = str(datetime(y, m, d) + timedelta(days)).split()[0]
    else:
        date_ago = str(date.today() + timedelta(days))
    return date_ago


def get_day_start_time(days, date_time=None):
    """
    获取 date_time前或后几天的日期的开始时间
    :param days: 大于0代表后几天，小于0代表前几天
    :param date_time: 计算时间的日期，如2019-04-02，不填代表当天
    :return: 返回str类型的时间日期
    """
    int_time = int(time.mktime(time.strptime(get_day_around(days, date_time), FORMART2)))
    return timestamp_toString(int_time, FORMART1)


def get_day_end_time(days, date_time=None):
    """
    获取 date_time前或后几天的日期的结束时间
    :param days: 大于0代表后几天，小于0代表前几天
    :param date_time: 计算时间的日期，如2019-04-02，不填代表当天
    :return: 返回str类型的时间日期
    """
    int_time = int(time.mktime(time.strptime(get_day_around(days + 1, date_time), FORMART2))) - 1
    return timestamp_toString(int_time, FORMART1)


def get_FirstAndLastDay_month(date_str=None):
    """
    获取指定时间月份的开始和结束时间
    :param date_str: str类型，格式“XXXX-XX-XX”
    :return: firstDay: 当月的第一天，str类型
             lastDay: 当月的最后一天，str类型
    """
    if date_str:
        year, month = date_str.split('-')[:2]
    else:
        year = date.today().year
        month = date.today().month
    year = int(year)
    month = int(month)
    monthRange = calendar.monthrange(year, month)[1]
    firstDay = date(year=year, month=month, day=1).strftime(FORMART2)
    lastDay = date(year=year, month=month, day=monthRange).strftime(FORMART2)
    return firstDay, lastDay


def get_month_around(months=0, date_time=None):
    """
    获取当前时间的前后几个月
    :param months: 大于0代表后几月，小于0代表前几月
    :param date_time: 指定时间， “XXXX-XX-XX”
    :return:  '%Y-%m'
    """
    if date_time:
        year, month = date_time.split('-')[:2]
    else:
        year = date.today().year
        month = date.today().month
    thisyear = int(year)
    thismon = int(month)
    totalmon = int(thismon + months)
    if 0 < totalmon <= 12:
        return date(year=thisyear, month=totalmon, day=1).strftime(FORMART4)
    else:
        i = totalmon // 12
        j = totalmon % 12
        if j == 0:
            i -= 1
            j = 12
        thisyear = thisyear + i
        return date(year=thisyear, month=j, day=1).strftime(FORMART4)


def get_month_ago(months=0, date_time=None):
    """
    获取当前时间的前后几个月 的 指定时间，date_time 为空代表当前时间
    :param months: 整数 (整数代表前，负数代表后)
    :param date_time: "%Y-%m-%d %H:%M:%S"
    :return:  "%Y-%m-%d %H:%M:%S"
    """
    if date_time is None:
        date_time = time.strftime(FORMART1, time.localtime())
    insert_time = datetime.strptime(date_time, FORMART1)
    temp_date = (insert_time - relativedelta(months=+ months)).strftime(FORMART1)
    return temp_date


def get_month_day_ago(months=0, date_time=None):
    """
    获取当前时间的前后几个月 的 指定时间，date_time 为空代表当前时间
    :param months: 整数 (整数代表前，负数代表后)
    :param date_time: "%Y-%m-%d"
    :return:  "%Y-%m-%d"
    """
    if date_time is None:
        date_time = time.strftime(FORMART2, time.localtime())
    insert_time = datetime.strptime(date_time, FORMART2)
    temp_date = (insert_time - relativedelta(months=+ months)).strftime(FORMART2)
    return temp_date


def time_between_month(start_day, end_day=None):
    """
    获取2个时间之间相差的月份
    :param start_day:  开始时间 XXXX:XX:XX
    :param end_day:  结束日期 XXXX:XX:XX
    :return:
    """
    start = datetime.strptime(start_day, FORMART2)
    if end_day is None:
        end = date.today()
    else:
        end = datetime.strptime(end_day, FORMART2)
    year1 = start.year
    year2 = end.year
    month1 = start.month
    month2 = end.month
    return (year2 - year1) * 12 + (month2 - month1)


def random_time(start_time, end_time, delay=0):
    """
    获取指定时间段内的随机时间
    :param start_time: 开始时间 XXXX-XX-XX XX:XX:XX
    :param end_time: 结束时间 XXXX-XX-XX XX:XX:XX
    :param delay: 延迟时间 秒
    :return:
    """
    start = datetime.strptime(start_time, FORMART1)
    end = datetime.strptime(end_time, FORMART1)
    delta = end - start
    inc = random.randrange(delta.total_seconds())
    return (start + timedelta(seconds=delay) + timedelta(seconds=inc)).strftime(FORMART1)


def random_day(start_day, end_day):
    """
    获取指定时间段内的随机日期
    :param start_day: 开始日期 XXXX-XX-XX
    :param end_day: 结束日期 XXXX-XX-XX
    :return:
    """
    start = int(time.mktime(datetime.strptime(start_day + ' 00:00:00', FORMART1).timetuple()))
    end = int(time.mktime(datetime.strptime(end_day + ' 23:59:59', FORMART1).timetuple()))
    t = random.randint(start, end)
    return time.strftime(FORMART2, time.localtime(t))


def get_nday_list(n, date_time=None):
    """
    获取指定时间前的n天列表
    :param n:  前n天
    :param date_time: 指定时间， XXXX-XX-XX
    :return:
    """
    before_n_days = list()
    if date_time is None:
        day = date.today()
    else:
        day = datetime.strptime(date_time, FORMART2)
    for i in range(n + 1):
        before_n_days.append((day - timedelta(days=i)).strftime(FORMART2))
    return before_n_days


if __name__ == '__main__':
    print(type(get_day_around(-1)))
