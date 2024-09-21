"""
    문제: 전화번호 목록
    출처: 프로그래머스 (https://school.programmers.co.kr/learn/courses/30/lessons/42577)

    문제 풀이:
        관련 개념 - 문자열 정렬
"""


def solution(phone_book):
    if len(phone_book) == 1:
        return True

    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i].startswith((phone_book[i - 1])):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
print(solution(["12"]))
