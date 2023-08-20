# 正则匹配相关

## regex_match

正则条件遍历匹配（支持设置默认值，选取首个匹配值）

### 参数

| 字段名   | 类型                  | 必须 | 描述                               |
| -------- | --------------------- | ---- | ---------------------------------- |
| patterns | Union[List[str], str] | 是   | 正则表达式（可多个）               |
| string   | str                   | 是   | 目标字符串                         |
| flags    | bool                  | 否   |                                    |
| default  | Any                   | 否   | 未匹配到时设定的值（默认：`None`） |
| first    | bool                  | 否   | 是否取第一个值（默认：`false`）    |

### 示例

```python
from easy_spider_tool import regex_match

a = 'easy_spider_tool'
b = 'easy_tool'
print(regex_match([r'spider', r'tool'], a, first=True, default=''))
# spider
print(regex_match([r'spider', r'tool'], b, first=True, default=''))
# tool
```

