
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import urllib.request
import urllib.parse

import json
app = Flask(__name__)

webHookURL = "https://b24-711w54.bitrix24.ru/rest/1/pf26w00qvw4fiqto/"


def http_build_query(data):
    parents = list()
    pairs = dict()

    def renderKey(parents):
        depth, outStr = 0, ''
        for x in parents:
            s = "[%s]" if depth > 0 or isinstance(x, int) else "%s"
            outStr += s % str(x)
            depth += 1
        return outStr

    def r_urlencode(data):
        if isinstance(data, list) or isinstance(data, tuple):
            for i in range(len(data)):
                parents.append(i)
                r_urlencode(data[i])
                parents.pop()
        elif isinstance(data, dict):
            for key, value in data.items():
                parents.append(key)
                r_urlencode(value)
                parents.pop()
        else:
            pairs[renderKey(parents)] = str(data)

        return pairs
    return urllib.parse.urlencode(r_urlencode(data))

def sendPOST(url='https://postman-echo.com/post',method="",params={"key1":"value"}):
    data = json.dumps(params).encode('utf-8')
    req = urllib.request.Request(url+method, method="POST")
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    req.add_header('Content-Length', len(data))
    res = {}
    with urllib.request.urlopen(req, data) as f:
        res = json.load(f)        
    return res

def sendGET(url='https://postman-echo.com/get/',method="",params={"key1":"value"}):
    with urllib.request.urlopen(url+method+"?"+http_build_query(params)) as f:
        res = json.load(f)        
    return res

def postToChat(message, to=1,typ="SYSTEM"):
    method = "im.notify"
    data = {
        "to":to,
        "message":message,
        "type":typ
    }
    # return sendPOST(webHookURL,method,data)
    return sendPOST()

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    data ={}
    if request.method == 'POST':
        data = request.form
    return(json.dumps(data))

@app.route('/eventsHandler', methods = ['GET', 'POST'])
def eventHandler():
    res = postToChat(json.dumps(request.form))
    return json.dumps(res)

if __name__ == "__main__":
    app.run()

