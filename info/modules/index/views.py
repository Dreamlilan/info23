from flask import current_app

from info import redis_store
from . import index_blue
from flask import render_template


@index_blue.route('/')
def index():
    # 测试redis存储数据
    # redis_store.set('name','lilan')
    # print(redis_store.get('name'))

    # 测试session存储信息
    # session['age'] = '13'
    # print(session.get('age'))

    # 输入记录信息
    # logging.debug('调试信息1')

    return render_template('news/index.html')


# 处理网站logo,浏览器在运行的时候，自动发送一个GET请求，向/favicon.ico地址
# 只需要编写对应的接口，返回一张图片即可
# 解决方法：current_app.send_static_file,自动向static文件夹中寻找制定资源
@index_blue.route('/favicon.ico')
def web_log():

    return current_app.send_static_file('news/favicon.ico')