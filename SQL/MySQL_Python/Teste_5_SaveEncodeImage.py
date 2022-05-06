import base64
import pymysql.cursors

conexao = pymysql.connect(db='db_funcionarios', user='root', passwd='W3l3a3@$')
cursor = conexao.cursor()

with open("luis.png", "rb") as imageFile:
    imgs = base64.b64encode(imageFile.read())

dados = ("Luis", imgs)

cursor.execute("INSERT INTO tbl_teste (Nome_Func, Img_pup) VALUES (%s, %s)", dados)

conexao.commit()
conexao.close()




