# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form1caKSwP.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PyQt6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1434, 753)
        MainWindow.setMinimumSize(QSize(75, 0))
        MainWindow.setStyleSheet(u"/* Modern Professional Trading Theme */\n"
"QMainWindow {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                                stop:0 #0c1117, stop:0.5 #0f151d, stop:1 #0a0e14);\n"
"    color: #e8edf2;\n"
"    font-family: 'Segoe UI', 'Inter', -apple-system, sans-serif;\n"
"    font-weight: 450;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ===== Modern Circular Radio Button ===== */\n"
"QRadioButton {\n"
"    color: #e2e8f0;\n"
"    \n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
" \n"
"}\n"
"\n"
"/* Default circle */\n"
"QRadioButton::indicator {\n"
"    width: 14px;\n"
"    height: 14px;\n"
"    border-radius: 9px; /* Perfect circle */\n"
"    border: 2px solid #475569; /* Neutral border (slate gray) */\n"
"    background: #1e293b;       /* Dark inner base */\n"
"}\n"
"\n"
"/* Hover (not selected) */\n"
"QRadioButton::indicator:hover:!checked {\n"
"    border: 2px solid #60a5fa; /* Blue border on hover */\n"
"    background: #273445;\n"
"}\n"
"\n"
"/* Selected (flat blue fill) */\n"
"QRadioB"
                        "utton::indicator:checked {\n"
"    background: #3b82f6;  /* Pure blue */\n"
"    border: 2px solid #001e3d; /* Blue border */\n"
"}\n"
"\n"
"/* Optional: subtle font color change when selected */\n"
"QRadioButton::indicator:checked + QRadioButton {\n"
"    color: #60a5fa;\n"
"}\n"
"\n"
"/* Disabled */\n"
"QRadioButton:disabled {\n"
"    color: rgba(226, 232, 240, 0.35);\n"
"}\n"
"QRadioButton::indicator:disabled {\n"
"    background: #1e293b;\n"
"    border: 2px solid rgba(148, 163, 184, 0.2);\n"
"}\n"
"\n"
"/* Modern Card Containers */\n"
"QGroupBox {\n"
"    background: rgba(30, 41, 59, 0.7);\n"
"    border: 1px solid rgba(148, 163, 184, 0.2);\n"
"    border-radius: 12px;\n"
"    margin-top: 16px;\n"
"    padding-top: 4px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    color: #60a5fa;\n"
"    font-weight: 600;\n"
"    font-size: 14px;\n"
"    subcontrol-origin: margin;\n"
"    left: 16px;\n"
"    padding: 4px 14px;\n"
"    background: rgba(15, 23, 42, 0.9);\n"
"    border-radius: 12px;\n"
"    border: 1px solid r"
                        "gba(96, 165, 250, 0.3);\n"
"}\n"
"\n"
"/* Modern Buttons with Smooth Gradients */\n"
"\n"
"/* Enhanced Lists with Modern Styling */\n"
"QListWidget {\n"
"    background: rgba(15, 23, 42, 0.5);\n"
"    border: 1px solid rgba(148, 163, 184, 0.2);\n"
"    border-radius: 10px;\n"
"    color: #e2e8f0;\n"
"    font-size: 13px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 4px 16px;\n"
"    border-bottom: 1px solid rgba(148, 163, 184, 0.1);\n"
"    border-radius: 6px;\n"
"    margin: 2px 6px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: rgba(96, 165, 250, 0.15);\n"
"    color: #60a5fa;\n"
"    border-left: 4px solid #60a5fa;\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background: rgba(148, 163, 184, 0.1);\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"/* Modern Tables with Enhanced Design */\n"
"\n"
"\n"
"/* Enhanced Input Fields */\n"
" QComboBox {\n"
"    background: rgba(15, 23, 42, 0.6);\n"
"    border: 1px solid rgba(148, 163, 184, 0.3);\n"
"    border-radius: 8px"
                        ";\n"
"    padding: 4px 4px;\n"
"    color: #f1f5f9;\n"
"    font-size: 14px;\n"
"    selection-background-color: #3b82f6;\n"
"\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #60a5fa;\n"
"    background: rgba(15, 23, 42, 0.8);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 32px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #94a3b8;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: rgba(15, 23, 42, 0.95);\n"
"    border: 1px solid rgba(148, 163, 184, 0.3);\n"
"    color: #e2e8f0;\n"
"    selection-background-color: rgba(96, 165, 250, 0.2);\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* Modern Tab Widget */\n"
"\n"
"/* Modern Scrollbars */\n"
"QScrollBar:vertical {\n"
"    background: rgba(30, 41, 59, 0.4);\n"
"    width: 14px;\n"
"    border-radius: 7px;\n"
"    margin: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    b"
                        "ackground: rgba(96, 165, 250, 0.6);\n"
"    border-radius: 7px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(96, 165, 250, 0.8);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/* Tool Tips */\n"
"QToolTip {\n"
"    background: rgba(15, 23, 42, 0.95);\n"
"    color: #e2e8f0;\n"
"    border: 1px solid rgba(96, 165, 250, 0.4);\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 13px;\n"
"\n"
"}")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionload = QAction(MainWindow)
        self.actionload.setObjectName(u"actionload")
        self.actionshow = QAction(MainWindow)
        self.actionshow.setObjectName(u"actionshow")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.actionlicense = QAction(MainWindow)
        self.actionlicense.setObjectName(u"actionlicense")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #121823, stop:0.5 #121823, stop:1 #27344b);\n"
