# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return -2147483648
        maxsum = cursum = nums[0]
        for i in range(1, len(nums)):
            cursum = max(cursum+nums[i], nums[i])
            maxsum = max(cursum, maxsum)
        return maxsum



 ###########################
 ##### Kadane Algo #########
 ###########################


 class Solution(object):
	def maxSubArray(self, nums):
		for i in range(1, len(nums)):
			if nums[i - 1] > 0: 
				nums[i] += nums[i - 1]
		return max(nums)



 #############################
 ##### Divide n conquer ######
 #############################


class Solution:
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)