from asyncio import constants
import time
import itertools
import random
import sys
import csv

# Check valid box or invalid box
def checkValid(board, num , pos):
    # Check column
    res = 0
    for i  in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i and num != 0:
            res += 1
    # Check row
    for i  in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i and num != 0:
            res += 1 
        
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
         for j in range(box_x * 3, box_x * 3 + 3):
             if board[i][j] == num and (i,j) != pos and num != 0:
                 res += 1
             
    return res
# Check empty box
def findEmpty(board):
    res =[]
    
    for i in range(len(board)):
        minires = []
        for j in range(len(board[0])):
            if board[i][j] == 0:
               minires += [j]
        res.append(minires)
    return res

# Find valid value for a box
def findSol_list(bo):
    res =[]
    for i in range(len(bo)):
        res.append(findNum(bo[i]))
    
    return res
# Evaluation Function for Hill Climbing algorithms
def checkPoint(bo):
    res = 0
    for i in range(len(bo)):
        for j in range(len(bo)):
            res += checkValid(bo,bo[i][j],(i,j)) 
            
    return res
# Check valid value of a box
def findNum(col):
    res =[]
    for i in range (1,10):
        if i not in col:
            res += [i] 
    return res
# Hill Climbing algorithms
def solve1(bo):
    z = 0
    prob = bo
    pos_list = findEmpty(bo)
    for i in range(0,9):
        
        for j in pos_list[i]:
            bo[i][j]= random.randint(1,9)
        while checkPoint(bo) != 0:
            if z > 200: break
            for j in pos_list[i]:
                bo[i][j]= random.randint(1,9)
            for j in pos_list[i]:
                for l in range (9,0,-1):
                    if l != bo[i][j]:
                        temp = checkPoint(bo)
                        temp1 = bo[i][j]
                        bo[i][j] = l
                        if checkPoint(bo) > temp:
                            bo[i][j] = temp1
            z = z+1
    # print(bo[0])
    if z == 201:
        return False
    else: return True

test1 = [ [0,0,3,5,1,0,6,2,8],
    [2,9,0,0,0,3,7,0,0],
    [0,0,0,0,4,0,0,0,5],
    [0,4,7,0,3,8,2,0,0],
    [5,1,2,6,0,7,0,4,0],
    [6,0,0,0,0,5,0,9,0],
    [7,8,0,0,0,0,0,6,0],
    [0,0,6,9,0,0,5,0,1],
    [1,0,4,2,7,0,3,0,0]]

test2 = [ [2,3,0,1,0,0,4,0,8],
    [7,0,5,0,0,2,0,6,0],
    [0,1,0,0,8,9,0,5,0],
    [0,0,6,3,0,7,0,0,2],
    [0,7,3,0,4,8,0,0,1],
    [8,4,0,0,9,0,0,0,5],
    [4,6,8,0,0,3,0,0,7],
    [0,0,1,5,7,0,9,0,0],
    [9,0,0,0,0,6,3,2,0]]
test3 =  [ [0,9,0,2,0,0,7,1,4],
    [0,0,8,7,0,6,0,0,3],
    [0,2,5,0,4,3,0,9,0],
    [2,0,0,0,0,0,8,6,0],
    [3,5,0,9,7,0,1,0,0],
    [0,4,1,0,5,2,0,0,7],
    [0,3,0,8,1,4,5,0,6],
    [1,0,0,0,0,0,0,2,9],
    [0,6,7,3,0,0,0,0,0]]

test4 =  [ [0,5,6,8,0,7,3,0,0],
    [0,2,0,3,0,0,9,0,0],
    [0,0,4,0,6,2,0,7,1],
    [0,8,0,0,2,5,1,0,7],
    [3,0,0,0,4,0,0,6,0],
    [0,7,0,1,0,0,2,9,4],
    [5,0,1,0,3,6,0,8,0],
    [8,9,3,0,7,1,0,2,5],
    [0,0,0,9,0,0,4,0,0]]

test5 =  [ [8,0,1,0,3,0,2,0,0],
    [3,0,0,9,1,0,0,5,7],
    [5,0,0,4,0,6,9,1,0],
    [6,3,0,0,0,0,4,0,2],
    [0,0,5,0,2,0,0,8,9],
    [0,8,0,3,7,9,1,0,0],
    [9,0,0,1,0,7,6,0,8],
    [2,4,0,5,6,0,0,0,0],
    [0,7,0,0,0,8,0,3,0]]

test6 =  [ [0,5,7,0,0,9,0,8,0],
    [6,0,8,0,3,2,0,7,0],
    [9,4,0,0,0,6,1,0,5],
    [0,7,0,1,0,3,5,0,0],
    [4,0,0,8,0,0,6,0,0],
    [0,2,5,0,7,0,0,9,3],
    [2,6,1,0,4,7,3,0,8],
    [0,0,0,0,6,1,0,2,4],
    [0,3,0,0,5,0,9,0,0]]

test7 =  [ [0,2,3,7,0,0,0,6,0],
    [6,0,0,0,2,0,0,3,0],
    [1,0,4,0,9,6,0,7,0],
    [0,0,5,0,0,2,4,0,0],
    [0,7,0,0,0,0,0,0,8],
    [0,0,9,1,8,0,0,2,0],
    [3,1,0,6,0,0,0,0,0],
    [0,0,6,0,0,0,9,4,0],
    [0,0,0,5,7,1,0,0,0]]

