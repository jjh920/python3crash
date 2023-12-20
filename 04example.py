# 1
# 프로그래밍 언어 실습시 글꼴은
# 고정폭 글꼴을 사용할 것을 추천!
print('*   *    **    ****    ****    *   *       /////  ')
print('*   *   *  *   *   *   *   *   *   *      | O O | ')
print('*****  *    *  ****    ****     * *      (|  ^  |)')
print('*   *  ******  *   *   *   *     *        | [_] | ')
print('*   *  *    *  *    *  *    *    *         -----  ')

   /\_/\
  ( ' ' )



# 3. 다음 중 자바 변수로 사용 가능한 것은 무엇인지 서술하여라.
# rate1, 1stPlayer, myprogram.java, long, TimeLimit, numberOfWindows
# 1stPlayer,myprogram.java 은 변수를 하용할 수 없다.

tate1 = 1
1stPlayer = 2       # 숫자가 앞에 있으면 안됨!
myprogram.java = 3  # 특수기호가 있으면 안됨!
long = 4
TimeLimit = 5
numberOfWindows = 6


# 학생 테이블의 각 컬럼 데이터도
# 변수로 선언하고 값으로 초기화
stno = 1
hakbun = 201350050
name = '김태희'
addr = '경기도 고양시'
birth = '1985.3.22'
deptid = 1
profid = 4
regdate = '2023-12-20 14:43:15'

print(stno, hakbun, name, name, addr, birth)
print(stno, deptid, profid, regdate)

#4. 다음 수학식을 자바 표현식으로 바꿔보아라.
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8

print(3 * x, 3 * x + y, (x + y) / 7, (3 * x + y) / (z + 2))
print( s0 + v0 * t + 1/2 * g * t ** 2)

#5 다음 문장의 실행결과는 무엇인지 서술하여라.
print(1 / 3, (1 / 3) * 3) # 부동소수점 연산의 헛점이 원인
print(7 / 3, 7 % 3, 7 // 3)
result = 2
result /= 2     # result = result / 2
print(result)

# 6다음 변수에 정의된 값을 이용해서 자바 표현식의 실행결과는
# 무엇인지 서술하여라.
#double x = 2.5;  double y = 1.5;  int m = 18;  int n = 4;



x = 2.5
y = 1.5
print(x, y)
m = 18
n = 4
print(x + n * y - (x + n) * y)
-1.25
print(m / n + m % n)
6.5
print(5 * x - n / 5 )
11.7
print(1 - (1 - (1 - (1 - (1 - n)))))
-3


x, y, m, n = 2.5, 1.5, 18, 4
print(x + n * y - (x + n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))


# 7각 표현식에 대한 결과 값을 계산하여라. 만일 틀린 식이 있다면 수정하여라.
print(3 + 4.5 * 2 + 27 / 8)
print (3 + (4.5 * 2) + (27 / 8))
print(true || false && 3 < 4 || !(5 == 7))
print(True or False and 3 < 4 or not(5 == 7) )
= True

true || (3 < 5 && 6 >= 2)
print(True or (3 < 5 and 6 >= 2))
= True

!true > 'A'
print(not True > bool('A'))

7 % 4 + 3 - 2 / 6 * 'Z'
print(7 % 4 + 3 - 2 / 6 * bool('Z'))

'D' + 1 + 'M' % 2 / 3
print(bool('D') + 1 + bool('M') % 2 / 3)

print(5.0 / 3 + 3 / 3)

print(53 % 21 < 45 / 18)

print((4 < 6) || true && false || false && (2 > 3))
print((4 < 6) or True and False or False and (2 > 3))


print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))


# 9 각 부울 표현식에 대한 값을 계산하여라. 자바는 단축식 평가
# short-circuit evaluation을 사용한다는 점에 주의하여라.
가.   true && false && true || true
print(True and False and True or True)

나. true || true && true && false
print(True or True and True and False)

다.   (true && false) || (true && ! false) || (false && !false)
print()

라.   (2 < 3) || (5 > 2) && !(4 == 4) || 9 != 4
print()

