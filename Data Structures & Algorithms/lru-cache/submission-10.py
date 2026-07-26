class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left = ListNode() #least recently used
        self.right = ListNode() #most recently used
        self.left.next = self.right 
        self.right.prev = self.left

    def add(self, node):
        prv = self.right.prev
        prv.next = node
        node.prev = prv
        node.next = self.right
        self.right.prev = node
        
    def remove(self, node):
        prv = node.prev 
        nxt = node.next 
        prv.next = nxt
        nxt.prev = prv

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.add(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        node = ListNode(key, value)
        self.hashmap[key] = node
        self.add(node)
        if len(self.hashmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]