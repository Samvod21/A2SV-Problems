class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash = {}

        self.recent, self.old = DoublyLinkedList(0, 0), DoublyLinkedList(0, 0)
        self.old.next = self.recent
        self.recent.prev = self.old
    
    def insertNode(self, node):
        prev = self.recent.prev
        next = self.recent
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
    
    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        

    def get(self, key):
        if key in self.hash:
            self.deleteNode(self.hash[key])
            self.insertNode(self.hash[key])
            return self.hash[key].val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.hash:
            self.deleteNode(self.hash[key])

        self.hash[key] = DoublyLinkedList(key, value)
        self.insertNode(self.hash[key])

        if len(self.hash) > self.capacity:
            leastrecent = self.old.next
            self.deleteNode(leastrecent)
            del self.hash[leastrecent.key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)