# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nutFPSI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_iosFps(object):
    def setupUi(self, iosFps):
        if not iosFps.objectName():
            iosFps.setObjectName(u"iosFps")
        iosFps.resize(272, 123)
        self.gridLayout_main = QGridLayout(iosFps)
        self.gridLayout_main.setObjectName(u"gridLayout_main")
        self.gridLayout_main.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_showMassag = QVBoxLayout()
        self.verticalLayout_showMassag.setObjectName(u"verticalLayout_showMassag")
        self.label_FPS = QLabel(iosFps)
        self.label_FPS.setObjectName(u"label_FPS")

        self.verticalLayout_showMassag.addWidget(self.label_FPS)

        self.label_costTime = QLabel(iosFps)
        self.label_costTime.setObjectName(u"label_costTime")

        self.verticalLayout_showMassag.addWidget(self.label_costTime)

        self.label_time = QLabel(iosFps)
        self.label_time.setObjectName(u"label_time")

        self.verticalLayout_showMassag.addWidget(self.label_time)


        self.gridLayout_main.addLayout(self.verticalLayout_showMassag, 1, 0, 1, 1)

        self.horizontalLayout_contralButton = QHBoxLayout()
        self.horizontalLayout_contralButton.setObjectName(u"horizontalLayout_contralButton")
        self.button_start = QPushButton(iosFps)
        self.button_start.setObjectName(u"button_start")

        self.horizontalLayout_contralButton.addWidget(self.button_start)

        self.button_stop = QPushButton(iosFps)
        self.button_stop.setObjectName(u"button_stop")

        self.horizontalLayout_contralButton.addWidget(self.button_stop)

        self.button_close = QPushButton(iosFps)
        self.button_close.setObjectName(u"button_close")

        self.horizontalLayout_contralButton.addWidget(self.button_close)


        self.gridLayout_main.addLayout(self.horizontalLayout_contralButton, 0, 0, 1, 1)


        self.retranslateUi(iosFps)

        QMetaObject.connectSlotsByName(iosFps)
    # setupUi

    def retranslateUi(self, iosFps):
        iosFps.setWindowTitle(QCoreApplication.translate("iosFps", u"iosFps", None))
        self.label_FPS.setText(QCoreApplication.translate("iosFps", u"FPS", None))
        self.label_costTime.setText(QCoreApplication.translate("iosFps", u"costTime", None))
        self.label_time.setText(QCoreApplication.translate("iosFps", u"time", None))
        self.button_start.setText(QCoreApplication.translate("iosFps", u"Start", None))
        self.button_stop.setText(QCoreApplication.translate("iosFps", u"Stop", None))
        self.button_close.setText(QCoreApplication.translate("iosFps", u"Close", None))
    # retranslateUi

