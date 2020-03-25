# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(s) < 2:
            return False
        stk = []
        d = {'}' : '{', ']' : '[', ')' : '('}
        for ch in s:
            if ch in d.values():
                stk.append(ch)
            else:
                if len(stk)>0 and stk[-1] == d[ch]:
                    stk.pop()
                else:
                    return False
        return stk == []



################################################

########## other interesting solution ##########

################################################

 class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False