# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        left = dummy
        right = head

    # Move right n steps ahead
        while n > 0:
            right = right.next
            n -= 1

    # Move both until right hits None
        while right:
            left = left.next
            right = right.next

    # Remove the node
        left.next = left.next.next

        return dummy.next