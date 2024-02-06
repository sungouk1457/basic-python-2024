# file: test39_nothread.py
# desc: Qt\ 스레드 동작

import sys
from PyQt5 import QtGui,QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BackWorker(QThread): #PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent #BackWorker에서 사용할 멤버변수

    def run(self) -> None: # 스레드 실행
        # 스레드로 동작할 내용
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        ###self.parent.pgbTask.setValue(0) #프로스레스바 0부터 시작  QThread에선 ui관련된 처리를 할 수 없음
        ###self.parent.pgbTask.setRange(0,maxVal-1)
        for i in range(maxVal):
            print_str = f'쓰레드 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
        ###    self.parent.txbLog.append(print_str)
        ###    self.parent.pgbTask.setValue(i)
    
class qtwin_exam(QWidget): #UI스레드
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/ThreadApp.ui',self)
        self.btnStart.clicked.connect(self.btnStartClicked)
        
    def btnStartClicked(self):
        th = BackWorker(self)
        th.start()  #BackWorker 내의 self.run 실행
        th.initSignal.connect(self.initpgbTask) # 스레드에서 초기화 시그널이 오면 initpgbTask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setpgbTask)
        th.setLog.connect(self.settxbLog) #textbrowser 위젯에 진행사항 전달

    #QWidget에 있는 closeEvent를 그대로 쓰면 닫힘
    # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
    def closeEvent(self,QCloseEvent) -> None: # x버튼 종료확인
        re = QMessageBox.question(self,'종료확인','종료확인',QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()

    #스레드에서 시그널이 넘어오면  UI처리를 대신 해주는 슬롯함수
    @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit 동작해서 실행
    def initpgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0,maxVal-1)

    @pyqtSlot(str) # BackWorker 스레드에서 self.setLog.emit 동작해서 실행
    def settxbLog(self,msg):
        self.txbLog.append(msg)
    
    @pyqtSlot(int)
    def setpgbTask(self, val):
        self.pgbTask.setValue(val)

if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()    