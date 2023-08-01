from ext.extension import mysql

class Matakuliah(mysql.Model):
    id = mysql.Column(mysql.Integer,primary_key=True,unique=True,nullable=False)
    matkul = mysql.Column(mysql.String(255),nullable=False)
    dosen_pengampu = mysql.Column(mysql.String(255),nullable=True)
    nilai_akhir = mysql.Column(mysql.Integer,nullable=True)
    SKS = mysql.Column(mysql.Integer,nullable=True)

    def __repr__(self):
        return f'{self.matkul},{self.dosen_pengampu},{self.nilai_akhir},{self.SKS}'