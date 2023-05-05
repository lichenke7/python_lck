from local import lck_constants
from utils import request_config

key_url = 'url'
key_data = 'data'
key_since_id = 'since_id'
key_pic_ids = 'pic_ids'
key_list = 'list'
key_pic_info_list = 'pic_infos'
key_mw2000 = 'mw2000'
key_largest = 'largest'
key_test = 'test'

# -------------------------------------------------value----------------------------------------------------------------
print_response = False

config = request_config.RequestConfig()

base_url = lck_constants.base_url
statues_url = base_url + 'statuses/'
# -----------------------------------------------------profile blog-----------------------------------------------------
blog = {
    'method': 'get',
    'url': statues_url + 'mymblog',
}

# ------------------------------------------download big image by profile blog------------------------------------------
blog_image = {
    'method': 'get',
    'url': base_url + 'common/download',
}

# ------------------------------------------single text comments-------------------------------------------------------
comments = {
    'method': 'get',
    'url': statues_url + 'buildComments',
}

# ----------------------------------------report a bad msg or a bad comment---------------------------------------------
# TODO
report = {

}

# -------------------------------------------sign super topic-----------------------------------------------------------
# TODO
sign_topic = {
    'method': 'get',
    'url': lck_constants.sign_topic_url
}
