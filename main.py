from flask import Flask
from config import DevConfig
from ext import db

app = Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)

from views import *
from views_admin import *

if __name__ == '__main__':
    app.run()
