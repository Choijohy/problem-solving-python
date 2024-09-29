"""
    문제: 약수 구하기
    출처: 프로그래머스(https://school.programmers.co.kr/learn/courses/30/lessons/120897)

    시도한 풀이:
        숫자(n)가 주어졌을때, 1부터 본인까지 탐색하며 약수인지 아닌지 판별
        --> O(n)으로 비효율적

    개선된 풀이:
        n = A * B 혹은 n = A * A 임을 생각 해보면,
        전체 탐색할 필요 없이 A가 될 수 있는 수까지만 탐색하면 됨( = 최대 루트n 까지만 탐색하면 됨)
"""


def solution(n):
    answer = []
    for i in range(1, int(n ** (1 / 2) + 1), 1):
        if n % i == 0:
            answer.append(i)
            if i ** 2 != n:
                answer.append(n // i)

    answer.sort()
    return answer
