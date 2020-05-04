# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.


# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        sum = list(grid[0])
        for j in xrange(1, len(grid[0])):
            sum[j] = sum[j - 1] + grid[0][j]

        for i in xrange(1, len(grid)):
            sum[0] += grid[i][0]
            for j in xrange(1, len(grid[0])):
                sum[j] = min(sum[j - 1], sum[j]) + grid[i][j]

        return sum[-1]