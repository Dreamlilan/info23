# 配置信息
import logging
import redis


class Config(object):
    DEBUG = None
    SECRET_KEY = 'ejwfewfkdsji'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/information23'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # session配置
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 3600 * 24 * 2

    # 设置日志等级默认就是DEBUG
    LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    LEVEL = logging.ERROR


config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
