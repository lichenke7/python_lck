from request import sign_topic


def common_request(request_obj):
    request_obj.main_request()


if __name__ == '__main__':
    common_request(sign_topic.SignTopic())
