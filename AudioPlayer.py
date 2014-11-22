# -*- coding: utf-8 -*-
import sip, sys, time, thread
reload(sys)
sys.setdefaultencoding('utf-8')

sip.setapi('QString', 2)
import random
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from AudioPlayerUI import Ui_AudioPlayer
from ListUI import Ui_musicList


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class music_player(QtGui.QMainWindow, Ui_AudioPlayer):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.setupUi(self)

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)

        self.mediaObject.setTickInterval(200)
        self.mediaObject.tick.connect(self.tick)

        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
        self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)

        Phonon.createPath(self.mediaObject, self.audioOutput)

        # self.setupActions()
        self.list.clicked.connect(self.showList)
        self.play.clicked.connect(self.clickPlay)
        self.stop.clicked.connect(self.mediaObject.stop)

        self.timeLcd.display("00:00")
        self.seekSlider.setMediaObject(self.mediaObject)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        # self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum,
        #         QtGui.QSizePolicy.Maximum)


        self.sources = []  #播放文件列表
        self.info = []

        self.Form1 = QtGui.QDialog()
        self.ListUI = Ui_musicList()
        self.ListUI.setupUi(self.Form1)
        self.ListUI.addButton.clicked.connect(self.addFiles)
        self.ListUI.deleteButton.clicked.connect(self.removeMusic)
        # self.ListUI.musicTable.cellClicked.connect(self.tableClicked)
        # self.ListUI.musicTable.cellDoubleClicked.connect(self.tableClicked)
        self.ListUI.musicTable.cellPressed.connect(self.tableClicked)
        headers = ("Title", "Artist", "Time")
        self.ListUI.musicTable.setHorizontalHeaderLabels(headers)

        self.playModes = [u'顺序播放', u'随机播放', u'单曲循环']
        self.playmode = u'顺序播放'
        self.ListUI.modeButton.setText(u'顺序播放')
        self.ListUI.modeButton.clicked.connect(self.changeMode)


        ft1 = QtGui.QFont()
        ft1.setPointSize(10)

        pa1 = QtGui.QPalette()
        pa1.setColor(QtGui.QPalette.WindowText, QtGui.QColor(162, 208, 255))
        self.nextLyric.setFont(ft1)
        self.nextLyric.setPalette(pa1)

        ft2 = QtGui.QFont()
        ft2.setPointSize(12)
        ft2.setBold(True)
        pa2 = QtGui.QPalette()
        pa2.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 255))
        self.currentLyric.setFont(ft2)
        self.currentLyric.setPalette(pa2)

        self.showlyric = True

        self.lyric.clicked.connect(self.setLyric)

    def showList(self):

        self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/on.png);"))


        if not self.Form1.isHidden():
            self.Form1.hide()
            return
        x = self.pos().x()
        y = self.pos().y()
        self.Form1.move(x - 415, y)
        self.Form1.show()
        self.Form1.exec_()

        self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))


    def addFiles(self):

        self.ListUI.addButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/on.png);"))
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                                                   'music')
        if not files:
            return
        index = len(self.sources)
        for string in files:  # 同时添加多个文件时的处理
            self.sources.append(Phonon.MediaSource(string))
        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])
        self.ListUI.addButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))


    def removeMusic(self):
        seletedRows = self.ListUI.musicTable.selectedItems()
        a = set()
        for widget in seletedRows:
            r = widget.row()
            a.add(r)
        index = self.sources.index(self.mediaObject.currentSource())
        if index in a:
            self.mediaObject.stop()
        l = list(a)
        l.reverse()
        for r in l:
            print r
            self.ListUI.musicTable.removeRow(r)
            self.sources.remove(self.sources[r])
            self.info.remove(self.info[r])


    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                                      self.metaInformationResolver.errorString())

            while self.sources and self.sources.pop() != self.metaInformationResolver.currentSource():
                pass

            return

        if newState != Phonon.StoppedState and newState != Phonon.PausedState:
            return

        if self.metaInformationResolver.currentSource().type() == Phonon.MediaSource.Invalid:
            return

        metaData = self.metaInformationResolver.metaData()

        title = metaData.get('TITLE', [''])[0]
        # if title[0] == '\\':
        #     title = title.encode('raw_unicode_escape').decode('gbk')
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()

        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict = dict(TITLE=title)

        artist = metaData.get('ARTIST', [''])[0]
        # artist = artist.encode('raw_unicode_escape').decode('gbk')
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(ARTIST=artist)

        totaltime = self.metaInformationResolver.totalTime()
        displayTime = unicode((totaltime / 60000) % 60) + ':' + unicode((totaltime / 1000) % 60)
        timeItem = QtGui.QTableWidgetItem(displayTime)
        timeItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(Time=totaltime)

        fileName = self.metaInformationResolver.currentSource().fileName().split('/')[-1]
        fileName = fileName[:fileName.rfind('.')]
        lyricName = fileName + '.lrc'
        path = 'music\\' + lyricName
        try:
            with open(path, 'r+') as f:
                lyricText = f.read()
        except IOError:
            lyricText = []
        mdict.update(LYRIC=lyricText)

        self.info.append(mdict)
        currentRow = self.ListUI.musicTable.rowCount()  # 显示音频信息
        self.ListUI.musicTable.insertRow(currentRow)
        self.ListUI.musicTable.setItem(currentRow, 0, titleItem)
        self.ListUI.musicTable.setItem(currentRow, 1, artistItem)
        self.ListUI.musicTable.setItem(currentRow, 2, timeItem)

        if not self.ListUI.musicTable.selectedItems():
            self.ListUI.musicTable.selectRow(0)
            self.mediaObject.setCurrentSource(self.metaInformationResolver.currentSource())



        index = self.sources.index(self.metaInformationResolver.currentSource()) + 1

        if len(self.sources) > index:
            self.metaInformationResolver.setCurrentSource(self.sources[index])  # 解析下一首歌的信息
        else:
            self.ListUI.musicTable.resizeColumnsToContents()
            if self.ListUI.musicTable.columnWidth(0) > 300:
                self.ListUI.musicTable.setColumnWidth(0, 300)


    def stateChanged(self, newState, oldState):  # 根据播放状态改变不同按键的状态
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                                          self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                                          self.mediaObject.errorString())

        elif newState == Phonon.PlayingState:
            self.stop.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.stop.setEnabled(False)
            self.play.setEnabled(True)
            self.timeLcd.display("00:00")

        elif newState == Phonon.PausedState:
            self.stop.setEnabled(True)
            self.play.setEnabled(True)


    def clickPlay(self):

        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.pause()
            self.play.setStyleSheet(_fromUtf8("border-image: url(:/icons/play.png);"))
            self.play.setGeometry(QtCore.QRect(130, 40, 48, 48))
        else:
            self.mediaObject.play()
            self.play.setStyleSheet(_fromUtf8("border-image: url(:/icons/pause.png);"))
            self.play.setGeometry(QtCore.QRect(128, 40, 50, 50))




    def showTitle(self):
        index = self.sources.index(self.mediaObject.currentSource())
        ft = QtGui.QFont()
        ft.setPointSize(14)
        ft.setBold(True)
        self.musicName.setFont(ft)
        self.musicName.setText(self.info[index].get('TITLE'))
        self.albumAndSinger.setText(self.info[index].get('ARTIST'))


    def sourceChanged(self, source):
        index = 0
        while index < len(self.sources) and self.sources[index] != source:
            index += 1
        self.ListUI.musicTable.selectRow(index)
        self.timeLcd.display('00:00')
        self.showTitle()



    def aboutToFinish(self):
        currentIndex = self.sources.index(self.mediaObject.currentSource())
        if self.playmode == u'顺序播放':
            index = currentIndex + 1
        elif self.playmode == u'随机播放':
            index = random.randint(0, len(self.sources) - 1)
            while index == currentIndex:
                index = random.randint(0, len(self.sources) - 1)
        elif self.playmode == u'单曲循环':
            index = currentIndex
        if index >= len(self.sources):
            index = 0
        self.mediaObject.enqueue(self.sources[index])  # enqueue动作触发currentSourceChanged信号


    def tick(self, time):  # 显示播放时间
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))
        self.showLyric(time)

    def tableClicked(self, row, column):  # 点击音频列表时的反应

        self.mediaObject.stop()
        self.mediaObject.clearQueue()

        self.mediaObject.setCurrentSource(self.sources[row])

        self.showTitle()
        self.mediaObject.play()


    def showLyric(self, currentTime):
        if not self.showlyric:
            return
        if self.mediaObject.state() != Phonon.PlayingState:
            return
        index = self.sources.index(self.mediaObject.currentSource())
        lyricText = self.info[index].get('LYRIC')
        if lyricText:
            lines = lyricText.split('\n')

            startline = 0
            while lines[startline][1:3] != '00':
                startline += 1

            line = startline
            while line < len(lines) and self.getTime(lines[line]) < currentTime:
                line += 1
            try:
                currentLyric = lines[line-1][11:].decode('gbk')
            except UnicodeDecodeError:
                currentLyric = lines[line-1][11:]
            self.currentLyric.setText(currentLyric)

            if line+1 < len(lines):
                try:
                    nextLyric = lines[line][11:].decode('gbk')
                except UnicodeDecodeError:
                    nextLyric = lines[line][11:]
            else:
                nextLyric = ''
            self.nextLyric.setText(nextLyric)




    def getTime(self, s):
        lyricTime = ( int(s[1:3]) * 60 + int(s[4:6])
                              + float(s[7:9]) / 100 ) * 1000
        return lyricTime


    def changeMode(self):
        if self.playmode == u'顺序播放':
            playmode = u'随机播放'
            self.ListUI.modeButton.setText(u'随机播放')
        elif self.playmode == u'随机播放':
            playmode = u'单曲循环'
            self.ListUI.modeButton.setText(u'单曲循环')
        elif self.playmode == u'单曲循环':
            playmode = u'顺序播放'
            self.ListUI.modeButton.setText(u'顺序播放')
        self.playmode = playmode


    def setLyric(self):
        if self.showlyric:
            self.showlyric = False
            self.lyric.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))
            self.currentLyric.setText('')
            self.nextLyric.setText('')
        else:
            self.showlyric = True
            self.lyric.setStyleSheet(_fromUtf8("border-image: url(:/icons/on.png);"))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Music Player")
    app.setQuitOnLastWindowClosed(True)

    window = music_player()
    window.show()

    sys.exit(app.exec_())
