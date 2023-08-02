from flask import Blueprint, render_template, redirect, url_for, request
from flask import flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user
from database.models.users import Users
from ext.extension import mysql

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('yt/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = request.form.get('remember')
    user_login = Users.query.filter_by(email=email).first()
    if not user_login and not check_password_hash(user_login.password, password):
        flash('please check your email and password')
        return redirect(url_for('auth.login'))

    login_user(user_login)
    return redirect(url_for('main.profile'))


@auth.route('/signup')
def signup():
    return render_template('yt/signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    role = 'user'

    user = Users.query.filter_by(email=email).first()

    if user:
        flash('email address already exist')
        return redirect(url_for('auth.signup'))

    new_user = Users(email=email, username=name, password=generate_password_hash(password, method='sha256'), role=role)

    mysql.session.add(new_user)
    mysql.session.commit()
    return redirect(url_for('auth.login'))


@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))
