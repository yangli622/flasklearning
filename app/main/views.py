#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Administrator
@file:views.py
@create_time:2018/10/13
"""

from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route('/', methods=['GET', 'POST'])   # 不同的蓝本装饰器不同
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('main.index'))  # 每个蓝本都有一个命令空间，生成url需要加上命名空间前缀
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False),
                           current_time=datetime.utcnow())
