from abc import ABC

from request.super_request import SuperRequest
from utils import constants, param_tools, time_tools
from request import basic_request
from local import lck_constants


# https://service.account..com/aj/reportspam?__rnd=1683268024511
# post
# refer: https://service.account..com/reportspam?rid=&type=3&from=1FFFF96039


class Report(SuperRequest, ABC):
    report_value = constants.report

    def get_cookie(self):
        return lck_constants.report_cookie

    def handel_response(self, response):
        print(response)

    def start_request(self):
        print('report')
        url = self.report_value.get(constants.key_url) + str(time_tools.get_timestamp())

        # request_url = param_tools.get_sign_topic_params(url, user_agent, topic_id)
        # return basic_request.request_get(request_url, headers=self.get_headers())

    def loop_request(self):
        self.start_request()
