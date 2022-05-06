from ftplib import FTP
from logging import log

ip = '127.0.0.10'
port = 2121

handler = FTP()
handler.connect(ip, port)
handler.login('Rasp1', '12345')

nameFile = 'Viagem.xls'

handler.storbinary('STOR ' + nameFile,
                   open('C:\\Users\\Willa\\OneDrive\\Área de Trabalho\\Send_Files\\Viagem.xls',
                        'rb'))



