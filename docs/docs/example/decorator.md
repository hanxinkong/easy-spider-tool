# Decorator
装饰器方法

## retry
异常重试装饰器，可捕获指定一个或者多个异常；重试次数

### 参数

| 字段名     | 类型                               | 必须 | 描述                             |
| ---------- | ---------------------------------- | ---- | -------------------------------- |
| num        | int                                | 是   | 重试次数                         |
| fail_msg   | str                                | 否   | 指定错误提示文本                 |
| exceptions | Union[Exception, Tuple[Exception]] | 否   | 指定异常，多个异常以元组格式传递 |

### 返回
* `Any`

### 示例

```python
import requests
from requests.exceptions import RequestException
from easy_spider_tool.decorator import retry


@retry(num=5, exceptions=RequestException)
def test_request():
    url = 'http://easy-spider-tool.xink.top/'
    r = requests.get(url, timeout=8)
    print(r.status_code)

    
if __name__ == '__main__':
    test_request()
```