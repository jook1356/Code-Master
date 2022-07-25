T = int(input())
for i in range(T):
    N, M = map(int,input().split())
    print(f'#{i+1}')
    if M == 4:
        for k in range(N + 1,0,-2):
            print(f"{' '*(((N+1)//2)-(k//2))}{'*'*(k//2)}")
        for l in range(2,((N+4)//2)):
            print(' '*(N//2-1),'*'*l)
    if M == 3:
        for m in range(N,-N-1,-2):
            if m != -1: print(f"{' '*((N-abs(m)) // 2)}{'*'*abs(m)}")
    if M == 2:
        for n in range(N+1,-N-2, -2):
            if n != 0 and n != -2: print(f"{' '*((abs(n)-2)//2)}{'*'*((N+1//2)-(abs(n)//2)-(N//3))}")
    if M == 1:
        for o in range(N+1,-N-2, -2):
            if o != 0 and o != -2: print(f"{'*'*((N+1//2)-(abs(o)//2)-(N//3))}") 