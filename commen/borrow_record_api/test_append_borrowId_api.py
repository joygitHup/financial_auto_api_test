# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/18 10:58
@Auth ： 你赖大爷
@File ：test_append_borrowId_api.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
import sys

from config import data_config

base_path = os.getcwd()
sys.path.append(base_path)
import json

import unittest

import requests


import allure



@allure.feature("调整质押率")
class test_append_borrowId_api(unittest.TestCase):
    """调整质押率"""
    @classmethod
    def setUpClass(self) -> None:
        self.url = data_config.host + data_config.borrow_append_borrowId_url
        print(self.url)
        self.header = data_config.header
        print(self.header)
        self.data=data_config.borrow_append_borrowId_data
    @allure.story('接口正常访问')
    def test_borrow_list_api_01(self):
        request = requests.post(url=self.url, headers=self.header, data=json.dumps(data_config.borrow_append_borrowId_data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')



    @allure.story('borrowId输入不符合规则的数据-小数0.8')
    def test_borrow_list_api_02(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url02,headers=self.header,data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('borrowId输入不符合规则的数据-负小数-0.8')
    def test_borrow_list_api_03(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url03, headers=self.header,data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('borrowId输入不符合规则的数据-负整数-8')
    def test_borrow_list_api_04(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url04, headers=self.header,data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('borrowId输入不符合规则的数据-字符串"test"')
    def test_borrow_list_api_05(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url05, headers=self.header,
                                data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('borrowId输入不符合规则的数据-超长正整数12231232 超过int64')
    def test_borrow_list_api_06(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url06, headers=self.header,
                                data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')


    @allure.story('borrowId输入不符合规则的数据-超长正整数12231232 超过int64')
    def test_borrow_list_api_07(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url07, headers=self.header,
                                data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('borrowId通过SQL语句查询')
    def test_borrow_list_api_08(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url08, headers=self.header,
                                data=json.dumps(self.data))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount不传入')
    def test_borrow_list_api_09(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data09))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount输入不符合规则的数据-超长字符123123123 超过int64')
    def test_borrow_list_api_010(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data010))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount输入不符合规则的数据-字符串”test“')
    def test_borrow_list_api_011(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data011))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount输入不符合规则的数据-小数0.8')
    def test_borrow_list_api_012(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data012))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount输入不符合规则的数据-负小数-0.8')
    def test_borrow_list_api_013(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data013))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount输入不符合规则的数据-负整数8')
    def test_borrow_list_api_014(self):
        request = requests.post(url=self.url, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data014))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @allure.story('appendAmount and borrowId输入错误的属性值appendAmount=test borrowId=test')
    def test_borrow_list_api_015(self):
        request = requests.post(url=data_config.borrow_append_borrowId_url015, headers=self.header,
                                data=json.dumps(data_config.borrow_append_borrowId_data015))
        print(request.content.decode('utf-8'))
        return request.content.decode('utf-8')

    @classmethod
    def tearDownClass(self) :
        print('test finnnshi!')

if __name__=="__main__":
    unittest.main()

# 生成allure
# pytest test_append_borrowId_api.py --alluredir D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test\target\allure_report
# allure generate D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test_back\allure_report\taget -o D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test_back\allure_report\html
# -o前面文件路径为生成数据的内径 -o后面的路径为生成web页面所需要的路径

# allure serve D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test_back\allure_report\html
# allure open  D:\pythonDdvWorkspace\pythonVersion310\financial_auto_api_test_back\allure_report\html

# pytest -v -s main.py  --alluredir=target\allure_result

# pip install requests  -i http://pypi.douban.com/simple --trusted-host=pypi.douban.com