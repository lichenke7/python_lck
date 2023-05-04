from request import blog


def request_blog():
    blog_obj = blog.Blog()
    blog_obj.main_blog_request()


if __name__ == '__main__':
    request_blog()