import random
import time


def random_time_sleep(start, end):
    random_num = random.randint(start, start)
    time.sleep(random_num)


def print_format_time(start_str):
    print(start_str + ' time :%s' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def duration_time(function):
    time_start = time.time()
    function()
    time_end = time.time()
    calculate_time = time_end - time_start
    print('------all complete-----seconds: ' + str(calculate_time))


def strftime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def format_hour(hour):
    return str(hour) if hour > 9 else '0' + str(hour)