# MANCA LA FUNZIONE DELL'E-MAIL

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from models import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@host/db'#da modificare a seconda se usiate mysql o meno 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

@app.route("/")
def home():
	return render_template('home.html')
        


if __name__ == '__main__':
    app.run(debug=True)