"    border: 1px dashed #64748b;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setMinimumSize(QSize(250, 0))
        self.leftPanel.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.symbolInput = QLineEdit(self.leftPanel)
        self.symbolInput.setObjectName(u"symbolInput")
        self.symbolInput.setMaximumSize(QSize(16777215, 39))
        self.symbolInput.setStyleSheet(u"#symbolInput {\n"
"    background-color: #0f172a;\n"
"    color: #e2e8f0;\n"
"    border: 2px solid #475569;\n"
"    border-radius: 8px;\n"
"	border-style: dashed;\n"
"    padding: 8px 12px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #3b82f6;\n"
"}\n"
"\n"
"#symbolInput:hover {\n"
"    border-color: #64748b;\n"
"    background-color: #1e293b;\n"
"}\n"
"\n"
"#symbolInput:focus {\n"
"    border-color: #3b82f6;\n"
"    background-color: #1e293b;\n"
"}\n"
"\n"
"#symbolInput[readOnly=\"true\"] {\n"
"    background-color: #0f172a;\n"
"    color: #94a3b8;\n"
"    border-style: dashed;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.symbolInput)

        self.watchlistGroup = QGroupBox(self.leftPanel)
        self.watchlistGroup.setObjectName(u"watchlistGroup")
        self.verticalLayout_3 = QVBoxLayout(self.watchlistGroup)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.watchlist = QListWidget(self.watchlistGroup)
        QListWidgetItem(self.watchlist)
        QListWidgetItem(self.watchlist)
        QListWidgetItem(self.watchlist)
        QListWidgetItem(self.watchlist)
        QListWidgetItem(self.watchlist)
        self.watchlist.setObjectName(u"watchlist")
        self.watchlist.setStyleSheet(u"font-size: 13px;\n"
"border-radius: 10px;\n"
"font-weight: 500;")

        self.verticalLayout_3.addWidget(self.watchlist)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.addToWatchlistBtn = QPushButton(self.watchlistGroup)
        self.addToWatchlistBtn.setObjectName(u"addToWatchlistBtn")
        self.addToWatchlistBtn.setMinimumSize(QSize(121, 0))
        self.addToWatchlistBtn.setMaximumSize(QSize(100, 30))
        self.addToWatchlistBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 4px 12px;\n"
"    background: rgba(59, 130, 246, 0.9); /* Base blue */\n"
"    color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(59, 130, 246, 0.6);\n"
"}\n"
"\n"
"/* Hover \u2013 slightly brighter */\n"
"QPushButton:hover {\n"
"    background: rgba(80, 150, 255, 1);\n"
"    border: 1px solid rgba(100, 170, 255, 0.9);\n"
"}\n"
"\n"
"/* Pressed \u2013 stronger color with push-down effect */\n"
"QPushButton:pressed {\n"
"    background: rgba(35, 95, 200, 0.95);\n"
"    border: 1px solid rgba(35, 95, 200, 0.6);\n"
"    padding-top: 4px; /* simulate press effect */\n"
"    padding-bottom: 7px;\n"
"}\n"
"\n"
"/* Focus \u2013 keyboard selection */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(120, 180, 255, 1); /* highlight border */\n"
"}\n"
"\n"
"/* Disabled \u2013 lower visibility */\n"
"QPushButton:disabled {\n"
"    background: rgba(59, 130, 246, 0.35);\n"
"    color: rgba(2"
                        "55, 255, 255, 0.4);\n"
"    border: 1px solid rgba(59, 130, 246, 0.25);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.addToWatchlistBtn)

        self.removeFromWatchlistBtn = QPushButton(self.watchlistGroup)
        self.removeFromWatchlistBtn.setObjectName(u"removeFromWatchlistBtn")
        self.removeFromWatchlistBtn.setMaximumSize(QSize(100, 30))
        self.removeFromWatchlistBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 8px 12px;\n"
"    background: rgba(239, 68, 68, 0.9);  /* base remove red */\n"
"    color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(239, 68, 68, 0.6);\n"
"}\n"
"\n"
"/* Hover \u2013 alerting effect */\n"
"QPushButton:hover {\n"
"    background: rgba(255, 90, 90, 1);\n"
"    border: 1px solid rgba(255, 115, 115, 0.9);\n"
"}\n"
"\n"
"/* Pressed \u2013 deeper red tone with push effect */\n"
"QPushButton:pressed {\n"
"    background: rgba(185, 40, 40, 0.95);\n"
"    border: 1px solid rgba(185, 40, 40, 0.6);\n"
"    padding-top: 9px;    /* tactile press feedback */\n"
"    padding-bottom: 7px;\n"
"}\n"
"\n"
"/* Focus \u2013 highlight outline for keyboard users */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(255, 150, 150, 1);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(239, 68, 68, 0.35);\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"    "
                        "border: 1px solid rgba(239, 68, 68, 0.25);\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.removeFromWatchlistBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.watchlistGroup)

        self.alertsTabWidget = QTabWidget(self.leftPanel)
        self.alertsTabWidget.setObjectName(u"alertsTabWidget")
        self.alertsTabWidget.setStyleSheet(u"/* === Global Tab Widget Pane === */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #334155;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1e293b,\n"
"        stop:1 #0f172a\n"
"    );\n"
"    border-radius: 10px;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"/* === Tab Styling === */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #475569,\n"
"        stop:1 #334155\n"
"    );\n"
"    color: #cbd5e1;\n"
"    padding: 4px 4px;\n"
"    margin-right: 5px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: 500;\n"
"    \n"
"    border: 1px solid #475569;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"/* === Selected Tab === */\n"
"QTabBar::tab:selected {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #3b82f6,\n"
"        stop:1 #1d4ed8\n"
"    );\n"
"    color: #ffffff;\n"
"    border-color:"
                        " #60a5fa;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* === Hover (with no selection) === */\n"
"QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #143583,\n"
"        stop:1 #0c2151\n"
"    );\n"
"    color: #f1f5f9;\n"
"    border: 1px solid #18409e;\n"
"}\n"
"\n"
"/* === Remove base frame === */\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"}\n"
"")
        self.alertsTabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.priceAlertsTab = QWidget()
        self.priceAlertsTab.setObjectName(u"priceAlertsTab")
        self.verticalLayout_11 = QVBoxLayout(self.priceAlertsTab)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.priceAlertsList = QListWidget(self.priceAlertsTab)
        QListWidgetItem(self.priceAlertsList)
        QListWidgetItem(self.priceAlertsList)
        QListWidgetItem(self.priceAlertsList)
        self.priceAlertsList.setObjectName(u"priceAlertsList")

        self.verticalLayout_11.addWidget(self.priceAlertsList)

        self.alertsTabWidget.addTab(self.priceAlertsTab, "")
        self.volumeAlertsTab = QWidget()
        self.volumeAlertsTab.setObjectName(u"volumeAlertsTab")
        self.verticalLayout_12 = QVBoxLayout(self.volumeAlertsTab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.volumeAlertsList = QListWidget(self.volumeAlertsTab)
        QListWidgetItem(self.volumeAlertsList)
        QListWidgetItem(self.volumeAlertsList)
        QListWidgetItem(self.volumeAlertsList)
        self.volumeAlertsList.setObjectName(u"volumeAlertsList")

        self.verticalLayout_12.addWidget(self.volumeAlertsList)

        self.alertsTabWidget.addTab(self.volumeAlertsTab, "")
        self.newsAlertsTab = QWidget()
        self.newsAlertsTab.setObjectName(u"newsAlertsTab")
        self.verticalLayout_13 = QVBoxLayout(self.newsAlertsTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.newsAlertsList = QListWidget(self.newsAlertsTab)
        QListWidgetItem(self.newsAlertsList)
        QListWidgetItem(self.newsAlertsList)
        QListWidgetItem(self.newsAlertsList)
        self.newsAlertsList.setObjectName(u"newsAlertsList")

        self.verticalLayout_13.addWidget(self.newsAlertsList)

        self.alertsTabWidget.addTab(self.newsAlertsTab, "")

        self.verticalLayout_2.addWidget(self.alertsTabWidget)

        self.quickActions = QGroupBox(self.leftPanel)
        self.quickActions.setObjectName(u"quickActions")
        self.gridLayout_3 = QGridLayout(self.quickActions)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.quickBuyBtn = QPushButton(self.quickActions)
        self.quickBuyBtn.setObjectName(u"quickBuyBtn")
        self.quickBuyBtn.setMinimumSize(QSize(0, 30))
        self.quickBuyBtn.setMaximumSize(QSize(16777215, 30))
        self.quickBuyBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    \n"
"    background: rgba(16, 185, 129, 0.9);   /* base teal green */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(16, 185, 129, 0.6);\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background: rgba(32, 205, 147, 1);\n"
"    border: 1px solid rgba(32, 205, 147, 0.85);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background: rgba(12, 140, 95, 0.95);\n"
"    border: 1px solid rgba(12, 140, 95, 0.6);\n"
"    /* subtle press effect */\n"
"    \n"
"    color: #EBFFF7;\n"
"}\n"
"\n"
"/* Focus (keyboard interaction) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(50, 255, 190, 0.9);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(16, 185, 129, 0.35);\n"
"    color: rgba(2, 18, 10, 0.3);\n"
"    border: 1px solid rgba(16, 185, 129, 0.25);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.quickBuyBtn, 0, 0, 1, 1)

        self.quickSellBtn = QPushButton(self.quickActions)
        self.quickSellBtn.setObjectName(u"quickSellBtn")
        self.quickSellBtn.setMaximumSize(QSize(16777215, 30))
        self.quickSellBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"    padding: 8px 12px;\n"
"    background: rgba(239, 68, 68, 0.9);  /* base remove red */\n"
"    color: #FFFFFF;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(239, 68, 68, 0.6);\n"
"}\n"
"\n"
"/* Hover \u2013 alerting effect */\n"
"QPushButton:hover {\n"
"    background: rgba(255, 90, 90, 1);\n"
"    border: 1px solid rgba(255, 115, 115, 0.9);\n"
"}\n"
"\n"
"/* Pressed \u2013 deeper red tone with push effect */\n"
"QPushButton:pressed {\n"
"    background: rgba(185, 40, 40, 0.95);\n"
"    border: 1px solid rgba(185, 40, 40, 0.6);\n"
"    padding-top: 9px;    /* tactile press feedback */\n"
"    padding-bottom: 7px;\n"
"}\n"
"\n"
"/* Focus \u2013 highlight outline for keyboard users */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(255, 150, 150, 1);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(239, 68, 68, 0.35);\n"
"    color: rgba(255, 255, 255, 0.4);\n"
"    "
                        "border: 1px solid rgba(239, 68, 68, 0.25);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.quickSellBtn, 0, 1, 1, 1)

        self.chartBtn = QPushButton(self.quickActions)
        self.chartBtn.setObjectName(u"chartBtn")
        self.chartBtn.setMaximumSize(QSize(16777215, 30))
        self.chartBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    \n"
"    background: rgba(59, 130, 246, 0.9);   /* base light blue (chart) */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(59, 130, 246, 0.6);\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background: rgba(80, 150, 255, 1);      /* brighter blue */\n"
"    border: 1px solid rgba(120, 180, 255, 0.85);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background: rgba(35, 95, 200, 0.95);    /* darker blue */\n"
"    border: 1px solid rgba(35, 95, 200, 0.6);\n"
"    color: #DFE8FF;\n"
"}\n"
"\n"
"/* Focus (keyboard interaction) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(140, 200, 255, 0.9);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(59, 130, 246, 0.35);\n"
"    color: rgba(255, 255, 255, 0.3);\n"
"    border: 1px solid rgba(59, 130, 246, 0.25);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.chartBtn, 1, 0, 1, 1)

        self.analysisBtn = QPushButton(self.quickActions)
        self.analysisBtn.setObjectName(u"analysisBtn")
        self.analysisBtn.setMinimumSize(QSize(0, 30))
        self.analysisBtn.setMaximumSize(QSize(16777215, 30))
        self.analysisBtn.setStyleSheet(u"QPushButton {\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"\n"
"    background: rgba(139, 92, 246, 0.9);   /* Base purple */\n"
"    color: white;\n"
"    border-radius: 6px;\n"
"    border: 1px solid rgba(139, 92, 246, 0.6);\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background: rgba(157, 115, 255, 1);    /* Brighter purple */\n"
"    border: 1px solid rgba(190, 150, 255, 0.85);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background: rgba(110, 55, 210, 0.95);  /* Deeper purple */\n"
"    border: 1px solid rgba(110, 55, 210, 0.6);\n"
"    color: #F1EBFF;\n"
"}\n"
"\n"
"/* Focus (keyboard interaction) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(200, 160, 255, 0.9);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(139, 92, 246, 0.35);\n"
"    color: rgba(255, 255, 255, 0.3);\n"
"    border: 1px solid rgba(139, 92, 246, 0.25);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.analysisBtn, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.quickActions)


        self.horizontalLayout_4.addWidget(self.leftPanel)

        self.separator = QFrame(self.centralwidget)
        self.separator.setObjectName(u"separator")
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.separator)

        self.centerPanel = QWidget(self.centralwidget)
        self.centerPanel.setObjectName(u"centerPanel")
        self.verticalLayout_6 = QVBoxLayout(self.centerPanel)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.liveModeLabel = QLabel(self.centerPanel)
        self.liveModeLabel.setObjectName(u"liveModeLabel")
        self.liveModeLabel.setMinimumSize(QSize(210, 0))
        self.liveModeLabel.setMaximumSize(QSize(16777215, 50))
        self.liveModeLabel.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 700;\n"
"color: #60a5fa;\n"
"padding: 4px;\n"
"background: rgba(96, 165, 250, 0.12);\n"
"border: 1px solid rgba(96, 165, 250, 0.3);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout.addWidget(self.liveModeLabel)

        self.horizontalSlider = QSlider(self.centerPanel)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMaximumSize(QSize(40, 16777215))
        self.horizontalSlider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border: 1px solid #555555;\n"
"    height: 6px;\n"
"    background: #2D2D2D;\n"
"    margin: 2px 0;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #666666, stop:1 #4A4A4A);\n"
"    border: 1px solid #333333;\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #777777, stop:1 #5A5A5A);\n"
"    border: 1px solid #0095FF;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"        stop:0 #0095FF, stop:1 #0078D4);\n"
"    border: 1px solid #005A9E;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #0095FF, stop:1 #0078D4);\n"
"    border: 1px solid #005A9E;\n"
"    heigh"
                        "t: 6px;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #2D2D2D;\n"
"    border: 1px solid #555555;\n"
"    height: 6px;\n"
"    border-radius: 6px;\n"
"}")
        self.horizontalSlider.setMaximum(1)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.horizontalSlider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.startBtn = QPushButton(self.centerPanel)
        self.startBtn.setObjectName(u"startBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.startBtn.sizePolicy().hasHeightForWidth())
        self.startBtn.setSizePolicy(sizePolicy)
        self.startBtn.setMinimumSize(QSize(60, 25))
        self.startBtn.setMaximumSize(QSize(60, 30))
        self.startBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #3b82f6, stop:1 #245dc5);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: 600;\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #2563eb, stop:1 #1d4ed8);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #1e40af;\n"
"    padding-top: 9px;\n"
"    padding-left: 13px;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.startBtn)

        self.refreshBtn = QPushButton(self.centerPanel)
        self.refreshBtn.setObjectName(u"refreshBtn")
        self.refreshBtn.setMinimumSize(QSize(75, 0))
        self.refreshBtn.setMaximumSize(QSize(75, 30))
        self.refreshBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 181, 71, 0.95),   /* lighter top */\n"
"                                stop:1 rgba(255, 153, 51, 0.95));  /* deeper bottom */\n"
"    color: #1a1a1a;          /* dark text for contrast */\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgba(255, 187, 100, 0.7);\n"
" \n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 196, 107, 1),\n"
"                                stop:1 rgba(255, 165, 82, 1));\n"
"    border: 1px solid rgba(255, 201, 126, 1);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(230, 145, 32, 0.95),\n"
"                                stop:1 rgba(200, 120, 20, 0.95));"
                        "\n"
"    border: 1px solid rgba(230, 145, 32, 0.7);\n"
"    padding-top: 7px;     /* push-down effect */\n"
"    padding-bottom: 5px;\n"
"}\n"
"\n"
"/* Focus */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(255, 213, 140, 0.9);\n"
"}\n"
"\n"
"/* Disabled */\n"
"QPushButton:disabled {\n"
"    background: rgba(255, 181, 71, 0.35);\n"
"    color: rgba(26, 26, 26, 0.4);\n"
"    border: 1px solid rgba(255, 213, 140, 0.25);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.refreshBtn)

        self.toolButton_image_review = QToolButton(self.centerPanel)
        self.toolButton_image_review.setObjectName(u"toolButton_image_review")
        self.toolButton_image_review.setMinimumSize(QSize(60, 25))
        self.toolButton_image_review.setMaximumSize(QSize(60, 30))
        font = QFont()
        font.setPointSize(12)
        #font.setWeight(QFont.DemiBold)
        self.toolButton_image_review.setFont(font)
        self.toolButton_image_review.setStyleSheet(u"#toolButton_image_review {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #9664ec, stop:1 #5048e6);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    font-weight: 600;\n"
"   \n"
"}\n"
"\n"
"#toolButton_image_review:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #4f46e5, stop:1 #4338ca);\n"
"}\n"
"\n"
"#toolButton_image_review:pressed {\n"
"    background: #403bb9;\n"
" \n"
"    padding-left: 13px;\n"
"}\n"
"\n"
"#toolButton_image_review:disabled {\n"
"    background: #475569;\n"
"    color: #94a3b8;\n"
"}")

        self.horizontalLayout.addWidget(self.toolButton_image_review)

        self.stopBtn = QPushButton(self.centerPanel)
        self.stopBtn.setObjectName(u"stopBtn")
        self.stopBtn.setMinimumSize(QSize(60, 0))
        self.stopBtn.setMaximumSize(QSize(60, 30))
        self.stopBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 75, 92, 0.95),    /* vibrant red  */\n"
