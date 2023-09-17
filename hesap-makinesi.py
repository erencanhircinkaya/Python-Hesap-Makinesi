print("""
***************************
Hesap Makinesi

1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Üs Alma
6.Karakök Bulma
7.Logaritma Bulma
8.Dereceyi Radyana Çevirme
9.Radyanı Dereceye Çevirme
10.Sinüs Bulma
11.Kosinüs Bulma
12.Tanjant Bulma
13.Cotanjant Bulma
Çıkmak için q ya basın...

***************************
""")

import time
import math
while True:
    islem = int(input("İşleminizi giriniz:"))

    if (islem == "q"):
        print("İşleminiz sonlandırılıyor...")
        time.sleep(1)
        print("Tekrar bekleriz...")
        break

    elif (islem == 1):
        sayi1 = int(input("Sayı giriniz:"))
        sayi2 = int(input("Sayı giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} + {} = {}".format(sayi1, sayi2, sayi1 + sayi2))

    elif (islem == 2):
        sayi1 = int(input("Sayı giriniz:"))
        sayi2 = int(input("Sayı giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} - {} = {}".format(sayi1, sayi2, sayi1 - sayi2))

    elif (islem == 3):
        sayi1 = int(input("Sayı giriniz:"))
        sayi2 = int(input("Sayı giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} x {} = {}".format(sayi1, sayi2, sayi1 * sayi2))

    elif (islem == 4):
        sayi1 = int(input("Sayı giriniz:"))
        sayi2 = int(input("Sayı giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("{} / {} = {}".format(sayi1, sayi2, sayi1 / sayi2))

    elif (islem == 5):
        sayi1 = int(input("Sayının tabanını giriniz:"))
        sayi2 = int(input("Üssü giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        x = math.pow(sayi1,sayi2)
        print("{} üssü {} = {}".format(sayi1, sayi2, math.pow(sayi1,sayi2)))

    elif (islem == 6):
        sayi1 = int(input("Sayı giriniz:"))
        print("İşlem yapılıyor...")
        time.sleep(1)
        x = math.sqrt(sayi1)
        print("{} karakökü = {}".format(sayi1,math.sqrt(sayi1)))

    elif (islem == 7):
        sayi1 = int(input("Sayı giriniz:"))
        sayi2 = int(input("Sayı giriniz:"))
        print("İşlem yapılıyor...")
        time.sleep(1)
        x = math.log(sayi1,sayi2)
        print("{} sayısının {} a logaritması = {}".format(sayi1,sayi2,math.log(sayi1,sayi2)))

    elif (islem == 8):
        sayi1 = int(input("Dereceyi giriniz:"))
        print("İşlem yapılıyor...")
        time.sleep(1)
        x = math.radians(sayi1)
        print("{} derece = {} radyandır".format(sayi1,math.radians(sayi1)))

    elif (islem == 9):
        sayi1 = int(input("Radyanı giriniz:"))
        print("İşlem yapılıyor...")
        time.sleep(1)
        x = math.radians(sayi1)
        print("{} radyan {} derecedir".format(sayi1, math.radians(sayi1)))

    elif (islem == 10):
        a = input("Radyan için = R , Derece için = D")
        if (a == "r" or a == "R"):
            sayi1 = int(input("Sayıyı giriniz:"))
            x = math.sin(sayi1)
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            print("Sin {} = {}".format(sayi1,x))

        elif (a == "d" or a == "D"):
            sayi1 = int(input("Dereceyi giriniz:"))
            x = math.sin(sayi1)
            y = math.radians(x)
            print("İşleminiz yapılıyor...")
            time.sleep(1)
            print("sin {} = {}".format(sayi1,y))

    elif (islem == 11):
       sayi1 = int(input("Dereceyi giriniz:"))
       print("İşleminiz yapılıyor...")
       time.sleep(1)
       print("Cos {} = {}".format(sayi1,math.cos(sayi1)))

    elif (islem == 12):
        sayi1 = int(input("Dereceyi giriniz"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        print("Tanjant {} = {}".format(sayi1,math.tan(sayi1)))

    elif (islem == 13):
        sayi1 = int(input("Dereceyi giriniz:"))
        print("İşleminiz yapılıyor...")
        time.sleep(1)
        x = math.cos(sayi1) / math.sin(sayi1)
        print("Cotanjant {} = {}".format(sayi1,x))


