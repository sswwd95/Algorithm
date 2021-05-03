# 부품 찾기-이진 탐색으로 해결

'''
전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 견적서를 요청했다
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해라

입력조건 : 1<= N <= 1,000,000, 1<= M <= 1,000,000
입력 :  5
        8 3 7 9 2
        3
        5 7 9
'''

# 이진 탐색을 사용하는 문제 풀이 방법의 경우 시간복잡도는 O((M + N) X logN)이다.

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# no yes yes