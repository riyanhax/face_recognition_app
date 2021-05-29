# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_추가 (1) (1)EsAFOU.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1210, 809)
        MainWindow.setMinimumSize(QSize(940, 560))
        MainWindow.setStyleSheet(u"")
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setEnabled(True)
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFont(font)
        self.topLogoInfo.setStyleSheet(u"background-color: rgb(124, 135, 166);")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Plain)
        self.topLogoInfo.setLineWidth(0)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))
        self.leftMenuFrame.setStyleSheet(u"background-color: rgb(87, 101, 146);")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMinimumSize(QSize(0, 0))
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.toggleButton.setFont(font1)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(images/icons/icon_menu.png);\n"
"background-color: rgb(4, 10, 50);\n"
"font: 12pt \"a\ud0c0\uc774\ud2c0\uace0\ub5152\";\n"
"color: rgb(255, 255, 255)")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(30, 45))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(images/icons/cil-home.png);\n"
"font: 12pt \"a\ud0c0\uc774\ud2c0\uace0\ub5152\";")

        self.verticalLayout_8.addWidget(self.btn_home, 0, Qt.AlignTop)

        self.btn_bookmark = QPushButton(self.topMenu)
        self.btn_bookmark.setObjectName(u"btn_bookmark")
        sizePolicy.setHeightForWidth(self.btn_bookmark.sizePolicy().hasHeightForWidth())
        self.btn_bookmark.setSizePolicy(sizePolicy)
        self.btn_bookmark.setMinimumSize(QSize(30, 45))
        self.btn_bookmark.setFont(font1)
        self.btn_bookmark.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_bookmark.setLayoutDirection(Qt.LeftToRight)
        self.btn_bookmark.setStyleSheet(u"background-image:url(images/images/bookmark.png);\n"
"font: 12pt \"a\ud0c0\uc774\ud2c0\uace0\ub5152\";")

        self.verticalLayout_8.addWidget(self.btn_bookmark)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")

        self.verticalMenuLayout.addLayout(self.formLayout)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setMinimumSize(QSize(0, 0))
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(30, 45))
        self.toggleLeftBox.setFont(font1)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image:url(images/images/path869.png);\n"
