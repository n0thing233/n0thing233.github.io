# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#一定要bottom-up with O(1) space
#花了大概一个小时理解了具体bottom-up的implementation非常难。。
#基本思想还是size 1 size 2 size 4 .....但是如何处理各种 start end refrence is super messy
#因为这么复杂所以需要死记硬背几个function: merge , get_size, cut
#照着答案写出来了。。。。。。wtf
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
        def get_length(node):
            count = 0
            while node:
                node = node.next
                count += 1
            return count
        
        def cut(start,size):
            for i in range(size-1):
                if not start:
                    break
                start = start.next
            if not start:
                return None
            res = start.next
            start.next = None
            return res
        
        def merge(l1,l2,last_tail):
            cur = last_tail
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            while cur.next:
                cur = cur.next
            return cur
        dummy = ListNode(-1)
        dummy.next = head
        length = get_length(head)
        size = 1
        while size < length:
            last_tail = dummy
            start = last_tail.next
            while start:
                left = start
                right = cut(left,size)
                start = cut(right,size)
                last_tail = merge(left,right,last_tail)
            size = size * 2
        return dummy.next
