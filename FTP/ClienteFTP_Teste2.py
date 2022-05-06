from ftplib import FTP
from logging import log

ip = '127.0.0.10'
port = 2121

handler = FTP()
handler.connect(ip, port)
handler.login('user', '12345')

handler.cwd('/Downloads/')

FTP.retrlines(handler, 'LIST' )

handler.storbinary('STOR ' + 'Viagem 2 2020-11-26.xls',
                   open('C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Estudo\\TCC\\def_main\\Relatórios\\Viagem 2 2020-11-26.xls',
                        'rb'))




FTP.retrlines(handler, 'LIST' )
