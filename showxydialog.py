# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QAction, QDialog, QFileDialog, QMenu, QMessageBox


from .show_xy import Ui_MbsTransformDialogBase


class ShowXYDialog(QDialog, Ui_MbsTransformDialogBase):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.close())
