from flask import abort
from flask import current_app, jsonify
from flask import g
from flask import render_template
from flask import session

from info.models import News, User
from info.utils.common import user_login_data
from info.utils.response_code import RET
from . import news_blue


# 功能描述: 获取新闻详细信息
# 请求路径: /news/<int:news_id>
# 请求方式: GET
# 请求参数:news_id
# 返回值: detail.html页面, 用户data字典数据
@news_blue.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    # 1.根据传入的新闻编号,获取新闻对象
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="新闻获取失败")

    # 2.判断新闻是否存在
    if not news:
        abort(404)

    # 功能：详情页面的热门新闻展示
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(8).all()
    except Exception as e:
        current_app.logger.error(e)

    # 将新闻列表转成,字典列表
    click_news_list = []
    for news in news_list:
        click_news_list.append(news.to_dict())

    # 从session获取用户的编号
    # user_id = session.get('user_id')
    # # 判断用户是否存在
    # user = None
    # if user_id:
    #     try:
    #         user = User.query.get(user_id)
    #     except Exception as e:
    #         current_app.logger.error(e)

    # 3.携带数据渲染页面
    data = {
        'news':news.to_dict(),
        'click_news_list':click_news_list,
        'user_info': g.user.to_dict() if g.user else ''
    }

    return render_template('news/detail.html',data=data)