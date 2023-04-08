'''
还能修修补补一下
'''
def generateMatrix(n: int):
    matrix = [[0] * n for i in range(n)]
    arr = []
    for i in range(1, n*n+1):
        arr.append(i)
    x, y = 0, n-1

    while x <= y:
        for i in range(x, y+1):
            matrix[x][i] = arr.pop(0)
        for i in range(x+1, y+1):
            matrix[i][y] = arr.pop(0)
        if x < y:
            for i in range(y-1, x, -1):
                matrix[y][i] = arr.pop(0)
            for i in range(y, x, -1):
                matrix[i][x] = arr.pop(0)
        x, y = x+1, y-1

    print(matrix)


def generateMatrix(n: int):
    matrix = [[0] * n for i in range(n)]
    x, y = 0, n-1
    m = 1
    while m < n * n:
        for i in range(x, y+1):
            matrix[x][i] = m
            m += 1
        for i in range(x+1, y+1):
            matrix[i][y] = m
            m += 1
        if x < y:
            for i in range(y-1, x, -1):
                matrix[y][i] = m
                m += 1
            for i in range(y, x, -1):
                matrix[i][x] = m
                m += 1
        x, y = x+1, y-1

    print(matrix)



n = 1
generateMatrix(n)