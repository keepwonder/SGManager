#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : config.py 
# @time  : 2017/11/06 10:33:42
# @description：

import os


class BaseConfig(object):
    # session需要设置secret_key
    SECRET_KEY = os.urandom(24)

    # 汉化后台flask-admin管理系统界面
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    BABEL_DEFAULT_TIMEZONE = 'UTC+8'


class ProConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    # 开启调试模式
    DEBUG = True

    # mysql数据库配置
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'root'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'sgmanager'
    SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT,
                                                                           DRIVER,
                                                                           USERNAME,
                                                                           PASSWORD,
                                                                           HOST,
                                                                           PORT,
                                                                           DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
