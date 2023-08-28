class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'Node[Data=%s]' %self.data

class DoublyLL:
    def __init__(self, head=None, tail=None):
        self.length = 0
        self.head = None
        self.tail = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = self.tail = Node(data) 
        else:
            newNode = Node(data)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

        current = self.head

    def insertAtGivenPosition(self, pos, data):
        if self.head is None or pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length:
            self.insertAtEnd(data)
        elif pos < self.length:
            curr = self.head
            count = 0
            while curr is not None and count < pos:
                curr = curr.next
                count += 1
            newNode = Node(data)
            newNode.next = curr
            newNode.prev = curr.prev
            curr.prev.next = newNode
            curr.prev = newNode
            self.length += 1

    def deleteFromBeginning(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1

    def deleteFromEnd(self):
        if self.head is None:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1

    def deleteAtPosition(self, pos):
        if self.head is None or pos < 0 or pos >= self.length:
            return
        if pos == 0:
            self.deleteFromBeginning()
        elif pos == self.length-1:
            self.deleteFromEnd()
        else:
            current = self.head
            count = 0
            while current is not None and count < pos:
                current = current.next
                count += 1
            current.prev.next = current.next
            current.next.prev = current.prev
            self.length -= 1
        
    def print(self):
        current = self.head
        while(current):
            print("%d,"%current.data)
            current = current.next