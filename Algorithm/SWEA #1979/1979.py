T = int(input())
result = 0
for i in range(T):
    N, K = map(int,input().split())
    arr = [list(map(int,input().split())) for r in range(N)]

    for j in range(N):
        digit_num = 0
        for k in range(N):
            if arr[j][k] == 1:
                digit_num += 1
            if arr[j][k] == 0 or k == N - 1:
                if digit_num == K:
                    result += 1
                digit_num = 0

        for k in range(N):
            if arr[k][j] == 1:
                digit_num += 1
            if arr[k][j] == 0 or k == N - 1:
                if digit_num == K:
                    result += 1
                digit_num = 0

    print(f'#{i+1} {result}')
    result = 0
    arr = []


