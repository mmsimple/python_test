'''
想法是正确的，就是判断条件错误了，可以多使用变量，无所谓，但要准确
'''
def spiralOrder(matrix):
    m, n = len(matrix), len(matrix[0])
    ans = list()
    left, right, top, bottom = 0, n-1, 0, m-1

    while left <= right and top <= bottom:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        for i in range(top + 1, bottom + 1):
            ans.append(matrix[i][right]) 
        if left < right and top < bottom:
            for i in range(right - 1, left, -1):
                ans.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                ans.append(matrix[i][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1
    print(ans[:m*n])

    return ans[:m*n]

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[6,9,7]]
# matrix = [[6],[9],[7]]
# matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
# matrix = [[2,5],[8,4],[0,-1]]
spiralOrder(matrix)


for i in range(5, 1, -1):
    print(i)