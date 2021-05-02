from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft() # 가장 먼저 들어온 원소를 꺼내준다.
        print(v, end= ' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
          
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
     [], # 1번 노드 / 인덱스 0에 대한 내용은 사용하지 않는다.
     [2,3,8], # 2번 노드와 연결 /  2, 3, 8노드와 인접
     [1,7],  # 3번 노드와 연결 / 1, 7노드와 인접
     [1,4,5],
     [3,5],
     [3,4],
     [7],
     [2,6,8],
     [1,7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9
# 모든 노드를 한번도 방문하지 않은 것 처럼 처리

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 1 2 3 8 7 4 5 6
 