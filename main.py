from queues.theQueue import Queue
from linkedLIst.doublyList import DoublyLL

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.__str__())

q.reverse()
print(q.__str__())
