import datetime


year = int(datetime.datetime.now().strftime('%Y'))-2
now  = str(datetime.datetime.now().strftime('%d/%m'))+"/"+str(year)
print now
