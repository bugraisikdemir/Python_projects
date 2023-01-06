import os
masalar = dict() #sözlük
for i in range(10):
    masalar[i] = 0


def hesapekle():
    masaNo = int(input("Masa No: "))
    gecerli = masalar[masaNo]
    eklenecek = float(input("Eklenecek Ücret:"))
    toplam = gecerli + eklenecek
    masalar[masaNo] = toplam


def hesapsil():
    masaNo = int(input("Masa No: "))
    gecerli = masalar[masaNo]
    eksilecek = float(input("Eksilecek Ücret:"))
    toplam = gecerli - eksilecek
    if toplam < 0:
        print("İşlemde hata var ! Kontrol ediniz.")
    else:
        print("İşlem tamamlandı !")
        masalar[masaNo] = toplam


def hesapkontrol(dosya_adi):
    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True
    except FileNotFoundError:
        dosya = open(dosya_adi, "w")
        dosya.close()
        print("İlk kez çalıştırıldı. Kayıt dosyası yaratıldı !")
        flag = False

    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])
    else:
        pass

def kayitgüncelle():
    dosya = open("kayitlar.txt","w")
    for i in range(10):
        ucret = masalar[i]
        ucret = str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()

def main():
    hesapkontrol("kayitlar.txt")
    while True:
        os.system("cls")
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle
        [3] Hesap Sil
        [Q] Çıkış
        """)


        secim = input("İşlemiiz: ")

        if secim == "1":
            for i in range(10):
                print("Masa {} için hesap {}".format(i,masalar[i]))
            print("İşlem tamamlandı !")
            print("Ana menü'ye dönmek için enter'e basın.")
            input()
        elif secim == "2":
            hesapekle()
            print("İşlem tamamlandı !")
            print("Ana menü'ye dönmek için enter'e basın.")
            input()

        elif secim == "3":
            hesapsil()
            print("Ana menü'ye dönmek için enter'e basın.")
            input()

        elif secim == "q" or secim == "Q":
            print("Çıkılıyor..")
            quit()

main()






