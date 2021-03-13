
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello froooom Flask!'

if __name__ == "__main__":
    app.run()

