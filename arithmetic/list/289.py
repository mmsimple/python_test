def gameOfLife(board):
    m, n = len(board), len(board[0])
    new_board = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_board[i][j] = board[i][j]

    for i in range(m):
        for j in range(n):
            index = search_alive(i, j, new_board)
            if board[i][j]:
                if index != 2 and index != 3:
                    board[i][j] = 0
            else:
                if index == 3:
                    board[i][j] = 1
    print(board)
    return board

def search_alive(i, j, board):
    m, n = len(board), len(board[0])
    x = (i-1, i, i+1)
    y = (j-1, j, j+1)

    flag = 0
    for col in x:
        for row in y:
            if col >=0 and row >= 0 and col < m and row < n:
                if col == i and row == j:
                    continue
                if board[col][row]:
                    flag += 1
    return flag

'''
用活的细胞影响其他周围八个细胞，当有一个活的，周围八个就加10，两位数，
既记录了本身当前状态，又统计了周围状态，而且只需统计活细胞影响周围的即可。
'''
def gameOfLife(board):
    m=len(board)
    n=len(board[0])

    def affect(x,y):
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                if i<0 or i>=m or j<0 or j>=n or (i==x and j==y):
                    continue
                board[i][j]+=10
    for i in range(m):
        for j in range(n):
            if board[i][j]%10==1:
                affect(i,j)

    def calculate(x,y):
        value=board[x][y]
        if value//10==3:
            board[x][y]=1
        elif value//10==2 and value%10==1:
            board[x][y]=1
        else:
            board[x][y]=0
    for i in range(m):
        for j in range(n):
            calculate(i,j)


# board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[1,1],[1,0]]
gameOfLife(board)