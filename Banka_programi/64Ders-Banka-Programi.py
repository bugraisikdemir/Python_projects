import time
from os import system as komut

class Musteri():
    def __init__(self,ID,PAROLA,ISIM):
        self.isim = ISIM
        self.id = ID
        self.parola = PAROLA
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()

    def musteri_ol(self,ID:str,PAROLA:str,ISIM:str):
        self.musteriler.append(Musteri(ID,PAROLA,ISIM))
        print("Bankamıza kayıt olduğunuz için teşekkür ederiz !")

def main():
    banka = Banka()
    while True:
        komut("cls")
        print("""
        [1] Banka müşterisiyim
        [2] Banka müşterisi olmak istiyorum
        """)

        secim = input("Seçiminiz: ")

        if secim == "1":
            ids = [i.id for i in banka.musteriler]
            ID = input("ID girin: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.id: #müşteri bulundu
                        print("Hoş geldiniz {}".format(musteri.isim))
                        parolaa = input("Parolanız: ")
                        if parolaa == musteri.parola:
                            print("Giriş başarılı.")
                            while True:
                                komut("cls")
                                print("""
                                [1] Bakiye sorgula
                                [2] Para yatır (kendi hesabıma)
                                [3] Para yatır (başka hesaba)
                                [4] Para çek
                                [Q] Çıkış
                                """)

                                secim2 = input("İşleminiz ?")

                                if secim2 == "1":
                                    print("Bakiyeniz: {}".format(musteri.bakiye))
                                    input("Ana menüye dönmek için enter'basın !")
                                elif secim2 == "2":
                                    miktar = int(input("Miktar: "))
                                    onay = input("Kendi hesabınıza {} Tl para yatırma işlemini onaylıyor musunuz? : E/H\n".format(miktar))
                                    if onay == "E" or onay == "e":
                                        musteri.bakiye += miktar
                                        print("Paranız hesabınıza yatırıldı.")
                                    elif onay == "H" or onay == "h":
                                        print("İşlem iptal edildi")
                                        input("Ana menüye dönmek için enter'e basın !")
                                    else:
                                        print("Hatalı girildi işlem iptal !")
                                        input("Ana menüye dönmek için enter'e basın !")
                                elif secim2 == "3":
                                    arananID = input("Para gönderilecek müşteri ID ? ")
                                    if arananID in ids:
                                        for digerMusteri in banka.musteriler:
                                            if arananID  == digerMusteri.id:
                                                if miktar <= musteri.bakiye:
                                                    miktar = int(input("Gönderilecek miktar ? "))
                                                    onay = input("{} adlı müşterimize {} Tl para yatırma işlemini onaylıyor musnuz ? E/H\n".format(digerMusteri.isim,miktar))
                                                    if onay == "e" or onay == "E":
                                                        digerMusteri.bakiye += miktar
                                                        musteri.bakiye -= miktar
                                                        print("Para gönderildi.")
                                                        input("Ana menüye dönmek için enter' basın.")
                                                    elif onay == "h" or onay == "H":
                                                        print("İşlem İptal edildi.")
                                                        input("Ana menüye dönmek için enter'e basın.")
                                                    else:
                                                        print("Hatalı giriş, işlem iptal.")
                                                        input("Ana menüye dönmek için enter'e basın.")
                                                else:
                                                    print("Bakiyeniz bu işlem için yetersiz.")
                                                    input("Ana menüye dönmek için enter'e basın.")
                                    else:
                                        print("Müşteri bulunamadı.")
                                        input("Ana menüye dönmek için enter'e basın.")
                                elif secim2 == "4":
                                    miktar = int(input("Çekilecek miktar: "))
                                    if miktar <= musteri.bakiye:
                                        musteri.bakiye -= miktar
                                        print("İşlem tamamlandı paranızı alınız.")
                                        input("Ana menüye dönmek için enter'e basınız.")
                                    else:
                                        print("Bakiyeniz bu işlem için yetersiz.")
                                        input("Ana menüye dönmek için enter'e basınız.")

                                elif secim2 == "q" or secim2 == "Q":
                                    break
            else:
                print("Bankamıza kayıtlı böyle bir kullanıcı yok. Lütfen müşteri kaydı yaptırın.")
                input("Ana menüye dönmek için enter'e basın.")
        elif secim == "2":
            ID = input("ID oluşturun: ")
            ISIM = input("İsminizi girin: ")
            PAROLA= input("Şifre oluşturun: ")
            banka.musteri_ol(ID,PAROLA,ISIM)
            time.sleep(1)
            input("Ana menüye dönmek için enter'e basın.")

        else:
            print("Hatalı giriş yaptınız.")
            input("Ana menüye dönmek için enter'e basın.")

if __name__ == "__main__":
    main()

