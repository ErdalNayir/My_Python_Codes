from flask import Flask

app=Flask(__name__)

@app.route('/')  #http://127.0.0.1:5000
def index():
    return  "<h1>Merhaba</h1>"

@app.route('/information')  #http://127.0.0.1:5000/information
def info():

    return "<h2>Türkiye ile ilgili bilgiler</h2>"


if __name__ == '__main__':
    app.run()
