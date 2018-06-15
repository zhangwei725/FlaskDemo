from flask_script import Manager, Server

# 参数  Flask对象的实例
from app import create_app

manager = Manager(create_app())

# 添加脚本
manager.add_command('start', Server(host='0.0.0.0', port=9000))

if __name__ == '__main__':
    manager.run()
