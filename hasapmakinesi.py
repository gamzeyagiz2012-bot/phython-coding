sayı1 = input("Birinci sayıyı giriniz: ")
sayı2 = input("İkinci sayıyı giriniz: ")
secim = input("Yapmak istediğiniz işlemi seçiniz (+, -, *, /): ")
if secim == "+":
    sonuc=sayı1 + sayı2
    print(sonuc)
elif secim == "*":
    sonuc=sayı1 *sayı2
    print(sonuc)
elif secim == "-":
    sonuc=sayı1 - sayı2
    print(sonuc)