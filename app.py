from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_restful import Api
from main import *
from auth import *
from config import *
# import models
from database.models import Biodata, Matakuliah, Users

# # inisialisasi aplikasi
myApp = Flask(__name__)

myApp.register_blueprint(auth)
myApp.register_blueprint(main)
# # inisialisasi api
myApi = Api(myApp)

CORS(myApp)

# database configuration
myApp.config['SECRET_KEY'] = SECRET_KEY
myApp.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

mysql.init_app(myApp)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(myApp)


@login_manager.user_loader
def load_user(user_id):
    # Your code here to load and return the user object based on user_id
    return Users.query.get(int(user_id))


# base routes
@myApp.route('/')
def data():
    akun = Users.query.filter_by(id=3).first()
    all_nilai = Matakuliah.query.all()
    all_user = Biodata.query.all()
    print(type(all_user))
    return render_template('main/hello.html', value=[all_user, all_nilai, akun.password])


@myApp.route('/card_items')
def index():
    return render_template('main/card_items.html')


@myApp.route('/card')
def card():
    return render_template('main/ccc.html')


if __name__ == '__main__':
    myApp.run(debug=True, host='localhost', port=5000)
