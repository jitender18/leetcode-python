# (This problem is an interactive problem.)

# A binary matrix means that all elements are 0 or 1. 
# For each individual row of the matrix, this row is sorted in non-decreasing order.

# Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed)
# with at least a 1 in it. If such index doesn't exist, return -1.

# You can't access the Binary Matrix directly. 
# You may only access the matrix using a BinaryMatrix interface:

# BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
# BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  
# Also, any solutions that attempt to circumvent the judge will result in disqualification.

# For custom testing purposes you're given the binary matrix mat as input in the following four examples. 
# You will not have access the binary matrix directly.

# Input: mat = [[0,0],[0,0]]
# Output: -1

# Input: mat = [[0,0],[0,1]]
# Output: 1

# Input: mat = [[0,0],[1,1]]
# Output: 0


# Hint:- (Optimal Approach) Imagine there is a pointer p(x, y) starting from top right corner.
# p can only move left or down. If the value at p is 0, move down. If the value at p is 1, move left. 
# Try to figure out the correctness and time complexity of this algorithm.


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        index = -1
        row = 0
        col = binaryMatrix.dimensions()[1] - 1
        while row < binaryMatrix.dimensions()[0] and col >= 0:
            cur = binaryMatrix.get(row, col)
            if cur == 1:
                index = col
                col -= 1
            elif cur == 0:
                row += 1
            else:
                return index
        return index

# Time: O(N+M)
# Space: O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        
        rows, cols = binaryMatrix.dimensions()
        
        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1
        
        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1
        
        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1


# Time: O(N log M)  -   Every binary search O(log M) and doing it N times
# Space: O(1)

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        for row in range(rows):
            # Binary Search for the first 1 in the row.
            lo = 0
            hi = cols - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid
            # If the last element in the search space is a 1, then this row
            # contained a 1.
            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)
        # If smallest_index is still set to cols, then there were no 1's in 
        # the grid. 
        return -1 if smallest_index == cols else smallest_index