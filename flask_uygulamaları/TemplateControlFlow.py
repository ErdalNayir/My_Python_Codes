from flask import Flask,render_template

app=Flask(__name__)



@app.route('/')  #http://127.0.0.1:5000
def index():
    mylist=[1,2,3,4]
    puppies=["kömür","rıfkı","boncuk","duman"]
    return  render_template("controlFlow.html",mylist=mylist,puppies=puppies)






if __name__ == '__main__':
    app.run(debug=True)
