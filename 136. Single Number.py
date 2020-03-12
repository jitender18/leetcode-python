
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4



def singleNumber(self, nums: List[int]) -> int:
    dic = {}
    for i in nums:
        if i in dic:
            del dic[i]
        else:
            dic[i] = 1
    return list(dic.keys())[0]



##########################
##### Other solutions ####
##########################

# def singleNumber1(self, nums):
#     dic = {}
#     for num in nums:
#         dic[num] = dic.get(num, 0)+1
#     for key, val in dic.items():
#         if val == 1:
#             return key



####### Elegant one-liner ############

# def singleNumber(self, nums):
#     return sum(list(set(nums)))*2 - sum(nums)






# def singleNumber(self, nums):
# """
# :type nums: List[int]
# :rtype: int
# """
# single = []
# for item in nums:
#     if item not in single:
#         single.append(item)
#     else:
#         single.remove(item)
# return single[0]