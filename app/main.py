from flask import Flask
from configuration import configure_all

app = Flask(__name__)

configure_all(app)

app.run(host="0.0.0.0", port=5000,debug=True)