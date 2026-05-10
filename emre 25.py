import datetime
import locale

locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')

tarih_metni = '29 Ekim 1923 saat 14:32:11'
print("Metin halindeki tarih = ", tarih_metni)

tarih_nesnesi = datetime.datetime.strptime(tarih_metni, '%d %B %Y saat %H:%M:%S')
print("Tarih nesnesi = ", tarih_nesnesi)

print(tarih_nesnesi.year)
print(tarih_nesnesi.month)
print(tarih_nesnesi.day)
