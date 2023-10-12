class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newNode
        self.length += 1

    def insertAtGivenPosition(self, pos, data):
        if pos > self.length-1 or pos < 0:
            return None
        
        if pos == 0:
            self.insertAtBeginning(data)
        elif pos == self.length-1:
            self.insertAtEnd(data)
        else:
            newNode = Node()
            newNode.data = data
            count = 1
            current = self.head
            while count < pos:
                count += 1
                current = current.next
            newNode.next = current.next
            current.next = newNode
        self.length += 1

    def deleteFromBeginning(self):
        if self.length != 0:
            self.head = self.head.next
            self.length -= 1

    def deleteFromEnd(self):
        if self.length != 0:
            currentNode = self.head
            previousNode = self.head
            while currentNode.next != None:
                previousNode = currentNode
                currentNode = currentNode.next
            previousNode.next = None
            self.length -= 1

    def deleteAtPosition(self, pos):
        count = 0
        currentNode = self.head
        previousNode = self.head

        if pos > self.length-1 or pos < 0:
            return None
        
        while currentNode.next != None or count < pos:
            count += 1
            if count == pos:
                previousNode.next = currentNode.next
                self.length -= 1
                return
            else:
                previousNode.next = currentNode
                currentNode = currentNode.next

    def show(self):
        if self.length != 0:
            pos = 0
            current = self.head
            while current != None:
                print(f'Node {self.pos} has value {current.data}')
                pos += 1
                if pos == self.length: return
                current = current.next

    def getNodeAtPosition(self, index):
        if self.length != 0:
            current = self.head
            i = 0
            while (current != None) and (i < index):
                current = current.next
                i += 1
            return current
        else:
            return None

    def printLastN(self, n):
        slow = fast = self.head
        count = 0
        while count < n and fast:
            fast = fast.next
        count += 1
        while fast.next != None:
            slow = slow.next
        fast = fast.next
        return ("Node (m - %d) has value %s"%(n, slow.data))
    
    def printReverse(self, head):
        if head == None:
            return
        self.printReverse(head.next)
        print(head.data)
    
    def insertInOrder(self, k):
        if self.length == 0:
            self.insertAtBeginning(k)

        current = self.head
        while current.next != None:
            if current.next.data < k:
                break
        current = current.next

        newNode = Node(k)
        if current.next == None:
            current.next = newNode
        else:
            newNode.next = current.next
            current.next = newNode
