# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = '')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]: # 방문하지 않은 노드들에 대해 방문 처리한다.
            dfs(graph, i, visited)
            
# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
     [], # 1번노드, 인덱스 0에 대한 내용은 비운다
     [2,3,8], # 1번 노드와 연결된 2,3,8 노드
     [1,7], # 2번 노드와 연결된 1,7 노드
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

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)

# 12768345
 