"                                stop:1 rgba(220, 20, 60, 0.95));   /* deeper crimson */\n"
"    color: #2B0508;              /* dark text for contrast */\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgba(255, 75, 92, 0.7);\n"
"\n"
"    font-size: 13px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 95, 110, 1),\n"
"                                stop:1 rgba(240, 45, 80, 1));\n"
"    border: 1px solid rgba(255, 110, 120, 0.9);\n"
"    color: #000000;  /* strong contrast when hovered */\n"
"}\n"
"\n"
"/* Pressed */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(200, 50, 65, 0.95),\n"
"                           "
                        "     stop:1 rgba(160, 30, 45, 0.95));\n"
"    border: 1px solid rgba(200, 50, 65, 0.6);\n"
"    padding-top: 7px;     /* subtle press-down effect */\n"
"    padding-bottom: 5px;\n"
"    color: #ffffff;       /* improve visibility inside press */\n"
"}\n"
"\n"
"/* Focus (keyboard focus) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(255, 170, 180, 0.9);\n"
"}\n"
"\n"
"/* Disabled state */\n"
"QPushButton:disabled {\n"
"    background: rgba(255, 75, 92, 0.35);\n"
"    color: rgba(43, 5, 8, 0.35);\n"
"    border: 1px solid rgba(160, 20, 40, 0.25);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.stopBtn)

        self.liveModeLabel_2 = QLabel(self.centerPanel)
        self.liveModeLabel_2.setObjectName(u"liveModeLabel_2")
        self.liveModeLabel_2.setMinimumSize(QSize(100, 0))
        self.liveModeLabel_2.setMaximumSize(QSize(100, 25))
        self.liveModeLabel_2.setStyleSheet(u"font-size: 15px;\n"
"font-weight: 600;\n"
"color: #60a5fa;\n"
"padding: 4px;\n"
"background: rgba(96, 165, 250, 0.12);\n"
"border: 1px solid rgba(96, 165, 250, 0.3);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout.addWidget(self.liveModeLabel_2)

        self.toolButton_show_output_folder = QToolButton(self.centerPanel)
        self.toolButton_show_output_folder.setObjectName(u"toolButton_show_output_folder")
        self.toolButton_show_output_folder.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.toolButton_show_output_folder.setFont(font1)
        self.toolButton_show_output_folder.setStyleSheet(u"#toolButton_show_output_folder {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #f59e0b, stop:1 #d97706);\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"}\n"
"\n"
"#toolButton_show_output_folder:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #d97706, stop:1 #b45309);\n"
"}\n"
"\n"
"#toolButton_show_output_folder:pressed {\n"
"    background: #b45309;\n"
"    \n"
"    padding-left: 13px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.toolButton_show_output_folder)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.alertsTabWidget_2 = QTabWidget(self.centerPanel)
        self.alertsTabWidget_2.setObjectName(u"alertsTabWidget_2")
        self.alertsTabWidget_2.setStyleSheet(u"/* === Global Tab Widget Pane === */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #334155;\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #1e293b,\n"
"        stop:1 #0f172a\n"
"    );\n"
"    border-radius: 10px;\n"
"    margin-top: 4px;\n"
"}\n"
"\n"
"/* === Tab Styling === */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #475569,\n"
"        stop:1 #334155\n"
"    );\n"
"    color: #cbd5e1;\n"
"    padding: 4px 4px;\n"
"    margin-right: 5px;\n"
"    border-top-left-radius: 6px;\n"
"    border-top-right-radius: 6px;\n"
"    font: 10pt \"Segoe UI\";\n"
"    font-weight: 500;\n"
"    \n"
"    border: 1px solid #475569;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"/* === Selected Tab === */\n"
"QTabBar::tab:selected {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #3b82f6,\n"
"        stop:1 #1d4ed8\n"
"    );\n"
"    color: #ffffff;\n"
"    border-color:"
                        " #60a5fa;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"/* === Hover (with no selection) === */\n"
"QTabBar::tab:hover:!selected {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #143583,\n"
"        stop:1 #0c2151\n"
"    );\n"
"    color: #f1f5f9;\n"
"    border: 1px solid #18409e;\n"
"}\n"
"\n"
"/* === Remove base frame === */\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;\n"
"}\n"
"")
        self.alertsTabWidget_2.setTabPosition(QTabWidget.TabPosition.North)
        self.priceAlertsTab_2 = QWidget()
        self.priceAlertsTab_2.setObjectName(u"priceAlertsTab_2")
        self.verticalLayout_15 = QVBoxLayout(self.priceAlertsTab_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget = QWidget(self.priceAlertsTab_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(20, 29, 47);\n"
"\n"
"\n"
"    border: 1px solid #3f589e;\n"
"    border-radius: 8px;")

        self.verticalLayout_15.addWidget(self.widget)

        self.alertsTabWidget_2.addTab(self.priceAlertsTab_2, "")
        self.volumeAlertsTab_2 = QWidget()
        self.volumeAlertsTab_2.setObjectName(u"volumeAlertsTab_2")
        self.verticalLayout_16 = QVBoxLayout(self.volumeAlertsTab_2)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.marketDataGroup = QGroupBox(self.volumeAlertsTab_2)
        self.marketDataGroup.setObjectName(u"marketDataGroup")
        self.gridLayout_5 = QGridLayout(self.marketDataGroup)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.marketDataGroup)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font-weight: 600;\n"
"color: #94a3b8;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.aaplPrice_2 = QLabel(self.marketDataGroup)
        self.aaplPrice_2.setObjectName(u"aaplPrice_2")
        self.aaplPrice_2.setStyleSheet(u"color: #10b981;\n"
"font-weight: 700;\n"
"font-size: 14px;")

        self.gridLayout_5.addWidget(self.aaplPrice_2, 0, 1, 1, 1)

        self.aaplChange_2 = QLabel(self.marketDataGroup)
        self.aaplChange_2.setObjectName(u"aaplChange_2")
        self.aaplChange_2.setStyleSheet(u"color: #10b981;\n"
"font-weight: 700;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.aaplChange_2, 0, 2, 1, 1)

        self.label_4 = QLabel(self.marketDataGroup)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font-weight: 600;\n"
"color: #94a3b8;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.tslaPrice_2 = QLabel(self.marketDataGroup)
        self.tslaPrice_2.setObjectName(u"tslaPrice_2")
        self.tslaPrice_2.setStyleSheet(u"color: #ef4444;\n"
"font-weight: 700;\n"
"font-size: 14px;")

        self.gridLayout_5.addWidget(self.tslaPrice_2, 1, 1, 1, 1)

        self.tslaChange_2 = QLabel(self.marketDataGroup)
        self.tslaChange_2.setObjectName(u"tslaChange_2")
        self.tslaChange_2.setStyleSheet(u"color: #ef4444;\n"
"font-weight: 700;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.tslaChange_2, 1, 2, 1, 1)

        self.label_6 = QLabel(self.marketDataGroup)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font-weight: 600;\n"
"color: #94a3b8;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.label_6, 2, 0, 1, 1)

        self.spyPrice_2 = QLabel(self.marketDataGroup)
        self.spyPrice_2.setObjectName(u"spyPrice_2")
        self.spyPrice_2.setStyleSheet(u"color: #10b981;\n"
"font-weight: 700;\n"
"font-size: 14px;")

        self.gridLayout_5.addWidget(self.spyPrice_2, 2, 1, 1, 1)

        self.spyChange_2 = QLabel(self.marketDataGroup)
        self.spyChange_2.setObjectName(u"spyChange_2")
        self.spyChange_2.setStyleSheet(u"color: #10b981;\n"
"font-weight: 700;\n"
"font-size: 13px;")

        self.gridLayout_5.addWidget(self.spyChange_2, 2, 2, 1, 1)


        self.verticalLayout_16.addWidget(self.marketDataGroup)

        self.calendarGroup = QGroupBox(self.volumeAlertsTab_2)
        self.calendarGroup.setObjectName(u"calendarGroup")
        self.verticalLayout_9 = QVBoxLayout(self.calendarGroup)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.calendarList_3 = QListWidget(self.calendarGroup)
        QListWidgetItem(self.calendarList_3)
        QListWidgetItem(self.calendarList_3)
        QListWidgetItem(self.calendarList_3)
        QListWidgetItem(self.calendarList_3)
        self.calendarList_3.setObjectName(u"calendarList_3")
        self.calendarList_3.setStyleSheet(u"font-size: 13px;\n"
"font-weight: 500;")

        self.verticalLayout_9.addWidget(self.calendarList_3)


        self.verticalLayout_16.addWidget(self.calendarGroup)

        self.alertsTabWidget_2.addTab(self.volumeAlertsTab_2, "")
        self.newsAlertsTab_2 = QWidget()
        self.newsAlertsTab_2.setObjectName(u"newsAlertsTab_2")
        self.verticalLayout_17 = QVBoxLayout(self.newsAlertsTab_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.alertsTabWidget_2.addTab(self.newsAlertsTab_2, "")

        self.verticalLayout_6.addWidget(self.alertsTabWidget_2)

        self.tradingControlsGroup = QGroupBox(self.centerPanel)
        self.tradingControlsGroup.setObjectName(u"tradingControlsGroup")
        self.tradingControlsGroup.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.tradingControlsGroup)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.intervalLabel = QLabel(self.tradingControlsGroup)
        self.intervalLabel.setObjectName(u"intervalLabel")
        self.intervalLabel.setMaximumSize(QSize(16777215, 20))
        self.intervalLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;\n"
"padding: 4px 0px;")

        self.verticalLayout_14.addWidget(self.intervalLabel)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.radio1m = QRadioButton(self.tradingControlsGroup)
        self.radio1m.setObjectName(u"radio1m")
        self.radio1m.setMinimumSize(QSize(0, 25))
        self.radio1m.setMaximumSize(QSize(16777215, 20))
        self.radio1m.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.radio1m)

        self.radio3m = QRadioButton(self.tradingControlsGroup)
        self.radio3m.setObjectName(u"radio3m")
        self.radio3m.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.radio3m)

        self.radio5m = QRadioButton(self.tradingControlsGroup)
        self.radio5m.setObjectName(u"radio5m")
        self.radio5m.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.radio5m)

        self.radio10m = QRadioButton(self.tradingControlsGroup)
        self.radio10m.setObjectName(u"radio10m")
        self.radio10m.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.radio10m)

        self.radio15m = QRadioButton(self.tradingControlsGroup)
        self.radio15m.setObjectName(u"radio15m")
        self.radio15m.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.radio15m)

        self.radio30m = QRadioButton(self.tradingControlsGroup)
        self.radio30m.setObjectName(u"radio30m")
        self.radio30m.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_7.addWidget(self.radio30m)

        self.riskLevelLabel = QLabel(self.tradingControlsGroup)
        self.riskLevelLabel.setObjectName(u"riskLevelLabel")
        self.riskLevelLabel.setMaximumSize(QSize(72, 40))
        self.riskLevelLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;\n"
