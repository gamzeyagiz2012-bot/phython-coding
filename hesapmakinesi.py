print("*** HESAP MAKİNESİ ***")

islem = input("İşlemi giriniz (Örn: 1+1): ")

try:
    sonuc = eval(islem)
    print("Sonuç:", sonuc)
except:
    print("Hata: Lütfen geçerli bir matematiksel işlem giriniz!")