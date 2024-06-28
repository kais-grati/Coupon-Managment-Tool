# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ressource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 720)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#header{\n"
"	background-color: rgb(236, 236, 236);\n"
"}\n"
"#sub_header{\n"
"	background-color: rgb(236, 236, 236);\n"
"	border: 2px solid rgb(0, 170, 0);\n"
"	margin: 30px;\n"
"	border-radius:10px;\n"
"}\n"
"#footer{\n"
"	background-color: rgb(236, 236, 236);\n"
"	border: 2px solid rgb(0, 170, 0);\n"
"	margin: 30px;\n"
"	border-radius:10px;\n"
"}\n"
"#body{\n"
"	background-color: rgb(236, 236, 236);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(18)
        self.header.setFont(font)
        self.header.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.import_2 = QPushButton(self.header)
        self.import_2.setObjectName(u"import_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.import_2.sizePolicy().hasHeightForWidth())
        self.import_2.setSizePolicy(sizePolicy1)
        self.import_2.setMinimumSize(QSize(300, 50))
        font1 = QFont()
        font1.setFamilies([u"Poppins"])
        font1.setPointSize(18)
        self.import_2.setFont(font1)
        self.import_2.setAutoFillBackground(False)
        self.import_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.import_2.setFlat(True)

        self.horizontalLayout.addWidget(self.import_2)

        self.export_2 = QPushButton(self.header)
        self.export_2.setObjectName(u"export_2")
        sizePolicy1.setHeightForWidth(self.export_2.sizePolicy().hasHeightForWidth())
        self.export_2.setSizePolicy(sizePolicy1)
        self.export_2.setMinimumSize(QSize(270, 50))
        self.export_2.setFont(font1)
        self.export_2.setAutoFillBackground(False)
        self.export_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px")
        self.export_2.setFlat(True)

        self.horizontalLayout.addWidget(self.export_2)

        self.remaining = QLabel(self.header)
        self.remaining.setObjectName(u"remaining")
        sizePolicy1.setHeightForWidth(self.remaining.sizePolicy().hasHeightForWidth())
        self.remaining.setSizePolicy(sizePolicy1)
        self.remaining.setMinimumSize(QSize(250, 60))
        self.remaining.setFont(font1)
        self.remaining.setAutoFillBackground(False)
        self.remaining.setStyleSheet(u"background-color: rgb(255, 170, 0);\n"
"border-radius:10px")
        self.remaining.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.remaining)


        self.verticalLayout.addWidget(self.header)

        self.sub_header = QWidget(self.centralwidget)
        self.sub_header.setObjectName(u"sub_header")
        sizePolicy.setHeightForWidth(self.sub_header.sizePolicy().hasHeightForWidth())
        self.sub_header.setSizePolicy(sizePolicy)
        self.sub_header.setMinimumSize(QSize(0, 200))
        self.sub_header.setMaximumSize(QSize(16777215, 220))
        self.sub_header.setAutoFillBackground(False)
        self.horizontalLayout_2 = QHBoxLayout(self.sub_header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 30, 30, 30)
        self.create_section = QWidget(self.sub_header)
        self.create_section.setObjectName(u"create_section")
        self.gridLayout = QGridLayout(self.create_section)
        self.gridLayout.setObjectName(u"gridLayout")
        self.coupon_section = QWidget(self.create_section)
        self.coupon_section.setObjectName(u"coupon_section")
        self.verticalLayout_2 = QVBoxLayout(self.coupon_section)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.coupon_label = QLabel(self.coupon_section)
        self.coupon_label.setObjectName(u"coupon_label")
        font2 = QFont()
        font2.setPointSize(15)
        self.coupon_label.setFont(font2)
        self.coupon_label.setStyleSheet(u"color:rgb(100, 100, 100)")
        self.coupon_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.coupon_label)

        self.coupon_input = QLineEdit(self.coupon_section)
        self.coupon_input.setObjectName(u"coupon_input")
        font3 = QFont()
        font3.setPointSize(13)
        self.coupon_input.setFont(font3)
        self.coupon_input.setStyleSheet(u"border:none;\n"
"border-radius:10px;")

        self.verticalLayout_2.addWidget(self.coupon_input)


        self.gridLayout.addWidget(self.coupon_section, 2, 0, 1, 1)

        self.coupon_section_2 = QWidget(self.create_section)
        self.coupon_section_2.setObjectName(u"coupon_section_2")
        self.verticalLayout_3 = QVBoxLayout(self.coupon_section_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.coupon_label_2 = QLabel(self.coupon_section_2)
        self.coupon_label_2.setObjectName(u"coupon_label_2")
        self.coupon_label_2.setFont(font2)
        self.coupon_label_2.setStyleSheet(u"color:rgb(100, 100, 100)")
        self.coupon_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.coupon_label_2)

        self.coupon_input_2 = QLineEdit(self.coupon_section_2)
        self.coupon_input_2.setObjectName(u"coupon_input_2")
        self.coupon_input_2.setFont(font3)
        self.coupon_input_2.setStyleSheet(u"border:none;\n"
"border-radius:10px;")

        self.verticalLayout_3.addWidget(self.coupon_input_2)


        self.gridLayout.addWidget(self.coupon_section_2, 0, 0, 2, 1)

        self.create_coupon = QPushButton(self.create_section)
        self.create_coupon.setObjectName(u"create_coupon")
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        self.create_coupon.setFont(font4)
        self.create_coupon.setStyleSheet(u"QPushButton {background-color: rgb(0, 170, 0);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"padding:10px}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(138, 226, 52);\n"
