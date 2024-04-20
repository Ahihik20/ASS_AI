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

def createBoard(stack, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "E":
                new_board1 = copy.deepcopy(board)
                new_board2 = copy.deepcopy(board)
                new_board1[i][j] = "M"
                new_board2[i][j] = "-1"
                stack.append(new_board1)
                stack.append(new_board2)
                return

def dfs(board):
    count = 0
    if goalState(board):
        return board    
        print(board)
    stack = []
    stack.append(board)
    while stack:
        temp = stack.pop()
        count +=1
        if goalState(temp):
            return temp
        createBoard(stack, temp)
    print(count)
    return []
    

# board = [["E","E","E","E","E"],["E","E","E","E","E"],["E","1","E","E","E"],["E","E","E","E","E"]]

board = [["2","E","E","1","E"],["E","2","3","E","E"],["2","E","E","E","2"],["E","2","2","E","E"],["E","2","E","1","E"]]

for row in board:
    print(row)

print()

start_time = time.time()
board = dfs(board)
time_run = time.time()-start_time
if board == []:
    print("No solution for problem")
else:
    for row in board:
        print(row)
    
print("Time run: ", time_run)
print("Memory uses: ", sys.getsizeof(board), " bytes")