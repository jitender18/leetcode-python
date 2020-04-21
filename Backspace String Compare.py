# Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        str1 = ''
        for i in range(len(S)):
            if S[i] != '#':
                str1 += S[i]
            else:
                str1 = str1[:-1]
        str2 = ''
        for i in range(len(T)):
            if T[i] != '#':
                str2 += T[i]
            else:
                str2 = str2[:-1]
        return str1 == str2


########### Other Approach #############

# Time - O(M + N)
# Space - O(M + N)

class Solution(object):
    def backspaceCompare(self, S, T):
        def build(S):
            ans = []
            for c in S:
                if c != '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(S) == build(T)




########### Two Pointer #############

# Time - O(M + N)
# Space - O(1)


class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.izip_longest(F(S), F(T)))