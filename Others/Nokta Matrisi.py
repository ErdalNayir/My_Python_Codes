# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:15:32 2021

@author: erdal
"""



from PyQt5.QtCore import* # QApplication oluşturmak için
import sys # sayfanın oluşması ve kapatılması için
from PyQt5 import*
from PyQt5.QtWidgets import*  # tableWidgetin kullanılması için
import numpy as np  # Matris oluşturabilmek için
from PyQt5.QtGui import*  # Renklendirme için
import random as rn  # rastgele renk oluşturmak için random değer üreten kütüphane

def sayiVarMi(metin):
    metin=str(metin)

    for s in metin:

        if s.isdigit():
            return True

def Nokta_Matrisi(satir,sutun,matriks):

    app =QCoreApplication.instance() # aktif appleri bulmak için

    if app is None: # hiç app yoksa oluştur
        app = QApplication(sys.argv)

    a=0

    sutunUzunluk=len(sutun)
    satirUzunluk=len(satir)

    qwidget=QWidget() # ana sayfa

    qwidget.setWindowTitle("Nokta Matrisi")  #Sayfa başlığı
    qwidget.resize(400,400)  # Açılan pencerenin boyu 300x300 e ayarlandı
    qwidget.setWindowIcon(QIcon(r"C:\Users\erdal\OneDrive\Masaüstü\dna.png"))


    layout=QVBoxLayout()  # Vertical layout ayarlandı

    tableWidget=QTableWidget() # tablo oluşturabilmek için

    tableWidget.setColumnCount(sutunUzunluk) #sütun sayısı
    tableWidget.setRowCount(satirUzunluk) # satır sayısı

    renkKod={}

    for i in range(sutunUzunluk):
        for j in range(satirUzunluk):

            şuankiHücre="({},{})".format(j,i) # Matrisin şuanki satır ve sütun konumu

            a=str(matriks[j][i])  # değer alınıp stringe çeviriliyor

            if a=="-":

                a=" "

                item=QTableWidgetItem(a)

                item.setTextAlignment(QtCore.Qt.AlignHCenter) # string hücre ortasına konuluyor

                tableWidget.setItem(j,i,item)

            else:

                if 0<j<satirUzunluk-1 and 0<i<sutunUzunluk-1: # matrisin sınırlarından çıkmamak için

                    if str(matriks[j-1][i-1])=="-" and str(matriks[j+1][i+1])=="-": # çapraz değerlere bak

                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item) # yanlız 0 lar kontrol edildi

                    else:
                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                        rnkctrl_g="({},{})".format(j-1,i-1)

                        if rnkctrl_g not in renkKod.keys():

                            renk=np.random.randint(0,255,3)

                            tableWidget.item(j,i).setBackground(QColor(renk[0],renk[1],renk[2]))

                            renkKod[şuankiHücre]=[int(r) for r in renk]
                        else:
                            renkKod[şuankiHücre]=[renkKod[rnkctrl_g][0],renkKod[rnkctrl_g][1],renkKod[rnkctrl_g][2]]
                            tableWidget.item(j,i).setBackground(QColor(renkKod[rnkctrl_g][0],renkKod[rnkctrl_g][1],renkKod[rnkctrl_g][2]))

                elif i==0 and 0<j<satirUzunluk-1:

                    if str(matriks[j+1][i+1])!="-":

                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                        rnkctrl="({},{})".format(j+1,i+1)

                        if rnkctrl not in renkKod.keys():

                            renk=np.random.randint(0,255,3)

                            tableWidget.item(j,i).setBackground(QColor(renk[0],renk[1],renk[2]))

                            renkKod[şuankiHücre]=[int(r) for r in renk]

                        else:
                            renkKod[şuankiHücre]=[renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]]
                            tableWidget.item(j,i).setBackground(QColor(renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]))

                    else:
                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                elif i==sutunUzunluk-1 and 0<j<satirUzunluk-1:

                    if str(matriks[j-1][i-1])!="-":

                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                        rnkctrl="({},{})".format(j-1,i-1)

                        if rnkctrl not in renkKod.keys():

                            renk=np.random.randint(0,255,3)

                            tableWidget.item(j,i).setBackground(QColor(renk[0],renk[1],renk[2]))

                            renkKod[şuankiHücre]=[int(r) for r in renk]

                        else:
                            renkKod[şuankiHücre]=[renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]]
                            tableWidget.item(j,i).setBackground(QColor(renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]))

                    else:
                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                elif j==0 and 0<=i<sutunUzunluk-1:

                    if str(matriks[j+1][i+1])!="-":

                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                        rnkctrl="({},{})".format(j+1,i+1)

                        if rnkctrl not in renkKod.keys():

                            renk=np.random.randint(0,255,3)

                            tableWidget.item(j,i).setBackground(QColor(renk[0],renk[1],renk[2]))

                            renkKod[şuankiHücre]=[int(r) for r in renk]

                        else:
                            renkKod[şuankiHücre]=[renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]]
                            tableWidget.item(j,i).setBackground(QColor(renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]))

                    else:
                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                elif j==satirUzunluk-1 and 0<i<sutunUzunluk-1:

                    if str(matriks[j-1][i-1])!="-":

                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                        rnkctrl="({},{})".format(j-1,i-1)

                        if rnkctrl not in renkKod.keys():

                            renk=np.random.randint(0,255,3)

                            tableWidget.item(j,i).setBackground(QColor(renk[0],renk[1],renk[2]))

                            renkKod[şuankiHücre]=[int(r) for r in renk]

                        else:
                            renkKod[şuankiHücre]=[renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]]
                            tableWidget.item(j,i).setBackground(QColor(renkKod[rnkctrl][0],renkKod[rnkctrl][1],renkKod[rnkctrl][2]))

                    else:
                        item=QTableWidgetItem(a)

                        item.setTextAlignment(QtCore.Qt.AlignHCenter)

                        tableWidget.setItem(j,i,item)

                else:
                    item=QTableWidgetItem(a)

                    item.setTextAlignment(QtCore.Qt.AlignHCenter)

                    tableWidget.setItem(j,i,item)

    for i,j in enumerate(sutun):

        j=str(j).upper()

        font = QFont()
        font.setBold(True)

        j=QTableWidgetItem(j)
        j.setForeground(QBrush(QColor(128,0,128))) #purple

        j.setFont(font)

        hheader = tableWidget.horizontalHeader()
        hheader.setSectionResizeMode(i, QHeaderView.Stretch)

        tableWidget.setHorizontalHeaderItem(i,j)

    for i,j in enumerate(satir):

        j=str(j).upper()+" "

        font = QFont()
        font.setBold(True)

        j=QTableWidgetItem(j)
        j.setForeground(QBrush(QColor(128,0,128))) #purple

        j.setFont(font)

        vheader=tableWidget.verticalHeader()
        vheader.setSectionResizeMode(i, QHeaderView.Stretch)

        tableWidget.setVerticalHeaderItem(i,j)

    layout.addWidget(tableWidget)

    qwidget.setLayout(layout)

    qwidget.show()

    sys.exit(app.exec_())

def getDeger():

    app =QApplication(sys.argv)

    qwidget_2=QWidget()

    msg=QMessageBox()

    qwidget_2.resize(200,200)
    qwidget_2.setWindowTitle("DNA parçaları ve k değeri(0<k<4)")
    qwidget_2.setWindowIcon(QIcon(r"C:\Users\erdal\OneDrive\Masaüstü\dna.png"))

    layout=QVBoxLayout()

    ilk_eylem=False
    ikinci_eylem=False
    üçüncü_eylem=False

    eylemler=[ilk_eylem,ikinci_eylem,üçüncü_eylem]
    sekanslar=[]

    k=0

    for i,j in enumerate(["Satır","Sütun"]):
        text, okPressed = QInputDialog.getText(qwidget_2,"DNA parçaları","{} için :".format(j), QLineEdit.Normal, "")

        if okPressed and text != '':

            text=str(text)

            if sayiVarMi(text):

                msg.setIcon(QMessageBox.Critical)

                msg.setText("Sadece Harf Girebilirsiniz!")

                x = msg.exec_()

                return "-","-","-"
            else:
                text=str(text)

                sekanslar.append(text)
                eylemler[i]=True

    k, okPressed = QInputDialog.getText(qwidget_2,"DNA parçaları","k için [1,3] :", QLineEdit.Normal, "")

    if okPressed and k != '':
        k=int(k)
        eylemler[2]=True

    if k>0 and k<4:
        if eylemler[0] and eylemler[1] and eylemler[2]:

            return sekanslar[0],sekanslar[1],k

        else:
            msg.setIcon(QMessageBox.Critical)

            msg.setText("Satır ve Sütun için Mutlaka DNA sekansı girilmelidir!")

            x = msg.exec_()

            return "-","-","-"

    else:
        msg.setIcon(QMessageBox.Critical)

        msg.setText("k 1 ile 3 (1 ve 3 dahil) arasındaki tam sayılardan biri olmalıdır")

        x = msg.exec_()

        return "-","-","-"

    qwidget_2.show()
    sys.exit(app.exec_())

def Sonuc():
    satır,sütun,k=getDeger()

    if satır!="-" and sütun!="-" and k!="-":

        satır=satır.upper()
        sütun=sütun.upper()

        sütuzl= len(sütun)
        satuzl=len(satır)

        adet=sütuzl*satuzl

        adetlist=[]

        for i in range(adet):
            adetlist.append("-")

        noktaMatrisi=np.array([adetlist]).reshape(satuzl,sütuzl)

        if k ==1:

            for i in range(sütuzl):
                for j in range(satuzl):
                    if sütun[i]==satır[j]:

                        if i ==0 or j==0:
                            sayı=0

                            sayı=str(sayı)

                            noktaMatrisi[j][i]=sayı

                            sayı=int(sayı)

                        elif i!=0 and j!=0:
                            sayı=0

                            if noktaMatrisi[j-1][i-1]!="-":

                                sayı=int(noktaMatrisi[j-1][i-1])

                                sayı+=1

                                sayı=str(sayı)

                                noktaMatrisi[j][i]=sayı

                            elif noktaMatrisi[j-1][i-1]=="-":

                                noktaMatrisi[j][i]="0"

        elif k==2:
            for i in range(sütuzl-1):
                for j in range(satuzl-1):

                    if str(sütun[i])+str(sütun[i+1])==str(satır[j])+str(satır[j+1]):

                        sayı=0

                        sayı=str(sayı)

                        noktaMatrisi[j][i]=sayı

                        sayı=int(sayı)

            for i in range(sütuzl):
                for j in range(satuzl):

                    if i ==0 or j==0:

                        noktaMatrisi[j][i]=str(noktaMatrisi[j][i])

                    elif i!=0 and j!=0:
                        sayı=0

                        if noktaMatrisi[j][i]=="0" and noktaMatrisi[j-1][i-1]!="-":

                            sayı=int(noktaMatrisi[j-1][i-1])

                            sayı+=1

                            sayı=str(sayı)

                            noktaMatrisi[j][i]=sayı

        elif k==3:
            for i in range(sütuzl-2):
                for j in range(satuzl-2):

                    if str(sütun[i])+str(sütun[i+1])+str(sütun[i+2])==str(satır[j])+str(satır[j+1])+str(satır[j+2]):

                        sayı=0

                        sayı=str(sayı)

                        noktaMatrisi[j][i]=sayı

                        sayı=int(sayı)

            for i in range(sütuzl):
                for j in range(satuzl):

                    if i ==0 or j==0:

                        noktaMatrisi[j][i]=str(noktaMatrisi[j][i])

                    elif i!=0 and j!=0:
                        sayı=0

                        if noktaMatrisi[j][i]=="0" and noktaMatrisi[j-1][i-1]!="-":

                            sayı=int(noktaMatrisi[j-1][i-1])

                            sayı+=1

                            sayı=str(sayı)

                            noktaMatrisi[j][i]=sayı

        Nokta_Matrisi(satır,sütun,noktaMatrisi)
    else:
        return

if __name__== '__main__':
    Sonuc()



#%%
