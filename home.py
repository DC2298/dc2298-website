from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/user", methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        user = User(username=request.form['username'],
                    email=request.form['email'])
        db.session.add(user)
        db.session.commit()
        
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
