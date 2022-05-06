import pyodbc

driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';Server=LAPTOP-M3HQ9GT1; DataBase=MyCompany; Trusted_Connection=yes') as conn:
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO MED_PUP (FK_ID_VIAGEM, MED_DATE, MED_TIME, AM1, AM2, AM3, AM4, AM5) SELECT * FROM EXCELLINK...[Pup$];")
        a = 0
        while a < 8:
            a += 1
            cursor.execute("UPDATE MED_PUP SET MEDIA = dbo.VLR_MEDIO(" + str(a) + ") WHERE ID_MED = " + str(a) + ";")
        cursor.execute("SELECT ID_MED, MED_DATE, MEDIA FROM MED_PUP;")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]) + " " + str(row[2])) #Define a quantidade de colunas que irá aparecer
            row = cursor.fetchone()
