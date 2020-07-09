from PyLibs.pre.pre_api import ecfront as pre_ecfront
import random
from HttpClientPyLibs.bussiness import bussiness_common
from AT_JSON.at_json import json_get_json_list_value
from HttpClientPyLibs.http_base.logger_handler import http_client_log
a = pre_ecfront.PreNewsGetList()
# list = []
list = a.news_get_list(page=100, everypage_count=10,class_id=1)
print(list)