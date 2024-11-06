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
        maps[current[0]][current[1]] = 0
        if current[0] == (N - 1) and current[1] == (M - 1):
            return current[2]
        else:
            for i in range(4):
                nx = current[0] + dx[i]
                ny = current[1] + dy[i]
                move_cnt = current[2] + 1
                if (nx >= 0) and (nx < N) and (ny >= 0) and (ny < M) and maps[nx][ny]:
                    q.append((nx, ny, move_cnt))
    return -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
print(solution([[1],[1]]))