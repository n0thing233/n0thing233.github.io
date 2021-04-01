class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(char):
            for i in range(3):
                if all([board[i][j] == char for j in range(3)]):
                    return True
                if all([board[j][i] == char for j in range(3)]):
                    return True
            if all([board[i][i] == char for i in range(3)]):
                return True
            if all([board[i][2-i] == char for i in range(3)]):
                return True
            return False
        count = collections.defaultdict(int)
        for i in range(3):
            for j in range(3):
                count[board[i][j]] += 1
        if win('X') and win('O'):
            return False
        if win('X') and count['X'] != count['O']+1:
            return False
        if win('O') and count['X'] != count['O']:
            return False
        if count['X'] > count['O'] + 1 or count['X'] < count['O']:
            return False
        return True
