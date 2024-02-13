# date : 20240213
# file : ds05_exf(x).py
# desc : 다항식 선형 리스트 표현, 계산 프로그램

## 다항식 형태 출력하는 함수
def printPoly(p_x) :
    term = len(p_x) -1 # 최고차항 숫자 = 배열길이 -1
    polyStr = 'P(x) = '

    for i in range(len(px)) :
        coef = p_x[i] # 계수

        if (coef >= 0) :
            polyStr += '+'
        polyStr += str(coef) + 'x^' + str(term) + " "
        term -= 1
    
    return polyStr

def calcPoly(xVal, p_x) :
    retValue = 0
    term = len(p_x) -1 # 최고차항 숫자 = 배열길이 -1

    for i in range(len(px)) :
        coef = p_x[i] # 계수
        retValue += coef * xVal ** term
        term -= 1

    return retValue

## 전역 변수 선언 부분
px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0


## 메인 코드 부문
if __name__ == '__main__' :
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input('X값 입력 > '))

    pxValue = calcPoly(xValue, px)
    print(pxValue)