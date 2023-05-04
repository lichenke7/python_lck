from local import lck_constants


class RequestConfig:
    __user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                   'Chrome/111.0.0.0 Safari/537.36'
    __cookie = lck_constants.cookie

    def get_cookie(self):
        return self.__cookie

    def get_headers(self, cookie=None, custom_headers=None):
        cookie = self.__cookie if cookie is None else cookie
        headers = {
            'cookie': cookie,
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'macOS',
            'user-agent': self.__user_agent,
            # 可选
            # 'authority': '',
            # 'method': 'GET',
            # 'path': '',
            # 'scheme': 'https',
            # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,
            # image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            # 'no-cache': 'no-cache',
            # 'pragma': 'no-cache',
            # 'referer': '',
            # 'sec-fetch-dest': 'document',
            # 'sec-fetch-mode': 'navigate',
            # 'sec-fetch-site': 'same-origin',
            # 'sec-fetch-user': '?1',
            # 'upgrade-insecure-requests': '1',
        }
        if custom_headers is not None and len(custom_headers) > 0:
            headers.update(custom_headers)
        return headers
