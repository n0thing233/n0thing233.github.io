#trick: rememver move_to_start,delelte-node and insert_at_start.
#the implementation of LRU Cache is double-linked list + hashmap
#the key of hashmap is the key and the value of hashmap is the listnode (listnode also have the key and value)
class ListNode:
    def __init__(self,key = None, val = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    def _delete_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def _insert_at_start(self,node):
        self.start.next.prev = node
        node.next = self.start.next
        node.prev = self.start
        self.start.next = node      
    def _move_to_start(self,node):
        self._delete_node(node)
        self._insert_at_start(node)
    def __init__(self,capacity):
        self.start = ListNode("start")
        self.end = ListNode("end")
        self.start.next = self.end
        self.end.prev = self.start
        self.capacity = capacity
        self.node_count = 0
        self.map = {}
    def get(self, key: int) -> int:
        if key in self.map:
            self._move_to_start(self.map[key])
            return self.map[key].val         
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self._move_to_start(self.map[key])
        else:
            new_node = ListNode(key,value)
            self.map[key] = new_node
            self._insert_at_start(new_node)
            self.node_count += 1
            if self.node_count > self.capacity:
                del self.map[self.end.prev.key]
                self._delete_node(self.end.prev)
                self.node_count -= 1
