from flask import Flask


app = Flask(__name__)


#register controllers
from controllers import homecontroller

app.register_blueprint(homecontroller.ctrl)