T = int(input())

for i in range(T):
    Hour = map(int,input().split())

    Hour = sum(Hour)

    if Hour >= 24:
        Hour = Hour % 24
    
    print(f'#{i+1} {Hour}')