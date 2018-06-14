from flask_script import Manager, Server
from flask import Flask

app = Flask(__name__)

# 参数  Flask对象的实例

manager = Manager(app)


@app.route('/show/')
def show():
    return '88888'


# 一个的路由命名能够让用户快速的记住,
# @app.route
@app.route('/')
def index():
    return '6666'


@app.route('/list/<page>/<size>')
def list(page, size):
    print(type(page))
    print(type(size))
    return '6666'


@app.route('/int/<int:page>/<int:size>')
def list1(page, size):
    print(type(page))
    print(type(size))
    return '6666'


@app.route('/show/<path:path>/')
def list_path(path):
    print(type(path))
    return '6666'


# 添加脚本
manager.add_command('start', Server(host='127.0.0.1', port=9000))

if __name__ == '__main__':
    manager.run()
