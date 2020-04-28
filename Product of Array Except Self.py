# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = []
        n = len(nums)
        p = 1
        
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        
        p = 1
        
        for i in range(n-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        
        return output




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # define left and right array
        if not nums:
            return 
        
        Left = [1] * len(nums)
        Right = [1] * len(nums)
        
        # calculate to the right
        for i in range(1, len(nums)):
            Left[i] = nums[i-1] * Left[i-1]
            
        for j in reversed(range(0, len(nums)-1)):
            Right[j] = nums[j+1] * Right[j+1]
        
                          
        for k in range(len(nums)):
            nums[k] = Left[k] * Right[k]
        
        
        
        return nums