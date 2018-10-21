"""
项目启动相关配置:
1. 数据库配置
2. redis配置
3. session配置, 为后续登陆保持做铺垫
4. 日志文件配置
5. CSRFProtect配置, 为了对,'POST','PUT','DISPATCH','DELETE'做保护
6. 迁移配置


"""""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)



# 配置信息
class Config(object):
    DEBUG = None
    SECRET_KEY = 'ejwfewfkdsji'

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@localhost/information23'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    #redis 配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app.config.from_object(Config)

# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

# 创建redis对象，关联app
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)


@app.route('/')
def index():
    # 测试redis存储数据
    redis_store.set('name','lilan')
    print(redis_store.get('name'))
    return 'hello world'


if __name__ == '__main__':
    app.run()
