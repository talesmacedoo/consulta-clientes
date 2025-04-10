
from flask import url_for, render_template
from main import app


@app.route('/')
def index():
    return render_template('index.html')
