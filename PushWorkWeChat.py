"""
消息推送企业微信
"""
import requests
import json
from Utils.PushUtil import *
from Utils.LoggerFile import *
from Enums.AddressEnum import *

# 日志对象
logger = create_logger(PUSH_WORK_WECHAT_LOG_PATH, "push_work_wechat_log")


def get_access_token(info):
    """获取token"""
    url = info['tokenurl']
    params = {
        'corpid': info['corpid'],
        'corpsecret': info['corpsecret']
    }
    res = requests.get(url=url, params=params)
    return json.loads(res.text)['access_token']


def create_chat(info, token):
    """创建群聊"""
    url = info['createchat']
    params = {
        'access_token': token
    }
    data = {
        'name': '巡检',
        'owner': 'ZhengChaoQun',
        'userlist': ['ZhengChaoQun', 'YueFeng']
    }
    res = requests.post(url=url, params=params, json=data)
    # 群聊ID：wrsoqnCAAAv1eSA2XGqrZIUTkMbkQD-w
    return res.text


def send_chat(info, token):
    """发送消息"""
    excel_date = get_excel_str_date(day=1)
    if is_push(date=excel_date):
        url = info['sendurl']
        params = {
            'access_token': token
        }
        content = get_push_content(date=excel_date)
        data = {
            'chatid': info['chatid'],
            'msgtype': 'markdown',
            'markdown': {
                'content': content
            },
            'safe': 0
        }
        res = requests.post(url=url, params=params, json=data)
        logger.info(excel_date + '巡检消息企业微信已推送；推送内容：' + content + '；推送结果：' + res.text)
    else:
        logger.warning(excel_date + '巡检消息企业微信未推送，没有在excel中获取到相关日期行')


if __name__ == '__main__':
    access_token = get_access_token(info=WECHAT_INSPECT)
    send_chat(info=WECHAT_INSPECT, token=access_token)
