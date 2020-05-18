# -*- coding:utf-8 -*-
import yaml
from common.utiltools import get_file_path

# 定位文件路径
file_name = get_file_path()
file_name_default = get_file_path() + "\\config\\config.yaml"
def get_yaml_msg(file_names = "\\config\\config.yaml", first_level="", second_level="", third_level=""):
    """
    获取yaml文件的统一方法
    :param first_level:
    :param second_level:
    :param third_level:
    :return:所对应路径下的数据
    """
    file = file_name + file_names
    fr = open(file, 'r')
    data = yaml.load(fr)
    if first_level == "":
        return ""
    elif second_level == "":
        yaml_msg = data[first_level]
        fr.close()
        return yaml_msg
    elif third_level == "":
        yaml_msg = data[first_level][second_level]
        fr.close()
        return yaml_msg
    else:
        yaml_msg = data[first_level][second_level][third_level]
        fr.close()
        return yaml_msg


def sender_username():
    """
    读取发件人邮箱地址
    :return: 用户名
    """
    fr = open(file_name_default, 'r')
    data = yaml.load(fr)
    get_user = data["mail"]["sender"]["username"]
    fr.close()
    return get_user


def sender_psw():
    """
    读取发件人邮箱密码
    :return: 密码
    """
    fr = open(file_name_default, 'r')
    data = yaml.load(fr)
    get_psw = data["mail"]["sender"]["password"]
    fr.close()
    return get_psw


def receiver_username():
    """
    读取收件人邮箱地址
    :return收件人邮箱地址
    """
    fr = open(file_name_default, 'r')
    data = yaml.load(fr)
    get_user = data["mail"]["receiver"]["username"]
    fr.close()
    return get_user


def get_login_info(name=""):
    """
    获取登录用户名以及密码
    :param name: 用户名字全拼
    :return: 用户名、密码的字典
    """
    fr = open(file_name_default, 'r')
    data = yaml.load(fr)
    user_msg = data["login"][name]
    fr.close()
    return user_msg


def get_account_info(name="default"):
    """
    获取账号信息
    :param name: 账号名称：默认default
    :return: 账号信息的字典
    """
    fr = open(file_name_default, 'rb')
    data = yaml.load(fr)
    account_msg = data["account"][name]
    fr.close()
    return account_msg

