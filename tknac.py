# Austin Liu
# tknac.py

import tkinter as tk
import random

board = [[" "," "," "],[" "," "," "],[" "," "," "]]
pos = [[[50, 50],[150, 50],[250, 50]],[[50, 150],[150, 150],[250, 150]],[[50, 250],[150, 250],[250, 250]]]

root = tk.Tk()
root.title("Tic Tac Toe")
canvas = tk.Canvas(root, width=300, height = 300)
l1 = canvas.create_line(98, 0, 98, 300, fill="black", width=4)
l2 = canvas.create_line(198, 0, 198, 300, fill="black", width=4)
l3 = canvas.create_line(0, 98, 300, 98, fill="black", width=4)
l4 = canvas.create_line(0, 198, 300, 198, fill="black", width=4)

dif = None

def destroydif():
    easy.destroy()
    medium.destroy()
    impossible.destroy()

def difsele():
    global dif
    dif = 0
    destroydif()
    canvas.bind('<Button-1>', boardInput)
    canvas.pack()

def difselm():
    global dif
    dif = 1
    destroydif()
    canvas.bind('<Button-1>', boardInput)
    canvas.pack()

def difseli():
    global dif
    dif = 2
    destroydif()
    canvas.bind('<Button-1>', boardInput)
    canvas.pack()

easy = tk.Button(root, text="Easy", width=20, font=("Segoe UI", 15, "bold"), bg="Green", command = difsele)
medium = tk.Button(root, text="Medium", width=20, font=("Segoe UI", 15, "bold"), bg="Yellow", command = difselm)
impossible = tk.Button(root, text="Impossible", width=20, font=("Segoe UI", 15, "bold"), bg="Red", command = difseli)
easy.pack(padx=50, pady=20)
medium.pack(padx=50, pady=20)
impossible.pack(padx=50, pady=20)

def pr(gameBoard):
    displayBoard()
    checkWin(gameBoard)

def circle(canvas, x, y, r):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")
    return

def draw_x(canvas, x, y):
    canvas.create_line(x-40, y-40, x+40, y+40, fill="red", width=4)
    canvas.create_line(x+40, y-40, x-40, y+40, fill="red", width=4)
    return

def displayBoard():
    global board
    global canvas
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'x':
                draw_x(canvas, pos[x][y][0], pos[x][y][1])
            elif board[x][y] == 'o':
                circle(canvas, pos[x][y][0], pos[x][y][1], 40)
    canvas.pack()

def checkWin(gameBoard):
    winArragements = {0:[0,0,0,1,0,2],1:[1,0,1,1,1,2],2:[2,0,2,1,2,2],3:[0,0,1,0,2,0],4:[0,1,1,1,2,1],5:[0,2,1,2,2,2],6:[0,0,1,1,2,2],7:[0,2,1,1,2,0]}
    for x in range(len(winArragements)):
        b = winArragements[x][0]
        c = winArragements[x][1]
        d = winArragements[x][2]
        e = winArragements[x][3]
        f = winArragements[x][4]
        g = winArragements[x][5]
        if gameBoard[b][c] == 'x' and gameBoard[d][e] == 'x' and gameBoard[f][g] == 'x':
            canvas.unbind('<Button-1>')
            canvas.create_rectangle(0, 100, 300, 200, fill="green")
            canvas.create_text(150, 150, text="You Win!", font=("Segoe UI", 24), fill='red')
            return 1
        elif gameBoard[b][c] == 'o' and gameBoard[d][e] == 'o' and gameBoard[f][g] == 'o':
            canvas.unbind('<Button-1>')
            canvas.create_rectangle(0, 100, 300, 200, fill="red")
            canvas.create_text(150, 150, text="AI wins.", font=("Segoe UI", 24), fill='green2')
            return 1
        elif gameBoard[0].count(" ") == 0 and gameBoard[1].count(" ") == 0 and gameBoard[2].count(" ") == 0:
            canvas.unbind('<Button-1>')
            canvas.create_rectangle(0, 100, 300, 200, fill="grey")
            canvas.create_text(150, 150, text="Game was a tie!", font=("Segoe UI", 20), fill='black')
            return 1
        elif x == 7:
            return 0

def boardInput(event):
    global board
    x = event.x
    y = event.y

    if x <= 100:
        if y <= 100:
            if board[0][0] == ' ': board[0][0] = 'x'
            else: return
        elif y <= 200 and board[1][0] == ' ':
            if board[1][0] == ' ': board[1][0] = 'x'
            else: return
        elif board[2][0] == ' ': board[2][0] = 'x'
        else: return
    elif x <= 200:
        if y <= 100 and board[0][1] == ' ':
            if board[0][1] == ' ': board[0][1] = 'x'
            else: return
        elif y <= 200 and board[1][1] == ' ':
            if board[1][1] == ' ': board[1][1] = 'x'
            else: return
        elif board[2][1] == ' ': board[2][1] = 'x'
        else: return
    else:
        if y <= 100 and board[0][2] == ' ':
            if board[0][2] == ' ': board[0][2] = 'x'
            else: return
        elif y <= 200 and board[1][2] == ' ':
            if board[1][2] == ' ': board[1][2] = 'x'
            else: return
        elif board[2][2] == ' ': board[2][2] = 'x'
        else: return
    displayBoard()
    if checkWin(board) == 0: aiPlay(board)

