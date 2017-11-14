#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : views.py 
# @time  : 2017/11/09 11:11:29
# @description：前台视图函数从主应用sgmanager.py抽离
from flask import request, redirect, url_for, render_template, g, session, flash
from models import User, Book
from main import app
from ext import db
import random


# from wt_forms import RegistrationForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter(User.username == username).first()
        if user and User.query.filter_by(password=password).first():
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('用户名和密码不能为空，请重新输入', 'error')
            flash('用户名或密码有误，请重新输入', 'error')
            return render_template('login.html', username=username, password=password)

    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user.username = username
        user.password = password
        user.email = email
        user.phone = phone
        if user.username and user.password:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'), )
        else:
            flash('用户名和密码不能为空', 'error')
            return render_template('register.html')
    return render_template('register.html')

    # form = RegistrationForm()
    # print(form.validate_on_submit())
    # print(form.errors)
    # if form.validate_on_submit():
    #     user = User()
    #     user.username = form.username.data
    #     user.password = form.password.data
    #     user.phone = form.phone.data
    #     user.email = form.email.data
    #     print('username:', user.username)
    #     print('password:', user.username)
    #     print('phone:', user.username)
    #     print('email:', user.username)
    #     if user.username and user.password:
    #         db.session.add(user)
    #         db.session.commit()
    #         return redirect(url_for('login'))
    #     else:
    #         flash('用户名和密码不能为空', 'error')
    #         print('something wrong')
    #         return render_template('register.html', form=form)
    #
    # return render_template('register.html', form=form)


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/book/list')
def list_books():
    # 已登录用，查看所有属于自己的记录
    books = Book.query.filter(Book.user_id == session.get('user_id')).all()

    # 未登录用户随机查看十条记录
    book_random = random.sample(Book.query.all(), 5)
    return render_template('list_books.html', books=books, book_random=book_random)


@app.route('/book/add/', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # print(session.get('user_id'))
        book = Book()
        book.book_name = request.form.get('book_name')
        book.book_author = request.form.get('book_author')
        book.publisher = request.form.get('publisher')
        book.book_category = request.form.get('book_category')
        book.is_paper = request.form.get('is_paper')
        # book.price = request.form.get('price')
        # book.actual_price = request.form.get('actual_price')
        # book.receive_time = request.form.get('receive_time')
        # book.begin_read_time = request.form.get('begin_read_time')
        # book.finish_read_time = request.form.get('finish_read_time')
        book.author_profile = request.form.get('author_profile')
        book.book_profile = request.form.get('book_profile')
        book.reading_notes = request.form.get('reading_notes')
        book.user_id = User.query.filter(User.id == session.get('user_id')).first().id
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('list_books'))

    return render_template('add_books.html')


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}

