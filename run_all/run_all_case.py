# -*- coding:utf-8 -*-
import unittest
from common.HTMLTestRunner import HTMLTestRunner
from common.sendmail import *
from common.utiltools import get_file_path
import os
from common.BeautifulReport import BeautifulReport


# 加载指定目录下的所有case
test_dir = get_file_path() + "\\test_case"
# 配置运行用例、运行方式
discover = unittest.defaultTestLoader.discover(test_dir, pattern='login_demo*.py', top_level_dir=None)
run_type = "BeautifulReport"  # BeautifulReport 或者 HTMLTestRunner

if __name__ == "__main__":
    # 判断report文件夹是否存在，不存在的话创建文件夹
    project_dir = os.listdir(get_file_path())
    dir_name = 'report'
    if dir_name not in project_dir:
        create_path = get_file_path() + '\\report'
        os.makedirs(create_path)
    # 获取时间
    runner = unittest.TextTestRunner()
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 运行生成测试报告
    if run_type == "HTMLTestRunner":
        filename = get_file_path() + "\\report\\" + now + " HTR.html"
        fp = open(filename, "wb")
        runner = HTMLTestRunner(stream=fp, title=u'集采UI自动化测试报告', description=u'用例执行情况：')
        runner.run(discover)
        fp.close()
    elif run_type == "BeautifulReport":
        log_path = get_file_path() + "\\report\\"
        runner = BeautifulReport(discover)
        runner.report(filename=now + "BR", description='用例执行情况', log_path=log_path)

    # 邮件发送测试报告
    # send_report()