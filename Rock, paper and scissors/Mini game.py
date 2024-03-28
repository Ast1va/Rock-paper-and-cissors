import random

def tas_kagit_makas():
    secenekler = ['taş', 'kağıt', 'makas']
    kullanici_skor = 0
    bilgisayar_skor = 0

    for _ in range(5):
        bilgisayar_secimi = random.choice(secenekler)
        kullanici_secimi = input("Taş, kağıt veya makas seçin: ").lower()

        while kullanici_secimi not in secenekler:
            print("Geçersiz giriş. Lütfen taş, kağıt veya makas seçin.")
            kullanici_secimi = input("Taş, kağıt veya makas seçin: ").lower()

        if kullanici_secimi == bilgisayar_secimi:
            print("Berabere! Bilgisayarın seçimi:", bilgisayar_secimi)
        elif (kullanici_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
             (kullanici_secimi == 'kağıt' and bilgisayar_secimi == 'taş') or \
             (kullanici_secimi == 'makas' and bilgisayar_secimi == 'kağıt'):
            kullanici_skor += 1
            print("Kazandınız! Bilgisayarın seçimi:", bilgisayar_secimi)
        else:
            bilgisayar_skor += 1
            print("Kaybettiniz! Bilgisayarın seçimi:", bilgisayar_secimi)

    print("Toplam Skorlar:")
    print("Kullanıcı:", kullanici_skor)
    print("Bilgisayar:", bilgisayar_skor)

    if kullanici_skor > bilgisayar_skor:
        print("Oyunu kazandınız!")
    elif kullanici_skor < bilgisayar_skor:
        print("Oyunu kaybettiniz!")
    else:
        print("Oyun berabere!")

tas_kagit_makas()
