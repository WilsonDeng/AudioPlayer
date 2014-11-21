# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AudioPlayer.ui'
#
# Created: Fri Nov 21 21:16:43 2014
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
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget.setStyleSheet(_fromUtf8("background-image: url(:/icons/background.png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.currentLyric = QtGui.QLabel(self.widget)
        self.currentLyric.setGeometry(QtCore.QRect(10, 90, 381, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(19)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentLyric.sizePolicy().hasHeightForWidth())
        self.currentLyric.setSizePolicy(sizePolicy)
        self.currentLyric.setStyleSheet(_fromUtf8("background:transparent"))
        self.currentLyric.setLineWidth(3)
        self.currentLyric.setText(_fromUtf8(""))
        self.currentLyric.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLyric.setObjectName(_fromUtf8("currentLyric"))
        self.nextLyric = QtGui.QLabel(self.widget)
        self.nextLyric.setGeometry(QtCore.QRect(10, 120, 381, 20))
        self.nextLyric.setStyleSheet(_fromUtf8("background:transparent"))
        self.nextLyric.setText(_fromUtf8(""))
        self.nextLyric.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLyric.setObjectName(_fromUtf8("nextLyric"))
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayoutTime = QtGui.QHBoxLayout()
        self.horizontalLayoutTime.setObjectName(_fromUtf8("horizontalLayoutTime"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.verticalLayoutWidget)
        self.seekSlider.setMaximumSize(QtCore.QSize(16777215, 40))
        self.seekSlider.setStyleSheet(_fromUtf8("background-image: url(:/icons/outlook.png);"))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.horizontalLayoutTime.addWidget(self.seekSlider)
        self.timeLcd = QtGui.QLCDNumber(self.verticalLayoutWidget)
        self.timeLcd.setStyleSheet(_fromUtf8("background-image: url(:/icons/outlook.png);"))
        self.timeLcd.setObjectName(_fromUtf8("timeLcd"))
        self.horizontalLayoutTime.addWidget(self.timeLcd)
        self.verticalLayout.addLayout(self.horizontalLayoutTime)
        self.widget_3 = QtGui.QWidget(self.verticalLayoutWidget)
        self.widget_3.setStyleSheet(_fromUtf8("background-color: rgb(166, 166, 166);"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.musicName = QtGui.QLabel(self.widget_3)
        self.musicName.setGeometry(QtCore.QRect(0, 235, 399, 30))
        self.musicName.setMinimumSize(QtCore.QSize(0, 0))
        self.musicName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.musicName.setText(_fromUtf8(""))
        self.musicName.setAlignment(QtCore.Qt.AlignCenter)
        self.musicName.setObjectName(_fromUtf8("musicName"))
        self.play = QtGui.QPushButton(self.widget_3)
        self.play.setGeometry(QtCore.QRect(170, 20, 51, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play.sizePolicy().hasHeightForWidth())
        self.play.setSizePolicy(sizePolicy)
        self.play.setMinimumSize(QtCore.QSize(40, 40))
        self.play.setStyleSheet(_fromUtf8("border-image: url(:/icons/play.png);"))
        self.play.setText(_fromUtf8(""))
        self.play.setIconSize(QtCore.QSize(40, 40))
        self.play.setObjectName(_fromUtf8("play"))
        self.stop = QtGui.QPushButton(self.widget_3)
        self.stop.setGeometry(QtCore.QRect(240, 30, 31, 31))
        self.stop.setStyleSheet(_fromUtf8("border-image: url(:/icons/stop.png);"))
        self.stop.setText(_fromUtf8(""))
        self.stop.setIconSize(QtCore.QSize(30, 30))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.pause = QtGui.QPushButton(self.widget_3)
        self.pause.setGeometry(QtCore.QRect(120, 30, 31, 31))
        self.pause.setBaseSize(QtCore.QSize(30, 30))
        self.pause.setStyleSheet(_fromUtf8("border-image: url(:/icons/pause.png);"))
        self.pause.setText(_fromUtf8(""))
        self.pause.setIconSize(QtCore.QSize(30, 30))
        self.pause.setObjectName(_fromUtf8("pause"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.widget_3)
        self.volumeSlider.setGeometry(QtCore.QRect(280, 90, 114, 36))
        self.volumeSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.volumeSlider.setAutoFillBackground(False)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.lyric = QtGui.QPushButton(self.widget_3)
        self.lyric.setGeometry(QtCore.QRect(100, 100, 75, 23))
        self.lyric.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.lyric.setObjectName(_fromUtf8("lyric"))
        self.albumAndSinger = QtGui.QLabel(self.widget_3)
        self.albumAndSinger.setGeometry(QtCore.QRect(0, 266, 399, 30))
        self.albumAndSinger.setMaximumSize(QtCore.QSize(16777215, 30))
        self.albumAndSinger.setText(_fromUtf8(""))
        self.albumAndSinger.setAlignment(QtCore.Qt.AlignCenter)
        self.albumAndSinger.setObjectName(_fromUtf8("albumAndSinger"))
        self.list = QtGui.QPushButton(self.widget_3)
        self.list.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.list.setStyleSheet(_fromUtf8("background-color: rgb(170, 170, 127);"))
        self.list.setObjectName(_fromUtf8("list"))
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 12)
        AudioPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(AudioPlayer)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayer)

    def retranslateUi(self, AudioPlayer):
        AudioPlayer.setWindowTitle(_translate("AudioPlayer", "MainWindow", None))
        self.lyric.setText(_translate("AudioPlayer", "歌词", None))
        self.list.setText(_translate("AudioPlayer", "播放列表", None))

from PyQt4 import phonon
import buttonIcon_rc
