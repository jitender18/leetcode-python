# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            # to check for odd case, like "aba"
            tmp = self.check_palindrome(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # to check for even case, like "abba"
            tmp = self.check_palindrome(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def check_palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]



#########################################################
################ Dynamic Programming ####################
#########################################################


# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         #1. create a 2D array, size is len(s) * len(s)
#         dp = [[False]*len(s) for _ in range(len(s))]
        
#         #2. initial lcs related char index
#         lcsStartIndex = 0
#         lcsEndIndex = 0
        
#         #3. dp algo
#         """
#             a b a
#             0 1 2
#         a 0 T X X
#         b 1 F T X
#         a 2 T F T
#         """
#         for i in range(len(s)):
#             #what we need is only the left bottom part
#             start = i
#             end = i
#             while start >= 0:
#                 #case1. if sub-string is 'a'
#                 if start == end:
#                     dp[start][end] = True
#                 #case2. if sub-string is 'ab'
#                 #We need this case because start + 1 may larger than end - 1 if using case3 directly
#                 elif start + 1 == end:
#                     dp[start][end] = s[start] == s[end]
#                 #case3. if sub-string is 'aba' 'abac' ..etc, i.e. len(sub) >= 3
#                 else:
#                     dp[start][end] = dp[start+1][end-1] and (s[start] == s[end])
            
#                 #if dp[start][end] is palidromic, check is it longer than current solution
#                 if dp[start][end] and (end - start + 1) > (lcsEndIndex - lcsStartIndex + 1):
#                     lcsStartIndex = start
#                     lcsEndIndex = end
                
#                 start = start - 1
        
#         return s[lcsStartIndex:lcsEndIndex+1]


#########################################################
################ Manacher Algorithm #####################
#########################################################



# class Solution:
#     #Manacher algorithm
#     #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
#     def longestPalindrome(self, s):
#         # Transform S into T.
#         # For example, S = "abba", T = "^#a#b#b#a#$".
#         # ^ and $ signs are sentinels appended to each end to avoid bounds checking
#         T = '#'.join('^{}$'.format(s))
#         n = len(T)
#         P = [0] * n
#         C = R = 0
#         for i in range (1, n-1):
#             P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
#             # Attempt to expand palindrome centered at i
#             while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
#                 P[i] += 1
    
#             # If palindrome centered at i expand past R,
#             # adjust center based on expanded palindrome.
#             if i + P[i] > R:
#                 C, R = i, i + P[i]
    
#         # Find the maximum element in P.
#         maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
#         return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]