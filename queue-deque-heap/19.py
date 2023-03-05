class MaxHeap:
    def __init__(self, capacity=10**5):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    
    def getParentIndex(self, index):
        return (index - 1) // 2
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    def getRightChildIndex(self, index):
        return 2 * index + 2

    
    def hasParent(self, index):
        return (index - 1) // 2 >= 0
    def hasLeftChild(self, index):
        return 2 * index + 1 < self.size
    def hasRightChild(self, index):
        return 2 * index + 2 < self.size

    
    def parent(self, index):
        return self.storage[(index - 1) // 2]
    def leftChild(self, index):
        return self.storage[2 * index + 1]
    def rightChild(self, index):
        return self.storage[2 * index + 2]

    
    def isFull(self):
        return self.size == self.capacity
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = \
            self.storage[index2], self.storage[index1]
    

    def insert(self, data):
        if(self.isFull()):
            raise("Heap is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()


    def heapifyUp(self):
        index = self.size - 1
        while self.hasParent(index) and self.parent(index) < self.storage[index]:
            self.swap((index - 1) // 2, index)
            index = (index - 1) // 2
    

    def removeMax(self):
        if self.size == 0:
            raise("Empty Heap")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()
        return data
    

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            biggerChildIndex = 2 * index + 1
            if self.hasRightChild(index) and self.rightChild(index) > self.leftChild(index):
                biggerChildIndex = 2 * index + 2
            if self.storage[index] > self.storage[biggerChildIndex]:
                break
            else:
                self.swap(index, biggerChildIndex)
            index = biggerChildIndex
    

n = int(input())
heap = MaxHeap(n)
for i in range(n):
    s = list(map(int, input().split()))
    if s[0] == 0:
        heap.insert(s[1])
    else:
        print(heap.removeMax())

