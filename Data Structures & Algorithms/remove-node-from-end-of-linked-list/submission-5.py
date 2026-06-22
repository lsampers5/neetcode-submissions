# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0

        while current:
            current = current.next
            length += 1
        
        if length == n:
            return head.next
        # Length is indexes
        cutIndex = length - n 

        if not head.next:
            return None
        current = head
        new = ListNode(0)
        while current:
            cutIndex -= 1
            prev = current
            current = current.next
            if cutIndex == 0:
                current = current.next
                prev.next = current
            
        return head

