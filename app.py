from flask import Flask
from flask import render_template
from pushould import Pushould
import os

app = Flask(__name__)

URL = os.environ['URL']
SERVER_TOKEN = os.environ['SERVER_TOKEN']
EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
CLIENT_TOKEN = os.environ['CLIENT_TOKEN']

pushould = Pushould(url=URL,
                    server_token=SERVER_TOKEN,
                    email=EMAIL,
                    password=PASSWORD)


@app.route('/')
def index():
    data = {'users': ['your', 'awesome', 'users'],
            'msg': 'from flask'}
    pushould.trigger(room='private area',
                     event='send',
                     data=data)

    return render_template('index.html',
                           url=URL,
                           client_token=CLIENT_TOKEN)


@app.route('/comment', methods=['POST'])
def comment():
    data = {'msg': 'new comment from flask'}
    pushould.trigger(room='private area',
                     event='send',
                     data=data)

    return ('', 200)


if __name__ == '__main__':
    app.run()
