class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        temp = self.head

        for i in range(index):
            temp = temp.next
        
        return temp.val
        

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
        

    def addAtTail(self, val):
        if self.size == 0:
            self.addAtHead(val)
            return

        node = Node(val)
        temp = self.head

        while temp.next:
            temp = temp.next
        
        temp.next = node
        self.size += 1
        

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        
        elif index <= 0:
            self.addAtHead(val)
            return

        newNode = Node(val)
        temp = self.head

        for i in range(index - 1):
            temp = temp.next
        
        newNode.next = temp.next
        temp.next = newNode
        self.size += 1
        

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        elif index == 0:
            self.head = self.head.next
        
        else:
            temp = self.head

            for i in range(index - 1):
                temp = temp.next
        
            temp.next = temp.next.next
        self.size -= 1