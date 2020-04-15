# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        ret = False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break

        # revert the change, a clean slate and no side-effect
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return ret

********************** OR ***********************

    def backtrack(self, row, col, suffix):
        """
            backtracking with side-effect,
               the matched letter in the board would be marked with "#".
        """
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True

        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False

        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            # sudden-death return, no cleanup.
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True

        # revert the marking
        self.board[row][col] = suffix[0]

        # Tried all directions, and did not find any match
        return False


####################################################
################ Other Solutions ###################
####################################################


def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res

 










class Solution:
	def exist(self, board, word):
		"""
		:type board: List[List[str]]
		:type word: str
		:rtype: bool
		"""
		letters = len(word)
		# check for longer word than board
		if letters > rows * cols:
			return False

		neighbors = [(0,1),(1,0),(0,-1),(-1,0)]

		# helper functiont to perform dfs
		def dfs(board, word, x, y, streak, count):
			if count == letters:
				return True
			for (x1,y1) in neighbors:
				x2, y2 = x + x1, y + y1
				if 0 <= x2 < rows and 0 <= y2 < cols and (x2, y2) not in streak:
					if board[x2][y2] == word[count]:
						streak.add((x2, y2))
						check = dfs(board, word, x2, y2, streak, count + 1)
						if check:
							return True
						else:
							streak.remove((x2, y2))
			return False

		# call dfs on all cells in board or until we get a hit
		for i in range(rows):
			for j in range(cols):
				if board[i][j] == word[0]:
					streak = {(i, j)}
					check = dfs(board, word, i, j, streak, 1)
					if check:
						return True
		return False



