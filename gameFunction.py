from PyQt5 import QtCore, QtGui, QtWidgets
from itertools import count

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
import ui_game_form

class gameSet(QtWidgets.QMainWindow,ui_game_form.Ui_GameWindow):

    #Обработка событий
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widgetGameMedium.hide()
        self.SettingsW_2.hide()


        #Тут кнопка рестарт
        self.Restart_Med.clicked.connect(lambda:self.restart())

        #Тут фон
        self.Settings_Fon_1.clicked.connect(lambda: self.firstGameZone())
        self.Settings_Fon_1.clicked.connect(lambda: self.Game())
        self.Settings_Fon_2.clicked.connect(lambda: self.secondGameZone())
        self.Settings_Fon_2.clicked.connect(lambda: self.Game())
        self.Settings_Fon_3.clicked.connect(lambda: self.thirdGameZone())
        self.Settings_Fon_3.clicked.connect(lambda: self.Game())

        #Тут счетчик он не работает
        self.A1_3.clicked.connect(lambda: self.Chort)
        self.B1_3.clicked.connect(lambda: self.Chort)
        self.B2_3.clicked.connect(lambda: self.Chort)
        self.B3_3.clicked.connect(lambda: self.Chort)
        self.C1_3.clicked.connect(lambda: self.Chort)
        self.C2_3.clicked.connect(lambda: self.Chort)
        self.C3_3.clicked.connect(lambda: self.Chort)
        self.C4_3.clicked.connect(lambda: self.Chort)
        self.C5_3.clicked.connect(lambda: self.Chort)
        self.D1_3.clicked.connect(lambda: self.Chort)
        self.D2_3.clicked.connect(lambda: self.Chort)
        self.D3_3.clicked.connect(lambda: self.Chort)
        self.D4_3.clicked.connect(lambda: self.Chort)
        self.D5_3.clicked.connect(lambda: self.Chort)
        self.D6_3.clicked.connect(lambda: self.Chort)
        self.D7_3.clicked.connect(lambda: self.Chort)

    def Chort(self, i= 0):
        if i == 0:
            i += 1
            a = "Игрок 2"
        else:
            i += -1
            a = "Игрок 1"
        self.ui.label_2.setText(a)


    #Тут возвращаю кнопки
    def restart(self):
        self.A1_3.show()
        self.B1_3.show()
        self.B2_3.show()
        self.B3_3.show()
        self.C2_3.show()
        self.C3_3.show()
        self.C4_3.show()
        self.C5_3.show()
        self.D1_3.show()
        self.D2_3.show()
        self.D3_3.show()
        self.D4_3.show()
        self.D5_3.show()
        self.D6_3.show()
        self.D7_3.show()
        self.C1_3.show()

    # Тут игровые поля
    def firstGameZone(self):
            self.pole = 1

    def secondGameZone(self):
            self.pole = 2

    def thirdGameZone(self):
            self.pole = 3

    # Тут Фон игры
    def Game(self):
        if self.pole == 1:
            self.label_4.show()
            self.label_5.hide()
            self.label_6.hide()
        if self.pole == 2:
            self.label_4.hide()
            self.label_5.show()
            self.label_6.hide()
        if self.pole == 3:
            self.label_4.hide()
            self.label_5.hide()
            self.label_6.show()


