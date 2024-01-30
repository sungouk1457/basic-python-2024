#date:20240130
#desc:구구단 프로그램
#spec: for문 잘 써야함. 2증 for문의 이해
#debugging
#F9(중단점 토글), F5(디버그시작), F10(한줄씩 실행), F11(함수안으로 진입)
# shift + F5(디버깅 종료)
#조사식을 확인
#x x y = x*y
#2x1=2, 2x2=4, 2x3=6 ......2x9=18 

print('구구단 시작')
for x in range(2,9+1): # 2부터 9까지 반복
    print(f'{x}단 -->')
    for y in range(1,10): # 1부터 9까지 반복
        print(f'{x} x {y} = {x*y:2d}|', end='  ') # end= 엔터대신 공백으로 변경
    print() # 안쪽 for문이 끝나면 마지막 엔터를 하나 추가
print('구구단 끝')