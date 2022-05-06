import pyodbc, os, time

def inserirPlan(plan, sheet, tabela):
    driver= '{ODBC Driver 17 for SQL Server}'
    with pyodbc.connect('DRIVER='+driver+';Server=LAPTOP-M3HQ9GT1; DataBase=MyCompany; Trusted_Connection=yes') as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO " + tabela + " (FK_ID_VIAGEM, MED_DATE, MED_TIME, AM1, AM2, AM3, AM4, AM5) SELECT * " +
                           "FROM OPENROWSET('Microsoft.ACE.OLEDB.12.0', " +
                           "'Excel 12.0; Database=C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Files_Received\\" + plan + "; HDR=YES + ; IMEX=1', " +
                           "'SELECT * FROM [" + sheet + "$]')")
            
def main():     
    driver= '{ODBC Driver 17 for SQL Server}'
    with pyodbc.connect('DRIVER=' + driver + ';Server=LAPTOP-M3HQ9GT1; DataBase=MyCompany; Trusted_Connection=yes') as conn:
        with conn.cursor() as cursor:

            cursor.execute("SELECT COUNT(1) FROM VIAGENS;")
            test = cursor.fetchone()
            lenght = test[0]
            flag = 1
            while flag <= lenght:
                try:
                    plan = 'Viagem ' + str(flag) + '.xls'
                    arq = open("C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Files_Received\\" + plan, "rb")
                except Exception:
                    flag += 1
                    pass
                else:
                    arq.close()
                    break
                     
            inserirPlan(plan, 'Pup', 'MED_PUP')
            inserirPlan(plan, 'Heart', 'MED_HEART')

            cursor.execute("SELECT COUNT(*) FROM MED_PUP;")
            test = cursor.fetchone()
            lenght = test[0]
            flag = 0
            while flag <= lenght:
                flag += 1
                cursor.execute("UPDATE MED_PUP SET MEDIA = dbo.VLR_MEDIOP(" + str(flag) + ") WHERE ID_MED = " + str(flag) + ";")
                cursor.execute("UPDATE MED_HEART SET MEDIA = dbo.VLR_MEDIOH(" + str(flag) + ") WHERE ID_MED = " + str(flag) + ";")
                
            os.remove(r"C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Files_Received\\" + plan)




if __name__ == '__main__':
    print("Iniciando inserção de dados no BD...\n")
    while True:
        time.sleep(2)
        try:
            main()
        except Exception:
            print('Nenhum arquivo importado no momento...')
        else:
            print('Arquivo importado para base de dados!')


