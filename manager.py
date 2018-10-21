"""
项目启动相关配置:
1. 数据库配置
2. redis配置
3. session配置, 为后续登录保持做铺垫
4. 日志文件配置
5. CSRFProtect配置, 为了对'POST','PUT','DISPATCH','DELETE'做保护
6. 迁移配置


"""""

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect

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

    #session配置
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 3600*24*2


app.config.from_object(Config)

# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

# 创建redis对象，关联app
redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT,decode_responses=True)

# 初始化Session，读取app身上的session配置信息
Session(app)

# 使用CSRFProtect，保护app
CSRFProtect(app)


@app.route('/')
def index():
    # 测试redis存储数据
    redis_store.set('name','lilan')
    print(redis_store.get('name'))

    #测试session存储信息
    session['age'] = '13'
    print(session.get('age'))

    return 'hello world'

if __name__ == '__main__':
    app.run()
