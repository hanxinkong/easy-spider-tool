# -*- coding: utf-8 -*-
# @Time : 2022/5/30 22:46
# @Author : hanxinkong
# @File : jsons.py
# @Description : json相关工具
# @Software : PyCharm
import json
import datetime

from typing import Union, Dict, List, Optional, Any

from jsonpath import jsonpath as super_jsonpath


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)


def format_json(src_json: Union[Dict, List], ensure_ascii: bool = False, indent: Optional[int] = 4, **kwargs) -> str:
    return json.dumps(src_json, ensure_ascii=ensure_ascii, indent=indent, cls=CJsonEncoder, **kwargs)


def jsonpath(src_data: Union[Dict, List], expr: Union[str, List[str]], default: Optional[Any] = None,
             first: bool = False):
    """
    jsonpath解析
    :param src_data: 解析对象
    :param expr: jsonpath,可选多个
    :param default: 未获取到返回默认值， 默认空字符串
    :param first: `True`只返回第一个， `False`返回全部
    :return: 解析值或者 default
    """
    values = None

    if isinstance(expr, str):
        expr = [expr]

    for i in expr:
        values = super_jsonpath(src_data, i)
        # 处理值本身为None的情况
        if isinstance(values, list) and not list(filter(lambda x: x is not None, values)):
            values = False

        if values:
            break

    if values is False or len(expr) == 0:
        return default

    if first is True:
        values = values[0]

    return values


def is_format_json(wait_json_string: str) -> bool:
    # noinspection PyBroadException
    try:
        data = json.loads(wait_json_string)
        if isinstance(data, dict):
            return True
    except json.JSONDecodeError:
        pass
    return False
