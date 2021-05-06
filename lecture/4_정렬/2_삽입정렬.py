array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 원소부터 시작한다.
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
    # (i,0,-1)에서 3번째 인자는 스텝을 의미한다.
    # j는 삽입하고자 하는 원소의 위치를 나타낸다.
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)
# [0,1,2,3,4,5,6,7,8,9]

