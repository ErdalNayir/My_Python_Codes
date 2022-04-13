from flask import Flask,render_template

app=Flask(__name__)



@app.route('/<name>')  #http://127.0.0.1:5000
def index(name):
    return  render_template('{}'.format(name))








if __name__ == '__main__':
    app.run(debug=True)
