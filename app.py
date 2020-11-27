# import dependency 
from flask import Flask 
#create a new Flask app instance 
app = Flask(__name__)
#create Flask routes 
@app.route('/')
def hello_world():
    return '''Hello world!'''
