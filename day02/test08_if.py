#date:20240130
#desc:홀/짝 구분

number = int(input('정수입력 : ')) # 입력받은 후 정수로 변경

if number % 2 == 0:
    print('짝수')
else:
    print('홀수')