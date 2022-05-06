seg = int(input("Por favor, entre com o número de segundos que deseja converter:"))

dia = seg//86400
hr = int(seg%86400/3600)
minu = int(seg/86400%1*24%1*60//1)
segu = int(seg/86400%1*24%1*60%1*60)

print(dia,"dias,", hr,"horas,", minu,"minutos e", segu,"segundos.")
