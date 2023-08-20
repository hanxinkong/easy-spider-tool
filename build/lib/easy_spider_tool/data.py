from typing import Dict, Any


def cookie_to_dic(cookie: str) -> Dict[str, Any]:
    if cookie:
        return {item.split('=')[0]: '='.join(item.split('=')[1:]) for item in cookie.split('; ')}
    return {}


def clear_value(data, value):
    """递归清除所有嵌套字典和列表中的指定值"""
    if isinstance(data, dict):
        for key, val in list(data.items()):
            if val == value:
                del data[key]
            else:
                clear_value(val, value)
    elif isinstance(data, list):
        for item in data:
            if item == value:
                data.remove(item)
            else:
                clear_value(item, value)
