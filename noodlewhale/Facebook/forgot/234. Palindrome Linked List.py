# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#reverse second half...
#指导思路但没信息写对，所以还是写一下,考点：
#1.快慢指针从dummy开始更简单而不是从head
#2.这种解法的edge case是只有一个元素，但可以在reverse function里handle这个edge case

#. d- > 1 - > 2 - > 3
#. d -> 2 - > 1 - > 3
#  d -> 3 - > 2 - > 1
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(node):
            d = ListNode()
            d.next = node
            while node and node.next:
                tmp = node.next.next
                tmp1 = node.next
                node.next = tmp
                tmp1.next = d.next
                d.next = tmp1
            return d.next
        
        if not head:
            return False
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        a = slow.next
        slow.next = None
        a = reverse(a)
        b = dummy.next
        while a:
            if a.val != b.val:
                return False
            a = a.next
            b = b.next
        return True
