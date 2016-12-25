from flask import Flask
from hexMap import hexMap
app = Flask(__name__)

@app.route('/')
def hello_world():
    mapObj = hexMap(12,6)
    mapObj.assign(2,2,10)
    mapObj.fillMap()
    str = mapObj.mapString()
    return str
