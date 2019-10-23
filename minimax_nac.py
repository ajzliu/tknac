board = [[None for x in range(3)] for x in range(3)]

def check_win(gameBoard):
    winArragements = {0:[0,0,0,1,0,2],1:[1,0,1,1,1,2],2:[2,0,2,1,2,2],3:[0,0,1,0,2,0],4:[0,1,1,1,2,1],5:[0,2,1,2,2,2],6:[0,0,1,1,2,2],7:[0,2,1,1,2,0]}
    for x in range(len(winArragements)):
        b = winArragements[x][0]
        c = winArragements[x][1]
        d = winArragements[x][2]
        e = winArragements[x][3]
        f = winArragements[x][4]
        g = winArragements[x][5]
        if gameBoard[b][c] == 'x' and gameBoard[d][e] == 'x' and gameBoard[f][g] == 'x':
            return -1
        elif gameBoard[b][c] == 'o' and gameBoard[d][e] == 'o' and gameBoard[f][g] == 'o':
            return 1
        elif gameBoard[0].count(None) == 0 and gameBoard[1].count(None) == 0 and gameBoard[2].count(None) == 0:
            return 0
        elif x == 7:
            return None

def display_board(board):
    print("┌" + "─┬" * 2 + "─┐")
    for x in range(3):
        print("│", end="")
        for cell in board[x]:
            if cell == None:
                print(" │", end="")
            else:
                print(cell + "│", end="")
        if x == 2:
            print("\n" + "└" + "─┴" * 2 + "─┘")
        else:
            print("\n" + "├" + "─┼" * 2 + "─┤")

def minimax(board, side='o'):
    # Assuming this will only be called when the AI (O) is playing
    if check_win(board) != None:
        return (-1, -1, check_win(board))
    else:
        values = []
        for row in range(3):
            for column in range(3):
                if board[row][column] == None:
                    board[row][column] = side
                    if side == 'o':
                        values.append((row, column, minimax(board, 'x')[2]))
                    if side == 'x':
                        values.append((row, column, minimax(board, 'o')[2]))
                    board[row][column] = None
        if side == 'o':
            return max(values, key=lambda x: x[2])
        elif side == 'x':
            return min(values, key=lambda x: x[2])

def place(board):
    while True:
        while True:
            row = input("Row (0-2): ")
            try:
                row = int(row)
                break
            except:
                continue
        while True:
            column = input("Column (0-2): ")
            try:
                column = int(column)
                break
            except:
                continue
        if board[row][column] != None:
            print("Not an empty cell!")
            continue
        else:
            board[row][column] = 'x'
            break

if __name__ == "__main__":
    while check_win(board) == None:
        display_board(board)
        place(board)
        move = minimax(board)
        board[move[0]][move[1]] = 'o'
    if check_win(board) == 1:
        print("{:*^80}".format("AI Wins!"))
    elif check_win(board) == -1:
        print("{:*^80}".format("Player Wins!"))
    else:
        print("{:*^80}".format("Tie!"))