"")

        self.horizontalLayout_7.addWidget(self.riskLevelLabel)

        self.riskProgressBar = QProgressBar(self.tradingControlsGroup)
        self.riskProgressBar.setObjectName(u"riskProgressBar")
        self.riskProgressBar.setMinimumSize(QSize(0, 22))
        self.riskProgressBar.setMaximumSize(QSize(200, 22))
        self.riskProgressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid rgba(148, 163, 184, 0.3);\n"
"    border-radius: 10px;\n"
"    background: rgba(15, 23, 42, 0.6);\n"
"    color: #e2e8f0;\n"
"    font-size: 11px;\n"
"    font-weight: 500;\n"
"    text-align: center;\n"
"\n"
"    min-height: 20px;   /* Ensure minimum height */\n"
"    max-height: 20px;   /* Fix to exact height */\n"
"}\n"
"\n"
"/* Filled part of the progress bar */\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0,\n"
"        x2:1, y2:0,\n"
"        stop:0   #60a5fa,\n"
"        stop:0.5 #4c8ffb,\n"
"        stop:1   #3b82f6\n"
"    );\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.riskProgressBar.setValue(65)

        self.horizontalLayout_7.addWidget(self.riskProgressBar)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)


        self.verticalLayout_6.addWidget(self.tradingControlsGroup)


        self.horizontalLayout_4.addWidget(self.centerPanel)

        self.separator_2 = QFrame(self.centralwidget)
        self.separator_2.setObjectName(u"separator_2")
        self.separator_2.setFrameShape(QFrame.Shape.VLine)
        self.separator_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_4.addWidget(self.separator_2)

        self.rightPanel = QWidget(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.rightPanel.setMinimumSize(QSize(250, 0))
        self.rightPanel.setMaximumSize(QSize(300, 16777215))
        self.verticalLayout = QVBoxLayout(self.rightPanel)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.orderExecutionLabel_3 = QLabel(self.rightPanel)
        self.orderExecutionLabel_3.setObjectName(u"orderExecutionLabel_3")
        self.orderExecutionLabel_3.setMinimumSize(QSize(164, 0))
        self.orderExecutionLabel_3.setMaximumSize(QSize(164, 50))
        self.orderExecutionLabel_3.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 700;\n"
"color: #60a5fa;\n"
"padding: 4px;\n"
"background: rgba(96, 165, 250, 0.12);\n"
"border: 1px solid rgba(96, 165, 250, 0.3);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_10.addWidget(self.orderExecutionLabel_3)

        self.marketStatusLabel_4 = QLabel(self.rightPanel)
        self.marketStatusLabel_4.setObjectName(u"marketStatusLabel_4")
        self.marketStatusLabel_4.setMinimumSize(QSize(0, 25))
        self.marketStatusLabel_4.setMaximumSize(QSize(115, 30))
        self.marketStatusLabel_4.setStyleSheet(u"color: #42c761;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"background: rgba(16, 185, 129, 0.15);\n"
"padding: 2px 2px;\n"
"border-radius: 8px;\n"
"border: 1px solid rgba(16, 185, 129, 0.3);")

        self.horizontalLayout_10.addWidget(self.marketStatusLabel_4)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.orderFormGroup = QGroupBox(self.rightPanel)
        self.orderFormGroup.setObjectName(u"orderFormGroup")
        self.gridLayout_4 = QGridLayout(self.orderFormGroup)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.quantityInput = QLineEdit(self.orderFormGroup)
        self.quantityInput.setObjectName(u"quantityInput")
        self.quantityInput.setMaximumSize(QSize(16777215, 31))
        self.quantityInput.setStyleSheet(u"QLineEdit {\n"
"    background-color: #0f172a;\n"
"    color: #e2e8f0;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 8px;\n"
"    padding: 4px 12px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #3b82f6;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.quantityInput, 2, 1, 1, 1)

        self.orderTypeLabel = QLabel(self.orderFormGroup)
        self.orderTypeLabel.setObjectName(u"orderTypeLabel")
        self.orderTypeLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;")

        self.gridLayout_4.addWidget(self.orderTypeLabel, 1, 0, 1, 1)

        self.priceInput = QLineEdit(self.orderFormGroup)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setMaximumSize(QSize(16777215, 31))
        self.priceInput.setStyleSheet(u"QLineEdit {\n"
"    background-color: #0f172a;\n"
"    color: #e2e8f0;\n"
"    border: 1px solid #475569;\n"
"    border-radius: 8px;\n"
"    padding: 4px 12px;\n"
"    font: 11pt \"Segoe UI\";\n"
"    selection-background-color: #3b82f6;\n"
"}\n"
"")

        self.gridLayout_4.addWidget(self.priceInput, 3, 1, 1, 1)

        self.symbolComboBox = QComboBox(self.orderFormGroup)
        self.symbolComboBox.addItem("")
        self.symbolComboBox.addItem("")
        self.symbolComboBox.addItem("")
        self.symbolComboBox.addItem("")
        self.symbolComboBox.setObjectName(u"symbolComboBox")
        self.symbolComboBox.setMaximumSize(QSize(16777215, 30))
        self.symbolComboBox.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.symbolComboBox, 0, 1, 1, 1)

        self.priceLabel = QLabel(self.orderFormGroup)
        self.priceLabel.setObjectName(u"priceLabel")
        self.priceLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;")

        self.gridLayout_4.addWidget(self.priceLabel, 3, 0, 1, 1)

        self.quantityLabel = QLabel(self.orderFormGroup)
        self.quantityLabel.setObjectName(u"quantityLabel")
        self.quantityLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;")

        self.gridLayout_4.addWidget(self.quantityLabel, 2, 0, 1, 1)

        self.symbolLabel = QLabel(self.orderFormGroup)
        self.symbolLabel.setObjectName(u"symbolLabel")
        self.symbolLabel.setStyleSheet(u"font-weight: 600;\n"
"color: #cbd5e1;\n"
"font-size: 14px;")

        self.gridLayout_4.addWidget(self.symbolLabel, 0, 0, 1, 1)

        self.orderTypeComboBox = QComboBox(self.orderFormGroup)
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.addItem("")
        self.orderTypeComboBox.setObjectName(u"orderTypeComboBox")

        self.gridLayout_4.addWidget(self.orderTypeComboBox, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.orderFormGroup)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buyBtn = QPushButton(self.rightPanel)
        self.buyBtn.setObjectName(u"buyBtn")
        self.buyBtn.setMinimumSize(QSize(0, 30))
        self.buyBtn.setMaximumSize(QSize(16777215, 30))
        self.buyBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(40, 220, 130, 0.98),   /* brighter bullish green */\n"
"                                stop:1 rgba(25, 186, 104, 0.98));  /* deeper market green */\n"
"    color: #02120A;              /* dark text for clear contrast */\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgba(40, 220, 130, 0.7);\n"
"    padding: 7px 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;            /* stronger emphasis */\n"
"}\n"
"\n"
"/* Hover - more aggressive (like market opportunity) */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(60, 240, 150, 1),\n"
"                                stop:1 rgba(30, 200, 120, 1));\n"
"    border: 1px solid rgba(60, 240, 150, 0.9);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed - deep confidence, action taken */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0"
                        ", y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(20, 150, 80, 0.95),\n"
"                                stop:1 rgba(12, 128, 68, 0.95));\n"
"    border: 1px solid rgba(20, 150, 80, 0.6);\n"
"    padding-top: 8px;        /* push-down feedback */\n"
"    padding-bottom: 6px;\n"
"    color: #eafdf5;          /* slight highlight */\n"
"}\n"
"\n"
"/* Focus (keyboard, rarely used but kept for UX completeness) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(60, 255, 170, 0.9);\n"
"}\n"
"\n"
"/* Disabled state - weak, unavailable trade action */\n"
"QPushButton:disabled {\n"
"    background: rgba(40, 220, 130, 0.35);\n"
"    color: rgba(2, 18, 10, 0.3);\n"
"    border: 1px solid rgba(40, 220, 130, 0.25);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.buyBtn)

        self.sellBtn = QPushButton(self.rightPanel)
        self.sellBtn.setObjectName(u"sellBtn")
        self.sellBtn.setMinimumSize(QSize(0, 30))
        self.sellBtn.setMaximumSize(QSize(16777215, 30))
        self.sellBtn.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 70, 85, 0.98),    /* bright warning red */\n"
