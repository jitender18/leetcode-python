


# Time:  O(n)
# Space: O(n)


# if the cumulative sum upto two indices, say i and j is at a difference of k
# i.e. if sum[i]−sum[j]=k, the sum of elements lying between indices i and j is k.
# start with dict {0:1} to cover the case if number in array == k.

import collections


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        accumulated_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0] += 1
        for num in nums:
            accumulated_sum += num
            result += lookup[accumulated_sum - k]
            lookup[accumulated_sum] += 1
        return result


########################### Other Solutions ##############################

class Solution(object):
    def subarraySum(self, nums, k):
		count = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    count += 1
        return count