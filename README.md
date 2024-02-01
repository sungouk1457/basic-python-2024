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
    - 파일 입출력
    - 가상환경

- 파이썬 활용
    - 주피터 노트북



    - 객체지향(나중에)
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속
        - 추상클래스

