# 떡볶이 떡 만들기
'''
떡의 길이가 일정하지 않지만 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다
절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다
높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다
떡을 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 잇는 
높이의 최댓값을 구하는 프로그램을 작성해라

입력조건 : 1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000
          둘째 주레는 떡의 개별 높이가 주어진다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다

입력 :  4 6
        19 15 10 17


'''


# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색), 높이값을 조절
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
# 15