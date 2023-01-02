rehber = {
    "karakter1": {"Ev adresi":"Ankara","İş adresi:":"Kırşehir","Ev telefonu":"02366844","Cep telefonu":"0546465454"}
}

isimler = rehber.keys()

aranankisi = input("Aranan isim: ")
if aranankisi in isimler:
    flag = True #bayrak
else:
    flag=False
arananozellik = input("Aranan bigi: ")


if flag:
    print(rehber.get(aranankisi).get(arananozellik,"Bilgi bulunamadı."))
else:
    print("Aranan kişi rehberde bulunamadı.")





