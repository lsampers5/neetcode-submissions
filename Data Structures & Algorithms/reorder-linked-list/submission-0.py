# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        holder = head
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow =slow.next

        # Reversing slow(Which is halfway) -- Need to clean up variables
        prev = None
        current = slow
        
        while current:
            next = current.next
            current.next = prev
            prev = current 
            current = next

        l2 = prev

        l1 = holder

        # So now we have newHead which is the reverse half    l2 == 10 -> 8 -> 6 -> None
        # We have the og list to which is the whole thing     l1 == 2 -> 4 -> 6 -> 8 -> 10 -> None

        # Figured it out - once 
        new = ListNode(0)

        while l1 and l2:
            if l2.val == l1.val:
                new.next = l2
                l2 = l2.next
                new = new.next
                break
        
            new.next = l1
            l1 = l1.next
            new = new.next

            new.next = l2
            l2 = l2.next
            new = new.next

            
        
        return None



        