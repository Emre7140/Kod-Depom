tercih=input("Ne izlemek istersiniz?(sinema/tiyatro):")

if tercih=="sinema":
    ogrenci=input("Öğrencisiniz?(E/H)")
    if ogrenci=="E":
        ucret=15*50/100
        print("Ödemeniz gereken tutar=",ucret,"TL dir.")
    else:
        print("Ödemeniz gereken ücret 15 TL dir") 

else:
    ogrenci=input("Öğrencisiniz?(E/H)")
    if ogrenci=="E":
        ucret=10*50/100
        print("Ödemeniz gereken tutar=",ucret,"TL dir.")
    else:
        print("Ödemeniz gereken ücret 10 TL dir")