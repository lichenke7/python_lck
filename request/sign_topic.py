from abc import ABC

from request.super_request import SuperRequest
from utils import constants, param_tools, time_tools
from request import basic_request
from local import lck_constants


class SignTopic(SuperRequest, ABC):
    sign_topic_value = constants.sign_topic

    def get_cookie(self):
        return lck_constants.topic_cookie

    def start_request(self, topic_id):
        url = self.sign_topic_value.get(constants.key_url)
        user_agent = self.request_config.get_user_agent()
        request_url = param_tools.get_sign_topic_params(url, user_agent, topic_id)
        return basic_request.request_get(request_url, headers=self.get_headers())

    def handel_response(self, response):
        print(response)

    def loop_request(self):
        for config in lck_constants.topic_id_config:
            topic_id = config.get('id')
            desc = config.get('desc')
            print('topic id is ' + topic_id + ',name: ' + desc)
            response = self.start_request(topic_id)
            self.handel_response(response)
            time_tools.random_time_sleep(30, 60)

    def main_request(self):
        super().main_request()
