class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        rows, cols, = len(board), len(board[0])


        def search(r, c, i):

            if not 0 <= r < rows or not 0 <= c < cols or board[r][c] != word[i]:
                return False
                        
            if i == len(word) - 1:
                return True

            
            tmp, board[r][c] = board[r][c], '/'

            res = search(r + 1, c, i + 1) or \
                search(r - 1, c, i + 1) or \
                search(r, c + 1, i + 1) or \
                search(r, c - 1, i + 1)

            board[r][c] = tmp
            return res


        for r in range(rows):
            for c in range(cols):
                if search(r, c, 0):
                    return True

        return False
