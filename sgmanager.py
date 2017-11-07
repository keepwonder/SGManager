from flask import Flask, render_template, request, redirect, url_for, session, g
from config import DevConfig
from ext import db
from models import User

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)


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
            session['user_id'] = user.user_id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return '用户名或密码有误，请确认后再登录！'

    return render_template('login.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user = User(request.form.get('username'))
        # user.username = username
        user.password = password
        user.email = email
        user.phone = phone
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.user_id == user_id).first()
        if user:
            g.user = user


@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}


if __name__ == '__main__':
    app.run()
