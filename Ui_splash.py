# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\User\Documents\VS_Code\HorseRiding\splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Splash(object):
    def setupUi(self, Splash):
        Splash.setObjectName("Splash")
        Splash.resize(400, 450)
        Splash.setMaximumSize(QtCore.QSize(400, 450))
        self.centralwidget = QtWidgets.QWidget(Splash)
        self.centralwidget.setMaximumSize(QtCore.QSize(8000000, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadowFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadowFrame.setMaximumSize(QtCore.QSize(400, 16777215))
        self.dropShadowFrame.setStyleSheet("QFrame {    \n"
"    background-color: rgb(112, 146, 190);    \n"
"    color: rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadowFrame.setObjectName("dropShadowFrame")
        self.label_title = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QtCore.QRect(40, 230, 300, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy)
        self.label_title.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("ＭＳ Ｐゴシック")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(255, 255, 0);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_description = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QtCore.QRect(40, 290, 300, 31))
        self.label_description.setMaximumSize(QtCore.QSize(800000, 16777215))
        font = QtGui.QFont()
        font.setFamily("ＭＳ Ｐゴシック")
        font.setPointSize(14)
        self.label_description.setFont(font)
        self.label_description.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_description.setAlignment(QtCore.Qt.AlignCenter)
        self.label_description.setObjectName("label_description")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(40, 330, 300, 23))
        self.progressBar.setMaximumSize(QtCore.QSize(800000, 16777215))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QtCore.QRect(40, 360, 300, 21))
        self.label_loading.setMaximumSize(QtCore.QSize(800000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_loading.setFont(font)
        self.label_loading.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_loading.setAlignment(QtCore.Qt.AlignCenter)
        self.label_loading.setObjectName("label_loading")
        self.label_credits = QtWidgets.QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QtCore.QRect(40, 400, 300, 21))
        self.label_credits.setMaximumSize(QtCore.QSize(800000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 114, 164);")
        self.label_credits.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_credits.setObjectName("label_credits")
        self.logo_image = QtWidgets.QGraphicsView(self.dropShadowFrame)
        self.logo_image.setGeometry(QtCore.QRect(60, 30, 256, 192))
        self.logo_image.setObjectName("logo_image")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)
        QtCore.QMetaObject.connectSlotsByName(Splash)

    def retranslateUi(self, Splash):
        _translate = QtCore.QCoreApplication.translate
        Splash.setWindowTitle(_translate("Splash", "MainWindow"))
        self.label_title.setText(_translate("Splash", "<html><head/><body><p>乗馬回数</p></body></html>"))
        self.label_description.setText(_translate("Splash", "<html><head/><body><p>月もしくは週毎の乗馬回数チェックリスト</p></body></html>"))
        self.label_loading.setText(_translate("Splash", "loading..."))
        self.label_credits.setText(_translate("Splash", "<html><head/><body><p><span style=\" font-weight:600;\">Created</span>: Kouji Matsumoto</p></body></html>"))
