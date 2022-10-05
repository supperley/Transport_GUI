# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_pop_upjqvhpK.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 210)
        Form.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 48))
        self.frame.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_header = QLabel(self.frame)
        self.label_header.setObjectName(u"label_header")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_header.setFont(font1)
        self.label_header.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.label_header)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton_postpone = QPushButton(self.frame)
        self.pushButton_postpone.setObjectName(u"pushButton_postpone")
        self.pushButton_postpone.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"icons/alarm-clock-blue_24_24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_postpone.setIcon(icon)
        self.pushButton_postpone.setIconSize(QSize(16, 16))
        self.pushButton_postpone.setAutoDefault(False)
        self.pushButton_postpone.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_postpone)

        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_close.sizePolicy().hasHeightForWidth())
        self.pushButton_close.setSizePolicy(sizePolicy1)
        self.pushButton_close.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u"icons/prohibition.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QSize(16, 16))
        self.pushButton_close.setFlat(True)

        self.horizontalLayout_2.addWidget(self.pushButton_close)


        self.verticalLayout.addWidget(self.frame)

        self.frame1 = QFrame(Form)
        self.frame1.setObjectName(u"frame1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame1.sizePolicy().hasHeightForWidth())
        self.frame1.setSizePolicy(sizePolicy2)
        self.horizontalLayout = QHBoxLayout(self.frame1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_depature = QLabel(self.frame1)
        self.label_depature.setObjectName(u"label_depature")

        self.horizontalLayout.addWidget(self.label_depature)

        self.timeEdit = QTimeEdit(self.frame1)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setEnabled(True)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timeEdit.setKeyboardTracking(False)

        self.horizontalLayout.addWidget(self.timeEdit)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.laberl_arrive = QLabel(self.frame1)
        self.laberl_arrive.setObjectName(u"laberl_arrive")

        self.horizontalLayout.addWidget(self.laberl_arrive)

        self.timeEdit_2 = QTimeEdit(self.frame1)
        self.timeEdit_2.setObjectName(u"timeEdit_2")
        self.timeEdit_2.setEnabled(True)
        self.timeEdit_2.setFrame(True)
        self.timeEdit_2.setReadOnly(True)
        self.timeEdit_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.timeEdit_2.setKeyboardTracking(False)
        self.timeEdit_2.setProperty("showGroupSeparator", False)

        self.horizontalLayout.addWidget(self.timeEdit_2)

        self.label_duration = QLabel(self.frame1)
        self.label_duration.setObjectName(u"label_duration")

        self.horizontalLayout.addWidget(self.label_duration)

        self.line_duration = QLineEdit(self.frame1)
        self.line_duration.setObjectName(u"line_duration")
        self.line_duration.setMaximumSize(QSize(105, 16777215))
        self.line_duration.setReadOnly(True)

        self.horizontalLayout.addWidget(self.line_duration)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_add = QPushButton(self.frame1)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy1.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"icons/arrow-curve.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setIconSize(QSize(24, 24))
        self.pushButton_add.setFlat(True)

        self.horizontalLayout.addWidget(self.pushButton_add)


        self.verticalLayout.addWidget(self.frame1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tickets_text = QTextEdit(self.frame_2)
        self.tickets_text.setObjectName(u"tickets_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tickets_text.sizePolicy().hasHeightForWidth())
        self.tickets_text.setSizePolicy(sizePolicy3)
        self.tickets_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.tickets_text)


        self.verticalLayout.addWidget(self.frame_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_header.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_postpone.setText(QCoreApplication.translate("Form", u"Postpone", None))
        self.pushButton_close.setText(QCoreApplication.translate("Form", u"To Favorites", None))
        self.label_depature.setText(QCoreApplication.translate("Form", u"Departure", None))
        self.laberl_arrive.setText(QCoreApplication.translate("Form", u"Arrive", None))
        self.label_duration.setText(QCoreApplication.translate("Form", u"Duration", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"None", None))
    # retranslateUi

