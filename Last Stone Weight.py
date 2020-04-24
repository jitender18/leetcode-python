# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together. 
# Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

# Note:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


# Time:  O(nlogn)
# Space: O(n)

import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        for i in xrange(len(stones)-1):
            x, y = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -abs(x-y))
        return -max_heap[0]



import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_list = [-x for x in stones]
        heapq.heapify(new_list)
        while len(new_list) > 1:
            y = heapq.heappop(new_list)
            x = heapq.heappop(new_list)
            if y != x:
                heapq.heappush(new_list, y-x)
        if len(new_list):
            return -heapq.heappop(new_list)
        return 0

####################### Other solutions ###########################


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        def remove_largest():
            index_of_largest = stones.index(max(stones))
            # Swap the stone to be removed with the end.
            stones[index_of_largest], stones[-1] = stones[-1], stones[index_of_largest]
            return stones.pop()

        while len(stones) > 1:
            stone_1 = remove_largest()
            stone_2 = remove_largest()
            if stone_1 != stone_2:
                stones.append(stone_1 - stone_2)

        return stones[0] if stones else 0



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)
        return stones[0] if stones else 0



class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            arr = stones[2:]
            y = stones[0]
            x = stones[1]
            if x != y:
                arr.append(y-x)
            stones = sorted(arr,reverse=True)
        if stones:
            return stones[0]
        return 0



######################### Bucket sort ###############################

# Time:  O(n + w)
# Space: O(w)
# w is length of the array == maximum element in the list

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Set up the bucket array.
        max_weight = max(stones)
        buckets = [0] * (max_weight + 1)

        # Bucket sort.
        for weight in stones:
            buckets[weight] += 1

        # Scan through the weights.
        biggest_weight = 0 
        current_weight = max_weight
        while current_weight > 0:
            if buckets[current_weight] == 0:
                current_weight -= 1
            elif biggest_weight == 0:
                buckets[current_weight] %= 2
                if buckets[current_weight] == 1:
                    biggest_weight = current_weight
                current_weight -= 1
            else:
                buckets[current_weight] -= 1
                if biggest_weight - current_weight <= current_weight:
                    buckets[biggest_weight - current_weight] += 1
                    biggest_weight = 0
                else:
                    biggest_weight -= current_weight
        return biggest_weight