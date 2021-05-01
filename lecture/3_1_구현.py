# 상하좌우
'''
여행가 A는 N X M 크기의 정사각형 공간 위에 서 있다. 
이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다. 
가장 왼쪽 위 좌표는(1,1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)이다. 

계획서는 다음과 같다. 
하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다. 
L : 왼쪽으로 한 칸 이동
R : 오른쪽으로 한 칸 이동
U : 위로 한 칸 이동
D : 아래로 한 칸 이동

이때 여행가 A가 N X M 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 

입력 조건 : 1 <= N <= 100
            둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다(1 <= 이동 횟수 <= 100)

입력 :  5
        R R R U D D
'''        

# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            print('nx :', nx)
            ny = y + dy[i]
            print('ny :',ny)
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)

# nx : 1
# ny : 2

# nx : 1
# ny : 3

# nx : 1
# ny : 4

# nx : 0
# ny : 4

# nx : 2
# ny : 4

# nx : 3
# ny : 4

# 3 4