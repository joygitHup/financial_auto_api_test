# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 18:52
@Auth ： 你赖大爷
@File ：test_c2c_purchase_list_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest

import requests

from config import data_config


class test_c2c_purchase_list_api(unittest.TestCase):
    """c2c产品申购列表"""
    @classmethod
    def setUpClass(self):
        self.url = data_config.host+data_config.c2c_purchase_list
        self.header = data_config.header
    '''case01:正确添加账号'''
    def test_c2c_purchase_list_api_01(self):
        requests_result=requests.get(url=self.url,headers=self.header)
        print(requests_result.content.decode('utf-8'))
        return requests_result

    '''case02:账号为空'''
    # def test_addcount02_by_admin(self):
    #     data=request_config.admin_manger_addcount02_data
    #     print(data)
    #     requests_result=requests.post(url=self.url,data=data,headers=self.header).json()
    #     return requests_result
    #
    # '''case03:账号已存在'''
    # def test_addcount03_by_admin(self):
    #     data=request_config.admin_manger_addcount03_data
    #     print(data)
    #     requests_result=requests.post(url=self.url,data=data,headers=self.header).json()
    #     return requests_result
    @classmethod
    def tearDownClass(self):
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()
