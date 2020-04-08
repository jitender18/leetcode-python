# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

# Time - O(N * KlogK)
# Space - O(N * K)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        out = collections.defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            out[sorted_s].append(s)
        return out.values()


###########################
##### Other Solutions #####
###########################


class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()



def groupAnagrams(self, strs):
    d = {}
    for w in sorted(strs):
        key = tuple(sorted(w))
        d[key] = d.get(key, []) + [w]
    return d.values()


def anagrams(self, strs):
    count = collections.Counter([tuple(sorted(s)) for s in strs])
    return filter(lambda x: count[tuple(sorted(x))]>1, strs)

# collections.Counter creates a counter object. A counter object is like a specific kind of dictionary where it is build for counting (objects that hashes to same value)
# tuple(sorted(s)) is used here so that anagrams will be hashed to the same value. tuple is used because sorted returns a list which cannot be hashed but tuples can be hashed
# filter: selects some elements of the list based on given function (first argument - a lambda function is given here)
# lambda function defined here returns True if number of anagrams of that elements is greater than 1