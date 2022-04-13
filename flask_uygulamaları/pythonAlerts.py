from flask import render_template,flash,Flask,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


app = Flask(__name__)

app.config['SECRET_KEY']='mykey'

class SimpleForm(FlaskForm):

    submit=SubmitField("Click Me!")




@app.route('/',methods=['GET', 'POST'])
def index():

    form = SimpleForm()

    if form.validate_on_submit():

        flash('You just clicked the button')

        return redirect(url_for('index'))

    return render_template('flash.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
