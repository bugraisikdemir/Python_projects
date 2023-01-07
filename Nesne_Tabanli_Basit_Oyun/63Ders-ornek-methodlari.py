import random,os

class Dusman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(30,70)
        self.kalkan = random.randint(0,10)
        self.guc = random.randint(20,50)

    def vur(self,Oyuncu):
        damage = self.guc - Oyuncu.kalkan
        Oyuncu.saglik -= damage
        if Oyuncu.saglik <= 0:
            Oyuncu.sagmi = False


class Oyuncu():
    def __init__(self):
        self.sagmi = True
        self.saglik = 500
        self.kalkan = 20
        self.guc = 55

    def vur(self,Dusman):
        damage = self.guc - Dusman.kalkan
        Dusman.saglik -= damage
        if Dusman.saglik <= 0:
            Dusman.sagmi = False
            dusmanlar.remove(Dusman)


dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman())

OyuncuBen = Oyuncu()

while True:
    os.system("cls")
    print("Oyuncu Durumu  ---> Sağlık: {}  ---> Güç: {}  ---> Kalkan: {}".format(OyuncuBen.saglik,OyuncuBen.guc,OyuncuBen.kalkan))
    if OyuncuBen.sagmi == False:
        print("Oyun Bitti")
        quit()
    if not dusmanlar:
        print("Tebrikler !!")
        quit()


    for i in dusmanlar:
        print("{}. Düşman Durum  ---> Sağlık: {}  ---> Güç: {}  ---> Kalkan: {}".format(dusmanlar.index(i),i.saglik,i.guc,i.kalkan))

    secim =int(input("Düşman seçin ! : "))
    Dusman=dusmanlar[secim]
    OyuncuBen.vur(Dusman)
    if dusmanlar:
        saldiran = dusmanlar[random.randint(0,len(dusmanlar) - 1)]
        saldiran.vur(OyuncuBen)



















