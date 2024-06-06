# American exspress=15 34 ve 37
# Master=16 51,52,53,54,55
#Visa=13 ve 16  4

import time


###
while True:
    try:
        toplam=0
        skno = ""  # str_kart_no
        num_list = []
        num_list2 = []
        kalan = 0
        bölüm = 0

        seçenek = int(input("Çıkış İçin 0 İşlem için 1 e basın...\n"))
        if seçenek==0:
            print("Hoçcakalın.Yine Bekleriz\n")
            break
        elif seçenek==1:
            kart_no=int(input("Kart Numaranızı Giriniz...\n"))

            skno=str(kart_no)

            for i in skno[-2::-2]:
                i=int(i)
                i=i*2
                num_list.append(i)
            for a in num_list:
                kalan=a%10
                bölüm=a/10
                bölüm=int(bölüm)
                num_list2.append(kalan)
                num_list2.append(bölüm)
            for i in num_list2:
                toplam+=i
            for sayı in skno[-1::-2]:
                sayı=int(sayı)
                toplam+=sayı

            if toplam%10!=0:
                print("Kartınız Sahtedir")
            elif toplam%10==0:
                if len(skno)==16:
                    if skno.startswith("51") or skno.startswith("52") or skno.startswith("53") or skno.startswith("54") or skno.startswith("55"):
                        print("""
                                 Kart Numarası: {}
                                 Kart Şirketi: {}
                        """.format(skno,"Master Card"))
                    elif skno.startswith("4"):
                        print("""
                                 Kart Numarası: {}
                                 Kart Şirketi: {}
                        """.format(skno,"Visa Card"))
                    else:
                        print("Girdiğiniz Kart Numarasına Ait Şirket Bulunmamaktadır...")

                elif len(skno)==15:
                    if skno.startswith("34") or skno.startswith("37"):
                        print("""
                                 Kart Numarası: {}
                                 Kart Şirketi: {}        
                        """.format(skno,"American Express"))
                    else:
                        print("Girdiğiniz Kart Numarasına Ait Şirket Bulunmamaktadır...")
                elif len(skno)==13:
                    if skno.startswith("4"):
                        print("""
                                 Kart Numarası: {}
                                 Kart Şirketi: {}
                        """.format(skno, "Visa Card"))
                    else:
                        print("Girdiğiniz Kart Numarasına Ait Şirket Bulunmamaktadır...")

                else:
                    print("Girdiğiniiz Kart Numarasının Uzunluğu Hiç bir şirketin Kart Uzunluğu ile uyuşmamaktadır.")
        else:
            print("Yanlış İşlem Seçildi")

    except ValueError:
        print("Sadece sayı girebilirsiniz...")



