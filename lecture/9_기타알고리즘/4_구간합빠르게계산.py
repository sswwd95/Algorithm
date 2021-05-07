# 데이터의 개수 N과 전체 데이터 선언
n = 5
data = [10, 20, 30, 40, 50]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산 (세 번째 수부터 네 번째 수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])

# 70

# 현재 코드에서는 쿼리가 1개만 존재하지만,
# N개만큼 많은 쿼리가 들어오더라도
# 각 쿼리에 대해서상수시간에 처리 가능하다.