"font: 12pt \"a\ud0c0\uc774\ud2c0\uace0\ub5152\";")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setAutoFillBackground(False)
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setStyleSheet(u"\n"
"background-color: rgb(198, 209, 224);")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.contentBox.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setKerning(True)
        self.contentTopBg.setFont(font2)
        self.contentTopBg.setStyleSheet(u"background-color: rgb(124, 135, 166)\n"
"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setStyleSheet(u"background-color: transparent;")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.contentBottom.setLineWidth(0)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.content.setLineWidth(0)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.pagesContainer.setLineWidth(0)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setAutoFillBackground(False)
        self.home.setStyleSheet(u"background-color: transparent;")
        self.camLabel = QLabel(self.home)
        self.camLabel.setObjectName(u"camLabel")
        self.camLabel.setGeometry(QRect(20, 210, 640, 360))
        self.camLabel.setCursor(QCursor(Qt.SizeHorCursor))
        self.camLabel.setStyleSheet(u"border-radius: 80;\n"
"border-style: solid;\n"
"\n"
"background-color: black; \n"
"box-shadow: 4px 4px 2px 1px rgba(0, 0, 0, .2);")
        self.label_2 = QLabel(self.home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 661, 141))
        self.label_2.setStyleSheet(u"font: 72pt \"a\ud0c0\uc774\ud2c0\uace0\ub5155\";\n"
"color: rgb(44, 61, 115);")
        self.label_3 = QLabel(self.home)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 130, 761, 71))
        self.label_3.setStyleSheet(u"font: 600 40pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(44, 61, 115);\n"
"")
        self.explain = QWidget(self.home)
        self.explain.setObjectName(u"explain")
        self.explain.setGeometry(QRect(40, 500, 421, 51))
        self.label_4 = QLabel(self.explain)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 0, 291, 41))
        self.label_4.setMaximumSize(QSize(16777215, 16777209))
        self.label_4.setStyleSheet(u"font: 13pt \"a\uc61b\ub0a0\uc0ac\uc9c4\uad003\";\n"
"color: rgb(41, 57, 108);\n"
"background-color: rgb(255, 255, 255);\n"
"text-align:center;\n"
"border-radius:7;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.explain)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 10, 21, 21))
        self.label_5.setStyleSheet(u"border-image: url(images/images/face-recognition.svg);")
        self.textBrowser = QTextBrowser(self.home)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(80, 580, 500, 31))
        self.textBrowser.setMinimumSize(QSize(500, 0))
        self.textBrowser.setMaximumSize(QSize(500, 200))
        self.textBrowser.setStyleSheet(u"background-color: transparent;")
        self.textBrowser.setFrameShape(QFrame.NoFrame)
        self.widget_2 = QWidget(self.home)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(670, 180, 120, 80))
        self.slicedPicture = QLabel(self.home)
        self.slicedPicture.setObjectName(u"slicedPicture")
        self.slicedPicture.setGeometry(QRect(820, 210, 131, 121))
        self.selectedId = QLabel(self.home)
        self.selectedId.setObjectName(u"selectedId")
        self.selectedId.setGeometry(QRect(810, 350, 151, 21))
        self.selectedId.setStyleSheet(u"font: 13pt \"a\uc61b\ub0a0\uc0ac\uc9c4\uad003\";\n"
"color: rgb(41, 57, 108);\n"
"background-color: rgb(255, 255, 255);\n"
"text-align:center;\n"
"border-radius:7;\n"
"padding: 2;")
        self.selectedId.setAlignment(Qt.AlignCenter)
        self.explain_2 = QWidget(self.home)
        self.explain_2.setObjectName(u"explain_2")
        self.explain_2.setGeometry(QRect(760, 390, 231, 51))
        self.function_text = QLabel(self.explain_2)
        self.function_text.setObjectName(u"function_text")
        self.function_text.setGeometry(QRect(10, 0, 221, 41))
        self.function_text.setMaximumSize(QSize(16777215, 16777209))
        self.function_text.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.function_text.setStyleSheet(u"font: 13pt \"a\uc61b\ub0a0\uc0ac\uc9c4\uad003\";\n"
"color: rgb(41, 57, 108);\n"
"background-color: rgb(255, 255, 255);\n"
"text-align:center;\n"
"border-radius:7;\n"
"padding:3;")
        self.function_text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.explain_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 10, 21, 21))
        self.label_9.setStyleSheet(u"border-image: url(images/images/face-recognition.svg);")
        self.function_button = QPushButton(self.explain_2)
        self.function_button.setObjectName(u"function_button")
        self.function_button.setGeometry(QRect(10, 0, 221, 41))
        self.function_button.setStyleSheet(u"border-color: transparent;")
        self.stackedWidget.addWidget(self.home)
        self.add = QWidget()
        self.add.setObjectName(u"add")
        self.adduser = QWidget(self.add)
        self.adduser.setObjectName(u"adduser")
        self.adduser.setGeometry(QRect(-10, -20, 1131, 791))
        self.adduser.setCursor(QCursor(Qt.ArrowCursor))
        self.adduser.setStyleSheet(u"background-color: rgba(100, 100, 100, 80)\n"
"")
        self.adduser.setInputMethodHints(Qt.ImhDate)
        self.frame_2 = QFrame(self.adduser)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(250, 160, 391, 391))
        self.frame_2.setStyleSheet(u"background-color: rgb(213, 213, 213)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.closeAppBtn_2 = QPushButton(self.frame_2)
        self.closeAppBtn_2.setObjectName(u"closeAppBtn_2")
        self.closeAppBtn_2.setGeometry(QRect(360, 0, 28, 28))
        self.closeAppBtn_2.setMinimumSize(QSize(28, 28))
        self.closeAppBtn_2.setMaximumSize(QSize(28, 28))
        self.closeAppBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn_2.setToolTipDuration(-1)
        self.closeAppBtn_2.setStyleSheet(u"border-color:rgb(213, 213, 213)")
        self.closeAppBtn_2.setIcon(icon)
        self.closeAppBtn_2.setIconSize(QSize(15, 15))
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 30, 371, 351))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 70, 291, 41))
        self.label_10.setAutoFillBackground(False)
        self.label_10.setStyleSheet(u"color: rgb(44, 61, 115);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 18pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac Bold\";")
        self.adduserName = QLineEdit(self.frame_3)
        self.adduserName.setObjectName(u"adduserName")
        self.adduserName.setGeometry(QRect(70, 150, 251, 41))
        self.adduserName.setAutoFillBackground(False)
        self.adduserName.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";\n"
