# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:03
@Auth ： 你赖大爷
@File ：test_borrow_order_add_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import allure
import requests

from config import data_config

@allure.feature("发起借款post")
class test_borrow_order_add_api(unittest.TestCase):
    """发起借款"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_order_add_url
        self.header = data_config.header
    @allure.story('正常访问接口')
    def test_borrow_order_add_api_01(self):
        request = requests.post(url=self.url,headers=self.header,data=data_config.borrow_order_add_data)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('不传入任何值')
    def test_borrow_order_add_api_02(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data02)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('amount数量为整数')
    def test_borrow_order_add_api_03(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data03)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('amount数量为小数0.232')
    def test_borrow_order_add_api_04(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data04)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('amount数量为负小数-0.232')
    def test_borrow_order_add_api_05(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data05)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('amount数量为字符串”test“')
    def test_borrow_order_add_api_06(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data06)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('amount数量为空')
    def test_borrow_order_add_api_07(self):
        request = requests.post(url=self.url, headers=self.header, data=data_config.borrow_order_add_data07)
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

