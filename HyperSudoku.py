class HyperSudoku:

    @staticmethod
    def isValidInsertion(grid, row, col, value):
        # Loop through a given row/col to check whether the given value is in that row/col or not
        for i in range(9):
            if (grid[row][i] == value or grid[i][col] == value):
                return False
        
        # If the row or col is in the hyper sudoku defined grids, then check for validity
        rowTemp = row
        colTemp = col
        if (rowTemp in [1, 2, 3, 5, 6, 7] and colTemp in [1, 2, 3, 5, 6, 7]):
            # If row is in the first hyper grid, let row be 1, else 5
            if (rowTemp < 4):
                rowTemp = 1
            else:
                rowTemp = 5
        
            # If col is in the first hyper grid, let col be 1, else 5
            if (colTemp < 4):
                colTemp = 1
            else:
                colTemp = 5
    
            for i in range(rowTemp, rowTemp + 3):
                for j in range(colTemp, colTemp + 3):
                    if (grid[i][j] == value):
                        return False
    
        # Gets the 3 by 3 grid in the row and col        
        row = row - row % 3;
        col = col - col % 3;
        
        # Loops through 3 rows of the 3 by 3 grid
        for i in range(row, row + 3):
            # Loops through 3 cols of the 3 by 3 grid
            for j in range(col, col + 3):
                if (grid[i][j] == value):
                    return False
        
        # Return true if the value is not in given row, col nor 3 by 3 grid
        return True
    
    @staticmethod
    def solveHelper(grid):
        # Loop through the rows of the grid (i.e. i = row)
        for i in range(9):
            # Loop through the cols of the grid (i.e. j = col)
            for j in range(9):
                # Check if the value at that row and col is assigned
                if (grid[i][j] == 0):
                    # Loop through all the possible sudoku numbers (i.e. k = 1-9)
                    for k in range(1, 10):
                        # Check if k is a valid insertion for the square at row i and col j
                        if (HyperSudoku.isValidInsertion(grid, i, j, k)):
                            grid[i][j] = k
                            
                            # If the insertion is valid, then we can finish this value, else set it to the unassigned value of 0
                            if (HyperSudoku.solveHelper(grid)[1]):
                                return (grid, True)
                            else:
                                grid[i][j] = 0;
                    return (grid, False) # This causes this function to go back in the DFS of the graph
        return (grid, True)
        
    
    @staticmethod
    def solve(grid):
        """
        Input: An 9x9 hyper-sudoku grid with numbers [0-9].
                0 means the spot has no number assigned.
                grid is a 2-Dimensional array. Look at
                Test.py to see how it's initialized.

        Output: A solution to the game (if one exists),
                in the same format. None of the initial
                numbers in the grid can be changed.
                'None' otherwise.
        """
        
        grid = HyperSudoku.solveHelper(grid)[0]
        
        # If there is a 0 in any of the slots then return None
        for i in range(9):
            for j in range(9):
                if (grid[i][j] == 0):
                    return None
        
        # Return grid if puzzle is solvable
        return grid

    @staticmethod
    def printGrid(grid):
        """
        Prints out the grid in a nice format.
        """
        print("-"*25)
        for i in range(9):
            print("|", end=" ")
            for j in range(9):
                print(grid[i][j], end=" ")
                if (j % 3 == 2):
                    print("|", end=" ")
            print()
            if (i % 3 == 2):
                print("-"*25)
