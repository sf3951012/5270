#Feb 22 class notes
# https://getbootstrap.com/docs/4.3/getting-started/introduction/
#import Flask
import flask
#import render_template from Flask
from flask import Flask
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

post = [
        {
            'author' :'Sijia Fan',
            'title': 'Blog',
            'date_posted': ''
        },
        {
            'author' :'Sijia Fan1',
            'title': 'Blog1'
        }
    ]


@app.route("/")
@app.route("/home")        
def home():
    return render_template('home.html')
        #'<h1> home page </h1>'
     
#```<!doctype html>
#<html> #make separete html files, and python code just point to that

#'''

@app.route("/about")
def about():
    return render_template('about.html')
        #'<h1> About Page </h1>'

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route("/login")
#def login():
#    form1 = Reg

@app.route("/register")
def login():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form=form)



