
# def findDiagonalOrder(mat):
#     l = len(mat[0])
#     h = len(mat)

#     arr = []
#     for i in range(l+h-1):
#         x = 0
#         y = 0
#         if not i % 2:
#             x = i if i < h - 1 else h - 1
#             while x >= 0 and x < h and i - x < l:
#                 y = i - x
#                 arr.append(mat[x][y])
#                 x = x - 1
#         else:
#             y = i if i < l - 1 else l - 1
#             print(y)
#             while y >=0 and y < l and i - y < h:
#                 x = i - y
#                 arr.append(mat[x][y])
#                 y = y - 1
            
#     print(arr)


# 减少了很多不必要的计算和判断
def findDiagonalOrder(mat):
    ans = []
    m, n = len(mat), len(mat[0])
    for i in range(m + n - 1):
        if i % 2:
            x = 0 if i < n else i - n + 1
            y = i if i < n else n - 1
            while x < m and y >= 0:
                ans.append(mat[x][y])
                x += 1
                y -= 1
        else:
            x = i if i < m else m - 1
            y = 0 if i < m else i - m + 1
            while x >= 0 and y < n:
                ans.append(mat[x][y])
                x -= 1
                y += 1
    return ans


# mat = [[1,2,3],[4,5,6],[7,8,9]]
# mat = [[1,2],[3,4]]
mat = [[2,3]]
findDiagonalOrder(mat)