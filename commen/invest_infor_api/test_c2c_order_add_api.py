# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:43
@Auth ： 你赖大爷
@File ：test_c2c_order_add_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import json
import unittest

import allure
import requests

from config import data_config

@allure.feature("c2c下单")
class test_c2c_order_add_api(unittest.TestCase):
    """c2c下单"""
    @classmethod
    def setUpClass(self):
        self.url = data_config.host+data_config.c2c_order_add_url
        self.header = data_config.header
    @allure.story('正常访问 c2c下单')
    def test_c2c_order_add_api_01(self):
        requests_result=requests.post(url=self.url,headers=self.header,data=data_config.c2c_order_add_data)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为整数')
    def test_c2c_order_add_api_02(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data02)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为小数0.232')
    def test_c2c_order_add_api_03(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data03)
        print(requests_result.content.decode('utf-8'))
        return requests_result


    @allure.story('buyAmount数量为小数0.232')
    def test_c2c_order_add_api_04(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data04)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为字符串”test“')
    def test_c2c_order_add_api_05(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data05)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为空')
    def test_c2c_order_add_api_06(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data06)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为空')
    def test_c2c_order_add_api_07(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data07)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @allure.story('buyAmount数量为空')
    def test_c2c_order_add_api_08(self):
        requests_result = requests.post(url=self.url, headers=self.header, data=data_config.c2c_order_add_data08)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    @classmethod
    def tearDownClass(self):
        print('test finnnshi!')


if __name__=="__main__":
    unittest.main()

