""" create our first flask code """

from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Hello from Home page"

@flask_app.route('/login')
def login():
    return "This is the logon page"

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=3000)