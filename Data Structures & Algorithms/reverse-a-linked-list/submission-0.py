# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        current = head
        stack = []
        result = []
        while current:
            
            stack.append(current)
            current = current.next
        
        current = stack.pop()
        head = current

        while stack:
            current.next = stack.pop()
            current = current.next
            
        
        current.next = None
        return head

