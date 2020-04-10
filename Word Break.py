# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false



# Time - O(N^2 * k) - O(N) for string comparison
# Space - O(N)

# The idea is the following:

# d is an array that contains booleans

# d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

# Example:

# s = "leetcode"

# words = ["leet", "code"]

# d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

# d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

# The result is the last index of d.

def word_break(s, words):
 	d = [False] * len(s)    
 	for i in range(len(s)):
 		for w in words:
 			if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
 				d[i] = True
 	return d[-1]