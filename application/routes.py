from application import app, db
from application.models import Address

from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
   
    return render_template("index.html", login=False)
