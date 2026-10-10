class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_verification = {}
        for i in range(9):
            horizontal = {}
            vertical = {}
            for y in range(9):
                ev = vertical.get(board[i][y],0)
                if ev != 0 and board[i][y] != '.':
                    return False
                vertical[board[i][y]] = 1
        
                ehv = horizontal.get(board[y][i],0)
                if ehv != 0 and board[y][i] != '.':
                    return False
                horizontal[board[y][i]] = 1

                v = board[i][y]
                if v != '.':
                    co = tuple([i // 3,y//3])
                    specific_box = box_verification.get(co,None)
                    if specific_box is None:
                        specific_box = {}
                        box_verification[co] = specific_box
                    else:
                        exists = specific_box.get(board[i][y],0) != 0
                        if exists:
                            return False
                    specific_box[v] = 1 
        return True
           
     
                