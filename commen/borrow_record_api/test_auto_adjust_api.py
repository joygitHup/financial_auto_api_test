# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 13:40
@Auth ： 你赖大爷
@File ：test_auto_adjust_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import allure
import requests

from config import data_config

@allure.feature("自动调整质押率")
class test_auto_adjust_api(unittest.TestCase):
   """自动调整质押率"""
   @classmethod
   def setUpClass(self) -> None:
     self.url = data_config.host + data_config.auto_adjust_url
     print(self.url)
     self.header = data_config.header
     self.data=data_config.auto_adjust_data
     print(self.data)

   @allure.story("正常访问接口")
   def test_auto_adjust_api_01(self):
     request = requests.post(url=self.url, headers=self.header, data=self.data.encode("utf-8"))
     print(request.content.decode('utf-8'))
     return request.content.decode('utf-8')

   @allure.story("isAutoAdjust 设置为false")
   def test_auto_adjust_api_02(self):
       request = requests.post(url=self.url, headers=self.header, data=data_config.auto_adjust_data02.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')
   @allure.story("isAutoAdjust  设置为T")
   def test_auto_adjust_api_03(self):
       request = requests.post(url=self.url, headers=self.header, data=data_config.auto_adjust_data03.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')

   @allure.story("isAutoAdjust  设置为F")
   def test_auto_adjust_api_04(self):
       request = requests.post(url=self.url, headers=self.header, data=data_config.auto_adjust_data04.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')

   @allure.story("isAutoAdjust  设置为12223")
   def test_auto_adjust_api_05(self):
       request = requests.post(url=self.url, headers=self.header, data=data_config.auto_adjust_data05.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')

   @allure.story("isAutoAdjust  空参")
   def test_auto_adjust_api_06(self):
       request = requests.post(url=self.url, headers=self.header, data=data_config.auto_adjust_data06.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')

   @allure.story("isAutoAdjust  borrowID空参")
   def test_auto_adjust_api_07(self):
       request = requests.post(url=data_config.auto_adjust_url07, headers=self.header, data=data_config.auto_adjust_data07.encode("utf-8"))
       print(request.content.decode('utf-8'))
       return request.content.decode('utf-8')



   @classmethod
   def tearDownClass(self):
      print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

