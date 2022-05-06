import psycopg2


con = psycopg2.connect(host='localhost', database='Teste',
user='postgres', password='W3l3a3@$', port = '5432')

cur = con.cursor()

file = open('D:/estoque_21032021.csv')

cur.copy_expert("copy estoque(codigo, produto, categoria, marca, preco, quantidade)  from 'D:/estoque.csv' with delimiter as ';' CSV HEADER", file)
con.commit()

file.close()


cur.execute('select * from estoque')

recset = cur.fetchall()

for rec in recset:
    print (rec)

con.close()
