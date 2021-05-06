# 메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)이다

d = [0] * 100

def fibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0 :
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

fibo(6)
# f(6) f(5) f(4) f(3) f(2) f(1) f(2) f(3) f(4)