test8 =  [ [6,1,5,0,4,0,0,3,0],
    [2,0,4,0,8,6,1,0,9],
    [8,0,9,1,0,7,0,4,0],
    [0,0,6,0,7,8,0,2,0],
    [0,5,2,0,6,0,9,0,8],
    [3,0,8,9,0,2,0,7,0],
    [9,0,1,7,3,0,2,0,0],
    [0,2,7,8,0,5,0,0,1],
    [0,8,0,6,0,0,7,0,4]]

test9 =  [ [0,6,0,0,7,4,0,0,8],
    [0,7,5,0,3,0,0,0,1],
    [4,0,2,9,6,0,0,0,3],
    [2,0,8,0,0,5,4,0,0],
    [0,0,7,2,9,0,0,1,5],
    [0,3,1,0,0,8,9,6,0],
    [0,0,0,3,2,9,0,0,6],
    [0,0,9,1,0,6,5,7,0],
    [8,1,0,4,0,0,0,2,0]]

test10 =  [ [0,1,0,0,4,0,0,8,5],
    [3,0,6,2,0,0,0,9,0],
    [0,2,0,0,1,0,0,3,0],
    [0,0,4,0,0,2,6,0,0],
    [1,0,0,0,0,5,0,0,9],
    [0,0,0,8,0,0,7,0,4],
    [0,6,0,0,0,0,8,0,1],
    [0,9,0,7,3,0,0,0,2],
    [0,0,5,6,0,0,0,0,0]]

test11 =  [ [0,5,0,1,3,0,4,0,8],
    [0,8,9,0,5,2,0,6,0],
    [3,0,6,9,7,0,1,0,0],
    [9,0,0,0,8,0,0,5,4],
    [0,7,2,0,0,4,0,0,1],
    [0,1,0,6,0,3,8,7,0],
    [7,0,0,0,1,5,9,0,0],
    [0,0,0,8,0,0,3,0,2],
    [4,3,1,0,6,0,0,0,7]]

test12 =  [ 
    [0,8,6,0,0,1,0,0,0],
    [7,0,0,5,0,0,0,9,2],
    [0,0,9,0,7,0,3,0,0],
    [1,9,0,0,2,0,4,0,0],
    [0,0,0,0,3,0,0,0,9],
    [0,7,0,8,4,0,0,5,0],
    [4,2,0,0,0,6,0,8,0],
    [0,5,7,0,0,0,1,0,0],
    [6,0,0,9,0,3,0,7,0]]
test13 =  [ 
    [0,0,0,0,0,0,0,8,5],
    [0,0,6,0,0,2,0,0,4],
    [0,0,9,3,7,0,0,0,0],
    [3,7,0,0,1,9,0,0,0],
    [2,1,0,0,0,0,6,3,0],
    [0,0,0,4,0,0,5,0,0],
    [8,0,1,0,6,0,9,0,0],
    [0,5,0,8,4,0,2,0,0],
    [7,0,0,0,3,0,0,0,1]]

test14 =  [ 
    [0,7,5,9,0,3,8,0,1],
    [3,8,0,0,2,0,0,4,0],
    [1,0,6,5,0,7,9,0,0],
    [0,2,7,0,0,8,4,5,0],
    [0,0,3,7,0,0,6,0,8],
    [9,1,0,4,6,0,3,7,0],
    [7,0,2,3,5,0,0,8,0],
    [0,9,1,0,7,4,0,3,6],
    [5,0,4,8,1,0,2,0,7]]

test15 =  [ 
    [0,0,2,0,3,4,0,0,7],
    [6,0,0,8,0,0,5,0,0],
    [0,3,0,0,1,0,0,9,0],
    [0,0,3,0,0,0,9,7,8],
    [0,4,9,0,7,0,2,0,0],
    [8,0,0,0,0,0,0,1,0],
    [0,9,4,0,0,0,0,2,0],
    [0,0,0,0,6,5,0,0,0],
    [7,0,8,2,0,0,0,3,5]]

test_case = [test1, test2, test3, test4, test5, test6, test7, test8, test9, test10, test11, test12, test13, test14, test15]
Result = []
for i in range(len(test_case)):
    print("Testcase {}:".format(i+1))
    for row in test_case[i]:
        print(row)
    time_start = time.time()
    result = solve1(test_case[i])
    time_run = time.time()-time_start
    if result:
        print("Result: ")
        for row in test_case[i]:
            print(row)
    else: print("No solution for problem")
    print("Time run = ",end="")
    print(time_run)
    print("Mem memorry usage = ",end="")
    print(sys.getsizeof(result))
    temp = {"Test case": i+1, "Time run": time_run, "Memory": sys.getsizeof(result), "Solution": result}
    Result.append(temp)

# Write information into CSV file
csv_file = r"Sudoku\Result_HillClimbing.csv"
fields = ['Test case', 'Time run', 'Memory','Solution']
with open(csv_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for result in Result:
        writer.writerow(result)



# TEST
# board = [ 
#     [3,6,2,0,1,0,8,5,4],
#     [0,5,0,4,0,8,0,2,0],
#     [0,0,0,0,0,0,0,0,0],
#     [6,0,5,9,0,1,2,0,8],
#     [2,0,0,0,0,0,0,0,6],
#     [8,0,3,2,0,6,9,0,5],
#     [0,0,0,0,0,0,0,0,0],
#     [0,2,0,8,0,4,0,3,0],
#     [4,3,9,0,2,0,1,8,7]]
# time_start = time.time()
# result = solve1(board)
# time_run = time.time()-time_start
# print("Testcase:")
# for row in board:
#     print(row)
# print()
# if result:
#     print("Result:")
#     for row in board:
#         print(row)
# else: print("No solution for problem")
# print("Time run = ",end="")
# print(str(time_run))
# print("Mem memorry usage = ",end="")
# print(sys.getsizeof(result))