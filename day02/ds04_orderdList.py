# date : 20240213
# file : ds04_orderdList.py
# desc : 선형 리스트 프로그램

kakaotalk = [] # 빈 배열 생성

def add_data(friend) :
    kakaotalk.append(None) # 배열에 빈자리 생성
    size = len(kakaotalk) # 배열의 전체 크기 확인
    kakaotalk[size-1] = friend

# 데이터 삽입 함수
def insert_data(pos, friedn) :
    if pos < 0 or pos > len(kakaotalk) :
        print('데이터 삽입 범위 초과')
        return # 함수를 빠져나감
    
    # 정상적인 처리시작
    kakaotalk.append(None) # 빈칸 추가
    size = len(kakaotalk) # 배열의 현재 크기
    
    # 데이터 삽입 위치까지 데이터를 하나씩 뒤로 보내는 작업
    for i in range(size-1, pos, -1) : # 역순으로, 맨 뒤에서부터 하나씩
        kakaotalk[i] = kakaotalk[i-1]
        kakaotalk[i-1] = None

    kakaotalk[pos] = friedn

## 데이터 삭제 함수
def delete_data(pos) : # 데이터 삭제는 위치값만
    if pos < 0 or pos >= len(kakaotalk) : # 마지막 끝범위를 크거나 같다로 설정하기
        print('데이터 삭제범위 초과')
        return
    
    size = len(kakaotalk)
    kakaotalk[pos] = None # 데이터 삭제

    for i in range(pos+1, size, 1) : 
        kakaotalk[i-1] = kakaotalk[i] # 뒤에 있는 값을 앞으로 
        kakaotalk[i] = None

    del(kakaotalk[size-1]) # 배열의 맨 마지막값 삭제

# 전역변수 선언
kakaotalk = [] # 빈 배열 생성
select = -1 # 1/추가, 2/삽입, 3/삭제, 4/종료

if __name__ == '__main__' :
    while (select != 4) :
        select = int(input('선택(1 : 추가, 2 : 삽입, 3 : 삭제, 4 : 종료) > '))

        if select == 1 :
            data = input('추가 데이터 -- > ')
            add_data(data)
            print(kakaotalk)
        elif select == 2 :
            pos = int(input('데이터 삽입 위치 > '))
            data = input('추가 데이터 -- > ')
            insert_data(pos, data)
            print(kakaotalk)
        elif select == 3 :
            pos = int(input('데이터 삭제 위치 > '))
            delete_data(pos)
            print(kakaotalk)
        elif select == 4 :
            print('프로그램 종료')
            exit(0) # 프로그램 완전종료 함수
        else :
            print('1 ~ 4 중 하나를 입력하세요')
            continue