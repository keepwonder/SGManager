#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : views_admin.py 
# @time  : 2017/11/09 11:48:00
# @description：后台管理视图从主应用sgmanager.py抽离
from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
from ext import db
from apps.front.models import User, Book
from main import app

babel = Babel(app)

admin = Admin(app, index_view=AdminIndexView(name='导航栏', template='/admin/welcome.html', url='/admin'))


# 自定义视图
class MyView(BaseView):
    # 这里类似于app.route()，处理url请求
    @expose('/')
    def index(self):
        return self.render('admin/hello.html')


class UserView(ModelView):
    # 这三个变量定义管理员是否可以增删改，默认为True
    # can_delete = False
    # can_edit = False
    # can_create = False

    # 这里是为了自定义显示的column名字
    column_labels = dict(
        id='序号',
        username='用户名',
        password='密码',
        phone='手机号',
        email='邮箱',
        create_time='创建时间'
    )

    # 如果不想显示某些字段，可以重载这个变量
    column_exclude_list = (
        # 'create_time', 创建时间不显示
    )


class BookView(ModelView):
    column_labels = dict(
        book_name='书名',
        book_author='作者',
        book_category='图书分类',
        is_paper='是否纸质书',
        publisher='出版社',
        price='定价',
        actual_price='实际购入价格',
        receive_time='到手时间',
        begin_read_time='开始阅读时间',
        finish_read_time='完成阅读时间',
        author_profile='作者简介',
        book_profile='图书简介',
        reading_notes='读后感想',
        users='所属用户'
    )

admin.add_view(MyView(name='Hello'))
# 只需把自己写的处理模型的视图加进去就行了，category是可选的目录
# admin.add_view(UserView(User, db.session, name='用户信息', category='管理用户'))
admin.add_view(UserView(User, db.session, name='管理用户'))
admin.add_view(BookView(Book, db.session, name='管理书籍'))
