toplam=0
sayac=0
sayi=0
while sayi!=1:
    sayi=int(input("Sayı giriniz:"))
    toplam+=sayi
    sayac+=1

print("Toplam=",toplam)
ort=toplam/sayac
print("Ortalama=",ort)