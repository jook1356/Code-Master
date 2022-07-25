N = int(input())
data_length = []
top_data_arr = []
bottom_data_arr = []
top_data = []
bottom_data = []
multiply = 0
multiply_arr = []
result = -99999999

#----------------------------------------------------------------------------------------
# 윗 열과 아래 열의 숫자를 정의, 
for i in range(N):
    data_length.append(input())
    top_data_arr.append(str(input()).split(' '))
    bottom_data_arr.append(str(input()).split(' '))
#--------------------------------------------------------------------------------------
for i in range(N):
    top_data = top_data_arr[i]
    bottom_data = bottom_data_arr[i]
    diff = abs(len(bottom_data) - len(top_data))

    if len(bottom_data) > len(top_data): # 윗 열의 숫자 개수가 더 적으면
        for j in range(diff + 1): # 윗 열과 아래 열의 숫자 개수 차이만큼 반복
            for k in range(len(top_data)): # 윗 열의 숫자의 개수만큼 반복
                multiply += int(top_data[k]) * int(bottom_data[k + j])
            multiply_arr.append(multiply)
            multiply = 0
    else: # 아래 열의 숫자 개수가 더 적으면
        for j in range(diff + 1): # 윗 열과 아래 열의 숫자 개수 차이만큼 반복
            for k in range(len(bottom_data)): # 아래 열의 숫자의 개수만큼 반복
                multiply += int(top_data[k + j]) * int(bottom_data[k])
            multiply_arr.append(multiply)
            multiply = 0

    for k in multiply_arr: # 리스트중 가장 큰 값의 숫자를 찾는다.
        if result < k:
            result = k

    print(f'#{i+1} {result}')

    multiply_arr = [] # 결과 초기화 후 다음 # 으로 넘어간다.
    result = -99999999
