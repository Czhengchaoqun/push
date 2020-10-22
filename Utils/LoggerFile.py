"""
日志输出工具类
"""
import logging
from logging.handlers import RotatingFileHandler


def create_logger(log_file, log_name):
    """创建日志对象"""
    my_logger = logging.getLogger(log_name)
    my_logger.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    consoleHandler.setFormatter(logging.Formatter("[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s"))
    rotatingHandler = RotatingFileHandler(log_file, maxBytes=30 * 1024 * 1024, backupCount=8, encoding='utf-8')
    rotatingHandler.setFormatter(logging.Formatter("[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s"))
    my_logger.addHandler(rotatingHandler)
    my_logger.addHandler(consoleHandler)
    return my_logger
