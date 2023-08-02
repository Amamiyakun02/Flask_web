from flask import Blueprint, render_template
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('yt/index.html')


@main.route('/profile')
@login_required
def profile():
    username = current_user.username
    return render_template('yt/profil.html', name=username)
