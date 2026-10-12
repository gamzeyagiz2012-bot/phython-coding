import random

secenekler = ["taş", "kağıt", "makas"]

while True:
    secim = input("Taş, kağıt veya makas seçin (çıkmak için 'q' tuşuna basın): ").lower()
    if secim == 'q': break
    if secim not in secenekler:continue

    bot = random.choice(secenekler)
    print(f"bilgisayar: {bot}")
    if secim == bot:
        print("Berabere!")
    elif (secim == "taş" and bot == "makas") or (secim == "kağıt" and bot == "taş") or (secim == "makas" and bot == "kağıt"):
        print("Kazandınız!")
    else:
        print("kaybettiniz!")