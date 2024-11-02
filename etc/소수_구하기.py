def solution(numbers):
    numbers = [char for char in numbers]
    # 소수 판별
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** (0.5))+1, 1):
            if n % i == 0:
                return False
        return True

    permutations_list = []

    # 조합 가능한 모든 순열(재귀 호출)
    def gen_permutations(prefix, remaining):
        if prefix != "":
            permutations_list.append(int(prefix))
        for i in range(len(remaining)):
            next_prefix = prefix + remaining[i]
            next_remaining = remaining[:i] + remaining[i + 1:]
            gen_permutations(next_prefix, next_remaining)

    gen_permutations("", numbers)
    cnt = 0

    for num in set(permutations_list):
        if is_prime(int(num)):
            cnt += 1
    return cnt


# test1
# print(solution("011"))

# print(solution("000"))

print(solution("121"))
