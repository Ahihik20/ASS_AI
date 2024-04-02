class SudokuState:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        
    def is_goal_state(self):
        for row in self.puzzle:
            if 0 in row:
                return False
        return True

    def get_next_empty_cell(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.puzzle[i][j] == 0:
                    return i, j
        return None

    def get_possible_values(self, row, col):
        values = set(range(1, self.size + 1))
        for i in range(self.size):
            values.discard(self.puzzle[row][i])
            values.discard(self.puzzle[i][col])
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                values.discard(self.puzzle[i][j])
        return values

    def generate_successors(self):
        empty_cell = self.get_next_empty_cell()
        if empty_cell:
            row, col = empty_cell
            for value in self.get_possible_values(row, col):
                new_puzzle = [row[:] for row in self.puzzle]
                new_puzzle[row][col] = value
                yield SudokuState(new_puzzle)

    def __lt__(self, other):
        return id(self) < id(other)


def astar_search(initial_state):
    open_list = [initial_state]
    closed_list = set()
    
    while open_list:
        current_state = open_list.pop(0)
        closed_list.add(current_state)
        
        if current_state.is_goal_state():
            return current_state.puzzle
        
        next_empty_cell = current_state.get_next_empty_cell()
        if next_empty_cell is None:
            continue  # No empty cell found in current state, skip to the next state

        for successor in current_state.generate_successors():
            if successor not in closed_list:
                open_list.append(successor)
                open_list.sort(key=lambda x: len(x.get_next_empty_cell() or []), reverse=True)
                
    return None

# Example puzzle
initial_puzzle = [[0,3,9,0,0,0,1,2,0],
      [0,0,0,9,0,7,0,0,0],
      [8,0,0,4,0,1,0,0,6],
      [0,4,2,0,0,0,7,9,0],
      [0,0,0,0,0,0,0,0,0],
      [0,9,1,0,0,0,5,4,0],
      [5,0,0,1,0,9,0,0,3],
      [0,0,0,8,0,5,0,0,0],
      [0,1,4,0,0,0,8,7,0]]

# Solve Sudoku using A*
solution = astar_search(SudokuState(initial_puzzle))
if solution:
    for row in solution:
        print(row)
else:
    print("No solution found.")
