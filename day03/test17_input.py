#date:20240131
#desc:콘솔입력

#input('내용추가') => 문자열로 인식
#출력 - 컴퓨터화면,프린터,스피커,빔프로젝트,VR,...
#입력 - 콘솔입력(키보드),마우스입력,목소리,오큘러스,조이스틱,...

temp_val = input('곱할 수 입력 : ')
if temp_val.isnumeric() == True: # 숫자입력이 아니며 튕겨내기
    temp_val = int(temp_val) #문자열 -> 정수 변환(형변환)
    print(f'입력값 = {temp_val}')
    #곱하기
    result = temp_val * 5
    print(f'결과 = {result}')
else:
    print('잘못된 입력, 정수만 입력하세요')