"                                stop:1 rgba(220, 40, 60, 0.98));   /* deeper bearish red */\n"
"    color: #2B0508;              /* deep dark for high contrast */\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgba(255, 70, 85, 0.7);\n"
"    padding: 7px 22px;\n"
"    font-size: 14px;\n"
"    font-weight: 700;\n"
"}\n"
"\n"
"/* Hover (more aggressive alert) */\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(255, 100, 115, 1),\n"
"                                stop:1 rgba(235, 65, 80, 1));\n"
"    border: 1px solid rgba(255, 120, 135, 0.9);\n"
"    color: #000000;\n"
"}\n"
"\n"
"/* Pressed (deep risk execution) */\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                stop:0 rgba(200"
                        ", 30, 45, 0.95),\n"
"                                stop:1 rgba(165, 20, 35, 0.95));\n"
"    border: 1px solid rgba(200, 30, 45, 0.6);\n"
"    padding-top: 8px;       /* subtle pressed-down effect */\n"
"    padding-bottom: 6px;\n"
"    color: #FFEAEA;         /* slight white shift for click clarity */\n"
"}\n"
"\n"
"/* Focus (keyboard) */\n"
"QPushButton:focus {\n"
"    outline: none;\n"
"    border: 1px solid rgba(255, 160, 170, 0.9);\n"
"}\n"
"\n"
"/* Disabled (action unavailable) */\n"
"QPushButton:disabled {\n"
"    background: rgba(255, 70, 85, 0.35);\n"
"    color: rgba(43, 5, 8, 0.35);\n"
"    border: 1px solid rgba(220, 40, 60, 0.25);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.sellBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.separator_3 = QFrame(self.rightPanel)
        self.separator_3.setObjectName(u"separator_3")
        self.separator_3.setFrameShape(QFrame.Shape.HLine)
        self.separator_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.separator_3)

        self.tradeHistoryLabel = QLabel(self.rightPanel)
        self.tradeHistoryLabel.setObjectName(u"tradeHistoryLabel")
        self.tradeHistoryLabel.setStyleSheet(u"font-size: 16px;\n"
"font-weight: 700;\n"
"color: #60a5fa;\n"
"padding: 4px;\n"
"background: rgba(96, 165, 250, 0.12);\n"
"border: 1px solid rgba(96, 165, 250, 0.3);\n"
"border-radius: 12px;\n"
"")

        self.verticalLayout.addWidget(self.tradeHistoryLabel)

        self.historyTable = QTableWidget(self.rightPanel)
        if (self.historyTable.columnCount() < 3):
            self.historyTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.historyTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.historyTable.rowCount() < 20):
            self.historyTable.setRowCount(20)
        self.historyTable.setObjectName(u"historyTable")
        font2 = QFont()
        self.historyTable.setFont(font2)
        self.historyTable.setStyleSheet(u"\n"
"/* === TABLE CORE STYLE (MATCHES CARD CONTAINER THEME) === */\n"
"QTableWidget {\n"
"    background: rgba(30, 41, 59, 0.7);                         /* same as QGroupBox */\n"
"    border: 1px solid rgba(148, 163, 184, 0.2);\n"
"    border-radius: 12px;\n"
"    gridline-color: rgba(148, 163, 184, 0.12);\n"
"    color: #60a5fa;\n"
"    font-size: 12px;\n"
"    selection-background-color: rgba(96, 165, 250, 0.2);\n"
"    selection-color: #60a5fa;\n"
"                             /* matches card blur */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* === TABLE HEADER (CONSISTENT WITH THEME) === */\n"
"QHeaderView::section {\n"
"    background: rgba(15, 23, 42, 0.9);                         /* same as title bg */\n"
"    color: #60a5fa;                                            /* same as title text */\n"
"    font-weight: 600;\n"
"    font-size: 11px;\n"
"    text-transform: uppercase;\n"
"    padding: 2px 6px;\n"
"    border: 1px solid rgba(96, 165, 250, 0.3);\n"
"}\n"
"\n"
"/* === HEADER EDGE RADIUS === */\n"
"QH"
                        "eaderView::section:first {\n"
"    border-top-left-radius: 12px;\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 12px;\n"
"}\n"
"\n"
"/* === TABLE CELLS === */\n"
"QTableWidget::item {\n"
"    border-bottom: 1px solid rgba(148, 163, 184, 0.08);\n"
"}\n"
"\n"
"/* Hover */\n"
"QTableWidget::item:hover:!selected {\n"
"    background: rgba(148, 163, 184, 0.08);\n"
"}\n"
"\n"
"/* Selected row */\n"
"QTableWidget::item:selected {\n"
"    background: rgba(96, 165, 250, 0.25);\n"
"    color: #60a5fa;\n"
"}\n"
"\n"
"/* === SCROLLBAR STYLE === */\n"
"QScrollBar:vertical {\n"
"    width: 8px;\n"
"    background: transparent;\n"
"    margin: 4px 0;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgba(148, 163, 184, 0.25);\n"
"    border-radius: 4px;\n"
"    min-height: 22px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: rgba(148, 163, 184, 0.35);\n"
"}\n"
"\n"
"/* === DISABLED === */\n"
"QTableWidget:disabled {\n"
"    background: rgba(30, 41, 59, 0.4);\n"
"    color:"
                        " rgba(226, 232, 240, 0.35);\n"
"    border: 1px solid rgba(148, 163, 184, 0.12);\n"
"}\n"
"\n"
"/* === REMOVE FOCUS OUTLINE === */\n"
"QTableWidget::item:focus {\n"
"    outline: none;\n"
"}\n"
"")
        self.historyTable.setRowCount(20)
        self.historyTable.setColumnCount(3)

        self.verticalLayout.addWidget(self.historyTable)

        self.performanceGroup = QGroupBox(self.rightPanel)
        self.performanceGroup.setObjectName(u"performanceGroup")
        self.horizontalLayout_8 = QHBoxLayout(self.performanceGroup)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pnlLabel = QLabel(self.performanceGroup)
        self.pnlLabel.setObjectName(u"pnlLabel")
        self.pnlLabel.setStyleSheet(u"color: #10b981;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"background: rgba(16, 185, 129, 0.15);\n"
"padding: 8px 14px;\n"
"border-radius: 8px;\n"
"border: 1px solid rgba(16, 185, 129, 0.3);")

        self.horizontalLayout_8.addWidget(self.pnlLabel)

        self.winRateLabel = QLabel(self.performanceGroup)
        self.winRateLabel.setObjectName(u"winRateLabel")
        self.winRateLabel.setStyleSheet(u"color: #60a5fa;\n"
"font-weight: 700;\n"
"font-size: 14px;\n"
"background: rgba(96, 165, 250, 0.15);\n"
"padding: 8px 14px;\n"
"border-radius: 8px;\n"
"border: 1px solid rgba(96, 165, 250, 0.3);")

        self.horizontalLayout_8.addWidget(self.winRateLabel)


        self.verticalLayout.addWidget(self.performanceGroup)


        self.horizontalLayout_4.addWidget(self.rightPanel)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1434, 34))
        self.menuBar.setMaximumSize(QSize(16777215, 40))
        self.menuBar.setStyleSheet(u"QMenuBar {\n"
"            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #1b2534, stop:0.5 #4f52bf, stop:1 #1b2534);\n"
"    color: #cbd5e1;\n"
"    font: 10pt \"Segoe UI\";\n"
"   \n"
"    border-bottom: 1px solid #334155;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent;\n"
"    padding: 6px 16px;\n"
"    margin: 2px;\n"
"    border-radius: 4px;\n"
"    color: #cbd5e1;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: #3b82f6;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background: #1d4ed8;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #1e293b;\n"
"    color: #cbd5e1;\n"
"    border: 1px solid #475569;\n"
"    padding: 8px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 6px 24px;\n"
"    background-color: transparent;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #3b82f6;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"  "
                        "  background: #475569;\n"
"    margin: 6px 8px;\n"
"}\n"
"")
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuDatabse = QMenu(self.menuBar)
        self.menuDatabse.setObjectName(u"menuDatabse")
        self.menuabout = QMenu(self.menuBar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuDatabse.menuAction())
        self.menuBar.addAction(self.menuabout.menuAction())
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionshow)
        self.menuDatabse.addAction(self.actionload)
        self.menuabout.addAction(self.actionhelp)
        self.menuabout.addAction(self.actionlicense)

        self.retranslateUi(MainWindow)

        self.alertsTabWidget.setCurrentIndex(0)
        self.alertsTabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Quantum Prime Trader Pro", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionload.setText(QCoreApplication.translate("MainWindow", u"load", None))
        self.actionshow.setText(QCoreApplication.translate("MainWindow", u"show", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"help", None))
        self.actionlicense.setText(QCoreApplication.translate("MainWindow", u"license", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.symbolInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\U0001f50d Search symbols (AAPL, TSLA, GOOGL...)", None))
        self.watchlistGroup.setTitle(QCoreApplication.translate("MainWindow", u"WATCHLIST", None))

        __sortingEnabled = self.watchlist.isSortingEnabled()
        self.watchlist.setSortingEnabled(False)
        ___qlistwidgetitem = self.watchlist.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"AAPL (Apple Inc) | $182.35 \u2197", None));
        ___qlistwidgetitem1 = self.watchlist.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TSLA (Tesla Inc) | $245.18 \u2198", None));
        ___qlistwidgetitem2 = self.watchlist.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"GOOGL (Google) | $138.21 \u2197", None));
        ___qlistwidgetitem3 = self.watchlist.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"AMZN (Amazon) | $154.65 \u2192", None));
        ___qlistwidgetitem4 = self.watchlist.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"MSFT (Microsoft) | $337.41 \u2197", None));
        self.watchlist.setSortingEnabled(__sortingEnabled)

        self.addToWatchlistBtn.setText(QCoreApplication.translate("MainWindow", u"+ Add Symbol", None))
        self.removeFromWatchlistBtn.setText(QCoreApplication.translate("MainWindow", u"\u2212 Remove", None))

        __sortingEnabled1 = self.priceAlertsList.isSortingEnabled()
        self.priceAlertsList.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.priceAlertsList.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Price above $150 (AAPL)", None));
        ___qlistwidgetitem6 = self.priceAlertsList.item(1)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Price below $240 (TSLA)", None));
        ___qlistwidgetitem7 = self.priceAlertsList.item(2)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Price target $145 (GOOGL)", None));
        self.priceAlertsList.setSortingEnabled(__sortingEnabled1)

        self.alertsTabWidget.setTabText(self.alertsTabWidget.indexOf(self.priceAlertsTab), QCoreApplication.translate("MainWindow", u"Price Alerts", None))

        __sortingEnabled2 = self.volumeAlertsList.isSortingEnabled()
        self.volumeAlertsList.setSortingEnabled(False)
        ___qlistwidgetitem8 = self.volumeAlertsList.item(0)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Volume spike (TSLA)", None));
        ___qlistwidgetitem9 = self.volumeAlertsList.item(1)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Volume spike (TSLA)", None));
        ___qlistwidgetitem10 = self.volumeAlertsList.item(2)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Unusual volume (AAPL)", None));
        self.volumeAlertsList.setSortingEnabled(__sortingEnabled2)

        self.alertsTabWidget.setTabText(self.alertsTabWidget.indexOf(self.volumeAlertsTab), QCoreApplication.translate("MainWindow", u"Volume Alerts", None))

        __sortingEnabled3 = self.newsAlertsList.isSortingEnabled()
        self.newsAlertsList.setSortingEnabled(False)
        ___qlistwidgetitem11 = self.newsAlertsList.item(0)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Earnings report (GOOGL) tomorrow", None));
        ___qlistwidgetitem12 = self.newsAlertsList.item(1)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Fed meeting today", None));
        ___qlistwidgetitem13 = self.newsAlertsList.item(2)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Product launch (AAPL) next week", None));
        self.newsAlertsList.setSortingEnabled(__sortingEnabled3)

        self.alertsTabWidget.setTabText(self.alertsTabWidget.indexOf(self.newsAlertsTab), QCoreApplication.translate("MainWindow", u"News Alerts", None))
        self.quickActions.setTitle(QCoreApplication.translate("MainWindow", u"QUICK ACTIONS", None))
        self.quickBuyBtn.setText(QCoreApplication.translate("MainWindow", u"Quick Buy", None))
        self.quickSellBtn.setText(QCoreApplication.translate("MainWindow", u"Quick Sell", None))
        self.chartBtn.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.analysisBtn.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.liveModeLabel.setText(QCoreApplication.translate("MainWindow", u"LIVE TRADING MODE", None))
        self.startBtn.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.refreshBtn.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.toolButton_image_review.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.stopBtn.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.liveModeLabel_2.setText(QCoreApplication.translate("MainWindow", u"01/12/2025", None))
