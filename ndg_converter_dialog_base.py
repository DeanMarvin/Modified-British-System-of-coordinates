# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ndg_converter_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MbsTransformDialogBase(object):
    def setupUi(self, MbsTransformDialogBase):
        MbsTransformDialogBase.setObjectName("MbsTransformDialogBase")
        MbsTransformDialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(MbsTransformDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.pushButton = QtWidgets.QPushButton(MbsTransformDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(120, 90, 171, 101))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/Modified-British-System-of-coordinates/show_marker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(45, 45))
        self.pushButton.setAutoRepeatInterval(96)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(MbsTransformDialogBase)
        self.button_box.accepted.connect(MbsTransformDialogBase.accept)
        self.button_box.rejected.connect(MbsTransformDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MbsTransformDialogBase)

    def retranslateUi(self, MbsTransformDialogBase):
        _translate = QtCore.QCoreApplication.translate
        MbsTransformDialogBase.setWindowTitle(_translate("MbsTransformDialogBase", "NDG Converter"))
