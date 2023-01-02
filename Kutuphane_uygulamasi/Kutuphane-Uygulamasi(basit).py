
import os
kitapliste = list()


menu = """
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış
"""

def kitapekle(kitap:tuple,liste:list): #eklenecek kitabı kitap değişkenine eklenecek listeyide liste değişkenine tanımladık ve profesyonel olması içinde tuple ve liste olduğunu belirttik
    liste.append(kitap)
    print("Ekleme işlemi tamamlandı.")
    print("Ana menuye dönmek için enter'e basın.")
    input()

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kitapcikar(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitap çıkarma işlemi tamamlandı.")
        print("Ana menuye dönmek için enter'e basın")
        input()
    else:
        print("Arattığınız kitap mevcut değildir.")
        print("Ana menuye dönmek için enter'e basın")
        input()

def listele(liste:list):
    for i in liste:
        print("Kitap Adı: {}  -------->>>>> Yazar: {}".format(i[0],i[1]))

    print("Ana menuye dönmek için enter'e basın")
    input()

while True:
    os.system("cls") #windows için cls --> Terminal ekranını temizler
    print(menu)

    secim = input("İşleminizi seçiniz : ")

    if secim == "1":
        kitap_adi = input("Kitabın adı: ")
        kitap_yazar= input("Kitabın yazarı: ")
        kitap = (kitap_adi,kitap_yazar)
        kitapekle(kitap,kitapliste)
    elif secim == "2":
        kitap_adi = input("Kitabın adı: ")
        kitap_yazar= input("Kitabın yazarı: ")
        kitap = (kitap_adi,kitap_yazar)
        kitapcikar(kitap,kitapliste)
    elif secim == "3":
        listele(kitapliste)
    elif secim == "q" or secim == "Q":
        print("Keyifli okumalar..")
        quit()
    else:
        print("Hatalı Giriş Yaptınız !")










