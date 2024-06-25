# -*- coding: utf-8 -*-
# @Time : 2022/5/30 22:27
# @Author : hanxinkong
# @File : decorator.py
# @Description : 装饰器工具
# @Software : PyCharm
from typing import Any

import logging

logger = logging.getLogger(__name__)


def retry(num: int = 3, fail_msg: str = None, exceptions: Any = Exception):
    """
    异常重试 可针对指定异常进行重试
    :param num: 重试次数
    :param fail_msg: 重试次数
    :param exceptions: 指定异常
    :return:
    """

    def decorator(func):
        def make_decorator(*args, **kwargs):
            for i in range(num):
                try:
                    finally_func = func(*args, **kwargs)
                    return finally_func
                except exceptions as e:
                    logger.error(f'方法：{func.__name__} 错误：{e} line：{e.__traceback__.tb_lineno}')
                    logger.debug(f'方法：{func.__name__} 准备第{i + 1}次重试')

            if fail_msg is None:
                logger.error(f'方法：{func.__name__} 重试{num}次无效')
            else:
                logger.error(fail_msg)

        return make_decorator

    return decorator
