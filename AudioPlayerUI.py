# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Audioplayer.ui'
#
# Created: Sat Nov 22 20:35:03 2014
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
        self.widget.setStyleSheet(_fromUtf8(""))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_3 = QtGui.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(0, 260, 399, 141))
        self.widget_3.setStyleSheet(_fromUtf8("border-image: url(:/icons/1.png);"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.musicName = QtGui.QLabel(self.widget_3)
        self.musicName.setGeometry(QtCore.QRect(0, 235, 399, 30))
        self.musicName.setMinimumSize(QtCore.QSize(0, 0))
        self.musicName.setMaximumSize(QtCore.QSize(16777215, 30))
        self.musicName.setText(_fromUtf8(""))
        self.musicName.setAlignment(QtCore.Qt.AlignCenter)
        self.musicName.setObjectName(_fromUtf8("musicName"))
        self.play = QtGui.QPushButton(self.widget_3)
        self.play.setGeometry(QtCore.QRect(130, 40, 48, 48))
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
        self.stop.setGeometry(QtCore.QRect(200, 40, 50, 50))
        self.stop.setStyleSheet(_fromUtf8("border-image: url(:/icons/stop.png);"))
        self.stop.setText(_fromUtf8(""))
        self.stop.setIconSize(QtCore.QSize(30, 30))
        self.stop.setObjectName(_fromUtf8("stop"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.widget_3)
        self.volumeSlider.setGeometry(QtCore.QRect(270, 100, 114, 36))
        self.volumeSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.volumeSlider.setAutoFillBackground(False)
        self.volumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.lyric = QtGui.QPushButton(self.widget_3)
        self.lyric.setGeometry(QtCore.QRect(70, 110, 51, 23))
        self.lyric.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))
        self.lyric.setObjectName(_fromUtf8("lyric"))
        self.albumAndSinger = QtGui.QLabel(self.widget_3)
        self.albumAndSinger.setGeometry(QtCore.QRect(0, 266, 399, 30))
        self.albumAndSinger.setMaximumSize(QtCore.QSize(16777215, 30))
        self.albumAndSinger.setText(_fromUtf8(""))
        self.albumAndSinger.setAlignment(QtCore.Qt.AlignCenter)
        self.albumAndSinger.setObjectName(_fromUtf8("albumAndSinger"))
        self.prev = QtGui.QPushButton(self.widget_3)
        self.prev.setGeometry(QtCore.QRect(60, 40, 50, 50))
        self.prev.setStyleSheet(_fromUtf8("border-image: url(:/icons/prev.png);"))
        self.prev.setText(_fromUtf8(""))
        self.prev.setObjectName(_fromUtf8("prev"))
        self.next = QtGui.QPushButton(self.widget_3)
        self.next.setGeometry(QtCore.QRect(270, 40, 50, 50))
        self.next.setStyleSheet(_fromUtf8("border-image: url(:/icons/next.png);"))
        self.next.setText(_fromUtf8(""))
        self.next.setObjectName(_fromUtf8("next"))
        self.timeLcd = QtGui.QLCDNumber(self.widget_3)
        self.timeLcd.setGeometry(QtCore.QRect(330, 0, 64, 32))
        self.timeLcd.setStyleSheet(_fromUtf8("border-image: url(:/icons/1.png);"))
        self.timeLcd.setObjectName(_fromUtf8("timeLcd"))
        self.seekSlider = phonon.Phonon.SeekSlider(self.widget_3)
        self.seekSlider.setGeometry(QtCore.QRect(0, 0, 327, 32))
        self.seekSlider.setMaximumSize(QtCore.QSize(16777215, 40))
        self.seekSlider.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.seekSlider.setStyleSheet(_fromUtf8(""))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.list = QtGui.QPushButton(self.widget_3)
        self.list.setGeometry(QtCore.QRect(10, 110, 51, 23))
        self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))
        self.list.setObjectName(_fromUtf8("list"))
        self.widget_2 = QtGui.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(-1, 0, 401, 261))
        self.widget_2.setStyleSheet(_fromUtf8("border-image: url(:/icons/background.png);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.nextLyric = QtGui.QLabel(self.widget_2)
        self.nextLyric.setGeometry(QtCore.QRect(0, 160, 401, 21))
        self.nextLyric.setStyleSheet(_fromUtf8("border-image: transparent"))
        self.nextLyric.setText(_fromUtf8(""))
        self.nextLyric.setAlignment(QtCore.Qt.AlignCenter)
        self.nextLyric.setObjectName(_fromUtf8("nextLyric"))
        self.currentLyric = QtGui.QLabel(self.widget_2)
        self.currentLyric.setGeometry(QtCore.QRect(0, 130, 401, 21))
        self.currentLyric.setStyleSheet(_fromUtf8("border-image: transparent"))
        self.currentLyric.setText(_fromUtf8(""))
        self.currentLyric.setAlignment(QtCore.Qt.AlignCenter)
        self.currentLyric.setObjectName(_fromUtf8("currentLyric"))
        self.verticalLayout.addWidget(self.widget)
        AudioPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(AudioPlayer)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayer)

    def retranslateUi(self, AudioPlayer):
        AudioPlayer.setWindowTitle(_translate("AudioPlayer", "MainWindow", None))
        self.lyric.setText(_translate("AudioPlayer", "歌词", None))
        self.list.setText(_translate("AudioPlayer", "列表", None))

from PyQt4 import phonon
import buttonIcon_rc
