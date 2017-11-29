from ext import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    books = db.relationship('Book', backref=db.backref('users'), lazy='dynamic')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)


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
