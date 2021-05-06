# 부품찾기 - 집합자료형 이용

# 이 문제는 단순히 특정한 수가 한 번이라도 등장했는지를 검사하면 된다
# set()함수는 집합 자료형을 초기화할 때 사용한다
# 소스코드가 간결한 측면에서는 가장 우수하다
# 하지만 이진 탐색으로도 충분히 풀 수 있다

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 입력 받아서 집합(Set) 자료형에 기록
array = set(map(int, input().split()))

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# no yes yes 