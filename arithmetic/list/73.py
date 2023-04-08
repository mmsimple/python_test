'''
o(mn)
'''
# def setZeroes(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     arr = []
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == 0:
#                 arr.append((i, j))

#     for a in arr:
#         for i in range(n):
#             matrix[a[0]][i] = 0
#         for i in range(m):
#             matrix[i][a[1]] = 0

#     print(matrix)


'''
o(m+n)
'''
# def setZeroes(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     row, col = [1] * m, [1] * n
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == 0:
#                 row[i] = col[j] = 0
#     print(row, col)

#     for i in range(m):
#         for j in range(n):
#             if not row[i] or not col[j]:
#                 matrix[i][j] = 0

#     print(matrix)


'''
o(1)
'''
def setZeroes(matrix):
    row = len(matrix)
    col = len(matrix[0])
    row0_flag = False
    col0_flag = False
    # 找第一行是否有0
    for j in range(col):
        if matrix[0][j] == 0:
            row0_flag = True
            break
    # 第一列是否有0
    for i in range(row):
        if matrix[i][0] == 0:
            col0_flag = True
            break

    # 把第一行或者第一列作为 标志位
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    #print(matrix)
    # 置0
    for i in range(1, row):
        for j in range(1, col):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if row0_flag:
        for j in range(col):
            matrix[0][j] = 0
    if col0_flag:
        for i in range(row):
            matrix[i][0] = 0


# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(matrix)
setZeroes(matrix)