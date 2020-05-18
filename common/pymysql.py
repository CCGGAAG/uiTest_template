import paramiko
from common.loadyaml import get_yaml_msg
from common.utiltools import get_file_path
import pymysql.cursors
import copy

def run_mysql_inSafe(sql_words):
    """
    运行sql语句
    :param sql_words: sql语句
    :return: 查询数据对应的字典列表
    """
    loadpath = get_file_path() + "//config//id_rsa_30"
    sql_results = []
    private_key = paramiko.RSAKey.from_private_key_file(loadpath)
    # 创建SSH对象

    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='172.16.2.30', port=22, username='dev', pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command(
        "mysql -h172.16.2.30 -P8073 -umc_jcSeUser -pyH8BgnLdj00TmU9 -e'%s' cenpur" % sql_words)
    # 结果存储
    for std in stdout:
        sql_results.append(std.strip())
    sql_dic = listToDic(sql_results)
    return sql_dic


def run_mysql_inTest(sql_words):
    """
        运行sql语句
        :param sql_words: sql语句
        :return: 查询数据对应的字典列表
    """
    connect = pymysql.Connect(
        host='10.82.12.76',
        port=3306,
        user='root',
        passwd='dbfin@123',
        db='cenpur',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor(cursor=pymysql.cursors.DictCursor)
    # 查询数据
    sql_list = []
    try:
        # 执行SQL语句
        cursor.execute(sql_words)
        connect.commit()
        # 获取所有记录列表
        results = cursor.fetchall()
        for i in results:
            sql_list.append(copy.deepcopy(i))
    except:
        print("Error: 无法获取数据库数据")
    # 关闭连接
    cursor.close()
    connect.close()
    return sql_list


def get_user_id_from_mysql(user, environment):
    """
    通过名字获取user_id
    :param user: 姓名全拼，例如：yanhaiyuan
    :param environment: 环境：例如test、safe
    :return: 唯一的user_id 例如：742e43807e324812a3d94d489ddae42e
    """
    user_id = ""
    cn_name = pinyin_to_chinese(user)
    inquire_words = "select mem_user_id FROM cenpur_user_mem_auth WHERE cn_name = '%s'" % (cn_name)
    if environment == "test":
        user_id_list = run_mysql_inTest(inquire_words)
        user_id = user_id_list[0]["mem_user_id"]
    elif environment == "safe":
        user_id_list = run_mysql_inSafe(inquire_words)
        user_id = user_id_list[0]["mem_user_id"]
    return user_id


def listToDic(lists):
    """
    将sql列表转换为字典
    :param lists: 空格分割
    :return: 字典信息的列表
    """
    title_list = lists[0].split("\t")
    hang = len(lists)
    sql_list = []
    for x in range(1, hang):
        app = {}
        lie_msg = lists[x].split("\t")
        if lie_msg:
            for i in range(len(lie_msg)):
                app[title_list[i]] = lie_msg[i]
            sql_list.append(copy.deepcopy(app))
    return sql_list
