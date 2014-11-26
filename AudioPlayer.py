# -*- coding: utf-8 -*-
import sip, sys
reload(sys)
sys.setdefaultencoding('utf-8')

sip.setapi('QString', 2)
import random, urllib, json, os
from PyQt4 import QtGui, QtCore, Qt
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

        self.listWindow = ListForm()
        self.ListUI = Ui_musicList()
        self.ListUI.setupUi(self.listWindow)
        self.ListUI.addButton.clicked.connect(self.addFiles)
        self.ListUI.deleteButton.clicked.connect(self.removeMusic)
        self.ListUI.musicTable.cellDoubleClicked.connect(self.tableClicked)
        headers = ("Title", "Artist", "Time")
        self.ListUI.musicTable.setHorizontalHeaderLabels(headers)
        self.ListUI.musicTable.setFrameShape(QtGui.QFrame.WinPanel)
        self.ListUI.musicTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.ListUI.musicTable.setAlternatingRowColors(True)


        self.list.clicked.connect(self.showList)
        self.playButton.clicked.connect(self.clickPlay)
        self.stopButton.clicked.connect(self.clickStop)
        self.nextButton.clicked.connect(self.nextSong)
        self.prevButton.clicked.connect(self.lastSong)
        self.closeButton.clicked.connect(app.exit)
        self.minimizeButton.clicked.connect(self.minimizeWindow)


        self.timeLcd.display("00:00")
        self.seekSlider.setMediaObject(self.mediaObject)
        self.volumeSlider.setAudioOutput(self.audioOutput)


        self.sources = []  #播放文件列表
        self.info = []
        self.filePath = 'music'
        self.isAboutToFinish = False


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

        self.dPos = Qt.QPoint()
        self.mousePos = Qt.QPoint()
        self.windowPos = Qt.QPoint()

        self.qm = QtGui.QBitmap(self.centralwidget.size())
        self.qm.fill()
        self.qp = QtGui.QPainter(self.qm)
        self.qp.setPen(Qt.Qt.black)
        self.qp.setBrush(Qt.Qt.black)
        self.qp.drawRoundedRect(self.qm.rect(), 15, 15)
        self.setMask(self.qm)


        self.widget_2.setAutoFillBackground(True)
        self.pa3 = QtGui.QPalette()
        self.pm = QtGui.QPixmap("C:\Users\Public\Pictures\Sample Pictures\考拉.jpg")
        self.pa3.setBrush(QtGui.QPalette.Window, QtGui.QBrush(self.pm))
        self.widget_2.setPalette(self.pa3)
        self.widget_2.show()


    def showList(self):
        if not self.listWindow.isHidden():
            self.listWindow.hide()
            self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/list_off.png);"))
            return
        x = self.pos().x()
        y = self.pos().y()
        self.listWindow.move(x - 401, y)
        self.listWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.listWindow.show()
        self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/list_on.png);"))


    def addFiles(self):

        self.ListUI.addButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/on.png);"))
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                                                   self.filePath)
        if not files:
            return
        index = len(self.sources)
        for string in files:  # 同时添加多个文件时的处理
            self.sources.append(Phonon.MediaSource(string))
        self.filePath = string[:string.rfind(u'\\')]
        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])
        self.ListUI.addButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/off.png);"))


    def removeMusic(self):
        seletedRows = self.ListUI.musicTable.selectedItems()
        if not seletedRows:
            return
        a = set()
        for widget in seletedRows:
            r = widget.row()
            a.add(r)
        index = self.sources.index(self.mediaObject.currentSource())
        if index in a:
            self.mediaObject.stop()
            self.currentLyric.setText('')
            self.nextLyric.setText('')
        l = list(a)
        l.reverse()
        for r in l:
            print r
            self.ListUI.musicTable.removeRow(r)
            self.sources.remove(self.sources[r])
            self.info.remove(self.info[r])


    def metaStateChanged(self, newState, oldState):
        a = newState
        b = oldState
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                                      self.metaInformationResolver.errorString())
            while self.sources and self.sources.pop() != self.metaInformationResolver.currentSource():
                pass                          # 把错误格式的文件及其后面的文件都移除掉
            return

        if newState != Phonon.StoppedState and newState != Phonon.PausedState:
            return

        if self.metaInformationResolver.currentSource().type() == Phonon.MediaSource.Invalid:
            return

        metaData = self.metaInformationResolver.metaData()

        title = metaData.get('TITLE', [''])[0]
        title = self.decodeGBK(title)
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()

        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict = dict(TITLE=title)

        artist = metaData.get('ARTIST', [''])[0]
        artist = self.decodeGBK(artist)
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(ARTIST=artist)

        totaltime = self.metaInformationResolver.totalTime()
        displayTime = unicode((totaltime / 60000) % 60) + ':' + unicode((totaltime / 1000) % 60)
        timeItem = QtGui.QTableWidgetItem(displayTime)
        timeItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(Time=totaltime)

        file = self.metaInformationResolver.currentSource().fileName()
        fileName = file.split('/')[-1]
        fileName = fileName[:fileName.rfind('.')]
        lyricName = fileName + '.lrc'
        path = file[:file.rfind('/')]
        lyric = path + '/' + lyricName
        musicInfo = self.getLyricAndCover(artist, title)
        if os.path.exists(lyric):
            f = open(lyric, 'r+')
            lyricText = f.read()
            f.close()
        elif musicInfo:
            f = urllib.urlopen(musicInfo.get('lrc'))
            lyricText = f.read().replace('\r', '')
            fw = open(lyric, 'w')
            fw.write(lyricText)
            fw.close()
            f.close()
        else:
            lyricText = ''
        mdict.update(LYRIC=lyricText)

        # coverUrl = u'http://geci.me/api/cover/' + unicode(musicInfo.get('aid'))
        # coverfile = urllib.urlopen(coverUrl)
        # if coverfile.get('count') != 0:
        #     picUrl = coverfile.get('result').get('cover')
        # data = urllib.urlopen(picUrl)
        # cover = open(fileName+'.bng', 'wb')
        # cover.write(data.read)
        # data.close()
        # cover.close()



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
            self.stopButton.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.stopButton.setEnabled(False)
            self.playButton.setEnabled(True)
            self.timeLcd.display("00:00")

        elif newState == Phonon.PausedState:
            self.stopButton.setEnabled(True)
            self.playButton.setEnabled(True)


    def clickPlay(self):
        if not self.sources:
            return
        if self.mediaObject.state() == Phonon.PlayingState:
            self.mediaObject.pause()
            self.playButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/play.png);"))
            self.playButton.setGeometry(QtCore.QRect(130, 40, 48, 48))
        else:
            self.mediaObject.play()
            self.playButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/pause.png);"))
            self.playButton.setGeometry(QtCore.QRect(128, 40, 50, 50))

    def clickStop(self):
        self.mediaObject.stop()
        self.currentLyric.setText('')
        self.nextLyric.setText('')
        self.playButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/play.png);"))




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
        self.isAboutToFinish = False



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
        if index < len(self.sources):
            self.mediaObject.enqueue(self.sources[index])  # enqueue动作触发currentSourceChanged信号
        else:
            self.mediaObject.stop()
        self.isAboutToFinish = True


    def tick(self, time):  # 显示播放时间
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))
        if self.mediaObject.state() == Phonon.PlayingState and self.mediaObject.currentSource() in self.sources:
            self.showLyric(time)

    def tableClicked(self, row, column):  # 点击音频列表时的反应

        self.currentLyric.setText('')
        self.nextLyric.setText('')
        self.mediaObject.stop()
        self.mediaObject.clearQueue()

        self.mediaObject.setCurrentSource(self.sources[row])

        self.showTitle()
        self.mediaObject.play()
        self.playButton.setStyleSheet(_fromUtf8("border-image: url(:/icons/pause.png);"))
        self.playButton.setGeometry(QtCore.QRect(128, 40, 50, 50))

    def showLyric(self, currentTime):
        if not self.showlyric:
            return
        if self.isAboutToFinish:
            self.currentLyric.setText('')
            return


        index = self.sources.index(self.mediaObject.currentSource())

        lyricText = self.info[index].get('LYRIC')
        if lyricText:
            lines = lyricText.split('\n')
            while '' in lines:
                lines.remove('')
            startline = 0
            while lines[startline][1:3] != '00':
                startline += 1

            line = startline
            seperateIndex = lines[line].find(']')
            if currentTime < self.getTime(lines[startline], seperateIndex):       # 前奏时暂不显示歌词
                return
            while line+1 < len(lines) and self.getTime(lines[line], seperateIndex) < currentTime:
                line += 1
            if line+1 < len(lines) or self.getTime(lines[line], seperateIndex) > currentTime:
                try:
                    currentLyric = lines[line-1][seperateIndex+1:].strip(' ').decode('gbk')
                    nextLyric = lines[line][seperateIndex+1:].strip(' ').decode('gbk')
                except UnicodeDecodeError:
                    currentLyric = lines[line-1][seperateIndex+1:].strip(' ').decode('utf-8')
                    nextLyric = lines[line][seperateIndex+1:].strip(' ').decode('utf-8')
            else:
                try:
                    currentLyric = lines[line][seperateIndex+1:].strip(' ').decode('gbk')
                except UnicodeDecodeError:
                    currentLyric = lines[line][seperateIndex+1:].strip(' ')
                nextLyric = ''
            self.currentLyric.setText(currentLyric)
            self.nextLyric.setText(nextLyric)




    def getTime(self, s, index):
        if index == 9:
            lyricTime = ( int(s[1:3]) * 60 + int(s[4:6])
                              + float(s[7:9]) / 100 ) * 1000
        elif index == 6:
            lyricTime = ( int(s[1:3]) * 60 + int(s[4:6])) * 1000

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
            self.lyric.setStyleSheet(_fromUtf8("border-image: url(:/icons/lyric_off.png);"))
            self.currentLyric.setText('')
            self.nextLyric.setText('')
        else:
            self.showlyric = True
            self.lyric.setStyleSheet(_fromUtf8("border-image: url(:/icons/lyric_on.png);"))


    def decodeGBK(self, s):
        try:
            s.encode('gbk')
        except UnicodeEncodeError:
            return s.encode('raw_unicode_escape').decode('gbk')
        else:
            return s


    def mousePressEvent(self, event=Qt.QMouseEvent):
        self.windowPos = self.pos()
        self.mousePos = event.globalPos()
        self.dPos = self.mousePos - self.windowPos


    def mouseMoveEvent(self, event=Qt.QMouseEvent):
        self.move(event.globalPos() - self.dPos)


    def nextSong(self):
        if not self.sources:
            return
        self.currentLyric.setText('')
        self.nextLyric.setText('')
        currentIndex = self.sources.index(self.mediaObject.currentSource())
        if self.playmode == u'顺序播放':
            nextIndex = (currentIndex + 1) % len(self.sources)
        elif self.playmode == u'随机播放':
            nextIndex = random.randint(0, len(self.sources) - 1)
            while nextIndex == currentIndex:
                nextIndex = random.randint(0, len(self.sources) - 1)
        elif self.playmode == u'单曲循环':
            nextIndex = currentIndex
        self.mediaObject.setCurrentSource(self.sources[nextIndex])
        self.mediaObject.play()


    def lastSong(self):
        if not self.sources:
            return
        self.currentLyric.setText('')
        self.nextLyric.setText('')
        currentIndex = self.sources.index(self.mediaObject.currentSource())
        if self.playmode == u'顺序播放':
            if currentIndex > 0:
                lastIndex = currentIndex - 1
            else:
                lastIndex =currentIndex
        elif self.playmode == u'随机播放':
            lastIndex = random.randint(0, len(self.sources) - 1)
            while lastIndex == currentIndex:
                lastIndex = random.randint(0, len(self.sources) - 1)
        elif self.playmode == u'单曲循环':
            lastIndex = currentIndex
        self.mediaObject.setCurrentSource(self.sources[lastIndex])
        self.mediaObject.play()

    def minimizeWindow(self):
        self.showMinimized()
        self.listWindow.hide()
        self.list.setStyleSheet(_fromUtf8("border-image: url(:/icons/list_off.png);"))


    def getLyricAndCover(self, artist, title):
        url = u'http://geci.me/api/lyric/' + title + u'/' + artist
        data = urllib.urlopen(url.encode('utf-8')).readline()
        urllib.urlopen(url.encode('utf-8')).close()

        dic = json.loads(data)
        result = dic.get('result')
        if not result:
            return []
        return result[0]
        # aid = result[0].get('aid')
        # lyricUrl = result[0].get('lrc')
        # lyricRead = urllib.urlopen(lyricUrl)
        #
        # coverUrl = 'http://geci.me/api/cover/' + unicode(aid)
        #
        #
        # return lyricRead

class ListForm(QtGui.QWidget):
    def __init__(self):
        super(QtGui.QWidget, self).__init__()
        self.dPos = Qt.QPoint()
        self.mousePos = Qt.QPoint()
        self.windowPos = Qt.QPoint()

    def mousePressEvent(self, event=Qt.QMouseEvent):
        self.windowPos = self.pos()
        self.mousePos = event.globalPos()
        self.dPos = self.mousePos - self.windowPos

    def mouseMoveEvent(self, event=Qt.QMouseEvent):
        self.move(event.globalPos() - self.dPos)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Music Player")
    app.setQuitOnLastWindowClosed(True)

    window = music_player()

    window.setWindowFlags(Qt.Qt.FramelessWindowHint)
    window.show()

    sys.exit(app.exec_())
