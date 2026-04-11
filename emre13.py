sayi1=int(input("Sayi1 Giriniz"))
sayi2=int(input("Sayi2 Giriniz"))
artim=int(input("Kaçar kaçar artar"))
toplam=0
sayac=0
for i in range(sayi1,sayi2,artim):
    print(i)
    sayac+=1
    toplam+=i

print("Toplam",toplam)
ortalama=toplam/sayac
print("Ortalama",ortalama)