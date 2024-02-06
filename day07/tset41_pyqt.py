#file:test41_pyqt.py
#desc:PyQt5 이미지 뷰어

import sys
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        #이미지 추가  .scaledToWidth(800) 큰 해상도를 w800으로 고정
        pixmap = QPixmap('./images/cat.jpg').scaledToWidth(800)
        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)

        lblSize = QLabel(self)
        lblSize.setText(f'{pixmap.width()}X{pixmap.height()}') # cat.jpg의 width X height

        vbox = QVBoxLayout(self) #QtDesigner VerticlaLayout 위젯 생성
        vbox.addWidget(lblImage) #VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) #from에 VL 추가와 동일

        self.setWindowIcon(QIcon('images\iot.png'))
        self.setWindowTitle('이미지 뷰어')
        self.setGeometry(300,300,300,300)
        self.show() #showFullScreen() 모니터를 꽉 채워서 출력
        self.setCenter()

    def setCenter(self): #윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() #모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(),screen_rect.height()
    print(width,'X',height)
    ins = WinApp()
    sys.exit(app.exec_()) #종료시 리소스 반환등 효율
