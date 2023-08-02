from flask import Flask, request,render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_login import LoginManager
from ext.extension import mysql

# import models
from database.models.biodata import Biodata
from database.models.matkul import Matakuliah
from main import *
from auth import *
from config import *


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

login_manager - LoginManager()
login_manager.login_view = 'auth.login'

# base routes
@myApp.route('/')
def data():
    all_akun = Users.query.all()
    all_nilai = Matakuliah.query.all()
    all_user = Biodata.query.all()
    print(type(all_user))
    return render_template('main/hello.html', value=[all_user,all_nilai,all_akun])

@myApp.route('/card_items')
def index():
    return render_template('main/card_items.html')


@myApp.route('/card')
def card():
    return render_template('main/ccc.html')

if __name__ == '__main__':

    myApp.run(debug=True,host='localhost',port=5000)


