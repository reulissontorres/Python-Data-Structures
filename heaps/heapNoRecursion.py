class Item:
    def __init__(self, k, v):
        self.key = k
        self.value = v

    def isEmpty(self):
        return len(self) == 0

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return f"({self.key}, {self.value})"
    

#
# A min-oriented heap
#
class Heap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    #
    # Para um nó na i-ésima posição, seu pai está na posição floor((i-1)/2)
    #
    def parent(self, index):
        return (index - 1) // 2

    #
    # Para um nó na i-ésima posição, seus filhos são 2*i e 2*i+1
    #
    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def hasLeft(self, index):
        return (
            self.leftChild(index) < self.size
        )  # verifica se está além do tamanho do heap

    def hasRight(self, index):
        return (
            self.rightChild(index) < self.size
        )  # verifica se está além do tamanho do heap

    def swap(self, i, j):
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def upHeap(self, j):
        while j > 0:
            parent = self.parent(j)
            if self.heapList[j] < self.heapList[parent]:
                self.swap(j, parent)
                j = parent
            else:
                break

    def downHeap(self, j):
        while self.hasLeft(j):
            left = self.leftChild(j)
            small_child = left

            if self.hasRight(j):
                right = self.rightChild(j)
                if self.heapList[right] < self.heapList[left]:
                    small_child = right

            if self.heapList[small_child] < self.heapList[j]:
                self.swap(j, small_child)
                j = small_child
            else:
                break

    def add(self, key, value):
        self.heapList.append(Item(key, value))
        if self.size > 0:
            self.upHeap(len(self.heapList) - 1)
        self.size += 1

    def min(self):
        if self.size == 0:
            raise IndexError
        item = self.heapList[0]
        return (item.key, item.value)

    def removeMin(self):
        if self.size == 0:
            raise IndexError
        self.swap(0, len(self.heapList) - 1)
        item = self.heapList.pop()
        self.downHeap(0)
        return (item.key, item.value)


# Create a heap
heap = Heap()

# Add elements to the heap
heap.add(4, 'four')
heap.add(2, 'two')
heap.add(7, 'seven')
heap.add(1, 'one')
heap.add(5, 'five')

# Test min operation
min_element = heap.min()
print("Minimum element:", min_element)

# Test removeMin operation
# removed_element = heap.removeMin()
# print("Removed minimum element:", removed_element)

# Print the updated heap
print("Updated heap:")
while heap.size > 0:
    print(heap.removeMin())

