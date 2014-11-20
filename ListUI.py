# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'List.ui'
#
# Created: Thu Nov 20 21:29:01 2014
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
        headers = ("Title", "Artist", "Time")
        self.musicTable.setHorizontalHeaderLabels(headers)
        self.musicTable.verticalHeader().setVisible(True)
        self.musicTable.verticalHeader().setDefaultSectionSize(30)
        self.verticalLayout.addWidget(self.musicTable)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.addButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.horizontalLayout.addWidget(self.addButton)
        self.deleteButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.horizontalLayout.addWidget(self.deleteButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(musicList)
        QtCore.QMetaObject.connectSlotsByName(musicList)

    def retranslateUi(self, musicList):
        musicList.setWindowTitle(_translate("musicList", "Form", None))
        self.addButton.setText(_translate("musicList", "Add", None))
        self.deleteButton.setText(_translate("musicList", "Delete", None))