"}")
        self.create_coupon.setIconSize(QSize(40, 40))
        self.create_coupon.setFlat(True)

        self.gridLayout.addWidget(self.create_coupon, 0, 2, 1, 1)

        self.start_section = QWidget(self.create_section)
        self.start_section.setObjectName(u"start_section")
        self.start_section.setMinimumSize(QSize(200, 0))
        self.verticalLayout_5 = QVBoxLayout(self.start_section)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.start_label = QLabel(self.start_section)
        self.start_label.setObjectName(u"start_label")
        self.start_label.setFont(font2)
        self.start_label.setStyleSheet(u"color:rgb(100, 100, 100)")
        self.start_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.start_label)

        self.start = QDateTimeEdit(self.start_section)
        self.start.setObjectName(u"start")
        sizePolicy1.setHeightForWidth(self.start.sizePolicy().hasHeightForWidth())
        self.start.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setBold(True)
        font5.setItalic(False)
        self.start.setFont(font5)
        self.start.setStyleSheet(u"QDateTimeEdit {\n"
"    border: 2px solid #999999;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"	font-size:15px;\n"
"	font-weight:bold\n"
"}\n"
"\n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px;\n"
"	border:none\n"
"}\n"
"\n"
"QDateTimeEdit::down-arrow {\n"
"    image: url(:/ressource/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: auto;\n"
"}\n"
"QDateTimeEdit::up-arrow {\n"
"    image: url(:/ressource/icons/chevron-up.svg);\n"
"}")
        self.start.setDate(QDate(2023, 9, 14))
        self.start.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.start.setCurrentSection(QDateTimeEdit.DaySection)
        self.start.setCalendarPopup(True)

        self.verticalLayout_5.addWidget(self.start)


        self.gridLayout.addWidget(self.start_section, 0, 1, 3, 1)

        self.end_section = QWidget(self.create_section)
        self.end_section.setObjectName(u"end_section")
        self.verticalLayout_4 = QVBoxLayout(self.end_section)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.end_label_2 = QLabel(self.end_section)
        self.end_label_2.setObjectName(u"end_label_2")
        self.end_label_2.setFont(font2)
        self.end_label_2.setStyleSheet(u"color:rgb(100, 100, 100)")
        self.end_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.end_label_2)

        self.end = QDateTimeEdit(self.end_section)
        self.end.setObjectName(u"end")
        sizePolicy1.setHeightForWidth(self.end.sizePolicy().hasHeightForWidth())
        self.end.setSizePolicy(sizePolicy1)
        self.end.setFont(font5)
        self.end.setStyleSheet(u"QDateTimeEdit {\n"
"    border: 2px solid #999999;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    background-color: #FFFFFF;\n"
"    color: #333333;\n"
"	font-size:15px;\n"
"	font-weight:bold\n"
"}\n"
"\n"
"QDateTimeEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right center;\n"
"    width: 20px;\n"
"	border:none\n"
"}\n"
"\n"
"QDateTimeEdit::down-arrow {\n"
"    image: url(:/ressource/icons/chevron-down.svg);\n"
"	width: 20px;\n"
"	height: auto;\n"
"}\n"
"QDateTimeEdit::up-arrow {\n"
"    image: url(:/ressource/icons/chevron-up.svg);\n"
"}")
        self.end.setDate(QDate(2023, 9, 14))
        self.end.setMinimumDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.end.setCurrentSection(QDateTimeEdit.DaySection)
        self.end.setCalendarPopup(True)

        self.verticalLayout_4.addWidget(self.end)


        self.gridLayout.addWidget(self.end_section, 1, 2, 2, 1)


        self.horizontalLayout_2.addWidget(self.create_section)


        self.verticalLayout.addWidget(self.sub_header)

        self.body = QWidget(self.centralwidget)
        self.body.setObjectName(u"body")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy2)
        self.body.setMinimumSize(QSize(0, 200))
        font6 = QFont()
        font6.setKerning(False)
        self.body.setFont(font6)
        self.body.setAutoFillBackground(False)
        self.horizontalLayout_5 = QHBoxLayout(self.body)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableWidget = QTableWidget(self.body)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.widget = QWidget(self.body)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/ressource/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/ressource/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.widget)


        self.verticalLayout.addWidget(self.body)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.test_coupon_wrapper = QWidget(self.footer)
        self.test_coupon_wrapper.setObjectName(u"test_coupon_wrapper")
        self.test_coupon_wrapper.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_4 = QHBoxLayout(self.test_coupon_wrapper)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.test_coupon_input = QLineEdit(self.test_coupon_wrapper)
        self.test_coupon_input.setObjectName(u"test_coupon_input")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.test_coupon_input.setFont(font7)

        self.horizontalLayout_4.addWidget(self.test_coupon_input)

        self.test_coupon_button = QPushButton(self.test_coupon_wrapper)
        self.test_coupon_button.setObjectName(u"test_coupon_button")
        self.test_coupon_button.setFont(font4)
        self.test_coupon_button.setStyleSheet(u"QPushButton {background-color: rgb(0, 170, 0);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);\n"
"padding:10px}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(138, 226, 52);\n"
"}")

        self.horizontalLayout_4.addWidget(self.test_coupon_button)

        self.test_coupon_label = QLabel(self.test_coupon_wrapper)
        self.test_coupon_label.setObjectName(u"test_coupon_label")
        self.test_coupon_label.setMinimumSize(QSize(150, 0))
        self.test_coupon_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.test_coupon_label)


        self.horizontalLayout_3.addWidget(self.test_coupon_wrapper)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.create_coupon.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.import_2.setText(QCoreApplication.translate("MainWindow", u"Import CSV", None))
        self.export_2.setText(QCoreApplication.translate("MainWindow", u"Export CSV", None))
        self.remaining.setText(QCoreApplication.translate("MainWindow", u"18/20 remaining", None))
        self.coupon_label.setText(QCoreApplication.translate("MainWindow", u"Coupon", None))
        self.coupon_label_2.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.coupon_input_2.setText("")
        self.create_coupon.setText(QCoreApplication.translate("MainWindow", u"Create Coupon", None))
        self.start_label.setText(QCoreApplication.translate("MainWindow", u"Start time", None))
        self.start.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy h:mm AP", None))
        self.end_label_2.setText(QCoreApplication.translate("MainWindow", u"End time", None))
        self.end.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy h:mm AP", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.test_coupon_button.setText(QCoreApplication.translate("MainWindow", u"Test coupon", None))
        self.test_coupon_label.setText("")
    # retranslateUi

