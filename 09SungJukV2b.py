# 성적 프로그램 V2b
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균을 계산하고 출력함
# 단, 리스트를 이용해서 학생 3명에 대해 성적처리를 진행함
# 반복문을 이용하면 코드를 간단히 작성 가능!
# 데이터 입력시 input 함수 이용


#<LV.1> - A 라는 1차원적 입력
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

#<LV.2> - 3가지 방법을 넣을때에 입력
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

print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
print(f'총점 :{tots[i]:d} , 평균: {avgs[i]:.1f}')

print(f'이름 :{names[1]:s} , 국어:{kors[1]} , 영어:{engs[1]} , 수학: {mats[1]}')
print(f'총점 :{tots[1]:d} , 평균: {avgs[1]:.1f}')

print(f'이름 :{names[2]:s} , 국어:{kors[2]} , 영어:{engs[2]} , 수학: {mats[2]},')
print(f'총점 :{tots[2]:d} , 평균: {avgs[2]:.1f}')



#<LV.3> - 반복문을 통한 입력 및 input 을 통한 입력
#성적 데이터 입력(입력데이터 선언 및 input을 이용한 입력데이터)
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []

for i in range(3):
    print(f'{i+1}번째 학생데이터 입력')
    names.append(input('이름은? :'))
    kors.append(int(input('국어는?')))
    engs.append(int(input('영어는?')))
    mats.append(int(input('수학은?')))


#성적 처리 (처리데이터의 반복문)
for i in range(len(names)):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)

#결과 출력의 반복문
for i in range(len(names)):
    print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
    print(f'총점 :{tots[i]:d} , 평균: {avgs[i]:.1f}')
