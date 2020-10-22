"""
消息推送工具类
"""
from Utils.DateUtil import *
from Utils.ExcelUtil import *
from Enums.MarkdownEnum import *
from Enums.AddressEnum import *


def is_push(date):
    """是否需推送"""
    row_data = get_rows_by_date(path=EXCEL_PATH, date=date)
    if row_data is not None and len(row_data) > 0:
        return True
    else:
        return False


def get_push_content(date):
    """获取推送内容"""
    content = '{}{}巡检排班\n'.format(THREE_LEVEL_TITLE, date)
    head_data = get_head(path=EXCEL_PATH)
    row_data = get_rows_by_date(path=EXCEL_PATH, date=date)
    for row_index in range(1, len(row_data)):
        row_val = row_data[row_index]
        head_val = head_data[row_index]
        content += '{}{}{}{}：{}\n\r'.format(PARAGRAPH_QUOTATION, BOLD, row_val, BOLD, head_val)
    content += '请关注！！！'
    return content
