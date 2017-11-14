#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : config.py 
# @time  : 2017/11/06 10:33:42
# @description：

import os


class BaseConfig(object):
    pass


class DevConfig(BaseConfig):
    # 开启调试模式
    DEBUG = False

    # 数据库配置
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'usg'
    PASSWORD = 'psg'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'dbsg'
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,
                                                                           DRIVER,
                                                                           USERNAME,
                                                                           PASSWORD,
                                                                           HOST,
                                                                           PORT,
                                                                           DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session需要设置secret_key
    SECRET_KEY = os.urandom(24)
