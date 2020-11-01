# coding=utf-8
"""
读取全局变量配置
"""

import os
from configparser import ConfigParser

# 项目目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件
CONFIG_FILE_PATH = os.path.join(BASE_DIR, 'config', 'config.ini')

# 日志目录
LOG_PATH = os.path.join(BASE_DIR, 'Log')

# 测试数据的路径
DATA_DIR = os.path.join(BASE_DIR, 'ts_data\\')


class MyConfig:
    def __init__(self):

        config = ConfigParser()
        config.read(CONFIG_FILE_PATH, 'utf-8')

        # 配置环境，SCE是生成环境, PE是测试环境
        self.environment = config.get("config", "environment")
        # 用户名手机号
        self.username = config.get("data", "username")
        # 密码
        self.password = config.get("data", "password")
        # 验证码
        self.auth_code = config.get("data", "auth_code")
        # 错误密码
        self.error_pwd = config.get("data", "error_pwd")
        # 错误五位数密码
        self.five_pwd = config.get("data", "five_pwd")


myconfig = MyConfig()
