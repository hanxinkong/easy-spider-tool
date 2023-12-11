from easy_spider_tool import date_parse, between_day, after_day, before_day, format_json, jsonpath, current_date, \
    timestamp, md5, regex_match, cookie_to_dic, clear_value, verify_ip_address, verify_domain_name, verify_url
from easy_spider_tool.date import format_date

if __name__ == '__main__':
    # print(date_parse('今天', select='date', timezone='Asia/Shanghai', default_time_scheme=None))
    # print(between_day('2天前', '今天'))
    # print(after_day('今天',))
    # print(before_day('今天'))
    print(current_date())
    # print(timezone_('今天'))
    # print(timestamp(ms=True))
    # print(format_date())
    # print(between_day('2023-08-01', '2023-08-05'))
    # text = 'http://localhost/'
    # print(md5(text))
    # a = 'easy_spider_tool'
    # b = 'easy_tool'
    # print(regex_match([r'spider', r'tool'], a, first=True, default=''))
    # print(regex_match([r'spider', r'tool'], b, first=True, default=''))
    # cookie = 'auth_token=ff8ea324a1b6d97bf05ee724e1f8f7b1f6968e2d; ct0=0d10adb132334979e412da21c9f2e071858296b6949e60208a39c0d2e5410484e4630075f47f793f1cd7783a4a8d25bd5950ffc526f5bc4e9b88cba725aa57277a0d49d081b3c368e9c4c00ed421abf0'
    # data = cookie_to_dic(cookie)

    data = {'page_limit': 30, 'data_type': 'information', 'time_interval': 'all',
            'options': {'key_word': '联通', 'drill_down_count': -1, 'comment_count': -1, 'time_interval': None,
                        'task_id': '联通', 'data_type': 'information'}, 'total_count': 0, 'min_time': 0,
            'max_time': 1701158992}

    # data = {
    #     "code": 200,
    #     "data": [
    #         {
    #             "id": 0,
    #             "username": "admin",
    #             "level": "boss"
    #         },
    #         {
    #             "id": 2,
    #             "username": "user",
    #             "level": "staff"
    #         }
    #     ]
    # }
    print(jsonpath(data, [], first=True, default='ff'))
    # clear_value(data, 'admin')
    # print(format_json(data))

    # print(verify_ip_address('192.168.2.0'))
    # print(verify_ip_address('192.168.2.256'))
    # print(verify_ip_address('192.fffff'))
    # print(verify_domain_name('www.baidu.com'))
    # print(verify_domain_name('http://www.baidu.com'))
    # print(verify_url('www.baidu.com'))
    # print(verify_url('http://www.baidu.com'))
