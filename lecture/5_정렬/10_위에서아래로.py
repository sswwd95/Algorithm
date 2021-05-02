# 위에서 아래로
'''
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 잇다.
이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만들어라

입력조건 : 1 <= N <= 500
입력 :  3
        15
        27
        12
'''

# N 입력 받기
n = int(input())

# N개의 정수를 입력 받아 리스트에 저장
array = []
for i in range(n):
    array.append(int(input()))

# 파이썬 정렬 라이브러리를 이용하여 내림차순 정렬 수행
array = sorted(array, reverse=True)

# 정렬이 수행된 결과를 출력
for i in array:
    print(i, end=' ')

# 27 15 12