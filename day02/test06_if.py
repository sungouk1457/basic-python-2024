#date:20240130
#desc:여러조건if

date = input('날짜 입력 : ')

month = date.split('-')[0]
day = date.split('-')[1]

if month == '12' and day == '25':
    print('메리 크리스마스')
elif month == '01' and day == '01':
    print('해피 뉴이어')
elif month == '04' and day == '14':
    print('짜장면 먹기')
else:
    print('보통날입니다')