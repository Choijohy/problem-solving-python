"""
    문제: H-Index
    출처: 프로그래머스(https://school.programmers.co.kr/learn/courses/30/lessons/42747/solution_groups?language=python3)

    풀이:
        정렬 후, 리스트 안의 요소를 하나씩 탐색하며 조건에 따라 h값을 조정
"""

def solution(citations):
    citations.sort()

    h = 0
    for i in range(len(citations)):
        if citations[i] > h:
            if citations[i] <= (len(citations) - i): # ex) [0,1,3,5,5] 에서 i=2 일때
                h = citations[i]
            else: # ex) [0,1,1,9,9]에서 i =3 일때, [0,1,3,5,6]에서 i=3일때
                h = max(h, len(citations) - i)
    return h


print(solution([3, 0, 6, 1, 5]))
print(solution([0,0,0]))
print(solution([0]))
print(solution([1,1,3,4,4,4,7]))
print(solution([10000]))