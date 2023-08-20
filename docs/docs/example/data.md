# 数据清洗/转换相关

## cookie_to_dic

 cookie转换为字典（Dict）格式

### 参数

| 字段名 | 类型 | 必须 | 描述         |
| ------ | ---- | ---- | ------------ |
| cookie | str  | 是   | cookie字符串 |

### 示例

```python
from easy_spider_tool import cookie_to_dic

print(cookie_to_dic(cookie))

# {'auth_token': 'ff8ea324a1b6d97bf05ee724e1f8f7b1f6968e2d', 'ct0': '0d10adb132334979e412da21c9f2e071858296b6949e60208a39c0d2e5410484e4630075f47f793f1cd7783a4a8d25bd5950ffc526f5bc4e9b88cba725aa57277a0d49d081b3c368e9c4c00ed421abf0'}
```



## clear_value

清除列表（List）或字典（Dict）中的指定值（递归清除所有嵌套字典和列表中的指定值），**会覆盖源数据**

### 参数

| 字段名 | 类型              | 必须 | 描述                       |
| ------ | ----------------- | ---- | -------------------------- |
| data   | Union[List, Dict] | 是   | 要处理的目标对象           |
| value  | Any               | 否   | 要清除的值（默认：`None`） |

### 示例

```python
from easy_spider_tool import clear_value, format_json

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

clear_value(data, 'admin')
print(format_json(data))
"""
{
    "code": 200,
    "data": [
        {
            "id": 1,
            "level": "boss"
        },
        {
            "id": 2,
            "username": "user",
            "level": "staff"
        }
    ]
}
"""
```



