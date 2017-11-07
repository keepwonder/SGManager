#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : models.py 
# @time  : 2017/11/06 16:01:21
# @description：
from ext import db
import datetime


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, username):
        self.username = username

    def __repr__(self, username):
        return '<Model User: %r>'.format(username)
