class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.left = Node() #least recently used
        self.right = Node() #most recently used
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right 
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def remove(self, node):
        prev = node.prev 
        nxt = node.next 
        prev.next = nxt
        nxt.prev = prev
        
    def get(self, key: int) -> int:    
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        self.hashmap[key] = Node(key, value)
        self.insert(self.hashmap[key])
        if len(self.hashmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hashmap[lru.key]



        
        
