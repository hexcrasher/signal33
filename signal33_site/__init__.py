from flask import Flask


app = Flask(__name__)


#register context processors

from template_ext.form import proc
app.register_blueprint(proc)

#register controllers
from controllers import homecontroller

app.register_blueprint(homecontroller.ctrl)