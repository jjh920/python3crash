# # 성적 프로그램 V2c
# # 이름, 국어, 영어, 수학을 이용해서
# # 총점, 평균, 학점을 계산하고 출력함
# # 학점 기준 : 수우미양가
# # 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# # 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
#
#
# #<LV.1> - A 라는 1차원적 입력
# # 입력 데이터 선언
# name = '홍길동'
# kor = 99
# eng = 98
# mat = 99
#
# # 처리 데이터 선언
# tot = kor + eng + mat
# avg = tot / 3
#
# #결과출력
# print(f'이름 :{name:s} , 국어:{kor} , 영어:{eng} , 수학: {mat}')
# print(f'총점 :{tot:d} , 평균: {avg:.1f}')
#
# #<LV.2> - 3가지 방법을 넣을때에 입력
# # 입력 데이터 선언
# names = ['혜교', '수지', '지현']
# kors = [55, 58, 98]
# engs = [68, 87, 99]
# mats = [67, 77, 98]
# tots = []
# avgs = []
#
#
# # 처리 데이터 선언
# tots.append(kors[0] + engs[0] + mats[0])
# avgs.append(tots[0] / 3)
#
# tots.append(kors[1] + engs[1] + mats[1])
# avgs.append(tots[1] / 3)
#
# tots.append(kors[2] + engs[2] + mats[2])
# avgs.append(tots[2] / 3)
#
# #결과출력
#
# print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
# print(f'총점 :{tots[i]:d} , 평균: {avgs[i]:.1f}')
#
# print(f'이름 :{names[1]:s} , 국어:{kors[1]} , 영어:{engs[1]} , 수학: {mats[1]}')
# print(f'총점 :{tots[1]:d} , 평균: {avgs[1]:.1f}')
#
# print(f'이름 :{names[2]:s} , 국어:{kors[2]} , 영어:{engs[2]} , 수학: {mats[2]},')
# print(f'총점 :{tots[2]:d} , 평균: {avgs[2]:.1f}')
#
#
#
# #<LV.3> - 반복문을 통한 입력 및 input 을 통한 입력
# #성적 데이터 입력(입력데이터 선언 및 input을 이용한 입력데이터)
# names = []
# kors = []
# engs = []
# mats = []
# tots = []
# avgs = []
#
# for i in range(3):
#     print(f'{i+1}번째 학생데이터 입력')
#     names.append(input('이름은? :'))
#     kors.append(int(input('국어는?')))
#     engs.append(int(input('영어는?')))
#     mats.append(int(input('수학은?')))
#
#
# #성적 처리 (처리데이터의 반복문)
# for i in range(len(names)):
#     tots.append(kors[i] + engs[i] + mats[i])
#     avgs.append(tots[i] / 3)
#
# #결과 출력의 반복문
# for i in range(len(names)):
#     print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
#     print(f'총점 :{tots[i]:d} , 평균: {avgs[i]:.1f}')
#
#
#
# #<LV.4> - 중첩조건을 통한 성적표
# #성적 데이터 입력(입력데이터 선언 및 input을 이용한 입력데이터)
# names = []
# kors = []
# engs = []
# mats = []
# tots = []
# avgs = []
# grd = []
# grds = []
#
#
# for i in range(3):
#     print(f'{i+1}번째 학생데이터 입력')
#     names.append(input('이름은? :'))
#     kors.append(int(input('국어는?')))
#     engs.append(int(input('영어는?')))
#     mats.append(int(input('수학은?')))
#
#
# #성적 처리 (처리데이터의 반복문) - grds 추가
# for i in range(len(names)):
#     tots.append(kors[i] + engs[i] + mats[i])
#     avgs.append(tots[i] / 3)
#
#     avg = avgs[len(avgs)-1]
#     grd = '수' if avg >= 90 else \
#           '우' if avg >= 80 else \
#           '미' if avg >= 70 else \
#           '양' if avg >= 69 else '가'
#      grds.append(grd)
#
#
# #결과 출력의 반복문 - 학점 추가
# for i in range(len(names)):
#     print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
#     print(f'총점 :{tots[i]:d} , 평균: {avgs[i]:.1f}, 학점: {grds[i]}')
#
#
#import sys

#<LV.5>
# 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grd = []
grds = []

# 프로그램 메뉴 출력을 위한 변수 선언

main_menu = '''
-----------------------
성적처리 프로그램 v3
-----------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
-----------------------
'''
for i in range(100):
    # 프로그램 주 실행부
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if   menu == '1':
        print('성적데이터 추가')
        sjpos = len(avgs)     # 현재 입력된 데이터 수
        names.append(input('이름은? :'))
        kors.append(int(input('국어는?')))
        engs.append(int(input('영어는?')))
        mats.append(int(input('수학은?')))

        tots.append(kors[sjpos] + engs[sjpos] + mats[sjpos])
        avgs.append(tots[sjpos] / 3)
        avg = avgs[sjpos]
        grd = '수' if avg >= 90 else \
        '우' if avg >= 80 else \
        '미' if avg >= 70 else \
        '양' if avg >= 69 else '가'
        grds.append(grd)


    elif menu == '2':
        print('성적데이터 조회')
        for i in range(len(names)):
           print(f'이름 :{names[i]:s} , 국어:{kors[i]} , 영어:{engs[i]} , 수학: {mats[i]}')
    elif menu == '3':
        print('성적데이터 상세조회')
    elif menu == '4':
        print('성적데이터 수정')
    elif menu == '5':
        print('성적데이터 삭제')
    elif menu == '0':
        print('성적데이터 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')

