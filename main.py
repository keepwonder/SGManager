from flask import Flask, render_template, redirect, url_for
from config import DevConfig
from ext import db
from app.front import bp as front_bp

# import app.front.hooks

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

app.register_blueprint(front_bp)

if __name__ == '__main__':
    app.run()
