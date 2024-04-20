import copy
import time
import sys
import csv

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
test1 = [["2","E","E","1","E"],
         ["E","2","3","E","E"],
         ["2","E","E","E","2"],
         ["E","2","2","E","E"],
         ["E","2","E","1","E"]]

test2 = [["E","E","2","E","1"],
         ["1","E","E","E","E"],
         ["E","1","3","3","E"],
         ["2","E","3","E","2"],
         ["E","3","E","E","E"]]

test3 = [["2","E","2","1","E"],
         ["E","E","E","E","E"],
         ["E","E","E","1","E"],
         ["2","E","1","E","E"],
         ["E","2","1","2","E"]]

test4 = [["E","1","E","E","2"],
         ["E","E","2","E","E"],
         ["E","E","2","E","E"],
         ["E","2","E","1","1"],
         ["E","2","E","E","1"]]

test5 = [["1","1","1","1","E"],
         ["1","E","2","E","E"],
         ["2","E","E","2","E"],
         ["E","E","1","E","E"],
         ["E","1","E","E","1"]] 

test6 = [["E","E","1","E","1"],
         ["3","E","E","E","E"],
         ["E","2","2","E","2"],
         ["2","3","E","E","E"],
         ["E","2","1","2","E"]]

test7 = [["1","E","E","E","E"],
         ["E","E","1","E","1"],
         ["E","E","2","1","E"],
         ["1","1","E","E","E"],
         ["1","E","2","1","E"]]

test8 = [["E","1","2","E","E"],
         ["E","E","2","1","E"],
         ["1","E","E","E","E"],
         ["E","2","1","E","E"],
         ["E","E","1","E","1"]]

test9 = [["E","1","2","E","E"],
         ["2","E","2","3","3"],
         ["E","3","E","E","E"],
         ["E","3","E","3","E"],
         ["E","2","2","E","E"]]

test10 = [["E","E","1","E","1"],
         ["E","1","E","1","1"],
         ["E","1","E","1","E"],
         ["E","1","E","E","1"],
         ["1","1","E","E","E"]]

test11 = [["E","2","1","2","E"],
         ["E","E","E","E","E"],
         ["1","E","2","E","1"],
         ["1","E","E","E","1"],
         ["1","2","E","2","E"]]

test12 = [["1","2","E","E","E"],
         ["1","E","E","3","E"],
         ["1","E","E","3","2"],
         ["E","E","2","E","E"],
         ["1","E","1","1","E"]]
 
test13 = [["E","1","2","E","1"],
         ["E","E","E","E","E"],
         ["E","1","E","1","E"],
         ["E","E","E","1","E"],
         ["1","E","E","1","1"]]
 
test14 = [["1","2","E","1","E"],
         ["1","E","E","E","E"],
         ["2","E","E","2","E"],
         ["1","E","2","3","E"],
         ["E","E","E","2","1"]]

test15 = [["E","1","2","E","1"],
         ["1","E","2","E","E"],
         ["E","E","E","E","1"],
         ["E","E","E","E","E"],
         ["E","2","3","2","E"]]

test_case = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15]
Result = []
check_solution = False
for i in range(len(test_case)):
    print("Testcase {}:".format(i+1))
    for row in test_case[i]:
        print(row)
    time_start = time.time()
    result = dfs(test_case[i])
    time_run = time.time()-time_start
    if result == []:
        print("No solution for problem")
        check_solution = False
    else:
        check_solution = True
        print("Result:")
        for row in result:
            print(row)
    print("Time run = ",end="")
    print(time_run)
    print("Mem memorry usage = ",end="")
    print(sys.getsizeof(result))
    temp = {"Test case": i+1, "Time run": time_run, "Memory": sys.getsizeof(result),"Solution":check_solution}
    Result.append(temp)

# Write information into CSV file
csv_file = r"Minesweeper\Result_DFS.csv"
fields = ['Test case', 'Time run', 'Memory','Solution']
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for result in Result:
        writer.writerow(result)


#Test
# board = [["2","E","2","1","E"],
#          ["E","E","E","E","E"],
#          ["E","E","E","1","E"],
#          ["2","E","1","E","E"],
#          ["E","2","1","2","E"]]
# print("Testcase:")
# for row in board:
#     print(row)

# print()

# start_time = time.time()
# board = dfs(board)
# time_run = time.time()-start_time
# if board == []:
#     print("No solution for problem")
# else:
#     print("Result:")
#     for row in board:
#         print(row)
    
# print("Time run: ", time_run)
# print("Memory uses: ", sys.getsizeof(board), " bytes")