# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        
        curr = head
        prev = None
        
        while head.next:
            temp_next = head.next
            
            head.next = prev
            
            prev = head
            curr = head.next
            head = temp_next
            
        head.next = prev
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # brute force:
        #   iterate through the list
        #   keep track of the previous node
        #   set the current's next to the previous
        # time:  O(n) 
        # space: O(n) because we're basically copying the list
        
        # better space:
        #   point the current node at the previous node
        #   - initialize prev to none
        #   - keep track of next (iter) because we will reassign current.next
        
        if not head:
            return None
        if not head.next:
            return head
        
        prev = None
        while head.next:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        head.next = prev
        return head
        
