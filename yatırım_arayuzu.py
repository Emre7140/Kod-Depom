import customtkinter as ctk
import requests

# Temel pencere ayarları (Karanlık Mod)
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class YatirimUygulamasi(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Yatırım Simülatörü v1.0")
        self.geometry("500x550")
        self.resizable(False, False)

        # Başlangıç Bakiyeleri
        self.cuzdan = {"TL": 10000.0, "USD": 0.0, "EUR": 0.0, "GAU": 0.0}
        self.fiyatlar = {"USD": 1.0, "EUR": 1.0, "GAU": 1.0}

        # --- ARAYÜZ ELEMANLARI ---
        
        # Başlık
        self.baslik = ctk.CTkLabel(self, text="PİYASA EKRENI & CÜZDAN", font=ctk.CTkFont(size=20, weight="bold"))
        self.baslik.pack(pady=20)

        # Fiyat ve Cüzdan Tablosu Kutusu
        self.bilgi_kutusu = ctk.CTkTextbox(self, width=440, height=180, font=ctk.CTkFont(size=14))
        self.bilgi_kutusu.pack(pady=10)
        
        # Güncelle Butonu
        self.guncelle_btn = ctk.CTkButton(self, text="Fiyatları ve Cüzdanı Yenile", command=self.piyasayi_guncelle, fg_color="green", hover_color="darkgreen")
        self.guncelle_btn.pack(pady=10)

        # İşlem Seçim Alanı
        self.islem_turu = ctk.CTkSegmentedButton(self, values=["AL", "SAT"])
        self.islem_turu.set("AL")
        self.islem_turu.pack(pady=10)

        # Para Birimi Seçimi
        self.para_turu = ctk.CTkComboBox(self, values=["USD", "EUR", "GAU"])
        self.para_turu.pack(pady=10)

        # Miktar Giriş Kutusu
        self.miktar_giris = ctk.CTkEntry(self, placeholder_text="Miktar giriniz...")
        self.miktar_giris.pack(pady=10)

        # Onayla Butonu
        self.onay_btn = ctk.CTkButton(self, text="İşlemi Gerçekleştir", command=self.islem_yap)
        self.onay_btn.pack(pady=15)

        # Durum Mesajı
        self.durum_etiketi = ctk.CTkLabel(self, text="Hoş geldiniz! Lütfen fiyatları yenileyin.", text_color="yellow")
        self.durum_etiketi.pack(pady=5)

        # İlk açılışta fiyatları çek
        self.piyasayi_guncelle()

    def fiyatlari_getir(self):
        try:
            url = "https://api.exchangerate-api.com/v4/latest/TRY"
            cevap = requests.get(url).json()
            dolar = round(1 / cevap["rates"]["USD"], 2)
            euro = round(1 / cevap["rates"]["EUR"], 2)
            altin = round(dolar * 79.5, 2)
            return {"USD": dolar, "EUR": euro, "GAU": altin}
        except:
            return {"USD": 33.50, "EUR": 36.20, "GAU": 2500.00}

    def piyasayi_guncelle(self):
        self.fiyatlar = self.fiyatlari_getir()
        
        # Metin kutusunu temizle ve yeni verileri yaz
        self.bilgi_kutusu.configure(state="normal")
        self.bilgi_kutusu.delete("1.0", "end")
        
        metin = f"=== ANLIK FİYATLAR ===\n"
        metin += f"Dolar (USD): {self.fiyatlar['USD']} TL\n"
        metin += f"Euro (EUR): {self.fiyatlar['EUR']} TL\n"
        metin += f"Altın (GAU): {self.fiyatlar['GAU']} TL\n\n"
        metin += f"=== CÜZDANINIZ ===\n"
        metin += f"TL: {round(self.cuzdan['TL'], 2)} TL | "
        metin += f"USD: {self.cuzdan['USD']} | "
        metin += f"EUR: {self.cuzdan['EUR']} | "
        metin += f"GAU: {self.cuzdan['GAU']}\n"
        
        self.bilgi_kutusu.insert("1.0", metin)
        self.bilgi_kutusu.configure(state="disabled")
        self.durum_etiketi.configure(text="Piyasa ve cüzdan güncellendi.", text_color="green")

    def islem_yap(self):
        tür = self.islem_turu.get()
        doviz = self.para_turu.get()
        
        try:
            miktar = float(self.miktar_giris.get())
            if miktar <= 0: raise ValueError
        except ValueError:
            self.durum_etiketi.configure(text="Hata: Lütfen geçerli bir miktar girin!", text_color="red")
            return

        fiyat = self.fiyatlar[doviz]

        if tür == "AL":
            toplam_tutar = miktar * fiyat
            if self.cuzdan["TL"] >= toplam_tutar:
                self.cuzdan["TL"] -= toplam_tutar
                self.cuzdan[doviz] += miktar
                self.durum_etiketi.configure(text=f"Başarılı: {miktar} {doviz} alındı!", text_color="green")
            else:
                self.durum_etiketi.configure(text="Hata: Yetersiz TL bakiyesi!", text_color="red")
                
        elif tür == "SAT":
            if self.cuzdan[doviz] >= miktar:
                toplam_gelir = miktar * fiyat
                self.cuzdan[doviz] -= miktar
                self.cuzdan["TL"] += toplam_gelir
                self.durum_etiketi.configure(text=f"Başarılı: {miktar} {doviz} satıldı!", text_color="green")
            else:
                self.durum_etiketi.configure(text=f"Hata: Yetersiz {doviz} bakiyesi!", text_color="red")

        self.piyasayi_guncelle()
        self.miktar_giris.delete(0, "end")

if __name__ == "__main__":
    app = YatirimUygulamasi()
    app.mainloop()