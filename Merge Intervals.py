# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key = lambda x: x[0])
        new_interval = []
        for i in intervals:
            if new_interval and i[0] <= new_interval[-1][-1]:
                new_interval[-1][-1] = max(new_interval[-1][-1], i[-1])
            else:
                new_interval.append(i)
        return new_interval