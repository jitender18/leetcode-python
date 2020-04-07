# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

###########################
##### Heap Solution #######
###########################

def minMeetingRooms(self, intervals):
    intervals.sort(key=lambda x:x.start)
    heap = []  # stores the end time of intervals
    for i in intervals:
        if heap and i.start >= heap[0]: 
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)
        else:
            # a new room is allocated
            heapq.heappush(heap, i.end)
    return len(heap)


###########################
##### Other Solution ######
###########################


 # Time:  O(nlogn)
# Space: O(n)
class Solution2(object):
    # @param {Interval[]} intervals
    # @return {integer}
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        s, e = 0, 0
        min_rooms, cnt_rooms = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                cnt_rooms += 1  # Acquire a room.
                # Update the min number of rooms.
                min_rooms = max(min_rooms, cnt_rooms)
                s += 1
            else:
                cnt_rooms -= 1  # Release a room.
                e += 1

        return min_rooms