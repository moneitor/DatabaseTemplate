# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_asset_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewAsset(object):
    def setupUi(self, NewAsset):
        if not NewAsset.objectName():
            NewAsset.setObjectName(u"NewAsset")
        NewAsset.setWindowModality(Qt.NonModal)
        NewAsset.resize(334, 404)
        NewAsset.setMaximumSize(QSize(340, 410))
        self.gridLayout = QGridLayout(NewAsset)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lyt_main = QVBoxLayout()
        self.lyt_main.setObjectName(u"lyt_main")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(NewAsset)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.ln_name = QLineEdit(NewAsset)
        self.ln_name.setObjectName(u"ln_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ln_name)

        self.label_3 = QLabel(NewAsset)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.cb_project = QComboBox(NewAsset)
        self.cb_project.addItem("")
        self.cb_project.addItem("")
        self.cb_project.addItem("")
        self.cb_project.addItem("")
        self.cb_project.setObjectName(u"cb_project")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cb_project)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cb_type = QComboBox(NewAsset)
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.addItem("")
        self.cb_type.setObjectName(u"cb_type")

        self.verticalLayout_2.addWidget(self.cb_type)


        self.formLayout.setLayout(3, QFormLayout.FieldRole, self.verticalLayout_2)

        self.label = QLabel(NewAsset)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label)


        self.lyt_main.addLayout(self.formLayout)

        self.label_4 = QLabel(NewAsset)
        self.label_4.setObjectName(u"label_4")

        self.lyt_main.addWidget(self.label_4)

        self.txt_description = QTextEdit(NewAsset)
        self.txt_description.setObjectName(u"txt_description")

        self.lyt_main.addWidget(self.txt_description)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel = QPushButton(NewAsset)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_create = QPushButton(NewAsset)
        self.btn_create.setObjectName(u"btn_create")

        self.horizontalLayout.addWidget(self.btn_create)


        self.lyt_main.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.lyt_main, 0, 0, 1, 1)


        self.retranslateUi(NewAsset)

        QMetaObject.connectSlotsByName(NewAsset)
    # setupUi

    def retranslateUi(self, NewAsset):
        NewAsset.setWindowTitle(QCoreApplication.translate("NewAsset", u"New Asset", None))
        self.label_2.setText(QCoreApplication.translate("NewAsset", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("NewAsset", u"Project:", None))
        self.cb_project.setItemText(0, QCoreApplication.translate("NewAsset", u"Global", None))
        self.cb_project.setItemText(1, QCoreApplication.translate("NewAsset", u"Project1", None))
        self.cb_project.setItemText(2, QCoreApplication.translate("NewAsset", u"Project2", None))
        self.cb_project.setItemText(3, QCoreApplication.translate("NewAsset", u"Project3", None))

        self.cb_type.setItemText(0, QCoreApplication.translate("NewAsset", u"Alembic", None))
        self.cb_type.setItemText(1, QCoreApplication.translate("NewAsset", u"Obj", None))
        self.cb_type.setItemText(2, QCoreApplication.translate("NewAsset", u"FBX", None))
        self.cb_type.setItemText(3, QCoreApplication.translate("NewAsset", u"Bgeo", None))

        self.label.setText(QCoreApplication.translate("NewAsset", u"Type:", None))
        self.label_4.setText(QCoreApplication.translate("NewAsset", u"Asset description:", None))
        self.btn_cancel.setText(QCoreApplication.translate("NewAsset", u"Cancel", None))
        self.btn_create.setText(QCoreApplication.translate("NewAsset", u"Create", None))
    # retranslateUi

