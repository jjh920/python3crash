# 사원정보를 입력받아 employees.csv 파일에 저장
# employees.csv 파일에 저장된 사원정보를 화면 출력
# 저장시 : 사번, 이름, 성, 이메일, 입사일, 직책, 급여, 부서번호
# 출력시 ; 사번, 이름, 직책, 부서번호
import joju.empv1 as emp

emp.load_employees()

while True:
    menu = emp.show_menu()

    if menu == '1': emp.add_employee()                          #C
    elif menu == '2': emp.read_employee()                       #R
    elif menu == '3': emp.readone_employee()                    #R
    elif menu == '4': emp.modify_employee()                     #U
    elif menu == '5': emp.remove_employee()                     #D
    elif menu == '0': emp.exit_program()
    else: print('메뉴를 잘못 선택하셨습니다!!')