import re
from typing import Optional, Any, List, Union


def regx_match(pattern, string, flags=0, first: bool = False, default: Optional[Any] = None):
    match_result = re.findall(pattern, string, flags=flags)
    if match_result and first is True:
        return match_result[0]
    elif match_result:
        return match_result
    else:
        return default


def for_to_regx_match(pattern_list: List, string, default: Optional[Any] = None, **kwargs):
    for pattern in pattern_list:
        value = regx_match(pattern, string, **kwargs)
        if value:
            return value

    return default


def regex_match(patterns: Union[List[str], str], string: str, flags=0, first: bool = False,
                default: Optional[Any] = None):
    """多条件正则匹配"""
    values = None
    if isinstance(patterns, str):
        patterns = [patterns]

    for pattern in patterns:
        values = re.findall(pattern, string, flags=flags)
        if values:
            break

    if values and first is True:
        return values[0]
    elif values:
        return values
    else:
        return default
