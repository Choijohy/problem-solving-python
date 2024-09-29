"""
    문제: 소인수분해
    출처: 프로그래머(https://school.programmers.co.kr/learn/courses/30/lessons/120852)

    풀이:
        나누는 수는 최대 루트n
        (다만, 마지막 나머지가 1이 아닌 경우에는 해당 나머지를 소인수 목록에 넣어줘야 함. ex) 15)

    기타 공부:
    ** 반복문의 종료 조건

        for문
        - range() 함수는 루프가 시작되기 전에 모든 값을 미리 계산
        - 즉, range(2, int(n**(1/2)+1), 1)에서 int(n**(1/2)+1) 값은 루프가 시작되기 전에 계산되고,
          n이 이후에 변경되더라도 range()는 이미 그 초기값을 기준으로 순회를 진행

        while문
        - while 문 내부에서 n이 변경되면 다음 번 조건을 체크할 때 n**(1/2) 값이 새로운 n 값에 따라 달라지게 됨.
        (즉, 종료 조건이 계속 달라지게 됨)

"""


def solution(n):
    d = 2
    answer = []
    end = int(n ** (1 / 2) + 1)

    while d < end:
        if n % d == 0:
            answer.append(d)
            n = n // d
        else:
            if d == 2:
                d += 1
            else:
                d += 2

    if n != 1:
        answer.append(n)

    if not answer:
        return [n]

    answer = list(set(answer))
    answer.sort()
    return answer
