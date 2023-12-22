# if 문
# 특정 조건을 만족하면 지정한 문장(들)을 실행하는 조건문
# if 조건식:
#    수행할 문장(들)

# 속도위반 체크 프로그램
# 기준속도 : 50 km/h


speed = int(input('속도는?'))

if speed >= 50:
    print ('속도위반 하셨습니다.')

# 파이썬의 코드 블록
# 특정한 동작을 위한 관코드를 한곳에 모아 둔것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함

# 조건식이 True인 경우 무조건 코드블록을 실행함
if True: print('Hello, World!!')


# if ~ else 문
# if문은 조건이 참일때만 지정한 코드를 실행하는데 비해
# if ~ else문은 조건이 참일때와 거짓일때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#    수행할 문장1
# else:
#    수행할 문장2

# 자동온도 조절 프로그램

temp = int(input('온도를 입력하세요. :'))

if temp >= 40:
    print('중지합니다.')
else:
    print('가동합니다.')


score = 70

if score >= 80:
    print('합격입니다.')
else:
    print('아쉽네요')



# 입력받은 정수를 3으로 나누고
# 소수점 첫째자리에서 반올림하기

num = int(input('정수를 입력하세요. :'))
result = num / 3
if (result - int(result)) >= 0.5:
    result = int(result) + 1
else:
    result = int(result)

print(num, result)


# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용

# 평균이 73.5라 할때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요


avg = 73.5

if avg >= 90: print('수')
else:
    if avg >= 80: print('우')
    else:
        if avg >= 70: print('양')
        else:
            print('가')
# 다중 if문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첩 if문을 단순하게 작성할 수 있는 조건문

# if 조건식1:
#     실행할문장1
# elif 조건식2:
#     실행할문장2
# else:
#     실행할문장3


avg = 85.5

if avg >= 90: print('미')
elif avg >= 80: print('우')
elif avg >= 70: print('미')
elif avg >= 60: print('양')
else: print('가')

# 자동주문 시스템
intro = '''
안녕하세요. 반갑습니다.
해당 번호를 선택 하시면
그에 맞게 언어를 변경 할 수 있습니다.
번호를 선택하십시오.
'''

print(intro, end='1. 대한민국 2. USA 3. 中国 4. 日本')
menu = input('')
if menu == '1': print('어떤것을 주문하시겠어요?')
elif menu == '2': print('would you like to order?')
elif menu == '3': print('要点什么？')
elif menu == '4': print('何を注文しますか？')
else:
    print('다시 설정해 주세요.')




# bmi 지수에 따른 결과 출력
# 몸무게 / (키/100) ** 2
weight = float(input('몸무게는?'))
height = float(input('키는? '))
bmi = weight / (height / 100) ** 2

if bmi <= 90: print(f'bmi 지수 : {bmi:.2f} 저체중')
elif bmi > 90 and bmi <= 110: print(f'bmi 지수 : {bmi:.2f} 정상체중')
elif bmi > 110 and bmi <= 120: print(f'bmi 지수 : {bmi:.2f} 과체중')
elif bmi > 120 and bmi <= 140 : print(f'bmi 지수 : {bmi:.2f} 비만')
else:
    print(f'bmi 지수 : {bmi:.2f} 고도비만')


weight = float(input('몸무게는?'))
height = float(input('키는? '))
bmi = weight / (height / 100) ** 2
if bmi >= 35: result = print(f'bmi 수치 : {bmi:.2f}  초고도비만')
elif bmi >= 30: result = print(f'bmi 수치 : {bmi:.2f}  고도비만')
elif bmi >= 25: result = print(f'bmi 수치 : {bmi:.2f}  비만')
elif bmi >= 23: result = print(f'bmi 수치 : {bmi:.2f}  과체중')
elif bmi >= 18.5: result = print(f'bmi 수치 : {bmi:.2f}  저체중')
else: result = '저체중'



# 누진세 적용 전기요금 계산
# 사용량 200이하 201 ~ 400 400 초과
# 단가 99.3원 187.9원 280.6원
# 기본요금 910원 1600원 7300원

# 전기사용량을 입력하세요
# 사용량
# 기본요금
# 단가
# 전기 요금

usage = int(input('전기 사용량을 입력하세요. :'))

if usage <= 200:
    print(f'사용량 : {usage} Kwh 기본요금 : 910원 단가 : 99.3원]\
    전기 요금 : {usage * 99.3 + 910}')
elif usage > 200 and usage <= 400:
    print(f'사용량 : {usage} Kwh 기본요금 : 1600원 단가 : 187.9원\
     전기 요금 : {usage * 187.9 + 1600}')
else:
    print(f'사용량 : {usage} Kwh 기본요금 : 7300원 단가 : 280.6원\
     전기 요금 : {usage * 280.6 + 7300}')

usage = int(input('전기 사용량을 입력하세요. :'))

basic = 910
price = 99.3

if usage > 400:
    price = 280.6
    basic = 7300
elif usage > 200:
    price = 187.9
    basic = 1600
pay = basic + (usage * price)
print(f'''
사용량 : {usage} 
기본요금 : {basic}
단가 : {price}
전기요금 : {pay}
''')




# 현재년도가 각각 1992, 2000, 2020(윤)과
# 1900, 2100(윤x)에 대해 윤년여부를 출력하는
# 조건식을 작성하세요
# 윤년 : 4로 나눠 나머지가 0이고
#       100으로 나눠 나머지가 0이 아니면
# 윤년 : 400으로 나눠 나머지가 0

year = int(input('년도는? '))

isLeap = '윤년아님!!'
cond1 = (year % 4 == 0) and (year % 100 != 0)
cond2 = year % 400 == 0

if cond1 or cond2:
    isLeap = '윤년 맞음!!'

print(f'{year} {isLeap}')