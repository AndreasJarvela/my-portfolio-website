from flask import Flask

from app.guest import guest

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(guest)

