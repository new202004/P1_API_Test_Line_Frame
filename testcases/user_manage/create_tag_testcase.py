# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: create_tag_testcase.py
# @time: 2020/6/7 11:27
# @desc

import unittest
import random
from common.config_value import config
from common import common_api
class CreateTagTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.hosts

    def tearDown(self) -> None:
        pass

    def test_create_tag(self):
        token = common_api.get_success_token()
        tag_name = '标签' + str(random.randint(10000,90000))
        res = common_api.create_tag(token, tag_name)
        tag_name_actual = res['tag']['name'].encode('utf-8').decode('unicode_escape')
        self.assertEqual(tag_name_actual,tag_name)

if __name__ == '__main__':
    unittest.main()