#if QT_CONFIG(tooltip)
        self.toolButton_show_output_folder.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; color:#000000;\">Shortcut = CTRL+F</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_show_output_folder.setText(QCoreApplication.translate("MainWindow", u"Calendar", None))
        self.alertsTabWidget_2.setTabText(self.alertsTabWidget_2.indexOf(self.priceAlertsTab_2), QCoreApplication.translate("MainWindow", u"   Chart   ", None))
        self.marketDataGroup.setTitle(QCoreApplication.translate("MainWindow", u"REAL-TIME MARKET DATA", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"AAPL", None))
        self.aaplPrice_2.setText(QCoreApplication.translate("MainWindow", u"$182.35", None))
        self.aaplChange_2.setText(QCoreApplication.translate("MainWindow", u"+1.2%", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TSLA", None))
        self.tslaPrice_2.setText(QCoreApplication.translate("MainWindow", u"$245.18", None))
        self.tslaChange_2.setText(QCoreApplication.translate("MainWindow", u"-0.8%", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SPY", None))
        self.spyPrice_2.setText(QCoreApplication.translate("MainWindow", u"$452.67", None))
        self.spyChange_2.setText(QCoreApplication.translate("MainWindow", u"+0.5%", None))
        self.calendarGroup.setTitle(QCoreApplication.translate("MainWindow", u"ECONOMIC CALENDAR", None))

        __sortingEnabled4 = self.calendarList_3.isSortingEnabled()
        self.calendarList_3.setSortingEnabled(False)
        ___qlistwidgetitem14 = self.calendarList_3.item(0)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u25cf APPL Earnings - Today 4:30 PM", None));
        ___qlistwidgetitem15 = self.calendarList_3.item(1)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u25cf TSLA Product Launch - Tomorrow", None));
        ___qlistwidgetitem16 = self.calendarList_3.item(2)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u25cf Fed Interest Decision - Wed 2:00 PM", None));
        ___qlistwidgetitem17 = self.calendarList_3.item(3)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u25cf Trade Balance Report - Friday", None));
        self.calendarList_3.setSortingEnabled(__sortingEnabled4)

        self.alertsTabWidget_2.setTabText(self.alertsTabWidget_2.indexOf(self.volumeAlertsTab_2), QCoreApplication.translate("MainWindow", u"   Market   ", None))
        self.alertsTabWidget_2.setTabText(self.alertsTabWidget_2.indexOf(self.newsAlertsTab_2), QCoreApplication.translate("MainWindow", u"   News Alerts   ", None))
        self.tradingControlsGroup.setTitle(QCoreApplication.translate("MainWindow", u"TRADING CONTROLS", None))
        self.intervalLabel.setText(QCoreApplication.translate("MainWindow", u"Time Interval:", None))
        self.radio1m.setText(QCoreApplication.translate("MainWindow", u"1m", None))
        self.radio3m.setText(QCoreApplication.translate("MainWindow", u"3m", None))
        self.radio5m.setText(QCoreApplication.translate("MainWindow", u"5m", None))
        self.radio10m.setText(QCoreApplication.translate("MainWindow", u"10m", None))
        self.radio15m.setText(QCoreApplication.translate("MainWindow", u"15m", None))
        self.radio30m.setText(QCoreApplication.translate("MainWindow", u"30m", None))
        self.riskLevelLabel.setText(QCoreApplication.translate("MainWindow", u"Risk Level:", None))
        self.orderExecutionLabel_3.setText(QCoreApplication.translate("MainWindow", u"ORDER EXECUTION", None))
        self.marketStatusLabel_4.setText(QCoreApplication.translate("MainWindow", u"ID CONNECTED", None))
        self.orderFormGroup.setTitle(QCoreApplication.translate("MainWindow", u"NEW ORDER", None))
        self.quantityInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"100", None))
        self.orderTypeLabel.setText(QCoreApplication.translate("MainWindow", u"Order Type:", None))
        self.priceInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"182.35", None))
        self.symbolComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"AAPL", None))
        self.symbolComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"TSLA", None))
        self.symbolComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"GOGL", None))
        self.symbolComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"AMZN", None))

        self.priceLabel.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.quantityLabel.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.symbolLabel.setText(QCoreApplication.translate("MainWindow", u"Symbol:", None))
        self.orderTypeComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Market", None))
        self.orderTypeComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Limit", None))
        self.orderTypeComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Stop", None))

        self.buyBtn.setText(QCoreApplication.translate("MainWindow", u"BUY", None))
        self.sellBtn.setText(QCoreApplication.translate("MainWindow", u"SELL", None))
        self.tradeHistoryLabel.setText(QCoreApplication.translate("MainWindow", u"TRADE & ORDER HISTORY", None))
        ___qtablewidgetitem = self.historyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.historyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Filled", None));
        ___qtablewidgetitem2 = self.historyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Pending", None));
        self.performanceGroup.setTitle(QCoreApplication.translate("MainWindow", u"TODAY'S PERFORMANCE", None))
        self.pnlLabel.setText(QCoreApplication.translate("MainWindow", u"P&L: +$1,245.50", None))
        self.winRateLabel.setText(QCoreApplication.translate("MainWindow", u"Win Rate: 68%", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuDatabse.setTitle(QCoreApplication.translate("MainWindow", u"orders", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

