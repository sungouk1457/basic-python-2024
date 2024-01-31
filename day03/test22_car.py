#date:20240131
#desc:자동차 클래스 만들기

class Car:
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    #전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__plate_num}이 전진합니다')
    
    def moveBackward(self):
        print(f'{self.__plate_num}이 후진합니다')
    
    def moveLef(self):
        print(f'{self.__plate_num}이 좌회전합니다')

    def moveRight(self):
        print(f'{self.__plate_num}이 우회전합니다')

    #생성자를 변경했으니까, 변경된 생성자로 호출
    def __init__(self,__plate_num,company,color,gear_type) -> None:
        self.__plate_num = __plate_num
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str:  #print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다'
    
    def getPlateNumber(self): #외부에서는 접근 할수 없도록 막는 조건
        return self.__plate_num

    def setPlateNumber(self, new_platenumber):
        self.__plate_num = new_platenumber

sarah = Car('54라 9538','현대자동차','흰색','자동')
#객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수도 있음
print(sarah)
print(f'차번호는 {sarah.getPlateNumber()}')
print(f'차색상은 {sarah.color}')
sarah.moveForward()

sarah.__plate_num = '98하 7789'
print(sarah)
sarah.setPlateNumber('54로 9555') #클래스에 인장받은 동작으로 값을 변경
print(sarah)
# csuv = Car('경남88 1922','기아자동차','회색','자동')
# print(f'차번호는 {csuv.plate_num}')