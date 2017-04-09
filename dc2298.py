from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from models import *


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@host/db'
# SQLALCHEMY_DATABASE_URI da modificare a seconda se usiate mysql o meno
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.app = app
db.init_app(app)

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='vinci98gl2@gmail.com',
    MAIL_DEFAULT_SENDER='vinci98gl2@gmail.com',
    MAIL_PASSWORD='*****************************************'
)
mailbox = Mail(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/mail", methods=['POST'])
def mail():
    app.logger.debug(request.form.get('Username'))
    text = request.form.get('Text') \
        + '\n\n' + request.form.get('Username').center(40, '=') \
        + '\n' + request.form.get('Email')
    msg = Message(
        'Contact form DC2298',
        recipients=['wayframer@cryptolab.net'],
        body=text)
    mailbox.send(msg)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
