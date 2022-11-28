import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Buttons")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.lbl = QLabel("My Text",parent=self)
        enterButton = QPushButton("Enter",parent=self)
        exitButton = QPushButton("Exit",parent=self)
        self.lbl.move(100,50)
        self.lbl.resize(150,20)
        enterButton.move(100,70)
        exitButton.move(185,70)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.lbl.setText('You clickes Enter')

    def exitFunc(self):
        self.lbl.setText('You clickes Exit')


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()