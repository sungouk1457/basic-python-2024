# file: test36_pyqt.py
# desc: PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtWidgets import QApplication, QWidget
# print(sys.argv)  현재 파이썬 파일의 경로 표시

class qtwin_exam(QWidget): #QWidget을 상속받아 사용, QWidget이 가진 모든것을 사용할 수 있다
    # 생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() # 화면초기화 함수를 호출
        
    def initUI(self):
        self.setGeometry((1920-400)//2,(1080-300)//2,400,300) # x, y, width, height
        self.setWindowTitle('Qt5 hello world')
        self.text = ''
        self.show()

    def drawText(self,event,paint):
        paint.setPen(QColor(10,10,10)) # r:0,g:0,b:0 -> black / r:255,g:255,b:255 -> white
        paint.setFont(QFont('NanumGothic',15))
        paint.drawText(400//2, 300//2 , 'hell world')
        paint.drawText(event.rect(), Qt.AlignCenter , self.text) # AlignLeft, AlignCenter, AlignRight -> 정렬

    def paintEvent(self, event) -> None: #재정의(override)
        paint = QPainter()
        paint.begin(self)
        self.drawText(event,paint)
        paint.end() # 닫는다
loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
instance = qtwin_exam()
loop.exec_()