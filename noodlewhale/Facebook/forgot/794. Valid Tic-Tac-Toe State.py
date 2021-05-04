#1:41 1:55 忘记win function了
#这题有一万种方法，但是最有效的就是come up with win function......死记硬背！
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        def win(c):
            for i in range(3):
                if all([board[i][j] == c for j in range(3)]):
                    return True
                if all([board[j][i] == c for j in range(3)]):
                    return True
            if all([board [i][i] == c for i in range(3)]):
                return True
            if all([board [i][2-i] == c for i in range(3)]):
                return True
            return False
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    x_count += 1
                elif board[i][j] == 'O':
                    o_count += 1
        if o_count > x_count or o_count < x_count - 1:
            return False
        x_win = win('X')
        o_win = win('O')
        if x_win and o_win:
            return False
        elif x_win and o_count != x_count -1:
            return False
        elif o_win and o_count != x_count:
            return False
        return True
