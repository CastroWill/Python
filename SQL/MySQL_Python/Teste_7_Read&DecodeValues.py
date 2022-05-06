import base64
import pymysql.cursors


conexao = pymysql.connect(db='db_funcionarios', user='root', passwd='W3l3a3@$')
cursor = conexao.cursor()

comando_sql = "SELECT * FROM tbl_teste WHERE ID_Func = 1;"

cursor.execute(comando_sql)


for row in cursor.fetchall() :
    img = (row[2])

fh = open("LuisDecode.png", "wb")
fh.write(base64.b64decode(img))
fh.close()

conexao.close()
