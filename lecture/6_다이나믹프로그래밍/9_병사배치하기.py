# 병사 배치하기
'''
N명의 병사가 무작위로 나열되어 있다
각 병사는 특정한 값의 전투력을 보유한다
병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 한다
(앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 한다)
배치과정에서 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다
그러면서도 남아있는 병사의 수가 최대가 되도록 한다

입력 조건 : 1 <= N <= 2,000, 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수
입력 :  7
        15 11 4 8 5 2 4
'''

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse() # 전투력이 높은 병사가 앞쪽에 오도록 내림차순 해준다

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))

# 7 (n 명의 병사)
# 15 11 4 8 5 2 4 (병사들의 전투력)

# 2