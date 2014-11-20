# -*- coding: utf-8 -*-
import sip, sys
sip.setapi('QString', 2)
from PyQt4 import QtGui, QtCore
from PyQt4.phonon import Phonon
from AudioPlayerUI import Ui_AudioPlayer
from ListUI import Ui_musicList

class music_player(QtGui.QMainWindow, Ui_AudioPlayer):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.setupUi(self)

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)

        self.mediaObject.setTickInterval(1000)
        self.mediaObject.tick.connect(self.tick)

        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
        self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)

        Phonon.createPath(self.mediaObject, self.audioOutput)

        #self.setupActions()
        self.list.clicked.connect(self.showList)
        self.play.clicked.connect(self.clickPlay)
        self.pause.clicked.connect(self.mediaObject.pause)
        self.stop.clicked.connect(self.mediaObject.stop)

        self.timeLcd.display("00:00")
        self.seekSlider.setMediaObject(self.mediaObject)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        # self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum,
        #         QtGui.QSizePolicy.Maximum)


        self.sources = []        #播放文件列表
        self.info = []
        self.musicIndex = 0

        self.Form1 = QtGui.QDialog()
        self.ListUI = Ui_musicList()
        self.ListUI.setupUi(self.Form1)
        self.ListUI.addButton.clicked.connect(self.addFiles)
        # self.ListUI.musicTable.cellClicked.connect(self.tableClicked)
        # self.ListUI.musicTable.cellDoubleClicked.connect(self.tableClicked)
        self.ListUI.musicTable.cellPressed.connect(self.tableClicked)



    def showList(self):

        x = self.pos().x()
        y = self.pos().y()
        self.Form1.move(x - 415, y)
        self.Form1.show()
        self.Form1.exec_()



    def addFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation))

        if not files:
            return

        index = len(self.sources)

        for string in files:                #同时添加多个文件时的处理
            self.sources.append(Phonon.MediaSource(string))

        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])



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
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()

        titleItem = QtGui.QTableWidgetItem(title)
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict = dict(TITLE=title)

        artist = metaData.get('ARTIST', [''])[0]
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(ARTIST=artist)

        album = metaData.get('ALBUM', [''])[0]
        albumItem = QtGui.QTableWidgetItem(album)
        albumItem.setFlags(albumItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(ALBUM=album)

        year = metaData.get('DATE', [''])[0]
        yearItem = QtGui.QTableWidgetItem(year)
        yearItem.setFlags(yearItem.flags() ^ QtCore.Qt.ItemIsEditable)
        mdict.update(DATE=year)

        self.info.append(mdict)

        currentRow = self.ListUI.musicTable.rowCount()       #显示音频信息
        self.ListUI.musicTable.insertRow(currentRow)
        self.ListUI.musicTable.setItem(currentRow, 0, titleItem)
        self.ListUI.musicTable.setItem(currentRow, 1, artistItem)
        self.ListUI.musicTable.setItem(currentRow, 2, albumItem)
        self.ListUI.musicTable.setItem(currentRow, 3, yearItem)

        if not self.ListUI.musicTable.selectedItems():
            self.ListUI.musicTable.selectRow(0)
            self.mediaObject.setCurrentSource(self.metaInformationResolver.currentSource())

        index = self.sources.index(self.metaInformationResolver.currentSource()) + 1

        if len(self.sources) > index:
            self.metaInformationResolver.setCurrentSource(self.sources[index])   #解析下一首歌的信息
        else:
            self.ListUI.musicTable.resizeColumnsToContents()
            if self.ListUI.musicTable.columnWidth(0) > 300:
                self.ListUI.musicTable.setColumnWidth(0, 300)



    def stateChanged(self, newState, oldState):     #根据播放状态改变不同按键的状态
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                        self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                        self.mediaObject.errorString())

        elif newState == Phonon.PlayingState:
            self.play.setEnabled(False)
            self.pause.setEnabled(True)
            self.stop.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.stop.setEnabled(False)
            self.play.setEnabled(True)
            self.pause.setEnabled(False)
            self.timeLcd.display("00:00")

        elif newState == Phonon.PausedState:
            self.pause.setEnabled(False)
            self.stop.setEnabled(True)
            self.play.setEnabled(True)


    def clickPlay(self):
        l1 = self.sources
        l2 = self.info
        self.showTitle()
        self.mediaObject.play()


    def showTitle(self):
        index = self.sources.index(self.mediaObject.currentSource())
        ft = QtGui.QFont()
        ft.setPointSize(14)
        ft.setBold(True)
        self.musicName.setFont(ft)
        self.musicName.setText(self.info[index].get('TITLE'))
        self.albumAndSinger.setText(self.info[index].get('ARTIST')
            + ' - ' + self.info[index].get('ALBUM'))


    def sourceChanged(self, source):
        index = 0
        while index < len(self.sources) and self.sources[index] != source:
            index += 1
        self.ListUI.musicTable.selectRow(index)
        self.timeLcd.display('00:00')


    def aboutToFinish(self):
        index = self.sources.index(self.mediaObject.currentSource()) + 1
        if len(self.sources) > index:
            self.mediaObject.enqueue(self.sources[index])         #enqueue动作触发currentSourceChanged信号


    def tick(self, time):     #显示播放时间
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.timeLcd.display(displayTime.toString('mm:ss'))

    def tableClicked(self, row, column):   #点击音频列表时的反应
        wasPlaying = (self.mediaObject.state() == Phonon.PlayingState)

        self.mediaObject.stop()
        self.mediaObject.clearQueue()

        self.mediaObject.setCurrentSource(self.sources[row])


        self.showTitle()
        self.mediaObject.play()






if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Music Player")
    app.setQuitOnLastWindowClosed(True)

    window = music_player()
    window.show()

    sys.exit(app.exec_())
