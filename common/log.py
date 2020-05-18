# -*-coding:utf-8 -*-
import os
import logging
from common.utiltools import *


# def get_file_path(project_name=""):
#     """
#     根据project_name工程名称来判断路径
#     入参：总文件夹名称（根据个人的项目文件夹名称来修改）
#     出参：此工程的电脑绝对路径
#     """
#     project_name = "cenpur_uitest"
#     absolute_path = os.getcwd()
#     begin_path = absolute_path.split(project_name)[0]
#     project_path = begin_path + project_name
#     return project_path


class Logger:
    def __init__(self, clevel=logging.DEBUG, Flevel=logging.INFO):
        # 判断log文件夹是否存在，不存在的话创建文件夹以及日志文件
        dir_name = 'log'
        file_name = "autolog.log"
        path = get_file_path() + "\\" + dir_name + "\\" + file_name
        assert_create_dir(dir_name=dir_name, file_name=file_name)
        # project_dir = os.listdir(get_file_path())
        # dir_name = 'log'
        # if dir_name not in project_dir:
        #     create_path = get_file_path() + '\\log'
        #     os.makedirs(create_path)
        #     file = open(create_path + '\\' + 'autotest' + '.log', 'w')
        #     file.close()
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        if not self.logger.handlers:
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            # 设置CMD日志
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)
            # 设置文件日志
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)
            self.logger.addHandler(sh)
            self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def war(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger.critical(message)

    def inter_face(self, in_dic, out_request):
        try:
            self.logger.info("请求参数:" + str(in_dic))
            self.logger.info("返回结果:" + str(out_request))
        except:
            self.logger.error(in_dic)
            self.logger.error(out_request)


if __name__ == '__main__':
    logyyx = Logger(clevel=logging.DEBUG, Flevel=logging.INFO)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')
