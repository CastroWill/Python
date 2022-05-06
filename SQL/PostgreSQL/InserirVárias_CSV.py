import psycopg2

def insere_plan(file, cur, con, d):
    cur.copy_expert("copy estoque(codigo, produto, categoria, marca, preco, quantidade)  from 'D:/estoque_"+str(d)+"032021.csv' with delimiter as ';' CSV HEADER", file)
    con.commit()


con = psycopg2.connect(host='localhost', database='Teste',
user='postgres', password='W3l3a3@$', port = '5432')

cur = con.cursor()

for d in range(21,25):
    print('D:/estoque_'+str(d)+'032021.csv')
    file = open('D:/estoque_'+str(d)+'032021.csv')
    insere_plan(file, cur, con, d)
    file.close()


cur.execute('select * from estoque')

recset = cur.fetchall()

for rec in recset:
    print (rec)

con.close()
