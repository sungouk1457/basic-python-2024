#date:20240131
#desc:객체지향 클래스 만들기

#클래스(사람이라는 객체를 만들기 위한 청사진) 만들기
class Person:  #사람 클래스 선언
    name = '' #멤버변수
    age = 0
    gender = ''

    #생성자 함수 (스페셜 함수) 클래스의 객체를 생성할때 동작
    #init == initialization(초기화)
    def __init__(self) -> None:
        self.name = '홍승욱'
        self.age = 25
        self.gender = '남자'

    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름 {self.name} 객체 생성'
        return strs

    #멤버함수 매개변수 self 필수
    def walk(self): 
        print(f'{self.name}이(가) 걷습니다')
    
    def stop(self):
        print(f'{self.name}이(가) 멈춥니다')
#사람 객체 생성, Instance(사례, 예제)
gd = Person() #함수호출처럼 작성하면 됨
gs = Person()

# print(type(mg))
# print(id(mg))  #다른 객체인지 확인
# print(id(es))

gd.name = '홍길동' #객체명.멤버변수 = ...
gd.age = 25
gd.gender = '남자'

gs.name = '홍길순'
gs.age = 25
gs.gender = '여자'

print(f'gd => 이름은 {gd.name}, 나이는 {gd.age}, 성별은 {gd.gender}입니다')
print(f'gs => 이름은 {gs.name}, 나이는 {gs.age}, 성별은 {gs.gender}입니다')

gd.walk()
print('1분동안 걷는다')
gd.stop()

gs.walk()
print('걷기 싫어함')
gs.stop()

print('생성자 함수 추가 ----------------------------------------')
sw = Person()
print(f'sw => 이름은 {sw.name}, 나이는 {sw.age}, 성별은 {sw.gender}입니다')
print(sw) # __str__ 호출