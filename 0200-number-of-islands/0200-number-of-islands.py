class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count=0

        for row in range(len(grid)):
            for column in range(len(grid[row])):

                if grid[row][column] == "1":
                    if(self.explore(grid,row,column,visited)):
                        count+=1

        return count
    
    def explore(self,grid,row, column,visited:set):
        rowInBound = row >= 0 and row < len(grid)

        if not rowInBound:
            return False

        columnInBound = column >= 0 and column < len(grid[row])

        if not columnInBound:
            return False

        if grid[row][column] =="0":
            return False

        element = str(row)+","+str(column)
        if element in visited:
            return False

        visited.add(element)
    

        self.explore(grid,row-1,column,visited)
        self.explore(grid,row+1,column,visited)
        self.explore(grid,row,column-1,visited)
        self.explore(grid,row, column+1,visited)

        return True
        