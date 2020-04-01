# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def paren(s='', left=0, right=0):
            if len(s) == 2*n:
                ans.append(s)
                return
            if left < n:
                paren(s+'(', left+1, right)
            if right<left:
                paren(s+')', left, right+1)
        paren()
        return ans