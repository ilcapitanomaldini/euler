#Quick solution(pen and paper). 20x20 grid,
#so 40 movements total to reach bottom right.
#Selecting the 20x(or y) movements of a total 40,
# 40C20 yields the answer = 137846528820.

#Dynamic solution?
#Seems that as we go down, the cell on the left 
#and right contribute to the new cell's value. 
#Boundary cells do a plus one(lane switcher in between)
#on next boundary cell.

def buildGrid(grid): 
    for row, rowList in enumerate(grid):
        for column, element in enumerate(rowList):
            if (column - 1) < 0 and (row - 1) < 0:
                grid[row][column] = 2
                continue
            if (column - 1) < 0:
                grid[row][column] = grid[row-1][column] + 1
                continue
            if (row - 1 < 0):
                grid[row][column] = grid[row][column-1] + 1
                continue
            grid[row][column] = grid[row][column-1] + grid[row-1][column]
    return grid    

grid = [[0 for x in range(20)] for y in range(20)]
grid = buildGrid(grid)
print(grid[19][19])