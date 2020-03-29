# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None



# Time:  O(nlogk)
# Space: O(1)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        def merge_two_lists(self, l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val<l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
        
        if not lists:
            return None
        left, right = 0, len(lists)-1
        
        while right>0:
            if left >= right:
                left = 0
            else:
                lists[left] = merge_two_lists(self, lists[left], lists[right])
                left += 1
                right -= 1
        return lists[0]




########################################
######### Divide and Conquer ###########
########################################

# Time:  O(nlogk)
# Space: O(logk)
# Divide and Conquer solution.
class Solution2(object):
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:
                return None
            if begin == end:
                return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))
