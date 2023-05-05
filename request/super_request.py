import time
from abc import abstractmethod

from utils import constants, time_tools
from local import lck_constants


def get_blog_time(item):
    created_at = item['created_at']
    time_str = time.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    end_time = str(time_str.tm_year) + '-' + str(time_str.tm_mon) + '-' + str(time_str.tm_mday)
    pic_tag = time_tools.format_hour(time_str.tm_hour) + '-' + time_tools.format_hour(time_str.tm_min)
    return end_time, pic_tag


class SuperRequest:
    request_config = constants.config
    target_uid = lck_constants.target_uid

    def __init__(self):
        print('init')

    def get_cookie(self):
        return self.request_config.get_cookie()

    def get_headers(self, custom_headers=None):
        return self.request_config.get_headers(self.get_cookie(), custom_headers)

    @abstractmethod
    def handel_response(self, response):
        if response is None:
            return
        print(' handel response')

    @abstractmethod
    def loop_request(self):
        print('loop request')

    @abstractmethod
    def main_request(self):
        print('main request')
        time_tools.duration_time(self.loop_request)
