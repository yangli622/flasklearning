#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@author:Administrator
@file:forms.py
@create_time:2018/10/13
"""

from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
