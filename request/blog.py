from abc import ABC

from request.super_request import SuperRequest
from utils import constants, param_tools, time_tools
from local import save_tools
from request import basic_request


class Blog(SuperRequest, ABC):
    blog_value = constants.blog
    blog_image_value = constants.blog_image

    loop_length = 1
    start_page = 1
    next_since_id_list = []

    def request_blog(self, page, since_id):
        print('start request blog')
        url = self.blog_value.get(constants.key_url)
        uid = self.target_uid
        request_url = param_tools.get_myblog_params(url, user_id=uid, page=page, since_id=since_id)
        return basic_request.request_get(request_url, headers=self.get_headers())

    def request_blog_image(self, pid):
        print('start request blog image')
        url = self.blog_image_value.get(constants.key_url)
        request_url = param_tools.get_blog_image_params(url, pid)
        custom_headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        return basic_request.basic_request_get(request_url, headers=self.get_headers(custom_headers))

    def handel_response(self, response):
        super().handel_response(response)
        print('handel blog response')
        data = None if response is None else response.get(constants.key_data)
        if data is None:
            return
        since_id = data[constants.key_since_id]
        self.next_since_id_list.append(since_id)
        msg_list = data[constants.key_list]
        for item in msg_list:
            pic_ids = item.get(constants.key_pic_ids)
            if pic_ids is None or len(pic_ids) <= 0:
                continue
            pic_info_list = item[constants.key_pic_info_list]
            end_time, pic_tag = super.get_blog_time(item)
            for pic_id in pic_ids:
                pic_detail = pic_info_list[pic_id]
                if pic_detail is None:
                    continue

                largest = pic_detail.get(constants.key_mw2000, pic_detail[constants.key_largest])
                image_url = largest[constants.key_url]
                pic_array = image_url.split('/')[-1].split('.')
                pic_name = pic_array[0]
                pic_end = pic_array[-1]
                print('image_url url: ' + image_url + ', pid: ' + pic_name + ',end_time: ' + end_time)

                if not save_tools.allow_download(pic_end):
                    continue
                pic_rl = self.request_blog_image(pic_name)
                save_tools.save_image_to_local(pic_rl, pic_name, end_time, pic_tag, pic_end)
                time_tools.random_time_sleep(1, 4)
                time_tools.print_format_time('download end')

    def loop_request(self):
        for i in range(self.loop_length):
            time_tools.print_format_time('request start')
            length = len(self.next_since_id_list)
            since_id = None if length == 0 else self.next_since_id_list[length - 1]
            response = self.request_blog(i + self.start_page, since_id)
            self.handel_response(response)
            if not save_tools.download_blog_image and self.loop_length > 1:
                time_tools.random_time_sleep(8, 16)
            time_tools.print_format_time('request end')

    def main_request(self):
        super().main_request()
        save_tools.save_blog_params(self.start_page, self.loop_length, self.next_since_id_list)
