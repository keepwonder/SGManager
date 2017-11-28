from flask import session
from apps.front.models import User
from main import app
from config import DevConfig


@app.before_request
def my_before_request():
    user_id = session.get(DevConfig.USER_ID)
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            g.user = user


@app.context_processor
def my_context_processor():
    if hasattr(g, 'user'):
        return {'user': g.user}
    return {}
