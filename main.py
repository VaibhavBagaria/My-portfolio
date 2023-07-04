from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from datetime import datetime
from tkinter import messagebox
import smtplib

my_gmail="coder.vaibhav21@gmail.com"
password="odjdimxkwkyeqhyr"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route('/')
def My_portfolio():
    return render_template("portfolio.html")

@app.route('/', methods=['GET','POST'])
def email():
    user_gmail=request.form['user_email']
    text=request.form['textarea']
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(my_gmail, password)
        connection.sendmail(
            user_gmail,
            my_gmail,
            msg=f'Subject:You got a mail from one of your website!\n\n{text}'
            )

if __name__ == "__main__":
    app.run(debug=True)
    