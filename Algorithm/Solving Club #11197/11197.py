T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    print(f'#{i+1}')
    if M == 1:
        for k in range(1, N+1):
            print('*'*k)

    if M == 2:
        for k in range(N,0,-1):
            print('*'*k)

    if M == 3:
        for k in range(1,N*2+1,2):
            blank = ((N*2-1) - k) // 2
            if k == N*2-1:
                print('*'*k)
            else:
                print(' '*(blank-1),'*'*k,' '*(blank-1))