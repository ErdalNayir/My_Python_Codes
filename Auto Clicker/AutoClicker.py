import os
from PyQt5.QtCore import* # QApplication oluşturmak için
import sys # sayfanın oluşması ve kapatılması için
from PyQt5 import*
from PyQt5.QtWidgets import*  # tableWidgetin kullanılması için
from PyQt5.QtGui import*
import time
import threading
from pynput.mouse import Button, Controller
import keyboard
import signal

exit_event=threading.Event()

def signal_handler(signum,frame):
    exit_event.set()

signal.signal(signal.SIGINT,signal_handler)



#delay = 1
#button = Button.left
# threading.Thread is used
# to control clicks
class ClickerMouse(threading.Thread):
  # delay and button is passed in class
  # to check execution of auto-clicker
    def __init__(self, delay, button,times=0):
        super().__init__()

        self.delay = delay
        self.button = button
        self.times=times
        self.running = False
        self.program_running = True


    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def start_stop_clicking(self):

        if self.running == False:
            self.start_clicking()
        else:
            self.stop_clicking()
    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    # for mouse click it set to button
    # and delay.
    def run(self):
        if self.delay<=0:
            while self.program_running:
                while self.running:
                    if self.times>0:
                        for i in range(self.times):
                            mouse.click(self.button)
                            time.sleep(self.delay)
                        self.stop_clicking()
                    else:
                        mouse.click(self.button)
                        time.sleep(self.delay)
                    time.sleep(0.1)
                time.sleep(0.1)
        else:
            return 0

# instance of mouse controller is created
mouse = Controller()

#click_thread = ClickerMouse(1,Button.left,0)
#click_thread.start()

#keyboard.add_hotkey('ctrl + s',click_thread.start_stop_clicking)
#keyboard.add_hotkey('ctrl + q',click_thread.exit)




class UserInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.width = 431
        self.height = 201
        self.qtRectangle = self.frameGeometry()
        self.centerPoint=QDesktopWidget().availableGeometry().center()
        self.msg= QMessageBox()
        self.isRunning=False


        self.initUI()

    def initUI(self):

        self.setWindowTitle("Auto Clicker")
        self.setFixedSize(self.width,self.height)

        self.qtRectangle.moveCenter(self.centerPoint)
        self.move(self.qtRectangle.topLeft())

        self.setWindowIcon(QIcon(r"C:\Users\erdal\OneDrive\Masaüstü\Auto Clicker\mouse.png"))


        self.Start = QPushButton('Başla (Ctrl+S)',self)
        self.Start.setFixedSize(201,51)
        self.Start.move(10,130)
        self.Start.clicked.connect(self.start_clicking)

        self.Stop = QPushButton('Durdur (Ctrl+Q)',self)
        self.Stop.setFixedSize(201,51)
        self.Stop.move(220,130)
        self.Stop.clicked.connect(self.stop_clicking)



        self.groupbox_1 = QGroupBox("Tıklama Aralığı",self)
        self.groupbox_1.setFixedSize(201,101)
        self.groupbox_1.move(10,10)

        self.Saniye = QLineEdit(self)
        self.Saniye.setFixedSize(91,31)
        self.Saniye.move(20,40)

        self.adet= QLabel(self)
        self.adet.setText("saniye")
        self.adet.setFixedSize(55,16)
        self.adet.move(120,50)



        self.groupbox_2 = QGroupBox("Tıklama Sayısı",self)
        self.groupbox_2.setFixedSize(201,101)
        self.groupbox_2.move(220,10)

        self.spinbox = QSpinBox(self)
        self.spinbox.setFixedSize(81,31)
        self.spinbox.move(230,40)

        self.tekrar= QLabel(self)
        self.tekrar.setText("kere")
        self.tekrar.setFixedSize(55,16)
        self.tekrar.move(320,50)



        self.Suresiz =QRadioButton("Durdurulana kadar devam et",self)
        self.Suresiz.clicked.connect(self.disable)
        self.Suresiz.move(230,80)

        self.show()

    def disable(self):
        self.spinbox.setDisabled(True)


    def start_clicking(self):
        if self.isRunning==False:
            self.isRunning=True

            self.spinbox.setEnabled(True)

            try:
                self

                sny=self.Saniye.text()
                saniye=float(sny)
            except ValueError:
                self.msg.setWindowTitle("Hata")
                self.msg.setText("Lütfen bir değer girin")
                self.msg.setIcon(QMessageBox.Critical)

                x = self.msg.exec_()

                return -1

            time= self.spinbox.value()
            time=int(time)

            if self.Suresiz.isChecked() :

                self.spinbox.setDisabled(True)
                self.click_thread = ClickerMouse(saniye, Button.left)
                self.click_thread.start()

                keyboard.add_hotkey('ctrl + q',self.click_thread.exit)
                keyboard.add_hotkey('ctrl + s',self.start_clicking)

                self.click_thread.start_clicking()

            elif time>0:
                self.click_thread = ClickerMouse(saniye, Button.left,time)
                self.click_thread.start()

                keyboard.add_hotkey('ctrl + q',self.click_thread.exit)
                keyboard.add_hotkey('ctrl + s',self.start_clicking)

                self.click_thread.start_clicking()
        else:
            return 0



    def stop_clicking(self):

        self.spinbox.setEnabled(True)











def main():
    app = QApplication(sys.argv)
    ui = UserInterface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
