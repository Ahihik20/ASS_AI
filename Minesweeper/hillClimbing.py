import random
import math
import copy
import time
import sys

def goalState(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "E" or board[row][col] == "M" or board[row][col] == "-1":
                continue
            mines = countMines(board, row, col)
            if str(mines) != board[row][col]:
                return False
    return True

def countMines(board, row, col):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_row = row + dx
            new_col = col + dy
            if 0<= new_row <len(board) and 0<=new_col<len(board[0]) and board[new_row][new_col] == "M":
                count += 1
    return count

def evaluationFunction(board):
    error = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "E" or board[row][col] == "M" or board[row][col] == "-1":
                continue
            mines = countMines(board, row, col)
            if str(mines) != board[row][col]:
                error += 1
    return error

def emptyList(board):
    listEmpty = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "E":
                listEmpty.append([row,col])
    return listEmpty

def hillClimbing(board):
    if goalState(board):
        return board
    listEmpty = emptyList(board)
    # error = evaluationFunction(board)
    step = 0
    while not goalState(board):
        if step > 200: break
        for position in listEmpty:
            board[position[0]][position[1]] = random.choice(["M","-1"])
        error = evaluationFunction(board)
        if error == 0:
            return board
        for position in listEmpty:
            for value in ["M","-1"]:
                if board[position[0]][position[1]] == value:
                    continue
                else:
                    temp = board[position[0]][position[1]]
                    board[position[0]][position[1]] = value
                    error_check = evaluationFunction(board)
                    if error_check == 0:
                        return board
                    if error_check < error:
                        error = error_check
                    else:
                        board[position[0]][position[1]] = temp
        step += 1   
    return []

#board = [["2","E","E","1","E"],["E","2","3","E","E"],["2","E","E","E","2"],["E","2","2","E","E"],["E","2","E","1","E"]]
board = [["E","E","3","E","3"],["2","E","E","E","E"],["E","2","2","2","E"],["E","E","E","E","E"],["E","1","2","E","1"]]
for row in board:
    print(row)

print()
start_time = time.time()
board = hillClimbing(board)
time_run = time.time()-start_time
if board == []:
    print("No solution for problem")
else:
    for row in board:
        print(row)
print("Time run: ", time_run)
print("Memory uses: ", sys.getsizeof(board), " bytes")

