# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/17 15:39
@Auth ： 你赖大爷
@File ：auto_log.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import  logging
import os
import re
from logging.handlers import TimedRotatingFileHandler
class loginmanger():
   def consel_out(self):
      logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='D:\\pythonDdvWorkspace\\pythonVersion310\\financial_auto_api_test_back\\log\\test.text',
                    filemode='w')
      console = logging.StreamHandler()  # 定义console handler
      console.setLevel(logging.INFO)  # 定义该handler级别
      formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
      console.setFormatter(formatter)

   def setup_log(log_name):
       '''高级日志的实现方式-自动清理'''
       # 创建logger对象。传入logger名字
       logger = logging.getLogger(log_name)
       log_path = os.path.join("D:\\pythonDdvWorkspace\\pythonVersion310\\financial_auto_api_test_back\\log", log_name)
       # 设置日志记录等级
       logger.setLevel(logging.INFO)
       # interval 滚动周期，
       # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
       # backupCount  表示日志保存个数
       file_handler = TimedRotatingFileHandler(
           filename=log_path, when="MIDNIGHT", interval=1, backupCount=30
       )
       # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
       file_handler.suffix = "%Y-%m-%d.log"
       # extMatch是编译好正则表达式，用于匹配日志文件名后缀
       # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
       file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
       # 定义日志输出格式
       file_handler.setFormatter(
           logging.Formatter(
               "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
           )
       )
       logger.addHandler(file_handler)
       return logger
if __name__=="__main__":
    op=loginmanger()
    op.consel_out()
