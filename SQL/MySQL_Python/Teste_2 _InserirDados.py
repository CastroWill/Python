# Importamos a biblioteca:
import pymysql.cursors

# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='db_funcionarios', user='root', passwd='W3l3a3@$')

# Cria um cursor:
cursor = conexao.cursor()

# Executa o comando:
cursor.execute("INSERT INTO tbl_teste (Nome_Func) VALUES ('T')")

# Efetua um commit no banco de dados.
# Por padrão, não é efetuado commit automaticamente. Você deve commitar para salvar
# suas alterações.
conexao.commit()

# Finaliza a conexão
conexao.close()
