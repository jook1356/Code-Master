T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    to_move = N - (M - 1)
    range_aval = 0
    range_list = []
    arr_ground = [list(map(int,input().split())) for tmp in range(N)]
    for j in range(to_move):
        for k in range(to_move):
            for l in range(M):
                for m in range(M):
                    range_aval += arr_ground[j + m][k + l]
            range_list.append(range_aval)
            range_aval = 0
    print(f'#{i+1} {max(range_list)}')
    


