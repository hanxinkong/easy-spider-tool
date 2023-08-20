# hash摘要相关

## md5
生成传入字符串的MD5值

### 参数

| 字段名   | 类型 | 必须 | 描述                     |
| -------- | ---- | ---- | ------------------------ |
| text     | str  | 是   | 加密对象                 |
| encoding | str  | 否   | 编码类型（默认：`utf-8`) |

### 返回
* md5值`str`

### 示例

```python
from easy_spider_tool import md5

text = 'http://localhost/'
print(md5(text))
# c9db569cb388e160e4b86ca1ddff84d7
```