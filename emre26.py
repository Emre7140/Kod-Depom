import datetime
import locale

locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

bugun = datetime.datetime.now()
yarin = datetime.date(bugun.year, bugun.month, bugun.day+1)

print('Bugün :', bugun)
print(bugun.strftime('%d/%m/%Y'))
print('Yarın :', yarin)
print(yarin.strftime('%d/%m (%Y)'))
print(bugun.strftime('%m/%d/%Y, %H:%M:%S'))
print(bugun.strftime('%d %b, %Y'))
print(bugun.strftime('%d %B, %Y'))
print(bugun.strftime('%I%p'))
