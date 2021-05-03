# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
# 3

# 중복되는 함수가 반복적으로 호출되어 심각한 문제가 생긴다
# 재귀 함수를 사용해 만들 수는 있지만 문제를 효율적으로 해결할 수 없다.