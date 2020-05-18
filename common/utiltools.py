import os


def get_file_path(project_name="jy_uitest"):
    """
    根据project_name工程名称来判断路径
    入参：总文件夹名称（根据个人的项目文件夹名称来修改）
    出参：此工程的电脑绝对路径
    """
    absolute_path = os.getcwd()
    begin_path = absolute_path.split(project_name)[0]
    project_path = begin_path + project_name
    return project_path


def pinyin_to_chinese(pinyin):
    if pinyin == "yanhaiyuan":
        return "阎海源"
    elif pinyin == "chenyixin":
        return "陈乙鑫"
    elif pinyin == "liuyang":
        return "刘洋"
    elif pinyin == "chenlei":
        return "陈磊"
    elif pinyin == "lipingping":
        return "李娉娉"
    else:
        print("没有匹配的名字")


def phone_create():
    phone = "120" + "".join(random.choice("0123456789") for i in range(8))
    return phone


def assert_create_dir(dir_name, dir_compara_path="", file_name=""):
    """
    检查工程内文件夹是否存在并且创建文件夹
    :param dir_name: 期望文件夹名称
    :param dir_compara_path: 文件夹相对路径(默认在工程根目录下)
    :param file_name: 要在创建的文件夹中，创建的文件全称（例如：auto_log.log）
    :return: 没有返回，直接创建
    """
    if dir_compara_path == "":
        dir_compara_path = "\\" + dir_name
    project_dir = os.listdir(get_file_path())
    if dir_name not in project_dir:
        create_path = get_file_path() + dir_compara_path
        os.makedirs(create_path)
        if file_name != "":
            file_create = open(create_path + '\\' + file_name, 'w')
            file_create.close()


def switch_test_host():
    """切换测试环境host"""
    test = ['10.82.12.244 sso.zsteel.cc']
    output = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'w')
    for hosts in test:
        output.write(hosts)
        output.write("\n")
    output.close()


def switch_safe_host():
    """切换安全环境host"""
    safe = ['10.82.12.243 sso.zsteel.cc']
    output = open(r'C:\WINDOWS\system32\drivers\etc\HOSTS', 'w')
    for hosts in safe:
        output.write(hosts)
        output.write("\n")
    output.close()


def get_current_system_time():
    """通过接口获取当前服务器时间"""
    pass


