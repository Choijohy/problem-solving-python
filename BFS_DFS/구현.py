"""
    문제: DFS, BFS 구현
    출처: 백준(https://www.acmicpc.net/problem/1260)

    풀이:
    N(정점 개수), M(간선 개수), V(시작 정점)
    공통적으로 정점마다의 연결 여부를 기록한 2차원 테이블 생성( N*1 x N*1로 생성하여 정점 번호 그대로를 인덱스 번호로 활용)
    visited 여부를 체크할 리스트 생성
        BFS -> deque 사용히여 풀이
        DFS -> 특별한 자료구조 없이 재귀를 통해 풀이

"""

from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_bfs = [False] * (N + 1)
visited_dfs = [False] * (N + 1)

answer_bfs = []
answer_dfs = []


def bfs(start):
    visited_bfs[start] = True
    answer_bfs.append(start)
    for i in range(1, N + 1):
        if (visited_bfs[i] is False) and (graph[start][i]) and (i not in queue):
            queue.append(i)


def dfs(start):
    visited_dfs[start] = True
    answer_dfs.append(start)
    for i in range(1, N + 1):
        if (visited_dfs[i] is False) and (graph[start][i]):
            dfs(i)


queue = deque([V])
while queue:
    node = queue.popleft()
    bfs(node)

dfs(V)
print(*answer_dfs)
print(*answer_bfs)
