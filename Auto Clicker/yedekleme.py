def start_clicking(self):

    if self.isRunning==False:
        self.isRunning=True

        self.spinbox.setEnabled(True)

        sny=self.Saniye.text()
        saniye=float(sny)

        time= self.spinbox.value()
        time=int(time)

        if self.Suresiz.isChecked() :

            self.spinbox.setDisabled(True)
            click_thread = ClickerMouse(saniye, Button.left)
            click_thread.start()

            keyboard.add_hotkey('ctrl + q',click_thread.exit)
            keyboard.add_hotkey('ctrl + s',self.start_clicking)

            click_thread.start_clicking()

        elif time>0:
            click_thread = ClickerMouse(saniye, Button.left,time)
            click_thread.start()

            keyboard.add_hotkey('ctrl + q',click_thread.exit)
            keyboard.add_hotkey('ctrl + s',self.start_clicking)

            click_thread.start_clicking()
    else:
        return 0


def stop_clicking(self):
    if self.isRunning==True:















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
