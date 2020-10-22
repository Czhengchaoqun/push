"""
消息推送息知
"""
import requests
from Utils.PushUtil import *
from Utils.LoggerFile import *
from Enums.AddressEnum import *

# 日志对象
logger = create_logger(PUSH_QQOQ_LOG_PATH, "push_qqoq_log")


def push(push_url):
    """推送消息"""
    excel_date = get_excel_str_date(day=1)
    if is_push(date=excel_date):
        url = push_url
        title = '{}巡检排班'.format(excel_date)
        content = get_push_content(date=excel_date)
        data = {
            'title': title,
            'content': content
        }
        res = requests.post(url=url, data=data)
        logger.info(excel_date + '巡检消息息知已推送；推送内容：' + content + '；推送结果：' + res.text)
    else:
        logger.warning(excel_date + '巡检消息息知未推送，没有在excel中获取到相关日期行')


if __name__ == '__main__':
    push(push_url=QQOQ_TEST['url'])
