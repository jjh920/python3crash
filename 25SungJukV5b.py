# 성적 프로그램 V5
# 이름, 국어, 영어, 수학을 이용해서
# 총점, 평균, 학점을 계산하고 출력함
# 학점 기준 : 수우미양가
# 성적 입력, 조회, 상세조회, 수정, 삭제 기능 구현
# 각 기능은 메뉴식으로 구현 - 기능별 메뉴 선택시 명령 수행
# 성적 데이터를 dict 자료구조로 구현
# 성적 처리기능을 함수로 구현
import sys
import joju.sjv5b as sjv5

#입력 데이터 선언
sungjuks = {'response': {'body': {'totalCount': 999, 'items': []}}}

# 프로그램 메뉴 출력을 위한 변수 선언

while True:
    # 프로그램 주 실행부
    sjv5.show_menu()
    menu = input('=> 메뉴를 선택하세요 : ')

    # 선택한 메뉴에 따라 해당 기능 수행
    if   menu == '1':
        print('성적데이터 추가')

        sj = sjv5.read_sungjuk()
        sjv5.compute_sungjuk(sj)

        sungjuks['response']['body']['items'].append(sj)

    elif menu == '2':
        print('성적데이터 조회')
        sjv5.show_sungjuk(sungjuks)

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

