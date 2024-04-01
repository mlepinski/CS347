import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get('http://api:5000/random')
    jsonResponse = response.json()
    num = jsonResponse['rand'];    
    return render_template("index.html", randNum = num)

if __name__ == '__main__':
    app.run(port=5000)
