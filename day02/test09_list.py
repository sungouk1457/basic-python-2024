#date:20240130
#desc:복합자료형 list

# s1 = 80
# s2 = 90
# s3 = 100
# s4 = 50
# s5 = 60 #학생수만큼 변수를 생성
# 총갯수 10(n) 면 인덱스의 마자막 값은 9(n-1)
#index = 0,1,2,3,4,5,6,7,8,9
#index = -10,-9,-8,-7,-6,-5,-4,-3,-2,-1 
  
std = [80,90,100,50,60,58,95,48,26,76]

print(std[9])

list_1 = [265,3.3,'문자',True,[1,2,3,4],(3,4),std]
print(list_1)
list_1[6] = '바꾼값'
print(list_1)

##리스트 연산
print(list_1[2:4]) # : 뒤의수는 출력하고 싶은 엔덱스+1이 필수
#마이너스 인덱스
print(list_1[-5:-3])
#이중 리스트
print(list_1[4][2])

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2])

list_4 = [1,2,3]
list_5 = [7,8,9]
##리스트 연산 > +,*만 사용가능
print(list_4+list_5)  # +는 리스트 연결 
print(list_5*2)  # *은 리스트 반복

##리스트의 길이
print(len(list_1))

## append() 리스트 마지막에 하나 추가
print(list_1)
list_1.append('hello')
print(list_1)

## insert(index,val) 리스트의 index 이후에 val 추가
list_1.insert(2,100)
print(list_1)

## extend() 기존 리스트 확장
list_4.extend(list_5)
print(list_4)

## 리스트 삭제
#del()은 완전삭제 print도 안됨
del list_4[3]
print(list_4)

#마지막 값을 꺼내오기
val=list_5.pop()
print(val)
print(list_5)

print(std)
val = std.pop(2)
print(val)
print(std)

#clear() 내용만 삭제
list_5.clear() 
print(list_5)

#sort()
print(list_1)
# list_1.sort() 문자열,숫자,블 섞여있는 리스트는 정렬X
std.sort() 
print(std)
std.sort(reverse=True)#내림차순 정렬
print(std)

#in,not in
print(95 in std)
print(98 in std)

#reverse(),copy(),count()....

# *리스트 : 전개연산자
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a,*list_b]
print(list_c)

list_d = [list_a,list_b]
print(list_d)