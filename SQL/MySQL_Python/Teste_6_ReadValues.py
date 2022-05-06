import base64
import pymysql.cursors
import numpy as np

conexao = pymysql.connect(db='db_funcionarios', user='root', passwd='W3l3a3@$')
cursor = conexao.cursor()

comando_sql = "SELECT Img_pup FROM tbl_teste WHERE ID_Func = 1;"

cursor.execute(comando_sql)

val_lidos = cursor.fetchall()

for i in val_lidos:
    val_lidos[i] *= 1

type(img)
