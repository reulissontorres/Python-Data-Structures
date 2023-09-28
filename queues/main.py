from theQueue import Queue

q = Queue()
q.enqueue('first')
q.enqueue('second')
q.enqueue('third')

print(q.__str__())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
