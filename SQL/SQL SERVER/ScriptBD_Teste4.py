import pyodbc

def inserirPlan(plan, sheet, tabela):
    cursor.execute("INSERT INTO " + tabela + " (FK_ID_VIAGEM, MED_DATE, MED_TIME, AM1, AM2, AM3, AM4, AM5) SELECT * " +
                   "FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0', " +
                   "'Excel 12.0; Database=C:\\Users\\Willa\\OneDrive\\Área de Trabalho\Relatórios\\" + plan + "; HDR=YES + ; IMEX=1', " +
                   "'SELECT * FROM [" + sheet + "$]')")

driver= '{ODBC Driver 17 for SQL Server}'
try:
    plan = 'Viagem.xls'
    arq = open("C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Relatórios\\" + plan, "rb")
    if arq != Exception:
        arq.close()
    with pyodbc.connect('DRIVER='+driver+';Server=LAPTOP-M3HQ9GT1; DataBase=MyCompany; Trusted_Connection=yes') as conn:
        with conn.cursor() as cursor:

            inserirPlan(plan, 'Pup', 'MED_PUP')
            inserirPlan(plan, 'Heart', 'MED_HEART')

            flag = 0
            while flag < 8:
                print (flag)
                flag += 1
                cursor.execute("UPDATE MED_PUP SET MEDIA = dbo.VLR_MEDIO(" + str(flag) + ") WHERE ID_MED = " + str(flag) + ";")
                cursor.execute("UPDATE MED_HEART SET MEDIA = dbo.VLR_MEDIOH(" + str(flag) + ") WHERE ID_MED = " + str(flag) + ";")

            cursor.execute("SELECT ID_MED, MED_DATE, MEDIA FROM MED_PUP;")
            
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]) + " " + str(row[2])) #Define a quantidade de colunas que irá aparecer
                row = cursor.fetchone()

            cursor.execute("SELECT ID_MED, MED_DATE, MEDIA FROM MED_HEART;")
            
            row = cursor.fetchone()
            while row:
                print (str(row[0]) + " " + str(row[1]) + " " + str(row[2])) #Define a quantidade de colunas que irá aparecer
                row = cursor.fetchone()

except Exception:
    print("Nenhum arquivo existente.")
