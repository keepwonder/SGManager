#!usr/bin/env python  
# -*- coding:utf-8 -*-  
# @author: Johnathon Qiang
# @file  : manager.py
# @time  : 2017/11/06 16:13:02
# @description：
from flask_script import Manager, Command, Server
from flask_migrate import Migrate, MigrateCommand
from sgmanager import app
from ext import db
from models import User

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server())
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app,
                db=db,
                User=User)


if __name__ == '__main__':
    manager.run()
