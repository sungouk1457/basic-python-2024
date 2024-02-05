# file: test39_nothread.py
# desc: Qt에서 스레드 없이 동작테스트

import sys
from PyQt5 import QtGui,QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class qtwin_exam(QWidget): 
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self)
        # 버튼에 대한 시그널처리
        self.btnStart.clicked.connect(self.btnStartClicked) #ui 파일내에 있는 위젯접근은 VScode상에서 색상으로 표시x

    
    def btnStartClicked(self):
        maxVal = 1000000
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) #프로그레스바 0부터 시작
        self.pgbTask.setRange(0,maxVal-1) # 0부터 100까지
        for i in range(maxVal):
            print_str = f'노쓰레드 출력 >> {i}'
            print(print_str)
            self.txbLog.append(print_str)
            self.pgbTask.setValue(i)

    def closeEvent(self,QCloseEvent) -> None:
        re = QMessageBox.question(self,'종료확인','종료확인',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        
if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()