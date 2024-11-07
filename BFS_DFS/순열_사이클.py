def main():
    test_case_num = int(input())
    for i in range(test_case_num):
        num = int(input())
        arr = list(map(int, input().split()))
        visited = [False]*num
        cnt = 0
        for i in range(num):
            if visited[i] == False:
                current = arr[i]-1
                while (i != current):
                    visited[current] = True
                    current = arr[current] - 1
                cnt += 1
            else:
                continue
        print(cnt)


if __name__ == '__main__':
    main()



