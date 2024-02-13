from flask import Flask

app = Flask(__name__)


@app.route('/v1/checkout')
def hello():
    return 'Hello from CHECKOUT server!'