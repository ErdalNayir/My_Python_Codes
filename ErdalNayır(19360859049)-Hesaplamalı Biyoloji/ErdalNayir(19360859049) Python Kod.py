# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 18:18:55 2021

@author: erdal
"""


import os # txt dosyasının olduğu konuma gitmek için
import numpy as np # başka bir matematik kütüphanesi
from scipy.integrate import quad as qd  # interal almak için gerekli bir kütüphane





"""
Dosya aç temizle fonksiyonunun çalışması için Bakteri_DNA.txt dosyasının bulunduğu konuma gidilmeli.

KOD:
    os.chdir('txt dosyasının kesin konumu')


"""

os.chdir(r"C:\Users\erdal\OneDrive\Masaüstü\ErdalNayır(19360859049)-Hesaplamalı Biyoloji")


def dosya_aç_temizle():
    with open("Bakteri_DNA.txt","r") as file: #Bakteri_DNA.txt adlı dosya açılıp içindeki veri saklanıyor
            DNA=file.read()

            DNA=DNA.replace("\n","") # veri string olduğundan satırbaşları \n ler siliniyor.

    return DNA

DNA_sekans=dosya_aç_temizle()



kesim_parçası_indeks=[]

def enzim_kesim_parçası_bul(): # CCGG nin bulunduğu tüm başlangıç indekslerini bulur.
    HpaII='CCGG'

    Kesim_başlangıç_indeks=[]

    for indeks in range(len(DNA_sekans)):
        if DNA_sekans.startswith(HpaII,indeks): #startswith("Aranacak string",aramaya_başlanan_indeks)
            Kesim_başlangıç_indeks.append(indeks)
    return Kesim_başlangıç_indeks

kesim_parçası_indeks=enzim_kesim_parçası_bul()



def dna_fragmanları_bul_ve_depola():

    fragmanlar=[]#sonradan fragmanları depolamak için liste oluşturuldu

    fragman_uzunlukları=[] # sonradan fragman uzunluklarını depolamak için oluşturuldu.

    for indeks in range(len(kesim_parçası_indeks)-1): # 326 ya kadar gitti  # 1 fazlası ile sınır aşılıyor

        sekans=str(DNA_sekans[kesim_parçası_indeks[indeks]+3:kesim_parçası_indeks[indeks+1]-1]) # fragmanlar oluşturuluyor

        sekans_uzunluk=len(sekans) #fragmanın uzunluğu hesaplanıyor



        fragmanlar.append(sekans) # fragman listeye konuluyor
        fragman_uzunlukları.append(sekans_uzunluk) # fragman uzunluğu listeye konuluyor


    sekans_son=str(DNA_sekans[kesim_parçası_indeks[327]+3:]) # geriye kalan string son fragman oluyor +3 olmasının sebebi ise baştaki CCGG yi dahil etmemek için.
    sekans_son_uzunluk=len(sekans_son) # kalan son parçanın uzunluğu


    fragmanlar.append(sekans_son) # son fragman depolanıyor
    fragman_uzunlukları.append(sekans_son_uzunluk) # son fragman uzunluğu depolanıyor

    return fragmanlar,fragman_uzunlukları


Fragmanlar,Fragman_Uzunlukları=dna_fragmanları_bul_ve_depola()

"""
uzunluk[0]==[0-100)
uzunluk[1]==[100-200)
uzunluk[2]==[200-300)
uzunluk[3]==[300-400)
uzunluk[4]==[400-500)
uzunluk[5]==[500-600)
uzunluk[6]==[600-Inf)

"""


def uzunlukları_aralıklara_böl():

    uzunluk=[0,0,0,0,0,0,0]

    for i in Fragman_Uzunlukları:

        if i>=0 and i<100:
            uzunluk[0]+=1
        elif i>=100 and i<200:
             uzunluk[1]+=1
        elif i>=200 and i<300:
             uzunluk[2]+=1
        elif i>=300 and i<400 :
             uzunluk[3]+=1
        elif i>=400 and i<500 :
             uzunluk[4]+=1
        elif i>=500 and i<600 :
             uzunluk[5]+=1
        elif i>=600:
             uzunluk[6]+=1

    return uzunluk

Gerçek_uzunluk_aralıkları=uzunlukları_aralıklara_böl()


def p_değerini_bul(): # fonksiyondaki p değeri için fonksiyon oluşturdum

    C_sayısı=0
    G_sayısı=0

    C_ihtimal=0
    G_ihtimal=0

    p_değeri=0

    for i in DNA_sekans:
        if i=="C":
            C_sayısı+=1
        elif i=="G":
            G_sayısı+=1

    C_ihtimal=C_sayısı/len(DNA_sekans)
    G_ihtimal=G_sayısı/len(DNA_sekans)


    p_değeri=C_ihtimal**2*G_ihtimal**2

    return p_değeri

p=p_değerini_bul()



def fonksiyon(x): # fonksiyonu tanımlıyoruz

    return p*np.exp(-p*x)


def integral_ile_olasılık_bul(fonksiyon):

    ihtimaller=[0 for i in range(7)] #çıkan olasılıklar depolanacak

    ihtimaller[0]=qd(fonksiyon,0,100)[0] # quad fonksiyonu 2 tane sonuç return eder biz ilk olanını alıyoruz
    ihtimaller[1]=qd(fonksiyon,100,200)[0]
    ihtimaller[2]=qd(fonksiyon,200,300)[0]
    ihtimaller[3]=qd(fonksiyon,300,400)[0]
    ihtimaller[4]=qd(fonksiyon,400,500)[0]
    ihtimaller[5]=qd(fonksiyon,500,600)[0]
    ihtimaller[6]=qd(fonksiyon,600,len(DNA_sekans))[0]

    return ihtimaller

olasılıklar=integral_ile_olasılık_bul(fonksiyon)


def uzunluk_aralıklarındaki_tahmini_miktarlar(): # fonksiyon uzunluk aralıklarındaki tahmini değerleri döncek

    tahmini_uzunluk=[0 for i in range(7)]

    i=0

    while(i<7):
        tahmini_uzunluk[i]=int(olasılıklar[i]*328)

        i+=1

    return tahmini_uzunluk

tahmini_uzunluk_aralıkları=uzunluk_aralıklarındaki_tahmini_miktarlar()


def ki_kare():

    toplam=0

    i=0

    while(i<7):
        toplam=toplam+  (Gerçek_uzunluk_aralıkları[i]-tahmini_uzunluk_aralıkları[i])**2/tahmini_uzunluk_aralıkları[i]

        i+=1
    return toplam

toplam_ki_kare=ki_kare()


def ekrana_bas():

    aralık=0
    fark=0

    for i in range(7):

        if i!=6:

            fark=Gerçek_uzunluk_aralıkları[i]-tahmini_uzunluk_aralıkları[i]
            print("[{}-{}) --> Gerçek değer: {} ----- Tahmini değer: {} ** Fark: {}".format(aralık,aralık+100,Gerçek_uzunluk_aralıkları[i],tahmini_uzunluk_aralıkları[i],fark))
            aralık+=100
        elif i==6:
            fark=Gerçek_uzunluk_aralıkları[i]-tahmini_uzunluk_aralıkları[i]
            print("[{}-{}) --> Gerçek değer: {} ----- Tahmini değer: {} ** Fark: {}".format(aralık,"Inf",Gerçek_uzunluk_aralıkları[i],tahmini_uzunluk_aralıkları[i],fark))


    print("\n")
    print("Toplam ki kare değeri: {}".format(toplam_ki_kare))


ekrana_bas()




#%%
