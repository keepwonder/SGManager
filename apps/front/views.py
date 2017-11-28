#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : views.py
# @time  : 2017/11/24 19:57:14
# @description：

from flask import (
    Blueprint, views, render_template, redirect, url_for, request, session, flash, g)
from .forms import LoginForm
from .models import User, Book
from config import DevConfig
from ext import db
import random

bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return render_template('front/index.html')


class LoginView(views.MethodView):
    def get(self):
        return render_template('front/login.html')

    def post(self):
        form = LoginForm(request.form)

        if form.validate():
            username = form.username.data
            password = form.password.data
            remember = form.remember.data

            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session[DevConfig.USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('front.index'))
            else:
                flash('用户名或密码有误', 'errors')
                return self.get()
        else:
            # message = form.errors.popitem()[1][0]
            return self.get()


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))


@bp.route('/register/', methods=['GET', 'POST'])
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
            return redirect(url_for('front.login'))
        else:
            flash('用户名和密码不能为空', 'error')
            return render_template('front/register.html')
    return render_template('front/register.html')


@bp.route('/logout/')
def logout():
    del session[DevConfig.USER_ID]
    return redirect(url_for('front.login'))


@bp.route('/list/')
def list_book():
    # 已登录用，查看所有属于自己的记录
    books = Book.query.filter(Book.user_id == session.get('user_id')).all()

    # 未登录用户随机查看十条记录
    book_random = random.sample(Book.query.all(), 5)
    return render_template('front/list_books.html', books=books, book_random=book_random)


@bp.route('/add/', methods=['GET', 'POST'])
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
        return redirect(url_for('front.list_book'))

    return render_template('front/add_books.html')


@bp.before_request
def my_before_request():
    # user_id = session.get(DevConfig.USER_ID)
    # if user_id:
    #     user = User.query.filter(User.id == user_id).first()
    #     if user:
    #         g.user = user
    if DevConfig.USER_ID in session:
        user_id = session.get(DevConfig.USER_ID)
        user = User.query.get(user_id)
        if user:
            g.user = user


@bp.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}
