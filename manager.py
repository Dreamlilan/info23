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
from info import create_app,db,models
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')

# 创建manage对象,管理app
manager = Manager(app)

# 使用Migrate,关联app,db
Migrate(app,db)

# 给manager添加操作命令
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
