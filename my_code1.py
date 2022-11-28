from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QShortcut

from PyQt5.QtMultimedia import QMediaContent
from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl

from PyQt5.QtGui import QKeySequence

import sys
import os

class PlayerWindow(QMainWindow):
    def __init__(self, parent=None):
        super(PlayerWindow, self).__init__(parent)
        
        self.win = QWidget()
        self.setCentralWidget(self.win)
        
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()
        self.mediaPlayer.setVideoOutput(videoWidget)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.win.setLayout(layout)
        
        layout.addWidget(videoWidget)
        
        self.shortcut1 = QShortcut(QKeySequence("1"), self)
        self.shortcut1.activated.connect(lambda :self.play_video('1'))
        
        self.shortcut2 = QShortcut(QKeySequence("2"), self)
        self.shortcut2.activated.connect(lambda :self.play_video('2'))
        
        self.shortcut3 = QShortcut(QKeySequence("3"), self)
        self.shortcut3.activated.connect(lambda :self.play_video('3'))
        
        self.shortcut4 = QShortcut(QKeySequence("4"), self)
        self.shortcut4.activated.connect(lambda :self.play_video('4'))
        
        self.shortcutQ = QShortcut(QKeySequence("q"), self)
        self.shortcutQ.activated.connect(self.close)

        
        self.showMaximized()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()
        
    def play_video(self, filename):
        path = os.path.join('videos',filename+'.mp4')
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        self.mediaPlayer.play()
        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    player = PlayerWindow()
    sys.exit(app.exec_())