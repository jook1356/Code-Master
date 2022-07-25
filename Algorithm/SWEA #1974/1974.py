T = int(input())
arr = []
arr_square = []
scan_num = [[]]
result = 1
def sudoku(x):
    return 1 if len(set(x[0])) == 9 and len(set(x[1])) == 9 and len(set(x[2])) == 9 else 0
    
for i in range(T):
    for j in range(9):
        arr.append(list(map(int,input().split())))
        arr_square.append([])

    for k in range(0,7,3):
        for l in range(9):
            for m in range(3):
                arr_square[round((l+2)/3)+k-1].append(arr[l][k+m])

    for k in range(9):
        scan_num.append(arr[k])
        scan_num.append(arr_square[k])
        for l in range(9):
            scan_num[0].append(arr[l][k])
        if result == 0:
            break
        result = sudoku(scan_num)
        scan_num = [[]]

    print(f'#{i+1} {result}')
    result = 1
    arr = []
    arr_square = []
        


    


# T = int(input())
# arr = []
# arr_square = []
# scan_num = [[]]
# result = 1
# def sudoku(x):
#     return 1 if len(set(x[0])) == 9 and len(set(x[1])) == 9 and len(set(x[2])) == 9 else 0
# for i in range(T):

#     for j in range(9):
#         arr.append(list(map(int,input().split())))
#         arr_square.append([])

#     for k in range(0,7,3):
#         for l in range(9):
#             for m in range(3):
#                 arr_square[round((l+2)/3)+k-1].append(arr[l][k+m])

#     for k in range(9):
#         scan_num.append(arr[k])
#         scan_num.append(arr_square[k])
#         for l in range(9):
#             scan_num[0].append(arr[l][k])
#         if result == 0:
#             break
#         result = sudoku(scan_num)
#         scan_num = [[]]

#     print(f'#{i+1} {result}')
#     result = 1
#     arr = []
#     arr_square = []
        


    
