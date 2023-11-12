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
        parent = self.parent(j)
        if j > 0:  # se o j for menor que o pai, ele sobe na árvore
            if self.heapList[j] < self.heapList[parent]:
                self.swap(j, parent)
                self.upHeap(parent)

    '''def downHeap(self, j):
        if self.hasLeft(j):
            left = self.leftChild(j)
            small_child = left
            if self.hasRight(j):
                right = self.rightChild(j)
                if self.heapList[right] < self.heapList[left]:
                    small_child = right
            if self.heapList[small_child] < self.heapList[j]:
                self.swap(j, small_child)
                self.downHeap(small_child)'''

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


# Creating a heap
heap = Heap()

# Adding elements to the heap
heap.add(3, 'Three')
heap.add(1, 'One')
heap.add(4, 'Four')
heap.add(2, 'Two')

# Displaying the heap
print("Heap after adding elements:")
print(heap.heapList)

# Retrieving and removing the minimum element
#min_element = heap.removeMin()
#print("\nRemoved minimum element:", min_element)

# Displaying the heap after removal
print("\nHeap after removing minimum element:")
print(heap.heapList)

# Retrieving the minimum element without removing it
min_element = heap.min()
print("\nMinimum element without removal:", min_element)

# Displaying the heap after retrieval
print("\nHeap after retrieving minimum element without removal:")
print(heap.heapList)