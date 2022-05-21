# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:17
@Auth ： 你赖大爷
@File ：test_borrow_repay_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import requests

from config import data_config


class test_borrow_repay_api(unittest.TestCase):
    """还款信息"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_repay_info_url
        self.header = data_config.header

    def test_borrow_list_api_01(self):
        request = requests.get(url=self.url,headers=self.header)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

