from ext.extension import mysql
from flask_login import mixins

class Users(mixins,mysql.Model):
    id = mysql.Column(mysql.Integer,primary_key=True,unique=True,nullable=False)
    username = mysql.Column(mysql.String(255),unique=False,nullable=False)
    password = mysql.Column(mysql.String(255),nullable=False)
    role = mysql.Column(mysql.String(255),nullable=True)
    def __repr__(self):
        return f'{self.username},{self.password},{self.role}'

