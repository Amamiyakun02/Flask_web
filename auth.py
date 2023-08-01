from flask import Blueprint,render_template, redirect,url_for


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('yt/login.html')

@auth.route('/signup')
def signup():
    return render_template('yt/signup.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('main.index'))