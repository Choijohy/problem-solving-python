"""
    문제명: 같은 숫자는 싫어
    출처: https://school.programmers.co.kr/learn/courses/30/lessons/12906

    풀이 설명
        관련 개념: 큐
        - 맨 앞 요소에 대한 insert, pop 연산이 필요 없으므로 list를 통한 큐 구현
        - list를 통한 큐 구현 ->
          1) 비교적 구현이 쉽고 간단
          2) 맨 마지막 요소에 대한 삽입 및 삭제 연산: O(1)
          ** 맨 앞 요소에 대한 삽입 및 삭제 연산은 O(n)이므로, 해당 메소드가 필요할 경우 list 사용 지양
"""


def solution(arr):
    answer = []

    pre = arr[0]
    answer.append(pre)

    for e in arr:
        if pre != e:
            answer.append(e)
        pre = e

    return answer
