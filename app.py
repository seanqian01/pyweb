from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello this is the beginning!'

if __name__ == '__main__':
    app.run()
