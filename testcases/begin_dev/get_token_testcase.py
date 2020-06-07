# !/usr/bin/env python
# encoding: utf-8
# @author: new
# @file: get_token_testcase.py
# @time: 2020/6/7 11:14
# @desc

import unittest
from common.config_value import config
from common.common_api import get_token


class GetTokenTestcase(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.hosts

    def tearDown(self) -> None:
        pass

    def test_get_token(self):
        res = get_token(config.grant_type, config.appid, config.secret)
        expires_in = res['expires_in']

        self.assertEqual(expires_in, 7200)

    def test_appid_error(self):
        res = get_token(config.grant_type, '1', config.secret)
        code = res['errcode']
        self.assertEqual(code, 40013)

    def test_grant_type_error(self):
        res = get_token(1, config.appid, config.secret)
        code = res['errcode']
        self.assertEqual(code, 40002)

    def test_secret_error(self):
        res = get_token(config.grant_type, config.appid, 1)
        code = res['errcode']
        self.assertEqual(code, 40125)


if __name__ == '__main__':
    unittest.main()
