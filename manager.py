"""
项目启动相关配置:
1. 数据库配置
2. redis配置
3. session配置, 为后续登录保持做铺垫
4. 日志文件配置
5. CSRFProtect配置, 为了对'POST','PUT','DISPATCH','DELETE'做保护
6. 迁移配置

"""""
import logging
from flask import Flask,session
from info import create_app

app = create_app('development')


@app.route('/',methods=['GET','post'])
def index():
    # 测试redis存储数据
    # redis_store.set('name','lilan')
    # print(redis_store.get('name'))

    # 测试session存储信息
    # session['age'] = '13'
    # print(session.get('age'))

    # 输入记录信息
    logging.debug('调试信息1')

    return 'hello world'

if __name__ == '__main__':
    app.run()
