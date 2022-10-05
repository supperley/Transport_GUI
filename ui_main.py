# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainluCgVL.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(890, 430)
        MainWindow.setMinimumSize(QSize(890, 430))
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#frame_top_menus .QPushButton {\n"
"	border: 0px solid;\n"
"	text-align: left;\n"
"	padding: 0px 25px 0px 25px;\n"
"	font: 600 11pt \"Mulish SemiBold\";\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_toggle .QPushButton {	\n"
"	border: 0px solid;\n"
"	text-align: left;\n"
"	padding: 0px 25px 0px 23px;\n"
"	font: 600 11pt \"Mulish SemiBold\";\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_top .QPushButton {	\n"
"	border: 0px solid;\n"
"	border-left: 0px solid transparent;\n"
"	text-align: left;\n"
"	icon-size: 25px;\n"
"}\n"
"#frame_top_menus .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#frame_top_menus .QPushButton:pressed {	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"QListWidget */\n"
"QListWidget {\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0, 133, 255);\n"
"	font-size: 18pt\n"
"}\n"
"QListWidget::item {\n"
"   "
                        "height: 40px;\n"
"}\n"
"QListWidget  QScrollBar:vertical {\n"
"    width: 20px;\n"
" }\n"
"QListWidget  QScrollBar:horizontal {\n"
"    height: 20px;\n"
" }\n"
"QListWidget:hover {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"QListWidget:focus {\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: #e2e2e2;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(40, 44, 52);\n"
"    color: #323232;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"TimeEdit */\n"
"QTimeEdit {\n"
"	background-color: #e2e2e2;\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding-left: 10px;\n"
"	selection-color: rgb"
                        "(255, 255, 255);\n"
"	selection-background-color: rgb(0, 133, 255);\n"
"    color: #323232;\n"
"}\n"
"QTimeEdit:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QTimeEdit:focus {\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QDateEdit{\n"
"	border-radius: 5px;\n"
"	border: 2px solid #939393;\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QDateEdit:hover{\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"QDateEdit::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: #939393;\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"/* /////////////////////////////////////////////////////////////////\n"
"QCalendarW"
                        "idget */\n"
"QCalendarWidget QToolButton{\n"
"color: #000;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#frame_pages QPushButton {\n"
"	border: 2px solid #939393;\n"
"	border-radius: 5px;	\n"
"	background-color: #e2e2e2;\n"
"    color: #000;\n"
"}\n"
"#frame_pages QPushButton:hover {\n"
"	border: 2px solid rgb(40, 44, 52);\n"
"}\n"
"#frame_pages QPushButton:pressed {	\n"
"	border: 2px solid rgb(0, 133, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMinimumSize(QSize(0, 40))
        self.Top_Bar.setMaximumSize(QSize(16777215, 60))
        self.Top_Bar.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 60))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(0, 133, 255);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"images/icons/icon_menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_date = QLabel(self.frame_top)
        self.label_date.setObjectName(u"label_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy1)
        self.label_date.setMinimumSize(QSize(600, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.label_date.setFont(font)
        self.label_date.setStyleSheet(u"font: 500 12pt \"Mulish\";")

        self.horizontalLayout_6.addWidget(self.label_date)

        self.label_acc_name = QLabel(self.frame_top)
        self.label_acc_name.setObjectName(u"label_acc_name")
        self.label_acc_name.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_acc_name.setFont(font1)
        self.label_acc_name.setStyleSheet(u"font: 600 12pt \"Mulish SemiBold\";")
        self.label_acc_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_acc_name)

        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMaximumSize(QSize(60, 16777215))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.frame)
        self.btn_settings.setObjectName(u"btn_settings")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.btn_settings)

        self.btn_notifications = QPushButton(self.frame)
        self.btn_notifications.setObjectName(u"btn_notifications")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_notifications.sizePolicy().hasHeightForWidth())
        self.btn_notifications.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u"images/icons/icon_notifications.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_notifications.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.btn_notifications)


        self.horizontalLayout_6.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(0, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName(u"frame_top_menus")
        self.frame_top_menus.setStyleSheet(u"")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName(u"btn_page_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_page_1.sizePolicy().hasHeightForWidth())
        self.btn_page_1.setSizePolicy(sizePolicy4)
        self.btn_page_1.setMinimumSize(QSize(0, 50))
        self.btn_page_1.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/icon_home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_1.setIcon(icon3)
        self.btn_page_1.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.btn_page_1)

        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName(u"btn_page_2")
        self.btn_page_2.setMinimumSize(QSize(0, 50))
        self.btn_page_2.setStyleSheet(u"background-color: rgb(157, 157, 157);")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/icon_bus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_2.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_page_2)

        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName(u"btn_page_3")
        self.btn_page_3.setMinimumSize(QSize(0, 50))
        self.btn_page_3.setStyleSheet(u"background-color: rgb(144, 144, 144);")
        icon5 = QIcon()
        icon5.addFile(u"images/icons/icon_train.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_3.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.btn_page_3)

        self.btn_page_4 = QPushButton(self.frame_top_menus)
        self.btn_page_4.setObjectName(u"btn_page_4")
        self.btn_page_4.setMinimumSize(QSize(0, 50))
        self.btn_page_4.setStyleSheet(u"background-color: rgb(120, 120, 120);")
        icon6 = QIcon()
        icon6.addFile(u"images/icons/icon_search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_page_4.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.btn_page_4)


        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setEnabled(True)
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_1 = QLabel(self.page_1)
        self.label_1.setObjectName(u"label_1")
        font2 = QFont()
        font2.setPointSize(20)
        self.label_1.setFont(font2)
        self.label_1.setStyleSheet(u"color: #000")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_1)

        self.Pages_Widget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.list_transport = QListWidget(self.page_2)
        self.list_transport.setObjectName(u"list_transport")

        self.verticalLayout_7.addWidget(self.list_transport)

        self.btn_get_transport = QPushButton(self.page_2)
        self.btn_get_transport.setObjectName(u"btn_get_transport")

        self.verticalLayout_7.addWidget(self.btn_get_transport)

        self.textEdit = QTextEdit(self.page_2)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout_7.addWidget(self.textEdit)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: #000")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.Pages_Widget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_11 = QVBoxLayout(self.page_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 0))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy5)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_departure = QLineEdit(self.frame_3)
        self.line_departure.setObjectName(u"line_departure")
        self.line_departure.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.line_departure)

        self.line_arrival = QLineEdit(self.frame_3)
        self.line_arrival.setObjectName(u"line_arrival")
        self.line_arrival.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_4.addWidget(self.line_arrival)

        self.dateEdit = QDateEdit(self.frame_3)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(110, 0))
        self.dateEdit.setStyleSheet(u"")
        self.dateEdit.setDateTime(QDateTime(QDate(2021, 10, 1), QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate(2021, 10, 1))

        self.horizontalLayout_4.addWidget(self.dateEdit)

        self.btn_search = QPushButton(self.frame_3)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_4.addWidget(self.btn_search)


        self.verticalLayout_8.addWidget(self.frame_3)


        self.verticalLayout_11.addWidget(self.widget)

        self.list_railway = QListWidget(self.page_3)
        self.list_railway.setObjectName(u"list_railway")

        self.verticalLayout_11.addWidget(self.list_railway)

        self.Pages_Widget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_5 = QHBoxLayout(self.page_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.list_postpone = QListWidget(self.page_4)
        self.list_postpone.setObjectName(u"list_postpone")

        self.horizontalLayout_5.addWidget(self.list_postpone)

        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_update = QPushButton(self.frame_4)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.btn_update)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.edit_log = QTextEdit(self.frame_2)
        self.edit_log.setObjectName(u"edit_log")
        self.edit_log.setMinimumSize(QSize(0, 0))
        self.edit_log.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.edit_log)


        self.horizontalLayout_5.addWidget(self.frame_2)

        self.Pages_Widget.addWidget(self.page_4)

        self.verticalLayout_5.addWidget(self.Pages_Widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_acc_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_settings.setText("")
        self.btn_notifications.setText("")
        self.btn_page_1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page_2.setText(QCoreApplication.translate("MainWindow", u"City Transport", None))
        self.btn_page_3.setText(QCoreApplication.translate("MainWindow", u"Railway", None))
        self.btn_page_4.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Transport Finder!", None))
        self.btn_get_transport.setText(QCoreApplication.translate("MainWindow", u"transport_info", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.line_departure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Departure", None))
        self.line_arrival.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Arrival", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
    # retranslateUi

