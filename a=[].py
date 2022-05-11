import cafe
coffee = cafe.books

##메뉴
def menu():
    print("\n----------\n")
    print('1.도서 추가 \n2.도서 검색 \n3.도서 정보 수정 \n4.도서 삭제 \n5.현재 총 도서 목록 출력 \n6.저장 \n7.프로그램 나가기')
    print("\n----------\n")



##1번을 눌렀을때: 도서 추가
def add_book() :#menu 1
    bookname=input('도서명:')
    person=input('저자:')    
    year=input('출판연도:')
    company=input('출판사명:')
    genre=input('장르:')
    coffee.append([bookname,person,year,company,genre])

##2번을 눌렀을때: 도서 검색
def search_book():
    ##서브메뉴
    while True:
        print("\n----------\n")
        print("1.도서명 \n2.저자 \n3.출판연도 \n4.출판사명 \n5.장르")
        print("\n----------\n")
        submenu=int(input("메뉴 선택>>"))

        if(submenu==1):
            tmp=0
            search=input('검색할 도서명:')
            for i in range(len(coffee)):
                if(coffee[i][0]==search):
                    print(coffee[i])
                    tmp+=1

            if(tmp>0):
                    print('총 %d개의 도서를 찾았습니다.'%tmp)
                    break
            else:
                    print('없는 도서입니다. 다시 검색해주세요.')

        elif(submenu==2):
            tmp=0
            search=input('검색할 저자:')
            for i in range(len(coffee)):
                if(coffee[i][1]==search):
                    print(coffee[i])
                    tmp+=1

            if(tmp>0):
                    print('총 %d개의 도서를 찾았습니다.'%tmp)
                    break
            else:
                    print('없는 도서입니다. 다시 검색해주세요.') 

        elif(submenu==3):
            tmp=0
            search=input('검색할 출판연도:')
            for i in range(len(coffee)):
                if(coffee[i][2]==search):
                    print(coffee[i])
                    tmp+=1

            if(tmp>0):
                print('총 %d개의 도서를 찾았습니다.'%tmp)
                break
            else:
                print('없는 도서입니다. 다시 검색해주세요.')

        elif(submenu==4):
            tmp=0
            search=input('검색할 출판사명:')
            for i in range(len(coffee)):
                if(coffee[i][3]==search):
                    print(coffee[i])
                    tmp+=1

            if(tmp>0):
                print('총 %d개의 도서를 찾았습니다.'%tmp)
                break
            else:
                print('없는 도서입니다. 다시 검색해주세요.') 

        elif(submenu==5):
            tmp=0
            search=input('검색할 장르:')
            for i in range(len(coffee)):
                if(coffee[i][4]==search):
                    print(coffee[i])
                    tmp+=1

            if(tmp>0):
                print('총 %d개의 도서를 찾았습니다.'%tmp)
                break
            else:
                print('없는 도서입니다. 다시 검색해주세요.') 

        elif(submenu==6):
            break 

##도서 정보 수정                                               
def modify_book():    
        for i in range(len(coffee)) :
            print(i+1, coffee[i][0],",", coffee[i][1], ",", coffee[i][2], ",", coffee[i][3], ",", coffee[i][4])

        i = int(input("수정할 도서의 번호를 입력하세요: \n")) - 1
        print("1.도서명 \n2.저자 \n3.출판연도 \n4.출판사명 \n5.장르")
        num = int(input("\n무엇을 수정하시겠습니까? : "))
    
        if num==1:
            coffee[i][0] = input("\n수정내용 : ")
            print("수정되었습니다.")

        elif num==2:
            coffee[i][1] = input("\n수정내용 : ")
            print("수정되었습니다.")

        elif num==3:
            coffee[i][2] = input("\n수정내용 : ")
            print("수정되었습니다.")

        elif num==4:
            coffee[i][3] = input("\n수정내용 : ")
            print("수정되었습니다.")       

        elif num==5:
            coffee[i][4] = input("\n수정내용 : ")
            print("수정되었습니다.")


##도서 삭제
def delete_book():    
        count=0 
        list=1 

        for i in range(len(coffee)):
            print(("%d"+str(coffee[i]))%list)
            list+=1

        count=int(input('삭제할 도서의 번호를 입력하세요:'))
        coffee.pop(count-1)
        print('**********')
        print('삭제 완료')
        print('**********')

##현재 총 도서 목록 출력
def print_book():    
    print(coffee)   
    

##저장
def save_book():    
        with open('c:/input.txt', 'w') as c:
            for i in range(len(coffee)):
                c.write(coffee[i][0])
                c.write(" ")
                c.write(coffee[i][1])
                c.write(" ")
                c.write(coffee[i][2])
                c.write(" ")
                c.write(coffee[i][3])
                c.write(" ")
                c.write(coffee[i][4])
                c.write("\n")
        print("저장되었습니다.")



##프로그램 나가기
def exit_book():    
    print("프로그램이 종료되었습니다.")
    save_book()
    exit()

while True:
    menu()
    num = int(input("\n수행할 기능의 번호를 입력하세요 : "))
    
    if num == 1 :
        add_book()
    elif num == 2 :
        search_book()
    elif num == 3 :
        modify_book()
    elif num == 4 :
        delete_book()
    elif num == 5 :
        print_book()
    elif num == 6 :
        save_book()    
    elif num == 7 :
        exit_book()