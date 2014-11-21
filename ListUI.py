# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List.ui'
#
# Created: Fri Nov 21 21:16:49 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_musicList(object):
    def setupUi(self, musicList):
        musicList.setObjectName(_fromUtf8("musicList"))
        musicList.resize(400, 400)
        musicList.setMinimumSize(QtCore.QSize(400, 400))
        musicList.setMaximumSize(QtCore.QSize(400, 400))
        self.verticalLayoutWidget = QtGui.QWidget(musicList)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.musicTable = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.musicTable.setGridStyle(QtCore.Qt.SolidLine)
        self.musicTable.setCornerButtonEnabled(True)
        self.musicTable.setColumnCount(3)
        self.musicTable.setObjectName(_fromUtf8("musicTable"))
        self.musicTable.setRowCount(0)
        self.musicTable.horizontalHeader().setVisible(True)
        self.musicTable.horizontalHeader().setDefaultSectionSize(127)
        self.musicTable.horizontalHeader().setMinimumSectionSize(127)
        self.musicTable.horizontalHeader().setSortIndicatorShown(False)
        self.musicTable.horizontalHeader().setStretchLastSection(True)
        self.musicTable.verticalHeader().setVisible(True)
        self.musicTable.verticalHeader().setDefaultSectionSize(30)
        self.musicTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.musicTable)
        self.widget = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget.setStyleSheet(_fromUtf8("background-color: rgb(166, 166, 166);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.deleteButton = QtGui.QPushButton(self.widget)
        self.deleteButton.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.deleteButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.addButton = QtGui.QPushButton(self.widget)
        self.addButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.addButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.modeButton = QtGui.QPushButton(self.widget)
        self.modeButton.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.modeButton.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.modeButton.setObjectName(_fromUtf8("modeButton"))
        self.verticalLayout.addWidget(self.widget)
        self.verticalLayout.setStretch(0, 8)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(musicList)
        QtCore.QMetaObject.connectSlotsByName(musicList)

    def retranslateUi(self, musicList):
        musicList.setWindowTitle(_translate("musicList", "Form", None))
        self.deleteButton.setText(_translate("musicList", "删除", None))
        self.addButton.setText(_translate("musicList", "添加", None))
        self.modeButton.setText(_translate("musicList", "mode", None))

