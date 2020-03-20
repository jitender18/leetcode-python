# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


class Solution:
    def trap(self, height: List[int]) -> int:
        
        if len(height) <= 2:
            return 0
        
        left=0
        maxleft=height[:]
        for i in range(len(height)):
            maxleft[i]=left
            if height[i]>left:
                left=height[i]
        right=0
        maxright=height[:]
        for i in range(len(height)-1,-1,-1):
            maxright[i]=right
            if height[i]>right:
                right=height[i]
        res=0
        for ind in range(len(height)):
            if min(maxleft[ind],maxright[ind])>height[ind]:
                res+=min(maxleft[ind],maxright[ind])-height[ind]
        return res