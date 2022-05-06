#encoding: utf-8

import xlwt

#from datetime import datetime

#from databases import get_databases

workbook = xlwt.Workbook()                  #cria o objeto, a planilha
worksheet = workbook.add_sheet(u'Simple')   #cria a folha
worksheet.write(0, 0, u'Simples')           #escreve na célula com base nas coordenadas
workbook.save('simple.xls')                 #salva a planilha e nomeia

