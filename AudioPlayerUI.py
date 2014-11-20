# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioPlayer.ui'
#
# Created: Thu Nov 20 16:36:49 2014
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

class Ui_AudioPlayer(object):
    def setupUi(self, AudioPlayer):
        AudioPlayer.setObjectName(_fromUtf8("AudioPlayer"))
        AudioPlayer.resize(400, 400)
        AudioPlayer.setMinimumSize(QtCore.QSize(400, 400))
        AudioPlayer.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtGui.QWidget(AudioPlayer)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.albumPic = QtGui.QLabel(self.verticalLayoutWidget)
        self.albumPic.setMinimumSize(QtCore.QSize(0, 200))
        self.albumPic.setBaseSize(QtCore.QSize(0, 500))
        self.albumPic.setText(_fromUtf8(""))
        self.albumPic.setObjectName(_fromUtf8("albumPic"))
        self.verticalLayout.addWidget(self.albumPic)
        self.horizontalLayoutTime = QtGui.QHBoxLayout()
        self.horizontalLayoutTime.setObjectName(_fromUtf8("horizontalLayoutTime"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.verticalLayoutWidget)
        self.seekSlider.setMaximumSize(QtCore.QSize(16777215, 40))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayoutTime.addWidget(self.seekSlider)
        self.timeLcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.timeLcd.setObjectName(_fromUtf8("timeLcd"))
        self.horizontalLayoutTime.addWidget(self.timeLcd)
        self.verticalLayout.addLayout(self.horizontalLayoutTime)
        self.musicName = QtGui.QLabel(self.verticalLayoutWidget)
        self.musicName.setMinimumSize(QtCore.QSize(0, 0))
        self.musicName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.musicName.setText(_fromUtf8(""))
        self.musicName.setAlignment(QtCore.Qt.AlignCenter)
        self.musicName.setObjectName(_fromUtf8("musicName"))
        self.verticalLayout.addWidget(self.musicName)
        self.albumAndSinger = QtGui.QLabel(self.verticalLayoutWidget)
        self.albumAndSinger.setMaximumSize(QtCore.QSize(16777215, 30))
        self.albumAndSinger.setText(_fromUtf8(""))
        self.albumAndSinger.setAlignment(QtCore.Qt.AlignCenter)
        self.albumAndSinger.setObjectName(_fromUtf8("albumAndSinger"))
        self.verticalLayout.addWidget(self.albumAndSinger)
        self.horizontalLayoutControl = QtGui.QHBoxLayout()
        self.horizontalLayoutControl.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayoutControl.setObjectName(_fromUtf8("horizontalLayoutControl"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutControl.addItem(spacerItem)
        self.play = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setObjectName(_fromUtf8("play"))
        self.horizontalLayoutControl.addWidget(self.play)
        self.pause = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pause.setBaseSize(QtCore.QSize(30, 30))
        self.pause.setObjectName(_fromUtf8("pause"))
        self.horizontalLayoutControl.addWidget(self.pause)
        self.stop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.stop.setObjectName(_fromUtf8("stop"))
        self.horizontalLayoutControl.addWidget(self.stop)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutControl.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayoutControl)
        self.horizontalLayoutOption = QtGui.QHBoxLayout()
        self.horizontalLayoutOption.setObjectName(_fromUtf8("horizontalLayoutOption"))
        self.list = QtGui.QPushButton(self.verticalLayoutWidget)
        self.list.setObjectName(_fromUtf8("list"))
        self.horizontalLayoutOption.addWidget(self.list)
        self.lyric = QtGui.QPushButton(self.verticalLayoutWidget)
        self.lyric.setObjectName(_fromUtf8("lyric"))
        self.horizontalLayoutOption.addWidget(self.lyric)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayoutOption.addItem(spacerItem2)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.verticalLayoutWidget)
        self.volumeSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.volumeSlider.setAutoFillBackground(False)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayoutOption.addWidget(self.volumeSlider)
        self.verticalLayout.addLayout(self.horizontalLayoutOption)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 6)
        self.verticalLayout.setStretch(3, 6)
        self.verticalLayout.setStretch(4, 8)
        self.verticalLayout.setStretch(5, 4)
        AudioPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(AudioPlayer)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayer)

    def retranslateUi(self, AudioPlayer):
        AudioPlayer.setWindowTitle(_translate("AudioPlayer", "MainWindow", None))
        self.play.setText(_translate("AudioPlayer", "play", None))
        self.pause.setText(_translate("AudioPlayer", "pause", None))
        self.stop.setText(_translate("AudioPlayer", "stop", None))
        self.list.setText(_translate("AudioPlayer", "list", None))
        self.lyric.setText(_translate("AudioPlayer", "lyric", None))

from PyQt4 import phonon
