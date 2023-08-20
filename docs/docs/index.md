一些简易、好用的爬虫工具，减少代码与文件冗余，能提升20%~50%的生产效率.

----
**文档地址：** <a href="/https://easy-easy-spider-tool.xink.top/" target="_blank">https://easy-spider-tool.xink.top/ </a>

**PyPi地址：** <a href="https://pypi.org/project/easy-spider-tool" target="_blank">https://pypi.org/project/easy-spider-tool </a>

**GitHub地址：** [https://github.com/hanxinkong/easy-spider-tool](https://github.com/hanxinkong/easy-spider-tool)

----

## 安装

<div class="termy">

```console
pip install easy-spider-tool
```

</div>

## 主要功能

- `时间相关`
    - `before_day` 昨天日期（可用于时间递减）
    - `after_day` 明天日期（可用于时间递增）
    - `between_day` 两个日期之间
    - `current_date` 当前时间
    - `timestamp` 当前时间戳（支持精确到毫秒）
    - `date_parse` 任意格式时间解析(支持时区转换，指定保留日期/时间（可设置默认值）部分)
- `json相关`
    - `format_json` 漂亮美观的格式化输出
    - `jsonpath` 任意多个json路径解析（支持设置默认值，选取首个匹配值）
- `hash摘要相关`
    - `md5` 字符经md5编码
- `正则匹配相关`
    - `regx_match` 单个条件匹配（支持设置默认值，选取首个匹配值）
    - `for_to_regx_match` 多个不相关条件匹配（支持设置默认值，选取首个匹配值）
- `数据清洗/转换相关`
    - `cookie_to_dic` cookie转换为字典（Dict）格式
    - `clear_value` 清除列表（List）或字典（Dict）中的指定值（递归清除所有嵌套字典和列表中的指定值）
- `合法性验证相关`
    - `verify_ip_address` IP地址合法性验证
    - `verify_domain_name` 域名合法性验证
    - `verify_port` 端口合法性验证
    - `verify_url` URL合法性验证
- `通知相关`
    - 暂无

## 简单使用

```python
from easy_spider_tool import format_json, jsonpath

data = {
    "code": 200,
    "data": [
        {
            "id": 1,
            "username": "admin",
            "level": "boss"
        },
        {
            "id": 2,
            "username": "user",
            "level": "staff"
        }
    ]
}

boss_name = jsonpath(data, '$.data[?(@.level=="boss")].username', first=True)
all_user_info = jsonpath(data, '$.data[*].username')

print(boss_name)
print(format_json(all_user_info))
```

## 依赖

内置依赖

- `re` Provides regular expression related functions for matching and processing text data.
- `datetime` Python Datetime module supplies classes to work with date and time.
- `hashlib` Secure hash and messag e digest algorithm library.
- `typing` Type Hints for Python.

第三方依赖

- `jsonpath` An XPath for JSON.
- `dateparser` Python library used for parsing dates from natural language text.
- `pytz` Python library used for working with timezone information.

_注：依赖顺序排名不分先后_

## 许可证

该项目根据 **MIT** 许可条款获得许可.

## 注明

该工具借鉴作者【xingcweb】,根据主观新增部分功能

**GitHub地址：** [https://github.com/xingcweb/simple-spider-tool](https://github.com/xingcweb/simple-spider-tool)