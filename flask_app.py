
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    data ={}
    if request.method == 'POST':
        data = request.form
    return(json.dumps(data))


if __name__ == "__main__":
    app.run()

