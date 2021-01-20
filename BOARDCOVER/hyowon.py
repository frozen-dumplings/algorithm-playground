dir = (((1, 0), (0, 1)), # ┍
        ((0, 1), (1, 1)),    # ㄱ
        ((1, 0), (1, 1)),    # ㄴ
        ((1, 0), (1, -1))) # ┘

def goNext(H, W, board):
    curRow, curCol = -1, -1
    gotcha = False
    for i in range(H):
        for j in range(W):
            if board[i][j] == '.':
                curRow, curCol = i, j
                gotcha = True
                break
        if gotcha:
            break

    if not gotcha:
        return 1

    ret = 0

    for i in range(4):
        nextRow1, nextCol1 = curRow + dir[i][0][0], curCol + dir[i][0][1]
        nextRow2, nextCol2 = curRow + dir[i][1][0], curCol + dir[i][1][1]

        if not (nextRow1 >= 0 and nextCol1 >= 0 and nextRow2 >= 0 and nextCol2 >= 0 and nextRow1 < H and nextRow2 < H and nextCol1 < W and nextCol2 < W):
            continue

        if board[nextRow1][nextCol1] == '.' and board[nextRow2][nextCol2] == '.':
            board[curRow][curCol] = '#'
            board[nextRow1][nextCol1] = '#'
            board[nextRow2][nextCol2] = '#'

            ret += goNext(H, W, board)

            board[curRow][curCol] = '.'
            board[nextRow1][nextCol1] = '.'
            board[nextRow2][nextCol2] = '.'

    return ret
    

if __name__ == '__main__':
    C = int(input())

    for _ in range(C):
        H, W = map(int, input().split())
        board = []
        for _ in range(H):
            board.append([c for c in input()])

        print(goNext(H, W, board))


