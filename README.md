# 파이썬 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어-파이썬

## 1일차
- 개발화경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual Studio Code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 설치
        - Github Desktop 설치
    
- 파이썬 기초
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

    ```python
    # 이부분은 주석입니다.
    var01 = 10 # 정수,실수,불 문자열 모두가능
    print(var01) # 10
    print(type(var01)) # <class of 'int'>

    print(5 + 4 / 2) #7.0
    print( 5 == 4) #False
    ```

## 2일차
- 파이썬 기초
    - 흐름제어
        - if문 : 참/거짓으로 조건 분기  (다른언어 switch)
        - for문 : 반복문  (다른언어 foreach)
        - while문 : 반복문 변형  (다른언어 do~while)
    - 복합자료형 + 연산자(연산함수)
        - 리스트
        - 튜플
        - 딕셔너리
    - 출력 포맷
    - 구구단 + 디버깅
    ```python
    #debugging
    #F9(중단점 토글), F5(디버그시작), F10(한줄씩 실행), F11(함수안으로 진입)
    #shift + F5(디버깅 종료)
    
    ## 구구단 :
    print('구구단 시작')
    for x in range(2,9+1): # 2부터 9까지 반복
        print(f'{x}단 -->')
        for y in range(1,10): # 1부터 9까지 반복
            print(f'{x} x {y} = {x*y:2d}|', end='  ') # end= 엔터대신 공백으로 변경
        print() # 안쪽 for문이 끝나면 마지막 엔터를 하나 추가
    print('구구단 끝')
    ```

## 3일차
- 파이썬 기초
    - 입력 방법
    - 별찍기
    - 함수, 람다함수는 나중에
    - 객체지향 OOP
        - 객체는 명사와 동사의 집합
        - 명사는 변수, 동사는 함수
        - 변수와 함수를 모두 모아둔 곳 : 클래스(class)
        - 클래스에서 하나씩 생성 : 객체(object)
        - 캡슐화(__plateN umber)
    - 패키지

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
    -   pip 사용
    ```shell
    pip --verion #버전확인
    pip list #현재 설치된 라이브러리 목록 확인
    pip install 패키지명 #패키지를 내컴퓨터에 설치
    pip uninstall 패키지명 #패키지를 삭제
    ```
    - 예외처리 : 비정상적 프로그램종료 막기
    ```python
    # ZeroDivisionError 발생
    def divide(x,y):
        try:
            return x/y 
        except ZeroDivisionError as e:
        print('제수는 0이 될 수 없습니다')
        return 0
    ```
    - 텍스트 파일 입출력
    ```python
    f = open('파일명',mode='r|w|a',encoding('cp949|utf-8'))
    f.read()
    f.readline() #읽기
    f.write() #쓰기
    f.close() # 파일은 반드시 닫는다
    ```

- 파이썬 응용
    - 주피터 노트북
        - ctrl + shift + p (명령팔레트)로 시작
        - 사용방법 (test31_jupyter.ipynb 참조)
    - folium 기본사용
    ![folium사용법](https://raw.githubusercontent.com/sungouk1457/basic-python-2024/main/images/Image001.png)

## 5일차
- 파이썬 활용
    - 주피터 노트북 활용(구글 코랩 Colab)
    - folium 마커 찍기기
    - json 입출력
    - 응용예제 연습
        - IP주소 연습
        - QR코드 만들기

## 6일차
- Python 라이브러리 경로 : C:\DEV\Langs\Python311\Lib\site-packages

- 파이썬 응용
    - Window App(PyQt) 만들기

    ```shell
    > pip install PyQt5
    > pip install PyQt5Designer
    ```
    - PyQt5 기본실행
    - QtDesigner 
    - ☆☆☆쓰레드 학습 : UI쓰레드와 Backround쓰레드 분리
        - GIL병렬프로세싱 더 학습할 것

     ![쓰레드 예제](https://raw.githubusercontent.com/sungouk1457/basic-python-2024/main/images/python_003.gif)

    ```python
    # 쓰레드 클래스에서 시그널 선언
    class BackWorker(QThread): #PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
        setSignal = pyqtSignal(int)
    #...

    def run(self) -> None: # 스레드 실행
        # 스레드로 동작할 내용
        maxVal = 1000001
        # ...

    class qtwin_exam(QWidget): #UI스레드
        #...
        def btnStartClicked(self):
        th = BackWorker(self)
        th.start()  #BackWorker 내의 self.run 실행
        th.initSignal.connect(self.initpgbTask)
        # ...

    #스레드에서 시그널이 넘어오면  UI처리를 대신 해주는 슬롯함수
        @pyqtSlot(int) # BackWorker 스레드에서 self.initSignal.emit 동작해서 실행
        def initpgbTask(self, maxVal):
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0,maxVal-1)
        #...
    ```

## 7일차
- 파이썬 응용
    - 객체지향 정리
        - 상속, 오버라이딩(재정의), 오버로딩(같은이름의 함수를 골라쓰기)
        ```python
        #오버 라이딩
        #QWidget에 있는 closeEvent를 그대로 쓰면 닫힘
        # 닫을지 말지를 한번더 물어보는 형태로 다시 구현하고 싶음(재정의 : Override)
        def closeEvent(self,QCloseEvent) -> None: # x버튼 종료확인
            re = QMessageBox.question(self,'종료확인','종료확인',QMessageBox.Yes|QMessageBox.No)
            if re == QMessageBox.Yes:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()
        #오버로딩
        rect = QRect(300,300,300,300) # x,y,w,h
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언해놓고 입맛에 맞게 골라쓰는 방법(오버로딩)
        self.setGeometry(300,300,300,300)
        ```
    - 가상환경 Virtualenv
        - 다른 버전 파이썬도 설치해야 가능
        - 3.11에서 3.9 강상환경을 만들려면 3.9 파이썬 설치필요

    - PyQt5와 응용예제 연습
        - 이미지 뷰어
        - 이미지 에디터

    ![PyQt예제](https://raw.githubusercontent.com/sungouk1457/basic-python-2024/main/images/python_004.png)

## 8일차
- 파이썬 응용
    - PyQt5 응용예제 계속
- 파이썬 기본 코딩테스트