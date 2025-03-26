# easy spider tool

在实际工作中，沉淀的一些简易、好用的爬虫工具，减少重复代码与文件冗余，希望一样能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

## 安装

```shell
pip install easy_spider_tool
```

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
    - `regex_match` 条件匹配（支持多个不相关条件匹配,支持设置默认值，选取首个匹配值）
    - `for_to_regx_match` 多个不相关条件匹配（兼容老版本保留）
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

## 链接

Github：https://github.com/hanxinkong/easy-spider-tool

## 注明
