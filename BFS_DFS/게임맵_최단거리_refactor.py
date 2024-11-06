"""
    문제: BFS
    출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/1844)

    풀이:
        0. N*M 사이즈의 2차원 배열(maps)가 주어짐
        1. (0,0)부터 (N-1, M-1)까지의 경로를 BFS로 탐색
        2. 이때, 최단 거리를 구해야 하므로 deque에 x,y 좌표 뿐 아니라 현재까지의 누적 이동 칸수도 함께 넣는다. Ex. deque의 원소 형태: (x,y,cnt)
        3. 가장 먼저 (N-1,M-1) 좌표에 도달했을때, 해당 cnt값을 return한다.
        4. 모든 경로를 탐색이 끝난 경우(=deque is empty)에도 return 되지 않았다면, 경로가 없는 것으로 간주하여 -1을 return 한다.

    기타:
        첫 풀이에서 테스트 케이스는 통과하였으나, 효율성 검사에서 실패
        주 원인은 방문 여부(maps[x][y] = 0)를 q에서 꺼낸 뒤에 해주었는데, 이는 q에 append 하는 시점에서는 방문처리를 하지 않기 때문에
        실제 방문되기 전까지는 중복된 노드가 q에 삽입될 수 있음(탐색 시간 증가)
        따라서, 애초에 q에 append 하는 시점에서 방문처리를 하여, 효율성을 높임.

"""
from collections import deque
from typing import List


def solution(maps: List[List[int]]):
    N = len(maps)  # row size
    M = len(maps[0])  # column size

    q = deque()
    q.append((0, 0, 1))

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        current = q.popleft()
        if current[0] == (N - 1) and current[1] == (M - 1):
            return current[2]
        else:
            for i in range(4):
                nx = current[0] + dx[i]
                ny = current[1] + dy[i]
                move_cnt = current[2] + 1
                if (nx >= 0) and (nx < N) and (ny >= 0) and (ny < M) and maps[nx][ny]:
                    maps[nx][ny] = 0
                    q.append((nx, ny, move_cnt))
    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1],[1]]))