"""
    문제: 가장 큰 수
    출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/42746)

    시도한 풀이:
        문자열로 바꾼 뒤, 사전식 정렬 후 -> 앞의 요소가 뒤의 요소로 시작하는지(startswith())를 판단하며 풀려고 시도
        -> 분기 처리가 많아져, 코드가 복잡해짐

    개선된 풀이:
        1. 모든 문자열에 최대 자릿수(3자리)만큼 곱한다. ex) 30 -> 303030, 300 -> 300300300
        -> 이 값을 int로 비교하여 가장 큰 수를 만들기 위해 알맞은 순서로 정렬할 수 있다.

        2. 비교 함수 구현 및 sort()에 적용

    기타 공부:
        - 람다 함수
        lambda x:x*3 -> x라는 인자를 x*3하여 반환

        - 비교 함수: 두 개의 값을 비교하여 이들 사이의 상대적 순서를 결정하는 함수
        return 값: 1(첫 번째 값이 두 번째 값보다 클 때), 0(두 값 같음), -1(첫 번째 값이 두 번째 값보다 작을 때)

        - sort(key= )
         1) 람다 함수를 기반으로 정렬할 경우, key의 매개변수에 lambda함수를 지정함으로서 간단하게 구현 가능
         lambda를 사용할 때는 각 요소에서 값을 추출하여 그 값을 기준으로 정렬하는 것이므로, 직접 비교 함수가 필요 없기 때문

         2) 비교함수를 기반으로 정렬할 경우, key의 매개변수에 지정할 때 functools.cmp_to_key()와 함께 사용해야함.
            cmp_to_key()는 비교 함수를 키 함수로 변환
"""


### 풀이 1
def solution(numbers):
    nums = [str(x) for x in numbers]
    nums.sort(key=lambda x: x * 3, reverse=True)

    answer = ''.join(nums)

    if int(answer) == 0:
        return "0"

    return answer


### 풀이 2
import functools


def solution2(numbers):
    def comparator(x, y):
        x_y = x + y
        y_x = y + x
        if int(x_y) > int(y_x):
            return 1
        if int(y_x) > int(x_y):
            return -1
        else:
            return 0

    nums = [str(x) for x in numbers]
    nums.sort(key=functools.cmp_to_key(comparator), reverse=True)
    answer = ''.join(nums)
    if int(answer) == 0:
        return "0"
    return answer
