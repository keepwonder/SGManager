#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : models.py 
# @time  : 2017/11/06 16:01:21
# @description：
from ext import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    books = db.relationship('Book', backref=db.backref('users'), lazy='dynamic')

    # def __init__(self, username):
    #     self.username = username
    #
    # def __repr__(self, username):
    #     return '<Model User: %r>'.format(self.username)


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    book_name = db.Column(db.String(255), nullable=False)
    book_author = db.Column(db.String(255))
    book_category = db.Column(db.String(255))
    is_paper = db.Column(db.Boolean, default=1)
    publisher = db.Column(db.String(255))
    price = db.Column(db.Float())
    actual_price = db.Column(db.Float())
    receive_time = db.Column(db.DateTime)
    begin_read_time = db.Column(db.DateTime)
    finish_read_time = db.Column(db.DateTime)
    author_profile = db.Column(db.Text)
    book_profile = db.Column(db.Text)
    reading_notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # def __init__(self, book_name):
    #     self.book_name = book_name

    # def __repr__(self, book_name):
    #     return '<Model Book: %r>'.format(self.book_name)