"color: rgb(81, 81, 81);\n"
"")
        self.adduserName.setInputMethodHints(Qt.ImhNone)
        self.adduserName.setEchoMode(QLineEdit.Normal)
        self.adduserName.setDragEnabled(True)
        self.adduserName.setClearButtonEnabled(True)
        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(30, 160, 31, 21))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";")
        self.complete = QPushButton(self.frame_3)
        self.complete.setObjectName(u"complete")
        self.complete.setGeometry(QRect(240, 260, 81, 31))
        self.complete.setCursor(QCursor(Qt.PointingHandCursor))
        self.complete.setToolTipDuration(-1)
        self.complete.setStyleSheet(u"color: rgb(44, 61, 115);\n"
"font: 700 11pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac Bold\";\n"
"background-color: rgb(255, 255, 255);")
        self.frame_3.raise_()
        self.closeAppBtn_2.raise_()
        self.stackedWidget.addWidget(self.add)
        self.bookmark = QWidget()
        self.bookmark.setObjectName(u"bookmark")
        self.bookmark.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.bookmark)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.scrollArea = QScrollArea(self.bookmark)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"font: 16pt \"a\ud0c0\uc774\ud2c0\uace0\ub5155\";\n"
"color: rgb(44, 61, 115)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1086, 692))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;")
        self.verticalLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 1092, 101))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.appname = QLabel(self.verticalLayoutWidget)
        self.appname.setObjectName(u"appname")
        self.appname.setStyleSheet(u"font: 72pt \"a\ud0c0\uc774\ud2c0\uace0\ub5155\";\n"
"color: rgb(44, 61, 115);")
        self.appname.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.appname)

        self.gridLayoutWidget = QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(90, 190, 848, 389))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.gridLayoutWidget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(420, 120))
        self.widget_5.setMaximumSize(QSize(16777215, 120))
        self.label_19 = QLabel(self.widget_5)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy1)
        self.label_19.setBaseSize(QSize(400, 100))
        self.label_19.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.editbutton1_2 = QPushButton(self.widget_5)
        self.editbutton1_2.setObjectName(u"editbutton1_2")
        self.editbutton1_2.setGeometry(QRect(330, 40, 71, 24))
        self.editbutton1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1_2.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1_2 = QPushButton(self.widget_5)
        self.delbutton1_2.setObjectName(u"delbutton1_2")
        self.delbutton1_2.setGeometry(QRect(330, 70, 71, 24))
        self.delbutton1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1_2.setStyleSheet(u"border-color: transparent;\n"
"")
        self.label_16 = QLabel(self.widget_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(62, 31, 211, 71))
        self.label_16.setStyleSheet(u"border-image: url(images/images/59-590993_waterfalls-clip-art.png);")

        self.gridLayout.addWidget(self.widget_5, 1, 2, 1, 1)

        self.widget_4 = QWidget(self.gridLayoutWidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(420, 120))
        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setBaseSize(QSize(400, 100))
        self.label_18.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.editbutton1 = QPushButton(self.widget_4)
        self.editbutton1.setObjectName(u"editbutton1")
        self.editbutton1.setGeometry(QRect(330, 38, 71, 24))
        self.editbutton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1 = QPushButton(self.widget_4)
        self.delbutton1.setObjectName(u"delbutton1")
        self.delbutton1.setGeometry(QRect(330, 71, 71, 24))
        self.delbutton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1.setStyleSheet(u"border-color: transparent;\n"
"")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(63, 35, 231, 61))
        self.label_8.setStyleSheet(u"border-image: url(images/images/\uc2dc\uadf8\ub2c8\ucc98 \uc88c\uc6b0\uc870\ud569(\uc815\uc7a51)_\uad6d\ubb38.jpg);")
        self.label_18.raise_()
        self.label_8.raise_()
        self.editbutton1.raise_()
        self.delbutton1.raise_()

        self.gridLayout.addWidget(self.widget_4, 0, 2, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.widget_6 = QWidget(self.gridLayoutWidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(420, 120))
        self.widget_6.setMaximumSize(QSize(16777215, 120))
        self.label_20 = QLabel(self.widget_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)
        self.label_20.setBaseSize(QSize(400, 100))
        self.label_20.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.editbutton1_3 = QPushButton(self.widget_6)
        self.editbutton1_3.setObjectName(u"editbutton1_3")
        self.editbutton1_3.setGeometry(QRect(330, 40, 71, 24))
        self.editbutton1_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1_3.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1_3 = QPushButton(self.widget_6)
        self.delbutton1_3.setObjectName(u"delbutton1_3")
        self.delbutton1_3.setGeometry(QRect(330, 70, 71, 24))
        self.delbutton1_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1_3.setStyleSheet(u"border-color: transparent;\n"
"")
        self.label_15 = QLabel(self.widget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 47, 211, 41))
        self.label_15.setStyleSheet(u"border-image:url(images/images/Naver_Logotype.svg);")

        self.gridLayout.addWidget(self.widget_6, 0, 3, 1, 1)

        self.widget_8 = QWidget(self.gridLayoutWidget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(420, 120))
        self.label_22 = QLabel(self.widget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setBaseSize(QSize(400, 100))
        self.label_22.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.editbutton1_5 = QPushButton(self.widget_8)
        self.editbutton1_5.setObjectName(u"editbutton1_5")
        self.editbutton1_5.setGeometry(QRect(330, 40, 71, 24))
        self.editbutton1_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1_5.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1_5 = QPushButton(self.widget_8)
        self.delbutton1_5.setObjectName(u"delbutton1_5")
        self.delbutton1_5.setGeometry(QRect(330, 70, 71, 24))
        self.delbutton1_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1_5.setStyleSheet(u"border-color: transparent;\n"
"")
        self.label_24 = QLabel(self.widget_8)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(62, 38, 61, 61))
        self.label_24.setStyleSheet(u"border-image: url(images/images/nav.logo.png);")
        self.label_25 = QLabel(self.widget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(130, 50, 141, 41))
        self.label_25.setStyleSheet(u"font: 24pt \"a\ud0c0\uc774\ud2c0\uace0\ub5154\";\n"
"color: rgb(198, 41, 23);")

        self.gridLayout.addWidget(self.widget_8, 2, 3, 1, 1)

        self.widget_9 = QWidget(self.gridLayoutWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(420, 120))
        self.label_23 = QLabel(self.widget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy1)
        self.label_23.setBaseSize(QSize(400, 100))
        self.label_23.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.editbutton1_6 = QPushButton(self.widget_9)
        self.editbutton1_6.setObjectName(u"editbutton1_6")
        self.editbutton1_6.setGeometry(QRect(330, 40, 71, 24))
        self.editbutton1_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1_6.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1_6 = QPushButton(self.widget_9)
        self.delbutton1_6.setObjectName(u"delbutton1_6")
        self.delbutton1_6.setGeometry(QRect(330, 70, 71, 24))
        self.delbutton1_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1_6.setStyleSheet(u"border-color: transparent;\n"
"")
        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(62, 36, 171, 61))
        self.label_17.setStyleSheet(u"border-image: url(images/images/Daum_communication_logo.svg);")

        self.gridLayout.addWidget(self.widget_9, 1, 3, 1, 1)

        self.widget_7 = QWidget(self.gridLayoutWidget)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(420, 120))
        self.widget_7.setMaximumSize(QSize(16777215, 120))
        self.label_21 = QLabel(self.widget_7)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(30, 20, 381, 91))
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        self.label_21.setBaseSize(QSize(400, 100))
        self.label_21.setStyleSheet(u"border-style:solid;\n"
"border-radius:23;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_24 = QPushButton(self.widget_7)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(58, -43, 241, 221))
        self.pushButton_24.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_24.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_24.setStyleSheet(u"border-image: url(images/images/blackboard-vector-logo.svg);")
        self.pushButton_24.setAutoRepeatInterval(0)
        self.editbutton1_4 = QPushButton(self.widget_7)
        self.editbutton1_4.setObjectName(u"editbutton1_4")
        self.editbutton1_4.setGeometry(QRect(330, 40, 71, 24))
        self.editbutton1_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.editbutton1_4.setStyleSheet(u"border-color: transparent;\n"
"")
        self.delbutton1_4 = QPushButton(self.widget_7)
        self.delbutton1_4.setObjectName(u"delbutton1_4")
        self.delbutton1_4.setGeometry(QRect(330, 70, 71, 24))
        self.delbutton1_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.delbutton1_4.setStyleSheet(u"border-color: transparent;\n"
"")

        self.gridLayout.addWidget(self.widget_7, 2, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.bookmark)
        self.pageinfo = QWidget()
        self.pageinfo.setObjectName(u"pageinfo")
        self.chageinfo = QWidget(self.pageinfo)
        self.chageinfo.setObjectName(u"chageinfo")
        self.chageinfo.setGeometry(QRect(-30, -10, 1131, 791))
        self.chageinfo.setCursor(QCursor(Qt.ArrowCursor))
        self.chageinfo.setStyleSheet(u"background-color: rgba(100, 100, 100, 80)\n"
"")
        self.chageinfo.setInputMethodHints(Qt.ImhDate)
        self.frame_4 = QFrame(self.chageinfo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(390, 160, 361, 391))
        self.frame_4.setStyleSheet(u"background-color: rgb(213, 213, 213)")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.closeAppBtn_3 = QPushButton(self.frame_4)
        self.closeAppBtn_3.setObjectName(u"closeAppBtn_3")
        self.closeAppBtn_3.setGeometry(QRect(330, 0, 28, 28))
        self.closeAppBtn_3.setMinimumSize(QSize(28, 28))
        self.closeAppBtn_3.setMaximumSize(QSize(28, 28))
        self.closeAppBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn_3.setToolTipDuration(-1)
        self.closeAppBtn_3.setStyleSheet(u"border-color:rgb(213, 213, 213)")
        self.closeAppBtn_3.setIcon(icon)
        self.closeAppBtn_3.setIconSize(QSize(15, 15))
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 30, 341, 351))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 30, 291, 41))
        self.label_12.setAutoFillBackground(False)
        self.label_12.setStyleSheet(u"color: rgb(44, 61, 115);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 18pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac Bold\";")
        self.adduserName_2 = QLineEdit(self.frame_5)
        self.adduserName_2.setObjectName(u"adduserName_2")
        self.adduserName_2.setGeometry(QRect(40, 120, 271, 41))
        self.adduserName_2.setAutoFillBackground(False)
        self.adduserName_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";\n"
