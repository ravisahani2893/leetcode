class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        columns = len(board[0])

        for row in range(0,rows):
            self.conquer(board,row,0)
            self.conquer(board,row,columns-1)
            


        for column in range(0,columns):
            self.conquer(board,0,column)
            self.conquer(board,rows-1,column)


        for row in range(0, rows):
            for col in range(0,columns):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] =="#":
                    board[row][col] = "O"
            
            

    def conquer(self, board, row, column):

        
        rows = len(board)
        columns = len(board[0])

        if row < 0 or row >= rows or column < 0 or column >= columns:
            return

        
        if board[row][column] != "O":
            return

       

        board[row][column]="#"


        self.conquer(board,row-1,column)
        self.conquer(board,row+1,column)
        self.conquer(board,row,column-1)
        self.conquer(board,row,column+1)