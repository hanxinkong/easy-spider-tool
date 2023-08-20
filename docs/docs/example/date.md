# 时间/日期相关

## before_day

生成昨天日期（可用于时间递减）

### 参数

| 字段名 | 类型                 | 必须 | 描述                                     |
| ------ | -------------------- | ---- | ---------------------------------------- |
| src    | Union[datetime, str] | 是   | 时间对象或者时间描述字符串               |
| is_fmt | bool                 | 否   | 是否格式化成字符串                       |
| scheme | str                  | 否   | 字符串格式 （默认：`%Y-%m-%d %H:%M:%S`） |

### 示例

```python
from easy_spider_tool import before_day

print(before_day('今天'))
# 2023-08-18 23:51:29
```



## after_day

生成明天日期（可用于时间递增）

### 参数

同before_day

### 示例

```python
from easy_spider_tool import after_day

print(after_day('今天'))
# 2023-08-20 23:54:20
```



## between_day

生成两个日期之间的日期

### 参数

| 字段名 | 类型                 | 必须 | 描述                                     |
| ------ | -------------------- | ---- | ---------------------------------------- |
| start  | Union[datetime, str] | 是   | 开始的时间对象或者时间描述字符串         |
| end    | Union[datetime, str] | 是   | 结束的时间对象或者时间描述字符串         |
| is_fmt | bool                 | 否   | 是否格式化成字符串                       |
| scheme | str                  | 否   | 字符串格式 （默认：`%Y-%m-%d %H:%M:%S`） |

### 示例

```python
from easy_spider_tool import between_day

print(between_day('2天前', '今天'))

# ['2023-08-17', '2023-08-18', '2023-08-19']
```

## current_date

当前时间的对象或者字符串

### 参数

| 字段名 | 类型 | 必须 | 描述                                     |
| ------ | ---- | ---- | ---------------------------------------- |
| is_fmt | bool | 否   | 是否格式化成字符串                       |
| scheme | str  | 否   | 字符串格式 （默认：`%Y-%m-%d %H:%M:%S`） |

### 返回
* 时间对象或者字符串。`Union[datetime, str]`



## date_parse

任意格式时间解析(支持时区转换，指定保留日期/时间（可设置默认值）部分)

### 参数

| 字段名              | 类型          | 必须 | 描述                                                         |
| ------------------- | ------------- | ---- | ------------------------------------------------------------ |
| obj                 | str           | 是   | 解析对象                                                     |
| select              | Optional[str] | 否   | 指定保留时间/日期部分（默认值：`None` ；可选值：`date`,`time`） |
| default_time_scheme | Optional[str] | 否   | 时间部分填充（默认值：`00:00:00` ）                          |
| timezone            | str           | 否   | 时区（默认值：`None`；可选值：附时区表）                     |
| is_fmt              | bool          | 否   | 是否格式化成字符串                                           |
| scheme              | str           | 否   | 字符串格式 （默认：`%Y-%m-%d %H:%M:%S`）                     |

### 返回
* 时间对象或者字符串。`Union[datetime, str]`

### 示例

```python
from easy_spider_tool import date_parse

print(date_parse('今天', select='date', timezone='Asia/Shanghai', default_time_scheme=None))
# 2023-08-20
```



## timestamp

生成当前时间戳；默认单位为秒，可选毫秒

### 参数

| 字段名 | 类型 | 必须 | 描述           |
| ------ | ---- | ---- | -------------- |
| ms     | bool | 是   | 生成毫秒时间戳 |

### 返回
* 时间戳。`int`



## timestamp_parse

时间戳解析为datetime对象，默认为格式化标准文本时间格式

### 参数

| 字段名 | 类型 | 必须 | 描述                                     |
| ------ | ---- | ---- | ---------------------------------------- |
| obj    | bool | 是   | 字符串时间戳                             |
| is_fmt | bool | 否   | 是否格式化成字符串                       |
| scheme | str  | 否   | 字符串格式 （默认：`%Y-%m-%d %H:%M:%S`） |

### 返回
* 时间对象或者字符串。`Union[datetime, str]`