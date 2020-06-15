from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '为什么我用了一天的时间才学会!'

if __name__ == '__main__':
    app.run()
