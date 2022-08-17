# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # two-pointer:
        #   have two pointers, l and r, that start at the beginning of the sorted list
        #   compare l and r. append the smaller value to a new list
        #   repeat until both pointers have no next
        #
        # time:  O(n+m) where n and m represent the size of the two lists
        # space: O(n+m) because we initialize a new list
        
        # in-place soln:
        #   compare the two first nodes. the lowest one will act as our inplace list
        #   compare the two values. 
        
        if not list1: return list2
        if not list2: return list1

        left = list1
        right = list2
        
        if left.val <= right.val:
            head = list1
            left = left.next
            while left and right:
                if left.val <= right.val:
                    list1.next = left
                    left = left.next
                    list1 = list1.next
                else:
                    list1.next = right
                    right = right.next
                    list1 = list1.next
            if left:
                list1.next = left
            if right:
                list1.next = right
            return head
        else:
            head = list2
            right = right.next
            while left and right:
                if left.val <= right.val:
                    list2.next = left
                    left = left.next
                    list2 = list2.next
                else:
                    list2.next = right
                    right = right.next
                    list2 = list2.next
            if left:
                list2.next = left
            if right:
                list2.next = right
            return head
