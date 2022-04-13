from flask import Flask,render_template,request

app=Flask(__name__)



@app.route('/')  #http://127.0.0.1:5000
def index():
    return render_template('index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('signUp.html')


@app.route('/thank_you')
def thank_you():
    first=request.args.get('first')
    last=request.args.get('last')

    return render_template('ThankYou.html',first=first,last=last)





if __name__ == '__main__':
    app.run(debug=True)
