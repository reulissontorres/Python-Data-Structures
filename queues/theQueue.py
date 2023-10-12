from stacks.stackLL import Stack

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"Node[Data={self.data}]"


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        if self.size == 0:
            n = Node(data)
            self.front = n
            self.rear = n
            self.size += 1
        else:
            n = Node(data)

            if self.size == 1:
                self.front.next = n
                n.prev = self.front
            else:
                self.rear.next = n
                n.prev = self.rear
            self.rear = n
            self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError
        else:
            n = self.front.data
            self.front = self.front.next
            self.size -= 1
            return n

    def front(self):
        return self.front.data

    def rear(self):
        return self.rear.data

    def is_empty(self):
        return self.size <= 0

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        current = self.front
        queue_str = "Queue: "
        while current is not None:
            queue_str += str(current.data) + " "
            current = current.next
        return queue_str.strip()

    '''inverte uma fila usando uma pilha'''
    def reverse(self):
        stack = Stack()
        while not self.is_empty():
            stack.push(self.dequeue())
        while not stack.is_empty():
            self.enqueue(stack.pop())