from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route("/")
def home():
    return render_template('form.html')

@app.route("/user", methods=['POST'])
def user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
