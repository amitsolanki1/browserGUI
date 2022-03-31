# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'brower.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import webbrowser as wb
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 449)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(520, 180, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.search.setFont(font)
        self.search.setStyleSheet("color:white;\n"
"border:1px solid white;\n"
"\n"
"border-radius:10%;\n"
"")
        self.search.setObjectName("search")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 180, 381, 51))
        self.lineEdit.setStyleSheet("color:black;background-color:white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 30, 521, 121))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("browser-pyqt\\google.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gmail = QtWidgets.QPushButton(self.centralwidget)
        self.gmail.setGeometry(QtCore.QRect(400, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.gmail.setFont(font)
        self.gmail.setStyleSheet("color:white;\n"
"background-color: rgb(125, 255, 3);\n"
"border-radius:10%;")
        self.gmail.setObjectName("gmail")
        self.facebook = QtWidgets.QPushButton(self.centralwidget)
        self.facebook.setGeometry(QtCore.QRect(230, 290, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.facebook.setFont(font)
        self.facebook.setStyleSheet("color:white;\n"
"background-color: rgb(16, 88, 255);\n"
"border-radius:10%;")
        self.facebook.setObjectName("facebook")
        self.instagram = QtWidgets.QPushButton(self.centralwidget)
        self.instagram.setGeometry(QtCore.QRect(230, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.instagram.setFont(font)
        self.instagram.setStyleSheet("color:white;\n"
"background-color: rgb(255, 17, 120);\n"
"border-radius:10%;")
        self.instagram.setObjectName("instagram")
        self.youtube = QtWidgets.QPushButton(self.centralwidget)
        self.youtube.setGeometry(QtCore.QRect(400, 350, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.youtube.setFont(font)
        self.youtube.setStyleSheet("color:white;\n"
"background-color: red;\n"
"border-radius:10%;")
        self.youtube.setObjectName("youtube")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.search.clicked.connect(self.searchtext)
        self.instagram.clicked.connect(self.searinstagram)
        self.facebook.clicked.connect(self.searfacebook)
        self.gmail.clicked.connect(self.seargmail)
        self.youtube.clicked.connect(self.searyoutube)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def searchtext(self):
            text=self.lineEdit.text()
            if text=="":
                    pass
            else:
                    wb.open("https://www.googel.com/search?q="+text)

    def searinstagram(self):
            wb.open("https://www.instagram.com")

    def searfacebook(self):
            wb.open("https://www.facebook.com")

    def seargmail(self):
            wb.open("https://www.gmail.com")

    def searyoutube(self):
            
            wb.open("https://www.youtube.com")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QT Browser"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.gmail.setText(_translate("MainWindow", "Gmail"))
        self.facebook.setText(_translate("MainWindow", "Facebook"))
        self.instagram.setText(_translate("MainWindow", "instagram"))
        self.youtube.setText(_translate("MainWindow", "Youtube"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

