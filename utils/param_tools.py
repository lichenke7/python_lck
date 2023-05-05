from utils import time_tools


def handle_common_params(basic_url, first_params, second_params=None):
    print('handle common params')
    complete_params = first_params
    if second_params is not None and len(second_params) > 0:
        for key, value in second_params.items():
            print('handle second params')
            if value is None:
                continue
            if type(value) is int and value <= 0:
                continue
            if type(value) is str and len(value) <= 0:
                continue
            complete_params[key] = value

    params_str = basic_url + '?'
    for key, value in complete_params.items():
        value_str = key + "=" + str(value)
        params_str = params_str + value_str + "&"
    params_str = params_str.strip('&')
    return params_str


def get_comments_params(url, user_id, comments_id, max_id=None):
    params = {
        'is_reload': '1',
        'id': comments_id,
        'is_show_bulletin': '2',
        'is_mix': '0',
        'uid': user_id,
        'fetch_level': '0',
    }
    is_not_first = max_id is not None and max_id > 0
    count = 20 if is_not_first else 10
    second_params = {
        'count': count,
        'max_id': max_id
    }
    return handle_common_params(url, params, second_params)


def get_myblog_params(url, user_id, page, since_id=None):
    params = {
        'page': page,
        'uid': user_id,
        'feature': '0',
    }
    second_params = {
        'since_id': since_id
    }

    return handle_common_params(url, params, second_params)


def get_blog_image_params(url, pid):
    params = {
        'pid': pid
    }
    return handle_common_params(url, params)


def get_sign_topic_params(url, user_agent, topic_id):
    time = time_tools.get_timestamp()
    params = {'ajwvr': '6', 'api': 'http://i.huati.weibo.com/aj/super/checkin', 'texta': '签到', 'textb': '已签到',
              'status': '0', 'id': topic_id, 'location': 'page_100808_super_index', 'timezone': 'GMT+0800',
              'lang': 'zh-cn', 'plat': 'MacIntel', 'ua': user_agent, 'screen': '1440*900', '__rnd': str(time)}

    return handle_common_params(url, params)
