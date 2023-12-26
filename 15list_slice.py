# 슬라이싱(slicing)
# 연속적인 객체들(리스트, 튜플, 문자열)에 범위를 지정하고
# 선택해서 부분적으로 객체를 가져오는 방법 및 표기법
# 리스트 객체에서 필요한 부분의 항목만 뽑아 사용하는 것
# 객체명[시작:끝-1:스텝]

# 다음 코드에서 생년월일 추출
jumin = '123456-1234567'

print(jumin[0:6])
print(jumin[:6])    # 시작을 생략하면 리스트의 인덱스는 0부터

# 생년월일과 - 를 제외한 나머지 추출
print(jumin[7:14])
print(jumin[7:])    # 끝을 생략하면 리스트의 인덱스는 0부터

# 코드에서 짝수/홀수 위치의 문자 추출
print(jumin[0:14:2])    # 홀수 위치 문자 추출
print(jumin[0::2])
print(jumin[::2])

print(jumin[1:14:2])    # 짝수 위치 문자 추출
print(jumin[1::2])

# 역순으로 추출 : step을 -로 설정
print(jumin[14:0:-1])
print(jumin[14::-1])
print(jumin[::-1])

#확인문제
alphabet = 'a','b','c','d','e','f','g','h','i','j'


# 역순출력
print(alphabet[:])
print(alphabet[::-1])

# 요구사항에 따라 출력
print(alphabet[2:5+1])
print(alphabet[:4+1])
print(alphabet[3:7+1])
print(alphabet[5:])
print(alphabet[3:8+1])


# 혈액 보관 시스템
bloods = []
a, b, ab, o = 0, 0, 0, 0

for idx in range(1, 10+1):
    print(f' 헌혈해 주셔서 감사합니다. 혈액형을 선택하세요 ({idx}/10')
    blood = input('A, B, AB, O :')
    bloods.append(blood)

for bd in bloods:
    if bd == 'A' : a += 1
    elif bd == 'B' : b += 1
    elif bd == 'AB' : ab += 1
    elif bd == 'O' : o += 1

print(f'''
----------------------------------
A형 : {a}
B형 : {b}
AB형 : {ab}
O형 : {o}
----------------------------------
''')

# 혈액형 항목별 빈도 계산 : count(값)
bloods.count(a)
bloods.count(b)
bloods.count(ab)
bloods.count(o)


