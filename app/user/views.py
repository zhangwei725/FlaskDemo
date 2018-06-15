from flask import Blueprint, render_template

"""
1> 实例化蓝图对象
2> 通过flask对象的实例注册蓝图实例
3> 通过蓝图对象的route方法声明
"""
user = Blueprint('user', __name__, template_folder=r'D:\work\PycharmProjects\FlaskDemo\templates')


def init_user(app):
    app.register_blueprint(user, url_prefix='/user', )


@user.route('/login')
def login():
    return render_template('index.html', msg='今天天气正好!!!  东京热还是武汉热')
