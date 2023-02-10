from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def greet():
    return 'welcome'


@app.route('/welcome/back')
def returning():
    return 'welcome back'


@app.route('/welcome/home')
def home():
    return 'welcome home'
