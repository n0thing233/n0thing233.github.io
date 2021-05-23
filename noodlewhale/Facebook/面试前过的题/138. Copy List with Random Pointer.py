"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#if random is none, then it does not have next edge case
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        dummy = Node(x = -1)
        dummy.next = head
        while head:
            tmp = head.next
            head.next = Node(head.val)
            head.next.next = tmp
            head = head.next.next
        
        #now add random pointer
        head = dummy.next
        while head:
            #edge case
            if head.random:
                head.next.random = head.random.next
            else:
                head.next.random = None
            head = head.next.next
        
        #now modify the next pointer of newly created nodes
        head = dummy.next.next
        while head and head.next:
            head.next = head.next.next
            head = head.next
        
        return dummy.next.next
            

        
            
