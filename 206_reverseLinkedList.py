# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # start at the head of the list
        # iterate through the list
        #   copy the current node
        #   set next of current node to the previous node
        
        if head == None: return None
        
        curr = head
        out = ListNode(head.val)
        prev = None
        while curr:
            out = ListNode(curr.val)
            out.next = prev 
            prev = out
            curr = curr.next
        return out
