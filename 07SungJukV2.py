# 성적 프로그램 V1
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함


# 입력 데이터 선언
name = '홍길동'
kor = 99
eng = 98
mat = 99

# 처리 데이터 선언
tot = kor + eng + mat
avg = tot / 3

#결과출력
print(f'이름 :{name:s} , 국어:{kor} , 영어:{eng} , 수학: {mat}')
print(f'총점 :{tot:d} , 평균: {avg:.1f}')

# 입력 데이터 선언
names = ['혜교', '수지', '지현']
kors = [55, 58, 98]
engs = [68, 87, 99]
mats = [67, 77, 98]
tots = []
avgs = []
# 처리 데이터 선언
tots.append(kors[0] + engs[0] + mats[0])
avgs.append(tots[0] / 3)

tots.append(kors[1] + engs[1] + mats[1])
avgs.append(tots[1] / 3)

tots.append(kors[2] + engs[2] + mats[2])
avgs.append(tots[2] / 3)

#결과출력
print(f'이름 :{names[0]:s} , 국어:{kors[0]} , 영어:{engs[0]} , 수학: {mats[0]}')
print(f'총점 :{tots[0]:d} , 평균: {avgs[0]:.1f}')

print(f'이름 :{names[1]:s} , 국어:{kors[1]} , 영어:{engs[1]} , 수학: {mats[1]}')
print(f'총점 :{tots[1]:d} , 평균: {avgs[1]:.1f}')

print(f'이름 :{names[2]:s} , 국어:{kors[2]} , 영어:{engs[2]} , 수학: {mats[2]}')
print(f'총점 :{tots[2]:d} , 평균: {avgs[2]:.1f}')

students = []

joju = (f'이름 :{name[0]:s} , 국어:{kor[0]} , 영어:{eng[0]} , 수학: {mat[0]}')
students.append(joju)

joju = (f'이름 :{name[1]:s} , 국어:{kor[1]} , 영어:{eng[1]} , 수학: {mat[1]}')
students.append(joju)

joju = (f'이름 :{name[2]:s} , 국어:{kor[2]} , 영어:{eng[2]} , 수학: {mat[2]}')
students.append(joju)




students.pop(0)
print(students[0])