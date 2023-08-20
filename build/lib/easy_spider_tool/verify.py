import re
from typing import Union

__all__ = ['verify_ip_address', 'verify_domain_name', 'verify_port', 'verify_url']

ipaddr_regex = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
domain_name_regex = re.compile(
    r'^(([a-zA-Z]{1})|([a-zA-Z]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z]{1}[0-9]{1})|([0-9]{1}[a-zA-Z]{1})|'
    r'([a-zA-Z0-9][-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9]))\.'
    r'([a-zA-Z]{2,13}|[a-zA-Z0-9-]{2,30}.[a-zA-Z]{2,3})$'
)
subdomain_name = re.compile(r'([a-zA-Z0-9\u4e00-\u9fa5]{1,61}\.){2,10}')
url_regex = re.compile(r'^https?:/{2}\w.+$')
port_regex = re.compile(r'\d+')


def verify_ip_address(address) -> bool:
    """验证ip地址合法性"""
    return True if ipaddr_regex.match(address) else False


def verify_domain_name(value: str) -> bool:
    """
    Return whether or not given value is a valid domain.
    If the value is valid domain name this function returns ``True``, otherwise False
    :param value: domain string to validate
    """
    if domain_name_regex.match(value):
        return True
    else:
        if re.findall(r'[\u4e00-\u9fa5]+', value):
            return True
        return False


def verify_subdomain_name(value) -> bool:
    """
    Return whether or not given value is a valid domain.
    If the value is valid domain name this function returns ``True``, otherwise False
    :param value: domain string to validate
    """
    if subdomain_name.match(value):
        return True
    return False


def verify_port(port: Union[int, str]) -> bool:
    """验证端口合法性"""

    if port_regex.match(str(port)):
        if all([
            int(port) > 1,
            int(port) < 65532
        ]):
            return True
    return False


def verify_url(url: str) -> bool:
    """验证url合法性"""
    verify_status = url_regex.match(url)
    return True if verify_status else False
