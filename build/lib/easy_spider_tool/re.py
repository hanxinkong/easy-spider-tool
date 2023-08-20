import re
from typing import Optional, Any, List


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
