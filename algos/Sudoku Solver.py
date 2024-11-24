class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        ans = []

        def bt():
            for c in range(9):
                for r in range(9):
                    if board[r][c] == ".":  
                        for num in range(1, 10):
                            board[r][c] = str(num)
                            if self.validateSudoku(board):
                                if bt():
                                    return True
                            board[r][c] = "."
                        return False
            return True
        bt()
        return board
        

    def validateSudoku(self, board):

        rowDict = defaultdict(set)
        colDict = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                #Validate rows
                if board[r][c] in rowDict[r]:
                    return False
                rowDict[r].add(board[r][c])

                #Validate cols
                if board[r][c] in colDict[c]:
                    return False
                colDict[c].add(board[r][c])

                #Validate blocks
                currBlock = (r // 3, c // 3)
                if board[r][c] in blocks[currBlock]:
                    return False
                blocks[currBlock].add(board[r][c])
    
        return True


