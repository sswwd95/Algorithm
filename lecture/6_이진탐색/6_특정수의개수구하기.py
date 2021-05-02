# 정렬된 배열에서 특정 수의 개수 구하기

'''
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다
이때 이 수열에서 X가 등장하는 횟수를 계산해라
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받는다

입력조건 : 1 <= N <= 1,000,000, -10**9 <= x <= 10**9
입력 :  7 2 
        1 1 2 2 2 2 3 
'''
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x,x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면 -1을 출력
if count == 0:
    print(-1) 
# 값이 x인 원소가 존재한다면 x의 개수 출력
else : 
    print(count)
# 4
