def insertNodeAtTail(head, data):
    a = SinglyLinkedListNode(data)
    
    if head is None:
        return a
    curr = head
    
    while curr.next:
        curr = curr.next
    
    curr.next = a       
    return head