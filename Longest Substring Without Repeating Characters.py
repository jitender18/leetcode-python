# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        if s == " ":
            return 1
        
        seen = ''
        mx = 0
		#1. for each character in s
        for c in s:
			#2. check if c is seen
            if c not in seen:
			#3. if not seen, add to seen list 
                seen+=c
            #4 if seen, slice seen list to previous c
            # for example, if c is 'a' and seen list is 'abc'
            # you will be slicing previous 'a'(seen.index(c)+1), thus seen list become 'bc'
            # then add the current 'a' bc + a, seenlist = 'bca'
            else:
                seen = seen[seen.index(c) + 1:] + c
            #5 check max length between current max with new length of seen
            mx = max(mx, len(seen))
        return mx



###################################
########## Other Solutions ########
###################################



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result=0
        temp=[]
        for item in s:
            if item in temp:
                if len(temp)>result:
                    result=len(temp)
                temp=temp[temp.index(item)+1:]
                temp.append(item)
            else:
                temp.append(item)
        return max(len(temp),result)




# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            if visited[ord(char)]:
                while char != s[start]:
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
        return longest

