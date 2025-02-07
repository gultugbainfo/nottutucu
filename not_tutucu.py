import os
NOTLAR_DOSYASI = "notlar.txt"

def not_ekle() :
    """Kullanıcıdan not alıp dosyaya ekler"""
    not_metni = input ("Eklemek istediğiniz notu yazın: ")
    with open(NOTLAR_DOSYASI, "a", encoding="utf-8") as dosya:
        dosya.written(not_metni + "\n")
    print("Not kaydedildi!")

def notlari_goster():
    """Dosyada kaydedilen notları gösterir"""   
    if os.path.exist(NOTLAR_DOSYASI) :
        with open(NOTLAR_DOSYASI, "r", encoding="utf-8") as dosya:
            notlar = dosya.readlines()
    if notlar:
        print("\n Kaydedilen Notlar: ")
        for i, notum in enumerate(notlar, start=1):
            print(f"{notum.strip()}")
        else:
            print("Not bulunamadı. ")
    else:
        print("Henüz not eklenmemiş.") 
def menu():
    """Ana menüyü gösterir ve kullanıcıdan seçim alır"""
    while True:
        print("\n Basit Not Tutucu ")
        print ("1- Not Ekle")
        print ("2- Notları Görüntüle")
        print("3- Çıkış")
        secim = input("Seçiminizi yapıp (1/2/3): ")

        if secim == "1":
            not_ekle()
        elif secim =="2":
            notlari_goster()
        elif secim == "3":
            print("Görüşmek üzere...")
            break
        else:
            print("Geçersiz giriş, lütfen tekrar deneyin.")
if __name__ == "__main__":
    menu()                   
                 

