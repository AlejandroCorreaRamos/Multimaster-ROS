# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.float1SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.float1SpinBox.setDecimals(2)
        self.float1SpinBox.setMaximum(9999.0)
        self.float1SpinBox.setObjectName("float1SpinBox")
        self.horizontalLayout.addWidget(self.float1SpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.float2SpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.float2SpinBox.setDecimals(2)
        self.float2SpinBox.setMaximum(9999.0)
        self.float2SpinBox.setObjectName("float2SpinBox")
        self.horizontalLayout_2.addWidget(self.float2SpinBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.robotComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.robotComboBox.setObjectName("robotComboBox")
        self.robotComboBox.addItem("")
        self.robotComboBox.addItem("")
        self.robotComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.robotComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_4.addWidget(self.sendButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ROS Service Interface"))
        self.label.setText(_translate("MainWindow", "Latitud:"))
        self.label_2.setText(_translate("MainWindow", "Longitud:"))
        self.label_3.setText(_translate("MainWindow", "Robot:"))
        self.robotComboBox.setItemText(0, _translate("MainWindow", "Robot1"))
        self.robotComboBox.setItemText(1, _translate("MainWindow", "Robot2"))
        self.robotComboBox.setItemText(2, _translate("MainWindow", "Mas Cercano"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
