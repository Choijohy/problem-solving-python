"""
    문제명: 기능개발
    출처: https://school.programmers.co.kr/learn/courses/30/lessons/42586

    풀이 설명
        관련 개념: 큐
        - 맨 앞 요소에 대한 insert, pop 연산이 필요 없으므로 list를 통한 큐 구현
          1) 비교적 구현이 쉽고 간단
          2) 맨 마지막 요소에 대한 삽입 및 삭제 연산:  O(1)
"""
from math import ceil


def solution(progresses, speeds):
    answer = []

    cnt = 0
    temp = 0
    max_pre = ceil((100 - progresses[0]) / speeds[0])
    for i in range(len(progresses)):
        temp = ceil((100 - progresses[i]) / speeds[i])
        if temp <= max_pre:
            cnt += 1
        else:
            answer.append(cnt)
            max_pre = temp
            cnt = 1

    if temp <= max_pre:
        answer.append(cnt)
    return answer
