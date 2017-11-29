import os


class BaseConfig(object):
    # session需要设置secret_key
    SECRET_KEY = os.urandom(24)
    # session设置
    USER_ID = 'ADSSGD'

    # 汉化后台flask-admin管理系统界面
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    BABEL_DEFAULT_TIMEZONE = 'UTC+8'


class ProConfig(BaseConfig):
    pass


class DevConfig(BaseConfig):
    # 开启调试模式
    DEBUG = False

    # mysql数据库配置
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
