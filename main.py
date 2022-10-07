import sys
from  PIL import Image
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QPushButton, QApplication, QSizePolicy, QWidget, QMainWindow, QWidgetItem, QFileDialog, \
    QLabel, QDialog, \
    QInputDialog, QMessageBox, QLineEdit
from PyQt5 import uic, QtCore


class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('test1.ui', self)

        self.open_reg()
        self.check_btn.clicked.connect(self.onClick)
        self.add_btn.clicked.connect(self.open_add)
            #pass


    def open_auth(self):
        self.auth_win = QDialog(self)
        uic.loadUi('reg.ui', self.auth_win)
        self.auth_win.show()

    def open_reg(self):
        self.reg_win = QDialog(self)
        uic.loadUi('reg.ui', self.reg_win)
        self.reg_win.show()

        #self.auth_win.show()

    def onClick(self):
        self.ok = QMessageBox(self)
        self.ok.setStandardButtons(QMessageBox.Ok)
        self.ok.setText("Оплатите заказ при получении")
        self.ok.setWindowTitle("Заказ оформлен")
        self.ok.show()
    def open_add(self):
        uic.loadUi('admin.ui', self)
        self.return_btn.clicked.connect(lambda x: uic.loadUi('test1.ui', self))



if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    app.exec_()


