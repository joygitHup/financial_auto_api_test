# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:24
@Auth ： 你赖大爷
@File ：test_borrow_repay_url_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import json
import unittest

import requests

from config import data_config


class test_borrow_repay_url_api(unittest.TestCase):
    """还款"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_repay_url
        self.header = data_config.header

    def test_borrow_repay_url_api_01(self):
        request = requests.post(url=self.url,headers=self.header,data=json.dumps(data_config.borrow_repay_data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