마.   6 == 9 || 5 < 6 && 8 < 4 || 4 > 3
print()

# 10 다음 중 유효한 표현식을 찾고, 그 결과 값의 데이터 유형을 서술하여라.
가.   27 / 13 + 4
print(27 / 13 + 4 )

나.   27 / 13 + 4.0
print(27 / 13 + 4.0  )

다.   42.7 % 3 + 18
print(42.7 % 3 + 18 )

마.   23 / 5 + 23 / 5.0
print(23 / 5 + 23 / 5.0)
바.   2.0 + 'a'
print(2.0 + bool('a'))      # 문자와 숫자간 산술연산 불가

자.   'a' / 'b'
print(bool('a') / bool('b') )# 문자끼리 산술연산 불가

사.   2 + 'a'
print(2 + bool('a') )

아.   'a' + 'b'
print(bool('a') + bool('b'))

카.   ( double ) 'a' / 'b'
print(float(bool('a') / bool('b')))

# 논리식과 산술식이 결합된 수식에서는
# 논리식의 결과가 True라면 값이 출력
# 논리식의 결과가 False라면 False가 출력
라.   (3 < 4) && 5 / 8
print((3 < 4) and 5 / 8)

print((3 > 4) and 5 / 8)        #답이 아니니 False


차.   'a' && ! 'b'
print('a' and not 'b')
# 11이름과 몸무게, 나이를 변수로 선언하고 자신의 것을 값으로 초기화하는
# 프로그램을 작성하여라 (MyInfo)
name = '홍길동'
weight = 32.5
age = 19
print(name, weight, age)

# 카멜 표기법 : 변수 정의 할때 알아보기 쉽게 대문자를 중간에 끼워 넣는 표기법
# 12 생년월일을 이용해서 나이를 계산하는 프로그램을 작성하여라. (MyAge)
# K-나이
# 세는 나이 : 출생시 1살, 해가지나면 +1
# 만나이 : 출생시 0살, 생일이 지나면 +1
# 연나이 : 현재년도 - 출생연도

birthYear = 2005
currentYear = 2023

age = currentYear - birthYear

print('연나이 : ' , age)


# 13 구구단 중 7단을 출력하는 프로그램을 작성하여라. (GuGu7Dan)
print('7 x 1 = 7')
print('7 x 2 = 14')
print('7 x 3 = 21')
print('7 x 4 = 28')
print('7 x 5 = 35')
print('7 x 6 = 42')
print('7 x 7 = 49')
print('7 x 8 = 56')
print('7 x 9 = 63')

dan = 7
print(f'{dan} x 1 = {dan * 1}')
print(f'{dan} x 2 = {dan * 2}')
print(f'{dan} x 3 = {dan * 3}')
print(f'{dan} x 4 = {dan * 4}')
print(f'{dan} x 5 = {dan * 5}')
print(f'{dan} x 6 = {dan * 6}')
print(f'{dan} x 7 = {dan * 7}')
print(f'{dan} x 8 = {dan * 8}')
print(f'{dan} x 9 = {dan * 9}')

print('%d x 1 = %d' % (dan, dan*1))
print('%d x 2 = %d' % (dan, dan*2))
print('%d x 3 = %d' % (dan, dan*3))
print('%d x 4 = %d' % (dan, dan*4))
print('%d x 5 = %d' % (dan, dan*5))
print('%d x 6 = %d' % (dan, dan*6))
print('%d x 7 = %d' % (dan, dan*7))
print('%d x 8 = %d' % (dan, dan*8))
print('%d x 9 = %d' % (dan, dan*9))

print('{} x 1 = {}'.format(dan, dan *1))
print('{} x 2 = {}'.format(dan, dan *2))
print('{} x 3 = {}'.format(dan, dan *3))
print('{} x 4 = {}'.format(dan, dan *4))
print('{} x 5 = {}'.format(dan, dan *5))
print('{} x 6 = {}'.format(dan, dan *6))
print('{} x 7 = {}'.format(dan, dan *7))
print('{} x 8 = {}'.format(dan, dan *8))
print('{} x 9 = {}'.format(dan, dan *9))