"color: rgb(81, 81, 81);\n"
"")
        self.adduserName_2.setInputMethodHints(Qt.ImhNone)
        self.adduserName_2.setEchoMode(QLineEdit.Normal)
        self.adduserName_2.setDragEnabled(True)
        self.adduserName_2.setClearButtonEnabled(True)
        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 90, 41, 21))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";")
        self.complete_2 = QPushButton(self.frame_5)
        self.complete_2.setObjectName(u"complete_2")
        self.complete_2.setGeometry(QRect(230, 300, 81, 31))
        self.complete_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.complete_2.setToolTipDuration(-1)
        self.complete_2.setStyleSheet(u"color: rgb(44, 61, 115);\n"
"font: 700 11pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac Bold\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_14 = QLabel(self.frame_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(40, 180, 51, 21))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setStyleSheet(u"color: rgb(130, 130, 130);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 10pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";")
        self.adduserName_3 = QLineEdit(self.frame_5)
        self.adduserName_3.setObjectName(u"adduserName_3")
        self.adduserName_3.setGeometry(QRect(40, 210, 271, 41))
        self.adduserName_3.setAutoFillBackground(False)
        self.adduserName_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"\ub098\ub214\uc2a4\ud018\uc5b4_ac\";\n"
"color: rgb(81, 81, 81);\n"
"")
        self.adduserName_3.setInputMethodHints(Qt.ImhNone)
        self.adduserName_3.setEchoMode(QLineEdit.Normal)
        self.adduserName_3.setDragEnabled(True)
        self.adduserName_3.setClearButtonEnabled(True)
        self.label_13.raise_()
        self.label_12.raise_()
        self.adduserName_2.raise_()
        self.complete_2.raise_()
        self.label_14.raise_()
        self.adduserName_3.raise_()
        self.stackedWidget.addWidget(self.pageinfo)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setStyleSheet(u"background-color: rgb(4, 10, 50)")
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setMinimumSize(QSize(300, 0))
        self.contentSettings.setStyleSheet(u"background-color: rgb(4, 10, 50)")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.contentSettings)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 0, 200, 80))
        self.widget.setMinimumSize(QSize(200, 80))
        self.widget.setMaximumSize(QSize(200, 80))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 30, 121, 41))
        self.label_7.setStyleSheet(u"font: 28pt \"a\uc61b\ub0a0\uc0ac\uc9c4\uad002\";")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 10, 65, 80))
        self.label_6.setStyleSheet(u"border-image: url(images/images/noun_Login_3407301.svg);\n"
"")
        self.scrollArea_2 = QScrollArea(self.contentSettings)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(10, 80, 280, 500))
        self.scrollArea_2.setMinimumSize(QSize(0, 500))
        self.scrollArea_2.setMaximumSize(QSize(300, 500))
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 280, 500))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 40))
        self.frame.setMaximumSize(QSize(200, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.name = QLabel(self.frame)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 0))
        self.name.setMaximumSize(QSize(16777215, 30))
        self.name.setStyleSheet(u"font: 15pt \"a\uc61b\ub0a0\uc0ac\uc9c4\uad002\";\n"
"color: rgb(0, 0, 0);\n"
"padding: 2;\n"
"border-radius: 10;\n"
"border: solid ;\n"
"background-color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.name, 1, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.contentSettings, 0, Qt.AlignHCenter)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.toggleButton, self.btn_home)
        QWidget.setTabOrder(self.btn_home, self.btn_bookmark)
        QWidget.setTabOrder(self.btn_bookmark, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnBtn)
        QWidget.setTabOrder(self.extraCloseColumnBtn, self.btn_share)
        QWidget.setTabOrder(self.btn_share, self.btn_adjustments)
        QWidget.setTabOrder(self.btn_adjustments, self.btn_more)
        QWidget.setTabOrder(self.btn_more, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.scrollArea_2)
        QWidget.setTabOrder(self.scrollArea_2, self.textBrowser)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"\uba54\ub274", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"\ud648", None))
        self.btn_bookmark.setText(QCoreApplication.translate("MainWindow", u"\ubd81\ub9c8\ud06c", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc544\uc6c3", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" "
                        "style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.camLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"FaceLink", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Face ID for your convenience.", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \ud560 \uc0ac\uc6a9\uc790\ub97c \uc120\ud0dd\ud574\uc8fc\uc138\uc694. ", None))
        self.label_5.setText("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'a\uc61b\ub0a0\uc0ac\uc9c4\uad003'; font-size:11pt; color:#000000;\">\ucea0\ud654\uba74\uc5d0 \uc778\uc2dd\ub41c \uc5bc\uad74\uc774\ub098 \ub85c\uadf8\uc778 \uba54\ub274\uc5d0 \ub4f1\ub85d\ub41c \uc774\ub984\uc744 \ud074\ub9ad\ud558\uc138\uc694!</span></p></body></html>", None))
        self.slicedPicture.setText("")
        self.selectedId.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.function_text.setText(QCoreApplication.translate("MainWindow", u"\uc5bc\uad74 \uc120\ud0dd\uc774 \ud544\uc694\ud569\ub2c8\ub2e4.", None))
        self.label_9.setText("")
        self.function_button.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn_2.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790\ub97c \ub4f1\ub85d\ud574\uc8fc\uc138\uc694", None))
        self.adduserName.setText("")
        self.adduserName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc601\uc5b4\ub85c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\uc774\ub984 :", None))
#if QT_CONFIG(tooltip)
        self.complete.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.complete.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"\ubd81\ub9c8\ud06c!", None))
        self.label_19.setText("")
        self.editbutton1_2.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1_2.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_16.setText("")
        self.label_18.setText("")
        self.editbutton1.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_8.setText("")
        self.label_20.setText("")
        self.editbutton1_3.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1_3.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_15.setText("")
        self.label_22.setText("")
        self.editbutton1_5.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1_5.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_24.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\uc5d0\ube0c\ub9ac\ud0c0\uc784", None))
        self.label_23.setText("")
        self.editbutton1_6.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1_6.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.label_17.setText("")
        self.label_21.setText("")
        self.pushButton_24.setText("")
        self.editbutton1_4.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.delbutton1_4.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
#if QT_CONFIG(tooltip)
        self.closeAppBtn_3.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn_3.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\uacc4\uc815 \uc815\ubcf4 \ubcc0\uacbd", None))
        self.adduserName_2.setText("")
        self.adduserName_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
#if QT_CONFIG(tooltip)
        self.complete_2.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.complete_2.setText(QCoreApplication.translate("MainWindow", u"\uc644\ub8cc", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.adduserName_3.setText("")
        self.adduserName_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_6.setText("")
        self.name.setText(QCoreApplication.translate("MainWindow", u"Unknown", None))
    # retranslateUi

