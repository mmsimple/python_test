def rotate(matrix):
    n = len(matrix)
    matrix_new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            matrix_new[j][n-i-1] = matrix[i][j]

    # 记住要这样写，不能直接等于
    matrix[:] = matrix_new
    return matrix

    # a = 0
    # b = 0
    # for i in range(h):
    #     for j in range(l):
    #         a = matrix[j][l - i]
    #         matrix[j][l - i] = matrix[i][j]



# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotate(matrix)

arr = [5,2,3,5,6,7,8,2,3,4,1]
b = arr.sort()
print(b)

