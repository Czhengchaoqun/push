"""
地址枚举
"""

"""
息知信息
"""
# 息知_巡检
QQOQ_INSPECT = {
    'url': 'https://xizhi.qqoq.net/XZ87696205d34d8c65ac72de468abb6130.channel'
}
# 息知_测试
QQOQ_TEST = {
    'url': 'https://xizhi.qqoq.net/XZ18ef591f6939789b58fa41a53dc7a216.channel'
}

"""
企业微信信息
"""
# 企业微信_巡检
WECHAT_INSPECT = {
    'tokenurl': 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
    'corpid': 'ww4e7dd8463a3f7f06',
    'corpsecret': '9NUEhhddqEjuFVsKZGUTJ1tKB8FHWwCuRDVuk9_Rj5o',
    'createchat': 'https://qyapi.weixin.qq.com/cgi-bin/appchat/create',
    'sendurl': 'https://qyapi.weixin.qq.com/cgi-bin/appchat/send',
    'chatid': 'wrsoqnCAAAv1eSA2XGqrZIUTkMbkQD-w'
}

"""
Excel信息
"""
# Excel路径
EXCEL_PATH = 'D:/巡检排班.xlsx'

"""
日志路径
"""
# 息知日志路径
PUSH_QQOQ_LOG_PATH = 'Logs/PushQQOQ.log'
# 企业微信日志路径
PUSH_WORK_WECHAT_LOG_PATH = 'Logs/PushWorkWeChat.log'
