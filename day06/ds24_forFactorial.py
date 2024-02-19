# file: ds24_forFactorial.py
# desc: 반복문으로 팩토리얼 구하기 fact(n), 
# n! = 1×2×3×⋯⋯×(n−1)×n

n = 1000
factValue = 1 # 곱셈이므로 1부터

for i in range(n, 0, -1): # n부터 1까지 역순으로
    factValue *= i

print(f'{n}! = {factValue}')

# 재귀호출 factorial
def factorial(num):
    if num <= 1: return 1

    return num * factorial(num-1)

print(f'{n}! = {factorial(n)}')
# 10 = 3628800, 20 = 2432902008176640000, 30 
# 재귀호출 1000을 하면 RecursionError: maximum recursion depth exceeded 재귀호출 최고 깊이를 초과
