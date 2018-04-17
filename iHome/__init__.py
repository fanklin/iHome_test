# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config



# 配置文件的加载
from manager import app

app.config.from_object(Config)

# 创建连接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象


manager = Manager(app)

Migrate(app,db)

manager.add_command('db', MigrateCommand)

CSRFProtect(app)

Session(app)