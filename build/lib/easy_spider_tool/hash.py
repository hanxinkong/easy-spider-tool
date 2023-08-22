# -*- coding: utf-8 -*-
# @Time : 2022/5/30 23:22
# @Author : hanxinkong
# @File : hash.py
# @Description : hash摘要相关
# @Software : PyCharm
import hashlib


def md5(text, encoding: str = 'utf-8'):
    data = hashlib.md5(text.encode(encoding))
    return data.hexdigest()
