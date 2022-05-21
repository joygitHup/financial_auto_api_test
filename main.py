# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#!/usr/bin/venv python
#coding=utf8
import os
import sys
# 获取文件地址
import HTMLTestRunner
from tools.auto_log import loginmanger
from tools.send_email import sendEmai

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
case_path=os.path.join(os.getcwd(),"commen")
print(case_path)
case_path1=os.path.join(os.getcwd(),"commen")
file_path=os.path.join(os.getcwd(),"report")

import time
import unittest

import os
# 添加为主要文件 即所有事件进行装箱操作
if __name__=='__main__':
    '''将运行的日志文件输出到指定文件中进行保存'''
    op = loginmanger()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_abspath = os.path.join(file_path, "result_" + now + ".html")
    suite = unittest.TestSuite()
    # 批量加载用例
    discover = unittest.defaultTestLoader.discover(start_dir=case_path1, pattern='test_*.py',top_level_dir=None)
    print(discover)
    # 将日志写入到指定文件夹中
    print(op.consel_out())
    with open(report_abspath, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='理财接口测试报告', description='用例执行情况')
        runner.run(discover)
    send_emai = sendEmai()
    send_emai.Sendemail(newfile=report_abspath)

# 1.文件的相对路径的处理 涉及到文件路径的地方 用函数表达
# 3.jmter的集成
# 4.脚本的调优
#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  gitup的登录token  joygitHup
 # 单一加载测试用例
    # test_suit = unittest.TestSuite()
    # test_suit.addTest(eidtor_infor_device_test('test_eidtor_infor_with_devicess'))
    # runtest = unittest.TextTestRunner()
    # 创建生成结果文件格式 且写入文件
    # now_time = time.strftime('%Y-%m-%d %H_%M_%S')
    # filepath = 'C:\\..\\zz_securityPrsystem\\report'
    # filename = filepath + "\\" + now_time + 'report.html'
    # fb = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fb, title='软件测试HTML报告', )description='测试报告'
    # # runner.run(test_suit)
    # runner.run(test_suit)
    # fb.close()
    # 将结果通过邮件发送到指定人

    #git 提交代码流程
    # 0. 在git中创建仓库
    # 1.git init   在项目名称中
    # 2.git add .   添加全部文件
    # 3.git status  获取状态 添加进来后 为绿色
    # git config --global user.email "you@example.com"
    # git config --global user.name "Your Name"
    # 4.git commit -m '描述'  提交添加进来的代码块 在这之前有可能还要登录
    # 5.git remote add origin https://github.com/joygitHup/Auto_test.git  连接到远程仓库(可以先连接) git@github.com:joygitHup/Auto_test.git
    # 6.git push -u origin master  推送代码到分支
#     查看分支
#     git branch -a  --sort committerdate --format '%(committerdate:short) %(refname:short)'
# 1.查看远程分支
# git branch -a
# 2.查看本地分支
# git branch
# 3.切换分支
# git checkout -b 想要的分支名 （如果本地有这分支的话，-b就可以省略了）








