# 合法性验证相关

## verify_ip_address

IP地址合法性验证

### 参数

| 字段名  | 类型 | 必须 | 描述               |
| ------- | ---- | ---- | ------------------ |
| address | str  | 是   | 要验证为IP的字符串 |

### 示例

```python
from easy_spider_tool import verify_ip_address

print(verify_ip_address('192.168.2.0'))
# True
print(verify_ip_address('192.168.2.256'))
# False
print(verify_ip_address('192.fffff'))
# False
```



## verify_domain_name

域名合法性验证

### 参数

| 字段名 | 类型 | 必须 | 描述                 |
| ------ | ---- | ---- | -------------------- |
| value  | str  | 是   | 要验证为域名的字符串 |

### 示例

```python
from easy_spider_tool import verify_domain_name

print(verify_domain_name('www.baidu.com'))
# True
print(verify_domain_name('http://www.baidu.com'))
# False
```



## verify_url

URL合法性验证

### 参数

| 字段名 | 类型 | 必须 | 描述                |
| ------ | ---- | ---- | ------------------- |
| url    | str  | 是   | 要验证为URL的字符串 |

### 示例

```python
from easy_spider_tool import verify_url

print(verify_url('www.baidu.com'))
# False
print(verify_url('http://www.baidu.com'))
# True
```



## verify_port

端口合法性验证

### 参数

| 字段名 | 类型            | 必须 | 描述                     |
| ------ | --------------- | ---- | ------------------------ |
| port   | Union[int, str] | 是   | 要验证端口的字符串或整数 |

### 示例

```python
from easy_spider_tool import verify_port

print(verify_port(65524))
# True
print(verify_url(65588))
# False
```

