from ext.extension import mysql


class Biodata(mysql.Model):
    id = mysql.Column(mysql.Integer,primary_key=True)
    username = mysql.Column(mysql.String(100),unique=True,nullable=False)
    usia = mysql.Column(mysql.Integer,nullable=True)
    skill = mysql.Column(mysql.String(100),nullable=True)
    NIM = mysql.Column(mysql.String(20),unique=True,nullable=False)

    def __repr__(self):
        return f'{self.username},{self.usia},{self.skill},{self.NIM}'