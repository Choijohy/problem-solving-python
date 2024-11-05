"""
    문제: DFS
    출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/43165)

    풀이:
        1. 주어진 숫자에서 부호만 바꾸어 가며, 모든 조합에 대한 합계를 구한다.(재귀 호출 => DFS)
           ex. [4,1,2,3] ->
                +4 , +1, +2
                         -2
                     -1 ,+2
                         -2
                        ...
        2.  해당 조합의 합계가 target 넘버인지 판단한다.


    기타:
        BFS -> deque 사용히여 풀이
        DFS -> 특별한 자료구조 없이 재귀를 통해 풀이

"""

from typing import List


def solution(numbers: List[int], target: int) -> int:
    def dfs(index: int, sum: int):
        if index == len(numbers):
            return 1 if sum == target else 0
        else:
            add_result = dfs(index+1, sum+numbers[index])
            sub_result = dfs(index+1, sum-numbers[index])
        return add_result + sub_result

    return dfs(0,0)


print(solution([4, 1, 2, 1], 4))
print(solution([1, 1, 1, 1, 1], 3))
