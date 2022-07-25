T = int(input())
for i in range(T):
    N = int(input())
    arr_num = []
    result = []
    result_str = ''
    
    for j in range(N):
        arr_num.append(list(map(int,input().split())))

    for rnum in range(len(arr_num[0])):
        result.append([])
    for k in range(len(arr_num[0])):
        for l in range(-1, -len(arr_num[0]) - 1, -1):
            result[k].append(arr_num[l][k])
    for m in range(-1, -len(arr_num[0]) - 1, -1):
        for n in range(-1, -len(arr_num[0]) - 1, -1):
            result[abs(m)-1].append(arr_num[m][n])
    for o in range(-1, -len(arr_num[0]) - 1, -1):
        for p in range(len(arr_num[0])):
            result[abs(o)-1].append(arr_num[p][o])
    print(f'#{i+1}')
    for q in range(len(arr_num[0])):
        for r in result[q]:
            result_str += str(r)
        print(f'{result_str[0:N]} {result_str[N:N*2]} {result_str[N*2:N*3]}')
        result_str = ''