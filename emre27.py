from datetime import datetime

bugun = datetime.today()
print("Bu günün tarihi", bugun)

yil = int(input("Lütfen doğduğunuz yılı girin: "))
ay = int(input("Lütfen doğduğunuz ayı girin: "))
gun = int(input("Lütfen doğduğunuz günü girin: "))

dogum = datetime(year=yil, month=ay, day=gun)
yas = bugun - dogum
print(yas)

print(yas)
print(yas.days, "gün")
print(yas.seconds, "saniye")
print(yas.microseconds, "mikrosaniye")
