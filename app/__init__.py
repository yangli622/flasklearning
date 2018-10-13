#!/usr/bin/env python
# -*-coding:utf-8 -*-

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def app_create(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])  # 可以直接把对象里面的配置数据转换到app.config里面
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # 路由和其他处理程序定义
    from .main import main as main_blueprint  # 从当前目录下面的main子目录导入main
    app.register_blueprint(main_blueprint)  # 注册蓝本
    # ...

    return app
