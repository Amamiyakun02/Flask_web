from flask import Blueprint, render_template, redirect, url_for, request
from flask import flash
from werkzeug.security import generate_password_hash
from database.models.users import Users
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('yt/login.html')

@auth.route('/signup')
def signup():
    return render_template('yt/signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first()

    if user:
        flash('email address already exist')
        return redirect(url_for('auth.login'))

    new_user = Users(email=email,name=name,password = generate_password_hash(password,method='sha256'))


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))

