from info import redis_store
from . import index_blue

@index_blue.route('/')
def index():
    # 测试redis存储数据
    redis_store.set('name','lilan')
    print(redis_store.get('name'))

    # 测试session存储信息
    # session['age'] = '13'
    # print(session.get('age'))

    # 输入记录信息
    # logging.debug('调试信息1')

    return 'hello world'