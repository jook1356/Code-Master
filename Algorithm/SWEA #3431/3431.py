T = int(input())

for i in range(T):
    case_time = list(map(int,input().split()))
    
    if case_time[1] >= case_time[2] >= case_time[0]:
        result = 0
    elif case_time[2] < case_time[0]:
        result = case_time[0] - case_time[2]
    elif case_time[2] > case_time[1]:
        result = -1
    
    print(f'#{i+1} {result}')