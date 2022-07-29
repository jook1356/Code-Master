T = int(input())

for i in range(T):
    N = int(input())
    block_list = []
    while len(block_list) != N:
        block_list = list(map(int,input().split()))
    block_list.append(block_list[len(block_list)-1])
    
    up_max = 0
    down_max = 0

    for j in range(len(block_list)-1):
        if block_list[j+1] > block_list[j] and (block_list[j+1] - block_list[j]) > up_max:
            up_max = block_list[j+1] - block_list[j]
        if block_list[j+1] < block_list[j] and (block_list[j] - block_list[j+1]) > down_max:
            down_max = block_list[j] - block_list[j+1]
        
    print(f'#{i+1} {up_max} {down_max}')

    