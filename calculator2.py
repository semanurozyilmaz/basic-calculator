from PyQt5 import QtWidgets
import sys
from calculator import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_topla.clicked.connect(self.topla)
        self.ui.btn_cikar.clicked.connect(self.cikar)
        self.ui.btn_carp.clicked.connect(self.carp)
        self.ui.btn_bol.clicked.connect(self.bol)
        self.ui.btn_hesapla.clicked.connect(self.hesapla)
        self.ui.btn_temizle.clicked.connect(self.temizle)

    def topla(self):
        self.islem = self.sender().text()
    def cikar(self):
        self.islem = self.sender().text()
    def carp(self):
        self.islem = self.sender().text()
    def bol(self):
        self.islem = self.sender().text()

    def temizle(self):
        self.ui.line_sayi1.clear()
        self.ui.line_sayi2.clear()

    def hesapla(self):
        if self.islem == '+':
            try:
                result = int(self.ui.line_sayi1.text()) + int(self.ui.line_sayi2.text())
                self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))
            except ValueError:
                self.ui.line_sayi1.clear()
                self.ui.line_sayi2.clear()
                
        elif self.islem == '-':
            try:
                result = int(self.ui.line_sayi1.text()) - int(self.ui.line_sayi2.text())
                self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))
            except ValueError:
                self.ui.line_sayi1.clear()
                self.ui.line_sayi2.clear()

        elif self.islem == '*':
            try:
                result = int(self.ui.line_sayi1.text()) * int(self.ui.line_sayi2.text())
                self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))
            except ValueError:
                self.ui.line_sayi1.clear()
                self.ui.line_sayi2.clear()

        elif self.islem == '/':
            try:
                result = int(self.ui.line_sayi1.text()) / int(self.ui.line_sayi2.text())
                self.ui.lbl_sonuc.setText('Sonuç: '+ str(result))
            except ValueError:
                self.ui.line_sayi1.clear()
                self.ui.line_sayi2.clear()
        

def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: red}")
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()