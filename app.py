from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '我现在也不知道到底哪个对.'

if __name__ == '__main__':
    app.run()
