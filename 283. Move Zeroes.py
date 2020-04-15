# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pos += 1



#######################################
########## Other SOlutions ############
#######################################



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        first, second = 0, 1
        while first < second and second < len(nums):
            if nums[first] == 0 and nums[second]!=0:
                nums[first], nums[second] = nums[second], nums[first]
            if nums[first] == 0 and nums[second] == 0:
                second += 1
                continue
            first += 1
            second += 1
        return nums


#######################################
############ One-liners ###############
#######################################

# nums.sort(key= lambda x: 1 if x == 0 else 0)

# OR

# nums.sort(key=bool, reverse=True)