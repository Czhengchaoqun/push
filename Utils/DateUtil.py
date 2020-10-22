"""
日期工具类
"""
import time
import datetime


def get_str_date(day=0, format='%Y-%m-%d'):
    """获取格式化日期"""
    return (datetime.datetime.now() + datetime.timedelta(days=day)).strftime(format)


def get_excel_str_date(day=0):
    """获取读取excel格式化时间"""
    now = (datetime.datetime.now() + datetime.timedelta(days=day))
    str_date = str(now.month) + '.' + str(now.day)
    return str_date


if __name__ == '__main__':
    print(get_excel_str_date(day=1))