def aiPlay(gameBoard):
    winArragements = {0:[0,0,0,1,0,2],1:[1,0,1,1,1,2],2:[2,0,2,1,2,2],3:[0,0,1,0,2,0],4:[0,1,1,1,2,1],5:[0,2,1,2,2,2],6:[0,0,1,1,2,2],7:[0,2,1,1,2,0]}
    if dif == 0:
        place(gameBoard, random.randint(0, 2), random.randint(0, 2))
        pr(gameBoard)
    elif dif == 1:
        for x in range(8):
            a = winArragements[x][0]
            b = winArragements[x][1]
            c = winArragements[x][2]
            d = winArragements[x][3]
            e = winArragements[x][4]
            f = winArragements[x][5]

            if gameBoard[a][b] == 'x' and gameBoard[c][d] == 'x' and gameBoard[e][f] == " ":
                gameBoard[e][f] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'x' and gameBoard[e][f] == 'x' and gameBoard[c][d] == " ":
                gameBoard[c][d] = "o"
                pr(gameBoard)
                return
            elif gameBoard[c][d] == 'x' and gameBoard[e][f] == 'x' and gameBoard[a][b] == " ":
                gameBoard[a][b] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'o' and gameBoard[c][d] == 'o' and gameBoard[e][f] == " ":
                gameBoard[e][f] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'o' and gameBoard[e][f] == 'o' and gameBoard[c][d] == " ":
                gameBoard[c][d] = "o"
                pr(gameBoard)
                return
            elif gameBoard[c][d] == 'o' and gameBoard[e][f] == 'o' and gameBoard[a][b] == " ":
                gameBoard[a][b] = "o"
                pr(gameBoard)
                return
        place(gameBoard, random.randint(0, 2), random.randint(0, 2))
        pr(gameBoard)
    elif dif == 2:
        pc = {0:[1,1],1:[0,0],2:[0,2],3:[2,0],4:[2,2],5:[0,1],6:[1,0],7:[1,2],8:[2,1]} # Prefers corners
        pm = {0:[1,1],1:[0,1],2:[1,0],3:[1,2],4:[2,1],5:[0,0],6:[0,2],7:[2,0],8:[2,2]} # Prefers middles
        for x in range(8):
            a = winArragements[x][0]
            b = winArragements[x][1]
            c = winArragements[x][2]
            d = winArragements[x][3]
            e = winArragements[x][4]
            f = winArragements[x][5]
            if gameBoard[a][b] == 'x' and gameBoard[c][d] == 'x' and gameBoard[e][f] == " ":
                gameBoard[e][f] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'x' and gameBoard[e][f] == 'x' and gameBoard[c][d] == " ":
                gameBoard[c][d] = "o"
                pr(gameBoard)
                return
            elif gameBoard[c][d] == 'x' and gameBoard[e][f] == 'x' and gameBoard[a][b] == " ":
                gameBoard[a][b] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'o' and gameBoard[c][d] == 'o' and gameBoard[e][f] == " ":
                gameBoard[e][f] = "o"
                pr(gameBoard)
                return
            elif gameBoard[a][b] == 'o' and gameBoard[e][f] == 'o' and gameBoard[c][d] == " ":
                gameBoard[c][d] = "o"
                pr(gameBoard)
                return
            elif gameBoard[c][d] == 'o' and gameBoard[e][f] == 'o' and gameBoard[a][b] == " ":
                gameBoard[a][b] = "o"
                pr(gameBoard)
                return
        for x in range(9):
            if gameBoard[0][0] == 'x' or gameBoard[0][2] == 'x' or gameBoard[2][0] == 'x' or gameBoard[2][2] == 'x':
                a = pm[x][0]
                b = pm[x][1]
            else:
                a = pc[x][0]
                b = pc[x][1]
            if gameBoard[a][b] == " ":
                gameBoard[a][b] = "o"
                pr(gameBoard)
                return

def place(gameBoard, row, column):
    if gameBoard[row][column] == " ":
        gameBoard[row][column] = 'o'
        return
    else:
        place(gameBoard, random.randint(0, 2), random.randint(0, 2))

def close():
    exit()

root.protocol("WM_DELETE_WINDOW", close)

while checkWin(board) == 0:
    root.mainloop()
