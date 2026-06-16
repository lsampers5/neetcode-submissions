# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # This is the fast and slow solution

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                return False
            if fast.next:
                fast = fast.next
            else:
                return False
            if fast == slow:
                return True
        return False
            
            
        