# 딕서너리
# 이름key과 값value으로 구성된 연관배열의 일종
# 자료구조 만들때 {}를 사용하고
# 이름과 값은 : 으로 구분해서 정의함
# 다른 언어의 JSON과 유사한 구조
# 데이터분석시 주로 사용하는 자료구조 : mongodb
# 키를 통해 자료를 찾는 해쉬테이블을 이용하므로 검색속도가 빠름

mids = {'C/C++': 'A', 'Java': 'B+', '네트워킹': 'C',
        '보안': 'A+', '해킹': 'F', '시스템': 'C+'}

print(mids)

# 회원정보를 dict 로 선언
# key : 이름, 아이디, 비번, 이메일, 주소, 성적(국영수)
member = {'name': '홍길동', 'userid': 'abc123', 'passwd': 'xyz987', 'email': 'abc123@naver.com',
          'addr': '서울특별시 관악구 봉천동', 'sungjuk': [98, 99, 98] }

print(member)

# 딕셔너리 다루기
# 조회 : 변수명[키], 변수명.get(키)
print(member['name'])
print(member['userid'])
print(member['sungjuk'])
print(member['sungjuk'][0])     # 국어

print(member.get('name'))
print(member.get('userid'))
print(member.get('sungjuk'))
print(member.get('sungjuk')[1])

# 존재하지 않는 키 지정시
member['zipcode']           # 오류
member.get('zipcode')       # None

# 새로운 항목 추가 : 변수명[새로운키] = 새로운값
member['zipcode'] = '12345'

print(member)

# 기존 항목 변경 : 변수명[키] = 변경할값
member['zipcode'] = '98765'
member['addr'] = '서울시 광진구 자양동'

print(member)

# 기존 항목 삭제 : del 변수명[키], 변수명.pop(키)

del member['zipcode']
member.pop('addr')

print(member)

# 존재하지 않는 키 삭제시
del member['blood']         #오류 발생
member.pop('blood')         #오류 발생
member.pop('blood', None)   #None

# 항목수 조회 : len
print(len(member))

# dict의 모든 키/값 조회 : keys, values
print(member.keys())
print(member.values())

# dict 전체 항목 출력
# 출력 형식은 '키 = 값'

for key in member.keys():
         print(f'{key} = {member[key]}')



# 1.중간고사의 성적(C/C++은 A, Java는 B+, 모바일은 C, 보안은 A+,
#   해킹은 F, 시스템은 C+)을 저장하는 딕셔너리를 만든다.

scores = {'C/C++': 'A', 'Java': 'B+', '모바일': 'C', '보안': 'A+', '해킹': 'F', '시스템': 'C+'}

# 2. 'Java'와 '시스템' 과목의 성적을 조회한다.
print(scores.get('Java'), scores.get('시스템'))
print(scores['Java'], scores['시스템'])

# 3. 추가로 2과목의 성적(파이썬은 A, OS는 A+)을 삽입한다.
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(scores)

# 4. 'Java'와 '시스템'의 성적을 각각 'F'와 'A'로 수정한다.
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(scores)

# 5. 전체 과목과 성적을 조회하여 최종 성적표를 출력한다.

for key in scores.keys():
    print(f'{key} : {scores[key]}')



# 수학시험 프로그램

quizs = (('3 + 2는? (3점)', 5, 3), ('5 ÷ 2의 몫은? (5점)', 2, 5),
         ('10 - 2는? (3점)', 8, 3), ('10의 2제곱 x 2는? (5점)', 200, 5),
         ('1-(10÷4의 나머지)는? (5점)', -1, 5), ('2의 4제곱은? (3점)', 16, 3),
         ('4 ÷ 2는? (3점)', 2, 3))
trueCount = 0
falseCount = 0
totalScore = 0
for idx, q in enumerate(quizs):
    print(f'문제 {idx+1}/7', q[0])
    answer = int(input('정답을 입력하세요 : '))

    if answer == q[1]:
        trueCount += 1
        totalScore += q[2]
    else: falseCount += 1

print(f'''
-----------------------------
정답 개수 : {trueCount}
오답 개수 : {falseCount}
총 점수  : {totalScore}
-----------------------------
''')




# # 수학시험 프로그램
users = {}
while True:
    menu = input('1. 회원가입 2. 프로그램 종료')
    if menu == '1':
        userid = input('아이디를 입력하세요')
        passwd = input('비밀번호를 입력하세요')
        users[userid] = passwd
    elif menu == '2':
        print('-------------------------')
        print('아이디 : 비밀번호')
        print('-------------------------')
        for k in users.keys():
            print(f'{k} : {users[k]}')
            break
else:
    print('잘못 입력하셨습니다!!')




#2
users = {'response': {'body': {'totalCount': 999, 'items': []}}}

print(users['response']['body']['items']
      .append({'uid': 'abc', 'pwd': '123'}))
print(users['response']['body']['items']
      .append({'uid': 'xyz', 'pwd': '987'}))
print(users['response']['body']['items'])


for item in users['response']['body']['items']:
    for key in item.keys():
        print(key, item[key])

while True:
    menu = input('1. 회원가입 2. 프로그램 종료')

    if menu == '1':
        userid = input('아이디를 입력하세요.')
        passwd = input('비밀번호를 입력하세요.')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)
    elif menu == '2':
        print('-------------------------')
        print('아이디 : 비밀번호')
        print('-------------------------')
        for item in users['response']['body']['items']:
            for k in item.keys():
                print(f'{k} : {item[k]}')
        print('-------------------------')
        break
    else:
        print('잘못 입력하셨습니다!!')




users = {'response': {'body': {'totalCount': 999, 'items': []}}}


print(users['response']['body']['totalCount'])
print(users['response']['body']['items'])

print(users['response']['body']['items']
      .append({'uid': 'abc', 'pwd': '123'}))
print(users['response']['body']['items']
      .append({'uid': 'xyz', 'pwd': '987'}))

while True:
    menu = input('1. 회원가입 2. 프로그램 종료')

    if menu == '1':
        userid = input('아이디를 입력하세요.')
        passwd = input('비밀번호를 입력하세요.')
        user = {}
        user['userid'] = userid
        user['passwd'] = passwd
        users['response']['body']['items'].append(user)
    elif menu == '2':
        print('-------------------------')
        print('아이디 : 비밀번호')
        print('-------------------------')
        for item in users['response']['body']['items']:
            for k in item.keys():
                print(f'{k} : {item[k]}')
        print('-------------------------')
        break
    else:
        print('잘못 입력하셨습니다!!')


